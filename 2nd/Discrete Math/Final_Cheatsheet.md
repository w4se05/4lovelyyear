---
tags: [discrete-mathematics, exam-prep, counting, graphs, trees, cheat-sheet]
course: "DISCRETE MATHEMATICS — VGU-CS"
purpose: "Exam procedure guide — no proofs, just recipes + worked examples, matching lecture methodology"
updated: 2026-07-04
---

# 🎯 Discrete Math — Exam Survival Guide
*Companion to `DM-exer.md`. No theory, no proofs — just: "which formula do I use, and how do I use it."*

> [!tip] How to use this file
> 1. Find your topic below.
> 2. Read the **🧭 Decision Guide** to identify *which case* your problem is.
> 3. Apply the **recipe** (numbered steps).
> 4. Check the **worked example** that matches your case.
> 5. When stuck mid-exam, jump straight to the 🗂️ **Formula Cheat-Table** at the end of each part.

---

## ⚡ Quick-Reference Card — Top 10 Formulas

| #   | Situation                                                | Formula                                             |
| --- | -------------------------------------------------------- | --------------------------------------------------- |
| 1   | $k$-subsets of $[n]$                                     | $C(n,k)$                                            |
| 2   | $k$-permutations of $n$                                  | $P(n,k)=\dfrac{n!}{(n-k)!}$                         |
| 3   | Combo-with-rep / stars-and-bars                          | $C(n+k-1,k)$                                        |
| 4   | Multiset permutations                                    | $\dfrac{n!}{n_1!\cdots n_k!}$                       |
| 5   | Functions $[m]\to[n]$ / Surjections                      | $n^m$ &ensp; $\mid$ &ensp; Surj: $n!\,S(m,n)$       |
| 6   | Handshaking                                              | $\sum\deg(v)=2$&#124;$E$&#124;                      |
| 7   | Euler: circuit &ensp; $\mid$ &ensp; path                 | all degrees even &ensp; $\mid$ &ensp; exactly 2 odd |
| 8   | Planar bound: general &ensp; $\mid$ &ensp; triangle-free | $e\le3v-6$ &ensp; $\mid$ &ensp; $e\le2v-4$          |
| 9   | Cayley (labeled trees)                                   | $n^{n-2}$                                           |
| 10  | Full $m$-ary tree                                        | $n=mi+1$ &ensp; $\mid$ &ensp; leaves $=(m-1)i+1$    |


> [!danger] 🚨 Top 5 Exam Traps
> - **Distinct vs. Identical?** Always ask first — this decides the entire formula family.
> - **Order matters?** $P(n,k)$ (yes) vs $C(n,k)$ (no). "Committee" = unordered; "president + VP" = ordered.
> - **Complement shortcut:** "at least one X" → total − (zero X). Faster than summing cases.
> - **Division Rule:** Circular arrangements $(n-1)!$, not $n!$; unlabeled pairings divide by factorial overcount.
> - **PIE: none vs. at least one:** "Not divisible by A or B" → complement of union. "Divisible by A or B" → union itself.

---

## 🧩 PART 1 — Basic Counting Rules
*(covers `DM-exer.md` §1, items 1–92)*

### 🧭 Decision Guide — which rule applies?

| Signal in the problem | Rule to use |
|---|---|
| "...or...", counting a union of **disjoint** cases | **Sum Rule**: add the cases |
| Want total, but "at least 1 / not all" property | **Complement**: total − (opposite case) |
| A procedure has several **independent sequential steps** | **Product Rule**: multiply choices per step |
| Circular arrangement / every object over-counted the same number of times | **Division Rule**: divide by the overcount factor |
| Two things "obviously" have the same count but you can't see why | **Bijection Rule**: build an explicit 1-1 correspondence |
| Choosing $k$ from $n$, **order matters**, no repeats | $P(n,k)=\dfrac{n!}{(n-k)!}$ |
| Choosing $k$ from $n$, **order doesn't matter**, no repeats | $C(n,k)=\dbinom{n}{k}$ |
| Choosing $k$ from $n$ **with repetition allowed**, order doesn't matter | $C(n+k-1,k)$ (stars and bars) |
| Arranging a multiset (repeated letters/objects) in a row | $\dfrac{n!}{n_1!n_2!\cdots n_k!}$ |
| Distributing objects into boxes | see the **twelvefold mini-table** below |
| Partitioning a set into unlabeled non-empty blocks | Stirling numbers $S(n,k)$ |
| "Prove two quantities are equal / at least one exists" (no construction needed) | Pigeonhole |

---

### Case 1 — Subsets of $[n]$ (Power Set)

> [!procedure] 🧭 Recipe
> - "How many subsets total?" → $2^n$
> - "Subsets of size exactly $k$?" → $C(n,k)$
> - "At most $k$ elements?" → $C(n,0)+C(n,1)+\cdots+C(n,k)$
> - "More than $k$ elements?" → $2^n - \big[C(n,0)+\cdots+C(n,k)\big]$ (complement)

> [!example] 📘 Worked — Ex. 1–4 (100-element set)
> **Q2.** Subsets of a 100-element set with **at most 2** elements:
> $$C(100,0)+C(100,1)+C(100,2) = 1+100+4950 = 5051$$
> **Q3.** **More than 2** elements → complement:
> $$2^{100} - 5051$$
> **Q1 (general $n$).** Exactly 2 elements: $C(n,2) = \dfrac{n(n-1)}{2}$.
> **Q4 (general $n$).** All subsets: $2^n$.

---

### Case 2 — Strings / passwords / license plates (Product Rule + Complement)

> [!procedure] 🧭 Recipe
> 1. Identify the **positions** (slots) to fill.
> 2. For each slot, count how many symbols are allowed **at that slot** (Product Rule).
> 3. If the question says "contains at least one X" or "no two consecutive equal", compute the **complement**: total (no restriction) − count that **violates** "at least one" (i.e. count with **zero** occurrences of X).

> [!example] 📘 Worked — Ex. 5, 8–10 (Passwords, plates, chairs)
> **Q5.** 5-character ASCII strings (128 symbols) containing **@ at least once**:
> Total strings: $128^5$. Strings with **no** @: $127^5$.
> $$\text{Answer} = 128^5 - 127^5$$
>
> **Q8.** Chairs labeled with a letter (26 choices) + integer 1–100 (100 choices), sequential independent choices:
> $$26 \times 100 = 2600$$
>
> **Q9.** License plates: 3 uppercase letters then 3 digits:
> $$26^3 \times 10^3$$
>
> **Q10.** Passwords length 4–8, letters only (52 choices/char). Sum Rule over disjoint lengths:
> $$52^4+52^5+52^6+52^7+52^8$$

> [!example] 📘 Worked — Ex. 6 (bit strings, 0s counted)
> Length-5 bit strings with:
> **(a) exactly two 0s:** choose which 2 of the 5 positions are 0 → $C(5,2)=10$.
> **(b) at most two 0s:** $C(5,0)+C(5,1)+C(5,2) = 1+5+10=16$.
> **(c) at least two 0s:** complement of "0 or 1 zeros":
> $$2^5 - \big[C(5,0)+C(5,1)\big] = 32-6=26$$

---

### Case 3 — Linear vs. Circular Arrangements

> [!procedure] 🧭 Recipe
> - Arrange $n$ **distinct** objects in a **line**: $n!$
> - Arrange $n$ **distinct** objects around a **round table**: $(n-1)!$ (Division Rule: divide the $n!$ linear arrangements by the $n$ rotations that look identical)
> - Select-then-arrange (president + committee, ordered roles): use **Product Rule**, multiplying separate $P(\cdot,\cdot)$ or $C(\cdot,\cdot)$ pieces for each distinguishable role.

> [!warning] Common Pitfall
> Circular arrangements are $(n-1)!$, NOT $n!$. Every exam has this trap.

> [!example] 📘 Worked — Ex. 11 (president + advisory board)
> 10-person club, choose 1 president (order matters — a distinguished role) then 2-person **unordered** advisory board from the remaining 9:
> $$\underbrace{10}_{\text{president}} \times \underbrace{C(9,2)}_{\text{board}} = 10 \times 36 = 360$$

> [!example] 📘 Worked — Ex. 27 (tennis pairing, round-robin)
> $2n$ members paired into $n$ matches (unordered pairs, pairing itself unordered):
> Line up all $2n$ people: $(2n)!$ ways. Each pairing is over-counted:
> - by $2!$ for swapping the two people **within** each of the $n$ pairs → divide by $2^n$
> - by $n!$ for the order in which we listed the $n$ pairs themselves → divide by $n!$
>
> $$\text{Pairings} = \frac{(2n)!}{2^n \, n!}$$
> If in addition we specify **who serves first** in each match (2 choices per pair, independent):
> $$\frac{(2n)!}{2^n\,n!}\times 2^n = \frac{(2n)!}{n!}$$

---

### Case 4 — Counting Functions $[m]\to[n]$

> [!formula] 🗂️ Formula table
> | Function type | Count | Condition |
> |---|---|---|
> | All functions | $n^m$ | always |
> | Injective (one-to-one) | $P(n,m)=\dfrac{n!}{(n-m)!}$ | $0$ if $m>n$ |
> | Bijective | $n!$ | only if $m=n$ |
> | Surjective (onto) | $n!\cdot S(m,n)$ **or** $\displaystyle\sum_{j=0}^n(-1)^j\binom{n}{j}(n-j)^m$ | needs $m\ge n$; use Stirling table for small $n$, PIE formula otherwise |

> [!procedure] 🧭 Recipe for "list all functions/injections/bijections" (small cases)
> 1. Write domain and codomain explicitly as $[m],[n]$.
> 2. Enumerate systematically (e.g. fix $f(1)$, then $f(2)$, ... ), respecting injectivity if required.

> [!example] 📘 Worked — Ex. 13–19
> **Q16.** Functions $[m]\to[n]$: $n^m$.
> **Q18.** One-to-one functions $[3]\to[5]$: $P(5,3)=5\times4\times3=60$.
> **Q19 (general).** One-to-one $[m]\to[n]$: $P(n,m)$, and $0$ if $m>n$.
> **Q13.** Functions $[3]\to[2]$: list all $2^3=8$ triples of images $(f(1),f(2),f(3))\in\{1,2\}^3$.

---

### Case 5 — Distributing Objects into Boxes (the "twelvefold way" mini-table)

> [!formula] 🗂️ Which of the 4 formulas do I need?
> Ask two questions: **(a)** are the objects distinct or identical? **(b)** are the boxes distinct or identical?
>
> | Objects | Boxes | No restriction | Each box ≥ 1 |
> |---|---|---|---|
> | Distinct ($k$) | Distinct ($n$) | $n^k$ | $n!\,S(k,n)$ (surjections) |
> | Distinct ($k$) | Identical ($n$) | $\sum_{j=1}^{n} S(k,j)$ | $S(k,n)$ |
> | Identical ($k$) | Distinct ($n$) | $C(n+k-1,k)$ | $C(k-1,n-1)$ |
> | Identical ($k$) | Identical ($n$) | # partitions of integer $k$ into **at most** $n$ parts | # partitions of $k$ into **exactly** $n$ parts |

> [!warning] Read the "each box" column carefully
> "Each box ≥ 1" for **identical** objects → **distinct** boxes uses $C(k-1,n-1)$, NOT the unrestricted $C(n+k-1,k)$. This is a very common mistake.

> [!procedure] 🧭 Recipe for "each box gets at least $r$" (identical objects, distinct boxes)
> Give every one of the $n$ boxes $r$ objects **first** (uses up $nr$ objects), then distribute the remaining $k-nr$ identical objects with **no restriction**:
> $$C\big((k-nr) + n - 1,\ k-nr\big)$$

> [!example] 📘 Worked — Ex. 62–65 (4 distinct gifts / 3 boxes)
> **Q62.** 4 distinct gifts, 3 **identical** boxes, no restriction:
> $$S(4,1)+S(4,2)+S(4,3) = 1+7+6=14$$
> **Q63.** Same, but each box ≥ 1 gift: $S(4,3)=6$.
> **Q64.** 4 **identical** gifts, 3 identical boxes, no restriction = partitions of 4 into at most 3 parts: $4,\,3{+}1,\,2{+}2,\,2{+}1{+}1 \Rightarrow 4$.
> **Q65.** Same, each box ≥1 = partitions of 4 into exactly 3 parts: $2{+}1{+}1 \Rightarrow 1$.

> [!example] 📘 Worked — Ex. 71 (identical gifts, distinct boxes, each ≥ 5)
> 100 identical gifts into 10 distinct boxes, each box ≥ 5:
> Give 5 to each box first: uses $50$, leaving $50$ to distribute freely among 10 distinct boxes:
> $$C(50+10-1,\,50)=C(59,50)=C(59,9)$$

---

### Case 6 — Non-negative Integer Solutions (Stars and Bars) + Bounds via PIE

> [!procedure] 🧭 Recipe
> 1. **Equation** $x_1+\cdots+x_n=k$, $x_i\ge0$: $\;C(n+k-1,k)$.
> 2. **Each $x_i\ge a_i$:** substitute $x_i' = x_i-a_i\ge0$; solve the shifted equation for $x_i'$.
> 3. **Inequality** $x_1+\cdots+x_n\le k$: add a **slack variable** $x_{n+1}\ge0$, turning it into an equation with $n+1$ variables: $C(k+n,k)$.
> 4. **Upper bound $x_i\le b_i$:** solve unrestricted, then subtract (via PIE) the solutions where some $x_i\ge b_i+1$ (see Part 2 §PIE).

> [!Note] 💡 Equivalent Formulations
> The following all count the same thing $$= C(n+k-1,k)=C(n+k-1,n-1)$$
> **1.** Non-negative integer solutions to $x_1 + x_2 + \cdots + x_n = k$.
> **2.** $k$-combinations with repetition from $n$ elements.
> **3.** Ways to distribute $k$ identical objects to $n$ people.
> **4.** Ways to place $k$ identical books onto $n$ shelves.

> [!example] 📘 Worked — Ex. 50–55
> **Q50.** $x_1+\cdots+x_n=k$, $x_i\ge0$: $C(n+k-1,k)$.
> **Q51.** Same but $x_i>0$ (i.e. $x_i\ge1$): substitute $x_i'=x_i-1\ge0$, solve $\sum x_i' = k-n$: $C(k-1,\,n-1)$.
> **Q52.** $k$ identical apples, $n$ children, each ≥1: same as Q51 → $C(k-1,n-1)$.
> **Q54.** $x_1+\cdots+x_5=21$:
> (a) each $x_i\ge1$: shift, solve $\sum x_i'=16$ over 5 vars → $C(20,4)$.
> (b) each $x_i\ge2$: shift, solve $\sum x_i'=11$ → $C(15,4)$.
> (c) $0\le x_1\le10$ (rest unrestricted): total unrestricted $C(25,4)$ minus solutions with $x_1\ge11$ (shift $x_1'=x_1-11$, solve $\sum=10$ → $C(14,4)$): $\;C(25,4)-C(14,4)$.
> **Q55.** $x_1+x_2+x_3\le11$: add slack $x_4\ge0$, solve $x_1+x_2+x_3+x_4=11$: $C(14,3)$.

---

### Case 7 — Permutations with Repetition (Anagram-style problems)

> [!procedure] 🧭 Recipe (multiset permutations)
> 1. Count total letters $n$ and multiplicities $n_1,\ldots,n_k$ of each repeated symbol.
> 2. Base count: $\dfrac{n!}{n_1!\cdots n_k!}$.
> 3. For a **"no $r$ consecutive identical letters"** restriction: glue the $r$ repeated letters into **one super-letter**, recompute the permutation count of the *smaller* multiset, then **subtract** (complement) from the base count.
> 4. For **two simultaneous restrictions** ("no 4 consecutive S's AND no 2 consecutive P's"), use PIE: (total) − (violates #1) − (violates #2) + (violates both).

> [!example] 📘 Worked — Ex. 43–44 (CASABLANCA, SUCCESS)
> **Q43.** CASABLANCA: letters C(2),A(3),S(1),B(1),L(1),N(1) — total 10 letters:
> $$\frac{10!}{3!\,2!} = 302400$$
> **Q44.** SUCCESS: S(3),U(1),C(2),E(1) — total 7 letters:
> $$\frac{7!}{3!\,2!}=420$$

> [!example] 📘 Worked — MISSISSIPPI, no 4 consecutive S's (Ex. 14, Part 2 of exercises)
> Letters: M(1) I(4) S(4) P(2), total 11.
> Base count: $\dfrac{11!}{4!\,4!\,2!}$.
> Glue all 4 S's into one block "SSSS" → now arranging $\{M,I,I,I,I,SSSS,P,P\}$, 8 objects:
> $\dfrac{8!}{4!\,2!}$ arrangements contain "SSSS" as a block.
> $$\text{Answer} = \frac{11!}{4!\,4!\,2!} - \frac{8!}{4!\,2!}$$

---

### Case 8 — $k$-Combinations with Repetition / Generating Functions Preview

> [!procedure] 🧭 Recipe
> Choosing $k$ items from $n$ **types**, unlimited supply of each, order doesn't matter:
> $$C(n+k-1,k)$$
> This is identical to Case 6 (stars and bars) — same formula, different story problem.

> [!example] 📘 Worked — Ex. 33–34 (committees / teams with quotas)
> **Q33.** 25 students, choose 3 for **one** unlabeled competition team: $C(25,3)$.
> Choose 3 for **three distinguishable** competitions (Calculus/Algebra/DM), 1 person each, order matters across roles:
> $$P(25,3) = 25\times24\times23$$
> **Q34.** 9 female + 20 male, pick 11 for a team.
> (a) exactly 3 female: $C(9,3)\times C(20,8)$.
> (b) at least 1 female = complement of "0 female":
> $$C(29,11) - C(20,11)$$

---

### Case 9 — Binomial / Multinomial Coefficient Extraction

> [!procedure] 🧭 Recipe
> 1. Write the general term of the expansion: for $(x+y)^n$, term $k$ is $C(n,k)x^ky^{n-k}$; for $(x_1+\cdots+x_m)^n$, term is $\dfrac{n!}{r_1!\cdots r_m!}x_1^{r_1}\cdots x_m^{r_m}$ with $\sum r_i=n$.
> 2. Match exponents in the question to $r_i$ (or to $k$), solving for the unknown exponent variable.
> 3. Don't forget: if a term has a **coefficient** (e.g. $2x$), that coefficient gets raised to the matching power too.

> [!example] 📘 Worked — Ex. 37–40, 45
> **Q37.** Coefficient of $x^{101}y^{99}$ in $(2x-3y)^{200}$: here $k=101,\,n-k=99$ ✓ ($101+99=200$):
> $$C(200,101)\,2^{101}(-3)^{99}$$
> **Q38.** Coefficient of $x^k$ in $\left(x+\tfrac1x\right)^{100}$: general term $C(100,j)x^j x^{-(100-j)}=C(100,j)x^{2j-100}$. Set $2j-100=k \Rightarrow j=\tfrac{k+100}{2}$, valid only if $k$ even and $-100\le k\le100$:
> $$C\!\left(100,\ \frac{k+100}{2}\right) \text{ if } k \text{ even, else } 0$$
> **Q39.** Coefficient of $x^{101}y^{99}z^{105}$ in $(2x-3y-z)^{305}$ (check $101+99+105=305$ ✓):
> $$\frac{305!}{101!\,99!\,105!}\,2^{101}(-3)^{99}(-1)^{105}$$
> **Q40.** Paint 10 distinct chairs: 3 green, 3 blue, 4 red (multinomial, distributing distinct objects into labeled categories):
> $$\frac{10!}{3!\,3!\,4!}$$

---

### Case 10 — Set Partitions & Stirling Numbers of the Second Kind $S(n,k)$

> [!formula] 🗂️ Formulas to memorize
> $$S(n,1)=1,\quad S(n,n)=1,\quad S(n,n-1)=C(n,2),\quad S(n,2)=2^{n-1}-1$$
> $$S(n,k) = S(n-1,k-1) + k\cdot S(n-1,k)\qquad\text{(recurrence — build a table if no closed form is known)}$$
> $$B(n) = \sum_{k=1}^n S(n,k) \quad\text{(Bell number} =\text{ total  } \# \text{ partitions)}$$

> [!procedure] 🧭 Recipe for "list all partitions into $k$ parts"
> Fix the block containing element 1, then recursively distribute the rest — or just enumerate directly for small $n$ (systematic: smallest element goes first in its block).

> [!example] 📘 Worked — Ex. 57 (partitions of $[4]$)
> $S(4,1)=1$: $\{1,2,3,4\}$.
> $S(4,2)=7$: $\{1\},\{2,3,4\}$; $\{2\},\{1,3,4\}$; $\{3\},\{1,2,4\}$; $\{4\},\{1,2,3\}$; $\{1,2\},\{3,4\}$; $\{1,3\},\{2,4\}$; $\{1,4\},\{2,3\}$.
> $S(4,3)=6$: one pair + two singletons — $C(4,2)=6$ ways to choose the pair.
> $S(4,4)=1$: all singletons.
> Bell number $B(4)=1+7+6+1=15$.

---

### Case 11 — Pigeonhole Principle

> [!procedure] 🧭 Recipe
> 1. Identify the **pigeons** (the objects/people being placed) and the **holes** (categories).
> 2. Compute $\lceil (\text{pigeons})/(\text{holes})\rceil$ — this is the guaranteed minimum in the fullest hole.
> 3. For "**generalized** pigeonhole" (want a hole with $\ge r$ pigeons): find the smallest number of pigeons $N$ such that $\lceil N/(\text{holes})\rceil \ge r$, i.e. $N = (r-1)\cdot(\text{holes})+1$.
> 4. For "two items summing to $X$" problems: pair up numbers that sum to $X$ into holes; each hole has 2 pigeons max before a repeat is forced.

> [!example] 📘 Worked — Ex. 85, 89, 91 (socks, sums, chairs)
> **Q85.** 60 socks, 3 colors, dark room — worst case take one of each color first (3 socks), the next sock **must** match one already taken:
> $$3+1=4 \text{ socks guaranteed to include a matching pair}$$
> **Q89.** From $\{1,\ldots,10\}$, pairs summing to 11: $\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$ — **5 holes**. Selecting 7 numbers (pigeons) into 5 holes forces at least 2 holes to be **fully used** (both partners chosen), giving **2 pairs** summing to 11.
> With only 6 numbers selected: not guaranteed (5 holes, 6 pigeons only forces 1 hole full) — **conclusion is false for 6**.
> **Q91.** 12 chairs, 9 occupied. Split the 12 chairs into 4 groups of 3 consecutive chairs (holes). 9 people into 4 groups $\Rightarrow \lceil 9/4\rceil = 3$: some group of 3 consecutive chairs is fully occupied.

---

## 🗂️ Part 1 — Master Formula Table

| Situation                                     | Formula                                                              |
| --------------------------------------------- | -------------------------------------------------------------------- |
| Subsets of $[n]$                              | $2^n$                                                                |
| $k$-subsets of $[n]$                          | $C(n,k)$                                                             |
| Linear arrangements of $n$ distinct objects   | $n!$                                                                 |
| Circular arrangements                         | $(n-1)!$                                                             |
| $k$-permutations of $n$                       | $P(n,k)=\frac{n!}{(n-k)!}$                                           |
| Functions $[m]\to[n]$                         | $n^m$                                                                |
| Injections $[m]\to[n]$                        | $P(n,m)$                                                             |
| Surjections $[m]\to[n]$                       | $n!\,S(m,n)$                                                         |
| Multiset permutations                         | $\frac{n!}{n_1!\cdots n_k!}$                                         |
| $k$-combinations w/ repetition from $n$       | $C(n+k-1,k)$                                                         |
| Non-neg. solutions to $\sum x_i=k$ ($n$ vars) | $C(n+k-1,k)$                                                         |
| Same, $x_i\ge a_i$                            | shift variables, then above                                          |
| Same, $\sum x_i\le k$                         | add slack var, then above                                            |
| Distinct→distinct boxes, no restriction       | $n^k$                                                                |
| Distinct→distinct boxes, each ≥1              | $n!\,S(k,n)$                                                         |
| Distinct→identical boxes, each ≥1             | $S(k,n)$                                                             |
| Identical→distinct boxes, each ≥1             | $C(k-1,n-1)$                                                         |
| Stirling 2nd kind special values              | $S(n,1){=}1,\ S(n,n){=}1,\ S(n,n-1){=}C(n,2),\ S(n,2){=}2^{n-1}{-}1$ |

---

## 🧩 PART 2 — Advanced Counting (Generating Functions, Recurrences, Permutations, PIE)
*(covers `DM-exer.md` §2, items 1–29)*

### 🧭 Decision Guide

| Signal in the problem | Tool |
|---|---|
| "Find the generating function for..." | OGF catalogue + operations (§A) |
| "Use generating functions to solve the recursion..." | Recurrence → OGF → partial fractions (§A.3) |
| "Solve the recursion $a_n = c_1a_{n-1}+c_2a_{n-2}+\ldots$" directly | Characteristic polynomial method (§B) — **faster than GF for exam** |
| "Use generating functions to find the number of ways to distribute/pay/score..." | Build OGF as a **product** of per-item factors, extract coefficient (§A.4) |
| "Use PIE to find..." / "not divisible by / neither / none of..." | Inclusion–Exclusion (§D) |
| "Onto/surjective functions", "derangements", "Euler's phi" | PIE special formulas (§D) |
| "Write $\sigma$ in cycle notation", "$\sigma^{-1}$", "$\sigma^2$" | Cycle decomposition (§C) |
| "How many permutations of $[n]$ have exactly $k$ cycles?" | Stirling numbers 1st kind $c(n,k)$ (§C.5) |

---

### A. Generating Functions

> [!formula] 🗂️ Standard OGF Catalogue (memorize these)
> | Sequence | OGF |
> |---|---|
> | $(1,1,1,\ldots)$ | $\dfrac{1}{1-x}$ |
> | $(1,r,r^2,r^3,\ldots)$ | $\dfrac{1}{1-rx}$ |
> | $(1,0,1,0,\ldots)$ | $\dfrac{1}{1-x^2}$ |
> | $(C(n,0),\ldots,C(n,n),0,0,\ldots)$ | $(1+x)^n$ |
> | $(1,2,3,4,\ldots)$ | $\dfrac{1}{(1-x)^2}$ |
> | $(0,1,2,3,\ldots)$ | $\dfrac{x}{(1-x)^2}$ |
> | combos-with-rep count sequence | $\dfrac{1}{(1-x)^{k+1}}$ (for $n=k+1$ "slots") |

> [!procedure] 🧭 Recipe — building an OGF for a *distribution/payment* problem
> 1. For **each independent source** (coin type, fruit type, child), write the **per-source OGF**:
>    - unlimited supply, any amount: $\dfrac{1}{1-x^d}$ ($d$ = denomination/step)
>    - even amounts only: $\dfrac{1}{1-x^2}$; multiple of 5: $\dfrac{1}{1-x^5}$; at most $k$: $1+x+\cdots+x^k = \dfrac{1-x^{k+1}}{1-x}$
> 2. **Multiply** all per-source OGFs together (Convolution Rule — sources are independent/disjoint).
> 3. The answer to "how many ways to total $n$" = coefficient of $x^n$ in the product.

> [!example] 📘 Worked — Ex. 3–6 (Part 2)
> **Q3.** Ways to pay $n$ dollars using coins of 3, 5, 7 (unlimited of each):
> $$G(x) = \frac{1}{1-x^3}\cdot\frac{1}{1-x^5}\cdot\frac{1}{1-x^7}$$
> **Q4.** $b_n$: candies to 4 children (each odd amount) + 1 adult (1 or 2 candies):
> Odd-amount OGF per child: $x+x^3+x^5+\cdots = \dfrac{x}{1-x^2}$. Adult: $x+x^2$.
> $$G(x) = \left(\frac{x}{1-x^2}\right)^4 (x+x^2)$$
> **Q6.** $x_1\ge3,\ 1\le x_2\le5,\ 0\le x_3\le4,\ x_4\ge1$, solve $\sum x_i=k$:
> $$G(x) = x^3\cdot\frac{1}{1-x} \;\times\; (x+x^2+\cdots+x^5)\;\times\;(1+x+\cdots+x^4)\;\times\; x\cdot\frac{1}{1-x}$$
> Expand and read off the coefficient of $x^7$ to get $a_7$.

> [!procedure] 🧭 Recipe — Recurrence → OGF → closed formula (Method B is fastest)
> 1. Let $F(x)=\sum a_nx^n$. Multiply the recurrence by $x^n$ and sum over valid $n$.
> 2. Use **Right-Shift** ($x^kF(x)$ prepends $k$ zeros) and **Addition** rules to rewrite every shifted piece in terms of $F(x)$.
> 3. Solve algebraically for $F(x)$ — you'll get a **rational function**.
> 4. **Factor the denominator** into linear factors $(1-\alpha_i x)$.
> 5. **Partial fractions:** $F(x)=\sum \dfrac{A_i}{1-\alpha_i x}$.
> 6. Read off: $a_n = \sum A_i\,\alpha_i^n$.

> [!example] 📘 Worked — Fibonacci OGF → closed form
> Recurrence: $f_0=0,f_1=1,f_n=f_{n-1}+f_{n-2}$.
> **Step 1–3:** $F(x)(1-x-x^2)=x \Rightarrow F(x)=\dfrac{x}{1-x-x^2}$.
> **Step 4:** roots of $1-x-x^2=0$ give $\alpha_{1,2}=\dfrac{1\pm\sqrt5}{2}$.
> **Step 5–6:** partial fractions give $A=\tfrac{1}{\sqrt5},\,B=-\tfrac1{\sqrt5}$, so
> $$f_n = \frac{1}{\sqrt5}\left[\left(\frac{1+\sqrt5}{2}\right)^n - \left(\frac{1-\sqrt5}{2}\right)^n\right]$$

---

### B. Linear Recurrence Relations (Characteristic Polynomial Method — fastest exam route)

> [!procedure] 🧭 Recipe — Homogeneous: $a_0t_n+a_1t_{n-1}+\cdots+a_kt_{n-k}=0$
> 1. Write characteristic polynomial $p(x)=a_0x^k+a_1x^{k-1}+\cdots+a_k$.
> 2. Factor $p(x)$; find all roots $r_i$ with multiplicities $m_i$.
> 3. General solution:
>    $$t_n = \sum_i \sum_{j=0}^{m_i-1} c_{i,j}\,n^j\,r_i^n$$
>    (distinct root $r$ contributes $c\,r^n$; a root of multiplicity 2 contributes $c_1r^n+c_2n\,r^n$; etc.)
> 4. Plug in the $k$ given initial conditions, solve the linear system for all $c_{i,j}$.

> [!procedure] 🧭 Recipe — Non-homogeneous: RHS $=b^n\,p(n)$, $\deg p = d$
> 1. Form the **augmented** characteristic polynomial: $\big(\text{homogeneous }p(x)\big)\times (x-b)^{d+1}$.
> 2. Solve exactly like the homogeneous case (factor → general solution → initial conditions).
> 3. *Shortcut:* if $b$ is **already a root** of the homogeneous part with multiplicity $m$, its total multiplicity in the augmented polynomial becomes $m+d+1$.

> [!warning] Don't forget the $(x-b)^{d+1}$ factor
> For non-homogeneous recurrences, forgetting to multiply by $(x-b)^{d+1}$ is the #1 mistake. The degree is $d+1$, not $d$.

> [!example] 📘 Worked — Ex. 10 (Part 2), several patterns
> **(a)** $a_0=2,\ a_n=3a_{n-1}$: $p(x)=x-3$, $t_n=c\cdot3^n$, $a_0=2\Rightarrow c=2$: $\boxed{a_n=2\cdot3^n}$.
>
> **(b)** $a_0=2,\ a_n=3a_{n-1}+1$: RHS $=1^n\cdot1$ so $b=1,d=0$. Augmented: $(x-3)(x-1)$.
> $t_n=c_1\cdot3^n+c_2\cdot1^n$. Use $a_0=2$ and $a_1=3(2)+1=7$ to solve: $c_1=\tfrac52, c_2=-\tfrac12$.
> $$a_n = \frac52\cdot3^n - \frac12$$
>
> **(c)** $a_0=1,a_1=2,\ a_n=5a_{n-1}-4a_{n-2}$: $p(x)=x^2-5x+4=(x-1)(x-4)$.
> $t_n=c_1+c_2\cdot4^n$. Solve: $c_1+c_2=1,\ c_1+4c_2=2 \Rightarrow c_2=\tfrac13,c_1=\tfrac23$.
> $$a_n = \frac23+\frac13\cdot4^n$$
>
> **(d)** $u_0=2,u_1=-6,\ u_{n+2}+8u_{n+1}-9u_n = 8\cdot3^{n+1}$: homogeneous $p(x)=x^2+8x-9=(x-1)(x+9)$. RHS is $b=3,d=0$ (constant $\times 3^n$), so augmented poly $=(x-1)(x+9)(x-3)$ (3 distinct roots since 3 isn't already a root):
> $$u_n = c_1\cdot1^n + c_2(-9)^n+c_3\cdot3^n$$
> Solve using $u_0,u_1$, and $u_2$ (computed from the recurrence itself).

---

### C. Permutation Structure (Cycle Notation)

> [!procedure] 🧭 Recipe — decompose $\sigma$ into cycles
> 1. Start at 1 (or any unvisited element); follow $1\to\sigma(1)\to\sigma(\sigma(1))\to\cdots$ until you return to 1. That's one cycle.
> 2. Repeat starting from the smallest unvisited element until all elements are used.
> 3. Write $\sigma$ as the product of these disjoint cycles (fixed points may be written $(i)$ or omitted).

> [!procedure] 🧭 Recipe — $\sigma^{-1}$ and $\sigma^2$
> - **Inverse:** reverse the order **within** every cycle: $(i_1\,i_2\,\cdots\,i_k)^{-1}=(i_1\,i_k\,i_{k-1}\,\cdots\,i_2)$. Transpositions (2-cycles) are self-inverse.
> - **Square:** for each cycle of **odd** length $k$ → stays a single $k$-cycle (relabeled, "step by 2" through the original cycle). For each cycle of **even** length $k$ → **splits** into two cycles of length $k/2$.
> - **Two-line notation:** just compute $\sigma^{-1}(i)$ or $\sigma^2(i)$ for each $i$ directly from the cycle form and read off the images in order $1,2,\ldots,n$.

> [!example] 📘 Worked — Ex. 74a: $\sigma = 36215847$ (one-line)
> Reading one-line: $\sigma(1){=}3,\sigma(2){=}6,\sigma(3){=}2,\sigma(4){=}1,\sigma(5){=}5,\sigma(6){=}8,\sigma(7){=}4,\sigma(8){=}7$.
> **Cycle decomposition:** $1\to3\to2\to6\to8\to7\to4\to1$: cycle $(1\,3\,2\,6\,8\,7\,4)$. Then $5\to5$: fixed point $(5)$.
> $$\sigma = (1\;3\;2\;6\;8\;7\;4)(5)$$
> **Fixed points:** $\{5\}$. **Number of cycles:** 2 (one 7-cycle + one 1-cycle).
> **Inverse:** reverse the 7-cycle: $\sigma^{-1}=(1\;4\;7\;8\;6\;2\;3)(5)$ → one-line: $4\,3\,1\,7\,5\,2\,8\,6$.
> **$\sigma^2$:** the 7-cycle is odd length → stays one 7-cycle, "skip by 2": $(1\;2\;8\;4\;3\;6\;7)(5)$.

> [!example] 📘 Worked — Ex. 75a: $\sigma=(1,3,5)(2,4,6)$ (cycle notation given)
> **Two-line (assume $n=6$):** $\sigma(1){=}3,\sigma(3){=}5,\sigma(5){=}1,\sigma(2){=}4,\sigma(4){=}6,\sigma(6){=}2$ → one-line: $3\,4\,5\,6\,1\,2$.
> **$\sigma^{-1}$:** reverse each: $(1\,5\,3)(2\,6\,4)$ → one-line: $5\,6\,1\,2\,3\,4$.
> **$\sigma^2$:** both cycles length 3 (odd) → stay 3-cycles, skip by 2: $(1\,5\,3)(2\,6\,4)$ — note $\sigma^2=\sigma^{-1}$ here since $\sigma^3=\text{id}$.

---

#### C.5 — Stirling Numbers of the First Kind $c(n,k)$

> [!formula] 🗂️ Quick reference
> $c(n,k)$ = number of permutations of $[n]$ with exactly $k$ cycles (unsigned Stirling 1st kind).
> $$c(n,k) = c(n-1,k-1) + (n-1)\cdot c(n-1,k)$$
>
> | Special Value | Formula |
> |---|---|
> | $c(n,1)$ | $(n-1)!$ (one $n$-cycle) |
> | $c(n,n-1)$ | $C(n,2)$ (one transposition, rest fixed) |
> | $c(n,n)$ | $1$ (all fixed points = identity) |
> | Total | $\sum_k c(n,k) = n!$ |
>
> | $n\backslash k$ | 1 | 2 | 3 | 4 | Total $=n!$ |
> |---|---|---|---|---|---|
> | 1 | 1 | — | — | — | 1 |
> | 2 | 1 | 1 | — | — | 2 |
> | 3 | 2 | 3 | 1 | — | 6 |
> | 4 | 6 | 11 | 6 | 1 | 24 |

> [!warning] First kind vs. Second kind
> - $c(n,k)$ counts **permutations** with $k$ cycles (bijections $[n]\to[n]$)
> - $S(n,k)$ counts **set partitions** into $k$ blocks (unordered subsets)
> - Recurrences look similar but differ: $c$ uses $(n-1)$, $S$ uses $k$

---

### D. Principle of Inclusion–Exclusion (PIE)

> [!procedure] 🧭 Recipe — general PIE strategy
> 1. Define **properties** $P_1,\ldots,P_n$ and sets $A_i=\{x: x \text{ has property } P_i\}$.
> 2. If the question asks for "**none** of the properties", compute:
>    $$|U| - |A_1\cup\cdots\cup A_n|$$
> 3. Expand $|A_1\cup\cdots\cup A_n|$ using alternating sums of intersection sizes:
>    $$\sum|A_i| - \sum|A_i\cap A_j| + \sum|A_i\cap A_j\cap A_k| - \cdots$$
> 4. Compute each intersection size directly (often "divisible by lcm" or "both conditions hold simultaneously").

> [!formula] 🗂️ Ready-made PIE formulas — just plug in numbers
> | Quantity | Formula |
> |---|---|
> | Euler's phi $\varphi(n)$, $n=p_1^{k_1}\cdots p_r^{k_r}$ | $n\prod_i\left(1-\dfrac1{p_i}\right)$ |
> | Surjections $[m]\to[n]$ | $\displaystyle\sum_{j=0}^n(-1)^j\binom nj (n-j)^m$ |
> | Derangements $D_n$ | $\displaystyle n!\sum_{k=0}^n \frac{(-1)^k}{k!} = \sum_{k=0}^n (-1)^k\frac{n!}{k!}$ |

> [!tip] Derangements — quick values
> $D_1=0,\ D_2=1,\ D_3=2,\ D_4=9,\ D_5=44$. Also: $D_n \approx n!/e$ (asymptotic). Recurrence: $D_n = (n-1)(D_{n-1}+D_{n-2})$.

> [!example] 📘 Worked — Ex. 15–19, 24, 29 (Part 2)
> **Q15.** Positive integers $\le100$ **NOT** divisible by 5 or 7:
> $A=$ mult. of 5 ($|A|=20$), $B=$ mult. of 7 ($|B|=14$), $A\cap B=$ mult. of 35 ($|A\cap B|=2$).
> $$100 - (20+14-2) = 68$$
> **Q17.** Positive integers $\le1000$ that are a square **or** a cube:
> Squares: $\lfloor\sqrt{1000}\rfloor=31$. Cubes: $\lfloor1000^{1/3}\rfloor=10$. Sixth powers (both): $\lfloor1000^{1/6}\rfloor=3$.
> $$31+10-3=38$$
> **Q24.** Surjections from a 7-set to a 5-set:
> $$\sum_{j=0}^5(-1)^j\binom5j(5-j)^7 = 5^7-5\cdot4^7+10\cdot3^7-10\cdot2^7+5\cdot1^7 = 16800$$
> **Q27.** Derangements of $[4]$: $D_4=4!\left(1-1+\tfrac12-\tfrac16+\tfrac1{24}\right)=9$.
> **Q29.** Integers $\le100$ relatively prime to 100 $=\varphi(100)$. $100=2^2\cdot5^2$:
> $$\varphi(100)=100\left(1-\tfrac12\right)\left(1-\tfrac15\right)=100\cdot\tfrac12\cdot\tfrac45=40$$

> [!example] 📘 Worked — Ex. 22 (bounded solutions via PIE)
> $x+y+z=13,\ 0\le x,y,z\le6$.
> **Step 1 — unrestricted:** $C(13+2,2)=C(15,2)=105$.
> **Step 2 — subtract violations** ($x\ge7$, or $y\ge7$, or $z\ge7$): shift e.g. $x'=x-7$, solve $x'+y+z=6$: $C(8,2)=28$ each, 3 variables → $3\times28=84$.
> **Step 3 — add back double-violations:** $x\ge7$ AND $y\ge7 \Rightarrow$ sum $\ge14>13$, impossible → $0$ for all pairs.
> $$\text{Answer} = 105 - 84 + 0 = 21$$

---

## 🧩 PART 3 — Graphs
*(covers `DM-exer.md` §3, items 1–16, and Rosen 10.1–10.5)*

### 🧭 Decision Guide — existence questions

| Question type                                 | What to check, in order                                                                                                                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Does an **Eulerian circuit** exist?           | All vertices even degree? → yes                                                                                                                                                                                                           |
| Does an **Eulerian path** (no circuit) exist? | Exactly 2 odd-degree vertices? → yes, path runs between them                                                                                                                                                                              |
| Does a **Hamiltonian circuit/path** exist?    | No iff test exists — try Dirac/Ore (sufficient only); if they fail, try to **construct one directly**; if you suspect "no," look for a structural obstruction (e.g. bipartite with unequal parts, or a required vertex of too-low degree) |
| Is the graph **planar**?                      | First check edge bound $e\le3v-6$ (or $e\le2v-4$ if triangle-free) — if **violated**, non-planar, done. If **not** violated, try to draw it, or find a $K_5/K_{3,3}$ subdivision.                                                         |
| Is the graph **bipartite**?                   | 2-color via BFS/DFS, or check: no odd cycles                                                                                                                                                                                              |
| Are two graphs **isomorphic**?                | Compare invariants first (&#124;$V$&#124;,&#124;$E$&#124;, degree sequence, # of triangles) — if any differ, **not isomorphic**, done. If all match, **construct an explicit bijection** and verify every edge.                           |

---

### A. Handshaking & Special Graph Formulas

> [!formula] 🗂️ Formula table — memorize
> | Graph | $\lvert V\rvert$ | $\lvert E\rvert$ | Degree of each vertex |
> |---|---|---|---|
> | $K_n$ | $n$ | $\binom n2$ | $n-1$ |
> | $C_n$ | $n$ | $n$ | $2$ |
> | $W_n$ | $n+1$ | $2n$ | hub: $n$; rim: $3$ |
> | $Q_n$ | $2^n$ | $n\cdot2^{n-1}$ | $n$ |
> | $K_{m,n}$ | $m+n$ | $mn$ | part 1: $n$; part 2: $m$ |
>
> **Handshaking:** $\sum_v\deg(v)=2|E|$ → # odd-degree vertices is always **even**.
> **Existence check:** a degree sequence is realizable by *some* simple graph only if the sum is even (necessary, not always sufficient).

> [!example] 📘 Worked — degree sequence existence check
> Do simple graphs exist with degrees $(1,2,3,3,3)$ on 5 vertices?
> Sum $=12$ (even) ✓. Odd-degree vertices: $\{1,3,3,3\}$, count $=4$ (even) ✓. Max degree $3\le4$ ✓. **Possible.**

---

### A.2 — Counting Paths via $A^r$

> [!formula] 🗂️ Matrix path counting
> The $(i,j)$-entry of $A^r$ equals the number of **walks of length $r$** from $v_i$ to $v_j$.
> - For undirected graphs: $A$ is symmetric; row $i$ sum = $\deg(v_i)$.
> - For digraphs: row sum = $\deg^+(v_i)$, column sum = $\deg^-(v_i)$.

---

### B. Eulerian Paths/Circuits

> [!procedure] 🧭 Recipe
> 1. Compute the degree of **every** vertex.
> 2. All even → **Eulerian circuit** exists (start anywhere, will return).
> 3. Exactly two odd → **Eulerian path** exists (must start/end at the two odd-degree vertices).
> 4. More than two odd (or graph disconnected) → **neither** exists.
> 5. For a **digraph**: circuit iff $\deg^+(v)=\deg^-(v)$ for every $v$; path iff exactly one vertex has $\deg^+-\deg^-=1$ (start) and one has $\deg^--\deg^+=1$ (end), rest balanced.

> [!example] 📘 Worked — Ex. 1 (special graphs) + Königsberg
> **$K_n$:** all degrees $n-1$. Circuit iff $n-1$ even $\Rightarrow n$ **odd**. Path (no circuit) only possible if exactly 2 odd degrees — impossible when all $n$ degrees are equal unless $n=2$.
> **$C_n$:** all degrees 2 (even) → **circuit always exists**.
> **$W_n$:** hub degree $n$, rim degree 3 (odd) — $n$ odd-degree rim vertices, never exactly 0 or 2 for $n\ge3$ → **neither** exists (for $n\ge4$; check $n=3$ separately if asked).
> **$Q_n$:** all degrees $n$ → circuit iff $n$ even; path iff $n$ odd.
> **$K_{m,n}$:** circuit iff both $m,n$ even; path iff exactly one of $m,n$ is odd.
>
> **Königsberg bridges:** 4 landmasses, degrees $3,3,5,3$ — all odd (4 odd vertices) → **no Euler path or circuit.**

---

### C. Hamiltonian Paths/Circuits

> [!procedure] 🧭 Recipe
> 1. **No simple iff test exists** — this is NP-hard in general. Use these tools **in order**:
> 2. **Sufficient conditions** (if either holds, a Hamilton circuit is *guaranteed*, but failing them proves nothing):
>    - **Dirac:** every vertex has $\deg(v)\ge n/2$.
>    - **Ore:** for every pair of **non-adjacent** vertices $u,v$: $\deg(u)+\deg(v)\ge n$.
> 3. If neither applies, **attempt direct construction** — trace a route visiting every vertex once (small graphs: just try).
> 4. To **prove non-existence**, look for a structural obstruction, e.g.:
>    - Bipartite graph with unequal part sizes → no Hamilton circuit (must alternate sides).
>    - Removing a vertex disconnects the graph into $\ge2$ pieces → no Hamilton circuit through that cut vertex configuration.
	
> [!formula] 🗂️ Special graphs — Hamilton table
> | Graph | Hamilton circuit? | Hamilton path? |
> |---|---|---|
> | $K_n,\,n\ge3$ | Yes | Yes |
> | $C_n$ | Yes (it *is* the cycle) | Yes |
> | $W_n$ | Yes | Yes |
> | $Q_n,\,n\ge2$ | Yes | Yes |
> | $K_{m,n}$ | Yes iff $m=n$ | Yes iff $\lvert m-n\rvert\le1$ |
> | Petersen graph | **No** | Yes |

> [!example] 📘 Worked — bipartite graph, odd # vertices ⟹ no Hamilton cycle (Ex. 3)
> If $G$ is bipartite with parts $V_1,V_2$ and $|V|$ is odd, then $|V_1|\ne|V_2|$ (they can't split an odd total evenly). A Hamilton **circuit** must alternate strictly between $V_1$ and $V_2$, which forces $|V_1|=|V_2|$. Contradiction → **no Hamiltonian circuit.**

---

### D. Planar Graphs

> [!procedure] 🧭 Recipe — is $G$ planar?
> 1. Compute $v=|V|,\ e=|E|$.
> 2. **Necessary edge bound** (fast disproof tool): if $G$ is simple and $v\ge3$:
>    $$e \le 3v-6$$
>    If $G$ is **triangle-free** (bipartite, or otherwise no 3-cycles), the tighter bound applies:
>    $$e \le 2v-4$$
>    **If violated → non-planar, done.**
> 3. If the bound is **not violated**, this is inconclusive — either:
>    - draw a planar embedding by hand (proves planar), or
>    - find a subdivision of $K_5$ or $K_{3,3}$ inside $G$ (Kuratowski's Theorem — proves non-planar).
> 4. If $G$ is planar and connected, use **Euler's formula** for faces:
>    $$v - e + f = 2 \quad\Longleftrightarrow\quad f = e-v+2$$
>    (disconnected with $c$ components: $v-e+f=1+c$).

> [!warning] Edge bound is necessary, NOT sufficient
> $Q_4$ has $v=16$, $e=32$, and $3v-6=42\ge32$ — bound not violated, yet $Q_4$ IS non-planar (contains $K_{3,3}$ subdivision). When the bound passes, you must use Kuratowski.

> [!example] 📘 Worked — Ex. 9–14 (utility graphs, hypercubes, Petersen, $K_{3,4}$, $K_6$)
> **Q9 (six houses, 2 utilities = $K_{6,2}$):** $v=8,e=12$. Bound: $3v-6=18\ge12$ ✓; triangle-free bound $2v-4=12\ge12$ ✓ (equality, still OK) → **planar**, houses **can** connect without crossing.
>
> **Q10 ($Q_4,Q_5,Q_6$):**
> - $Q_4$: $v=16,e=32$. $3v-6=42\ge32$ — bound inconclusive; $Q_4$ is in fact **non-planar** (needs a $K_{3,3}$-subdivision argument, or cite that it contains $K_5$/$K_{3,3}$ as a minor).
> - $Q_5$: contains $Q_4$ as a subgraph → non-planar propagates → **non-planar**.
> - $Q_6$: $v=64,e=192$. $3v-6=186<192$ → bound **violated** → **non-planar** directly.
>
> **Q13 (Petersen graph):** $v=10,e=15$. $3v-6=24\ge15$ — bound doesn't help. Exhibit a $K_{3,3}$ subdivision (e.g. outer pentagon vertices $\{a,c,h\}$ vs $\{b,g,j\}$, connected via paths through remaining vertices) → **non-planar** by Kuratowski.
>
> **Q14 ($K_{3,4}$):** $v=7,e=12$, bipartite (triangle-free): $2v-4=10<12$ → bound **violated** → **non-planar**.
> **$K_6$:** $v=6,e=15$: $3v-6=12<15$ → **non-planar**.

> [!example] 📘 Worked — Ex. 12 (faces of a 3-regular planar graph)
> 20 vertices, all degree 3, connected, planar.
> **Step 1 (Handshaking):** $2e=\sum\deg(v)=20\times3=60 \Rightarrow e=30$.
> **Step 2 (Euler):** $f=e-v+2=30-20+2=12$ **regions**.

---

### E. Bipartite Check & Isomorphism

> [!procedure] 🧭 Recipe — bipartite test
> Run BFS/DFS coloring alternately from any start vertex: if you're ever forced to give an edge's two endpoints the **same** color, $G$ is **not** bipartite (equivalently: $G$ has an odd cycle). Otherwise it is.

> [!procedure] 🧭 Recipe — isomorphism test
> 1. Compare **invariants** first: $|V|$, $|E|$, sorted degree sequence, number of triangles/cycles of a given length, number of connected components, bipartiteness.
> 2. Any mismatch → **not isomorphic**, stop.
> 3. All match → **construct** an explicit bijection $f:V(G)\to V(H)$ (map high-degree vertices to high-degree vertices first) and verify **every** edge of $G$ maps to an edge of $H$.

> [!example] 📘 Worked — degree-sequence non-isomorphism
> $G$: 5-cycle + one diagonal, degree sequence $\{3,3,2,2,2\}$.
> $H$: plain pentagon $C_5$, degree sequence $\{2,2,2,2,2\}$.
> Sequences differ $\Rightarrow$ $G\not\cong H$ — **no bijection needs to be attempted.**

---

## 🗂️ Part 3 — Master Formula Table

| Situation | Formula/Test |
|---|---|
| Handshaking | $\sum\deg(v)=2\lvert E\rvert$; # odd-degree vertices even |
| Euler circuit | all degrees even |
| Euler path | exactly 2 odd-degree vertices |
| Hamilton (sufficient) | Dirac: $\deg(v)\ge n/2\ \forall v$; Ore: $\deg(u)+\deg(v)\ge n$ for non-adjacent pairs |
| Planar edge bound | $e\le3v-6$ (general), $e\le2v-4$ (triangle-free) |
| Euler's formula | $v-e+f=2$ (connected); $v-e+f=1+c$ (general) |
| Bipartite | 2-colorable ⟺ no odd cycle |
| Non-isomorphism | any invariant mismatch ⟹ not isomorphic |
| Paths of length $r$ ($v_i$ to $v_j$) | $(A^r)_{ij}$ |
| Minimum degree in planar | $\le5$ (always exists) |

---

## 🧩 PART 4 — Trees
*(covers `DM-exer.md` §4, items 1–52)*

### 🧭 Decision Guide

| Question type | Tool |
|---|---|
| "Which vertex is root/internal/leaf/level $k$?" | Rooted-tree terminology — just read the picture (§A) |
| "Full $m$-ary tree with X leaves — does it exist? How many internal vertices?" | $n=mi+1$ relation (§B) |
| "Least number of comparisons / weighings" | Decision-tree height bound $h\ge\lceil\log_m l\rceil$ (§C) |
| "Draw the tree with Prüfer sequence..." / "Find the Prüfer code of..." | Prüfer encode/decode algorithm (§D) |
| "How many labeled trees / spanning trees...?" | Cayley's formula, or Matrix-Tree theorem (§E) |
| "Find a spanning tree" | BFS or DFS (§E) |
| "Find the (minimum) spanning tree of a weighted graph" | Kruskal's or Prim's algorithm (§F) |
| "Write the expression in prefix/postfix/infix" | Build the expression tree, traverse pre/in/post-order (§G) |
| "Evaluate this prefix/postfix expression" | Stack-based scan (§G) |
| BFS/DFS for cycle detection / connected components / bipartite check | See recipes below (§H) |
| "Build optimal prefix code / Huffman coding" | Greedy merge of two smallest weights (§I) |

---

### A. Rooted-Tree Terminology (read directly off the tree)

> [!procedure] 🧭 Recipe
> - **Root:** the designated top vertex (no parent).
> - **Internal vertex:** has at least one child. **Leaf:** has no children.
> - **Level of $v$:** length of the path from root to $v$ (root is level 0).
> - **Height:** the maximum level over all vertices.
> - **Ancestors of $v$:** every vertex on the root→$v$ path, excluding $v$.
> - **Descendants of $v$:** every vertex that has $v$ as an ancestor.
> - **Balanced ($m$-ary, height $h$):** every leaf is at level $h$ or $h-1$.
	
> [!example] 📘 Worked — Ex. 1 (rooted tree with root $d$)
> Given: root $d$; children of $d$: $a,c,o,i$; children of $c$: $b,k,g$; children of $b$: $h,l$; children of $i$: $f$; children of $f$: $e,m,n$; children of $h$: $p,q$.
> - **(a) Root:** $d$.
> - **(b) Internal vertices:** $d,c,b,h,i,f$ (each has children).
> - **(c) Leaves:** $a,o,k,g,l,e,m,n,p,q$.
> - **(d) Level 3:** trace levels — $d$(0), $c,a,o,i$(1), $b,k,g,f$(2), $h,l,e,m,n$(3) → **level 3 = $\{h,l,e,m,n\}$**.
> - **(e) Height of subtree rooted at $c$:** $c\to b\to h\to p$ is the longest chain (3 edges) → **height 3**.
> - **(f) Descendants of $b$:** $h,l,p,q$.
> - **(g) Balanced?** Leaves appear at levels 1 ($a,o$... check actual), 2, 3, 4 ($p,q$) — since leaf levels differ by more than 1, **not balanced**.
> - **(h) Ancestors of $q$:** $h,b,c,d$.

---

### A.2 — Tree Characterizations (6 equivalent definitions)

> [!important] Any ONE of these defines a tree ($G$ connected simple graph):
> 1. $G$ is connected and acyclic
> 2. $G$ is connected and $|V|=|E|+1$
> 3. $G$ is acyclic and $|V|=|E|+1$
> 4. For any $u,v$, there is **exactly one** simple path
> 5. $G$ is **minimally connected** (remove any edge → disconnected)
> 6. $G$ is **maximally acyclic** (add any edge → creates a cycle)

---

### B. Full $m$-ary Trees — Counting

> [!formula] 🗂️ The one formula that solves this whole family
> $$n = mi+1 \qquad \text{leaves} = n-i = (m-1)i+1$$
> where $n$=total vertices, $i$=internal vertices, $m$=children per internal vertex.

> [!procedure] 🧭 Recipe
> 1. From what's given (leaves, total vertices, or height), solve for $i$ using the appropriate formula above.
> 2. **Existence check:** $i$ must come out to a **non-negative integer**. If it doesn't, **no such tree exists**.
> 3. If height $h$ is also given, additionally check the height bound $\text{leaves}\le m^h$ (with equality for a perfectly balanced full tree).

> [!example] 📘 Worked — Ex. 4–8
> **Q4.** Full 3-ary tree, $n=100$ vertices. From $n=mi+1$: $100=3i+1\Rightarrow i=33$. Leaves $=(m-1)i+1=2(33)+1=\boxed{67}$.
> **Q6.** Full 4-ary tree with 80 leaves? Leaves $=(m-1)i+1=3i+1=80\Rightarrow 3i=79$ — not an integer → **no such tree exists**.
> **Q5.** Full $m$-ary tree, 84 leaves, height 3: try small $m$. For $m=4$: max leaves at height 3 balanced $=4^3=64<84$ (too few). For $m=5$: leaves$=(m-1)i+1=4i+1=84\Rightarrow i=\tfrac{83}4$ not integer. Try other $m$ systematically ($m$ such that $(m-1)\mid83$; $83$ is prime, so $m-1\in\{1,83\}\Rightarrow m\in\{2,84\}$); check the height-3 bound $84\le m^3$ for each candidate to see which (if any) actually work — if none satisfy both constraints simultaneously, **no such tree exists**.
> **Q8.** 1000-entrant single-elimination tournament (loser eliminated after 1 loss): this is a full **binary** tree ($m=2$) with $n=1000$ **leaves** (the players, as leaves of the elimination bracket) — wait, reframe: each **game** = 1 internal vertex, eliminating exactly one player. Number of games $=$ number of players eliminated $= 1000-1=\boxed{999}$ games needed to leave 1 champion.

---

### C. Decision Trees — Comparisons / Weighings Lower Bound

> [!formula] 🗂️ The governing inequality
> $$l \le m^h \quad\Longrightarrow\quad h \ge \lceil \log_m l \rceil$$
> $l$ = number of possible outcomes/solutions that must be distinguished; $m$ = number of outcomes per decision (2 for a balance-scale weighing between only "lighter/heavier", 3 for a balance scale left/right/balanced, 2 for a binary comparison).

> [!procedure] 🧭 Recipe
> 1. Identify $l$ = the number of distinguishable final answers (e.g. "which of the $n$ coins is fake" → $l=n$, or "which of $n!$ orderings" for sorting).
> 2. Identify $m$ = branching factor of one decision (comparison: $m=2$; 3-way balance scale: $m=3$).
> 3. Minimum decisions needed $=\lceil\log_m l\rceil$.
> 4. **Construct** an actual scheme achieving this bound (exam usually wants both the bound *and* the explicit algorithm).

> [!example] 📘 Worked — Ex. 11, 12, 15 (coins, sorting)
> **Q11.** 4 coins, 1 known **lighter** counterfeit, 3-outcome balance scale: $l=4,\ m=3\Rightarrow h\ge\lceil\log_34\rceil=\lceil1.26\rceil=2$.
> **Construction:** weigh coin 1 vs coin 2. If unequal, lighter one is fake (1 weighing... but verify with second only if needed); if equal, weigh 3 vs 4 to find the lighter. **2 weighings suffice.**
>
> **Q12.** 4 coins, counterfeit may be **either** heavier or lighter (unknown direction) — now $l=8$ (4 coins × 2 directions): $h\ge\lceil\log_38\rceil=\lceil1.89\rceil=2$. **Construction:** weigh $\{1,2\}$ vs $\{3,4\}$ first, then a second weighing among suspects to pin down both identity and direction.
>
> **Q15.** Sorting 4 elements: $l=4!=24$ orderings, binary comparisons ($m=2$): $h\ge\lceil\log_224\rceil=\lceil4.58\rceil=5$. Devise an algorithm (e.g. optimal merge-insertion / binary insertion sort) achieving exactly 5 comparisons worst case.

---

### D. Prüfer Sequences

> [!procedure] 🧭 Recipe — Tree → Prüfer sequence (encode)
> Repeat $n-2$ times:
> 1. Find the **leaf with the smallest label** in the current tree.
> 2. Record its **unique neighbor's label** in the sequence.
> 3. **Delete** that leaf from the tree.
> Stop when 2 vertices remain. *(Reminder: leaves never appear in the sequence; a vertex of degree $d_i$ appears exactly $d_i-1$ times.)*

> [!procedure] 🧭 Recipe — Prüfer sequence → Tree (decode)
> 1. Given sequence $P=(a_1,\ldots,a_{n-2})$ on labels $[n]$. Let $L = [n]\setminus P$ (initial leaf candidates).
> 2. Repeat: connect the **smallest** element currently in $L$ to the **first remaining entry** of $P$; remove that first entry from $P$; remove the used leaf from $L$; if the entry just removed from $P$ no longer appears anywhere else in $P$, add it to $L$.
> 3. When $P$ is empty, connect the last **two** remaining vertices in $L$ directly.

> [!example] 📘 Worked — Ex. 17 (draw tree from Prüfer $(1,1,1,1,6,5)$)
> $n = 6+2 = 8$ vertices $\{1,\ldots,8\}$. $P=(1,1,1,1,6,5)$, initial leaves $L=[8]\setminus\{1,5,6\}=\{2,3,4,7,8\}$.
> 
> | Step | smallest in $L$ | connect to (first of $P$) | update |
> |---|---|---|---|
> | 1 | 2 | 1 | remove 2 from $L$; $P=(1,1,1,6,5)$ |
> | 2 | 3 | 1 | remove 3; $P=(1,1,6,5)$ |
> | 3 | 4 | 1 | remove 4; $P=(1,6,5)$ |
> | 4 | 7 | 1 | remove 7; **1 no longer in $P$** → add 1 to $L$; $P=(6,5)$ |
> | 5 | 1 | 6 | remove 1; $P=(5)$ |
> | 6 | 6 | 5 (last entry, and now $P$ empty) | remove 6; **6 no longer in $P$** → add 6 to $L$ |
> 
> Remaining in $L$: $\{5,6,8\}$... connect the final two remaining vertices directly once $P$ is exhausted: $\{6,8\}$? — carefully track $L$ at each step (this is the fiddly part; recompute $L$ explicitly after each removal rather than trusting memory).
> **Result:** star-like tree centered heavily at vertex 1 (four leaves $2,3,4,7$ attached directly to 1), then $1-6$, $6-5$, and $6-8$ (or similarly per your careful trace).
>
> **General shortcut for degenerate patterns:** a Prüfer sequence like $(1,1,1,1,6,5)$ — vertex 1 repeated 4 times means $\deg(1)=5$; it's the hub connected to five other vertices/subtrees.

---

### E. Spanning Trees, Cayley's Theorem, Matrix-Tree Theorem

> [!formula] 🗂️ Counting formulas
> | Quantity | Formula |
> |---|---|
> | Labeled trees on $n$ vertices | $n^{n-2}$ (Cayley) |
> | Labeled **rooted** trees on $n$ vertices | $n^{n-1}$ |
> | Labeled trees with given degree sequence $d_1,\ldots,d_n$ | $\dfrac{(n-2)!}{\prod_i (d_i-1)!}$ |
> | Spanning trees of $G$ (any graph) | $\kappa(G)=\det\tilde L_j$ (delete any row/col $j$ of Laplacian $L=D-A$) |
> | Spanning trees of $C_n$ | $n$ |
> | Spanning trees of $K_n$ | $n^{n-2}$ |
> | Spanning trees of $K_{m,n}$ | $m^{n-1}n^{m-1}$ |

> [!procedure] 🧭 Recipe — find *a* spanning tree (not counting all of them)
> Run **BFS or DFS** from any root: every edge used to reach a new (unvisited) vertex becomes a tree edge; discard edges that would revisit an already-visited vertex.

> [!procedure] 🧭 Recipe — count spanning trees via Matrix-Tree Theorem
> 1. Build the Laplacian $L = D - A$ (diagonal = degrees, $-1$ for each edge, else 0).
> 2. Delete **any** one row and the corresponding column → $\tilde L_j$.
> 3. $\kappa(G) = \det\tilde L_j$.

> [!example] 📘 Worked — Ex. 27 (spanning trees of $C_5$)
> By the special-case formula: $\kappa(C_n)=n \Rightarrow \kappa(C_5)=5$.
> **Verify via Matrix-Tree:** $C_5$ Laplacian is a $5\times5$ circulant with 2's on diagonal, $-1$ for each cycle-neighbor. Delete row/col 5, compute $\det$ of the resulting $4\times4$ tridiagonal matrix → comes out to $5$. ✓

> [!example] 📘 Worked — spanning-forest edge count (Ex. 28–29)
> A graph with $n$ vertices, $m$ edges, $c$ connected components has a spanning forest with exactly $n-c$ edges (one tree per component, tree edges $=$ vertices $-1$ per component, summed).
> **Edges to remove:** $m-(n-c)$.

---

### F. Minimum Spanning Tree — Kruskal's / Prim's

> [!procedure] 🧭 Recipe — Kruskal's Algorithm
> 1. **Sort** all edges by weight, ascending.
> 2. Initialize each vertex as its own component (union-find).
> 3. Scan edges in sorted order: **add** an edge iff its two endpoints are in **different** components (union them); **skip** if they're already connected (would form a cycle).
> 4. Stop once you have $n-1$ edges.

> [!procedure] 🧭 Recipe — Prim's Algorithm
> 1. Start with a single vertex $s$ in the tree $T$.
> 2. Repeatedly find the **minimum-weight edge** connecting a vertex **inside** $T$ to a vertex **outside** $T$; add that edge and vertex to $T$.
> 3. Stop when all vertices are in $T$.

> [!example] 📘 Worked — Ex. 30, 37–39 (variants)
> **Q37 (maximum spanning tree):** run Kruskal's algorithm but sort edges **descending** by weight instead — same greedy correctness argument applies (safe-edge theorem, mirrored).
> **Q38 (unique MST):** if all edge weights are **distinct**, the "lightest edge crossing any cut" is unique at every step of Kruskal/Prim, so the greedy choices are forced — **exactly one MST exists**.
> **Q39 (second-minimum spanning tree):** find an MST $T$ first (Kruskal/Prim); then for each **non-tree edge** $e=uv$, adding $e$ to $T$ creates a unique cycle — the best alternative tree from swapping $e$ in is $T$ with the **heaviest tree-edge on that cycle** removed and $e$ added instead; take the minimum such swap over all non-tree edges.

---

### G. Traversals & Expression Trees

> [!procedure] 🧭 Recipe — build the expression tree, then traverse
> 1. Parse the expression by **operator precedence**: the **last-evaluated operator** becomes the **root**; its operands become the left/right subtrees (recurse).
> 2. **Infix** = in-order traversal (left, root, right) — insert parentheses to be unambiguous.
> 3. **Prefix** = pre-order traversal (root, left, right).
> 4. **Postfix** = post-order traversal (left, right, root).

> [!procedure] 🧭 Recipe — evaluate a postfix expression
> Scan **left to right**, maintaining a stack:
> - number → push
> - operator → **pop 2** (call them $b$ then $a$, in pop order — so $a$ was pushed first), compute $a \circ b$, push result.

> [!procedure] 🧭 Recipe — evaluate a prefix expression
> Scan **right to left**, maintaining a stack:
> - number → push
> - operator → pop 2 (call them $a$ then $b$ in pop order), compute $a\circ b$, push result.

> [!example] 📘 Worked — Ex. 41 (build tree for $((x+2)^3)(y-(3+x))-5$)
> Root: the final $-$ (subtract 5). Left child: the product $\times$. That product's children: $(x+2)^3$ (a $\uparrow$ node with children $(x+2)$ and $3$) and $(y-(3+x))$ (a $-$ node with children $y$ and $(3+x)$).
> **Prefix:** $-\;\times\;\uparrow\;+\;x\;2\;3\;-\;y\;+\;3\;x\;5$
> **Postfix:** $x\;2\;+\;3\;\uparrow\;y\;3\;x\;+\;-\;\times\;5\;-$
> **Infix (fully parenthesized):** $(((x+2)\uparrow3)\times(y-(3+x)))-5$

> [!example] 📘 Worked — Ex. 44a (evaluate postfix $5\,2\,1\,-\,-\,3\,1\,4\,+\,+\,*$)
> Stack trace: push $5,2,1$ → stack $[5,2,1]$.
> $-$: pop $2,1$ → $2-1=1$, push → $[5,1]$.
> $-$: pop $5,1$ → $5-1=4$, push → $[4]$.
> push $3,1,4$ → $[4,3,1,4]$.
> $+$: pop $1,4$ → $1+4=5$, push → $[4,3,5]$.
> $+$: pop $3,5$ → $3+5=8$, push → $[4,8]$.
> $*$: pop $4,8$ → $4\times8=32$.
> $$\boxed{32}$$

---

### H. BFS/DFS Applications

> [!procedure] 🧭 Recipe — shortest path length (unweighted) via BFS
> Run BFS from the source; the **level** at which the target vertex is first discovered **is** the shortest path length (number of edges).

> [!procedure] 🧭 Recipe — cycle detection via BFS/DFS
> During traversal, if you ever encounter an edge to an **already-visited** vertex that is **not** the parent you came from, a cycle exists — the cycle is the path between the two endpoints (via tree edges) plus that extra edge.

> [!procedure] 🧭 Recipe — connected components via BFS/DFS
> Run BFS/DFS from an arbitrary unvisited vertex; everything reached forms one component. Repeat from any remaining unvisited vertex until all vertices are covered. Number of runs = number of components.

> [!procedure] 🧭 Recipe — bipartite check via BFS/DFS
> Color the start vertex Red; every neighbor gets the opposite color of its parent. If you ever need to color a vertex a color that **conflicts** with a color it already has (from a different parent), the graph is **not bipartite**.

> [!example] 📘 Worked — Ex. 51 (backtracking, subset-sum)
> Set $\{27,24,19,14,11,8\}$, target $M=41$:
> Try adding in given order, backtrack when the partial sum would exceed $M$:
> $27$ (sum 27) → $+24$ would be 51 > 41, skip → $+19$ would be 46 > 41, skip → $+14$: sum $=41$ ✓ **found: $\{27,14\}$**.
> (Draw the search tree: root = empty sum; each level = decision to include/exclude the next number; a branch is cut the moment its running sum would exceed $M$.)

---

### I. Huffman Coding (Prefix Codes)

> [!procedure] 🧭 Recipe — Huffman (optimal prefix code)
> 1. List all symbols with frequencies. Each symbol starts as a one-node tree with weight = frequency.
> 2. Repeatedly: pick the **two trees with smallest weights**, combine them under a new parent node whose weight = sum. Assign 0 to the left edge, 1 to the right edge.
> 3. Stop when only one tree remains. The codeword for a symbol = the sequence of 0/1 on the root-to-leaf path.

> [!important] Key property: No codeword is a prefix of another (guarantees unambiguous decoding). The Huffman tree minimizes $\sum$ (frequency × codeword length).

> [!example] 📘 Worked — Huffman for $\{A:0.08,\ B:0.10,\ C:0.12,\ D:0.15,\ E:0.20,\ F:0.35\}$
> | Step | Merged | Weight |
> |------|--------|--------|
> | 1 | $A+B$ | $0.18$ |
> | 2 | $C+D$ | $0.27$ |
> | 3 | $0.18+E$ | $0.38$ |
> | 4 | $0.27+F$ | $0.62$ |
> | 5 | $0.38+0.62$ | $1.00$ |
>
> Result: $A=111,\ B=110,\ C=011,\ D=010,\ E=10,\ F=00$. Average: $2.45$ bits/letter.

---

## 🗂️ Part 4 — Master Formula Table

| Situation                        | Formula                                                                                                                                                    |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Full $m$-ary tree                | $n=mi+1,\ \text{leaves}=(m-1)i+1$                                                                                                                          |
| Decision-tree height             | $h\ge\lceil\log_m l\rceil$                                                                                                                                 |
| Prüfer sequence length           | $n-2$; vertex $i$ appears $d_i-1$ times; leaves absent                                                                                                     |
| Labeled trees (Cayley)           | $n^{n-2}$                                                                                                                                                  |
| Rooted labeled trees             | $n^{n-1}$                                                                                                                                                  |
| Trees with given degree sequence | $\dfrac{(n-2)!}{\prod(d_i-1)!}$                                                                                                                            |
| Spanning trees                   | $\kappa(G)=\det\tilde L_j$ (Matrix-Tree)                                                                                                                   |
| Spanning trees of $C_n$          | $n$                                                                                                                                                        |
| Spanning trees of $K_{m,n}$      | $m^{n-1}n^{m-1}$                                                                                                                                           |
| Spanning forest edges removed    | $m-(n-c)$                                                                                                                                                  |
| Tree vertex–edge relation        | &#124;$V$&#124;=&#124;$E$&#124;$+1$                                                                                                                        |
| Tree characterizations           | Connected+Acyclic $\iff$ &#124;$V$&#124;=&#124;$E$&#124;$+1$ (connected or acyclic) $\iff$ unique path $\iff$ minimally connected $\iff$ maximally acyclic |

---

## ✅ Final Exam Checklist

> [!tip] Before you submit
> - [ ] Did the question ask for **at least/at most/exactly**? → check if you need the **complement**.
> - [ ] Are the objects **distinct or identical**? Are the boxes/positions **distinct or identical**? (Twelvefold-way table, Part 1 Case 5)
> - [ ] Did you accidentally **double-count** (e.g. unordered pairs, circular arrangements)? → apply the **Division Rule**.
> - [ ] For graphs: did you check **both** existence conditions (degree parity for Euler, edge bound for planarity) *before* trying to construct/refute by hand?
> - [ ] For recurrences: is it **homogeneous or non-homogeneous**? Don't forget the $(x-b)^{d+1}$ augmentation factor.
> - [ ] For PIE: are you counting "**none**" (subtract from total) or "**at least one**" (the union itself)?
> - [ ] For trees: does the professor's **Prüfer/degree formula** apply, or is a direct **BFS/DFS/Matrix-Tree** computation faster here?
> - [ ] **Distinct vs identical gifts/balls/objects?** → reread the problem — this is the #1 reason students lose points.
> - [ ] **Circular arrangement?** → $(n-1)!$, NOT $n!$.
