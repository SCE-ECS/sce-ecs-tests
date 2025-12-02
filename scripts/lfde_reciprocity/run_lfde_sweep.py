#!/usr/bin/env python
import argparse
from pathlib import Path
import numpy as np

from sceecs_tests.config import load_config
from metrics.lfde_reciprocity import (
    compute_lfde_reciprocity,
    save_lfde_results,
)


def load_hit_field(cfg):
    """
    Placeholder för HIT-inläsning.
    TODO: ersätt med verklig inläsning från cfg['files']['velocity_raw'].
    """
    data_root = Path(cfg["data_root"])
    vel_rel_path = cfg["files"]["velocity_raw"]
    vel_path = data_root / vel_rel_path

    # Just nu: ignorera vel_path och skapa ett syntetiskt fält.
    # Senare läser vi riktig HIT-data istället.
    field = np.random.randn(64, 64, 64)
    return field


def main():
    parser = argparse.ArgumentParser(
        description="Run LFDE reciprocity test for HIT.",
        exit_on_error=False  # Fix för Jupyter/Colab
    )
    parser.add_argument(
        "--config",
        default="configs/turbulence_hit.yaml",
        help="Path to YAML config file.",
    )

    # Ignorera Jupyters egna argument om de smyger sig in
    args, unknown = parser.parse_known_args()

    cfg = load_config(args.config)
    ks = cfg["lfde"]["ks_values"]

    field = load_hit_field(cfg)
    df = compute_lfde_reciprocity(field, ks)

    output_csv = cfg["lfde"]["output_csv"]
    output_plot = cfg["lfde"]["output_plot"]
    save_lfde_results(df, output_csv, output_plot)

    print(f"Saved CSV to {output_csv}")
    print(f"Saved plot to {output_plot}")


if __name__ == "__main__":
    main()
