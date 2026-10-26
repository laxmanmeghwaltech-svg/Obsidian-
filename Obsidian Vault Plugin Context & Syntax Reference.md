---
title: 🧠 Obsidian Vault Plugin Context & Syntax Reference (For AI/LLMs)
aliases:
  - Obsidian AI Context
  - Plugin Syntax Spec
  - Vault Architecture
tags:
  - ai-context
  - system-prompt
  - obsidian-plugins
  - documentation
cssclasses:
  - wide-page
created: 2026-10-23
status: active
---

# :LiCpu: Obsidian Vault Plugin Context & Syntax Reference (LLM System Guide)

> [!important] **SYSTEM INSTRUCTION FOR AI / LLMs**
> The user's Obsidian vault is enhanced with **14 specific Community Plugins**. Whenever you are asked to write, format, or refactor an Obsidian `.md` (or `.canvas`) file for this user, **do not output plain, static Markdown** if the document can benefit from interactive dashboards, live queries, clickable buttons, mind-map hierarchies, task automation, image sizing/alignment, or vector icons. Follow the exact syntax specifications and anti-collision rules documented below.

---

## :LiDatabase: 1. Installed Community Plugins Inventory (14 Plugins)

| # | Plugin Name | Version | Author | Role in Markdown & Vault Generation |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Advanced Canvas** | `v7.1.0` | `Developer-Mike` | **(NEW)** Supercharges native `.canvas` files with flowchart node shapes, presentation slides, portals, and collapsible groups. |
| 2 | **BRAT** | `v2.2.0` | `TfTHacker` | Beta plugin tester (system utility; no direct Markdown syntax required). |
| 3 | **Buttons** | `v0.9.13` | `shabegom` | Renders interactive UI buttons inside notes to open URLs, run Obsidian commands, or insert templates. |
| 4 | **Dataview** | `v0.5.68` | `Michael Brenan` | Turns notes into a live database via YAML properties, inline fields (`[Key:: Value]`), and `dataview` DQL codeblocks. |
| 5 | **Editing Toolbar** | `v4.1.10` | `Cuman` | MS Word-like UI formatting bar (supports HTML highlight tags `<mark>`, callouts, and colored text spans). |
| 6 | **Excalidraw** | `v2.29.0` | `Zsolt Viczian` | Embeds visual 4D PKM sketches (`![[Drawing.excalidraw]]`) and launches canvas drawings via command buttons. |
| 7 | **Iconize** | `v2.14.7` | `Florian Woelki` | Injects inline Lucide/FontAwesome vector icons into headers, callouts, and lists using `:LiIconName:` shortcodes. |
| 8 | **Image Converter** | `v1.4.6` | `xRyul` | **(NEW)** Resizes, aligns, crops, and annotates images directly via Obsidian pipe syntax (`![[image.webp\|center\|400]]`). |
| 9 | **Kanban** | `v2.0.51` | `mgmeyers` | Converts a dedicated `.md` file into a drag-and-drop visual Kanban board via `kanban-plugin: board` frontmatter. |
| 10 | **Latex Suite** | `v1.14.0` | `artisticat` | Renders inline (`$...$`) and block (`$$...$$`) MathJax/LaTeX equations for Physics, Chemistry, Math, and metrics. |
| 11 | **Mind Map** | `v1.1.0` | `James Lynch` | **(NEW)** Renders notes as interactive Markmap mind maps based on clean Markdown heading (`#` to `####`) and nested list hierarchies. |
| 12 | **Notebook Navigator** | `v3.4.3` | `Johan Sanneblad` | Two-pane UI explorer that relies on clean YAML `tags`, `aliases`, and `title` properties for previews and sorting. |
| 13 | **QuickAdd** | `v2.32.1` | `Christian B. B. Houmann` | Automates note creation, macros, and data capture; can be triggered directly via `Buttons` command blocks. |
| 14 | **Tasks** | `v8.6.0` | `Clare Macrae & Ilyas Landikov` | **(UPDATED)** Adds due dates, recurring intervals, priority emojis, and live `tasks` query codeblocks to checklists. |

---

## :LiSliders: 2. Exact Syntax Specifications (How the AI Must Write Code)

### A. Mind Map (`v1.1.0`) — Markmap-Compatible Hierarchy Rules (NEW)
The **Mind Map** plugin dynamically parses headings (`#`, `##`, `###`, `####`) and nested bullet points (`-`) into an interactive visual tree.
- **Strict Hierarchy Rule:** Never skip heading levels (e.g., do not jump from `# H1` to `### H3`). Maintain a strict `#` $\rightarrow$ `##` $\rightarrow$ `###` $\rightarrow$ `- Bullet` tree so the Markmap renderer builds clean branches.
- **Concise Node Titles:** Keep headings concise and scannable so mind map nodes do not stretch across the screen. Put lengthy explanations inside sub-bullets or foldable callouts.
- **Quick-Preview Button:** In study notes, revision sheets, or brainstorming docs, include a button to open the Mind Map view:
````markdown
```button
name 🧠 Preview Note as Mind Map
type command
action Mind Map: Preview the current note as a Mind Map
color purple
```
````

---

### B. Advanced Canvas (`v7.1.0`) — Flowcharts, Presentations & `.canvas` JSON (NEW)
When the user asks for a flowchart, system architecture map, or visual presentation in Obsidian Canvas (`.canvas` JSON format) or embeds a canvas (`![[Architecture.canvas]]`):
- **Embed Syntax:** Use `![[File_Name.canvas]]` to embed interactive canvases inside standard `.md` notes.
- **Advanced Canvas JSON Properties:** When generating raw `.canvas` JSON files for the user, leverage `Advanced Canvas` extended node metadata (`styleAttributes`):
  - **Node Shapes (`shape`):** `"oval"`, `"diamond"` (for decision nodes), `"parallelogram"` (input/output), `"database"`, `"document"`, `"hexagon"`.
  - **Presentation Slides:** Add `"isSlide": true` to nodes to turn a `.canvas` file into a step-by-step slide deck.
  - **Portals:** Embed another `.canvas` inside a node with `"portal": true` to view nested workflows directly.

---

### C. Image Converter (`v1.4.6` by `xRyul`) — Image Alignment & Sizing (NEW)
Whenever embedding images, diagrams, or screenshots in `.md` files, do not use raw unstyled embeds if layout matters. Use **Image Converter**'s extended pipe syntax:
- **Internal Vault Embeds:** `![[diagram.webp|center|500]]` or `![[screenshot.png|right|350]]`
- **External Markdown Images:** `![Alt Text|center|600](https://example.com/image.png)`
- **Valid Alignment Keywords:** `left`, `center`, `right`, ` float-left`, `float-right`
- **Dimensions:** `|400` (width in px) or `|400x250` (width $\times$ height in px).

---

### D. Dataview (`v0.5.68`) — Live Queries & Inline Metadata
When creating directories, trackers, study logs, or resource lists, **avoid static Markdown tables** if the user wants sorting or filtering. Instead:
1. **Inline Fields:** Embed metadata inside bullet points using `[Field:: Value]` (visible key) or `(Field:: Value)` (hidden key).
   - *Example:* `* **[Claude](https://claude.ai)** — [Category:: Coding] | [Tier:: 2] | [Score:: 95]`
2. **DQL Block Syntax:** Query inline list items within the *same* file using `FLATTEN file.lists AS L`:
````markdown
```dataview
TABLE WITHOUT ID
  L.text AS "Item",
  L.Category AS "Category",
  L.Score + "%" AS "Score"
FROM ""
WHERE file.name = this.file.name
FLATTEN file.lists AS L
WHERE L.Category
SORT L.Score DESC
```
````

---

### E. Buttons (`v0.9.13`) — Interactive UI Launchers
Whenever a note includes frequently visited URLs, dashboards, or repetitive Obsidian commands (like Mind Map preview, Excalidraw, or QuickAdd), wrap them in `button` codeblocks.
- **Valid Colors:** `default`, `blue`, `red`, `green`, `yellow`, `purple`
- **URL Button Syntax:**
````markdown
```button
name ⚡ Launch Workspace
type link
action https://aistudio.google.com/
color blue
```
````
- **Command Palette Button Syntax:**
````markdown
```button
name ➕ QuickAdd Capture
type command
action QuickAdd: Run QuickAdd
color green
```
````

---

### F. Tasks (`v8.6.0`) — Smart Checklists & Auto-Queries
Never write plain `- [ ]` tasks for action items that have deadlines, priorities, or recurring schedules. Append **Tasks Emoji Shorthand** at the end of the line:
- **Priority Emojis:** `🔺` Highest | `⏫` High | `🔼` Medium | `🔽` Low | `⏬` Lowest
- **Dates & Recurrence:**
  - `🔁 every day` / `🔁 every week on Sunday` (Must appear *before* the due date emoji)
  - `🛫 YYYY-MM-DD` (Start Date) | `⏳ YYYY-MM-DD` (Scheduled Date) | `📅 YYYY-MM-DD` (Due Date) | `✅ YYYY-MM-DD` (Done Date)
- **Correct Task Line Example:**
  `- [ ] Revise Electrochemistry Nernst Equation #jee-chem ⏫ 🔁 every 3 days 📅 2026-10-25`
- **Live Tasks Query Block:**
````markdown
```tasks
not done
path includes {{query.file.path}}
sort by priority
sort by due
hide backlink
```
````

---

### G. Iconize (`v2.14.7`) — Vector Icons in Headings & Callouts
Use **Iconize Lucide shortcodes** (`:LiIconName:`) in headings to give notes a clean, modern UI feel:
- `:LiCpu:` (AI / System) | `:LiZap:` (Speed / Quick Actions) | `:LiTerminal:` (Coding / Prompts)
- `:LiDatabase:` (Dataview / Vault) | `:LiCheckSquare:` (Tasks) | `:LiBookOpen:` (Study / Playbooks)
- `:LiNetwork:` (Mind Map / Canvas / Flowcharts) | `:LiImage:` (Image Converter / Visuals)
- *Example Header:* `## :LiNetwork: Concept Mind Map & Architecture`

---

### H. Latex Suite (`v1.14.0`) — Mathematical & Scientific Typesetting
- Always wrap inline variables, Greek letters, chemical formulas, and equations in single dollar signs: `$E = E^\circ - \frac{RT}{nF}\ln Q$`
- Wrap standalone equations, matrices, and derivations in double dollar signs (`$$...$$`) using `\begin{aligned}` for multi-step proofs:
```markdown
$$
\begin{aligned}
\eta_{\text{workflow}} &= \frac{\text{Valid Output Tokens}}{\text{Prompt Latency (s)} \times \text{Cost}}
\end{aligned}
$$
```

---

### I. Kanban (`v2.0.51`) — Critical Anti-Collision Rule
> [!danger] **CRITICAL RULE FOR KANBAN (`mgmeyers`)**
> Adding `kanban-plugin: board` to the YAML frontmatter converts the **ENTIRE** `.md` file into a Kanban board interface, which **hides all standard paragraphs, Dataview tables, Callouts, and Buttons**.
- **Rule 1:** NEVER put `kanban-plugin: board` inside a general dashboard or study note.
- **Rule 2:** Only generate a Kanban file as a **separate, dedicated `.md` file** when the user asks for a board view.

---

### J. Notebook Navigator (`v3.4.3`), Editing Toolbar (`v4.1.10`) & Callouts
1. **Mandatory YAML Frontmatter:** Every `.md` file must begin with a clean YAML header (`title`, `aliases`, `tags`, `cssclasses: [wide-page]`, `created`, `status`) so **Notebook Navigator** can index and preview notes accurately.
2. **Foldable Multi-Color Callouts:** Use `> [!abstract]+`, `> [!tip]+`, `> [!warning]+`, `> [!example]+`, and `> [!todo]+` to group dense content cleanly.
3. **Editing Toolbar Highlights:** Use `==highlighted text==` or `<mark style="background: #ffb86cA6;">important concept</mark>` for key takeaways.

---

## :LiCheckSquare: 3. Pre-Output Checklist for the AI
Before outputting any Obsidian `.md` file for this user, verify:
1. [x] Does it start with valid YAML frontmatter (`title`, `aliases`, `tags`, `cssclasses: [wide-page]`)? ✅ 2026-10-23
2. [x] Is the heading hierarchy (`#` $\rightarrow$ `##` $\rightarrow$ `###` $\rightarrow$ `-`) strictly sequential so **Mind Map (`v1.1.0`)** renders a clean tree? ✅ 2026-10-23
3. [x] Are key external links and Obsidian commands (e.g., Mind Map preview, Excalidraw, QuickAdd) upgraded into ```` ```button ```` blocks? ✅ 2026-10-23
4. [x] Are structured lists formatted with `[Key:: Value]` inline fields and paired with a ```` ```dataview ```` query block? ✅ 2026-10-23
5. [x] Do action items use **Tasks (`v8.6.0`)** emojis (`⏫`, `🔁`, `📅`) and a ```` ```tasks ```` query block? ✅ 2026-10-23
6. [x] Do image embeds use **Image Converter (`v1.4.6`)** pipe syntax (`|center|500`)? ✅ 2026-10-23
7. [x] Are headings enhanced with `:Li...:` **Iconize** shortcodes and organized with `> [!callout]+` blocks? ✅ 2026-10-23
8. [x] Is `kanban-plugin: board` kept strictly in its own separate `.md` file so it doesn't break the main document view? ✅ 2026-10-23