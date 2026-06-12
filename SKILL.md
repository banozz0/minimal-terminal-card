---
name: minimal-terminal-card
description: Use when turning a conversation excerpt, idea, prompt, note, or topic into a minimal black-and-white terminal screenshot card for X/Twitter. Extracts the core idea first, chooses a layout based on information shape, generates deterministic SVG/PNG, and visually verifies the result.
version: 1.3.0
author: Hermes Agent
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [visual, terminal-card, svg, twitter, infographic, conversation-artifact]
    related_skills: [architecture-diagram, baoyu-infographic]
---

# Minimal Terminal Card

## Overview

Create crisp, minimal black-and-white terminal-style image cards from either:

1. **Conversation context** — the user says something like “save this part as a terminal card” or “turn what we just discussed into a card”.
2. **A direct prompt/topic** — the user gives a topic, thesis, note, or content brief.

This is **not just an image-generation style**. The skill owns the full workflow:

```
conversation / prompt → idea extraction → content compression → layout choice → SVG → PNG → visual QA
```

The output should feel like a clean screenshot from a technical terminal manual: sparse, intentional, monochrome, and diagrammatic.

Use deterministic SVG/HTML rendering rather than normal AI image generation so text remains crisp, spellable, aligned, and editable.

## When to Use

Use this skill when the user asks for:

- “terminal card”
- “X/Twitter image in that screenshot style”
- “save this as a card”
- “turn this conversation/topic into a visual card”
- “make this into the minimal black/white diagram style”
- “use the terminal screenshot layout/style”
- reusable visual cards based on an idea, insight, workflow, or comparison

Do **not** use this for:

- photorealistic images
- colorful infographics
- posters with gradients/glow
- long-form documents
- charts that require real data plotting unless the data is provided and verified
- precise corporate brand graphics unless the user provides brand constraints

## Core Principle

The card should preserve the **idea**, not necessarily every word.

If the source is a conversation, extract the useful concept and compress it into card-friendly language. Do not dump raw chat text into the image.

Good card content is:

- short
- high-signal
- structured
- visually scannable
- suited to one clear layout

Bad card content is:

- paragraph-heavy
- full of caveats
- too many arrows
- too many boxes
- trying to say everything

## Inputs

### Input Mode A — Conversation Extraction

Triggered by requests like:

> “Save this part of the conversation about X as a terminal card.”

Workflow:

1. Identify the relevant discussion in the active context.
2. If the user references an earlier session or “that thing we talked about before”, use `session_search` before asking them to repeat it.
3. Extract:
   - central thesis
   - supporting points
   - useful contrast/loop/structure
   - any wording worth preserving
4. Compress into visual-card content.
5. Choose the layout that fits the information shape.
6. Generate SVG + PNG.
7. QA visually before sending.

### Input Mode B — Direct Prompt / Topic

Triggered by requests like:

> “Make a terminal card about why agents need memory.”

Workflow:

1. Interpret the topic.
2. Draft a concise thesis and supporting structure.
3. Choose the best layout.
4. Generate SVG + PNG.
5. QA visually before sending.

If the topic requires factual claims, current facts, market data, prices, dates, schedules, fixtures, or research-backed claims, use the appropriate research/web tool first. Do not invent data. If the output involves time zones, perform conversion with a real tool/library and state the target timezone on the card.

## Style Rules — Strict Default

Default style is the **minimal screenshot lane**.

Required:

- canvas: square `1600x1600` by default
- background: near-black `#050505`
- primary text: off-white `#eeeeee`
- muted text: gray `#9a9a9a`
- dim labels: gray `#626262`
- font: monospace, preferably `SF Mono`, `Berkeley Mono`, `JetBrains Mono`, `IBM Plex Mono`, Menlo, Consolas fallback
- terminal-window frame with small dot controls
- thin rectangular boxes
- thin arrows/lines
- generous whitespace
- concise labels
- SVG source preserved
- PNG export verified visually

Forbidden unless the user explicitly asks:

- color accents
- gradients
- glow
- decorative grids
- 3D/isometric effects
- emoji
- icons that break the terminal aesthetic
- dense paragraph blocks
- AI-image generation for text-heavy cards
- over-designed SaaS poster aesthetic

## Layout Selection

Pick layout by **information shape**, inspired by infographic layout systems but constrained to the minimal terminal style.

### `comparison`

Use for A/B contrasts:

- bad vs good agents
- before vs after
- manual vs automated
- wrong way vs right way
- options/tradeoffs

Structure:

```
LEFT: wrong / old / weak
RIGHT: right / new / strong
rows: 3-5 paired contrasts
bottom rule: one sentence
```

### `loop`

Use for recurring systems and compounding processes:

- memory flywheels
- verification loops
- operating rhythms
- learning cycles

Structure:

```
5-6 nodes around center concept
orthogonal or very clean circular routing
central thesis
bottom rule
```

Important: loop arrows must be especially clean. Prefer right-angle/orthogonal routing over messy curves.

### `matrix`

Use for responsibility/capability maps:

- agent ownership
- model/tool selection
- role → responsibility → output
- feature comparison

Structure:

```
columns: entity / owns / returns
rows: 4-6 max
minimal table grid
bottom rule
```

### `hub-spoke`

Use for central platform/ecosystem ideas:

- command center / central interface
- central interface with specialist capabilities
- one concept connected to surrounding modules

Structure:

```
central box
4-6 surrounding boxes
spokes must stop before boxes
outer panel must not collide with dividers
```

### `agency-map`

Use for org charts and multi-agent setups:

- user → CEO/interface → specialists
- AI agency structure
- operating model
- chain of responsibility

Structure:

```
user / principal at top
CEO/interface below
specialists below
optional analyst/reviewer layer
clean delegation + return/proof paths
```

### `linear-process`

Use for step-by-step workflows:

- inspect → decide → act → verify
- tutorial steps
- pipelines
- sequential operating procedures

Structure:

```
numbered steps left-to-right or top-to-bottom
one short label + one short explanation per step
simple arrows, no crossing
```

### `stack`

Use for layered systems:

- architecture layers
- priority levels
- responsibility hierarchy
- mental models with foundations

Structure:

```
top layer = user-facing outcome
middle layers = agents/tools/memory
bottom layer = runtime/foundation
```

### `funnel`

Use for narrowing many options into one decision or proof:

- idea triage
- prioritization
- option filtering
- noisy input → focused output
- selection processes

Structure:

```
wide top rectangle: many options / raw input
middle rectangle: constraints / filter
narrow bottom rectangle: chosen test / output
simple vertical arrows
optional side guide: MANY → FEWER → PROOF
```

Important: avoid angled trapezoid funnels by default. They tend to look like generic slideware and clash with the terminal-card aesthetic. Prefer a stepped narrowing filter stack made of rectangles.

### `bento-field-note`

Use for multiple related notes that do not form a sequence:

- principles
- rules
- compact manifestos
- topic overviews

Structure:

```
4-6 modules/cards
no heavy arrows
each module one idea
```

### `dense-schedule`

Use for dated lists with many items:

- sports fixtures
- event schedules
- conference agendas
- release calendars
- deadline lists

Structure:

```
two-column stack of date boxes
each box: DAY DD MMM + time/item rows
footer: date window + source/timezone note
```

Important: schedule/date boxes must use **dynamic height based on item count**. Do not use fixed-height boxes when days have uneven numbers of rows. See `references/dense-schedule-cards.md`.

## Templates and Examples

V1.2 ships with reusable layout templates, a generic approved example gallery, guardrails, and a small helper CLI.

Templates (editable and renderable) live under the skill directory:

```text
templates/base-card.svg
templates/comparison.svg
templates/loop.svg
templates/matrix.svg
templates/hub-spoke.svg
templates/agency-map.svg
templates/linear-process.svg
templates/dense-field-note.svg
templates/timeline.svg
templates/stack.svg
templates/funnel.svg
templates/bento-field-note.svg
```

Approved examples live under:

```text
examples/comparison-proof-vs-confidence.svg/png
examples/loop-knowledge-compounds.svg/png
examples/matrix-team-ownership.svg/png
examples/dense-conference-agenda.svg/png
examples/timeline-release-checkpoints.svg/png
examples/stack-product-layers.svg/png
examples/funnel-idea-to-signal.svg/png
examples/bento-operating-principles.svg/png
examples/example-contact-sheet.svg/png
```

Workflow:

1. Choose the best-matching template based on information shape.
2. Copy the template to the output location.
3. Replace placeholder text like `{{TITLE}}`, `{{SUBTITLE}}`, and layout-specific placeholders.
4. Export to PNG and visually QA the rendered PNG.

This is explicitly **not** an AI image-generation skill. The primary work is idea extraction and layout choice, not styling from scratch each time.

## Portability

Although this is packaged as a Hermes skill, the repo is plain markdown, SVG templates, examples, references, and a small Python helper script.

Primary usage is as a Hermes skill. Secondary usage is manual or file-tool usage: read `SKILL.md`, copy a template, render with `scripts/minimal_card.py`, and validate the SVG/PNG.

Keep public docs generic and stable. Avoid naming specific third-party agents unless there is a concrete integration to document.

## Content Compression Rules

Before drawing, create a mini content plan:

```text
Topic:
Thesis:
Layout:
Title:
Subtitle:
Sections / nodes:
Bottom rule:
```

Card copy guidelines:

- title: 2-6 words preferred
- subtitle: one line if possible
- node labels: 1-3 words
- node sublabels: 1-5 words
- body lines: short enough to avoid overflow
- bottom rule: one memorable sentence

If the conversation has many good points, select the strongest 3-6. Do not cram everything in.

## Diagram and Arrow Rules

This style succeeds or fails on clean geometry.

Rules:

- arrows must not pass through boxes
- arrowheads should stop a small gap before target boxes instead of touching borders
- duplicate arrows pointing in the same direction should be removed unless semantically intentional
- return flows should use separate outer rails or dashed paths
- avoid diagonal lines unless they are visually cleaner than orthogonal lines
- prefer right-angle routing for flowcharts
- no arrow should collide with text
- no outer panel should collide with bottom dividers or footer rules
- if an arrow route looks “auto-generated”, redraw it manually

## Public Repo Hardening

When the card/template/example set is meant for a public GitHub repo, scrub it before calling it ready:

- replace personal names, handles, named agents, private system labels, and internal architecture terms with generic role names
- replace event-specific reference examples unless the event is intentionally part of the public sample
- keep examples reusable across domains: product, schedule, roadmap, decision, principles, ownership, process
- search docs, templates, examples, scripts, and contact sheets for stale private/event-specific terms
- regenerate all PNGs and the contact sheet after renaming/replacing examples
- validate both SVG and PNG outputs with the helper CLI, then visually QA the contact sheet

This is especially important when examples started as user-specific working artifacts. The final public skill should read as a reusable visual system, not a snapshot of one person's setup.

## Output Files

Default location:

```text
./terminal-cards/<slug>.svg
./terminal-cards/<slug>.png
```

For layout experiments:

```text
./terminal-layout-cards/<layout>.svg
./terminal-layout-cards/<layout>.png
```

Always preserve the SVG source. The SVG is the editable artifact; the PNG is the shareable artifact.

## Helper CLI

V1.3 includes a small helper under `scripts/`:

```bash
python3 scripts/minimal_card.py list-templates
python3 scripts/minimal_card.py render examples/comparison-proof-vs-confidence.svg
python3 scripts/minimal_card.py render-dir threads/proof-over-confidence
python3 scripts/minimal_card.py contact-sheet --dir examples
python3 scripts/minimal_card.py validate
```

The renderer tries macOS `qlmanage`, then `rsvg-convert`, then `inkscape`.

## Mobile Readability Guardrails

Use these limits before rendering:

- minimum font size: `17px`
- preferred body text: `20-24px`
- max text node length: roughly 56 characters
- max text nodes per card: 95
- safe outer margin: 92px or more
- max rows per table/matrix: 6 unless the layout is specifically dense
- max boxes/nodes in normal cards: 6
- split to two cards when the card needs paragraph text, more than 6 modules, or more than 95 text nodes

These are guardrails, not substitutes for visual QA.

## Multi-card Thread Mode

Default to **one PNG** whenever the idea fits. The whole point of the skill is to preserve a compact context artifact, so thread mode is only for ideas that would become cramped or unreadable as one card.

Use thread mode when:

- the concept needs a sequence: hook → model → proof → takeaway
- one card would need paragraph text or tiny fonts
- there are more than 6 modules/nodes
- the user explicitly asks for a thread/carousel

Do not use thread mode just because it looks cool. If one card works, one card wins.

Each thread card should share the same visual lane, footer, title family, and a visible sequence marker such as `01/04`. Choose the best layout per card rather than forcing every card into the same template.

V1.3 includes a rendered reference thread under:

```text
threads/proof-over-confidence/
```

See `references/multi-card-thread-mode.md` for the decision gate, example arc, file structure, and CLI workflow.

## Export Workflow

On macOS, Quick Look can render SVG to PNG:

```bash
qlmanage -t -s 1600 -o /path/to/output /path/to/card.svg
cp /path/to/output/card.svg.png /path/to/output/card.png
```

If using a different renderer later, keep the same requirement: exported PNG must be `1600x1600` unless the user asks for another aspect ratio.

## Verification Before Sending

After export, use visual inspection (`vision_analyze`) before claiming the card is ready.

Checklist:

- [ ] PNG exists and is `1600x1600`
- [ ] full card visible, no accidental crop
- [ ] no text overflow
- [ ] no clipping
- [ ] title/subtitle readable on mobile
- [ ] diagram labels readable
- [ ] arrows do not cross boxes
- [ ] arrowheads stop before boxes
- [ ] outer panels do not touch dividers/footers
- [ ] style remains black/white/gray minimal screenshot lane
- [ ] if factual/current data is used, source and date/time context are noted
- [ ] if times are shown, timezone conversion was done with a tool/library and the target timezone is visible
- [ ] if using schedule/date boxes, each box height fits its row count
- [ ] SVG source preserved

If QA finds issues, patch the SVG, re-export, and QA again.

## Example Requests

Conversation-based:

> “This part about agents needing proof over confidence is good. Save it as a terminal card.”

Expected behavior:

- Extract thesis: proof beats confidence
- Likely layout: `comparison` or `linear-process`
- Create card with bad/good contrast or inspect→verify flow

Prompt-based:

> “Make a terminal card about a multi-agent team setup.”

Expected behavior:

- Choose `agency-map` or `matrix`
- Show user → operator/interface → specialists
- Use short role labels and proof/ownership framing

Prompt-based with layout:

> “Make a loop card about how knowledge compounds.”

Expected behavior:

- Use `loop`
- Nodes like capture, extract, verify, store, retrieve, improve
- Keep arrows clean and orthogonal

Prompt-based tests created during V1.1:

> “Make a terminal card about why agents need verification.”

Output:

- `tests/verification-needed.svg`
- `tests/verification-needed.png`
- Layout: `linear-process`
- Thesis: inspection → action → verification → reporting is the source of trust

> “Make a terminal card comparing a solo AI assistant vs a multi-agent system.”

Output:

- `tests/solo-vs-multi-agent.svg`
- `tests/solo-vs-multi-agent.png`
- Layout: `comparison`
- Thesis: multi-agent wins on ownership and leverage when handoffs are clean

> “Make a terminal card showing an agent ownership model.”

Output (reused approved matrix example):

- `tests/agent-ownership-model.svg`
- `tests/agent-ownership-model.png`
- Layout: `matrix`
- Thesis: agent value comes from clear ownership, work type, and proof output

## Common Pitfalls

1. **Treating this as pure image generation.** Wrong. The main job is extracting/structuring the idea before drawing.
2. **Overstuffing.** If every insight goes on the card, the card gets worse.
3. **Style drift.** Glow, gradients, colors, and grids turn this into a different product.
4. **Bad arrow routing.** Clean terminal cards require hand-placed arrows.
5. **Text inside boxes too long.** Shorten labels before resizing everything.
6. **Skipping QA.** Always inspect the rendered PNG, not just the SVG text.
7. **Destroying editability.** Always keep the `.svg`.
8. **Using stale conversation context.** If the user references an older discussion, retrieve it with `session_search` instead of guessing.
9. **Fixed-height schedule boxes.** Dense schedules with uneven daily item counts will overflow unless box height is calculated from row count.
10. **Unverified timezone math.** For fixture/event cards, convert with a real timezone library/tool and show the target timezone on the card.
11. **Redesigning from scratch every time.** V1.1 exists so future cards reuse templates and examples instead of re-deriving geometry.
12. **Confusing prompts and conversation extraction.** For prompt mode, draft structure explicitly; for conversation mode, preserve the core idea rather than copying raw chat text.
13. **Publishing private examples.** If the user wants to upload the skill or examples publicly, genericize names, roles, events, handles, and system-specific references before publishing.
14. **Slideware funnel shapes.** Angled trapezoid funnels often look worse than the rest of the pack. Use a stepped rectangular filter stack unless the user explicitly wants classic funnel geometry.
15. **Over-documenting other-agent usage.** Keep public docs generic and stable unless there is a concrete integration to support.
16. **Using thread mode by default.** The default remains one PNG. Split only when the idea would become cramped, tiny, or sequence-dependent.

## Lessons Learned from V1.1 Tests

From the V1.1 prompt tests:

- Comparison cards are the fastest and cleanest layout to generate consistently.
- Linear-process cards work well for operational theses like “agents need verification”.
- The matrix layout is the strongest reusable layout for ownership explanations.
- Approved templates reduce most styling mistakes, but arrow routing and box collision issues still require visual QA on the rendered PNG.
- Dense schedules still break if box height is not calculated dynamically from row count.
- The skill improves most when the workflow is treated as idea extraction first, diagram generation second.

## Acceptance Standard

A successful terminal card should feel like:

> “A clean black-and-white technical screenshot artifact that captured the strongest idea from the conversation.”

Not:

> “An infographic poster that happens to use monospace text.”

## V1.1 Status

V1.1 is considered shipped. It includes:

- reusable per-layout templates
- approved example gallery
- tested prompt-mode output examples
- updated SKILL.md guidance

## V1.2 Status

V1.2 is considered shipped. It adds:

- generic dense schedule example replacing the event-specific fixture example
- new templates: `timeline`, `stack`, `funnel`, `bento-field-note`
- generic examples for each new V1.2 layout
- `scripts/minimal_card.py` for listing templates, rendering, validation, and contact sheet generation
- mobile-readability guardrails for font size, line length, row count, and split decisions
- publication cleanup through `examples/README.md` and `templates/README.md`

## V1.3 Status

V1.3 is considered shipped. It adds:

- multi-card thread mode with a single-card-first decision gate
- rendered reference thread under `threads/proof-over-confidence/`
- thread manifest and thread contact sheet examples
- helper CLI support for `render-dir` and directory-based contact sheets
- updated docs that keep public usage generic and avoid unnecessary integration-specific claims

Remaining before GitHub publishing:

- package as a standalone repo folder
- add top-level `README.md`, `LICENSE`, and `.gitignore`
- run final repo-level validation after packaging
- create/push the GitHub repo only after user approval
