from __future__ import annotations

import random as _py_random
from dataclasses import dataclass
from typing import Any

from psyflow.sim.contracts import Action, Feedback, Observation, SessionInfo


@dataclass
class TaskSamplerResponder:
    """Task-specific simulation responder for Raven-style matrix reasoning."""

    key: str | None = None
    hit_rate: float = 0.82
    timeout_rate: float = 0.08
    rt_mean_s: float = 1.75
    rt_sd_s: float = 0.45
    rt_min_s: float = 0.35
    practice_bonus: float = 0.08
    complexity_penalty: float = 0.05
    complexity_rt_step: float = 0.18

    def __post_init__(self) -> None:
        self._rng: Any = None
        self.hit_rate = max(0.0, min(1.0, float(self.hit_rate)))
        self.timeout_rate = max(0.0, min(1.0, float(self.timeout_rate)))
        self.rt_mean_s = float(self.rt_mean_s)
        self.rt_sd_s = max(1e-6, float(self.rt_sd_s))
        self.rt_min_s = max(0.0, float(self.rt_min_s))
        self.practice_bonus = float(self.practice_bonus)
        self.complexity_penalty = float(self.complexity_penalty)
        self.complexity_rt_step = float(self.complexity_rt_step)

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def on_feedback(self, fb: Feedback) -> None:
        return None

    def end_session(self) -> None:
        self._rng = None

    def _sample_normal(self, mean: float, sd: float) -> float:
        rng = self._rng
        if hasattr(rng, "normal"):
            return float(rng.normal(mean, sd))
        return float(rng.gauss(mean, sd))

    def _sample_random(self) -> float:
        rng = self._rng
        if hasattr(rng, "random"):
            return float(rng.random())
        return float(_py_random.random())

    def _pick_valid_key(self, valid_keys: list[str], correct_key: str | None) -> str | None:
        if correct_key and correct_key in valid_keys:
            return correct_key
        if self.key and self.key in valid_keys:
            return self.key
        return valid_keys[0] if valid_keys else None

    def _profile(self, obs: Observation) -> dict[str, Any]:
        task_factors = dict(getattr(obs, "task_factors", {}) or {})
        if not task_factors and isinstance(getattr(obs, "extras", None), dict):
            task_factors = dict(obs.extras.get("task_factors", {}) or {})

        category = str(task_factors.get("category", "scored"))
        practice = bool(task_factors.get("practice", category == "practice"))
        complexity_map = {"practice": 0, "easy": 1, "medium": 2, "hard": 3}
        complexity = int(task_factors.get("complexity", complexity_map.get(category, 1 if not practice else 0)))
        complexity = max(0, complexity)

        effective_hit_rate = self.hit_rate + (self.practice_bonus if practice else 0.0) - (self.complexity_penalty * complexity)
        effective_timeout_rate = self.timeout_rate + (0.015 * complexity) - (0.02 if practice else 0.0)
        effective_rt_mean = self.rt_mean_s + (self.complexity_rt_step * complexity) - (0.25 if practice else 0.0)

        return {
            "task_factors": task_factors,
            "category": category,
            "practice": practice,
            "complexity": complexity,
            "hit_rate": max(0.0, min(1.0, effective_hit_rate)),
            "timeout_rate": max(0.0, min(1.0, effective_timeout_rate)),
            "rt_mean_s": max(self.rt_min_s, effective_rt_mean),
        }

    def act(self, obs: Observation) -> Action:
        valid_keys = [str(key) for key in list(obs.valid_keys or [])]
        if not valid_keys:
            return Action(key=None, rt_s=None, meta={"source": "task_sampler", "reason": "no_valid_keys"})

        rng = self._rng
        if rng is None:
            return Action(key=None, rt_s=None, meta={"source": "task_sampler", "reason": "rng_missing"})

        profile = self._profile(obs)
        task_factors = profile["task_factors"]
        correct_key = task_factors.get("correct_key") or getattr(obs, "correct_key", None)
        correct_key = str(correct_key) if correct_key is not None else None

        if self._sample_random() < profile["timeout_rate"]:
            return Action(
                key=None,
                rt_s=None,
                meta={
                    "source": "task_sampler",
                    "outcome": "timeout",
                    "correct_key": correct_key,
                    "category": profile["category"],
                },
            )

        rt = max(self.rt_min_s, self._sample_normal(profile["rt_mean_s"], self.rt_sd_s))

        if self._sample_random() > profile["hit_rate"]:
            wrong_keys = [key for key in valid_keys if key != correct_key]
            chosen_key = wrong_keys[0] if wrong_keys else self._pick_valid_key(valid_keys, correct_key)
            return Action(
                key=chosen_key,
                rt_s=rt,
                meta={
                    "source": "task_sampler",
                    "outcome": "miss",
                    "correct_key": correct_key,
                    "category": profile["category"],
                },
            )

        chosen_key = self._pick_valid_key(valid_keys, correct_key)
        return Action(
            key=chosen_key,
            rt_s=rt,
            meta={
                "source": "task_sampler",
                "outcome": "hit",
                "correct_key": correct_key,
                "category": profile["category"],
            },
        )
