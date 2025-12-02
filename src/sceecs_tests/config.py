from pathlib import Path
import yaml

def load_config(path):
    """
    Läs YAML-konfig och returnera som dict.
    Justerar data_root till absolut sökväg relativt repo-roten.

    Parameters
    ----------
    path : str or Path
        Sökväg till YAML-fil, t.ex. "configs/turbulence_hit.yaml".
    """
    path = Path(path).resolve()
    with path.open("r") as f:
        cfg = yaml.safe_load(f)

    # Antag: repo-root är två nivåer upp: .../configs/ -> repo-root
    repo_root = path.parents[1]

    if "data_root" in cfg:
        cfg["data_root"] = str((repo_root / cfg["data_root"]).resolve())

    return cfg
