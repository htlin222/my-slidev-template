# IMS-IMWG 2025 Slidev Project

## Dev Server

- `vite.config.ts` reads `SLIDEV_BASE` env var for base path (defaults to `/`)
- For Tailscale Funnel: set `SLIDEV_BASE=/<project-name>/` and run `tailscale funnel --set-path=/<project-name> 3030`
- `vite.config.ts`: `server.allowedHosts` includes the Tailscale hostname
- `NODE_OPTIONS='--dns-result-order=ipv4first'` in the dev script forces IPv4 binding (Node/Vite defaults to IPv6 `[::1]` which Tailscale Funnel can't reach)
- `pnpm presenter` enables multi-device sync via WebSocket (`--remote` flag); presenter view at `/presenter` route

## Large-File Editing Strategy (slides.md)

`slides.md` is 886+ lines. Never rewrite it in one shot. Use segmented subagent workflow:

### Workflow

1. **Segment**: Split the target section(s) into temp files under `/tmp/<project-name>/partNN.md` (e.g., `part01.md`, `part02.md`, …)
2. **Delegate**: Spawn Task subagents per segment — each agent edits only its own part file
3. **Research**: Subagents use `WebSearch` / `WebFetch` to find evidence-based data (trial results, survival stats, guidelines)
4. **Cite (AMA + DOI)**: All references must use AMA citation format with DOI. Validate DOIs via `https://api.crossref.org/works/{DOI}` before including
5. **Aggregate**: Once all subagents complete, read each part file in order and apply edits back into `slides.md` using `Edit` (not full rewrite)
6. **Cleanup**: Remove temp files after successful aggregation

### AMA Citation Format

```
AuthorLastname Initials, … Title. *Journal*. Year;Vol(Issue):Pages. doi:10.xxxx/xxxxx
```

### DOI Validation

```bash
# Returns 200 + metadata if valid
curl -s -o /dev/null -w "%{http_code}" "https://api.crossref.org/works/10.1234/example"
```

### Rules

- Each subagent receives: section boundaries (slide `---` delimiters), context of adjacent slides, and the research brief
- Subagents must NOT modify content outside their assigned section
- Prefer `Edit` over `Write` when touching `slides.md` — surgical changes only
- Temp dir: `/tmp/<project-name>/` (derive from repo directory name; create if not exists)

## Slide Density Limits

- Single-column slide: max 8 bullets, OR 1 table + max 3 bullets
- Two-column layout: max 5 items per column
- If content exceeds these limits, split into multiple slides upfront — do not pack a slide full then split later

## Mermaid Diagrams

- Always use `neutral` theme with main teal color `#3D6869`
- Keep diagrams compact: max 5 columns and 5 rows
- If a diagram exceeds this, simplify or split into multiple diagrams

```
%%{init: {'theme': 'neutral', 'themeVariables': {'primaryColor': '#3D6869'}}}%%
```

## Formatting

- Use `<!-- prettier-ignore -->` before markdown tables inside HTML `<div>` containers to prevent prettier from breaking table alignment in two-column layouts
