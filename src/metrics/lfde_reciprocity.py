import numpy as np
import pandas as pd
from pathlib import Path

def compute_lfde_reciprocity(field, ks_values):
    """
    SKELETT för LFDE-reciprocitet.
    TODO: ersätt med din faktiska LFDE-avatar-beräkning.

    Parameters
    ----------
    field : np.ndarray
        T.ex. ett 3D-velocityfält från HIT.
    ks_values : sequence of float
        Diskreta skalor/vågtal.

    Returns
    -------
    pd.DataFrame
        Kolumner: k, lfde_value
    """
    lfde_vals = []
    for k in ks_values:
        # Här skall senare LFDE-invarianten per k räknas.
        # Just nu: dummy som bara ger något tal.
        val = float(k)
        lfde_vals.append(val)

    return pd.DataFrame({"k": ks_values, "lfde_value": lfde_vals})


def save_lfde_results(df, output_csv, output_plot=None):
    """
    Spara LFDE-resultat som CSV och ev. enkel plot.
    """
    output_csv = Path(output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)

    if output_plot is not None:
        import matplotlib.pyplot as plt
        output_plot = Path(output_plot)
        output_plot.parent.mkdir(parents=True, exist_ok=True)

        plt.figure()
        plt.plot(df["k"], df["lfde_value"], marker="o")
        plt.xscale("log")
        plt.xlabel("k")
        plt.ylabel("LFDE reciprocity (arb. units)")
        plt.tight_layout()
        plt.savefig(output_plot)
        plt.close()


import pandas as pd
import numpy as np
import healpy as hp


def compute_lfde_reciprocity_cmb(cmb: dict, ks) -> pd.DataFrame:
    """
    Placeholder/L3-skelett för LFDE-reciprocitetsberäkning på CMB-data.

    Parametrar
    ----------
    cmb : dict
        Dict från sceecs_tests.cmb_io.load_cmb_dataset:
          {
            "T": np.ndarray eller None,
            "Q": np.ndarray eller None,
            "U": np.ndarray eller None,
            "mask": np.ndarray eller None,
            "nside": int
          }
    ks : sekvens av "skalor" (t.ex. multipol-bins eller liknande)

    Returnerar
    ----------
    pandas.DataFrame med kolumner:
      - 'k'
      - 'lfde_value'

    OBS:
      Detta är en strukturell placeholder så att CMB-pipelinen är komplett.
      Själva LFDE-avatar-metriken för CMB ska ersätta denna implementering.
    """
    T = cmb.get("T")
    mask = cmb.get("mask")
    nside = cmb.get("nside")

    if T is None:
        raise ValueError("CMB-dataset saknar T-karta; åtminstone T_map krävs för LFDE CMB-analys.")

    npix = T.size
    expected_npix = 12 * nside * nside
    if npix != expected_npix:
        raise ValueError(f"T-kartan har fel antal pixlar: {npix}, förväntade {expected_npix} för nside={nside}.")

    # Applicera mask om den finns
    if mask is not None:
        if mask.size != npix:
            raise ValueError("Mask och T-karta har olika antal pixlar.")
        T_eff = T.copy()
        T_eff[~mask] = np.nan
    else:
        T_eff = T

    # Placeholder-beräkning:
    # För varje k: ta t.ex. medelvärdet av |T| på hela himlen delat med (1 + k)
    rows = []
    abs_T = np.abs(T_eff)
    mean_abs_T = np.nanmean(abs_T)

    for k in ks:
        # Denna formel är bara en strukturell placeholder.
        lfde_val = mean_abs_T / (1.0 + float(k))
        rows.append({"k": float(k), "lfde_value": lfde_val})

    df = pd.DataFrame(rows)
    return df
