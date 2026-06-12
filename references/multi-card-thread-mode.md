# Multi-card Thread Mode

Use when one idea is too large for one terminal card without cramming.

The default output is still **one PNG**. Thread mode is an escape hatch for ideas that would become unreadable, not a replacement for the normal single-card workflow.

## Decision Gate

Try a single card first when:

- the idea has one thesis
- it fits 3-6 sections, boxes, rows, or nodes
- the card can stay readable at normal font sizes
- the user wants one portable context artifact

Split into a thread only when:

- the card needs paragraph text
- the idea has more than 6 modules/nodes
- the idea naturally has an arc: hook → model → proof → takeaway
- the user explicitly asks for a thread or carousel
- the single-card layout would require tiny text, dense arrows, or overloaded boxes

If unsure, make the single-card version first. Thread mode should justify itself.

## Thread Shape

A good thread is not just several cards. It has a sequence arc:

```text
01 hook       catch attention / establish thesis
02 model      explain the mechanism
03 proof      show ownership, evidence, or examples
04 takeaway   give checklist/rule/action
```

Each card should have:

- same monochrome terminal visual lane
- same title family and footer
- visible sequence marker: `01/04`, `02/04`, etc.
- one job per card
- a layout chosen for that card's information shape

## Example

Topic: why automated work needs verification, not confidence.

### Card 01/04 — Hook

Layout: `comparison`

```text
Title: proof beats confidence

CONFIDENCE          PROOF
sounds right        command output
probably fixed      regression test
agent said done     verified artifact
looks okay          inspected result

Rule: Trust starts when claims become checkable.
```

### Card 02/04 — Model

Layout: `linear-process`

```text
Title: the trust loop

01 inspect     understand current state
02 act         make the smallest useful change
03 verify      run the real check
04 report      show evidence, not vibes

Rule: The loop is only complete after verification.
```

### Card 03/04 — Ownership

Layout: `matrix`

```text
Title: who owns what

ROLE       OWNS             RETURNS
planner    scope            decision
builder    implementation   artifact
reviewer   risk             findings
operator   release          status

Rule: Unowned work becomes unverified work.
```

### Card 04/04 — Takeaway

Layout: `bento-field-note`

```text
Title: before you say done

artifact exists   not just a plan
command ran       not just assumed
output checked    not just skimmed
edge case seen    not just happy path
source preserved  not just screenshot
claim matches     not just confidence

Rule: Done means demonstrated.
```

## File Shape

```text
threads/<slug>/
  <slug>-01-hook.svg/png
  <slug>-02-model.svg/png
  <slug>-03-proof.svg/png
  <slug>-04-takeaway.svg/png
  thread-manifest.md
  thread-contact-sheet.svg/png
```

## CLI Workflow

```bash
python3 scripts/minimal_card.py render-dir threads/<slug>
python3 scripts/minimal_card.py contact-sheet \
  --dir threads/<slug> \
  --out threads/<slug>/thread-contact-sheet.svg \
  --title "<thread title>" \
  --subtitle "4 cards · hook → model → proof → takeaway"
python3 scripts/minimal_card.py render threads/<slug>/thread-contact-sheet.svg
python3 scripts/minimal_card.py validate threads/<slug>/*.svg threads/<slug>/*.png
```

## Reference Implementation

V1.3 includes a rendered reference thread:

```text
threads/proof-over-confidence/
```

Use it as the style and file-structure reference for future thread mode work.
