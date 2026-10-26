---
title: "Master Vault Map of Content (MOC)"
aliases:
  - Vault Index
  - Master MOC
tags:
  - moc
  - index
  - architecture
cssclasses:
  - wide-page
created: 2026-10-23
status: active
---
# :LiNetwork: Master Vault Map of Content (MOC)

> [!abstract]+ **Vault Topology & Architecture Overview**
> This Master Map of Content (MOC) aggregates and cross-links all **36+ nodes** identified in your Obsidian graph view. Your knowledge base resolves into three primary operational pillars: **Systems & Architecture** (`00`), **Content & Audience Engine** (`01`), and **Design & Vibe Coding Stack** (`02`). 

```button
name 🧠 Preview Note as Mind Map
type command
action Mind Map: Preview the current note as a Mind Map
color purple
```
^button-preview-mindmap

```button
name 📋 Open Companion Kanban
type command
action Kanban: Open board
color blue
```
^button-open-kanban

---

## :LiCpu: 1. Core Systems & Architecture Hub
- **[[00 - Laxman AI Systems Hub]]** — The root vertex of the entire vault, governing multi-agent setups.
- **[[Ai system]]** — Architectural notes and configurations for AI systems.
- **[[laxman_voice_profile_full]]** — Core voice identity, cadence calibration.

## :LiShare2: 2. Content Engine & Distribution
- **[[01 - Content Engine]]** — Central hub for social frameworks, viral mechanics.
- **[[LinkedIn_posts]]** — Repository of published and staged LinkedIn authority posts.
- **[[40-storytelling-hooks]]** — High-conversion narrative opening frameworks.
- **[[Hook template]]** — Reusable headline and visual opener formulas.
- **[[How a good post looks]]** — Anatomy of an authority post.
- **[[Anti AI writing knowledge base]]** — Heuristics, banned vocabulary.
- **[[GOOGLE SPARK]]** — System prompts for daily brief generation.

## :LiPalette: 3. Design System & Visual Assets
- **[[02 - Design and Build Stack]]** — Main operational stack coordinating visual UI.
- **[[DESIGN_SYSTEM]]** — Visual token specifications, typography pairings.
- **[[CANVA - CLAUDE AD PROMPTS]]** — Generative ad creative and layout generation.
- **[[30 free design resources]]** — Curated library of icons, mockups, vector packs.

## :LiCode: 4. Vibe Coding, Apps & Web Tools
- **[[Make an ai app (codex)]]** — Scaffolding AI applications using code generators.
- **[[10 new websites that will help you get more done in less time (3rd August, 2026 edition)]]** — High-leverage automation tools.
- **[[AI work CHeat sheet]]** — Rapid syntax, shortcut, and operator cheat sheet.
- **[[15 website make learning fun]]** — Interactive learning engines.
- **[[5 Projects That Teach You More Than Your Degree]]** — High-leverage portfolio projects.

## :LiFolderOpen: 5. Vault Meta, Compilations & Utilities
- **[[Companion AI Kanban Board]]** — Kanban board tracking ongoing pipeline tickets.
- **[[Medical tips]]** — Personal wellness, posture, and health reference notes.

---
## :LiBarChart2: Vault Node Directory & DQL Index
```dataview
TABLE WITHOUT ID
  file.link AS "Node File",
  file.folder AS "Folder",
  file.mtime AS "Last Modified"
FROM ""
WHERE file.name != this.file.name
SORT file.name ASC
```
