# CHANGELOG

All notable development changes for `T000048-ravens-progressive-matrices` are documented here.

## [v0.1.0-dev] - 2026-04-16

### Added
- Raven-style matrix reasoning task flow with fixation, blank screen, 3x3 matrix presentation, clock warning, practice feedback, and ITI phases.
- Deterministic 15-item short-form bank with 3 practice items and 12 scored items.
- Task-specific sampler simulation support for build, QA, and smoke testing.

### Changed
- Replaced the visual-world scaffold with a nonverbal matrix reasoning proxy built from runtime-generated geometric patterns and four-card answer selection.
- Reworked the runtime around sequential condition ordering so practice items always appear first.
- Updated the task metadata, triggers, README, reference notes, and queue-facing descriptors for the Raven task.

### Fixed
- Removed sentence-audio and object-card assumptions from the inherited scaffold.
- Aligned the practice feedback path, response timing, and simulation profile with the matrix reasoning workflow.
