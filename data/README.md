# Data layout för SCE–ECS Tier-3 LFDE-tester

Denna mapp innehåller inga riktiga datafiler i repo:t.

Varje extern testare ansvarar för att:

1. Ladda ner dataset från officiella källor (t.ex. HIT, WMAP, Planck PR4, egna simuleringar).
2. Placera dem i en lämplig undermapp här, t.ex.:

```text
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
