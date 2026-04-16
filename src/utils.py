from __future__ import annotations

import random
from typing import Any, Iterable

from psychopy import logging
from psychopy.visual import Circle, Polygon, Rect, TextStim

OPTION_KEY_ORDER = ("1", "2", "3", "4")
OPTION_POSITION_ORDER = ("top_left", "top_right", "bottom_left", "bottom_right")

DEFAULT_OPTION_KEY_MAP = {
    "top_left": "1",
    "top_right": "2",
    "bottom_left": "3",
    "bottom_right": "4",
}

DEFAULT_MATRIX_POSITIONS = {
    "top_left": (-132.0, 180.0),
    "top_center": (0.0, 180.0),
    "top_right": (132.0, 180.0),
    "middle_left": (-132.0, 68.0),
    "middle_center": (0.0, 68.0),
    "middle_right": (132.0, 68.0),
    "bottom_left": (-132.0, -44.0),
    "bottom_center": (0.0, -44.0),
    "bottom_right": (132.0, -44.0),
}

DEFAULT_OPTION_POSITIONS = {
    "top_left": (-180.0, -190.0),
    "top_right": (180.0, -190.0),
    "bottom_left": (-180.0, -310.0),
    "bottom_right": (180.0, -310.0),
}

DEFAULT_MATRIX_PANEL_SIZE = 88.0
DEFAULT_OPTION_PANEL_SIZE = (132.0, 92.0)

DEFAULT_TRIAL_BANK: dict[str, dict[str, Any]] = {
    "practice_01": {
        "practice": True,
        "category": "practice",
        "template": "shape_cols_count_rows",
        "shape_cycle": ["square", "triangle", "diamond"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.24,
    },
    "practice_02": {
        "practice": True,
        "category": "practice",
        "template": "shape_rows_count_cols",
        "shape_cycle": ["triangle", "diamond", "square"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.24,
    },
    "practice_03": {
        "practice": True,
        "category": "practice",
        "template": "shape_cols_count_rows_rotation_phase",
        "shape_cycle": ["diamond", "square", "triangle"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.235,
    },
    "easy_01": {
        "practice": False,
        "category": "easy",
        "template": "shape_cols_count_rows",
        "shape_cycle": ["square", "triangle", "diamond"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 45.0, 90.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.235,
    },
    "easy_02": {
        "practice": False,
        "category": "easy",
        "template": "shape_rows_count_cols",
        "shape_cycle": ["triangle", "square", "diamond"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 45.0, 90.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.235,
    },
    "easy_03": {
        "practice": False,
        "category": "easy",
        "template": "shape_cols_count_rows",
        "shape_cycle": ["diamond", "triangle", "square"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 45.0, 90.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.235,
    },
    "easy_04": {
        "practice": False,
        "category": "easy",
        "template": "shape_rows_count_cols",
        "shape_cycle": ["square", "diamond", "triangle"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 45.0, 90.0],
        "symbol_layout": "horizontal",
        "symbol_size_scale": 0.235,
    },
    "medium_01": {
        "practice": False,
        "category": "medium",
        "template": "shape_cols_count_rows_rotation_phase",
        "shape_cycle": ["square", "diamond", "triangle"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "vertical",
        "symbol_size_scale": 0.225,
    },
    "medium_02": {
        "practice": False,
        "category": "medium",
        "template": "shape_rows_count_cols_rotation_phase",
        "shape_cycle": ["triangle", "square", "diamond"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "vertical",
        "symbol_size_scale": 0.225,
    },
    "medium_03": {
        "practice": False,
        "category": "medium",
        "template": "shape_cols_count_rows_rotation_phase",
        "shape_cycle": ["diamond", "triangle", "square"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "vertical",
        "symbol_size_scale": 0.225,
    },
    "medium_04": {
        "practice": False,
        "category": "medium",
        "template": "shape_rows_count_cols_rotation",
        "shape_cycle": ["square", "triangle", "diamond"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "vertical",
        "symbol_size_scale": 0.225,
    },
    "hard_01": {
        "practice": False,
        "category": "hard",
        "template": "shape_cols_count_rows_rotation_phase",
        "shape_cycle": ["diamond", "square", "triangle"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "triad",
        "symbol_size_scale": 0.21,
    },
    "hard_02": {
        "practice": False,
        "category": "hard",
        "template": "shape_rows_count_cols_rotation_phase",
        "shape_cycle": ["triangle", "diamond", "square"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "triad",
        "symbol_size_scale": 0.21,
    },
    "hard_03": {
        "practice": False,
        "category": "hard",
        "template": "shape_cols_count_rows_rotation_phase",
        "shape_cycle": ["square", "triangle", "diamond"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "triad",
        "symbol_size_scale": 0.21,
    },
    "hard_04": {
        "practice": False,
        "category": "hard",
        "template": "shape_rows_count_cols_rotation_phase",
        "shape_cycle": ["diamond", "triangle", "square"],
        "count_cycle": [1, 2, 3],
        "rotation_cycle": [0.0, 30.0, 60.0],
        "symbol_layout": "triad",
        "symbol_size_scale": 0.21,
    },
}


def _coerce_position(value: Any, fallback: tuple[float, float]) -> tuple[float, float]:
    if isinstance(value, (list, tuple)) and len(value) >= 2:
        try:
            return float(value[0]), float(value[1])
        except Exception:
            return fallback
    return fallback


def _coerce_size(value: Any, fallback: tuple[float, float]) -> tuple[float, float]:
    if isinstance(value, (list, tuple)) and len(value) >= 2:
        try:
            return float(value[0]), float(value[1])
        except Exception:
            return fallback
    if isinstance(value, (int, float)):
        size = float(value)
        return size, size
    return fallback


def _coerce_sequence(value: Any, default: Iterable[Any]) -> list[Any]:
    if isinstance(value, (list, tuple)):
        items = list(value)
        if items:
            return items
    return list(default)


def _trial_rng(*, overall_seed: int, block_idx: int, trial_id: int, condition_label: str) -> random.Random:
    condition_hash = sum(ord(ch) for ch in str(condition_label))
    mixed_seed = (
        (int(overall_seed) * 1_000_003)
        + ((int(block_idx) + 1) * 1_009)
        + (int(trial_id) * 97)
        + condition_hash
    ) % (2**32)
    return random.Random(mixed_seed)


def get_trial_spec(settings: Any, condition_label: str) -> dict[str, Any]:
    trial_bank = dict(getattr(settings, "trial_bank", {}) or {})
    if not trial_bank and isinstance(getattr(settings, "item_bank", None), dict):
        trial_bank = dict(getattr(settings, "item_bank", {}) or {})
    if not trial_bank:
        trial_bank = dict(DEFAULT_TRIAL_BANK)

    label = str(condition_label)
    if label not in trial_bank:
        raise KeyError(f"Unknown Raven trial label: {label!r}")

    spec = dict(trial_bank[label])
    spec["condition_label"] = label
    spec["practice"] = bool(spec.get("practice", False))
    spec["category"] = str(spec.get("category", "practice" if spec["practice"] else "scored"))
    spec["template"] = str(spec.get("template", "shape_cols_count_rows_rotation"))
    spec["shape_cycle"] = [str(item) for item in _coerce_sequence(spec.get("shape_cycle"), ("square", "triangle", "diamond"))]
    spec["count_cycle"] = [int(item) for item in _coerce_sequence(spec.get("count_cycle"), (1, 2, 3))]
    spec["rotation_cycle"] = [float(item) for item in _coerce_sequence(spec.get("rotation_cycle"), (0.0, 30.0, 60.0))]
    spec["symbol_layout"] = str(spec.get("symbol_layout", "horizontal"))
    spec["symbol_color"] = str(spec.get("symbol_color", "#111111"))
    spec["panel_fill_color"] = str(spec.get("panel_fill_color", "#F6F6F6"))
    spec["panel_line_color"] = str(spec.get("panel_line_color", "#111111"))
    spec["panel_line_width"] = float(spec.get("panel_line_width", 2.0))
    spec["symbol_size_scale"] = float(spec.get("symbol_size_scale", 0.24))
    spec["symbol_line_width"] = float(spec.get("symbol_line_width", 2.0))
    return spec


def _feature_index(template: str, row: int, col: int) -> tuple[int, int, int]:
    if template == "shape_cols_count_fixed":
        return col, 0, 0
    if template == "shape_rows_count_fixed":
        return row, 0, 0
    if template == "shape_rows_count_cols":
        return row, col, 0
    if template == "shape_cols_count_rows":
        return col, row, 0
    if template == "shape_rows_count_cols_rotation":
        return row, col, row + col
    if template == "shape_cols_count_rows_rotation_phase":
        return col, row, (2 * row) + col
    if template == "shape_rows_count_cols_rotation_phase":
        return row, col, (2 * row) + col
    return col, row, row + col


def _resolve_feature(spec: dict[str, Any], row: int, col: int) -> dict[str, Any]:
    shape_idx, count_idx, rotation_idx = _feature_index(str(spec.get("template", "")), row, col)
    shape_cycle = list(spec["shape_cycle"])
    count_cycle = list(spec["count_cycle"])
    rotation_cycle = list(spec["rotation_cycle"])
    shape = str(shape_cycle[shape_idx % len(shape_cycle)])
    count = int(count_cycle[count_idx % len(count_cycle)])
    rotation = float(rotation_cycle[rotation_idx % len(rotation_cycle)])
    return {
        "shape": shape,
        "count": count,
        "rotation": rotation,
        "layout": str(spec["symbol_layout"]),
    }


def _feature_signature(feature: dict[str, Any]) -> tuple[Any, ...]:
    return (
        str(feature.get("shape", "")),
        int(feature.get("count", 0)),
        round(float(feature.get("rotation", 0.0)), 4),
        str(feature.get("layout", "")),
    )


def _advance_unique(
    base_feature: dict[str, Any],
    *,
    shape_cycle: list[str],
    count_cycle: list[int],
    rotation_cycle: list[float],
    shape_step: int = 0,
    count_step: int = 0,
    rotation_step: int = 0,
    force_rotation_visible: bool = False,
) -> dict[str, Any]:
    shape = str(base_feature["shape"])
    count = int(base_feature["count"])
    rotation = float(base_feature["rotation"])
    layout = str(base_feature.get("layout", "horizontal"))

    if shape_step:
        shape_idx = shape_cycle.index(shape) if shape in shape_cycle else 0
        shape = str(shape_cycle[(shape_idx + shape_step) % len(shape_cycle)])

    if count_step:
        count_idx = count_cycle.index(count) if count in count_cycle else 0
        count = int(count_cycle[(count_idx + count_step) % len(count_cycle)])

    if rotation_step:
        rotation_idx = 0
        for idx, candidate in enumerate(rotation_cycle):
            if round(float(candidate), 4) == round(rotation, 4):
                rotation_idx = idx
                break
        rotation = float(rotation_cycle[(rotation_idx + rotation_step) % len(rotation_cycle)])

    if force_rotation_visible and shape == "circle":
        shape_idx = shape_cycle.index(shape) if shape in shape_cycle else 0
        shape = str(shape_cycle[(shape_idx + 1) % len(shape_cycle)])

    return {"shape": shape, "count": count, "rotation": rotation, "layout": layout}


def _option_variants(
    correct_feature: dict[str, Any],
    *,
    shape_cycle: list[str],
    count_cycle: list[int],
    rotation_cycle: list[float],
) -> list[dict[str, Any]]:
    shape_variant = _advance_unique(correct_feature, shape_cycle=shape_cycle, count_cycle=count_cycle, rotation_cycle=rotation_cycle, shape_step=1)
    count_variant = _advance_unique(correct_feature, shape_cycle=shape_cycle, count_cycle=count_cycle, rotation_cycle=rotation_cycle, count_step=1)
    rotation_variant = _advance_unique(
        correct_feature,
        shape_cycle=shape_cycle,
        count_cycle=count_cycle,
        rotation_cycle=rotation_cycle,
        rotation_step=1,
        force_rotation_visible=True,
    )

    variants = [shape_variant, count_variant, rotation_variant]
    unique_variants: list[dict[str, Any]] = []
    seen = {_feature_signature(correct_feature)}
    for variant in variants:
        sig = _feature_signature(variant)
        if sig in seen:
            # Fall back to a more visible change if the first pass duplicated the correct answer.
            variant = _advance_unique(
                variant,
                shape_cycle=shape_cycle,
                count_cycle=count_cycle,
                rotation_cycle=rotation_cycle,
                shape_step=1,
                count_step=1,
                rotation_step=1,
                force_rotation_visible=True,
            )
            sig = _feature_signature(variant)
        if sig in seen:
            continue
        unique_variants.append(variant)
        seen.add(sig)

    while len(unique_variants) < 3:
        unique_variants.append(
            _advance_unique(
                correct_feature,
                shape_cycle=shape_cycle,
                count_cycle=count_cycle,
                rotation_cycle=rotation_cycle,
                shape_step=len(unique_variants) + 1,
                count_step=1,
                rotation_step=1,
                force_rotation_visible=True,
            )
        )
    return unique_variants[:3]


def _symbol_positions(count: int, layout: str, spread: float) -> list[tuple[float, float]]:
    count = max(1, int(count))
    if count == 1:
        return [(0.0, 0.0)]

    if layout == "vertical":
        if count == 2:
            return [(0.0, spread / 2.0), (0.0, -spread / 2.0)]
        if count == 3:
            return [(0.0, spread), (0.0, 0.0), (0.0, -spread)]

    if layout == "triad" and count >= 3:
        return [(0.0, spread * 0.85), (-spread * 0.8, -spread * 0.55), (spread * 0.8, -spread * 0.55)]

    if count == 2:
        return [(-spread / 2.0, 0.0), (spread / 2.0, 0.0)]
    if count == 3:
        return [(-spread, 0.0), (0.0, 0.0), (spread, 0.0)]

    positions: list[tuple[float, float]] = []
    for idx in range(count):
        x = (idx - (count - 1) / 2.0) * spread
        positions.append((x, 0.0))
    return positions


def _build_symbol(
    *,
    win,
    center: tuple[float, float],
    shape: str,
    rotation: float,
    size: float,
    color: str,
    line_width: float,
) -> Any:
    x, y = center
    if shape == "square":
        return Rect(
            win=win,
            pos=(x, y),
            width=size,
            height=size,
            ori=rotation,
            fillColor=color,
            lineColor=color,
            lineWidth=line_width,
        )
    if shape == "diamond":
        return Rect(
            win=win,
            pos=(x, y),
            width=size,
            height=size,
            ori=rotation + 45.0,
            fillColor=color,
            lineColor=color,
            lineWidth=line_width,
        )
    if shape == "triangle":
        return Polygon(
            win=win,
            pos=(x, y),
            edges=3,
            radius=size * 0.55,
            ori=rotation,
            fillColor=color,
            lineColor=color,
            lineWidth=line_width,
        )
    if shape == "pentagon":
        return Polygon(
            win=win,
            pos=(x, y),
            edges=5,
            radius=size * 0.55,
            ori=rotation,
            fillColor=color,
            lineColor=color,
            lineWidth=line_width,
        )
    return Circle(
        win=win,
        pos=(x, y),
        radius=size * 0.35,
        fillColor=color,
        lineColor=color,
        lineWidth=line_width,
    )


def _build_symbol_cluster(
    *,
    win,
    center: tuple[float, float],
    feature: dict[str, Any],
    symbol_size: float,
    symbol_color: str,
    line_width: float,
) -> list[Any]:
    layout = str(feature.get("layout", "horizontal"))
    count = int(feature.get("count", 1))
    rotation = float(feature.get("rotation", 0.0))
    shape = str(feature.get("shape", "square"))
    spread = float(symbol_size) * 0.75
    offsets = _symbol_positions(count, layout, spread)
    stimuli: list[Any] = []
    for dx, dy in offsets:
        stimuli.append(
            _build_symbol(
                win=win,
                center=(center[0] + dx, center[1] + dy),
                shape=shape,
                rotation=rotation,
                size=symbol_size,
                color=symbol_color,
                line_width=line_width,
            )
        )
    return stimuli


def _build_panel(
    *,
    win,
    pos: tuple[float, float],
    size: tuple[float, float],
    fill_color: str,
    line_color: str,
    line_width: float,
) -> Rect:
    return Rect(
        win=win,
        pos=pos,
        width=size[0],
        height=size[1],
        fillColor=fill_color,
        lineColor=line_color,
        lineWidth=line_width,
    )


def build_matrix_scene(
    *,
    win,
    settings: Any,
    trial_id: int,
    block_idx: int,
    trial_spec: dict[str, Any],
    show_numbers: bool,
    show_clock_warning: bool = False,
) -> dict[str, Any]:
    """Build the 3x3 matrix and the four answer cards for a Raven-style item."""
    layout = dict(getattr(settings, "layout", {}) or {})
    rng = _trial_rng(
        overall_seed=int(getattr(settings, "overall_seed", 2026)),
        block_idx=int(block_idx),
        trial_id=int(trial_id),
        condition_label=str(trial_spec.get("condition_label", "")),
    )

    option_key_map = dict(getattr(settings, "option_key_map", {}) or {})
    if not option_key_map and isinstance(layout.get("option_key_map"), dict):
        option_key_map = dict(layout.get("option_key_map", {}) or {})
    if not option_key_map:
        option_key_map = dict(DEFAULT_OPTION_KEY_MAP)
    for position, default_key in DEFAULT_OPTION_KEY_MAP.items():
        option_key_map.setdefault(position, default_key)

    matrix_positions_cfg = dict(layout.get("matrix_positions_px", {}) or {})
    option_positions_cfg = dict(layout.get("option_positions_px", {}) or {})
    matrix_panel_size = _coerce_size(layout.get("matrix_panel_size_px", DEFAULT_MATRIX_PANEL_SIZE), (DEFAULT_MATRIX_PANEL_SIZE, DEFAULT_MATRIX_PANEL_SIZE))
    option_panel_size = _coerce_size(layout.get("option_panel_size_px", DEFAULT_OPTION_PANEL_SIZE), DEFAULT_OPTION_PANEL_SIZE)
    symbol_size_scale = float(layout.get("symbol_size_scale", trial_spec.get("symbol_size_scale", 0.24)))
    panel_fill_color = str(layout.get("panel_fill_color", trial_spec.get("panel_fill_color", "#F6F6F6")))
    panel_line_color = str(layout.get("panel_line_color", trial_spec.get("panel_line_color", "#111111")))
    panel_line_width = float(layout.get("panel_line_width", trial_spec.get("panel_line_width", 2.0)))
    option_fill_color = str(layout.get("option_fill_color", panel_fill_color))
    option_line_color = str(layout.get("option_line_color", panel_line_color))
    option_line_width = float(layout.get("option_line_width", panel_line_width))
    symbol_color = str(layout.get("symbol_color", trial_spec.get("symbol_color", "#111111")))
    symbol_line_width = float(layout.get("symbol_line_width", trial_spec.get("symbol_line_width", 2.0)))
    number_color = str(layout.get("number_color", "#444444"))
    number_height = float(layout.get("number_height_px", 18.0))
    number_font = str(layout.get("number_font", "Arial"))

    matrix_cells: list[dict[str, Any]] = []
    stimuli: list[Any] = []

    for row, row_name in enumerate(("top", "middle", "bottom")):
        for col, col_name in enumerate(("left", "center", "right")):
            cell_name = f"{row_name}_{col_name}"
            pos = _coerce_position(
                matrix_positions_cfg.get(cell_name),
                DEFAULT_MATRIX_POSITIONS[f"{row_name}_{col_name}"],
            )
            feature = _resolve_feature(trial_spec, row, col)
            is_missing = row == 2 and col == 2
            panel = _build_panel(
                win=win,
                pos=pos,
                size=matrix_panel_size,
                fill_color=panel_fill_color,
                line_color=panel_line_color,
                line_width=panel_line_width,
            )
            stimuli.append(panel)
            if not is_missing:
                symbol_size = float(min(matrix_panel_size)) * symbol_size_scale
                stimuli.extend(
                    _build_symbol_cluster(
                        win=win,
                        center=pos,
                        feature=feature,
                        symbol_size=symbol_size,
                        symbol_color=symbol_color,
                        line_width=symbol_line_width,
                    )
                )
            matrix_cells.append(
                {
                    "cell": cell_name,
                    "pos": [float(pos[0]), float(pos[1])],
                    "feature": feature,
                    "is_missing": is_missing,
                }
            )

    correct_feature = _resolve_feature(trial_spec, 2, 2)
    distractor_features = _option_variants(
        correct_feature,
        shape_cycle=list(trial_spec["shape_cycle"]),
        count_cycle=list(trial_spec["count_cycle"]),
        rotation_cycle=list(trial_spec["rotation_cycle"]),
    )

    options = [correct_feature] + distractor_features
    rng.shuffle(options)

    option_records: list[dict[str, Any]] = []
    correct_key = ""
    correct_position = ""
    option_position_label_map = {
        "top_left": "top-left",
        "top_right": "top-right",
        "bottom_left": "bottom-left",
        "bottom_right": "bottom-right",
    }

    for position_name, feature in zip(OPTION_POSITION_ORDER, options, strict=True):
        pos = _coerce_position(option_positions_cfg.get(position_name), DEFAULT_OPTION_POSITIONS[position_name])
        panel = _build_panel(
            win=win,
            pos=pos,
            size=option_panel_size,
            fill_color=option_fill_color,
            line_color=option_line_color,
            line_width=option_line_width,
        )
        stimuli.append(panel)
        symbol_size = float(min(option_panel_size)) * max(0.20, symbol_size_scale * 1.08)
        stimuli.extend(
            _build_symbol_cluster(
                win=win,
                center=pos,
                feature=feature,
                symbol_size=symbol_size,
                symbol_color=symbol_color,
                line_width=symbol_line_width,
            )
        )

        key_label = str(option_key_map.get(position_name, ""))
        if not key_label:
            raise ValueError(f"Missing response key for option position {position_name!r}.")
        if show_numbers:
            number_text = TextStim(
                win=win,
                text=key_label,
                pos=(pos[0] - option_panel_size[0] * 0.38, pos[1] + option_panel_size[1] * 0.32),
                color=number_color,
                height=number_height,
                font=number_font,
                alignText="center",
                anchorHoriz="center",
                anchorVert="center",
            )
            stimuli.append(number_text)

        is_correct = _feature_signature(feature) == _feature_signature(correct_feature)
        if is_correct:
            correct_key = key_label
            correct_position = position_name

        option_records.append(
            {
                "position": position_name,
                "position_label": option_position_label_map[position_name],
                "key": key_label,
                "feature": feature,
                "is_correct": is_correct,
                "pos": [float(pos[0]), float(pos[1])],
            }
        )

    if not correct_key:
        raise RuntimeError(f"Failed to assign the correct option for {trial_spec['condition_label']!r}.")

    logging.data(
        "[Raven] trial=%s condition=%s correct_key=%s template=%s"
        % (trial_id, trial_spec["condition_label"], correct_key, trial_spec["template"])
    )

    return {
        "stimuli": stimuli,
        "matrix_cells": matrix_cells,
        "options": option_records,
        "correct_key": correct_key,
        "correct_position": correct_position,
        "correct_label": option_position_label_map[correct_position],
        "display_order": [record["position_label"] for record in option_records],
        "template": str(trial_spec["template"]),
        "category": str(trial_spec["category"]),
        "practice": bool(trial_spec["practice"]),
    }
