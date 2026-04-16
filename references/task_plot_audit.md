# Task Plot Audit

- generated_at: 2026-04-16T10:40:58
- mode: existing
- task_path: E:\Taskbeacon\T000048-ravens-progressive-matrices

## 1. Inputs and provenance

- E:\Taskbeacon\T000048-ravens-progressive-matrices\README.md
- E:\Taskbeacon\T000048-ravens-progressive-matrices\config\config.yaml
- E:\Taskbeacon\T000048-ravens-progressive-matrices\src\run_trial.py

## 2. Evidence extracted from README

- | Step | Description |
- |---|---|
- | Fixation | Show a centered fixation cross for 0.5 s. |
- | Blank Screen | Show a white blank screen for 0.1 s between fixation and stimulus onset. |
- | Matrix Response Open | Show the 3x3 matrix, four answer cards, and response prompt for up to 25 s. |
- | Matrix Response Warning | Show the same matrix plus a clock warning banner for the last 5 s if needed. |
- | Practice Feedback | Show correctness feedback for practice items only. |
- | ITI | Show the fixation cross again for 0.6 s before the next trial. |

## 3. Evidence extracted from config/source

- practice_01: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- practice_01: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- practice_01: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- practice_01: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- practice_01: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- practice_01: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- practice_02: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- practice_02: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- practice_02: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- practice_02: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- practice_02: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- practice_02: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- practice_03: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- practice_03: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- practice_03: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- practice_03: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- practice_03: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- practice_03: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- easy_01: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- easy_01: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- easy_01: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- easy_01: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- easy_01: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- easy_01: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- easy_02: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- easy_02: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- easy_02: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- easy_02: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- easy_02: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- easy_02: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- easy_03: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- easy_03: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- easy_03: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- easy_03: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- easy_03: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- easy_03: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- easy_04: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- easy_04: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- easy_04: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- easy_04: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- easy_04: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- easy_04: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- medium_01: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- medium_01: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- medium_01: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- medium_01: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- medium_01: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- medium_01: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- medium_02: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- medium_02: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- medium_02: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- medium_02: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- medium_02: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- medium_02: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- medium_03: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- medium_03: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- medium_03: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- medium_03: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- medium_03: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- medium_03: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- medium_04: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- medium_04: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- medium_04: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- medium_04: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- medium_04: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- medium_04: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- hard_01: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- hard_01: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- hard_01: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- hard_01: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- hard_01: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- hard_01: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- hard_02: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- hard_02: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- hard_02: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- hard_02: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- hard_02: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- hard_02: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- hard_03: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- hard_03: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- hard_03: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- hard_03: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- hard_03: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- hard_03: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- hard_04: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- hard_04: phase=blank screen, deadline_expr=blank_duration, response_expr=n/a, stim_expr='blank_screen'
- hard_04: phase=matrix response open, deadline_expr=response_open_duration, response_expr=n/a, stim_expr='matrix_and_options'
- hard_04: phase=matrix response warning, deadline_expr=response_warning_duration, response_expr=n/a, stim_expr='matrix_and_options+clock_warning'
- hard_04: phase=practice feedback, deadline_expr=feedback_duration, response_expr=n/a, stim_expr=feedback_name
- hard_04: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 15
- screens_per_timeline: 6
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.029, right=0.032, blank=0.115
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0294, 'right_ratio': 0.0319, 'blank_ratio': 0.1149}

## 7. Output files and checksums

- E:\Taskbeacon\T000048-ravens-progressive-matrices\references\task_plot_spec.yaml: sha256=0c04e4680572ffbf7146afe6242067cf0c2def3b77c27d7933509420f2a3c577
- E:\Taskbeacon\T000048-ravens-progressive-matrices\references\task_plot_spec.json: sha256=50ad802be25c6bbc4fc30b73d6b0938e4a084dba1bb415340821a0db55f64ccb
- E:\Taskbeacon\T000048-ravens-progressive-matrices\references\task_plot_source_excerpt.md: sha256=5d7ebf407d3d25f1c10fab3d6b98826e28e4ec6ccc26f7efd739e80c7f0fd6b0
- E:\Taskbeacon\T000048-ravens-progressive-matrices\task_flow.png: sha256=278d64bed1eecdcc19b4b16aae282b744f33e6dccfcf1666be39077a63ece94e

## 8. Inferred/uncertain items

- practice_01:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- practice_01:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- practice_01:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- practice_01:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- practice_01:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- practice_01:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- practice_02:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- practice_02:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- practice_02:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- practice_02:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- practice_02:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- practice_02:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- practice_03:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- practice_03:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- practice_03:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- practice_03:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- practice_03:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- practice_03:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- easy_01:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- easy_01:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- easy_01:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- easy_01:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- easy_01:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- easy_01:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- easy_02:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- easy_02:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- easy_02:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- easy_02:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- easy_02:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- easy_02:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- easy_03:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- easy_03:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- easy_03:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- easy_03:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- easy_03:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- easy_03:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- easy_04:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- easy_04:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- easy_04:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- easy_04:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- easy_04:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- easy_04:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- medium_01:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- medium_01:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- medium_01:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- medium_01:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- medium_01:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- medium_01:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- medium_02:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- medium_02:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- medium_02:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- medium_02:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- medium_02:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- medium_02:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- medium_03:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- medium_03:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- medium_03:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- medium_03:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- medium_03:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- medium_03:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- medium_04:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- medium_04:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- medium_04:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- medium_04:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- medium_04:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- medium_04:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- hard_01:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- hard_01:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- hard_01:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- hard_01:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- hard_01:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- hard_01:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- hard_02:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- hard_02:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- hard_02:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- hard_02:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- hard_02:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- hard_02:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- hard_03:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- hard_03:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- hard_03:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- hard_03:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- hard_03:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- hard_03:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- hard_04:fixation:heuristic numeric parse from '_duration(settings, 'fixation_duration', 0.5)'
- hard_04:blank screen:heuristic numeric parse from '_duration(settings, 'blank_duration', 0.1)'
- hard_04:matrix response open:heuristic numeric parse from '_duration(settings, 'response_open_duration', 25000.0)'
- hard_04:matrix response warning:heuristic numeric parse from '_duration(settings, 'response_warning_duration', 5000.0)'
- hard_04:practice feedback:heuristic numeric parse from '_duration(settings, 'feedback_duration', 0.8)'
- hard_04:iti:heuristic numeric parse from '_duration(settings, 'iti_duration', 0.6)'
- collapsed equivalent condition logic into representative timeline: practice_01, practice_02, practice_03, easy_01, easy_02, easy_03, easy_04, medium_01, medium_02, medium_03, medium_04, hard_01, hard_02, hard_03, hard_04
- unparsed if-tests defaulted to condition-agnostic applicability: correct_key not in response_keys; not response_keys; open_response is None; response_correct; timed_out; trial_data['practice']
