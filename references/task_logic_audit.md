# Task Logic Audit

## 1. Paradigm Intent

- Task: Raven's Progressive Matrices
- Primary construct: fluid intelligence and nonverbal abstract reasoning
- Manipulated factors: practice versus scored items, relational complexity, shape-set variant, and symbol layout
- Dependent measures: accuracy, response time, timeouts, and practice feedback performance
- Key citations:
  - `W2981704638` Chierchia et al., 2019, open-access matrix reasoning item bank
  - `W2088055785` Hampshire et al., 2012, reasoning as one component of intelligence
  - `W2167749256` Brouwers et al., 2008, Raven score variation across settings

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: 1
- Trials per block: 15
- Randomization/counterbalancing: no shuffling; items are presented in a fixed order for every participant
- Condition weight policy:
  - `task.condition_weights` is null in all configs
  - `TaskSettings.resolve_condition_weights()` is not needed because the item order is fixed
- Condition generation method:
  - Built-in `BlockUnit.generate_conditions(...)` is sufficient
  - `order='sequential'` preserves the canonical item order
  - Each condition label is a unique item ID from the item bank
- Runtime-generated trial values:
  - Matrix cell content, answer options, and trial-specific shapes are generated deterministically from the item spec
  - The generator uses the task seed plus the item label so the same participant always sees the same item sequence
  - The default bank lives in `src/utils.DEFAULT_TRIAL_BANK`; config files define the human-readable instructions, timing, and trigger map
  - The runtime uses an open-access Raven-style proxy because the canonical Raven item set is copyrighted

### Trial State Machine

1. State name: fixation
   - Onset trigger: `fixation_onset`
   - Stimuli shown: centered fixation cross
   - Valid keys: none
   - Timeout behavior: fixed 500 ms
   - Next state: blank screen

2. State name: blank_screen
   - Onset trigger: `blank_onset`
   - Stimuli shown: white blank screen
   - Valid keys: none
   - Timeout behavior: fixed 100 ms
   - Next state: matrix_response_open

3. State name: matrix_response_open
   - Onset trigger: `matrix_response_open_onset`
   - Stimuli shown: 3x3 abstract matrix with one missing cell and four response options
   - Valid keys: `1`, `2`, `3`, `4`
   - Timeout behavior: response capture remains open for 25 s
   - Next state: matrix_response_warning if no response, otherwise practice_feedback or iti

4. State name: matrix_response_warning
   - Onset trigger: `matrix_response_warning_onset`
   - Stimuli shown: same matrix and options, plus a clock warning indicator
   - Valid keys: `1`, `2`, `3`, `4`
   - Timeout behavior: final 5 s of the 30 s item limit
   - Next state: practice_feedback if practice trial, otherwise iti

5. State name: practice_feedback
   - Onset trigger: `practice_feedback_onset`
   - Stimuli shown: correctness feedback or timeout feedback
   - Valid keys: none
   - Timeout behavior: fixed brief feedback duration
   - Next state: iti

6. State name: iti
   - Onset trigger: `iti_onset`
   - Stimuli shown: brief fixation-only inter-trial interval
   - Valid keys: none
   - Timeout behavior: fixed brief duration
   - Next state: next trial

## 3. Condition Semantics

For each condition token in `task.conditions`:

- `practice_01` / `practice_02` / `practice_03`
  - Participant-facing meaning: practice item before the scored bank
  - Concrete stimulus realization (visual/audio): 3x3 matrix with abstract shapes; deterministic row/column progression; four response options; practice feedback enabled
  - Outcome rules: scored as practice only and followed by correctness feedback

- `easy_01` / `easy_02` / `easy_03` / `easy_04`
  - Participant-facing meaning: scored item with a two-rule matrix pattern
  - Concrete stimulus realization (visual/audio): 3x3 matrix with abstract shapes; row/column progression plus a simple count rule; four response options; no feedback screen
  - Outcome rules: contributes to accuracy and RT metrics

- `medium_01` / `medium_02` / `medium_03` / `medium_04`
  - Participant-facing meaning: scored item with a three-rule matrix pattern
  - Concrete stimulus realization (visual/audio): 3x3 matrix with abstract shapes; row/column progression plus a rotation shift; four response options; no feedback screen
  - Outcome rules: contributes to accuracy and RT metrics

- `hard_01` / `hard_02` / `hard_03` / `hard_04`
  - Participant-facing meaning: scored item with the most demanding pattern family in the short-form bank
  - Concrete stimulus realization (visual/audio): 3x3 matrix with abstract shapes; triad-style layout progression plus rotation shift; four response options; no feedback screen
  - Outcome rules: contributes to accuracy and RT metrics

Also document where participant-facing condition text/stimuli are defined:

- Participant-facing text source (config stimuli / code formatting / generated assets): `config/*.yaml` for instructions, prompts, feedback, and summary screens; `src/utils.DEFAULT_TRIAL_BANK` for deterministic matrix item rules
- Why this source is appropriate for auditability: the text and timings remain in config, while the non-text matrix geometry is generated deterministically from explicit item specs in code
- Localization strategy (how language variants are swapped via config without code edits): if another language is added, only the instruction, response prompt, clock warning, practice feedback, and summary YAML strings need to change; the matrix rules remain unchanged

## 4. Response and Scoring Rules

- Response mapping: `1` = top-left option, `2` = top-right option, `3` = bottom-left option, `4` = bottom-right option
- Response key source (config field vs code constant): config-defined `task.response_keys` and `task.key_list`
- If code-defined, why config-driven mapping is not sufficient: not needed; the mapping is fully config-driven
- Missing-response policy: after 30 s the item times out and the trial is scored as unanswered
- Correctness logic: the selected response key must match the item spec's correct option key
- Reward/penalty updates: none
- Running metrics: accuracy, mean correct RT, timeout count, and practice feedback counts

## 5. Stimulus Layout Plan

For every screen with multiple simultaneous options/stimuli:

- Screen name: instruction screen
  - Stimulus IDs shown together: `instruction_text`
  - Layout anchors (`pos`): centered on screen
  - Size/spacing (`height`, width, wrap): large centered text with wrap width around 1000 px
  - Readability/overlap checks: single-stimulus screen, no overlap risk
  - Rationale: explains the matrix format before trials begin

- Screen name: matrix response screen
  - Stimulus IDs shown together: 3x3 matrix cells, blank target cell, four answer options, response prompt, optional clock warning
  - Layout anchors (`pos`): matrix centered slightly above midline; options in a 2x2 grid below the matrix; prompt near the bottom; clock banner at the top
  - Size/spacing (`height`, width, wrap): matrix cells roughly 88 px with consistent gaps; options in larger cards to keep the 1-4 mapping readable
  - Readability/overlap checks: labels and shapes must remain separated at 1280x720, with a QA pass for the 2x2 option grid
  - Rationale: preserves the standard Raven-style matrix-plus-options layout

- Screen name: practice feedback screen
  - Stimulus IDs shown together: `practice_feedback_correct`, `practice_feedback_incorrect`, or `practice_feedback_timeout`
  - Layout anchors (`pos`): centered
  - Size/spacing (`height`, width, wrap): single short message, large enough for quick reading
  - Readability/overlap checks: single-stimulus screen, no overlap risk
  - Rationale: gives practice-only response guidance without interrupting scored items

- Screen name: block break / goodbye
  - Stimulus IDs shown together: `block_break_text` and `good_bye_text`
  - Layout anchors (`pos`): centered
  - Size/spacing (`height`, width, wrap): centered wrapped text with summary metrics
  - Readability/overlap checks: single-stimulus screen, no overlap risk
  - Rationale: reports summary performance and preserves a simple flow

## 6. Trigger Plan

- `exp_onset`: task start
- `exp_end`: task end
- `block_onset`: block start
- `block_end`: block end
- `fixation_onset`: fixation cross onset
- `blank_onset`: white blank screen between fixation and matrix
- `matrix_response_open_onset`: matrix response window open
- `matrix_response_warning_onset`: last 5 s warning window
- `response_1` / `response_2` / `response_3` / `response_4`: option selection triggers
- `response_timeout`: no response by the end of the 30 s limit
- `practice_feedback_onset`: practice-only feedback onset
- `iti_onset`: inter-trial interval onset

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style (simple single flow / helper-heavy / why): simple single flow with a mode-aware setup and a single block loop
- `utils.py` used? (yes/no): yes
- If yes, exact purpose (adaptive controller / sequence generation / asset pool / other): deterministic matrix generation, answer-option generation, and layout bookkeeping
- Custom controller used? (yes/no): no
- If yes, why PsyFlow-native path is insufficient: not needed
- Legacy/backward-compatibility fallback logic required? (yes/no): no
- If yes, scope and removal plan: not applicable

## 8. Inference Log

- Decision: use an open-access matrix reasoning item bank as the implementation proxy rather than the copyrighted Raven item set
  - Why inference was required: the classic Raven items are not freely reusable
  - Citation-supported rationale: the MaRs-IB paper explicitly says its items were designed to be similar to Raven's matrices and are open access

- Decision: keep a fixed three-item practice prefix
  - Why inference was required: the paper's practice protocol continues until three items are completed correctly, but the PsyFlow runtime is more auditable with a fixed prefix
  - Citation-supported rationale: the MaRs-IB paper reports that participants practiced until three correct items were completed and received feedback on all items

- Decision: split the 30 s response period into a 25 s open window and a 5 s warning window
  - Why inference was required: the paper specifies the 25 s clock warning but the runtime benefits from a clear phase boundary
  - Citation-supported rationale: the MaRs-IB paper states that items begin with a 500 ms fixation, then a 100 ms white screen, with a clock appearing after 25 s and a 30 s total response limit

- Decision: use a 15-item short-form bank with 3 practice items and 12 scored items
  - Why inference was required: the open item bank contains 80 items and the task runner needs a brief behavioral version
  - Citation-supported rationale: the MaRs-IB paper explicitly notes that researchers can select items to create tasks of custom duration and difficulty

## Contract Note

- Participant-facing labels/instructions/options should be config-defined whenever possible.
- `src/run_trial.py` should not hardcode participant-facing text that would require code edits for localization.
