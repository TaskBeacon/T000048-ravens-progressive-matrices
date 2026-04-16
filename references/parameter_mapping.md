# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|---|
| task_name | `task.task_name` | Raven's Progressive Matrices | W2981704638; W2167749256 | Matrix reasoning / Raven-style abstract reasoning construct | direct | Title aligned to the target paradigm name. |
| total_blocks | `task.total_blocks` | 1 | W2981704638 | Short-form single-session behavioral build | inferred | One block keeps the short proxy easy to audit. |
| trial_per_block | `task.trial_per_block` | 15 | W2981704638 | Open item bank allows task-length selection | inferred | Fixed short-form bank: 3 practice + 12 scored items. |
| condition_order | `task.conditions` | `practice_01, practice_02, practice_03, easy_01, easy_02, easy_03, easy_04, medium_01, medium_02, medium_03, medium_04, hard_01, hard_02, hard_03, hard_04` | W2981704638 | Practice-first ordered bank with item-level sequential scheduling | inferred | The code defaults to the 15-item ordered Raven proxy. |
| fixation_duration_s | `timing.fixation_duration` | 0.5 | W2981704638 | 500 ms fixation before each item | direct | Matches the paper's pre-item fixation timing. |
| blank_duration_s | `timing.blank_duration` | 0.1 | W2981704638 | 100 ms white screen after fixation | direct | Explicit blank phase separates fixation from the matrix. |
| response_open_duration_s | `timing.response_open_duration` | 25000 (normalized to 25.0 s in runtime) | W2981704638 | Clock warning appears after 25 s in a 30 s total window | direct | Open response phase before the warning banner. |
| response_warning_duration_s | `timing.response_warning_duration` | 5000 (normalized to 5.0 s in runtime) | W2981704638 | Final 5 s warning to finish the response | direct | Completes the 30 s response limit. |
| feedback_duration_s | `timing.feedback_duration` | 0.8 | W2981704638 | Practice feedback is shown after practice items | inferred | Duration chosen for auditable practice feedback without slowing the block. |
| iti_duration_s | `timing.iti_duration` | 0.6 | W2981704638 | Brief between-item reset period | inferred | Keeps pacing similar to the source workflow. |
| response_keys | `task.response_keys` | `["1", "2", "3", "4"]` | W2981704638 | Four-way multiple-choice response format | direct | Keys map to the four answer cards in fixed screen positions. |
| practice_feedback_mode | `src/run_trial.py` + `stimuli.practice_feedback_*` | Practice-only correctness feedback | W2981704638 | Practice until criteria / feedback on practice items | inferred | Feedback is suppressed on scored items. |
