from pathlib import Path
import healpy as hp
import numpy as np

def load_cmb_dataset(cfg):
    """
    Laddar en WMAP/Planck-liknande CMB-dataset enligt config-filen.

    Returnerar en dict med keys: T, Q, U, mask, nside
    """
    data_root = Path(cfg["data_root"])
    files = cfg["files"]
    meta = cfg["metadata"]

    nside = int(meta["nside"])

    # Hjälpfunktion: läs karta om den finns
    def load_map(key):
        if key not in files:
            return None
        path = data_root / files[key]
        if not path.exists():
            raise FileNotFoundError(f"Filen hittades inte: {path}")
        return hp.read_map(path.as_posix(), verbose=False)

    # Läs T/Q/U
    T = load_map("T_map")
    Q = load_map("Q_map")
    U = load_map("U_map")

    # Läs mask om definierad
    mask = None
    if "mask" in meta:
        mask_path = data_root / meta["mask"]
        if not mask_path.exists():
            raise FileNotFoundError(f"Maskfil saknas: {mask_path}")
        mask = hp.read_map(mask_path.as_posix(), verbose=False).astype(bool)

    return {
        "T": T,
        "Q": Q,
        "U": U,
        "mask": mask,
        "nside": nside,
    }
