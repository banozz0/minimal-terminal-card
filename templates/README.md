# Templates

Reusable SVG templates for the minimal terminal card style.

## Files

- `base-card.svg` — shared base shell + placeholders
- `comparison.svg` — A/B contrast layout
- `loop.svg` — circular/compounding flow layout
- `matrix.svg` — responsibility/capability table layout
- `hub-spoke.svg` — central concept with surrounding modules layout
- `agency-map.svg` — org/team operating model layout
- `linear-process.svg` — step-by-step workflow layout
- `dense-field-note.svg` — compact field-note / schedule layout
- `timeline.svg` — four-checkpoint roadmap layout
- `stack.svg` — layered system / hierarchy layout
- `funnel.svg` — triage, filtering, and selection layout
- `bento-field-note.svg` — six peer notes / principles layout

## Workflow

1. Copy the closest template to the target output path.
2. Replace placeholders like `{{TITLE}}`, `{{SUBTITLE}}`, and layout-specific tokens.
3. Render:

```bash
python3 ../scripts/minimal_card.py render ../examples/example-name.svg
```

4. Validate:

```bash
python3 ../scripts/minimal_card.py validate ../examples/example-name.svg ../examples/example-name.png
```

5. Visually QA the rendered PNG before sending or publishing.

## Guardrails

- Keep SVG/PNG square at `1600x1600` unless explicitly requested otherwise.
- Keep font sizes at `17px` or higher.
- Keep most text nodes under 56 characters.
- Use no more than 95 text nodes per card; split when the idea exceeds that.
- Preserve the monochrome terminal aesthetic: black, off-white, gray, thin lines.
