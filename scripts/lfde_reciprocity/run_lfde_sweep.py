#!/usr/bin/env python
import argparse
from pathlib import Path
import numpy as np

from sceecs_tests.config import load_config
from metrics.lfde_reciprocity import (
    compute_lfde_reciprocity,
    save_lfde_results,
)


def main():
    parser = argparse.ArgumentParser(
        description="Run LFDE reciprocity test for HIT.",
        exit_on_error=False  # <-- Fix för Jupyter
    )
    parser.add_argument(
        "--config",
        default="configs/turbulence_hit.yaml",
        help="Path to YAML config file.",
    )

    # Använd parse_known_args för att ignorera Jupyers egna argument
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
