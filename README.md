# sce-ecs-tests
Constitution-compliant test suite for SCE–ECS  automated LFDE reciprocity, geometry–deviation coupling and uni-phasal scaling tests for HIT, WMAP and Planck PR4 datasets.
# SCE–ECS Tier-3 Testbed for LFDE-Reciprocity

Detta repository är den officiella Tier-3 testbädden för oberoende tester
av LFDE-reciprocitet enligt SCE–ECS/UFT-ramverket.

Designprinciper:

- **Parameterfritt**: ingen kontinuerlig tuning i koden.
- **Datamängdsagnostiskt**: samma LFDE-avatar och metrik används för alla datasets.
- **Config-styrt**: all information om data anges i YAML-filer i `configs/`.
- **Reproducerbart**: kan köras direkt i Google Colab.
- **Transparent**: inga dolda parametrar – alla diskreta val är explicita.

---

## 1. Struktur

```text
sce-ecs-tests/
  configs/
    README.md
    turbulence_hit.yaml           # Exempelkonfig för HIT
    template_turbulence.yaml      # Mall för egen turbulensdata
    template_cmb_wmap.yaml        # Mall för WMAP-liknande CMB-data
    template_cmb_planck_pr4.yaml  # Mall för Planck PR4-liknande CMB-data
  data/
    HIT/
      raw/
      processed/
    WMAP/
      raw/
      processed/
    Planck_pr4/
      raw/
      processed/
    README.md                     # Instruktioner för data-layout
  notebooks/
    01_turbulence_lfde_colab.ipynb  # Colab-notebook (skapas via Colab)
  results/
    sample_runs/
    user_submitted_runs/
  scripts/
    lfde_reciprocity/
      run_lfde_sweep.py
  src/
    sceecs_tests/
      __init__.py
      config.py
    metrics/
      __init__.py
      lfde_reciprocity.py
  README.md
  requirements.txt

## Notebooks (Google Colab entry points)

Följande notebooks finns under `notebooks/` som färdiga Tier-3 ingångar:

- `01_turbulence_lfde_colab.ipynb`  
  Kör LFDE-reciprocitetstestet på en HIT-liknande turbulensdataset
  via `configs/turbulence_hit.yaml`.

- `02_wmap_lfde_colab.ipynb`  
  Kör den CMB-specifika LFDE-pipelinen på en WMAP W-band T/Q/U-dataset
  via `configs/wmap_wband_TQU.yaml`.
  Kräver att användaren placerar WMAP-FITS-filer i `data/WMAP/...` enligt config.

- `03_planck_pr4_lfde_colab.ipynb`  
  Kör samma CMB-pipeline på en Planck PR4 SMICA T/Q/U-dataset
  via `configs/planck_pr4_smica_TQU.yaml`.
  Kräver att användaren placerar Planck PR4-FITS-filer i `data/Planck_pr4/...` enligt config.

