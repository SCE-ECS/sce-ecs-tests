from pathlib import Path
from typing import Dict, Any

import numpy as np
import healpy as hp


def load_cmb_dataset(cfg: Dict[str, Any]) -> Dict[str, np.ndarray]:
    """
    Laddar ett CMB-dataset (WMAP/Planck-liknande) baserat på YAML-konfigurationen.

    Förväntad struktur i cfg:
      domain: "cmb"
      data_root: "data/WMAP" eller "data/Planck_pr4" etc.
      files:
        T_map: "raw/....fits"  (valfritt men starkt rekommenderat)
        Q_map: "raw/....fits"  (valfritt)
        U_map: "raw/....fits"  (valfritt)
      metadata:
        nside: <int>
        mask: "processed/...mask.fits" (valfritt)
        ... (övriga fält ignoreras av denna funktion)

    Returnerar en dict:
      {
        "T": np.ndarray eller None,
        "Q": np.ndarray eller None,
        "U": np.ndarray eller None,
        "mask": np.ndarray eller None,
        "nside": int
      }

    OBS: Denna funktion implementerar bara IO och grundläggande kontroll.
         Själva LFDE-metriken för CMB ligger i metrics.lfde_reciprocity.
    """
    if cfg.get("domain") != "cmb":
        raise ValueError(f"Expected domain 'cmb' in config, got: {cfg.get('domain')}")

    data_root = Path(cfg["data_root"])
    files = cfg.get("files", {})
    meta = cfg.get("metadata", {})

    nside = int(meta.get("nside", 0))
    if nside <= 0:
        raise ValueError("metadata.nside måste vara satt till ett positivt heltal för CMB-dataset.")

    def _read_map_if_present(key: str):
        if key not in files:
            return None
        path = data_root / files[key]
        if not path.exists():
            raise FileNotFoundError(f"CMB-fil saknas: {path}")
        return hp.read_map(path.as_posix(), verbose=False)

    T = _read_map_if_present("T_map")
    Q = _read_map_if_present("Q_map")
    U = _read_map_if_present("U_map")

    # Mask är frivillig men starkt rekommenderad
    mask = None
    mask_name = meta.get("mask") or files.get("mask")
    if mask_name:
        mask_path = data_root / mask_name
        if not mask_path.exists():
            raise FileNotFoundError(f"CMB-maskfil saknas: {mask_path}")
        mask = hp.read_map(mask_path.as_posix(), verbose=False).astype(bool)

    return {
        "T": T,
        "Q": Q,
        "U": U,
        "mask": mask,
        "nside": nside,
    }
