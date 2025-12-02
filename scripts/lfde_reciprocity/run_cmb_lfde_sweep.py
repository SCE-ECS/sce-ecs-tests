#!/usr/bin/env python
import argparse

from sceecs_tests.config import load_config
from sceecs_tests.cmb_io import load_cmb_dataset
from metrics.lfde_reciprocity import (
    compute_lfde_reciprocity_cmb,
    save_lfde_results,
)


def main():
    parser = argparse.ArgumentParser(
        description="Run LFDE reciprocity test for CMB (WMAP/Planck-like datasets).",
        exit_on_error=False,
    )
    parser.add_argument(
        "--config",
        default="configs/template_cmb_wmap.yaml",
        help="Path to YAML config file describing a CMB dataset.",
    )

    args, unknown = parser.parse_known_args()

    cfg = load_config(args.config)

    if cfg.get("domain") != "cmb":
        raise ValueError(f"Config domain must be 'cmb' for CMB LFDE tests, got: {cfg.get('domain')}")

    ks = cfg["lfde"]["ks_values"]

    cmb = load_cmb_dataset(cfg)
    df = compute_lfde_reciprocity_cmb(cmb, ks)

    output_csv = cfg["lfde"]["output_csv"]
    output_plot = cfg["lfde"]["output_plot"]
    save_lfde_results(df, output_csv, output_plot)

    print(f"Saved CSV to {output_csv}")
    print(f"Saved plot to {output_plot}")


if __name__ == "__main__":
    main()
