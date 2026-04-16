from __future__ import annotations

from functools import partial
from typing import Any

from psyflow import StimUnit, next_trial_id, set_trial_context

from .utils import OPTION_KEY_ORDER, build_matrix_scene, get_trial_spec


def _parse_condition(condition: Any) -> str:
    if isinstance(condition, dict):
        return str(condition.get("condition", condition.get("condition_label", "practice_01")))
    if isinstance(condition, tuple) and condition:
        return str(condition[0])
    return str(condition)


def _selected_label(display_items: list[dict[str, Any]], response_key: str) -> str:
    for item in display_items:
        if str(item.get("key", "")) == str(response_key):
            return str(item.get("position_label", ""))
    return ""


def _duration(settings: Any, name: str, fallback: float) -> float:
    timing = dict(getattr(settings, "timing", {}) or {})
    value = timing.get(name, fallback)
    try:
        duration = float(value)
        if name in {"response_open_duration", "response_warning_duration"} and duration > 100.0:
            return duration / 1000.0
        return duration
    except Exception:
        return float(fallback)


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    trigger_runtime,
    block_id=None,
    block_idx=None,
):
    """Run one Raven-style matrix reasoning trial."""
    trial_id = int(next_trial_id())
    condition_label = _parse_condition(condition)
    block_id_val = str(block_id) if block_id is not None else "block_0"
    block_idx_val = int(block_idx) if block_idx is not None else 0

    trial_spec = get_trial_spec(settings, condition_label)
    fixation_duration = _duration(settings, "fixation_duration", 0.5)
    blank_duration = _duration(settings, "blank_duration", 0.1)
    response_open_duration = _duration(settings, "response_open_duration", 25000.0)
    response_warning_duration = _duration(settings, "response_warning_duration", 5000.0)
    feedback_duration = _duration(settings, "feedback_duration", 0.8)
    iti_duration = _duration(settings, "iti_duration", 0.6)

    response_keys = [str(key) for key in list(getattr(settings, "response_keys", list(OPTION_KEY_ORDER)))]
    if not response_keys:
        response_keys = list(OPTION_KEY_ORDER)

    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    scene_open = build_matrix_scene(
        win=win,
        settings=settings,
        trial_id=trial_id,
        block_idx=block_idx_val,
        trial_spec=trial_spec,
        show_numbers=True,
        show_clock_warning=False,
    )
    scene_warning = build_matrix_scene(
        win=win,
        settings=settings,
        trial_id=trial_id,
        block_idx=block_idx_val,
        trial_spec=trial_spec,
        show_numbers=True,
        show_clock_warning=True,
    )

    scene_open_stimuli = list(scene_open["stimuli"])
    scene_open_stimuli.append(stim_bank.get("response_prompt"))
    scene_warning_stimuli = list(scene_warning["stimuli"])
    scene_warning_stimuli.append(stim_bank.get("response_prompt"))
    scene_warning_stimuli.append(stim_bank.get("clock_warning"))

    correct_key = str(scene_open["correct_key"])
    if correct_key not in response_keys:
        raise ValueError(
            f"Target key {correct_key!r} is not included in response keys {response_keys!r} "
            f"for condition {condition_label!r}."
        )

    trial_data: dict[str, Any] = {
        "trial_id": trial_id,
        "block_id": block_id_val,
        "block_idx": block_idx_val,
        "condition": condition_label,
        "condition_id": f"{condition_label}_{block_idx_val}_{trial_id}",
        "practice": bool(scene_open["practice"]),
        "category": str(scene_open["category"]),
        "template": str(scene_open["template"]),
        "correct_key": correct_key,
        "correct_position": str(scene_open["correct_position"]),
        "correct_label": str(scene_open["correct_label"]),
    }

    fixation_unit = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        fixation_unit,
        trial_id=trial_id,
        phase="fixation",
        deadline_s=fixation_duration,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "fixation",
            "condition": condition_label,
            "practice": trial_data["practice"],
            "category": trial_data["category"],
            "block_idx": block_idx_val,
        },
        stim_id="fixation",
    )
    fixation_unit.show(
        duration=fixation_duration,
        onset_trigger=settings.triggers.get("fixation_onset"),
    ).to_dict(trial_data)

    blank_unit = make_unit(unit_label="blank_screen").add_stim(stim_bank.get("blank_screen"))
    set_trial_context(
        blank_unit,
        trial_id=trial_id,
        phase="blank_screen",
        deadline_s=blank_duration,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "blank_screen",
            "condition": condition_label,
            "practice": trial_data["practice"],
            "category": trial_data["category"],
            "block_idx": block_idx_val,
        },
        stim_id="blank_screen",
    )
    blank_unit.show(
        duration=blank_duration,
        onset_trigger=settings.triggers.get("blank_onset"),
    ).to_dict(trial_data)

    matrix_open_unit = make_unit(unit_label="matrix_response_open").add_stim(scene_open_stimuli)
    set_trial_context(
        matrix_open_unit,
        trial_id=trial_id,
        phase="matrix_response_open",
        deadline_s=response_open_duration,
        valid_keys=response_keys,
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "matrix_response_open",
            "condition": condition_label,
            "practice": trial_data["practice"],
            "category": trial_data["category"],
            "template": trial_data["template"],
            "correct_key": correct_key,
            "correct_position": trial_data["correct_position"],
            "block_idx": block_idx_val,
        },
        stim_id="matrix_and_options",
    )
    matrix_open_unit.capture_response(
        keys=response_keys,
        correct_keys=[correct_key],
        duration=response_open_duration,
        onset_trigger=settings.triggers.get("matrix_response_open_onset"),
        response_trigger={key: settings.triggers.get(f"response_{key}") for key in response_keys},
        timeout_trigger=settings.triggers.get("response_timeout"),
    ).to_dict(trial_data)

    open_response = matrix_open_unit.get_state("response", None)
    open_rt = matrix_open_unit.get_state("rt", None)
    response_key = str(open_response) if open_response is not None else ""
    response_rt: float | None
    response_phase = "open"

    if open_response is None:
        matrix_warning_unit = make_unit(unit_label="matrix_response_warning").add_stim(scene_warning_stimuli)
        set_trial_context(
            matrix_warning_unit,
            trial_id=trial_id,
            phase="matrix_response_warning",
            deadline_s=response_warning_duration,
            valid_keys=response_keys,
            block_id=block_id_val,
            condition_id=trial_data["condition_id"],
            task_factors={
                "stage": "matrix_response_warning",
                "condition": condition_label,
                "practice": trial_data["practice"],
                "category": trial_data["category"],
                "template": trial_data["template"],
                "correct_key": correct_key,
                "correct_position": trial_data["correct_position"],
                "block_idx": block_idx_val,
                "time_remaining_s": response_warning_duration,
            },
            stim_id="matrix_and_options+clock_warning",
        )
        matrix_warning_unit.capture_response(
            keys=response_keys,
            correct_keys=[correct_key],
            duration=response_warning_duration,
            onset_trigger=settings.triggers.get("matrix_response_warning_onset"),
            response_trigger={key: settings.triggers.get(f"response_{key}") for key in response_keys},
            timeout_trigger=settings.triggers.get("response_timeout"),
        ).to_dict(trial_data)

        warning_response = matrix_warning_unit.get_state("response", None)
        warning_rt = matrix_warning_unit.get_state("rt", None)
        if warning_response is not None:
            response_key = str(warning_response)
            response_phase = "warning"
            response_rt = response_open_duration + float(warning_rt or 0.0)
        else:
            response_rt = None
            response_phase = "timeout"
    else:
        response_rt = float(open_rt) if isinstance(open_rt, (int, float)) else None

    selected_label = _selected_label(scene_open["options"], response_key) if response_key else ""
    response_correct = bool(response_key and response_key == correct_key)
    timed_out = response_key == ""

    trial_data.update(
        {
            "responded": bool(response_key),
            "response_key": response_key,
            "selected_label": selected_label,
            "response_phase": response_phase,
            "response_rt": response_rt,
            "response_correct": response_correct,
            "timed_out": timed_out,
        }
    )

    if trial_data["practice"]:
        if timed_out:
            feedback_stim = stim_bank.get_and_format(
                "practice_feedback_timeout",
                correct_label=trial_data["correct_label"],
                correct_key=trial_data["correct_key"],
                selected_label=selected_label,
                response_key=response_key,
            )
            feedback_name = "practice_feedback_timeout"
        elif response_correct:
            feedback_stim = stim_bank.get_and_format(
                "practice_feedback_correct",
                correct_label=trial_data["correct_label"],
                correct_key=trial_data["correct_key"],
                selected_label=selected_label,
                response_key=response_key,
            )
            feedback_name = "practice_feedback_correct"
        else:
            feedback_stim = stim_bank.get_and_format(
                "practice_feedback_incorrect",
                correct_label=trial_data["correct_label"],
                correct_key=trial_data["correct_key"],
                selected_label=selected_label,
                response_key=response_key,
            )
            feedback_name = "practice_feedback_incorrect"

        feedback_unit = make_unit(unit_label="practice_feedback").add_stim(feedback_stim)
        set_trial_context(
            feedback_unit,
            trial_id=trial_id,
            phase="practice_feedback",
            deadline_s=feedback_duration,
            valid_keys=[],
            block_id=block_id_val,
            condition_id=trial_data["condition_id"],
            task_factors={
                "stage": "practice_feedback",
                "condition": condition_label,
                "practice": True,
                "category": trial_data["category"],
                "feedback_name": feedback_name,
                "response_key": response_key,
                "correct_key": trial_data["correct_key"],
                "block_idx": block_idx_val,
            },
            stim_id=feedback_name,
        )
        feedback_unit.show(
            duration=feedback_duration,
            onset_trigger=settings.triggers.get("practice_feedback_onset"),
        ).to_dict(trial_data)

    iti_unit = make_unit(unit_label="iti").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        iti_unit,
        trial_id=trial_id,
        phase="iti",
        deadline_s=iti_duration,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "iti",
            "condition": condition_label,
            "practice": trial_data["practice"],
            "category": trial_data["category"],
            "block_idx": block_idx_val,
        },
        stim_id="fixation",
    )
    iti_unit.show(
        duration=iti_duration,
        onset_trigger=settings.triggers.get("iti_onset"),
    ).to_dict(trial_data)

    return trial_data
