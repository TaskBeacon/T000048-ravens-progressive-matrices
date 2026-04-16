# Stimulus Mapping

Map each implemented condition/stimulus to the selected literature source.
All unresolved markers must be removed before publish.

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| instruction screen | instruction | `instruction_text` | Task instructions explaining the 3x3 matrix, four answer cards, practice-first structure, and 30 s limit with a clock warning | W2981704638 | Matrix reasoning task instructions and timed response window | psychopy_builtin | `config/config.yaml`; `config/config_qa.yaml`; `config/config_scripted_sim.yaml`; `config/config_sampler_sim.yaml` | Config-defined static text. |
| fixation | fixation | `fixation` | Center fixation cross | W2981704638 | 500 ms fixation before each item | psychopy_builtin | `config/*.yaml` | Shared across all phases. |
| blank screen | pre-stimulus | `blank_screen` | White blank screen between fixation and stimulus onset | W2981704638 | 100 ms white screen between fixation and item display | psychopy_builtin | `config/*.yaml` | Explicit blank phase for timing fidelity. |
| `practice_01` | matrix_response_open; practice_feedback | `matrix_panels`, `answer_cards`, `response_prompt`, `practice_feedback_correct`, `practice_feedback_incorrect`, `practice_feedback_timeout` | 3x3 abstract matrix with one missing cell, four answer cards labeled 1-4, and practice-only feedback | W2981704638 | 3x3 matrices, four-choice response format, practice feedback | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Practice item from the short-form ordered bank. |
| `practice_02` | matrix_response_open; practice_feedback | `matrix_panels`, `answer_cards`, `response_prompt`, `practice_feedback_correct`, `practice_feedback_incorrect`, `practice_feedback_timeout` | 3x3 abstract matrix with one missing cell, four answer cards labeled 1-4, and practice-only feedback | W2981704638 | 3x3 matrices, four-choice response format, practice feedback | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Practice item from the short-form ordered bank. |
| `practice_03` | matrix_response_open; practice_feedback | `matrix_panels`, `answer_cards`, `response_prompt`, `practice_feedback_correct`, `practice_feedback_incorrect`, `practice_feedback_timeout` | 3x3 abstract matrix with one missing cell, four answer cards labeled 1-4, and practice-only feedback | W2981704638 | 3x3 matrices, four-choice response format, practice feedback | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Practice item from the short-form ordered bank. |
| `easy_01` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a two-rule pattern and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `easy_02` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a two-rule pattern and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `easy_03` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a two-rule pattern and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `easy_04` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a two-rule pattern and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `medium_01` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a rotation shift and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `medium_02` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a rotation shift and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `medium_03` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a rotation shift and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `medium_04` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with a rotation shift and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `hard_01` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with triad layout progression and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `hard_02` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with triad layout progression and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `hard_03` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with triad layout progression and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| `hard_04` | matrix_response_open | `matrix_panels`, `answer_cards`, `response_prompt` | 3x3 abstract matrix with triad layout progression and four answer cards | W2981704638 | Matrix reasoning items used as an abstract reasoning proxy | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Scored item. |
| all conditions | matrix_response_warning | `matrix_panels`, `answer_cards`, `response_prompt`, `clock_warning` | Same matrix and answer cards plus a clock warning banner for the final 5 s | W2981704638 | 25 s clock warning followed by a 30 s total limit | psychopy_builtin | `src/utils.py`; `config/*.yaml` | Shown only if no response is collected during the open window. |
| all conditions | block summary | `block_break` | Block summary with accuracy, mean correct RT, and timeouts | W2981704638 | Short-form block-level feedback and pacing | psychopy_builtin | `config/*.yaml` | Shown once after the single block. |
| all conditions | final summary | `good_bye` | Final task summary and exit screen | W2981704638 | End-of-task summary screen | psychopy_builtin | `config/*.yaml` | Keeps the closing flow auditable. |

Accepted implementation modes:
- `psychopy_builtin`
- `generated_reference_asset`
- `licensed_external_asset`

Decision rule:
- Participant-facing text should be configured in `config/*.yaml` stimuli and referenced via stimulus IDs.
