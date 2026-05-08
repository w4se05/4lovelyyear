> You are generating **Obsidian-ready study notes** for my DSA course.
> ---
> 
> ## 📁 Source & Scope
> 
> - Use the uploaded files as the **sole content source** — do not add outside material, but you may rephrase for clarity and conciseness.
> - Generate **one separate `.md` file per chapter or topic**. If a topic spans multiple files, merge them into a single note.
> - Cover **every** definition, theorem, property, corollary, and worked example present in the source files. Nothing should be omitted.
> - For proofs: include them **only if they are examinable**. If unclear, include them.
> - For figures and tables: recreate in Markdown/LaTeX where possible; otherwise insert a `> [!Missing] Figure: [description]` placeholder.
> 
> ---
> 
> ## 📐 Formatting Requirements
> 
> - I installed mermaid graph, so feel free to draw some graph if needed
> 
> - Output each note inside a **single fenced markdown code block** (` ```markdown ... ``` `) so I can copy it cleanly.
> - Write in clean Markdown with **full LaTeX math support** — use `$...$` for inline and `$$...$$` for display math. Never use `(...)` for LaTeX.
> - **Notation:** If notation varies across source files, standardize it throughout and declare the chosen convention at the top of the note under a `> [!Note] Notation Conventions` callout.
> - **All symbols and variables must be explained inline the first time they appear.**
> - Use **Obsidian callouts** with emojis for visual separation:
>     - `> [!Definition] 📖`, `> [!Theorem] 📌`, `> [!Proof] 🔷`, `> [!Property] ⚙️`, `> [!Note] 💡`, `> [!Warning] ⚠️`, `> [!Example] 📘`
> - Use clear headers: `#` for the topic title, `##` for major sections, `###` for subsections.
> - **Numbered lists inside callouts:** use bolded markers (`**1.**`, `**2.**`, ...) instead of standard list syntax to prevent Obsidian rendering breaks.
> - Begin each file with **YAML front matter**:
> 
> ```yaml
> ---
> tags: [course-name, topic-name]
> topic: "Chapter/Topic Title"
> course: "COURSE NAME"
> ---
> ```
> 
> ---
> 
> ## 🏗️ Structure Requirements
> 
> Each note must follow this exact three-part structure:
> 
> ### Part 1 — Conceptual Section (Teach Mode)
> 
> - Logical progression per concept: **Definition → Concept → Property → Implication**.
> - Definitions, formulas, theorems, and properties written concisely inside callouts.
> - Introduce and clarify any new terminology, abbreviations, or notation immediately when first used.
> - Keep math notation **consistent throughout** — no switching between equivalent forms without declaring it.
> 
> ### Part 2 — Application Section (Exam Mode)
> 
> - Grouped under the header `## 📘 Examples & Applications`.
> - Include **all worked examples from the source files**.
> - If the source contains fewer than 2 examples, supplement with one exam-style problem that combines multiple concepts from the topic.
> - Each example opens with a tag line: `**Using:** [list of concepts applied]`.
> - Solutions must be **fully worked, step-by-step, in LaTeX math form** — no skipped steps.
> 
> ### Part 3 — Summary Section
> 
> - Grouped under `## 🗂️ Summary`.
> - Concise bullet-point recap of all key results, formulas, and facts for exam revision.
> - No new content introduced here — only consolidation.
> 
> ---
> 
> ## 🎯 Tone & Pedagogy
> 
> - Write as a **clear, exam-oriented manual** — no filler, no historical background, no motivation unless it directly aids understanding.
> - Every section must be **self-contained and logically connected**.
> - Difficulty should reflect **actual exam-level problems** — prioritize examples that combine multiple concepts.
> 
> ---
> 
> ## ⚙️ Processing Instructions
> 
> - Process files **one chapter/topic at a time**. After each file, confirm what was covered and ask before proceeding to the next.
> - If any source content is **ambiguous, incomplete, or appears to have gaps**, flag it with a `> [!Warning] ⚠️ Possible Gap` callout rather than guessing.
> - Do not begin generating until I confirm which file or chapter to start with.
