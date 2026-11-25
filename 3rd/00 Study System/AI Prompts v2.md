---
tags: [study-system, ai-prompts]
---
> [!warning] What changes compared to your old "Obsidian Prompt"
> The old prompt asked the AI for *"every definition … nothing omitted"* and produced 6,000–9,000-word notes. That makes the AI do the part that creates memory (selecting, compressing, explaining), and leaves you with text that is too long to review. These prompts produce a **small study layer** and make **you** do the recall. Back to [[00 Start Here]].

## Prompt A — Recall layer for a new lecture
```text
You are helping me build a RECALL LAYER (not full notes) for one lecture of <COURSE>.
Source: ONLY the attached slides/script. Do not add outside material.

Output ONE Obsidian markdown note with exactly these parts:
1. YAML front matter: tags [<course>, <topic>, recall-note], topic, course.
2. A Mermaid `mindmap` of the lecture: max 35 nodes, max 3 levels,
   NO brackets/parentheses/quotes in node text (they break Mermaid).
3. "Core sheet": the essential definitions, rules and formulas as compact bullets/tables
   (max ~1.5 screens). Use the lecture's own terms and notation.
4. "Gold examples": the 3–5 most exam-typical problems of this lecture, each in a collapsed
   callout `> [!example]- title` with a fully worked solution.
5. "Self-check": the lecture's own summary/self-check questions, if any.

Then output a SECOND file (flashcards for the Obsidian Spaced Repetition plugin):
- First line: #flashcards/<course>/<nn-topic>
- 15–25 fact cards as ONE line each: `Question::Answer` (answers ≤ 30 words).
- 4–6 understanding cards (why / how / compare / calculate) with ONLY the question:
  ✍️ <question>
  ?
  ✍️ your answer — then check <section or slide>
- Separate cards with a blank line. Never use **bold**, ==highlights== or {{double braces}}
  in the card file (my plugin turns them into cloze cards).
Finally list 5 pre-questions for the NEXT lecture if the slides show what comes next.
Flag anything unclear or contradictory in the slides with ⚠️ instead of guessing.
```
Save the note next to your other notes (e.g. `3rd/OpSyS/06_File_Systems.md`) and the cards in `Cards/` (e.g. `Cards/OS-06 File Systems.md`). **Then write the ✍️ answers yourself.**

## Prompt B — Examiner quiz
```text
Quiz me on <topic> of <course> like a strict examiner. Ask ONE question at a time and wait
for my answer. Then: grade it 0–2, say exactly what was missing or wrong, and ask the next
question. Mix: 50 % define/explain in my own words, 30 % apply/calculate, 20 % compare/why.
After 10 questions, list my 3 weakest points as flashcards in `Question::Answer` format
(no bold).
```

## Prompt C — Exam simulator (works best for OS, using past exams)
```text
Here are two past exams of <course> with their structure and points. Create a NEW exam with
the same structure, point distribution and difficulty, but new numbers and scenarios.
Do not show solutions. When I send my answers, mark them strictly with this scale:
1.0 = 95 %, 1.3 = 90 %, 1.7 = 85 %, 2.0 = 80 %, pass = 50 %. List every lost point and why.
```

## Prompt D — Explain my error
```text
Here is a problem, my solution and the official solution. Do NOT just repeat the right
answer. Find the exact step where my reasoning went wrong, name the misconception in one
sentence, and give me one new similar problem so I can test that I fixed it.
```

## Prompt E — Feynman check
```text
I will explain <concept> in my own words. Act as a smart student who has never heard of it:
ask me the 3 questions that expose the gaps in my explanation. Then tell me what an examiner
would mark as incomplete or imprecise.
```

## Prompt F — Weekly plan check-in
```text
Here is my study plan for this week and what I actually did (with my confidence ratings 1–5
per topic and my Error Log). Tell me honestly: what should I cut, what should I repeat, and
which 3 tasks have the highest exam value for next week? Keep it under 150 words.
```
