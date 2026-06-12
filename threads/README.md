# Threads

Reference multi-card sequences for the minimal terminal card style.

Thread mode is not the default. Use it only when one PNG would become cramped or unreadable.

## Included

- `proof-over-confidence/` — V1.3 reference thread showing hook → model → ownership → checklist

## Workflow

```bash
python3 ../scripts/minimal_card.py render-dir proof-over-confidence
python3 ../scripts/minimal_card.py contact-sheet \
  --dir proof-over-confidence \
  --out proof-over-confidence/thread-contact-sheet.svg \
  --title "proof over confidence thread"
python3 ../scripts/minimal_card.py render proof-over-confidence/thread-contact-sheet.svg
python3 ../scripts/minimal_card.py validate proof-over-confidence/*.svg proof-over-confidence/*.png
```
