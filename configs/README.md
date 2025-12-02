# Configs för SCE–ECS Tier-3 LFDE-tester

Varje YAML-fil i denna mapp definierar **ett dataset** och tillhörande LFDE-test.

Koden (`src/`, `scripts/`) är densamma för alla dataset.  
Endast:

- vilken data som läses
- hur filerna tolkas
- vilka resultatfilnamn som används

styrs via config.

---

## 1. Obligatoriska fält

Varje config *måste* innehålla:

```yaml
dataset: "NamnPåDataset"
domain: "turbulence"   # eller "cmb"

data_root: "data/HIT"  # eller "data/WMAP", "data/Planck_pr4", eller egen mapp

files:
  ...                   # filnamn relativt data_root

metadata:
  ...                   # tolkning av filerna (grid, nside, frekvens m.m.)

lfde:
  ks_values: [...]      # lista av diskreta vågtal/skalfaktorer
  output_csv: "results/..."
  output_plot: "results/..."
