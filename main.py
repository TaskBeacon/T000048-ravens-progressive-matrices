from contextlib import nullcontext
from functools import partial
from pathlib import Path

import pandas as pd
from psychopy import core

from psyflow import (
    BlockUnit,
    StimBank,
    StimUnit,
    SubInfo,
    TaskRunOptions,
    TaskSettings,
    context_from_config,
    count_down,
    initialize_exp,
    initialize_triggers,
    load_config,
    parse_task_run_options,
    runtime_context,
)

from src import run_trial

MODES = ("human", "qa", "sim")
DEFAULT_CONFIG_BY_MODE = {
    "human": "config/config.yaml",
    "qa": "config/config_qa.yaml",
    "sim": "config/config_scripted_sim.yaml",
}


def _prepare_voice_assets(stim_bank: StimBank, settings: TaskSettings) -> StimBank:
    voice_name = str(getattr(settings, "voice_name", "en-US-AriaNeural"))
    if bool(getattr(settings, "voice_enabled", True)):
        stim_bank = stim_bank.convert_to_voice("instruction_text", voice=voice_name)

        trial_bank = dict(getattr(settings, "trial_bank", {}) or {})
        for condition_label, spec in trial_bank.items():
            sentence_text = str(dict(spec).get("sentence_text", "")).strip()
            if not sentence_text:
                continue
            stim_bank.add_voice(str(condition_label), sentence_text, voice=voice_name)

    return stim_bank


def run(options: TaskRunOptions):
    """Run task in human/qa/sim mode with one auditable runtime flow."""
    task_root = Path(__file__).resolve().parent
    cfg = load_config(str(options.config_path))

    output_dir: Path | None = None
    runtime_scope = nullcontext()
    runtime_ctx = None
    if options.mode in ("qa", "sim"):
        runtime_ctx = context_from_config(task_dir=task_root, config=cfg, mode=options.mode)
        output_dir = runtime_ctx.output_dir
        runtime_scope = runtime_context(runtime_ctx)

    with runtime_scope:
        if options.mode == "qa":
            subject_data = {"subject_id": "qa"}
        elif options.mode == "sim":
            participant_id = "sim"
            if runtime_ctx is not None and runtime_ctx.session is not None:
                participant_id = str(runtime_ctx.session.participant_id or "sim")
            subject_data = {"subject_id": participant_id}
        else:
            subform = SubInfo(cfg["subform_config"])
            subject_data = subform.collect()

        settings = TaskSettings.from_dict(cfg["task_config"])
        if options.mode in ("qa", "sim") and output_dir is not None:
            settings.save_path = str(output_dir)
        settings.add_subinfo(subject_data)

        if options.mode == "qa" and output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            settings.res_file = str(output_dir / "qa_trace.csv")
            settings.log_file = str(output_dir / "qa_psychopy.log")
            settings.json_file = str(output_dir / "qa_settings.json")

        settings.triggers = cfg["trigger_config"]
        trigger_runtime = initialize_triggers(mock=True) if options.mode in ("qa", "sim") else initialize_triggers(cfg)

        win, kb = initialize_exp(settings)

        stim_bank = StimBank(win, cfg["stim_config"])
        stim_bank = _prepare_voice_assets(stim_bank, settings)
        stim_bank = stim_bank.preload_all()

        settings.save_to_json()

        trigger_runtime.send(settings.triggers.get("exp_onset"))

        instruction = StimUnit("instruction_text", win, kb, runtime=trigger_runtime).add_stim(
            stim_bank.get("instruction_text")
        )
        if options.mode not in ("qa", "sim") and stim_bank.has("instruction_text_voice"):
            instruction.add_stim(stim_bank.get("instruction_text_voice"))
        instruction.wait_and_continue()

        all_data = []
        condition_weights = settings.resolve_condition_weights()

        for block_i in range(settings.total_blocks):
            if options.mode not in ("qa", "sim"):
                count_down(win, 3, color="black")

            block_seed = int(getattr(settings, "overall_seed", 2026)) + (block_i * 1009)
            block = (
                BlockUnit(
                    block_id=f"block_{block_i}",
                    block_idx=block_i,
                    settings=settings,
                    window=win,
                    keyboard=kb,
                )
                .generate_conditions(
                    n_trials=int(settings.trials_per_block),
                    condition_labels=list(getattr(settings, "conditions", [])),
                    weights=condition_weights,
                    order="sequential",
                    seed=block_seed,
                )
                .on_start(lambda b: trigger_runtime.send(settings.triggers.get("block_onset")))
                .on_end(lambda b: trigger_runtime.send(settings.triggers.get("block_end")))
                .run_trial(
                    partial(
                        run_trial,
                        stim_bank=stim_bank,
                        trigger_runtime=trigger_runtime,
                        block_id=f"block_{block_i}",
                        block_idx=block_i,
                    )
                )
                .to_dict(all_data)
            )

            block_trials = block.get_all_data()
            correct_trials = [trial for trial in block_trials if bool(trial.get("response_correct", False))]
            accuracy = (len(correct_trials) / len(block_trials)) if block_trials else 0.0
            rts = [
                float(trial["response_rt"])
                for trial in correct_trials
                if isinstance(trial.get("response_rt"), (int, float))
            ]
            mean_rt = (sum(rts) / len(rts)) if rts else 0.0
            timeout_count = sum(1 for trial in block_trials if bool(trial.get("timed_out", False)))

            StimUnit("block", win, kb, runtime=trigger_runtime).add_stim(
                stim_bank.get_and_format(
                    "block_break",
                    block_num=block_i + 1,
                    total_blocks=settings.total_blocks,
                    block_accuracy=accuracy,
                    mean_rt_ms=mean_rt * 1000.0,
                    timeout_count=timeout_count,
                )
            ).wait_and_continue()

        total_correct = sum(1 for trial in all_data if bool(trial.get("response_correct", False)))
        total_timeouts = sum(1 for trial in all_data if bool(trial.get("timed_out", False)))
        all_rts = [
            float(trial["response_rt"])
            for trial in all_data
            if bool(trial.get("response_correct", False)) and isinstance(trial.get("response_rt"), (int, float))
        ]
        total_accuracy = (total_correct / len(all_data)) if all_data else 0.0
        mean_rt_ms = (sum(all_rts) / len(all_rts) * 1000.0) if all_rts else 0.0

        StimUnit("goodbye", win, kb, runtime=trigger_runtime).add_stim(
            stim_bank.get_and_format(
                "good_bye",
                total_trials=len(all_data),
                total_accuracy=total_accuracy,
                mean_rt_ms=mean_rt_ms,
                total_timeouts=total_timeouts,
            )
        ).wait_and_continue(terminate=True)

        trigger_runtime.send(settings.triggers.get("exp_end"))

        pd.DataFrame(all_data).to_csv(settings.res_file, index=False)

        trigger_runtime.close()
        core.quit()


def main() -> None:
    task_root = Path(__file__).resolve().parent
    options = parse_task_run_options(
        task_root=task_root,
        description="Run task in human/qa/sim mode.",
        default_config_by_mode=DEFAULT_CONFIG_BY_MODE,
        modes=MODES,
    )
    run(options)


if __name__ == "__main__":
    main()
