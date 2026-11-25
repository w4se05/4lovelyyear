---
tags: [study-system]
updated: 2026-11-25
---

# 🎯 WS26/27 Study System — Start Here

> [!abstract] The whole idea in one sentence
> Your lecture notes are now a **reference library**: you *search* them, you don't re-read them. You study from a **thin layer on top**: per lecture **1 mind map + 15–30 flashcards + 3–5 gold examples** — and you always **try before you look**.

## Why you felt overwhelmed — and what changes
| Before | From now on |
|---|---|
| AI writes 6,000–9,000-word notes, you read them | Notes = reference. New lectures get a **lean note** (1–2 screens) via [[AI Prompts v2#Prompt A — Recall layer for a new lecture\|Prompt A]] |
| SR plugin installed, 0 cards in 3rd year | One **deck per lecture** in each course's `Cards/` folder, reviewed **daily** |
| 1 mind map in the whole vault, notes not linked | Mind map in every note's **🧠 Recall Layer** + one per course, **drawn from memory first** |
| Exercise sheets and past exams at the very end | Exercise sheet **closed-book within 48 h** of the lecture; past exams from Christmas on |
| Last-minute cheatsheets ("Final Boss", "Ultimate…") | Cheat sheets built **during revision**, in versions (OS: 1 A4 side · Stats: 2 sides) |

## ✅ Do this first (today / tomorrow)
- [x] ⚠️ **Obsidian → Settings → Spaced Repetition → Flashcards → turn OFF "Convert \*\*bolded text\*\* to clozes"** (also "highlights" and "curly brackets" if you don't use clozes). Your notes contain thousands of bold phrases; with this setting on, tagging a note creates hundreds of junk cards. That's why all cards live in separate `Cards/` files.
- [x] Open the flashcard review (ribbon icon or command "Spaced Repetition: Review flashcards in all decks") and check that 4 decks appear: `os`, `cn`, `db`, `stats`.
- [ ] **Exam registration:** for OS, exchange students must register **in person at the Prüfungsamt** (Prof. Baun's FAQ) — ask there about the other three and the deadline.
- [ ] New rule since WS26/27: you can no longer withdraw from an exam without a reason — missing it without a medical certificate = **5.0**.
- [ ] Ask Prof. Hahm (CompNet) and Prof. Klingemann (DB): allowed aids? exam date? sample questions?
- [ ] Turn your **Obsidian Git** backup back on — the last backup was on 8 July; none of your 3rd-year notes are backed up.

## 📅 The four exams (exam weeks 1–20 Feb 2027)
| Course | Format | Allowed | 1.0 means | Plan |
|---|---|---|---|---|
| Operating Systems | written, 90 min, 90 pts | calculator + 1 handwritten A4 sheet, **one side** | ≥ 85.5 / 90 | [[00 OpSys Plan]] |
| Computer Networks | written, 90 min | not announced yet | — | [[00 CompNet Plan]] |
| Databases | written, 120 min | not announced yet | — | [[00 DB Plan]] |
| Statistics | computer-based in R, 90 min | lecture notes + Intro to R on the PC, 1 double-sided handwritten sheet, own keyboard | — | [[00 Statistics Plan]] |
Week-by-week overview of all four: **[[Master Calendar]]**

## 🔁 The daily loop (~2.5–3 h on weekdays)
Your vault's backup history clusters around **9–13 h** and **20–22 h** → deep work in the morning, reviews in the evening (move blocks around your timetable).
1. **🧠 Deep block, 90–120 min (morning):** the 48-hour loop for the latest lecture **or** a practice set (exercise sheet / past-exam questions).
2. **🃏 Flashcards, 20–30 min (evening):** review all due cards. New cards: about 20 per day in total.
3. **✍️ 2 min log:** tick the plan, write every mistake into the [[Error Log]].
**Minimum day** (sick/tired): 15 min cards + 1 exercise. Never zero.

## ⏱️ The 48-hour loop — after every lecture
1. **Before** the lecture (10 min): answer the **pre-questions** in the course plan. Wrong answers are fine — they make the lecture stick.
2. **Same day** (10 min): **blank page** — draw everything you remember as a mind map. No looking.
3. **Fix it** (15 min) against the slides — mark gaps in red. The gaps become cards first.
4. **Lean note + deck** (20 min): [[AI Prompts v2#Prompt A — Recall layer for a new lecture|Prompt A]] → save the note in the course folder, the cards in `Cards/` → write the ✍️ answers **yourself**.
5. **Exercise sheet closed-book** (45–60 min) → then the solution → mistakes into the [[Error Log]].

## 🗓️ The weekly loop (Sunday, 60–90 min)
1. Redraw each course mind map from memory (5 min each), compare with the plan.
2. Redo 2 old problems from *different* courses/weeks (interleaving).
3. Update the **Confidence** column (1–5) in each topic tracker.
4. Read the Error Log: anything that happened twice becomes a card.
5. Look at next week in the [[Master Calendar]].

## 🃏 How to use the flashcards
- **Where:** `3rd/OpSyS/Cards`, `3rd/CompNet/Cards`, `3rd/DB/Cards`, `3rd/Statistics/Cards` — one file per lecture, each with its own deck tag (`#flashcards/os/05-memory` …).
- **Fact cards** (`Question::Answer`): written from your own notes. Rate honestly: *Hard* if you hesitated, *Good* if right, *Easy* only if instant.
- **✍️ cards** (only the question is given): **before** reviewing a new deck, open its file and replace every `✍️ your answer` line with **your own answer from memory**, then check it with the linked section. Writing that answer *is* the learning — don't let AI fill it in.
- Cards are yours: too long → split it, useless → delete it.
- Phase 1: unlock about one deck per day (see the plans), so reviews don't pile up.

## 🗺️ Mind maps
Every lecture note now ends with a **🧠 Recall Layer** (mind map, gold examples, connections, exam lens); every plan has a course mind map. Always **draw from memory first** (paper or an Obsidian canvas), *then* compare. Looking at a mind map is not the same as knowing it.

## 🛑 Five rules against overwhelm
1. **Start every session with a question**, not with reading.
2. **Never re-read a whole note** — search it (Ctrl+F / Ctrl+Shift+F) for what you got wrong.
3. **Card cap per lecture: ~25** (30 for very dense ones). If it doesn't fit, it isn't core.
4. **Stuck for more than 20 min?** Mark it ❓, move on, ask in the exercise session.
5. **One source of truth per topic**: lean note + deck. No new "Ultimate Cheatsheet" files.

## 🧭 Map of the system
- [[Master Calendar]] · [[Error Log]] · [[AI Prompts v2]]
- Plans: [[00 OpSys Plan]] · [[00 CompNet Plan]] · [[00 DB Plan]] · [[00 Statistics Plan]]
- Lean notes (new): [[03-Data-Link-Framing-Switching]] · [[04-Data-Link-MAC-Error-Control]] · [[2.SQL]] · [[P1 Probability]] · [[P2 Descriptive Statistics]]
- Your notes with a new Recall Layer: [[01_OS_Fundamentals_and_Generations|OS-01]] · [[02_OS_Classifications_Kernels_Layers_Booting|OS-02]] · [[03_Computer_Architecture_IO_Storage|OS-03]] · [[04_HDD_SSD_RAID|OS-04]] · [[05_Memory_Management_Paging_Replacement|OS-05]] · [[01-Basics|CN-01]] · [[02-Physical-Layer|CN-02]] · [[1.Relations|DB-1]]
- Backups of your 8 notes before I edited them: `3rd/00 Study System/.backup 2026-11-25/` — the dot hides the folder inside Obsidian (so the duplicate note names don't confuse your links); open it in File Explorer if you ever need it.
