# Anthologion

Deterministic Orthodox liturgical service assembler. Clone, install, run.
No AI is required at runtime.

## Sources

- **Services (source of truth):** St. Sergius PDFs — Full Menaion (`services/emenaion/`) for the twelve Great Feasts, General Menaion, Octoechos, Triodion, Pentecostarion.
- **Variable priority:** Full Menaion (great feasts) → General Menaion → ordinary Octoechos. Moveable books still apply outside those feasts.
- **Calendars:** `calendar=1` old (civil date − 13 days for the menaion), `calendar=0` new.

## No AI required to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_api.txt
python generate.py --date 2026-09-21 --calendar old
python api.py   # JSON/HTML/EPUB/PDF on port 5000
```

## Generate day or month packs

Output tree:

```
out/{old|new}/YYYY/MM/DD/day.{md,html,epub,pdf}
out/{old|new}/YYYY/MM/month.{md,html,epub,pdf}
```

```bash
python generate.py --date 2026-09-21 --calendar old --formats md,html,epub
python generate.py --date 2026-09-08 --calendar new --formats md,html,epub
python generate.py --month 2026-09 --calendar old --formats md,epub --services vespers
```

PDF needs weasyprint plus its system libraries (cairo/pango). Markdown, HTML, and EPUB do not.

## API

```
GET /api/resolve?m=9&d=21&y=2026&calendar=1
GET /api/resolve?m=9&d=21&y=2026&service=vespers&format=html&calendar=1
GET /api/resolve?m=9&d=21&y=2026&format=epub&scope=day&calendar=1
GET /api/resolve?m=9&y=2026&format=epub&scope=month&calendar=1
GET /api/paschalion?m=4&d=12&y=2026
```

`calendar`: `1` old (default), `0` new.

## Tests

```bash
pip install pytest
python -m pytest tests/ -q
```

## Destinations (later)

This repo builds artifacts. Later layers (not wired here): GitHub artifact mirror, Family Hub devotionals, manual X/Substack drafts. Input PDFs may be copyrighted — do not wide-redistribute until rights are clear.

## Honest gaps

- Full 366-day menaion is not extracted. The **nine fixed Great Feasts** use Full Menaion (`database/full_menaion_data.json`); other days use general saint-class templates, then octoechos.
- Palm Sunday, Ascension, and Pentecost remain in Triodion/Pentecostarion (moveable).
- Triodion/Pentecostarion vespers often arrive as truncated PDF blobs. Those are kept as source notes (`stichera_block`) and do **not** overwrite structured octoechos/menaion stichera.
- Pascha Sunday vespers is missing from pentecostarion file `10` (matins/liturgy only).
- Liturgy has no HTML template yet; JSON/Markdown still emit liturgy variables when present.
