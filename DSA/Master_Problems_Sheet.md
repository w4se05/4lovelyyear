---
tags: [dsa, practice-problems, master-sheet]
aliases: [DSA Problem Bank]
course: "61CSE108: Algorithms and Data Structures"
modules: 11
verified: true
created: 2026-06-03
---

# 📚 61CSE108 — Master Problems Sheet

> [!info] How to use this sheet
> One **`##` module per lecture** (Complexity → Dynamic Programming). Every question lives in a `> [!question]` callout; every answer is a **foldable** `> [!success]-` block — *try the problem before you expand it*. Mermaid diagrams sit inside the solutions for all tree / graph / linked-list states. Difficulty is calibrated to be **equal to or harder than** the past quizzes (Quizzes 1–6).
>
> Every numeric answer here was **re-derived from scratch** — do not assume a value is right just because it once appeared on a marked quiz. Where a past quiz answer was *wrong*, the correction is flagged with `> [!bug]`.

> [!tip] Topic graph
> Core links to pre-populate your vault: [[Complexity Analysis]] · [[Searching Algorithms]] · [[Sorting Algorithms]] · [[Priority Queues]] · [[Heaps]] · [[Linked Lists]] · [[Stacks and Queues]] · [[Hashing]] · [[Trees]] · [[Binary Search Trees]] · [[AVL Trees]] · [[Graphs]] · [[Dynamic Programming]] · [[Data Structure Selection]]

---

## 📐 Module 1 — [[Complexity Analysis]]

### 1.1 Asymptotic Notation

> [!question] Q: Big-Oh membership — prove or disprove
>
> For each line decide whether the relation holds. Give a **witness pair** $(c, n_0)$ if it holds, or derive a contradiction if it does not.
>
> a) $n^2 \in O(n^2)$
> b) $n^2 \in O(n)$
> c) $n^3 \in O(n^2)$
> d) $\log_2 n \in O(n)$
> e) Give the tightest class for $g(n) = (\log_4 n)^5$.

> [!success]- Solution
>
> **a) True.** Take $c=1,\ n_0=1$: $n^2 \le 1\cdot n^2$ for all $n\ge 1$. ✔
>
> **b) False.** Suppose $n^2 \le c\,n$ for all $n \ge n_0$. Dividing by $n$ gives $n \le c$, impossible as $n\to\infty$. ✘
>
> **c) False.** $n^3 \le c\,n^2 \Rightarrow n \le c$ — same contradiction. ✘
>
> **d) True.** $\log_2 n \le n$ for all $n\ge 1$, so $c=1,\ n_0=1$ works. ✔
>
> **e)** Change of base: $(\log_4 n)^5 = \left(\tfrac{\log_2 n}{2}\right)^5 = \tfrac{1}{32}(\log_2 n)^5$. The constant $\tfrac{1}{32}$ is irrelevant asymptotically, so the tightest class is $\Theta\!\big((\log n)^5\big)$ — **polylogarithmic**: faster-growing than any constant power of $\log$ below 5, but slower than $n^\varepsilon$ for every $\varepsilon>0$.

---

> [!question] Q: Three functions, one sum
>
> Three routines each compute $\sum_{i=1}^{n} i$.
> - **F1** — recursion: `F1(n) = n + F1(n-1)`, base `F1(0)=0`.
> - **F2** — one `for` loop `i = 1..n` accumulating the sum.
> - **F3** — nested loops: outer `i = 1..n`, inner `j = 1..i`, incrementing a counter.
>
> Give the time complexity of each. Which one would you ship, and why?

> [!success]- Solution
>
> **F1.** $T(n) = T(n-1) + \Theta(1)$, $T(0)=\Theta(1)$. Unrolling the chain of $n$ calls gives $T(n)=\Theta(n)$. (Also uses $\Theta(n)$ stack frames.)
>
> **F2.** Exactly $n$ iterations of constant work $\Rightarrow \Theta(n)$, with $\Theta(1)$ space.
>
> **F3.** Inner loop runs $i$ times, so total work $= \sum_{i=1}^{n} i = \dfrac{n(n+1)}{2} = \Theta(n^2)$.
>
> **Ship F2** — same $\Theta(n)$ time as the recursion but $\Theta(1)$ space (no recursion stack, no overflow risk). F3 is asymptotically worse for no benefit.
>
> > [!bug] Quiz 1 grading note
> > A marked script wrote F1 as "$O(n^w)$". The correct, unambiguous answer is $O(n)$ — there is no hidden exponent.

---

### 1.2 Loop Counting & Recurrences

> [!question] Q: Triple-nested counter (exact count + Θ)
>
> ```text
> count = 0
> for i = 1 to n:
>     for j = 1 to i:
>         for k = 1 to j:
>             count = count + 1
> ```
> Give a **closed form** for the final value of `count`, then its asymptotic class.

> [!success]- Solution
>
> $$\text{count} = \sum_{i=1}^{n}\sum_{j=1}^{i}\sum_{k=1}^{j} 1 = \sum_{i=1}^{n}\sum_{j=1}^{i} j = \sum_{i=1}^{n}\frac{i(i+1)}{2}.$$
>
> Using $\sum i^2 = \tfrac{n(n+1)(2n+1)}{6}$ and $\sum i = \tfrac{n(n+1)}{2}$:
>
> $$\text{count} = \binom{n+2}{3} = \frac{n(n+1)(n+2)}{6} = \Theta(n^3).$$
>
> Sanity check at $n=3$: formula gives $\tfrac{3\cdot4\cdot5}{6}=10$. Hand count: $1+(1+2)+(1+2+3)=1+3+6=10$. ✔

---

> [!question] Q: Recurrence classification
>
> Give a tight $\Theta$ bound for each (assume $T(1)=\Theta(1)$):
>
> a) $T(n) = 2T(n/2) + \Theta(n)$  *(merge sort)*
> b) $T(n) = T(n-1) + \Theta(n)$  *(quick sort worst case)*
> c) $T(n) = 2T(n/2) + \Theta(1)$  *(tree traversal / heapify-style)*
> d) $T(n) = T(n/2) + \Theta(1)$  *(binary search)*

> [!success]- Solution
>
> | Recurrence | Method | Result |
> |---|---|---|
> | a) $2T(n/2)+\Theta(n)$ | Master Thm, case 2 ($n^{\log_2 2}=n$) | $\Theta(n\log n)$ |
> | b) $T(n-1)+\Theta(n)$ | Unroll: $\sum_{k=1}^{n} k$ | $\Theta(n^2)$ |
> | c) $2T(n/2)+\Theta(1)$ | Master Thm, case 1 ($n^{\log_2 2}=n \gg 1$) | $\Theta(n)$ |
> | d) $T(n/2)+\Theta(1)$ | Master Thm, case 2 ($n^{\log_2 1}=1$) | $\Theta(\log n)$ |

---

### 1.3 Growth-Rate Ordering

> [!question] Q: Sort by asymptotic growth
>
> Order from **slowest** to **fastest** growing. Group any that are $\Theta$-equivalent.
>
> $$2^n,\quad n!,\quad n\log_2 n,\quad \tfrac{n^2}{2},\quad \sqrt{n},\quad \log_2 n,\quad n^{1/3},\quad 100\,n,\quad \log_2(n^2)$$

> [!success]- Solution
>
> First simplify: $\log_2(n^2) = 2\log_2 n = \Theta(\log n)$, so it ties $\log_2 n$. The constants in $100n$ and $\tfrac{n^2}{2}$ vanish asymptotically.
>
> $$\underbrace{\log_2 n \;\equiv\; \log_2(n^2)}_{\Theta(\log n)} \;\prec\; n^{1/3} \;\prec\; \sqrt{n} \;\prec\; 100\,n \;\prec\; n\log_2 n \;\prec\; \tfrac{n^2}{2} \;\prec\; 2^n \;\prec\; n!$$
>
> Rule of thumb: **(poly)log $\prec$ powers of $n$ ($n^{1/3}\prec n^{1/2}\prec n^1$) $\prec$ $n\log n$ $\prec$ higher polynomials $\prec$ exponential $\prec$ factorial.**

---

## 🔎 Module 2 — [[Searching Algorithms]]

### 2.1 Binary Search on a Descending Array

> [!question] Q: Deepest probes + unsuccessful search *(Quiz 2 style, harder)*
>
> A **descending** array (`mid = ⌊(left+right)/2⌋`):
>
> | idx | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
> |---|---|---|---|---|---|---|---|---|---|---|
> | val | 95 | 85 | 77 | 74 | 63 | 51 | 40 | 32 | 11 | 5 |
>
> a) Which element(s) require the **most** comparisons to find? Give the count.
> b) Searching for **38** (absent), how many iterations run before failure?

> [!success]- Solution
>
> > [!warning] Reversed comparisons
> > The array is sorted **descending**, so the branch test flips: if `key < A[mid]` search **right**, if `key > A[mid]` search **left**.
>
> **a)** Build the *decision tree* of midpoints. Levels (depth = comparisons):
>
> ```mermaid
> graph TD
>     M4["idx4 = 63"] --> M1["idx1 = 85"]
>     M4 --> M7["idx7 = 32"]
>     M1 --> M0["idx0 = 95"]
>     M1 --> M2["idx2 = 77"]
>     M7 --> M5["idx5 = 51"]
>     M7 --> M8["idx8 = 11"]
>     M2 --> M3["idx3 = 74"]
>     M5 --> M6["idx6 = 40"]
>     M8 --> M9["idx9 = 5"]
> ```
>
> The deepest leaves (level 4) are **74, 40, 5** (indices 3, 6, 9) → **4 comparisons each**.
>
> **b)** Trace for key = 38:
>
> | step | left | right | mid | A[mid] | decision |
> |---|---|---|---|---|---|
> | 1 | 0 | 9 | 4 | 63 | 38 < 63 → go right |
> | 2 | 5 | 9 | 7 | 32 | 38 > 32 → go left |
> | 3 | 5 | 6 | 5 | 51 | 38 < 51 → go right |
> | 4 | 6 | 6 | 6 | 40 | 38 < 40 → go right |
> | — | 7 | 6 | — | — | left > right → **not found** |
>
> **4 iterations.** ✔ (matches the verified Quiz 2 answer)

---

> [!question] Q: Worst-case unsuccessful probes *(MCQ — Quiz 3 Q10)*
>
> For a sorted array of **32** elements, the maximum number of comparisons binary search needs to conclude a key is **not present** is:
> **A.** 32  **B.** 16  **C.** 6  **D.** 5

> [!success]- Solution
>
> An unsuccessful search shrinks the live range $32\to16\to8\to4\to2\to1\to\varnothing$ — it probes at sizes $32,16,8,4,2,1$ before the range empties: $\lfloor\log_2 32\rfloor + 1 = 5+1 = \mathbf{6}$.
>
> **Answer: C (6).** The "+1" is the final boundary check that confirms absence — that is exactly why D (5) is the classic trap.

---

### 2.2 Merging Sorted Arrays

> [!question] Q: Merge pointers after *k* outputs *(Quiz 2 P2, harder ask)*
>
> Two ascending arrays, both indexed from 0:
> - `A = [1, 2, 3, 5, 8, 13, 21]`
> - `B = [4, 9, 15, 16, 25, 36]`
>
> `Merge` builds ascending `C`. With pointers `i` (into A) and `j` (into B):
> a) State the time complexity of `Merge` for sizes $m,n$.
> b) Give `(i, j)` **immediately after `C` receives its 7th element**, and list `C` so far.

> [!success]- Solution
>
> **a)** Each comparison advances exactly one pointer, and there are $m+n$ elements total ⇒ $O(m+n)$.
>
> **b)** Trace (✓ = element copied to C):
>
> | # | compare | take | i | j |
> |---|---|---|---|---|
> | 1 | A[0]=1 vs B[0]=4 | 1 ✓ | 1 | 0 |
> | 2 | A[1]=2 vs B[0]=4 | 2 ✓ | 2 | 0 |
> | 3 | A[2]=3 vs B[0]=4 | 3 ✓ | 3 | 0 |
> | 4 | A[3]=5 vs B[0]=4 | 4 ✓ | 3 | 1 |
> | 5 | A[3]=5 vs B[1]=9 | 5 ✓ | 4 | 1 |
> | 6 | A[4]=8 vs B[1]=9 | 8 ✓ | 5 | 1 |
> | 7 | A[5]=13 vs B[1]=9 | 9 ✓ | 5 | 2 |
>
> After the 7th element: **`i = 5`, `j = 2`**, and `C = [1, 2, 3, 4, 5, 8, 9]`. ✔
>
> *(Interpretation: `i`,`j` point at the **next** unconsumed element. A has consumed indices 0–4 ⇒ `i=5`; B has consumed 0–1 ⇒ `j=2`.)*

---

### 2.3 Randomized Search

> [!question] Q: Success probability after *t* draws
>
> An array of $n=100$ holds exactly one copy of key $k$. We draw indices uniformly **with replacement**. After **63** draws, what is the probability $k$ has been hit at least once? Does it clear a 0.40 threshold?

> [!success]- Solution
>
> Per-draw hit probability $p=\tfrac{1}{100}$. Probability of *all misses*:
> $$(1-p)^{63} = 0.99^{63} \approx e^{-63/100} = e^{-0.63} \approx 0.533.$$
> So $P(\text{found}) \approx 1 - 0.533 = \mathbf{0.467} \ge 0.40$. ✔

---

## 🔢 Module 3 — [[Sorting Algorithms]]

### 3.1 Insertion & Selection Sort

> [!question] Q: Insertion sort — trace + shift count
>
> Trace insertion sort on `A = [5, 3, 8, 1, 9, 2]`. Show the array after each outer iteration and report the **total element shifts** (moves, not comparisons).

> [!success]- Solution
>
> | after key | array | shifts |
> |---|---|---|
> | 3 | `[3, 5, 8, 1, 9, 2]` | 1 |
> | 8 | `[3, 5, 8, 1, 9, 2]` | 0 |
> | 1 | `[1, 3, 5, 8, 9, 2]` | 3 |
> | 9 | `[1, 3, 5, 8, 9, 2]` | 0 |
> | 2 | `[1, 2, 3, 5, 8, 9]` | 4 |
>
> **Total shifts = 1 + 0 + 3 + 0 + 4 = 8.** Sorted output `[1, 2, 3, 5, 8, 9]`.

---

### 3.2 Heaps & Heap Sort

> [!question] Q: Max-heap construction (bottom-up) *(Quiz 4 P3a)*
>
> Using **`BuildMaxHeap`** (heapify from the last internal node down), build a max-heap from
> `A = [1, 30, 3, 12, 53, 62, 14, 32, 41, 49]` (0-indexed). Give the final array.

> [!success]- Solution
>
> $n=10$; last internal node is index $\lfloor n/2\rfloor-1 = 4$. Sift-down indices 4 → 0:
>
> - **i=4** (53): child idx9=49 → 53>49, no change.
> - **i=3** (12): children 32, 41 → swap with 41. `…41…12 @8`.
> - **i=2** (3): children 62, 14 → swap with 62. `…62…3 @5`.
> - **i=1** (30): children 41, 53 → swap 53; then idx4 child 49 → swap 49. `30` lands @9.
> - **i=0** (1): children 53, 62 → swap 62; then idx2 children 3,14 → swap 14; `1` lands @6.
>
> **Result: `[62, 53, 14, 41, 49, 3, 1, 32, 12, 30]`** ✔
>
> ```mermaid
> graph TD
>     A["62 (0)"] --> B["53 (1)"]
>     A --> C["14 (2)"]
>     B --> D["41 (3)"]
>     B --> E["49 (4)"]
>     C --> F["3 (5)"]
>     C --> G["1 (6)"]
>     D --> H["32 (7)"]
>     D --> I["12 (8)"]
>     E --> J["30 (9)"]
> ```

---

> [!question] Q: Is this array a max-heap? *(Quiz 4 P3b)*
>
> Give an algorithm that decides whether an $n$-element array is a max-heap, and state its complexity. Then test `[90, 40, 80, 10, 30, 70, 60]`.

> [!success]- Solution
>
> **Algorithm.** For every internal node $i = 0 \dots \lfloor n/2\rfloor-1$, verify `A[i] ≥ A[2i+1]` and (if `2i+2 < n`) `A[i] ≥ A[2i+2]`. Return false on the first violation, true otherwise. Each node is checked once ⇒ **$\Theta(n)$** time, $\Theta(1)$ space.
>
> **Test** (internal nodes 0,1,2): node0 90≥40,80 ✔; node1 40≥10,30 ✔; node2 80≥70,60 ✔ → **valid max-heap.**

---

> [!question] Q: Heap sort — extract until the tail is sorted *(Quiz 4 P3c)*
>
> Start from the max-heap `[62, 53, 14, 41, 49, 3, 1, 32, 12, 30]`. Perform heap-sort extractions until the array's **last three** elements are `49, 53, 62` (ascending). Show each swap + sift-down.

> [!success]- Solution
>
> Heap-sort repeats: swap root with last heap slot, shrink heap by 1, sift the new root down.
>
> **Extraction 1** — swap 62↔30 (heap size 10→9), sift 30:
> `[53, 49, 14, 41, 30, 3, 1, 32, 12 | 62]`
>
> **Extraction 2** — swap 53↔12 (size 9→8), sift 12:
> `[49, 41, 14, 32, 30, 3, 1, 12 | 53, 62]`
>
> **Extraction 3** — swap 49↔12 (size 8→7), sift 12:
> `[41, 32, 14, 12, 30, 3, 1 | 49, 53, 62]`
>
> The tail is now **`… 49, 53, 62`** ✔. Final array after the three extractions: **`[41, 32, 14, 12, 30, 3, 1, 49, 53, 62]`**.

---

### 3.3 Quick Sort

> [!question] Q: Median-of-three pivot + first partition *(Quiz 4 P4)*
>
> Array `A = [1, 30, 3, 12, 53, 62, 14, 32, 41, 49]` (0-indexed).
> a) Median-of-three pivot value (uses first, middle `⌊(0+9)/2⌋=4`, last).
> b) Using that pivot, give the array **after the first Lomuto partition**.

> [!success]- Solution
>
> **a)** Candidates: `A[0]=1`, `A[4]=53`, `A[9]=49`. Median of $\{1, 49, 53\}$ = **49**.
>
> **b)** Pivot 49 already sits at index 9. Lomuto scan (boundary `i`, everything $\le$ pivot pushed left):
>
> Elements `1,30,3,12` stay; `53,62` are skipped; `14,32,41` swap left; final pivot swap drops 49 into index 7.
>
> **Result: `[1, 30, 3, 12, 14, 32, 41, 49, 53, 62]`** — pivot 49 at index 7, all of $\{1,30,3,12,14,32,41\} < 49 < \{53,62\}$. ✔

---

### 3.4 Linear-Time & Recursive Sorts

> [!question] Q: Radix sort (LSD) trace
>
> Sort `[329, 457, 657, 839, 436, 720, 355]` with **LSD radix sort** (base 10, stable per digit). Show the array after each digit pass.

> [!success]- Solution
>
> | pass | key digit | array after pass |
> |---|---|---|
> | 1 | ones | `[720, 355, 436, 457, 657, 329, 839]` |
> | 2 | tens | `[720, 329, 436, 839, 355, 457, 657]` |
> | 3 | hundreds | `[329, 355, 436, 457, 657, 720, 839]` ✔ |
>
> Cost $\Theta(d(n+b))$ with $d=3$ digits, base $b=10$ — linear in $n$ for fixed $d$.

---

> [!question] Q: Sorting properties — fill the matrix
>
> Give **worst-case time**, **in-place?**, **stable?** for each algorithm.
>
> | Algorithm | Worst time | In-place | Stable |
> |---|---|---|---|
> | Selection | ? | ? | ? |
> | Insertion | ? | ? | ? |
> | Merge | ? | ? | ? |
> | Quick | ? | ? | ? |
> | Heap | ? | ? | ? |
> | Radix (LSD) | ? | ? | ? |

> [!success]- Solution
>
> | Algorithm | Worst time | In-place | Stable |
> |---|---|---|---|
> | Selection | $O(n^2)$ | ✔ | ✘ (long-range swaps) |
> | Insertion | $O(n^2)$ | ✔ | ✔ |
> | Merge | $O(n\log n)$ | ✘ ($O(n)$ aux) | ✔ |
> | Quick | $O(n^2)$ | ✔ ($O(\log n)$ stack) | ✘ |
> | Heap | $O(n\log n)$ | ✔ | ✘ |
> | Radix (LSD) | $O(d(n+b))$ | ✘ | ✔ (must be) |

---

> [!question] Q: Which sort? — algorithm selection
>
> Pick the best sort and justify in one line.
> a) $10^6$ ints, **nearly sorted** (≤ k misplaced, $k \ll n$).
> b) $10^6$ ints, **stable** required, with $O(n)$ scratch available.
> c) $10^6$ **d-digit** ints in base $b$, want $O(n)$.
> d) Average speed critical, rare $O(n^2)$ acceptable, want **in-place**.

> [!success]- Solution
>
> | | Sort | Why |
> |---|---|---|
> | a | **Insertion** | $O(nk)$ on nearly-sorted input; each item moves $\le k$ slots |
> | b | **Merge** | stable + guaranteed $O(n\log n)$; the $O(n)$ buffer is allowed |
> | c | **Radix (LSD)** | $O(d(n+b))$ = linear for constant $d,b$ |
> | d | **Quick** (randomized / median-of-three) | $O(n\log n)$ average, tiny constant, in-place |

---

## ⛰️ Module 4 — [[Priority Queues]] & [[Heaps]]

### 4.1 Heap Operations

> [!question] Q: Sequential insert into a binary heap
>
> Starting from an empty **max-heap**, insert `[15, 10, 25, 8, 30, 5]` one at a time (sift-up after each). Draw the final heap and give its array.

> [!success]- Solution
>
> - insert 15 → `[15]`
> - insert 10 → `[15, 10]`
> - insert 25 → sift-up past 15 → `[25, 10, 15]`
> - insert 8 → `[25, 10, 15, 8]`
> - insert 30 → sift-up 30 past 10, past 25 → `[30, 25, 15, 8, 10]`
> - insert 5 → `[30, 25, 15, 8, 10, 5]`
>
> ```mermaid
> graph TD
>     A["30 (0)"] --> B["25 (1)"]
>     A --> C["15 (2)"]
>     B --> D["8 (3)"]
>     B --> E["10 (4)"]
>     C --> F["5 (5)"]
> ```
>
> Final array: **`[30, 25, 15, 8, 10, 5]`**.

---

> [!question] Q: Build-heap vs. repeated insert — the complexity trap
>
> a) Cost of building a heap from $n$ items by **`BuildMaxHeap`** (bottom-up)?
> b) Cost of building it by **$n$ successive inserts**?
> c) Which is tighter, and what is the intuition?

> [!success]- Solution
>
> **a)** $\Theta(n)$. Although a single sift-down is $O(\log n)$, most nodes are near the bottom: $\sum_{h\ge0}\frac{n}{2^{h+1}}\,h = O(n)$.
>
> **b)** $\Theta(n\log n)$ worst case — each insert sifts up to the root through $O(\log n)$ levels, and (unlike build-heap) the expensive nodes are the *last* (deepest) ones inserted.
>
> **c)** **Build-heap ($\Theta(n)$) is tighter.** Intuition: bottom-up spends little work on the many leaves; insertion spends the most work exactly on the many late, deep elements.

---

### 4.2 Priority Queue as an ADT

> [!question] Q: Backing-store trade-offs
>
> Complete the average-case table for a **priority queue** under three implementations.
>
> | Backing store | `insert` | `find-max` | `extract-max` |
> |---|---|---|---|
> | Unsorted array | ? | ? | ? |
> | Sorted array (desc) | ? | ? | ? |
> | Binary max-heap | ? | ? | ? |

> [!success]- Solution
>
> | Backing store | `insert` | `find-max` | `extract-max` |
> |---|---|---|---|
> | Unsorted array | $O(1)$ | $O(n)$ | $O(n)$ |
> | Sorted array (desc) | $O(n)$ | $O(1)$ | $O(1)$ |
> | Binary max-heap | $O(\log n)$ | $O(1)$ | $O(\log n)$ |
>
> The heap is the balanced choice — no single operation is linear, which is why it is the default PQ.

---

## 🥞 Module 5 — [[Linked Lists]]

### 5.1 Conceptual Trade-offs

> [!question] Q: True / False with one-line justification
>
> a) Insertion at a **known** node in a linked list is $O(1)$.
> b) Searching an **unsorted singly linked list (SLL)** is $O(\log n)$.
> c) A circular **doubly** linked list supports forward *and* backward traversal.
> d) Deleting the **tail** of an SLL given only `pHead` is $O(1)$.
> e) Why is binary search "impossible" on a standard SLL? *(Quiz 3 Q5)*

> [!success]- Solution
>
> | | Verdict | Reason |
> |---|---|---|
> | a | **True** | Re-link is 2 pointer writes once the node is in hand |
> | b | **False** | No random access ⇒ linear scan ⇒ $O(n)$ |
> | c | **True** | `pNext` forward, `pPrev` backward; circular ⇒ no null ends |
> | d | **False** | Must walk to the *node before* the tail to null its `next` ⇒ $O(n)$ |
> | e | — | Binary search needs **$O(1)$ access to the middle index**; a list only offers sequential access (Quiz 3 Q5 answer **D**) |

---

> [!question] Q: SLL insert-after — pointer surgery + diagram
>
> Given `10 → 20 → 30 → 40 → NULL`, insert value **25** after the node holding 20. Write the exact pointer operations (order matters) and draw the result.

> [!success]- Solution
>
> ```text
> newNode        = Node(25)
> newNode->next  = node20->next   // 25 → 30   (do this FIRST)
> node20->next   = newNode        // 20 → 25
> ```
> Reversing the two lines would leak `30 → 40` — always wire the new node's `next` **before** redirecting the predecessor.
>
> ```mermaid
> graph LR
>     H[pHead] --> N10[10] --> N20[20] --> N25[25] --> N30[30] --> N40[40] --> NUL[NULL]
> ```

---

> [!question] Q: `findMidNode` — fast/slow pointers, no extra memory *(Quiz 3 Q11)*
>
> ```cpp
> struct Node { int value; Node* next; };
> ```
> Return the middle node; on **even** length return the **second** middle. No extra arrays/lists.
> `{1}→{2}→{3}→{4}→{5}` ⇒ `3`;  `{1}→…→{6}` ⇒ `4`.

> [!success]- Solution
>
> ```cpp
> Node* findMidNode(Node* headRef) {
>     if (headRef == nullptr) return nullptr;
>     Node* slow = headRef;
>     Node* fast = headRef;
>     while (fast != nullptr && fast->next != nullptr) {
>         slow = slow->next;          // +1
>         fast = fast->next->next;    // +2
>     }
>     return slow;                    // second middle when even
> }
> ```
>
> **Why it lands on the 2nd middle (even case, n=6):** after iterations `slow` visits 2→3→4 while `fast` visits 3→5→null; loop exits with `slow = node 4`. For $n=5$, `slow` ends at node 3. Time $O(n)$, space $O(1)$. ✔

---

> [!question] Q: Reverse an SLL in place
>
> Reverse `1 → 2 → 3 → 4 → NULL` iteratively. Give the loop and the result.

> [!success]- Solution
>
> ```cpp
> Node* reverse(Node* head) {
>     Node* prev = nullptr;
>     while (head) {
>         Node* nxt = head->next;  // save
>         head->next = prev;       // flip
>         prev = head;             // advance prev
>         head = nxt;              // advance head
>     }
>     return prev;                 // new head
> }
> ```
>
> ```mermaid
> graph LR
>     H[pHead] --> N4[4] --> N3[3] --> N2[2] --> N1[1] --> NUL[NULL]
> ```
> $O(n)$ time, $O(1)$ space — exactly three pointer writes per node.

---

## 🥪 Module 6 — [[Stacks and Queues]]

### 6.1 Concept MCQs *(Quiz 3, verified)*

> [!question] Q: Six rapid-fire concept checks
>
> 1. Why keep **both head and tail** pointers in a queue built on a linked list?
> 2. Even with a tail pointer, why is deleting the last SLL node inefficient?
> 3. Disadvantage of a **static-array** stack vs. a linked-list stack?
> 4. In a queue, where do enqueue / dequeue happen?
> 5. Which structure is **LIFO**?
> 6. Popping an **empty** stack causes what?

> [!success]- Solution
>
> | # | Answer | Reason |
> |---|---|---|
> | 1 | **Avoid traversing the whole list to enqueue** | tail pointer gives $O(1)$ insert at the rear |
> | 2 | **Must find the node *before* the tail** | SLL has no back-pointer ⇒ $O(n)$ walk |
> | 3 | **Stack overflow once the fixed size is exceeded** | static arrays can't grow |
> | 4 | **Enqueue at rear, dequeue at front** (FIFO) | |
> | 5 | **Stack** | Last-In-First-Out |
> | 6 | **Stack underflow** | no element to remove |

---

### 6.2 Expression Evaluation

> [!question] Q: Postfix → infix + evaluate *(Quiz 3 Q9)*
>
> Convert to fully-parenthesized infix and compute the value:
> `18 3 / 7 5 2 + * + 4 6 * - 9 +`

> [!success]- Solution
>
> Stack-evaluate left to right:
>
> | token | stack after |
> |---|---|
> | 18 3 / | `[6]` |
> | 7 5 2 + | `[6, 7, 7]` |
> | * | `[6, 49]` |
> | + | `[55]` |
> | 4 6 * | `[55, 24]` |
> | - | `[31]` |
> | 9 + | `[40]` |
>
> **Infix:** $\big((18 / 3) + 7 \times (5 + 2)\big) - (4 \times 6) + 9$
> **Value:** $(6 + 49) - 24 + 9 = \mathbf{40}$. ✔

---

> [!question] Q: Balanced-brackets via a stack
>
> Is `([]{()[]})` balanced? Describe the stack algorithm and trace it.

> [!success]- Solution
>
> Push every opener; on a closer, pop and check the match. Balanced ⇔ every closer matches the top **and** the stack ends empty.
>
> | char | action | stack |
> |---|---|---|
> | `(` | push | `(` |
> | `[` | push | `( [` |
> | `]` | pop `[` ✔ | `(` |
> | `{` | push | `( {` |
> | `(` | push | `( { (` |
> | `)` | pop `(` ✔ | `( {` |
> | `[` | push | `( { [` |
> | `]` | pop `[` ✔ | `( {` |
> | `}` | pop `{` ✔ | `(` |
> | `)` | pop `(` ✔ | *(empty)* |
>
> Stack empty at the end ⇒ **balanced.** ✔

---

> [!question] Q: Queue from two stacks
>
> Implement a FIFO queue using two LIFO stacks `in` and `out`. Give amortized costs.

> [!success]- Solution
>
> - **enqueue(x):** `in.push(x)` — $O(1)$.
> - **dequeue():** if `out` empty, pour everything from `in` into `out` (reversing order), then `out.pop()`.
>
> Each element is moved across at most once ⇒ **amortized $O(1)$** per operation (worst-case single dequeue $O(n)$).

---

## #️⃣ Module 7 — [[Hashing]]

### 7.1 Open Addressing — Build All Three Tables

> [!question] Q: Linear, quadratic & double hashing *(Hashing quiz P1a)*
>
> Empty table, $m = 13$, $h(k) = k \bmod 13$. Insert in order:
> **40, 31, 53, 44, 66, 77, 17, 90, 30, 102.**
>
> Collision schemes (home slot $h(k)$ tried first; on the $i$-th collision use):
> - **Linear:** $h(k,i) = h(k) + i$
> - **Quadratic:** $h(k,i) = h(k) + 2i^2 + 1$  *(offsets $+3, +9, +19, \dots$ for $i=1,2,3$)*
> - **Double:** $h_2(k) = 7 - (k \bmod 7)$, $h(k,i) = h(k) + i\cdot h_2(k)$
>
> Fill all three tables.

> [!success]- Solution
>
> **Home slots** $k \bmod 13$: `40→1, 31→5, 53→1*, 44→5*, 66→1*, 77→12, 17→4, 90→12*, 30→4*, 102→11` (`*` = collision).
>
> | slot | Linear | Quadratic | Double |
> |---|---|---|---|
> | 0 | 90 | 30 | 90 |
> | 1 | 40 | 40 | 40 |
> | 2 | 53 | 90 | — |
> | 3 | 66 | — | — |
> | 4 | 17 | 53 | 53 |
> | 5 | 31 | 31 | 31 |
> | 6 | 44 | — | 30 |
> | 7 | 30 | 17 | — |
> | 8 | — | 44 | 17 |
> | 9 | — | — | 66 |
> | 10 | — | 66 | 44 |
> | 11 | 102 | 102 | 102 |
> | 12 | 77 | 77 | 77 |
>
> **Worked collisions (double hashing):** $h_2$ values — $40\!:\!2,\ 53\!:\!3,\ 44\!:\!5,\ 66\!:\!4,\ 17\!:\!4,\ 90\!:\!1,\ 30\!:\!5$.
> e.g. **30**: home 4 (53) → $4+1\cdot5=9$ (66) → $4+2\cdot5=14\!\bmod13=1$ (40) → $4+3\cdot5=19\!\bmod13=\mathbf{6}$ ✔.
> e.g. **30 (quadratic)**: home 4 (53) → $4+3=7$ (17) → $4+9=13\!\bmod13=\mathbf{0}$ ✔. *(All three columns independently verified.)*

---

> [!question] Q: Probe counting — find / insert *(Hashing quiz P1b–f)*
>
> Using the three tables above, count probes for each query. (Unsuccessful search stops at the first **empty** slot.)
>
> b) find **31**  c) find **17**  d) find **28** (absent)  f) insert **56**

> [!success]- Solution
>
> | query | Linear | Quadratic | Double |
> |---|---|---|---|
> | find 31 | 1 | 1 | 1 |
> | find 17 | 1 | 2 | 2 |
> | find 28 *(home 2, absent)* | 7 | 5 | 1 |
> | insert 56 *(home 4)* | 3 | 6 | 4 |
>
> **`find 28` (home slot 2), linear:** slots `2,3,4,5,6,7` occupied, slot `8` empty → **7 probes**. **Double:** slot `2` is already empty → **1 probe**. This is the clustering penalty of linear probing made concrete.
>
> > [!note] Rule
> > Unsuccessful search ⇒ probe until an **empty** slot. Successful search ⇒ probe until the key is matched. With tombstones, deletions count as occupied for *searching* but reusable for *inserting*.

---

### 7.2 Hash-Function Design & Chaining

> [!question] Q: Why $m = 2^p$ is a poor table size
>
> Explain why the division method $h(k)=k \bmod m$ with $m=2^p$ is a bad choice. What is the standard remedy?

> [!success]- Solution
>
> $k \bmod 2^p$ keeps only the **low $p$ bits** of $k$. Keys that agree on those bits collide regardless of their high bits, and any low-bit pattern in the data is amplified into clustering. The function throws away most of the key's information.
>
> **Remedy:** pick $m$ **prime**, away from powers of 2 (and 10). Good choices: 13, 17, 31, 53, 97, 193, …

---

> [!question] Q: Separate chaining — load factor & search cost
>
> A chained table has $m = 13$ buckets and $n = 26$ keys, uniformly hashed.
> a) Load factor $\alpha$?
> b) Expected probes for an **unsuccessful** search? For a **successful** one?

> [!success]- Solution
>
> **a)** $\alpha = n/m = 26/13 = \mathbf{2}$.
>
> **b)** Under simple uniform hashing:
> - Unsuccessful $\approx \alpha = \mathbf{2}$ (scan a full chain of expected length $\alpha$).
> - Successful $\approx 1 + \tfrac{\alpha}{2} = 1 + 1 = \mathbf{2}$.
>
> Both are $O(1+\alpha)$ — chaining degrades gracefully and never "fills up."

---

## 🌳 Module 8 — [[Trees]] · [[Binary Search Trees]] · [[AVL Trees]]

### 8.1 Traversals

> [!question] Q: BST preorder *(Quiz 5 P1 — corrected)*
>
> ```text
>         6
>        / \
>       3   9
>      / \    \
>     1   4    12
>      \   \     \
>       2   5     10
> ```
> Write the **preorder** (Root → Left → Right) sequence. *(Node 2 is the right child of 1; node 5 is the right child of 4.)*

> [!success]- Solution
>
> Visit order: 6 → (left subtree of 3) → (right subtree of 9).
>
> **`6, 3, 1, 2, 4, 5, 9, 12, 10`** ✔
>
> ```mermaid
> graph TD
>     N6[6] --> N3[3]
>     N6 --> N9[9]
>     N3 --> N1[1]
>     N3 --> N4[4]
>     N1 --> N2[2]
>     N4 --> N5[5]
>     N9 --> N12[12]
>     N12 --> N10[10]
> ```
>
> > [!bug] Correction
> > A marked script wrote `6, 3, 1, 4, 2, 5, …`. That is **wrong**: after visiting 1, preorder descends into 1's child **2** *before* climbing back to 4. Correct order keeps `…1, 2, 4…`.

---

> [!question] Q: Reconstruct unknown nodes from post-order *(Quiz 5 P4)*
>
> The tree's **post-order** (Left → Right → Root) is
> `15, 25, 20, 40, 35, 70, 60, 90, 85, 75, 50`.
> ```text
>             50
>           /    \
>          x1     x3
>         /  \   /  \
>        20  40 60   x4
>       /  \     \     \
>      x2  25    70     90
> ```
> Find $x_1, x_2, x_3, x_4$.

> [!success]- Solution
>
> Post-order of the skeleton is `x2, 25, 20, 40, x1, 70, 60, 90, x4, x3, 50`. Align term-by-term with the given sequence:
>
> $$x_2 = 15,\quad x_1 = 35,\quad x_4 = 85,\quad x_3 = 75.$$
>
> ```mermaid
> graph TD
>     N50[50] --> N35["x1 = 35"]
>     N50 --> N75["x3 = 75"]
>     N35 --> N20[20]
>     N35 --> N40[40]
>     N75 --> N60[60]
>     N75 --> N85["x4 = 85"]
>     N20 --> N15["x2 = 15"]
>     N20 --> N25[25]
>     N60 --> N70[70]
>     N85 --> N90[90]
> ```

---

### 8.2 AVL — Rotations

> [!question] Q: The four imbalance cases (mini-drills)
>
> For each insertion into the (sub)tree shown, name the case (LL / LR / RR / RL) and give the rebalanced root.
> a) insert `1` into `3 ← 2` (2 is left child of 3, 1 makes it left-left)
> b) insert `20` into `30 ← 10` (10 left child of 30; 20 is right child of 10)
> c) insert `50` into `30 → 40` (40 right child of 30; 50 right child of 40)
> d) insert `25` into `20 → 40 ← 30` (40 right child of 20; 30 left child of 40)

> [!success]- Solution
>
> | | shape | case | rotation | new local root |
> |---|---|---|---|---|
> | a | left-left | **LL** | single **right** at 3 | **2** → `1, 3` |
> | b | left-right | **LR** | left @10 then right @30 | **20** → `10, 30` |
> | c | right-right | **RR** | single **left** at 30 | **40** → `30, 50` |
> | d | right-left | **RL** | right @40 then left @20 | **30** → `20, 40` |

---

> [!question] Q: AVL deletion with rebalancing *(Quiz 5 P3)*
>
> Delete **33** from this AVL tree; show the steps.
> ```text
>           33
>          /   \
>         13    53
>        /  \     \
>       9   21     61
>      / \
>     8  11
> ```

> [!success]- Solution
>
> **Step 1 — delete.** 33 has two children; replace it by its **in-order successor** = leftmost of the right subtree = **53** (53 has no left child). 53's old slot is filled by its right child 61.
>
> **Step 2 — check balances bottom-up.** New root 53 now has left height 3 (13→9→8) and right height 1 (61): balance $= +2$ → violation. Left child 13 is left-heavy (balance $+1$) ⇒ **Left-Left**.
>
> **Step 3 — single right rotation at 53:**
>
> ```mermaid
> graph TD
>     N13[13] --> N9[9]
>     N13 --> N53[53]
>     N9 --> N8[8]
>     N9 --> N11[11]
>     N53 --> N21[21]
>     N53 --> N61[61]
> ```
>
> Result is a balanced AVL tree rooted at **13** (all balance factors in $\{-1,0,+1\}$). ✔

---

### 8.3 AVL — Construction & Conversion

> [!question] Q: Build an AVL tree from a sequence
>
> Insert `10, 20, 30, 40, 50, 25` into an initially empty AVL tree. Note every rotation and draw the final tree.

> [!success]- Solution
>
> - `10, 20` → fine.
> - insert `30`: 10→20→30 right chain ⇒ **RR at 10** → root 20 `(10, 30)`.
> - insert `40`: balanced.
> - insert `50`: 30→40→50 ⇒ **RR at 30** → subtree root 40 `(30, 50)`. Tree: `20(10, 40(30,50))`.
> - insert `25`: lands as left child of 30. Node 20 becomes right-heavy with a **left-heavy** right child ⇒ **RL** (right @40, then left @20).
>
> ```mermaid
> graph TD
>     N30[30] --> N20[20]
>     N30 --> N40[40]
>     N20 --> N10[10]
>     N20 --> N25[25]
>     N40 --> N50[50]
> ```
>
> Final AVL root = **30**, perfectly balanced.

---

> [!question] Q: Convert an unbalanced BST into an AVL tree *(Quiz 5 P2 — corrected)*
>
> ```text
>             10
>           /    \
>          5      20
>         / \    /  \
>        2   7  15   25
>       /
>      1
>     /
>    0
> ```
> Apply the minimum rotations to make it a valid AVL tree.

> [!success]- Solution
>
> Heights: the left spine `5→2→1→0` makes node **5** the **lowest** violator (balance $+2$), and its left child **2** is itself left-heavy ⇒ **Left-Left**. One **right rotation at 5** fixes everything:
>
> ```mermaid
> graph TD
>     N10[10] --> N2[2]
>     N10 --> N20[20]
>     N2 --> N1[1]
>     N2 --> N5[5]
>     N1 --> N0[0]
>     N20 --> N15[15]
>     N20 --> N25[25]
> ```
>
> Now every balance factor is in $\{-1,0,+1\}$ (root 10 has left height 3, right height 2 ⇒ $+1$). ✔
>
> > [!bug] Correction
> > Only **one** rotation is needed (right @5). The marked attempt rotated at the root and produced a non-AVL result — always rebalance from the **lowest** unbalanced node first.

---

### 8.4 BST Concept

> [!question] Q: Why can a BST degenerate?
>
> a) What insertion order turns a BST into a "linked list", and what is the resulting search cost?
> b) Which traversal of a BST yields sorted output, and why?

> [!success]- Solution
>
> **a)** Inserting **already-sorted** keys (e.g. `1,2,3,4,5`) creates a right-leaning chain of height $n$ ⇒ search/insert/delete degrade to $O(n)$. This is exactly the motivation for self-balancing (AVL) trees.
>
> **b)** **In-order** (Left → Root → Right). The BST invariant (left < node < right) means in-order visits keys in non-decreasing order.

---

## 🕸️ Module 9 — [[Graphs]]

### 9.1 Graph Theory — True / False

> [!question] Q: Three claims about an undirected graph $G(V,E)$ *(Quiz 6 P1)*
>
> a) If $G$ is connected, then $G$ is a tree **iff** $|V| = |E| + 1$.
> b) DFS/BFS run in $O(|V| + |E|)$ using an **adjacency matrix**.
> c) If $G$ is complete and $|E|$ is odd, then $|V|$ is odd.

> [!success]- Solution
>
> **a) True.** A connected graph is a tree $\Leftrightarrow$ it is acyclic $\Leftrightarrow$ it has exactly $|V|-1$ edges, i.e. $|V| = |E|+1$.
>
> **b) False.** The matrix needs a full row scan ($|V|$ entries) per vertex ⇒ $O(|V|^2)$. The $O(|V|+|E|)$ bound is for the **adjacency list**.
>
> **c) False.** $K_n$ has $|E| = \tfrac{n(n-1)}{2}$. Counterexample $K_2$: $|E| = 1$ (odd) but $|V| = 2$ (even). ($K_6$ likewise: 15 edges, 6 vertices.)

---

### 9.2 Degree Sequences

> [!question] Q: Which sequences are graphical? *(Quiz 6 P2 — two corrections)*
>
> Decide whether each decreasing sequence is the degree sequence of a **simple** graph. Justify (parity, max-degree bound, or Havel–Hakimi / Erdős–Gallai).
>
> A. `6, 5, 4, 2, 1, 1, 1, 1`
> B. `7, 6, 5, 4, 4, 3, 2, 1`
> C. `6, 6, 6, 6, 3, 3, 2, 2`
> D. `7, 6, 6, 4, 4, 3, 2, 2`
> E. `8, 7, 7, 6, 4, 2, 1, 1`

> [!success]- Solution
>
> | seq | sum | verdict | reason |
> |---|---|---|---|
> | A | 21 | **No** | odd sum violates the handshake lemma |
> | B | 32 | **Yes** | Havel–Hakimi reduces to all-zeros |
> | C | 34 | **No** ⚠ | Erdős–Gallai fails at $k=4$: $24 > 4\cdot3 + (3+3+2+2)=22$ |
> | D | 34 | **Yes** | Havel–Hakimi reduces to all-zeros |
> | E | 36 | **No** ⚠ | max degree 8 but only $n=8$ vertices ⇒ need degree $\le n-1 = 7$ |
>
> **Havel–Hakimi for D** `7,6,6,4,4,3,2,2`: drop 7, subtract 1 from next 7 → `5,5,3,3,2,1,1` → drop 5 → `4,2,2,1,1,0` (sorted `4,2,2,1,1,0`) → drop 4 → `1,1,0,0,0` → drop 1 → `0,0,0,0` ✔.
>
> > [!bug] Two corrections
> > The marked script answered **Yes** for both **C** and **E**. Both are **No** — C fails Erdős–Gallai at $k=4$, and E is impossible because no vertex in an 8-vertex simple graph can have degree 8.

---

### 9.3 Representations & Traversal

> [!question] Q: Adjacency list + BFS + DFS
>
> Undirected graph:
> ```text
> 1: 2,3   2: 1,4,5   3: 1,6,7   4: 2,8   5: 2,8   6: 3   7: 3,8   8: 4,5,7
> ```
> Visiting neighbours in **increasing** order, give the **BFS** and **DFS** sequences from vertex **1**.

> [!success]- Solution
>
> ```mermaid
> graph TD
>     1 --- 2
>     1 --- 3
>     2 --- 4
>     2 --- 5
>     3 --- 6
>     3 --- 7
>     4 --- 8
>     5 --- 8
>     7 --- 8
> ```
>
> **BFS(1):** `1, 2, 3, 4, 5, 6, 7, 8` (level by level).
>
> **DFS(1):** `1, 2, 4, 8, 5, 7, 3, 6` — dive 1→2→4→8, then 8's next unvisited (5), back up to 8→7→3→6.

---

### 9.4 Minimum Spanning Trees

> [!question] Q: Prim's MST step-by-step *(Quiz 6 P3, start = F, x = 8)*
>
> Weighted graph below (edge $F\!-\!I$ has weight $x=8$). Run **Prim** from **F** and give the MST edge set and total weight.
>
> ```mermaid
> graph LR
>     A((A)) ---|8| B((B))
>     A ---|6| H((H))
>     B ---|7| C((C))
>     B ---|18| D((D))
>     B ---|20| F((F))
>     B ---|10| I((I))
>     C ---|10| D
>     D ---|8| E((E))
>     E ---|7| F
>     F ---|5| G((G))
>     F ---|8| I
>     G ---|5| H
>     H ---|5| I
> ```

> [!success]- Solution
>
> Greedily add the cheapest edge leaving the visited set:
>
> | step | edge added | weight | visited |
> |---|---|---|---|
> | 1 | F–G | 5 | F,G |
> | 2 | G–H | 5 | F,G,H |
> | 3 | H–I | 5 | F,G,H,I |
> | 4 | H–A | 6 | +A |
> | 5 | F–E | 7 | +E |
> | 6 | A–B | 8 | +B |
> | 7 | B–C | 7 | +C |
> | 8 | E–D | 8 | +D |
>
> **MST weight $= 5+5+5+6+7+8+7+8 = \mathbf{51}$.** ✔ (Edge $F\!-\!I=8$ is *not* used — $H\!-\!I=5$ is cheaper.)

---

> [!question] Q: Kruskal's MST (fresh graph)
>
> ```mermaid
> graph LR
>     A((A)) ---|7| B((B))
>     A ---|5| D((D))
>     B ---|8| C((C))
>     B ---|9| D
>     B ---|7| E((E))
>     C ---|5| E
>     D ---|15| E
>     D ---|6| F((F))
>     E ---|8| F
> ```
> Run **Kruskal**: sort edges, add if no cycle. Give the MST and total weight.

> [!success]- Solution
>
> Sorted: `AD5, CE5, DF6, AB7, BE7, BC8, EF8, BD9, DE15`.
>
> | edge | weight | cycle? | action |
> |---|---|---|---|
> | A–D | 5 | no | **add** |
> | C–E | 5 | no | **add** |
> | D–F | 6 | no | **add** |
> | A–B | 7 | no | **add** |
> | B–E | 7 | no | **add** (joins {A,B,D,F} + {C,E}) |
> | B–C | 8 | yes | skip |
> | … | | | stop — 5 edges, 6 vertices |
>
> **MST $= \{AD, CE, DF, AB, BE\}$, weight $5+5+6+7+7 = \mathbf{30}$.**

---

### 9.5 Shortest Paths

> [!question] Q: Dijkstra table from a single source
>
> Undirected weighted graph:
> ```text
> A-B:4   A-C:1   C-B:2   B-D:5   C-D:8   C-E:10   D-E:2
> ```
> Run **Dijkstra from A**. Give the final distance to every vertex and the shortest path to **E**.

> [!success]- Solution
>
> | settle | A | B | C | D | E |
> |---|---|---|---|---|---|
> | init | 0 | ∞ | ∞ | ∞ | ∞ |
> | A(0) | 0 | 4 | **1** | ∞ | ∞ |
> | C(1) | 0 | **3** | 1 | 9 | 11 |
> | B(3) | 0 | 3 | 1 | **8** | 11 |
> | D(8) | 0 | 3 | 1 | 8 | **10** |
> | E(10) | — | — | — | — | 10 |
>
> Final: $A\!=\!0,\ C\!=\!1,\ B\!=\!3,\ D\!=\!8,\ E\!=\!10$.
> Shortest path to E: **A → C → B → D → E** (1 + 2 + 5 + 2 = 10).

---

### 9.6 Euler & Hamilton

> [!question] Q: Circuit conditions
>
> For each, state whether an **Euler circuit**, **Euler trail**, **Hamiltonian circuit**, or **none guaranteed** exists.
> a) Connected, every vertex even degree.
> b) Connected, exactly two odd-degree vertices.
> c) $K_5$.
> d) Path graph $P_n$ ($n \ge 3$).

> [!success]- Solution
>
> | | Euler | Hamilton | note |
> |---|---|---|---|
> | a | **Euler circuit** ✔ | not guaranteed | all-even + connected is exactly the Euler-circuit condition |
> | b | **Euler trail** (not circuit) | not guaranteed | trail starts/ends at the two odd vertices |
> | c | **Euler circuit** ✔ (every degree = 4, even) | **Hamiltonian circuit** ✔ | $K_n$ ($n\ge3$) is always Hamiltonian |
> | d | **Euler trail** (two odd endpoints) | **No** Hamiltonian *circuit* (it's an open path) | a Hamiltonian *path* does exist |

---

## 🧩 Module 10 — [[Dynamic Programming]]

### 10.1 Matrix-Chain Multiplication

> [!question] Q: Optimal parenthesization
>
> Four matrices with dimension vector $p = [3, 5, 2, 4, 3]$, i.e. $A_1{:}\,3\times5,\ A_2{:}\,5\times2,\ A_3{:}\,2\times4,\ A_4{:}\,4\times3$.
> Fill the cost table $m[i,j]$, find $m[1,4]$, and give the optimal parenthesization.

> [!success]- Solution
>
> Recurrence $m[i,j] = \min_{i\le k<j}\big(m[i,k] + m[k{+}1,j] + p_{i-1}p_k p_j\big)$, $m[i,i]=0$.
>
> **Length 2:** $m[1,2]=3{\cdot}5{\cdot}2=30$; $m[2,3]=5{\cdot}2{\cdot}4=40$; $m[3,4]=2{\cdot}4{\cdot}3=24$.
>
> **Length 3:**
> - $m[1,3]=\min(0{+}40{+}3{\cdot}5{\cdot}4=100,\ 30{+}0{+}3{\cdot}2{\cdot}4=54)=\mathbf{54}$ at $k=2$.
> - $m[2,4]=\min(0{+}24{+}5{\cdot}2{\cdot}3=54,\ 40{+}0{+}5{\cdot}4{\cdot}3=100)=\mathbf{54}$ at $k=2$.
>
> **Length 4:**
> $$m[1,4]=\min\begin{cases}k{=}1: 0+54+3{\cdot}5{\cdot}3 = 99\\ k{=}2: 30+24+3{\cdot}2{\cdot}3 = \mathbf{72}\\ k{=}3: 54+0+3{\cdot}4{\cdot}3 = 90\end{cases} = \mathbf{72}\ (k{=}2).$$
>
> | $m[i,j]$ | j=1 | j=2 | j=3 | j=4 |
> |---|---|---|---|---|
> | i=1 | 0 | 30 | 54 | **72** |
> | i=2 | | 0 | 40 | 54 |
> | i=3 | | | 0 | 24 |
> | i=4 | | | | 0 |
>
> Split at $k=2$ ⇒ **$((A_1 A_2)(A_3 A_4))$**, cost $30 + 24 + (3{\cdot}2{\cdot}3{=}18) = \mathbf{72}$ scalar multiplications.

---

### 10.2 0/1 Knapsack

> [!question] Q: Fill the knapsack table + recover items
>
> Capacity $W = 7$; items (weight, value): $1{:}(1,1),\ 2{:}(3,4),\ 3{:}(4,5),\ 4{:}(5,7)$.
> Build $V[k][w]$, give the optimal value, and list the chosen items.

> [!success]- Solution
>
> $V[k][w] = \max\big(V[k{-}1][w],\ v_k + V[k{-}1][w-w_k]\big)$ when $w_k \le w$, else $V[k{-}1][w]$.
>
> | k \\ w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> |---|---|---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | 1 (1,1) | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
> | 2 (3,4) | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
> | 3 (4,5) | 0 | 1 | 1 | 4 | 5 | 6 | 6 | **9** |
> | 4 (5,7) | 0 | 1 | 1 | 4 | 5 | 7 | 8 | **9** |
>
> **Optimal value $V[4][7] = 9$.** Trace back: $V[4][7]=V[3][7]$ → item 4 out; $V[3][7]\ne V[2][7]$ → **item 3 in** (go to $V[2][3]$); $V[2][3]\ne V[1][3]$ → **item 2 in** (go to $V[1][0]$); done.
> **Chosen: items {2, 3}**, weight $3+4=7$, value $4+5=9$. ✔

---

### 10.3 Longest Common Subsequence

> [!question] Q: LCS length + one witness
>
> $X = $ `XMJYAUZ`, $Y = $ `MZJAWXU`. Fill $L[i][j]$, give the LCS length and one valid LCS.

> [!success]- Solution
>
> $L[i][j] = L[i{-}1][j{-}1]+1$ if $X_i = Y_j$, else $\max(L[i{-}1][j], L[i][j{-}1])$.
>
> | | ∅ | M | Z | J | A | W | X | U |
> |---|---|---|---|---|---|---|---|---|
> | ∅ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | X | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
> | M | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
> | J | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 |
> | Y | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 |
> | A | 0 | 1 | 1 | 2 | 3 | 3 | 3 | 3 |
> | U | 0 | 1 | 1 | 2 | 3 | 3 | 3 | **4** |
> | Z | 0 | 1 | 2 | 2 | 3 | 3 | 3 | **4** |
>
> **LCS length = 4.** Back-tracking the diagonal matches gives **`MJAU`**.

---

### 10.4 When (not) to Use DP

> [!question] Q: Optimal substructure & overlapping subproblems
>
> For each, state whether it has (a) optimal substructure and (b) overlapping subproblems, and whether DP is the right tool.
> 1. Shortest path in a **DAG**.
> 2. Counting ways to make change for $n$ cents.
> 3. **Merge sort.**

> [!success]- Solution
>
> | problem | optimal substructure | overlapping subproblems | DP? |
> |---|---|---|---|
> | DAG shortest path | ✔ | ✔ (sub-paths reused) | **Yes** |
> | coin change count | ✔ | ✔ (amounts recomputed) | **Yes** |
> | merge sort | ✔ | ✘ (halves are disjoint) | **No** — plain divide-and-conquer |
>
> DP pays off **only** when subproblems *recur*; disjoint subproblems (merge sort) gain nothing from a memo table.

---

## ⚡ Module 11 — Synthesis & [[Data Structure Selection]]

### 11.1 Pick the Right Structure

> [!question] Q: Match the requirement to a structure
>
> a) $O(1)$ average search/insert/delete; $O(n)$ find-min acceptable.
> b) $O(\log n)$ for **all** of search, insert, delete, find-min.
> c) $O(1)$ push/pop, LIFO.
> d) $O(1)$ enqueue/dequeue, processed in arrival order.
> e) Repeatedly extract the **maximum**.

> [!success]- Solution
>
> | | structure | reason |
> |---|---|---|
> | a | **Hash table** | $O(1)$ avg ops; unordered, so min is linear |
> | b | **Balanced BST / AVL** | every operation $O(\log n)$, incl. find-min |
> | c | **Stack** | LIFO by definition |
> | d | **Queue** | FIFO, $O(1)$ both ends |
> | e | **Max-heap** | $O(1)$ find-max, $O(\log n)$ extract-max |

---

> [!question] Q: Master complexity table (average case)
>
> Fill **search / insert / delete / find-min** for each.
>
> | Structure | Search | Insert | Delete | Find-min |
> |---|---|---|---|---|
> | Unsorted array | ? | ? | ? | ? |
> | Sorted array | ? | ? | ? | ? |
> | Singly linked list | ? | ? | ? | ? |
> | Hash table | ? | ? | ? | ? |
> | Balanced BST (AVL) | ? | ? | ? | ? |
> | Binary min-heap | ? | ? | ? | ? |

> [!success]- Solution
>
> | Structure | Search | Insert | Delete | Find-min |
> |---|---|---|---|---|
> | Unsorted array | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |
> | Sorted array | $O(\log n)$ | $O(n)$ | $O(n)$ | $O(1)$ |
> | Singly linked list | $O(n)$ | $O(1)$ | $O(1)$* | $O(n)$ |
> | Hash table | $O(1)$ | $O(1)$ | $O(1)$ | $O(n)$ |
> | Balanced BST (AVL) | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
> | Binary min-heap | $O(n)$ | $O(\log n)$ | $O(\log n)$† | $O(1)$ |
>
> *List delete is $O(1)$ given a pointer to the node, else $O(n)$ to find it. †Heap delete is $O(\log n)$ for the min (root); arbitrary delete needs a position index.

---

> [!question] Q: One disadvantage each — name it
>
> State the single most important **disadvantage** of each, exam-style.
> a) Hash table   b) AVL tree   c) Static-array stack   d) Adjacency matrix   e) Quick sort

> [!success]- Solution
>
> | | disadvantage |
> |---|---|
> | a) Hash table | no useful ordering ⇒ range queries / find-min are $O(n)$; worst case $O(n)$ on bad hashing |
> | b) AVL tree | rotations on every insert/delete ⇒ higher constant factor than a plain BST |
> | c) Static-array stack | fixed capacity ⇒ **stack overflow** when exceeded |
> | d) Adjacency matrix | $\Theta(|V|^2)$ space even for sparse graphs; neighbour scan is $O(|V|)$ |
> | e) Quick sort | $O(n^2)$ worst case (bad pivots); not stable |

---

> [!question] Q: Capstone — design a phone-book autocomplete
>
> You must support: insert a contact, look up by exact name in near-$O(1)$, and list all names with a given prefix. Which structures, and why a hash table alone is insufficient?

> [!success]- Solution
>
> - **Exact lookup / insert:** a **hash table** keyed by full name gives $O(1)$ average.
> - **Prefix listing:** a hash table cannot do this — hashing destroys ordering and locality, so there is no way to enumerate "all keys starting with `An`" without scanning every bucket ($O(n)$).
> - **Fix:** add a **trie** (prefix tree) — $O(L)$ to walk the prefix of length $L$, then collect the subtree; or a **balanced BST** for $O(\log n)$ ordered range scans. Pairing a hash table (point queries) with a trie/BST (prefix/range queries) is the standard composite design.

---

> [!quote] End of sheet
> Re-derive, don't memorize. Every table above was recomputed by hand — if a number here ever disagrees with a graded paper, recompute it yourself and trust the derivation, not the red pen.
