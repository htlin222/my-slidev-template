---
theme: default
title: My Slidev Template
info: A compact, topic-neutral demo deck for the reusable Slidev template.
drawings:
  persist: false
transition: fade
mdc: true
colorSchema: light
layout: my-cover
seriesName: Template Demo
date: "2026-04-08"
author: 林協霆 Hsieh-Ting Lin
affiliation: ""
email: ""
---

# My Slidev Template

A minimal topic-neutral deck that demonstrates the template features.

---

# Basics

---

<script setup>
import { Image, Layers, ListChecks, Presentation, Table2 } from 'lucide-vue-next'
</script>

## Content Patterns

- <span class="icon-badge"><Presentation size="1em" /></span> **Cover and chapter layouts** keep the deck structure visible
- <span class="icon-badge"><Layers size="1em" /></span> **Top navigation** is generated from `h1` section slides
- <span class="icon-badge"><ListChecks size="1em" /></span> **Bold list keywords** receive the template badge treatment
- <span class="icon-badge"><Table2 size="1em" /></span> **Tables and callouts** use compact, high-contrast styling
- <span class="icon-badge"><Image size="1em" /></span> **Images and citations** keep visual material grounded

> This slide demonstrates icon badges, list styling, the bottom progress bar, and a callout block.

<cite>Template demo citation</cite>

---

## Tables, Images, and Diagrams

<div class="grid grid-cols-2 gap-8 items-center">
<div>

| Feature | Demo                   |
| ------- | ---------------------- |
| Table   | Compact rows           |
| Image   | Aspect ratio preserved |
| Mermaid | Centered diagram       |

<img
  src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 640 320'%3E%3Crect width='640' height='320' fill='%23ecedef'/%3E%3Ccircle cx='180' cy='160' r='80' fill='%233d6869' opacity='.9'/%3E%3Crect x='300' y='105' width='220' height='36' rx='8' fill='%233d6869'/%3E%3Crect x='300' y='164' width='160' height='24' rx='8' fill='%238fc1c0'/%3E%3C/svg%3E"
  alt="Generic placeholder graphic"
  class="h-36 mx-auto mt-4"
/>

</div>
<div>

```mermaid
%%{init: {'theme': 'neutral', 'themeVariables': {'primaryColor': '#3D6869'}}}%%
flowchart LR
  A[Cover] --> B[Content]
  B --> C[Data]
  C --> D[Share]
```

</div>
</div>

---

### Breadcrumb Example

This `h3` slide follows an `h2` slide, so the top overlay shows the parent heading for context.

<v-clicks>

- First reveal
- Second reveal
- Third reveal

</v-clicks>

---

# Data

---

## Trial Protocol

<img
  src="/drawio/trial-protocol.svg"
  alt="Trial protocol Draw.io diagram"
  class="w-full max-w-full mt-6"
/>

<cite>Source: public/drawio/trial-protocol.drawio</cite>

---

## Flow Chart Template

<img
  src="/drawio/flow-chart-template.svg"
  alt="Left-to-right Draw.io flow chart template"
  class="w-full max-w-full mt-2"
/>

<cite>Source: public/drawio/flow-chart-template.drawio</cite>

---

## Bar and Line Charts

<div class="grid grid-cols-2 gap-8 h-80">
<div>

<ChartBar
  :labels="['One', 'Two', 'Three']"
  :datasets="[{ label: 'Demo', data: [12, 19, 8] }]"
  title="Bar"
/>

</div>
<div>

<ChartLine
  :labels="['Q1', 'Q2', 'Q3', 'Q4']"
  :datasets="[{ label: 'Demo', data: [4, 9, 7, 12], fill: true }]"
  title="Line"
/>

</div>
</div>

---

## Pie, Doughnut, and Radar Charts

<div class="grid grid-cols-3 gap-4 h-72">
<div>

<ChartPie
  :labels="['A', 'B', 'C']"
  :data="[45, 30, 25]"
  title="Pie"
/>

</div>
<div>

<ChartDoughnut
  :labels="['Build', 'Review', 'Share']"
  :data="[50, 30, 20]"
  title="Doughnut"
/>

</div>
<div>

<ChartRadar
  :labels="['Clarity', 'Speed', 'Focus', 'Reuse']"
  :datasets="[{ label: 'Demo', data: [8, 7, 9, 8] }]"
  title="Radar"
/>

</div>
</div>

---

## Ready to Customize

- Replace the examples with your topic
- Keep `h1` slides for automatic chapters and navigation
- Use charts, images, tables, citations, and callouts only when they help the story

Thank you
