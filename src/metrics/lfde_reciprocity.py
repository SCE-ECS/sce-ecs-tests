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

def compute_lfde_reciprocity_cmb(cmb, ks):
    """
    En mycket enkel placeholder för CMB-versionen av LFDE-reciprocitet.
    Vi beräknar bara mean(|T|) / (1 + k) för att pipeline ska fungera.

    Detta ersätts senare med din riktiga LFDE-avatar för CMB.
    """

    T = cmb["T"]
    mask = cmb["mask"]

    if T is None:
        raise ValueError("CMB-dataset saknar T_map.")

    # Om mask finns: sätt masked pixlar till nan
    if mask is not None:
        T = T.copy()
        T[~mask] = np.nan

    mean_abs_T = np.nanmean(np.abs(T))

    rows = []
    for k in ks:
        lfde_val = mean_abs_T / (1 + float(k))
        rows.append({"k": float(k), "lfde_value": lfde_val})

    return pd.DataFrame(rows)
