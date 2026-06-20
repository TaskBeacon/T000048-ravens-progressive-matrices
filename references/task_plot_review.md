# Task Plot Review

## Evidence Match

- Pass: title and construct match Raven's Progressive Matrices.
- Pass: rows reflect practice, easy, medium, and hard item contexts.
- Pass: phase order matches README and `src/run_trial.py`: Fixation -> Blank screen -> Matrix response open -> Matrix response warning -> Practice feedback or no-feedback -> ITI.
- Pass: timing labels match config: 500 ms fixation, 100 ms blank, 25000 ms response open, 5000 ms warning, 800 ms practice feedback, 600 ms ITI.
- Pass: response mapping shows keys 1/2/3/4.
- Pass: scored rows show no trial feedback, while practice row shows feedback.
- Pass: diagram uses abstract geometric matrix proxies and does not recreate copyrighted Raven items.

## Visual Quality

- Pass: labels and timings are readable.
- Pass: generated timeline content stays below the header band.
- Pass: fixed title and Construct subtitle are centered.
- Pass: top-right TaskBeacon logo lockup is borderless and non-overlapping.
- Pass: no generated title, logo, watermark, people, devices, or decorative scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
