# Dense Schedule / Fixture Cards

Guidance for making generic dense schedule cards in the minimal terminal style.

Use this reference when the user asks for a terminal card containing many dated items: sports fixtures, event schedules, release calendars, conference agendas, or deadline lists.

## Information Shape

This is **not** a flowchart. Use a dense field-note / schedule grid layout.

Good structure:

```text
Title: opening week fixtures
Subtitle: all times converted to Malta time · CEST / UTC+2
Two-column stack of date boxes
Each date box:
  DAY DD MMM
  HH:MM Team A v Team B
  HH:MM Team C v Team D
Footer:
  time window + source + timezone conversion note
```

## Workflow

1. Fetch or verify the schedule from current sources.
2. Identify the source timezone for kickoff times.
3. Convert into the requested timezone with a real timezone library/tool, not mental math.
4. Decide the date window explicitly:
   - User says “this week” → clarify only if the meaning changes output materially.
   - For international sports, late US kickoffs may land on the next Malta date. Make the displayed window clear.
5. Group matches by **local target date**, not by source-site date, if the user asked for Malta time.
6. Generate a dense two-column SVG layout.
7. Export PNG.
8. Visually QA.

## Layout Rules

- Use two columns for 6-10 date groups.
- Date boxes must have dynamic height based on item count.
- Do not use fixed-height boxes when days have uneven numbers of matches.
- Use a vertical stacking algorithm per column:

```text
col_y[col] starts at body_top
for each date group:
  height = header_height + row_height * item_count
  draw box at col_y[col]
  col_y[col] += height + gap
```

- Keep match names short enough for one line.
- Abbreviate only when needed for fit, and avoid ambiguous abbreviations.
- If full official country names overflow, use common short forms.

## QA Issues Caught

The first dense fixture render used fixed-height boxes. Days with 4-5 fixtures overflowed the box borders and collided with neighboring panels.

Fix:

- calculate box height from number of rows
- stack boxes dynamically within each column
- re-export and visually inspect again

## Copy Rules

- Header should identify the tournament/event and timezone.
- Footer should state sources and timezone conversion.
- Avoid decorative arrows; schedules usually do not need arrows.
- Use `layout/dense-field-note` or `layout/dense-schedule` as the footer label.

## Verification Checklist

- [ ] Source data was fetched/verified.
- [ ] Timezone conversion was done with a tool/library.
- [ ] Dates are grouped by requested target timezone.
- [ ] Every date box has enough height for its rows.
- [ ] No match row crosses a box border.
- [ ] No box collides with another box or footer divider.
- [ ] Source/timezone note is visible.
