# Proof Over Confidence — Example Thread

This is the V1.3 reference thread for multi-card mode.

Use this mode only when a single PNG would become cramped. The default remains one card.

## Arc

- `01-hook` — establish the thesis with a comparison
- `02-model` — explain the operating loop
- `03-ownership` — show who owns which proof
- `04-checklist` — end with a reusable takeaway

## Files

- `proof-over-confidence-01-hook.svg/png`
- `proof-over-confidence-02-model.svg/png`
- `proof-over-confidence-03-ownership.svg/png`
- `proof-over-confidence-04-checklist.svg/png`
- `thread-contact-sheet.svg/png`

## Render

```bash
python3 ../../scripts/minimal_card.py render-dir .
python3 ../../scripts/minimal_card.py contact-sheet --dir . --out thread-contact-sheet.svg --title "proof over confidence thread" --subtitle "4 cards · hook → model → ownership → checklist"
python3 ../../scripts/minimal_card.py render thread-contact-sheet.svg
python3 ../../scripts/minimal_card.py validate *.svg *.png
```
