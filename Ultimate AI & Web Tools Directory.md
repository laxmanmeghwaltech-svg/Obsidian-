---
title: ⚡ AI Command Center & Token Directory
aliases:
  - AI Hub
  - AI Tools Directory
  - Token Tracker
tags:
  - ai-tools
  - dashboard
  - productivity
  - obsidian-hub
cssclasses:
  - wide-page
created: 2026-10-17
status: active
---

# :LiCpu: AI Command Center & Token Directory

> [!abstract]+ :LiSliders: **System Architecture & Value Formula (Latex Suite)**
> Every AI platform in this vault is indexed via **Dataview** inline metadata and ranked using our custom Usability Efficiency Index ($U_{score}$):
> $$U_{score} = \left( \frac{\text{Model Intelligence} \times \text{Output Speed}}{\text{Friction} + \text{Paywall Strictness}} \right) \times 100\%$$
> - **Tier 1 (`100% Free`):** Zero hard paywalls, generous/unlimited usage, or free API playgrounds.
> - **Tier 2 (`Freemium`):** High-tier models with strict daily/monthly token resets.

---

## :LiRocket: Quick-Launch Daily Drivers (Buttons Plugin)

> [!tip]+ **One-Click Workspace Launchers**
> *Click any button below to launch your core stack directly in your browser or trigger QuickAdd.*

```button
name ⚡ Launch Gemini
type link
action https://gemini.google.com/app
color blue
```
```button
name 🧠 Claude (Sonnet/Opus)
type link
action https://claude.ai/new
color purple
```
```button
name 🛠️ Google AI Studio
type link
action https://aistudio.google.com/prompts/new_chat
color green
```
```button
name 🔀 OpenRouter (:free)
type link
action https://openrouter.ai/workspaces/default
color default
```
```button
name 📊 Topmate Dashboard
type link
action https://topmate.io/dashboard/home
color yellow
```
```button
name ➕ QuickAdd New AI Tool
type command
action QuickAdd: Run QuickAdd
color red
```

---

## :LiActivity: Live Dataview Intelligence Tables

> [!example]+ :LiTrophy: **Auto-Ranked Tier 1 Powerhouse Tools (Score $\ge 92\%$)**
> *Automatically generated via `Dataview` from the tool database below.*
> ```dataview
> TABLE WITHOUT ID
>   L.Tool AS "🔥 AI Platform",
>   L.Category AS "📂 Category",
>   L.Quota AS "♾️ Access / Quota",
>   L.Score + "%" AS "📈 Value Score",
>   L.Strategy AS "💡 Pro Strategy"
> FROM ""
> WHERE file.name = this.file.name
> FLATTEN file.lists AS L
> WHERE L.Tier = 1 AND L.Score >= 92
> SORT L.Score DESC
> ```

> [!warning]+ :LiClock: **Tier 2 Token Rationing Watchlist (Freemium Quotas)**
> *Automatically generated via `Dataview` to monitor tools with daily/rolling token limits.*
> ```dataview
> TABLE WITHOUT ID
>   L.Tool AS "⚡ Freemium Tool",
>   L.Category AS "📂 Category",
>   L.Quota AS "⏳ Reset Cycle",
>   L.Score + "%" AS "📊 Usability %",
>   L.Strategy AS "🎯 Token Strategy"
> FROM ""
> WHERE file.name = this.file.name
> FLATTEN file.lists AS L
> WHERE L.Tier = 2
> SORT L.Score DESC
> ```

---

## :LiCheckSquare: Daily Token & Quota Checklist (Tasks Plugin)

> [!todo]+ **Daily High-Value Credit Burn Tracker**
> *Uses the **Tasks** plugin (`🔁 every day`). When you check a box today, Tasks will automatically spawn tomorrow's reset!*

- [ ] Use **Lovable.dev** 5 daily free prompts for UI component prototyping #ai-quota ⏫ 🔁 every day 📅 2026-10-17
- [ ] Run high-reasoning architecture review on **Claude.ai** (5-hour rolling window) #ai-quota 🔼 🔁 every day 📅 2026-10-17
- [ ] Claim/Burn **Leonardo.ai** 150 daily image tokens for carousel graphics #ai-quota 🔽 🔁 every day 📅 2026-10-17
- [ ] Check **Arena.ai (LMSYS)** leaderboard & test frontier blind models #ai-quota 🔁 every week 📅 2026-10-17

### :LiFilter: Active Pending Quotas (Live Tasks Query)
```tasks
not done
path includes {{query.file.path}}
tag includes #ai-quota
sort by priority
hide backlink
```

---

## :LiDatabase: Master AI Database (Dataview Inline Indexed)

### :LiMessageSquare: 1. Daily Chatbots, Reasoning & Writing

* **[Gemini](https://gemini.google.com/app)** — [Tool:: [Gemini](https://gemini.google.com/app)] | [Tier:: 1] | [Category:: Chatbot & Writing] | [Quota:: Unlimited Flash / Generous Pro] | [Score:: 96] | [Strategy:: Daily driver for long-context synthesis, ideation, and workspace drafts]

* **[Chat.z.ai (GLM-4)](https://chat.z.ai/)** — [Tool:: [Chat.z.ai](https://chat.z.ai/)] | [Tier:: 1] | [Category:: Chatbot & Writing] | [Quota:: 100% Free Web Access] | [Score:: 94] | [Strategy:: Fast drafting, structured hooks, and zero-cost agentic prompts]

* **[Qwen Chat (Alibaba)](https://chat.qwen.ai/)** — [Tool:: [Qwen Chat](https://chat.qwen.ai/)] | [Tier:: 1] | [Category:: Coding & Math] | [Quota:: 100% Free (Qwen-Max & Coder)] | [Score:: 95] | [Strategy:: Best free alternative when Claude hits rate limits; elite at coding and math]

* **[DeepSeek Chat](https://chat.deepseek.com/)** — [Tool:: [DeepSeek](https://chat.deepseek.com/)] | [Tier:: 1] | [Category:: Reasoning & Logic] | [Quota:: 100% Free (V3 & R1)] | [Score:: 95] | [Strategy:: Unbeatable for step-by-step logic, physics/math derivations, and system prompts]

* **[NotebookLM](https://notebooklm.google.com/)** — [Tool:: [NotebookLM](https://notebooklm.google.com/)] | [Tier:: 1] | [Category:: Research & Study] | [Quota:: 100% Free (50 sources/notebook)] | [Score:: 98] | [Strategy:: Upload PDFs, YouTube links, and docs for zero-hallucination study guides]

* **[Duck.ai](https://duck.ai/)** — [Tool:: [Duck.ai](https://duck.ai/)] | [Tier:: 1] | [Category:: Anonymous Chat] | [Quota:: Free / No Sign-Up] | [Score:: 88] | [Strategy:: Instant private access to GPT-4o-mini, Claude Haiku, and Llama]

* **[Goblin.tools](https://goblin.tools/)** — [Tool:: [Goblin.tools](https://goblin.tools/)] | [Tier:: 1] | [Category:: Task & Tone Utility] | [Quota:: 100% Free / No Sign-Up] | [Score:: 95] | [Strategy:: Break down complex tasks and adjust writing tone instantly]

* **[Hemingway Editor](https://hemingwayapp.com/)** — [Tool:: [Hemingway](https://hemingwayapp.com/)] | [Tier:: 1] | [Category:: Writing Polish] | [Quota:: 100% Free Web Editor] | [Score:: 90] | [Strategy:: Eliminate passive voice and improve sentence readability]

* **[Claude.ai](https://claude.ai/new)** — [Tool:: [Claude.ai](https://claude.ai/new)] | [Tier:: 2] | [Category:: Elite Writing & Code] | [Quota:: ~10-15 msgs / 5 hours] | [Score:: 88] | [Strategy:: Ration strictly for final LinkedIn copy polish, SKILL.md design, and complex UI code]

* **[Perplexity AI](https://www.perplexity.ai/)** — [Tool:: [Perplexity](https://www.perplexity.ai/)] | [Tier:: 2] | [Category:: Deep Web Search] | [Quota:: Unlimited Basic / ~3-5 Pro Daily] | [Score:: 85] | [Strategy:: Toggle 'Pro' ONLY when verifying live citations or multi-step technical data]

* **[DeepL Write](https://www.deepl.com/write)** — [Tool:: [DeepL Write](https://www.deepl.com/write)] | [Tier:: 2] | [Category:: Grammar & Style] | [Quota:: Character Limit per Prompt] | [Score:: 85] | [Strategy:: Polish paragraphs one by one for academic or professional flow]

---

### :LiTerminal: 2. Vibe Coding, Sandboxes & Multi-Model Routers

* **[Google AI Studio](https://aistudio.google.com/prompts/new_chat)** — [Tool:: [Google AI Studio](https://aistudio.google.com/prompts/new_chat)] | [Tier:: 1] | [Category:: Developer Workbench] | [Quota:: Free (1M-2M Context + System Prompts)] | [Score:: 99] | [Strategy:: Ultimate free playground for testing system instructions, temperature, and massive codebases]
* **[Project IDX (Google)](https://idx.google.com/)** — [Tool:: [Project IDX](https://idx.google.com/)] | [Tier:: 1] | [Category:: Cloud IDE] | [Quota:: 100% Free Cloud VM + Gemini Assist] | [Score:: 96] | [Strategy:: Full VS Code in browser when Replit hits free limits]
* **[Arena.ai (LMSYS)](https://arena.ai/text)** — [Tool:: [LMSYS Arena](https://arena.ai/text)] | [Tier:: 1] | [Category:: Multi-Model Eval] | [Quota:: 100% Free Unlimited] | [Score:: 95] | [Strategy:: Use 'Direct Chat' tab to access paid frontier models (Claude, GPT, Gemini) for free]
* **[DesignArena.ai](https://www.designarena.ai/)** — [Tool:: [DesignArena](https://www.designarena.ai/)] | [Tier:: 1] | [Category:: UI/UX Benchmark] | [Quota:: 100% Free] | [Score:: 92] | [Strategy:: Compare which LLM generates the cleanest frontend HTML/Tailwind/Three.js components]
* **[Cerebras Playground](https://inference.cerebras.ai/)** — [Tool:: [Cerebras](https://inference.cerebras.ai/)] | [Tier:: 1] | [Category:: Ultra-Fast Inference] | [Quota:: 1,000,000 Free Tokens / Day] | [Score:: 93] | [Strategy:: Runs Llama 3.3 70B at ~2,000 tokens/sec for instant code refactoring]
* **[GroqCloud Playground](https://console.groq.com/playground)** — [Tool:: [GroqCloud](https://console.groq.com/playground)] | [Tier:: 2] | [Category:: Fast LPU Inference] | [Quota:: ~500k Free Tokens / Day] | [Score:: 94] | [Strategy:: Instantaneous text and code generation]
* **[OpenRouter](https://openrouter.ai/workspaces/default)** — [Tool:: [OpenRouter](https://openrouter.ai/workspaces/default)] | [Tier:: 2] | [Category:: Model Aggregator] | [Quota:: Unlimited on `:free` (~200 req/day)] | [Score:: 90] | [Strategy:: Filter strictly by `:free` models to test new open-weight releases at $0]
* **[NVIDIA NIM](https://build.nvidia.com/explore/discover)** — [Tool:: [NVIDIA NIM](https://build.nvidia.com/explore/discover)] | [Tier:: 2] | [Category:: Enterprise API] | [Quota:: 1,000 to 5,000 Free Credits] | [Score:: 84] | [Strategy:: Free browser UI testing; save API credits for multi-agent orchestration pipelines]
* **[GitHub (+ Copilot Free)](https://github.com/)** — [Tool:: [GitHub](https://github.com/)] | [Tier:: 2] | [Category:: Code Hosting & AI] | [Quota:: 2,000 Completions + 50 Chats / Month] | [Score:: 95] | [Strategy:: Core repository hub + monthly free Copilot IDE quota]
* **[Bolt.new](https://bolt.new/)** — [Tool:: [Bolt.new](https://bolt.new/)] | [Tier:: 2] | [Category:: Full-Stack Builder] | [Quota:: 150k Daily / 1M Monthly Tokens] | [Score:: 85] | [Strategy:: Rapid browser-based full-stack app prototyping]
* **[Lovable.dev](https://lovable.dev/)** — [Tool:: [Lovable](https://lovable.dev/)] | [Tier:: 2] | [Category:: Vibe Coding] | [Quota:: 5 Free Messages / Day (30/mo)] | [Score:: 78] | [Strategy:: Draft full specs in AI Studio first, then paste 1 master prompt into Lovable]
* **[v0 by Vercel](https://v0.dev/)** — [Tool:: [v0.dev](https://v0.dev/)] | [Tier:: 2] | [Category:: React/Tailwind UI] | [Quota:: Monthly Free Credits] | [Score:: 80] | [Strategy:: Generate the UI shell in v0, then export code to Cursor or IDX]
* **[Replit](https://replit.com/~)** — [Tool:: [Replit](https://replit.com/~)] | [Tier:: 2] | [Category:: Cloud IDE] | [Quota:: 3 Public Apps / Limited Agent] | [Score:: 65] | [Strategy:: Good for quick prototypes, but use Project IDX for unlimited free dev]
* **[Uncensored AI](https://uncensored.com/ai)** — [Tool:: [Uncensored AI](https://uncensored.com/ai)] | [Tier:: 2] | [Category:: Unfiltered Chat] | [Quota:: Limited Free Daily Messages] | [Score:: 75] | [Strategy:: Creative fiction or unrestricted topics rejected by mainstream bots]

---

### :LiImage: 3. Visuals, Diffusion, Video & Utility Vault

* **[Google Labs Flow (FX)](https://labs.google/fx/tools/flow)** — [Tool:: [Google Labs FX](https://labs.google/fx/tools/flow)] | [Tier:: 1] | [Category:: Image & Video] | [Quota:: 100% Free Experimental] | [Score:: 95] | [Strategy:: Powered by Imagen 3 & Veo; zero cost for high-end visual assets]
* **[Google Vids](https://docs.google.com/videos/u/0/?pli=1)** — [Tool:: [Google Vids](https://docs.google.com/videos/u/0/?pli=1)] | [Tier:: 1] | [Category:: Video Storyboarding] | [Quota:: Free with Google Account] | [Score:: 90] | [Strategy:: Quick presentation and storyboard-to-video creation]
* **[540+ Viral Image Prompts](https://gpt-image2.canghe.ai/?utm_source=newsletter.theresanaiforthat.com&utm_medium=newsletter&utm_campaign=540-viral-ai-image-prompts&_bhlid=141bba87bc9663e5b5822b4faf5f396d88f485be)** — [Tool:: [540+ Prompts Library](https://gpt-image2.canghe.ai/)] | [Tier:: 1] | [Category:: Prompt Library] | [Quota:: 100% Free Reference] | [Score:: 95] | [Strategy:: Copy proven lighting/composition structures for infographics]
* **[TAAFT Free Mini-Tools](https://free.theresanaiforthat.com/mini-tools/recommended/)** — [Tool:: [TAAFT Mini-Tools](https://free.theresanaiforthat.com/mini-tools/recommended/)] | [Tier:: 1] | [Category:: Micro-Utilities] | [Quota:: 100% Free] | [Score:: 90] | [Strategy:: Single-purpose AI text and workflow helpers]
* **[TinyWow](https://tinywow.com/tools/file_conversion)** — [Tool:: [TinyWow](https://tinywow.com/tools/file_conversion)] | [Tier:: 1] | [Category:: File & PDF Utility] | [Quota:: 100% Free Unlimited] | [Score:: 96] | [Strategy:: Instant PDF tools, background remover, and file conversions]
* **[FMHY](https://fmhy.net/) & [NoSignUps](https://nosignups.net/)** — [Tool:: [FMHY & NoSignUps](https://fmhy.net/)] | [Tier:: 1] | [Category:: Mega-Index] | [Quota:: 100% Free Directories] | [Score:: 98] | [Strategy:: Bookmark for discovering zero-login utilities and alternative AI sandboxes]
* **[Wan Video (Alibaba)](https://create.wan.video/generate)** — [Tool:: [Wan Video](https://create.wan.video/generate)] | [Tier:: 2] | [Category:: AI Video] | [Quota:: Daily Free Sign-In Credits] | [Score:: 88] | [Strategy:: Best free realistic motion generator; test prompts carefully]
* **[Utopai Studios](https://pai.utopaistudios.com/project/new)** — [Tool:: [Utopai Studios](https://pai.utopaistudios.com/project/new)] | [Tier:: 2] | [Category:: AI Storyboarding] | [Quota:: Free Trial / Project Credits] | [Score:: 80] | [Strategy:: Pre-visualizing cinematic sequences]
* **[Leonardo AI](https://leonardo.ai/)** — [Tool:: [Leonardo AI](https://leonardo.ai/)] | [Tier:: 2] | [Category:: Image Diffusion] | [Quota:: 150 Fast Tokens / Day] | [Score:: 88] | [Strategy:: Generates ~15-30 high-res graphics every 24 hours]

---

## :LiPenTool: Visual Workflow Canvas (Excalidraw Plugin)

> [!info]+ **Sketch Your Multi-Agent & Content Workflows**
> Use your installed **Excalidraw** plugin to map how prompts flow from **AI Studio** $\rightarrow$ **Claude** $\rightarrow$ **LinkedIn / Topmate**.

```button
name 🎨 Create New Excalidraw Architecture Sketch
type command
action Excalidraw: Create new drawing - in a new tab
color purple
```
