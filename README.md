# My Slidev Template

A reusable [Slidev](https://sli.dev) presentation template with custom layouts, Chart.js components, and Tailscale Funnel dev server support.

[![Use this template](https://img.shields.io/badge/Use%20this%20template-green?style=for-the-badge)](https://github.com/htlin222/my-slidev-template/generate)

## Quick Start

Click **"Use this template"** on GitHub to create a new repo, then:

```bash
pnpm install
pnpm dev
```

The dev server starts at `http://localhost:3030`.

## Features

- **Custom layouts** — `my-cover`, `chapter`, `default`
- **Chart.js components** — Bar, Doughnut, Line, Pie, Radar (via `vue-chartjs`)
- **Lucide icons** — `lucide-vue-next` for inline SVG icons
- **PDF export** — `pnpm export`
- **Tailscale Funnel** — serve over HTTPS with `tailscale funnel --set-path=/<path> 3030`

## Project Structure

```
├── components/       # Vue components (charts, etc.)
├── layouts/          # Custom Slidev layouts
├── public/           # Static assets (images, fonts)
├── setup/            # Vite plugins & code runners
├── styles/           # Global CSS
├── util/             # Helper scripts
├── slides.md         # Presentation content
└── vite.config.ts    # Vite configuration
```

## Usage

1. Edit `slides.md` with your presentation content
2. Update frontmatter fields (`title`, `seriesName`, `date`, `author`, `affiliation`)
3. Place images in `public/`
4. Run `pnpm dev` to preview, `pnpm build` to build, `pnpm export` to export PDF

## Configuration

- `vite.config.ts` — set `base` path and allowed hosts for Tailscale Funnel
- `styles/index.css` — global styling overrides
- `setup/vite-plugins.ts` — custom Vite plugins

## License

ISC
