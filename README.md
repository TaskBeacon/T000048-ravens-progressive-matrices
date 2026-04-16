# Raven's Progressive Matrices

| Field | Value |
|---|---|
| Name | Raven's Progressive Matrices |
| Version | v0.1.0-dev |
| URL / Repository | `E:\Taskbeacon\T000048-ravens-progressive-matrices` |
| Short Description | Behavioral proxy for matrix reasoning with 3x3 abstract pattern completion |
| Created By | TaskBeacon build pipeline |
| Date Updated | 2026-04-16 |
| PsyFlow Version | 0.1.12 |
| PsychoPy Version | 2025.2.4 |
| Modality | Behavior |
| Language | English |

## 1. Task Overview

This task implements a Raven-style matrix reasoning proxy in PsychoPy/PsyFlow. Participants view a 3x3 abstract matrix with one missing cell and select the best completion from four answer cards using keys 1-4.

The build uses a fixed 15-item ordered bank:
3 practice items first, followed by 12 scored items. The matrices are generated from deterministic geometric rules so that the runtime remains auditable without relying on copyrighted Raven stimuli.

## 2. Task Flow

![Task Flow](task_flow.png)

### Block-Level Flow

| Step | Description |
|---|---|
| Load Config | Read the mode-specific config and task metadata. |
| Collect Subject Info | Collect subject ID in human mode or inject deterministic IDs in QA/sim. |
| Initialize Runtime | Create the PsychoPy window, keyboard, triggers, and stimulus bank. |
| Show Instructions | Present the Raven-style instructions and key mapping. |
| Run Block | Present the fixed 15-item bank in sequential order. |
| Show Block Break | Display accuracy, mean correct RT, and timeout count. |
| Save Outputs | Write CSV data and the settings JSON to the mode output folder. |
| Finish | Present the goodbye screen, send the end trigger, and quit PsychoPy. |

### Trial-Level Flow

| Step | Description |
|---|---|
| Fixation | Show a centered fixation cross for 0.5 s. |
| Blank Screen | Show a white blank screen for 0.1 s between fixation and stimulus onset. |
| Matrix Response Open | Show the 3x3 matrix, four answer cards, and response prompt for up to 25 s. |
| Matrix Response Warning | Show the same matrix plus a clock warning banner for the last 5 s if needed. |
| Practice Feedback | Show correctness feedback for practice items only. |
| ITI | Show the fixation cross again for 0.6 s before the next trial. |

### Controller Logic

| Feature | Description |
|---|---|
| Condition Scheduling | `BlockUnit.generate_conditions(...)` runs the condition list sequentially so the practice prefix always comes first. |
| Determinism | The item generator uses the configured overall seed plus the trial label to keep the matrix bank reproducible. |
| Trial Context | Every participant-visible phase in `src/run_trial.py` calls `set_trial_context(...)` before display or response capture. |
| Scoring | Correctness is based on matching the selected response key to the key assigned to the correct answer card. |
| Simulation | The scripted responder exercises the response path, and the sampler responder varies accuracy, RT, and timeout behavior. |

## 3. Configuration Summary

### a. Subject Info

| Field | Meaning |
|---|---|
| `subject_id` | Three-digit participant identifier. |

### b. Window Settings

| Parameter | Value |
|---|---|
| `window.size` | `[1280, 720]` |
| `window.units` | `pix` |
| `window.bg_color` | `black` |
| `window.fullscreen` | `false` |
| `window.screen` | `0` |

### c. Stimuli

| Stimulus ID | Purpose |
|---|---|
| `instruction_text` | Intro screen explaining the matrix task, practice structure, and response keys. |
| `fixation` | Center fixation cross. |
| `blank_screen` | Brief white inter-stimulus screen. |
| `response_prompt` | Prompt shown during the response window. |
| `clock_warning` | Final-5-second warning banner. |
| `practice_feedback_correct` / `practice_feedback_incorrect` / `practice_feedback_timeout` | Practice-only feedback screens. |
| `block_break` | Block summary with accuracy, mean RT, and timeouts. |
| `good_bye` | Final task summary and exit screen. |

### d. Timing

| Parameter | Value |
|---|---|
| `timing.fixation_duration` | `0.5` s |
| `timing.blank_duration` | `0.1` s |
| `timing.response_open_duration` | `25,000` ms (`25.0` s) |
| `timing.response_warning_duration` | `5,000` ms (`5.0` s) |
| `timing.feedback_duration` | `0.8` s |
| `timing.iti_duration` | `0.6` s |

### e. Triggers

| Trigger | Code |
|---|---|
| `exp_onset` / `exp_end` | `1` / `2` |
| `block_onset` / `block_end` | `10` / `11` |
| `fixation_onset` | `20` |
| `blank_onset` | `21` |
| `matrix_response_open_onset` | `30` |
| `matrix_response_warning_onset` | `31` |
| `response_1` / `response_2` / `response_3` / `response_4` | `41` / `42` / `43` / `44` |
| `response_timeout` | `45` |
| `practice_feedback_onset` | `50` |
| `iti_onset` | `60` |

## 4. Methods (for academic publication)

Participants completed a nonverbal matrix reasoning task implemented in PsychoPy/PsyFlow. Each trial presented a 3x3 abstract matrix with one missing cell and four candidate answer cards. Participants selected the best completion with a 4-choice keyboard mapping.

The build uses a fixed short-form bank with practice items first and scored items afterward. Matrix features are generated deterministically from the task seed and item label so the task is reproducible for auditing, simulation, and plotting while remaining free of copyrighted Raven stimulus assets.
