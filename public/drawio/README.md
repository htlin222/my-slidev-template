# Draw.io Templates

Keep the editable source as `.drawio` and export a sibling `.svg` for Slidev.

```bash
drawio -x -f svg --svg-theme light -o public/drawio/trial-protocol.svg public/drawio/trial-protocol.drawio
drawio -x -f svg --svg-theme light -o public/drawio/flow-chart-template.svg public/drawio/flow-chart-template.drawio
```

Draw.io may still emit adaptive dark/light CSS in SVG output, which can invert colors in Slidev. After export, force the light color values:

```bash
perl -0pi -e 's/color-scheme:\s*light dark;/color-scheme: light;/g; s/light-dark\((#[0-9A-Fa-f]{3,8}),\s*#[0-9A-Fa-f]{3,8}\)/$1/g; s/light-dark\((#[0-9A-Fa-f]{3,8}),\s*var\(--ge-dark-color,\s*#[0-9A-Fa-f]{3,8}\)\)/$1/g; s/light-dark\((rgb\([^)]+\)),\s*rgb\([^)]+\)\)/$1/g' public/drawio/*.svg
```

Check the exported SVG before committing:

```bash
rg "light-dark|color-scheme: light dark" public/drawio/*.svg
pnpm build
```

Use the SVG in `slides.md`:

```html
<img
  src="/drawio/trial-protocol.svg"
  alt="Trial protocol Draw.io diagram"
  class="h-72 mx-auto mt-6"
/>
```

## Flow Chart Workflow

Use `trial-protocol.drawio` as the layout reference when creating new flow charts.
It exports tightly around the diagram and fits the Slidev page well.

Efficient setup:

1. Set the Draw.io page to `1600 x 560`.
2. Do not add a full-page white background rectangle. A fake canvas shape forces the SVG export to include a lot of empty padding.
3. Sketch the flow as rows and columns before drawing. For dense flow charts, target about four rows and five columns.
4. Keep nodes compact: use smaller font sizes, lower `spacing`, and rectangular nodes unless rounded corners are needed.
5. Place nodes on fixed lane centers. In the current flow template the lane centers are `70`, `188`, `306`, and `424`.
6. For one-to-many routing, do not fan out directly from a single node. Add a thin splitter bus and route from the bus to each lane with fixed `mxPoint` source and target points.
7. Export a temporary PNG and inspect it before committing the SVG:

```bash
drawio -x -f png --transparent -o /tmp/flow-chart-template.png public/drawio/flow-chart-template.drawio
```

Common mistakes to avoid:

- Do not preserve a 2:1 canvas just for aspect ratio. Let Draw.io crop to the real diagram bounds.
- Do not leave direct `Start -> Route A-D` edges when the start node fans out to multiple rows. Draw.io may choose diagonal elbows that look messy.
- Do not trust SVG export alone for routing quality. Check a PNG or Slidev preview when changing edge geometry.

## Templates

- `trial-protocol.drawio` / `trial-protocol.svg`: protocol diagram example.
- `flow-chart-template.drawio` / `flow-chart-template.svg`: light-theme left-to-right flow chart template matched to the trial diagram export layout.
