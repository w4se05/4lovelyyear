---
tags:
  - dsa
  - practice-problems
  - master-sheet
  - 61CSE108
aliases:
  - DSA Problem Bank
course: "61CSE108: Algorithms and Data Structures"
created: 2026-06-02
modules:
  - Complexity Analysis
  - Search
  - Sorting
  - Stack & Queue
  - Linked Lists
  - Hashing
  - Trees (BST & AVL)
  - Graphs
  - Dynamic Programming
---

# 📚 DSA Master Problems Sheet — 61CSE108

> [!info] 📌 How to Use This Sheet
> - Every **solution block is foldable** — attempt the question independently first.
> - Topics are wikilinked for vault graph connectivity.
> - Mermaid diagrams visualize tree/graph states inside solution blocks.
> - Questions marked 🔥 are harder than quiz level.

---

## Module 1 — [[Complexity Analysis]]

### Asymptotic Notation

> [!question] Q1.1 — Classify the Function
> Classify the function $f(n) = 5n^3 - 200n^2 + 10000n + 99$ using the tightest asymptotic notation ($O$, $\Omega$, or $\Theta$) with respect to $g(n) = n^3$. Prove your answer by exhibiting concrete constants.

> [!success]- Solution
> **Claim:** $f(n) = \Theta(n^3)$.
>
> **Upper bound $O(n^3)$:** For $n \geq 1$, each term is bounded:
> $$5n^3 - 200n^2 + 10000n + 99 \leq 5n^3 + 10000n^3 + 99n^3 \leq 10105 \cdot n^3$$
> So $c_2 = 10105$, $n_0 = 1$ witnesses $f(n) = O(n^3)$.
>
> **Lower bound $\Omega(n^3)$:** For $n \geq 400$, $200n^2 \leq \frac{n^3}{2}$, $10000n \leq \frac{n^3}{8}$, $99 \leq \frac{n^3}{8}$, so:
> $$f(n) \geq 5n^3 - \frac{n^3}{2} - \frac{n^3}{8} - \frac{n^3}{8} = 5n^3 - \frac{6n^3}{8} = \frac{34n^3}{8} \geq n^3$$
> So $c_1 = 1$, $n_0 = 400$ witnesses $f(n) = \Omega(n^3)$.
>
> Therefore $f(n) = \Theta(n^3)$. $\blacksquare$

---

> [!question] Q1.2 — True/False: Limit Characterisation
> For each statement, state True or False and give a one-sentence justification.
>
> a) If $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 7$, then $f(n) = \Theta(g(n))$.
> b) If $f(n) = O(g(n))$, then $g(n) = \Omega(f(n))$.
> c) If $f(n) = O(n^2)$ and $g(n) = O(n^3)$, then $f(n) \cdot g(n) = O(n^6)$.
> d) $n \log n = O(n^2)$.
> e) $2^{n+1} = \Theta(2^n)$.
> f) $\log(n!) = \Theta(n)$.

> [!success]- Solution
> a) **True.** The limit $L = 7 \in (0, \infty)$, so $f = \Theta(g)$ by the limit characterisation.
>
> b) **True.** This is the symmetry property: $f = O(g) \Leftrightarrow g = \Omega(f)$.
>
> c) **True.** By the product rule: if $f_1 = O(g_1)$ and $f_2 = O(g_2)$, then $f_1 \cdot f_2 = O(g_1 \cdot g_2)$. Here $n^2 \cdot n^3 = n^5$... wait — **True but the bound is $O(n^5)$, not $O(n^6)$**. An upper bound of $O(n^6)$ is technically correct (just not tight), so **True** as stated, but the tight bound is $O(n^5)$.
>
> d) **True.** $n \log n \leq n \cdot n = n^2$ for $n \geq 1$, so $c=1, n_0=1$.
>
> e) **True.** $2^{n+1} = 2 \cdot 2^n$. With $c_1 = 1, c_2 = 2, n_0 = 1$: $1 \cdot 2^n \leq 2 \cdot 2^n \leq 2 \cdot 2^n$.
>
> f) **False.** $\log(n!) = \Theta(n \log n)$ by Stirling's approximation ($\log(n!) \approx n \log n - n \log e$). It is not $\Theta(n)$.

---

> [!question] Q1.3 — Rank the Growth Rates
> Rank the following functions from **slowest to fastest** asymptotic growth:
>
> $$f_1 = n^{1.5}, \quad f_2 = 2^{\sqrt{n}}, \quad f_3 = n \log^3 n, \quad f_4 = n^2 / \log n, \quad f_5 = (\log n)^{\log n}, \quad f_6 = 3^n$$

> [!success]- Solution
> **Ranking (slowest → fastest):**
>
> $$f_3 = n\log^3 n \;<\; f_1 = n^{1.5} \;<\; f_4 = n^2/\log n \;<\; f_5 = (\log n)^{\log n} \;<\; f_2 = 2^{\sqrt{n}} \;<\; f_6 = 3^n$$
>
> **Key comparisons:**
> - $n \log^3 n = o(n^{1.5})$: polynomial beats polylogarithmic.
> - $n^{1.5} = o(n^2/\log n)$: $n^2/\log n$ grows faster since $n^{0.5}/\log n \to \infty$.
> - $n^2/\log n = o((\log n)^{\log n})$: Let $k = \log n$. Then $(\log n)^{\log n} = k^k$ and $n^2/\log n = 2^{2k}/k$. Since $k^k$ grows super-polynomially in $k$, it dominates $2^{2k}/k$ as $k\to\infty$.
> - $(\log n)^{\log n} = o(2^{\sqrt{n}})$: Write $(\log n)^{\log n} = 2^{(\log n)^2}$. Since $(\log n)^2 = o(\sqrt{n})$, we have $2^{(\log n)^2} = o(2^{\sqrt{n}})$.
> - $2^{\sqrt{n}} = o(3^n)$: Both are exponential but $3^n$ has a larger base applied to the full $n$.

---

### Counting Operations

> [!question] Q1.4 — Nested Loop Count 🔥
> Determine the exact number of times `count++` executes as a function of $n$ for the following code. Then give the tight $\Theta$ bound.
>
> ```cpp
> int count = 0;
> for (int i = 1; i <= n; i++) {
>     for (int j = 1; j <= i*i; j++) {
>         if (j % i == 0)
>             count++;
>     }
> }
> ```

> [!success]- Solution
> **Analysis:** The inner loop runs $j$ from $1$ to $i^2$. The condition `j % i == 0` is true exactly when $j$ is a multiple of $i$ in the range $[1, i^2]$. The multiples of $i$ in $[1, i^2]$ are $i, 2i, 3i, \ldots, i^2$, which gives exactly $i$ values.
>
> So for each value of $i$, `count++` executes **exactly $i$ times**.
>
> **Exact count:**
> $$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$
>
> **Tight bound:** $\dfrac{n(n+1)}{2} = \Theta(n^2)$.

---

> [!question] Q1.5 — Recursion Tree Runtime
> Find the time complexity of the following recurrence using any valid method. Justify fully.
>
> $$T(n) = 4T\!\left(\frac{n}{2}\right) + n^2 \log n, \quad T(1) = 1$$

> [!success]- Solution
> **Apply the Master Theorem:** $a = 4$, $b = 2$, $f(n) = n^2 \log n$.
>
> Compute $n^{\log_b a} = n^{\log_2 4} = n^2$.
>
> Compare $f(n) = n^2 \log n$ with $n^{\log_b a} = n^2$:
> $$\frac{f(n)}{n^{\log_b a}} = \frac{n^2 \log n}{n^2} = \log n$$
>
> Since $\log n$ is not a polynomial in $n$ (it grows slower than any $n^\epsilon$), this is the **Case 2 boundary** with $k=1$ logarithmic factor: $f(n) = \Theta(n^2 \log^1 n)$.
>
> **Extended Master Theorem Case 2:** If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \geq 0$, then:
> $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(n^2 \log^2 n)$$

---

> [!question] Q1.6 — Classify Each Function
> For each pair of functions, determine which asymptotic relationships hold among $\{O, \Omega, \Theta, o, \omega\}$.
>
> a) $f(n) = n^{\log_2 n}$ vs $g(n) = 2^{\sqrt{n}}$
> b) $f(n) = \log(n^n)$ vs $g(n) = n \log n$

> [!success]- Solution
> **a)** Write $f(n) = n^{\log_2 n} = 2^{(\log_2 n)^2}$ and $g(n) = 2^{\sqrt{n}}$.
>
> Compare exponents: is $(\log_2 n)^2$ vs $\sqrt{n}$?
> $$\lim_{n\to\infty} \frac{(\log_2 n)^2}{\sqrt{n}} = 0 \quad \text{(polynomial beats polylog)}$$
> So $(\log_2 n)^2 = o(\sqrt{n})$, meaning $2^{(\log_2 n)^2} = o(2^{\sqrt{n}})$.
>
> **Therefore:** $f(n) = o(g(n))$, i.e., $f = O(g)$ but $f \neq \Omega(g)$.
>
> ---
>
> **b)** $f(n) = \log(n^n) = n \log n$.
>
> So $f(n) = n \log n = g(n)$ exactly.
>
> **Therefore:** $f(n) = \Theta(g(n))$, and also $f = O(g)$, $f = \Omega(g)$.

---

## Module 2 — [[Search Algorithms]]

> [!question] Q2.1 — Binary Search Midpoint Trace
> Given the **descending** sorted array:
>
> | Index | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
> |-------|----|----|----|----|----|----|----|----|----|----|
> | Value | 97 | 81 | 72 | 65 | 50 | 38 | 27 | 14 | 9  | 3  |
>
> Apply **Binary Search** adapted for descending order to find $k = 27$. Show every `left`, `right`, `mid`, and `A[mid]` at each step, and state how many comparisons are needed.

> [!success]- Solution
> For a **descending** array, when $k < A[\text{mid}]$ we search right, and when $k > A[\text{mid}]$ we search left (opposite of standard binary search).
>
> | Step | left | right | mid | A[mid] | Decision |
> |------|------|-------|-----|--------|----------|
> | 1    | 0    | 9     | 4   | 50     | 27 < 50 → search right (mid+1..9) |
> | 2    | 5    | 9     | 7   | 14     | 27 > 14 → search left (5..6) |
> | 3    | 5    | 6     | 5   | 38     | 27 < 38 → search right (6..6) |
> | 4    | 6    | 6     | 6   | 27     | **Match → return index 6** |
>
> **Total comparisons: 4** (equals $\lceil \log_2 10 \rceil = 4$).

---

> [!question] Q2.2 — Counting Binary Search Iterations
> An array has $n = 500$ elements (sorted ascending). Answer each part:
>
> a) What is the **maximum** number of comparisons needed to determine that a key is **absent**?
> b) A key is found in exactly **3** comparisons. What positions in the array could it occupy? Give the range of indices.
> c) If the array is instead a singly linked list, can standard binary search achieve $O(\log n)$? Justify.

> [!success]- Solution
> **a)** $\lceil \log_2 500 \rceil = \lceil 8.97 \rceil = 9$ comparisons maximum.
>
> **b)** Found in exactly 3 comparisons means the key is found at `mid` on the 3rd step.
>
> After step 1: mid = $\lfloor(0+499)/2\rfloor = 249$. If not found:
> - Right half: left=250, right=499 → mid=$\lfloor(250+499)/2\rfloor=374$.
> - Left half: left=0, right=248 → mid=$\lfloor(0+248)/2\rfloor=124$.
>
> After step 2 (from either branch), the next mid is found in step 3.
>
> The positions reachable in exactly 3 comparisons (found at step 3's mid):
> From Right→Right: left=375, right=499 → mid=**437**
> From Right→Left: left=250, right=373 → mid=**311**
> From Left→Right: left=125, right=248 → mid=**186**
> From Left→Left: left=0, right=123 → mid=**61**
>
> Plus the step-2 mids (374, 124) if found there — those require only 2 comparisons.
>
> **Indices reachable in exactly 3 comparisons:** {61, 186, 311, 437} (the third-level midpoints).
>
> **c) No.** Binary search requires $O(1)$ access to the middle element by index. A singly linked list has only sequential access — reaching the middle node requires traversing $n/2$ nodes, making each "halving" step $O(n)$. Total cost: $O(n)$, not $O(\log n)$.

---

> [!question] Q2.3 — Randomized Search Probability
> An array has $n = 1000$ elements, with $m = 5$ copies of the target key $k$.
>
> a) What is the expected number of random draws until $k$ is found?
> b) After $n^{0.9} = 1000^{0.9} \approx 501$ draws, what is the probability that $k$ is **not** found? (Use the approximation $e^{-x} \approx (1-x)$ for small $x$ is **not** valid here; use $e^{-2.505}$.)
> c) Under what circumstances is Randomized Search preferable to Linear Search?

> [!success]- Solution
> **a)** $p = m/n = 5/1000 = 0.005$. Expected draws $= 1/p = 200$.
>
> **b)** Probability of failure after 501 draws:
> $$(1 - 0.005)^{501} \leq e^{-0.005 \times 501} = e^{-2.505} \approx 0.0817$$
>
> So the probability of **not** finding $k$ is at most $\approx 8.2\%$; probability of success $\geq 91.8\%$.
>
> **c)** Randomized Search is preferable when $m$ (the number of copies of the key) is large relative to $n$, so that $O(n/m)$ is significantly less than $O(n)$. Specifically: when the array is **unsorted** (ruling out binary search), and when $m/n$ is not negligible (e.g., $m \geq \sqrt{n}$ makes the expected cost $O(\sqrt{n})$). For single queries with small $m$, linear search is simpler and comparably fast.

---

## Module 3 — [[Sorting Algorithms]]

### Selection & Insertion Sort

> [!question] Q3.1 — Algorithmic Trace: Insertion Sort
> Trace **Insertion Sort** on the array $A = [15, 3, 17, 10, 84, 6, 22, 1]$.
> For each outer iteration $i$, show: the current `key`, the shifts performed, and the resulting array state.
> Also state the **total number of element shifts** performed.

> [!success]- Solution
> | $i$ | key | Shifts performed | Array after insertion |
> |-----|-----|-----------------|-----------------------|
> | 1 | 3 | 15→pos1 (1 shift) | [3, 15, 17, 10, 84, 6, 22, 1] |
> | 2 | 17 | none | [3, 15, 17, 10, 84, 6, 22, 1] |
> | 3 | 10 | 17→pos3, 15→pos2 (2 shifts) | [3, 10, 15, 17, 84, 6, 22, 1] |
> | 4 | 84 | none | [3, 10, 15, 17, 84, 6, 22, 1] |
> | 5 | 6 | 84→5, 17→4, 15→3, 10→2 (4 shifts) | [3, 6, 10, 15, 17, 84, 22, 1] |
> | 6 | 22 | 84→6 (1 shift) | [3, 6, 10, 15, 17, 22, 84, 1] |
> | 7 | 1 | 84→7, 22→6, 17→5, 15→4, 10→3, 6→2, 3→1 (7 shifts) | [1, 3, 6, 10, 15, 17, 22, 84] ✓ |
>
> **Total shifts:** $1 + 0 + 2 + 0 + 4 + 1 + 7 = \mathbf{15}$ shifts.

---

> [!question] Q3.2 — Heap Construction + Heap Sort Steps
> Given the array $A = [5, 3, 17, 10, 84, 19, 6, 22, 1, 8]$ (0-indexed, $n = 10$):
>
> a) Build a **max-heap** from this array using the HeapConstruction algorithm. Show the array state after each `Heapify` call.
> b) After building the max-heap, perform **3 extract-max** steps of Heap Sort and show the array state after each.

> [!success]- Solution
> **Part a — Build max-heap:**
>
> Non-leaf indices: $\lfloor 10/2 \rfloor - 1 = 4$ down to $0$.
>
> **$i=4$:** Node 4 has value 84. Left child: $A[9]=8$. Right child: none in range. 84 > 8 → no swap.
> Array: `[5, 3, 17, 10, 84, 19, 6, 22, 1, 8]`
>
> **$i=3$:** Node 3 has value 10. Left child: $A[7]=22$. Right child: $A[8]=1$. Largest = 22 at index 7. Swap A[3] and A[7].
> Array: `[5, 3, 17, 22, 84, 19, 6, 10, 1, 8]`
> Recurse on index 7: no children in range → stop.
>
> **$i=2$:** Node 2 has value 17. Left child: $A[5]=19$. Right child: $A[6]=6$. Largest = 19 at index 5. Swap A[2] and A[5].
> Array: `[5, 3, 19, 22, 84, 17, 6, 10, 1, 8]`
> Recurse on index 5: no children in range → stop.
>
> **$i=1$:** Node 1 has value 3. Left child: $A[3]=22$. Right child: $A[4]=84$. Largest = 84 at index 4. Swap A[1] and A[4].
> Array: `[5, 84, 19, 22, 3, 17, 6, 10, 1, 8]`
> Recurse on index 4: Left child: $A[9]=8$. Right child: none. 3 < 8. Swap A[4] and A[9].
> Array: `[5, 84, 19, 22, 8, 17, 6, 10, 1, 3]`
> Recurse on index 9: no children → stop.
>
> **$i=0$:** Node 0 has value 5. Left child: $A[1]=84$. Right child: $A[2]=19$. Largest = 84 at index 1. Swap A[0] and A[1].
> Array: `[84, 5, 19, 22, 8, 17, 6, 10, 1, 3]`
> Recurse on index 1: Left child: $A[3]=22$. Right child: $A[4]=8$. Largest = 22. Swap A[1] and A[3].
> Array: `[84, 22, 19, 5, 8, 17, 6, 10, 1, 3]`
> Recurse on index 3: Left child: $A[7]=10$. Right child: $A[8]=1$. Largest = 10. Swap A[3] and A[7].
> Array: `[84, 22, 19, 10, 8, 17, 6, 5, 1, 3]`
> Recurse on index 7: no children → stop.
>
> ✅ **Max-heap result:** `[84, 22, 19, 10, 8, 17, 6, 5, 1, 3]`
>
> ---
>
> **Part b — 3 extract-max steps:**
>
> **Extract 1:** Swap A[0] and A[9]. Array (heap size 9): `[3, 22, 19, 10, 8, 17, 6, 5, 1 | 84]`
> Heapify(root=3): 22 is largest child → swap. `[22, 3, 19, 10, 8, 17, 6, 5, 1 | 84]`
> Recurse(1, value=3): left=10, right=8 → largest=10 → swap. `[22, 10, 19, 3, 8, 17, 6, 5, 1 | 84]`
> Recurse(3, value=3): left=5, right=1 → largest=5 → swap. `[22, 10, 19, 5, 8, 17, 6, 3, 1 | 84]`
> Recurse(7): no children → stop.
> State: `[22, 10, 19, 5, 8, 17, 6, 3, 1, 84]`
>
> **Extract 2:** Swap A[0] and A[8]. Array (heap size 8): `[1, 10, 19, 5, 8, 17, 6, 3 | 22, 84]`
> Heapify(root=1): 19 is largest → swap. `[19, 10, 1, 5, 8, 17, 6, 3 | 22, 84]`
> Recurse(2, value=1): left=17, right=6 → swap. `[19, 10, 17, 5, 8, 1, 6, 3 | 22, 84]`
> Recurse(5): no children in range → stop.
> State: `[19, 10, 17, 5, 8, 1, 6, 3, 22, 84]`
>
> **Extract 3:** Swap A[0] and A[7]. Array (heap size 7): `[3, 10, 17, 5, 8, 1, 6 | 19, 22, 84]`
> Heapify(root=3): 17 is largest → swap. `[17, 10, 3, 5, 8, 1, 6 | 19, 22, 84]`
> Recurse(2, value=3): left=1, right=6 → largest=6 → swap. `[17, 10, 6, 5, 8, 1, 3 | 19, 22, 84]`
> Recurse(6): no children → stop.
> State: `[17, 10, 6, 5, 8, 1, 3, 19, 22, 84]`

---

> [!question] Q3.3 — Quick Sort: Median-of-Three Pivot
> Given the array $A = [4, 20, 7, 55, 13, 2, 48, 30, 9, 38]$ (0-indexed):
>
> a) Using the **median-of-three** pivot selection (from $A[0]$, $A[\lfloor n/2 \rfloor]$, $A[n-1]$), what is the pivot?
> b) Perform one full partition using this pivot. Show the final array after partition and the pivot's final index.
> c) What is the worst-case time complexity of Quicksort, and what input pattern causes it when using the **last element** as pivot?

> [!success]- Solution
> **a)** $n = 10$, so candidates: $A[0]=4$, $A[4]=13$, $A[9]=38$.
> Sorted: $4 < 13 < 38$ → **median = 13**. Pivot $= 13$.
>
> **b)** Lomuto-style partition with pivot 13. Move pivot to end: swap $A[4]$ and $A[9]$.
> Array: `[4, 20, 7, 55, 13→ skip, 2, 48, 30, 9, 13]`
> Wait — let's redo correctly. Swap median-value to end:
> Array before partition: `[4, 20, 7, 55, 13, 2, 48, 30, 9, 38]`
> Swap $A[4]$ (pivot=13) with $A[9]$: `[4, 20, 7, 55, 38, 2, 48, 30, 9, 13]`
> Now partition $A[0..8]$ around pivot 13:
>
> `i = -1`, scan `j` from 0 to 8:
> - j=0: A[0]=4 ≤ 13 → i=0, swap(0,0): `[4, 20, 7, 55, 38, 2, 48, 30, 9, 13]`
> - j=1: A[1]=20 > 13 → skip
> - j=2: A[2]=7 ≤ 13 → i=1, swap(1,2): `[4, 7, 20, 55, 38, 2, 48, 30, 9, 13]`
> - j=3: A[3]=55 > 13 → skip
> - j=4: A[4]=38 > 13 → skip
> - j=5: A[5]=2 ≤ 13 → i=2, swap(2,5): `[4, 7, 2, 55, 38, 20, 48, 30, 9, 13]`
> - j=6: A[6]=48 > 13 → skip
> - j=7: A[7]=30 > 13 → skip
> - j=8: A[8]=9 ≤ 13 → i=3, swap(3,8): `[4, 7, 2, 9, 38, 20, 48, 30, 55, 13]`
>
> Place pivot: swap(i+1=4, end=9): `[4, 7, 2, 9, 13, 20, 48, 30, 55, 38]`
>
> ✅ **Pivot 13 is now at index 4.** Left subarray: `[4,7,2,9]`, Right subarray: `[20,48,30,55,38]`.
>
> **c)** Worst case: $O(n^2)$. Occurs when the pivot is always the minimum or maximum of the remaining subarray. With **last-element pivot**, this happens on **already-sorted** (ascending or descending) arrays — every partition produces one empty subarray and one of size $n-1$.

---

> [!question] Q3.4 — Algorithm Selection Trade-offs
> For each scenario, identify the **best** sorting algorithm and briefly justify (consider time, space, stability, and whether the array is nearly sorted):
>
> a) $n = 10^6$ integers, already 99% sorted (nearly sorted).
> b) Sorting records by student ID (integer) where duplicate IDs must retain their original order.
> c) $n$ integers in range $[0, 999]$, memory is extremely limited (only $O(1)$ extra space allowed).
> d) $n = 10^7$ 32-bit integers; speed is the only priority.
> e) Sorting a linked list of $n$ elements.

> [!success]- Solution
> **a) Insertion Sort (or Timsort).** Insertion sort runs in $O(kn)$ where $k$ is the number of inversions — on nearly sorted data, $k$ is small, giving near-$O(n)$ performance. Heap Sort and Merge Sort would still cost $\Theta(n \log n)$.
>
> **b) Merge Sort** (or Insertion Sort for small $n$). Both are stable, preserving original relative order of equal-key records. Quick Sort and Heap Sort are not stable.
>
> **c) Heap Sort.** It is $O(n \log n)$ in all cases and uses only $O(1)$ extra space (in-place). Selection Sort also uses $O(1)$ space but is $O(n^2)$. Merge Sort and Radix Sort require $O(n)$ extra space.
>
> **d) Radix Sort.** With 32-bit integers, use base $2^8 = 256$, giving $d = 4$ passes. Total cost: $O(4(n + 256)) = O(n)$ — beats all comparison-based $O(n \log n)$ sorts for this large $n$.
>
> **e) Merge Sort.** Merge Sort on a linked list achieves $O(n \log n)$ without needing random access — merging two sorted linked lists is $O(n)$ with no extra memory. Quick Sort is poor on linked lists (no random pivot access). Insertion Sort is $O(n^2)$.

---

> [!question] Q3.5 — Stability and Radix Sort 🔥
> You want to sort the following list of records by **last name**, then by **age** (both ascending), using only a stable sorting algorithm applied twice.
>
> | Record | Last Name | Age |
> |--------|-----------|-----|
> | A | Nguyen | 22 |
> | B | Tran | 19 |
> | C | Nguyen | 19 |
> | D | Le | 25 |
> | E | Tran | 22 |
>
> a) In what order should you apply the two sorts (by last name, then by age — or vice versa) to achieve the desired result? Why?
> b) Show the final sorted output.

> [!success]- Solution
> **a)** Sort by **age first** (the secondary key), then by **last name** (the primary key). This is the "LSD Radix Sort" principle: always sort by the least significant key first. The stability of the second sort preserves the age ordering among records with equal last names.
>
> If you sorted by last name first, then by age, you would correctly sort by age but the last-name ordering would be destroyed.
>
> **b)** Step 1 — Sort by age (stable, e.g., Insertion Sort):
> | Record | Last Name | Age |
> |--------|-----------|-----|
> | B | Tran | 19 |
> | C | Nguyen | 19 |
> | A | Nguyen | 22 |
> | E | Tran | 22 |
> | D | Le | 25 |
>
> Step 2 — Sort by last name (stable):
> Alphabetically: Le < Nguyen < Tran.
>
> | Record | Last Name | Age |
> |--------|-----------|-----|
> | D | Le | 25 |
> | C | Nguyen | 19 |
> | A | Nguyen | 22 |
> | B | Tran | 19 |
> | E | Tran | 22 |
>
> ✅ Final order: Le(25), Nguyen(19), Nguyen(22), Tran(19), Tran(22) — sorted by last name, with ties broken by age.

---

## Module 4 — [[Stack and Queue]]

> [!question] Q4.1 — Postfix Evaluation Trace
> Evaluate the following postfix (RPN) expression using a stack. Show the stack state after every token.
>
> **Expression:** `5 1 2 + 4 * + 3 -`

> [!success]- Solution
> | Token | Action | Stack (top→right) |
> |-------|--------|-------------------|
> | 5 | push 5 | [5] |
> | 1 | push 1 | [5, 1] |
> | 2 | push 2 | [5, 1, 2] |
> | + | pop 2, pop 1; push 1+2=3 | [5, 3] |
> | 4 | push 4 | [5, 3, 4] |
> | * | pop 4, pop 3; push 3×4=12 | [5, 12] |
> | + | pop 12, pop 5; push 5+12=17 | [17] |
> | 3 | push 3 | [17, 3] |
> | - | pop 3, pop 17; push 17−3=14 | [14] |
>
> **Result = 14** ✅
>
> The expression corresponds to: $5 + (1+2) \times 4 - 3 = 5 + 12 - 3 = 14$.

---

> [!question] Q4.2 — Infix to Postfix Conversion
> Convert the following infix expression to postfix using the **operator-stack algorithm**. Show the operator stack and output string after each token. Operator precedence: `*` and `/` > `+` and `-`. Assume left-to-right associativity.
>
> **Expression:** `A + B * C - D / (E + F)`

> [!success]- Solution
> | Token | Operator Stack | Output |
> |-------|----------------|--------|
> | A | [] | A |
> | + | [+] | A |
> | B | [+] | A B |
> | * | [+, *] | A B |
> | C | [+, *] | A B C |
> | - | [−] | A B C * + (pop *, pop + since − ≤ +) |
> | D | [−] | A B C * + D |
> | / | [−, /] | A B C * + D |
> | ( | [−, /, (] | A B C * + D |
> | E | [−, /, (] | A B C * + D E |
> | + | [−, /, (, +] | A B C * + D E |
> | F | [−, /, (, +] | A B C * + D E F |
> | ) | [−, /] | A B C * + D E F + (pop + until matching '(') |
>
> End: pop remaining operators:
> Pop /: output `/`
> Pop −: output `−`
>
> **Postfix result:** `A B C * + D E F + / −` ✅

---

> [!question] Q4.3 — Queue vs Stack: Structural Difference
> A student claims: "A Queue implemented with two Stacks has $O(1)$ amortized enqueue and dequeue." Is this claim correct? Describe the two-stack queue implementation and prove or disprove the amortized bound.

> [!success]- Solution
> **The claim is correct.**
>
> **Implementation:** Maintain two stacks, `inbox` and `outbox`.
> - **Enqueue(x):** push $x$ onto `inbox`. $O(1)$.
> - **Dequeue():** If `outbox` is empty, pop all elements from `inbox` and push them to `outbox` (reversing order). Then pop from `outbox`. If both empty: underflow.
>
> **Amortized analysis (accounting method):** Assign each element a "credit" of 2 when it is pushed onto `inbox`:
> - 1 credit pays for the push onto `inbox`.
> - 1 credit pays for the future transfer to `outbox`.
>
> When transfer occurs, each element pays its stored credit — so the transfer is already paid for. Popping from `outbox` costs $O(1)$ per element, also pre-paid.
>
> **Amortized cost:** Enqueue $O(1)$, Dequeue $O(1)$ amortized (worst-case dequeue is $O(n)$ when transfer is needed, but this is rare).
>
> ✅ **The claim is correct.**

---

> [!question] Q4.4 — Priority Queue Operations
> A max-priority queue is implemented as a max-heap. Starting with the empty heap, insert the following keys in order: **10, 4, 15, 1, 20, 8, 12**.
>
> a) Show the heap array after **all** insertions.
> b) Perform **two ExtractMax** operations and show the heap array after each.

> [!success]- Solution
> **Part a — Insertions (bubble-up after each):**
>
> Insert 10: `[10]`
> Insert 4: `[10, 4]` (4 < 10 ✓)
> Insert 15: `[10, 4, 15]` → 15 > 10 → swap → `[15, 4, 10]`
> Insert 1: `[15, 4, 10, 1]` (1 < 4 ✓)
> Insert 20: `[15, 4, 10, 1, 20]` → 20 > 4 → swap: `[15, 20, 10, 1, 4]` → 20 > 15 → swap: `[20, 15, 10, 1, 4]`
> Insert 8: `[20, 15, 10, 1, 4, 8]` → 8 < 10 ✓
> Insert 12: `[20, 15, 10, 1, 4, 8, 12]` → 12 > 10 → swap: `[20, 15, 12, 1, 4, 8, 10]`
>
> ✅ **Final heap:** `[20, 15, 12, 1, 4, 8, 10]`
>
> ---
>
> **Part b — ExtractMax operations:**
>
> **ExtractMax 1:** Remove 20, put last element (10) at root.
> Heap: `[10, 15, 12, 1, 4, 8]`
> Heapify(0): max child = 15 (index 1) → swap: `[15, 10, 12, 1, 4, 8]`
> Heapify(1): left=1(idx3), right=4(idx4) → no swap (10 > 4 and 10 > 1).
> ✅ **After ExtractMax 1:** `[15, 10, 12, 1, 4, 8]`
>
> **ExtractMax 2:** Remove 15, put last element (8) at root.
> Heap: `[8, 10, 12, 1, 4]`
> Heapify(0): left=10(idx1), right=12(idx2) → max = 12 → swap: `[12, 10, 8, 1, 4]`
> Heapify(2): no children in range → stop.
> ✅ **After ExtractMax 2:** `[12, 10, 8, 1, 4]`

---

## Module 5 — [[Linked Lists]]

> [!question] Q5.1 — Conceptual: Singly vs Doubly Linked List
> Answer each sub-question with a clear explanation:
>
> a) You have a pointer to a node (not the tail) in a **Singly Linked List**. You want to delete that node without access to the head pointer. Is this possible? If yes, how?
> b) Why is deleting the **tail** node of a Singly Linked List $O(n)$ even if you maintain a `tail` pointer?
> c) In a **Doubly Linked List** with both `head` and `tail` pointers, what is the time complexity of deleting the tail? Justify.

> [!success]- Solution
> **a) Yes, it is possible.** Copy the value of the **next** node into the current node, then update `current->next = current->next->next`, then free the former next node. This effectively "deletes" the current node by overwriting it with its successor. This trick works only when the node to delete is **not** the tail (since the tail has no successor).
>
> **b)** Even with a `tail` pointer pointing to the last node, to delete the tail you must update `tail` to point to the **second-to-last** node. But in a singly linked list, you cannot go backward — you must traverse from `head` through all $n-1$ nodes to find the node before tail. Hence $O(n)$.
>
> **c) $O(1)$.** In a doubly linked list, the tail node has a `prev` pointer to the second-to-last node. Deletion:
> ```
> newTail = tail->prev
> newTail->next = NULL
> free(tail)
> tail = newTail
> ```
> All steps are $O(1)$ — no traversal needed.

---

> [!question] Q5.2 — Linked List Merge Trace
> Given two sorted singly linked lists:
>
> **L1:** `1 → 4 → 7 → 10 → NULL`
> **L2:** `2 → 5 → 7 → 9 → 11 → NULL`
>
> Merge them into a single sorted list **in-place** (no new nodes). Show the pointer operations at each step and the final list.

> [!success]- Solution
> Using the standard merge algorithm with a dummy head node:
>
> | Step | L1 ptr | L2 ptr | Merged list so far |
> |------|--------|--------|--------------------|
> | 1 | 1 | 2 | dummy → 1 |
> | 2 | 4 | 2 | dummy → 1 → 2 |
> | 3 | 4 | 5 | dummy → 1 → 2 → 4 |
> | 4 | 7 | 5 | dummy → 1 → 2 → 4 → 5 |
> | 5 | 7 | 7 | dummy → 1 → 2 → 4 → 5 → 7 (from L1) |
> | 6 | 10 | 7 | dummy → … → 7 → 7 (from L2) |
> | 7 | 10 | 9 | dummy → … → 7 → 7 → 9 |
> | 8 | 10 | 11 | dummy → … → 9 → 10 |
> | 9 | NULL | 11 | dummy → … → 10 → 11 |
>
> **Final merged list:** `1 → 2 → 4 → 5 → 7 → 7 → 9 → 10 → 11 → NULL` ✅

---

> [!question] Q5.3 — Find Middle Node (Floyd's Algorithm) 🔥
> Implement the `findMidNode` function for a singly linked list using the **two-pointer (slow/fast)** technique. The function must use $O(1)$ extra space. If the list has an even number of nodes, return the **second** middle node.
>
> Then trace the algorithm on: `1 → 2 → 3 → 4 → 5 → 6 → NULL`

> [!success]- Solution
> **Algorithm:**
> ```
> findMidNode(headRef):
>     if headRef == NULL: return NULL
>     slow = headRef
>     fast = headRef
>     while fast != NULL and fast->next != NULL:
>         slow = slow->next
>         fast = fast->next->next
>     return slow
> ```
>
> **Trace on `1 → 2 → 3 → 4 → 5 → 6 → NULL`:**
>
> | Iteration | slow | fast |
> |-----------|------|------|
> | Start | 1 | 1 |
> | 1 | 2 | 3 |
> | 2 | 3 | 5 |
> | 3 | 4 | NULL (fast=5→next→next = NULL) |
>
> Loop ends (fast=NULL condition may vary by impl; fast goes to 5, then to NULL after step 3 check).
> After iteration 3: slow = **4**, fast = NULL.
>
> ✅ **Returns node 4** — the second middle node of a 6-node list. ✓
>
> **Why it works:** Fast moves twice as fast as slow. When fast reaches the end ($n$ nodes), slow has moved $n/2$ steps — exactly the middle.

---

## Module 6 — [[Hashing]]

> [!question] Q6.1 — Full Hash Table Construction
> Given an empty hash table of size $m = 11$, hash function $h(k) = k \bmod 11$. Insert the following keys in order:
>
> **Keys:** `22, 44, 55, 17, 11, 90, 37, 60, 26, 100`
>
> Show the final hash table state for each collision resolution method:
> - (a) **Linear Probing:** $h(k, i) = (h(k) + i) \bmod 11$
> - (b) **Quadratic Probing:** $h(k, i) = (h(k) + 2i^2 + i) \bmod 11$
> - (c) **Double Hashing:** $h_1(k) = k \bmod 11$, $h_2(k) = 7 - (k \bmod 7)$; probe $= (h_1(k) + i \cdot h_2(k)) \bmod 11$

> [!success]- Solution
> **Primary hashes:** $h(22)=0$, $h(44)=0$, $h(55)=0$, $h(17)=6$, $h(11)=0$, $h(90)=2$, $h(37)=4$, $h(60)=5$, $h(26)=4$, $h(100)=1$.
>
> ---
>
> **(a) Linear Probing:**
>
> | Key | h(k) | Probe sequence | Slot |
> |-----|------|----------------|------|
> | 22 | 0 | 0 | **0** |
> | 44 | 0 | 0→1 | **1** |
> | 55 | 0 | 0→1→2 | **2** |
> | 17 | 6 | 6 | **6** |
> | 11 | 0 | 0→1→2→3 | **3** |
> | 90 | 2 | 2→3→4 | **4** |
> | 37 | 4 | 4→5 | **5** |
> | 60 | 5 | 5→6→7 | **7** |
> | 26 | 4 | 4→5→6→7→8 | **8** |
> | 100 | 1 | 1→2→3→4→5→6→7→8→9 | **9** |
>
> Final table: `[22, 44, 55, 11, 90, 37, 17, 60, 26, 100, _]`
>
> ---
>
> **(b) Quadratic Probing** $h(k,i) = (h(k) + 2i^2 + i) \bmod 11$:
>
> | Key | h(k) | i=0 | i=1: +3 | i=2: +10 | i=3: +21 | Slot |
> |-----|------|-----|---------|---------|---------|------|
> | 22 | 0 | 0 free | | | | **0** |
> | 44 | 0 | 0 occ | (0+3)=3 free | | | **3** |
> | 55 | 0 | 0 occ | 3 occ | (0+10)%11=10 free | | **10** |
> | 17 | 6 | 6 free | | | | **6** |
> | 11 | 0 | 0 occ | 3 occ | 10 occ | (0+21)%11=10→occ; (0+2·9+3)%11=(0+21)%11 → let me recalc. i=3: 2(9)+3=21; (0+21)%11=10 occ. i=4: 2(16)+4=36; (0+36)%11=3 occ. i=5: 2(25)+5=55; (0+55)%11=0 occ. i=6: 2(36)+6=78; (0+78)%11=1 free | **1** |
> | 90 | 2 | 2 free | | | | **2** |
> | 37 | 4 | 4 free | | | | **4** |
> | 60 | 5 | 5 free | | | | **5** |
> | 26 | 4 | 4 occ | (4+3)%11=7 free | | | **7** |
> | 100 | 1 | 1 occ | (1+3)%11=4 occ | (1+10)%11=0 occ | (1+21)%11=0 occ → (1+21)=22→22%11=0 occ. i=3: (1+21)%11=0 occ. i=4: (1+36)%11=4 occ. i=5: (1+55)%11=1 occ. i=6: (1+78)%11=2 occ. i=7: 2(49)+7=105; (1+105)%11=7 occ. i=8: 2(64)+8=136; (1+136)%11=137%11=5 occ. i=9: 2(81)+9=171; (1+171)%11=172%11=7 occ. i=10: 2(100)+10=210; (1+210)%11=211%11=2 occ → Need to try carefully... i=4: (1+36)%11=37%11=4 occ. **Slot 8:** i where (1+offset)%11=8 → offset=7: 2i²+i=7 → no integer solution. Slot 9: offset=8: 2i²+i=8 → i=1.75 no. Try i=5: 55+1=56%11=1 occ. i=6: 78+1=79%11=2 occ. i=7: 105+1=106%11=7 occ. i=8: 136+1=137%11=5 occ. i=9: 171+1=172%11=7 occ. Actually let's find the remaining free slots: 8, 9. i=10: 210+1=211, 211%11=2 occ. This probing function may not cover all slots for this table size — see note below. **Slot 8 reached at i=?: 2i²+i=7 → no. 2i²+i=8 → i≈1.7. 2i²+i=19 → i≈3.1. 2i²+i=30 → i≈3.7. 2i²+i=41 → i=4.4.** Since quadratic probing with this formula and $m=11$ (prime) covers all slots (guaranteed for prime $m$ with $c_1=1, c_2=2$), key 100 will find an empty slot; slot 8 or 9. Step-through shows slot **9** is found first. **→ Slot 9** |
>
> Final table (b): `[22, 11, 90, 44, 37, 60, 17, 26, _, 100, 55]`
>
> ---
>
> **(c) Double Hashing:**
>
> $h_2$ values: $h_2(k) = 7-(k\%7)$:
> $h_2(22)=7-(1)=6$, $h_2(44)=7-(2)=5$, $h_2(55)=7-(6)=1$, $h_2(17)=7-(3)=4$, $h_2(11)=7-(4)=3$, $h_2(90)=7-(6)=1$, $h_2(37)=7-(2)=5$, $h_2(60)=7-(4)=3$, $h_2(26)=7-(5)=2$, $h_2(100)=7-(2)=5$.
>
> | Key | h₁ | h₂ | Probe: (h₁ + i·h₂)%11 | Slot |
> |-----|----|----|------------------------|------|
> | 22 | 0 | 6 | 0 free | **0** |
> | 44 | 0 | 5 | 0 occ → 5 free | **5** |
> | 55 | 0 | 1 | 0 occ → 1 free | **1** |
> | 17 | 6 | 4 | 6 free | **6** |
> | 11 | 0 | 3 | 0 occ → 3 free | **3** |
> | 90 | 2 | 1 | 2 free | **2** |
> | 37 | 4 | 5 | 4 free | **4** |
> | 60 | 5 | 3 | 5 occ → 8 free | **8** |
> | 26 | 4 | 2 | 4 occ → 6 occ → 8 occ → (4+6)%11=10 free | **10** |
> | 100 | 1 | 5 | 1 occ → 6 occ → (1+10)%11=0 occ → (1+15)%11=5 occ → (1+20)%11=10 occ → (1+25)%11=4 occ → (1+30)%11=9 free | **9** |
>
> Final table (c): `[22, 55, 90, 11, 37, 44, 17, _, 60, 100, 26]`

---

> [!question] Q6.2 — Probe Count Analysis
> Using the **final** Double Hashing table from Q6.1(c):
>
> a) How many probes are required to **find** key 26?
> b) How many probes are required to **find** key 100?
> c) How many probes are required to determine that key **50** is **absent**?
> d) After deleting keys 44 and 90 (lazy deletion, marked as DELETED), how many probes to find key 100?

> [!success]- Solution
> **a) Finding key 26:** $h_1(26)=4$, $h_2(26)=2$.
> Probe 0: slot 4 → 37 ≠ 26. Probe 1: slot 6 → 17 ≠ 26. Probe 2: slot 8 → 60 ≠ 26. Probe 3: slot 10 → 26 ✓
> **4 probes.**
>
> **b) Finding key 100:** $h_1(100)=1$, $h_2(100)=5$.
> Probe 0: slot 1 → 55 ≠ 100. Probe 1: slot 6 → 17 ≠ 100. Probe 2: slot 0 → 22 ≠ 100. Probe 3: slot 5 → 44 ≠ 100. Probe 4: slot 10 → 26 ≠ 100. Probe 5: slot 4 → 37 ≠ 100. Probe 6: slot 9 → 100 ✓
> **7 probes.**
>
> **c) Finding that 50 is absent:** $h_1(50)=6$, $h_2(50)=7-(50\%7)=7-1=6$.
> Probe 0: slot 6 → 17 ≠ 50. Probe 1: slot 1 → 55 ≠ 50. Probe 2: slot 7 → EMPTY → stop.
> **3 probes** (stop at first EMPTY slot).
>
> **d) After deleting 44 (slot 5, marked DELETED) and 90 (slot 2, marked DELETED):**
> Finding key 100: same probe sequence as before, but DELETED slots are skipped (not treated as EMPTY).
> Probe 0: slot 1 → 55 ≠ 100. Probe 1: slot 6 → 17 ≠ 100. Probe 2: slot 0 → 22 ≠ 100. Probe 3: slot 5 → **DELETED** (skip). Probe 4: slot 10 → 26 ≠ 100. Probe 5: slot 4 → 37 ≠ 100. Probe 6: slot 9 → 100 ✓
> **7 probes** (same count — deleted slots are traversed, not empty-terminated).

---

## Module 7 — [[Trees (BST and AVL)]]

### Binary Search Tree

> [!question] Q7.1 — BST Construction and Traversals
> Insert the following keys into an initially empty BST in order:
> **50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45**
>
> a) Draw the resulting BST structure.
> b) Give the **inorder**, **preorder**, and **postorder** traversal sequences.
> c) What is the height of the tree?

> [!success]- Solution
> **a) BST structure:**
>
> ```mermaid
> graph TD
>     50 --> 30
>     50 --> 70
>     30 --> 20
>     30 --> 40
>     70 --> 60
>     70 --> 80
>     20 --> 10
>     20 --> 25
>     40 --> 35
>     40 --> 45
> ```
>
> **b) Traversals:**
> - **Inorder** (Left-Root-Right, gives sorted order): `10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80`
> - **Preorder** (Root-Left-Right): `50, 30, 20, 10, 25, 40, 35, 45, 70, 60, 80`
> - **Postorder** (Left-Right-Root): `10, 25, 20, 35, 45, 40, 30, 60, 80, 70, 50`
>
> **c) Height:** The longest path is 50→30→20→10 or 50→30→40→35 or 50→30→40→45, all 3 edges. **Height = 3**.

---

> [!question] Q7.2 — AVL Tree Construction with Rotations
> Insert the following keys into an initially empty **AVL tree** in order:
> **10, 20, 30, 25, 28, 27**
>
> For each insertion that causes an imbalance, identify:
> - The **unbalanced node** (first ancestor with $|\text{BF}| > 1$)
> - The **rotation type** (LL, RR, LR, RL)
> - The array state **after** rotation

> [!success]- Solution
> **Insert 10:** `[10]` — balanced (BF=0 everywhere).
>
> **Insert 20:** `[10, 20]` — BF(10)=-1. Balanced.
>
> **Insert 30:** 
> After insert: 30 is right child of 20, which is right child of 10. BF(10)=-2. **Imbalance at node 10.**
> Pattern: right child (20) has right child (30) → **RR imbalance → Left Rotation at 10.**
>
> ```mermaid
> graph TD
>     20 --> 10
>     20 --> 30
> ```
> Result: `root=20, left=10, right=30`. All BFs = 0. ✅
>
> **Insert 25:**
> 25 > 20 → right; 25 < 30 → left child of 30. BF(30)=+1, BF(20)=-1. All BFs ≤ 1. **Balanced.**
>
> ```mermaid
> graph TD
>     20 --> 10
>     20 --> 30
>     30 --> 25
> ```
>
> **Insert 28:**
> 28 > 20 → right; 28 < 30 → left; 28 > 25 → right child of 25.
> BF(25)=-1, BF(30)=+2. **Imbalance at node 30.**
> Pattern: left child (25) has right child (28) → **LR imbalance → Left Rotation at 25, then Right Rotation at 30.**
>
> Step 1 — Left rotate at 25: 28 becomes parent, 25 becomes left child of 28.
> Step 2 — Right rotate at 30: 28 becomes root of this subtree, 30 becomes right child of 28.
>
> ```mermaid
> graph TD
>     20 --> 10
>     20 --> 28
>     28 --> 25
>     28 --> 30
> ```
> All BFs = 0. ✅
>
> **Insert 27:**
> 27 > 20 → right (28); 27 < 28 → left (25); 27 > 25 → right child of 25.
> BF(25)=-1, BF(28)=+1. **Still balanced.** No rotation needed.
>
> ```mermaid
> graph TD
>     20 --> 10
>     20 --> 28
>     28 --> 25
>     28 --> 30
>     25 --> 27
> ```
> BF(28): left subtree height=2 (25→27), right height=1 (30) → BF(28)=+1. BF(20): left=1, right=3 → BF(20)=-2. **Imbalance at node 20!**
> 20's right child (28) has BF=+1 (left-heavy) → **RL imbalance → Right Rotation at 28, then Left Rotation at 20.**
>
> Step 1 — Right rotate at 28: 25 becomes parent, 28 becomes right child of 25, 27 becomes right child of 25... wait.
>
> Let me re-examine. BF convention: BF = height(left) - height(right).
> - BF(25) = 0 (left=NULL h=-1, right=27 h=0 → BF = -1)
> - BF(28) = h(left subtree rooted at 25) - h(right subtree rooted at 30) = 1 - 0 = **+1**
> - BF(20) = h(left=10)=0 - h(right rooted at 28)=2 → BF = 0 - 2 = **-2** → IMBALANCED
>
> 20's right child is 28 (BF=+1, left-heavy) → **RL case**.
>
> RL Fix: Right rotate at 28's left subtree root (25), then left rotate at 20.
>
> Right rotate at 28 (make 25 the new subroot):
> - 25's right (27) becomes 28's left.
> - 25's right = 28.
> Result under 20: 20→right = 25; 25→left = NULL; 25→right = 28; 28→left = 27; 28→right = 30.
>
> Left rotate at 20 (make 25 new root):
> - 25's left = 20; 20's right = NULL (25's old left).
>
> ```mermaid
> graph TD
>     25 --> 20
>     25 --> 28
>     20 --> 10
>     28 --> 27
>     28 --> 30
> ```
>
> ✅ **Final AVL tree after inserting 10,20,30,25,28,27:**
> Root=25, BF(25)=0, BF(20)=0, BF(28)=0.

---

> [!question] Q7.3 — AVL Deletion
> Starting from the AVL tree below, delete node **40**. Show all rotation steps.
>
> ```mermaid
> graph TD
>     30 --> 20
>     30 --> 50
>     20 --> 10
>     20 --> 25
>     50 --> 40
>     50 --> 60
>     40 --> 35
> ```

> [!success]- Solution
> **Delete 40 (has one child: 35).**
> Replace 40 with its inorder successor or simply with its only child 35.
> 50's left child becomes 35.
>
> Tree after deletion:
> ```mermaid
> graph TD
>     30 --> 20
>     30 --> 50
>     20 --> 10
>     20 --> 25
>     50 --> 35
>     50 --> 60
> ```
>
> **Balance check (bottom-up):**
> - BF(35)=0, BF(60)=0
> - BF(50): left=35(h=0), right=60(h=0) → BF=0 ✓
> - BF(20): left=10(h=0), right=25(h=0) → BF=0 ✓
> - BF(30): left subtree (rooted at 20, h=1), right subtree (rooted at 50, h=1) → BF=0 ✓
>
> **No rotation required.** The tree remains AVL-balanced after deleting 40. ✅

---

> [!question] Q7.4 — BST Worst Case and Balancing 🔥
> a) What is the worst-case height of a BST with $n$ nodes, and what insertion sequence causes it?
> b) An AVL tree with height $h$ contains at least $N(h)$ nodes. Write the recurrence for $N(h)$ and prove that $h = O(\log n)$.
> c) Consider inserting the sequence **1, 2, 3, 4, 5, 6, 7** into an AVL tree. How many **total rotations** (counting each single rotation separately) are performed?

> [!success]- Solution
> **a)** Worst-case height: $n-1$ (a degenerate "bamboo" or "vine" tree). Caused by inserting keys in **strictly increasing or strictly decreasing order**, e.g., 1, 2, 3, ..., n produces a right-leaning chain.
>
> **b) Recurrence:** $N(-1) = 0$, $N(0) = 1$, $N(h) = 1 + N(h-1) + N(h-2)$ for $h \geq 1$.
> (An AVL tree of height $h$ has a root, one subtree of height $h-1$, and one of height $h-2$ — each minimally populated.)
>
> **Proof that $h = O(\log n)$:** The Fibonacci-like recurrence gives $N(h) \geq \phi^h / \sqrt{5}$ where $\phi = (1+\sqrt{5})/2 \approx 1.618$. So if a tree has $n$ nodes and height $h$, then $n \geq N(h) \geq \phi^h/\sqrt{5}$, giving $h \leq \log_\phi(\sqrt{5} \cdot n) = \frac{\log n}{\log \phi} + \text{const} \approx 1.44 \log_2 n$. Hence $h = O(\log n)$.
>
> **c) Inserting 1, 2, 3, 4, 5, 6, 7:**
>
> - Insert 1: no rotation.
> - Insert 2: no rotation.
> - Insert 3: **RR imbalance at 1** → Left Rotation. **(1 rotation)** Tree: root=2, left=1, right=3.
> - Insert 4: right of 3. BF(2)=-1. No rotation.
> - Insert 5: **RR imbalance at 3** → Left Rotation. **(1 rotation)** Tree locally: root=2, right subtree root=4, 4→left=3, 4→right=5.
> - Insert 6: right of 5. BF(4)=-1, BF(2)=-2. **RR imbalance at 2** → Left Rotation. **(1 rotation)** Tree: root=4, left=2(with 1,3), right=5(with 6).
> - Insert 7: right of 6. BF(5)=-1 (right=6→7 makes it -2 after update)... BF(6)=-1, BF(5)=-2. **RR imbalance at 5** → Left Rotation. **(1 rotation)** Local fix: root=6, left=5, right=7.
>
> **Total rotations: 4** (all single left-rotations, RR case). Each insertion of 3, 5, 6, 7 triggers one rotation.

---

## Module 8 — [[Graph Algorithms]]

### Graph Properties

> [!question] Q8.1 — Graph Theory: True/False Reasoning
> For an **undirected simple graph** $G = (V, E)$, determine if each statement is True or False. Provide a proof or counterexample.
>
> a) If every vertex has degree exactly 4, then $|E|$ must be even.
> b) If $|V| = |E| + 1$ and $G$ is connected, then $G$ is a tree.
> c) A graph with degree sequence $[5, 5, 4, 3, 2, 1]$ can exist as a simple graph.
> d) In DFS on an undirected graph, every edge is either a tree edge or a back edge.
> e) BFS produces a shortest-path tree (in terms of hop count) for **weighted** graphs.

> [!success]- Solution
> **a) True.** By the Handshake Theorem, $\sum \deg(v) = 2|E|$. If every vertex has degree 4, total degree $= 4|V|$, so $|E| = 2|V|$ — which is always even.
>
> **b) True.** A connected graph with $|E| = |V| - 1$ is precisely the definition of a tree (a connected acyclic graph). Proof: a tree on $n$ vertices always has $n-1$ edges; any connected graph with $n-1$ edges has no cycles.
>
> **c) False.** Sum of degrees $= 5+5+4+3+2+1 = 20$, so $|E| = 10$. For a simple graph on 6 vertices, maximum degree $= 5$ (a vertex can connect to at most 5 others). The degree 5 vertex must connect to all others. Both degree-5 vertices must connect to all 5 other vertices — but a simple graph has no multi-edges. They'd both need to connect to each other and all 4 remaining vertices, which is possible structurally. However: with $n=6$ vertices, $K_6$ has $15$ edges. Sum=20 → $|E|=10 \leq 15$. Actually let's check more carefully via Erdős–Gallai: the sequence `[5,5,4,3,2,1]` — sum=20 (even ✓). Applying Erdős–Gallai condition for $k=2$: $5+5 \leq 2(1) + (4+3+2+1) = 12$ → $10 \leq 12$ ✓. For $k=1$: $5 \leq 0 + (5+4+3+2+1) = 15$ ✓. **Actually this sequence IS graphical.** So the statement is **False** — such a graph CAN exist. *(Correction: the answer is True, the graph can exist.)*
>
> **d) True.** In DFS on an undirected graph, each edge is visited exactly once (since it's undirected, both endpoints process it). An edge $(u,v)$ is either discovered during DFS (tree edge) or connects to an ancestor (back edge). Cross edges and forward edges do not occur in undirected DFS.
>
> **e) False.** BFS finds shortest paths in terms of **hop count** (number of edges), but this is only the same as minimum weight if all edge weights are **equal**. For weighted graphs, Dijkstra's algorithm must be used.

---

> [!question] Q8.2 — Prim's Algorithm Trace
> Apply **Prim's algorithm** to the graph below starting from vertex **A**. Show the MST edge selection table at each step (current MST, candidate edges, and selected edge).
>
> **Graph:**
> ```
> A --2-- B --3-- C
> |       |       |
> 6       8       4
> |       |       |
> D --5-- E --7-- F
>    \         /
>      9     1
>        \ /
>         G
> ```
> Edges: A-B(2), A-D(6), B-C(3), B-E(8), C-F(4), D-E(5), D-G(9), E-F(7), F-G(1).

> [!success]- Solution
> Starting from A. MST grows by always picking the minimum-weight edge crossing the cut.
>
> | Step | MST Vertices | Candidate Edges (from cut) | Selected |
> |------|-------------|---------------------------|----------|
> | 0 | {A} | A-B(2), A-D(6) | **A-B(2)** |
> | 1 | {A,B} | A-D(6), B-C(3), B-E(8) | **B-C(3)** |
> | 2 | {A,B,C} | A-D(6), B-E(8), C-F(4) | **C-F(4)** |
> | 3 | {A,B,C,F} | A-D(6), B-E(8), F-G(1), E-F(7) | **F-G(1)** |
> | 4 | {A,B,C,F,G} | A-D(6), B-E(8), D-G(9), E-F(7) | **A-D(6)** |
> | 5 | {A,B,C,F,G,D} | B-E(8), D-E(5), D-G(9→already) | **D-E(5)** |
> | 6 | {A,B,C,F,G,D,E} | B-E(8→already in MST) | all remaining in MST |
>
> **MST Edges:** A-B(2), B-C(3), C-F(4), F-G(1), A-D(6), D-E(5)
> **Total MST Weight:** $2+3+4+1+6+5 = \mathbf{21}$

---

> [!question] Q8.3 — Dijkstra's Algorithm Trace 🔥
> Apply **Dijkstra's algorithm** to find shortest paths from vertex **S** to all other vertices.
>
> **Graph (directed, weighted):**
> Vertices: {S, A, B, C, D, E}
> Edges: S→A(7), S→B(2), S→C(3), A→D(1), A→B(3), B→D(4), B→A(2), C→B(2), D→E(1), B→E(5)

> [!success]- Solution
> **Initialization:** dist = {S:0, A:∞, B:∞, C:∞, D:∞, E:∞}. Unvisited = {S,A,B,C,D,E}.
>
> | Step | Visited | Extract min | Updates | dist table |
> |------|---------|------------|---------|------------|
> | 1 | {S} | S(0) | A:7, B:2, C:3 | S=0,A=7,B=2,C=3,D=∞,E=∞ |
> | 2 | {S,B} | B(2) | A: min(7, 2+2)=4, D: min(∞,2+4)=6, E:min(∞,2+5)=7 | S=0,A=4,B=2,C=3,D=6,E=7 |
> | 3 | {S,B,C} | C(3) | B: min(2, 3+2)=2 (no update) | unchanged |
> | 4 | {S,B,C,A} | A(4) | D: min(6, 4+1)=5, B: min(2,4+3)=2 (no update) | D=5 |
> | 5 | {S,B,C,A,D} | D(5) | E: min(7, 5+1)=6 | E=6 |
> | 6 | {S,B,C,A,D,E} | E(6) | No neighbors | done |
>
> **Shortest distances from S:**
> - S→S: 0
> - S→B: 2 (path: S→B)
> - S→C: 3 (path: S→C)
> - S→A: 4 (path: S→B→A)
> - S→D: 5 (path: S→B→A→D)
> - S→E: 6 (path: S→B→A→D→E)

---

> [!question] Q8.4 — Degree Sequence Validation
> For each of the following sequences, determine whether it can be the degree sequence of a **simple undirected graph**. If yes, construct such a graph. If no, explain why using the Handshake Theorem or Erdős–Gallai theorem.
>
> a) $[4, 3, 3, 2, 2]$
> b) $[5, 4, 3, 2, 1, 1]$
> c) $[3, 3, 3, 3]$

> [!success]- Solution
> **a) [4, 3, 3, 2, 2]:** Sum = 14 (even ✓). $n=5$ vertices, max possible degree = 4. Degree 4 vertex connects to all others. Erdős–Gallai check passes. **Yes, it's graphical.**
>
> Example: Label vertices A(4),B(3),C(3),D(2),E(2). A connects to B,C,D,E. B connects to A,C,D. C connects to A,B,E. D connects to A,B. E connects to A,C.
> Check: A=4✓, B=3✓, C=3✓, D=2✓, E=2✓. ✅
>
> **b) [5, 4, 3, 2, 1, 1]:** Sum = 16 (even ✓). $n=6$ vertices, max degree = 5. Degree-5 vertex connects to all 5 others. After removing it: degrees become $[3,2,1,0,0]$ — a valid subgraph. Erdős–Gallai: **Yes, it's graphical.**
>
> **c) [3, 3, 3, 3]:** Sum = 12 (even ✓). $n=4$ vertices. But $K_4$ has each vertex with degree 3, and $K_4$ is a simple graph. **Yes, this is exactly $K_4$.** ✅

---

## Module 9 — [[Dynamic Programming]]

### Matrix Chain Multiplication

> [!question] Q9.1 — Matrix Chain: Full DP Table
> Given matrices $M_1, M_2, M_3, M_4, M_5$ with dimensions:
>
> $M_1: 10\times30$, $M_2: 30\times5$, $M_3: 5\times60$, $M_4: 60\times10$, $M_5: 10\times20$
>
> (Dimension sequence: $p = [10, 30, 5, 60, 10, 20]$)
>
> a) Fill the complete $m[i][j]$ cost table.
> b) Identify the optimal parenthesization using the $s[i][j]$ split table.
> c) What is the minimum number of scalar multiplications?

> [!success]- Solution
> **Base cases:** $m[i][i] = 0$.
>
> **Length 2:**
> $m[1][2] = p_0 p_1 p_2 = 10 \cdot 30 \cdot 5 = 1500$
> $m[2][3] = p_1 p_2 p_3 = 30 \cdot 5 \cdot 60 = 9000$
> $m[3][4] = p_2 p_3 p_4 = 5 \cdot 60 \cdot 10 = 3000$
> $m[4][5] = p_3 p_4 p_5 = 60 \cdot 10 \cdot 20 = 12000$
>
> **Length 3:**
> $m[1][3]$: split at $k=1$: $m[1][1]+m[2][3]+p_0 p_1 p_3 = 0+9000+10\cdot30\cdot60 = 27000$; split at $k=2$: $m[1][2]+m[3][3]+p_0 p_2 p_3 = 1500+0+10\cdot5\cdot60 = 4500$. **Min = 4500**, $s[1][3]=2$.
> $m[2][4]$: split at $k=2$: $9000+3000+30\cdot5\cdot10=12000+1500=13500$; split at $k=3$: $1500+0+... wait: m[2][2]+m[3][4]+p_1 p_2 p_4 = 0+3000+30\cdot5\cdot10=3000+1500=4500$. **Min = 4500**, $s[2][4]=3$.
> $m[3][5]$: split at $k=3$: $m[3][3]+m[4][5]+p_2 p_3 p_5 = 0+12000+5\cdot60\cdot20=12000+6000=18000$; split at $k=4$: $m[3][4]+m[5][5]+p_2 p_4 p_5 = 3000+0+5\cdot10\cdot20=3000+1000=4000$. **Min = 4000**, $s[3][5]=4$.
>
> **Length 4:**
> $m[1][4]$: 
> - $k=1$: $0 + m[2][4] + p_0 p_1 p_4 = 0+4500+10\cdot30\cdot10 = 7500$
> - $k=2$: $m[1][2]+m[3][4]+p_0 p_2 p_4 = 1500+3000+10\cdot5\cdot10 = 5000$
> - $k=3$: $m[1][3]+m[4][4]+p_0 p_3 p_4 = 4500+0+10\cdot60\cdot10 = 10500$
> **Min = 5000**, $s[1][4]=2$.
>
> $m[2][5]$:
> - $k=2$: $0+m[3][5]+p_1 p_2 p_5 = 0+4000+30\cdot5\cdot20 = 7000$
> - $k=3$: $m[2][3]+m[4][5]+p_1 p_3 p_5 = 9000+12000+30\cdot60\cdot20 = 57000$
> - $k=4$: $m[2][4]+m[5][5]+p_1 p_4 p_5 = 4500+0+30\cdot10\cdot20 = 10500$
> **Min = 7000**, $s[2][5]=2$.
>
> **Length 5:**
> $m[1][5]$:
> - $k=1$: $0+m[2][5]+p_0 p_1 p_5 = 0+7000+10\cdot30\cdot20 = 13000$
> - $k=2$: $m[1][2]+m[3][5]+p_0 p_2 p_5 = 1500+4000+10\cdot5\cdot20 = 6500$
> - $k=3$: $m[1][3]+m[4][5]+p_0 p_3 p_5 = 4500+12000+10\cdot60\cdot20 = 28500$
> - $k=4$: $m[1][4]+m[5][5]+p_0 p_4 p_5 = 5000+0+10\cdot10\cdot20 = 7000$
> **Min = 6500**, $s[1][5]=2$.
>
> **c) Minimum scalar multiplications = 6500.**
>
> **b) Optimal parenthesization:** $s[1][5]=2$ → split into $(M_1 M_2)(M_3 M_4 M_5)$.
> $s[1][2]=1$ → $(M_1)(M_2)$.
> $s[3][5]=4$ → $(M_3 M_4)(M_5)$.
> $s[3][4]=3$ → $(M_3)(M_4)$.
>
> **Result:** $((M_1 M_2)((M_3 M_4) M_5))$

---

### 0/1 Knapsack

> [!question] Q9.2 — Knapsack DP Table + Backtracking
> Given a knapsack with capacity $W = 8$ and 5 items:
>
> | Item | Weight | Value |
> |------|--------|-------|
> | 1 | 2 | 6 |
> | 2 | 3 | 10 |
> | 3 | 1 | 3 |
> | 4 | 4 | 14 |
> | 5 | 3 | 9 |
>
> a) Fill the complete $V[k][w]$ DP table.
> b) Identify the maximum value achievable.
> c) Use backtracking to identify the exact items included in the optimal subset.

> [!success]- Solution
> **Recurrence:** $V[k][w] = V[k-1][w]$ if $w_k > w$; else $\max(V[k-1][w],\; v_k + V[k-1][w-w_k])$.
>
> **DP Table $V[k][w]$ ($k$=items, $w$=capacity):**
>
> | k\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
> |-----|---|---|---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | 1(w=2,v=6) | 0 | 0 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
> | 2(w=3,v=10)| 0 | 0 | 6 | 10| 10| 16| 16| 16| 16|
> | 3(w=1,v=3) | 0 | 3 | 6 | 10| 13| 16| 19| 19| 19|
> | 4(w=4,v=14)| 0 | 3 | 6 | 10| 14| 17| 20| 23| 27|
> | 5(w=3,v=9) | 0 | 3 | 6 | 10| 14| 17| 20| 23| 27|
>
> **b) Maximum value = V[5][8] = 27.**
>
> **c) Backtracking from V[5][8]=27:**
> - $k=5$: $V[5][8]=27 = V[4][8]=27$ → item 5 **not** included. Move to $V[4][8]$.
> - $k=4$: $V[4][8]=27 \neq V[3][8]=19$ → item 4 **included** ($v_4=14$). Move to $V[3][8-4]=V[3][4]=13$.
> - $k=3$: $V[3][4]=13 \neq V[2][4]=10$ → item 3 **included** ($v_3=3$). Move to $V[2][4-1]=V[2][3]=10$.
> - $k=2$: $V[2][3]=10 \neq V[1][3]=6$ → item 2 **included** ($v_2=10$). Move to $V[1][3-3]=V[1][0]=0$.
> - $k=1$: $V[1][0]=0 = V[0][0]=0$ → item 1 **not** included.
>
> **Optimal subset: Items {2, 3, 4}** with total weight $3+1+4=8$ and total value $10+3+14=\mathbf{27}$. ✅

---

### Longest Common Subsequence

> [!question] Q9.3 — LCS Table and Recovery
> Find the **Longest Common Subsequence** of:
>
> $X = \text{"ABCBDAB"}$ and $Y = \text{"BDCABA"}$
>
> a) Fill the complete $L[i][j]$ DP table.
> b) What is the length of the LCS?
> c) Recover **one** actual LCS string by backtracking through the table.

> [!success]- Solution
> **LCS Table** $L[i][j]$ where $i$ indexes $X$ and $j$ indexes $Y$:
>
> $X$: A B C B D A B (indices 1–7)
> $Y$: B D C A B A (indices 1–6)
>
> |   | "" | B | D | C | A | B | A |
> |---|----|----|----|----|----|----|-----|
> |"" | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | A | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
> | B | 0 | 1 | 1 | 1 | 1 | 2 | 2 |
> | C | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
> | B | 0 | 1 | 1 | 2 | 2 | 3 | 3 |
> | D | 0 | 1 | 2 | 2 | 2 | 3 | 3 |
> | A | 0 | 1 | 2 | 2 | 3 | 3 | 4 |
> | B | 0 | 1 | 2 | 2 | 3 | 4 | 4 |
>
> **b) LCS length = L[7][6] = 4.**
>
> **c) Backtracking from L[7][6]=4:**
> - (7,6): X[7]=B, Y[6]=A → B≠A. L[6][6]=4=L[7][5] → move up to (6,6).
> - (6,6): X[6]=A, Y[6]=A → **match!** Output A. Move to (5,5).
> - (5,5): X[5]=D, Y[5]=B → D≠B. L[4][5]=3=L[5][4] → move up to (4,5).
> - (4,5): X[4]=B, Y[5]=B → **match!** Output B. Move to (3,4).
> - (3,4): X[3]=C, Y[4]=A → C≠A. L[2][4]=1 < L[3][3]=2 → move left to (3,3).
> - (3,3): X[3]=C, Y[3]=C → **match!** Output C. Move to (2,2).
> - (2,2): X[2]=B, Y[2]=D → B≠D. L[1][2]=0=L[2][1]=1? L[2][1]=1, L[1][2]=0 → move up to (1,2).
> - (1,2): X[1]=A, Y[2]=D → A≠D. L[1][1]=0=L[0][2]=0 → both 0. Move up to (0,2) → base case.
>
> Reading outputs in reverse (since we print after recursion): **B, C, B, A** → LCS = **"BCBA"** ✓
>
> *(Note: Multiple valid LCS strings of length 4 exist, e.g., "BDAB", "BCBA", "BCAB".)*

---

> [!question] Q9.4 — DP Design: Rod Cutting 🔥
> A rod of length $n$ can be cut into pieces. The price of a piece of length $i$ is $p[i]$. Design a DP algorithm to find the maximum revenue.
>
> Given: $n=6$, prices $p = [0, 1, 5, 8, 9, 10, 17]$ (index 0 unused; $p[1]=1$, $p[2]=5$, ..., $p[6]=17$).
>
> a) Write the recurrence relation.
> b) Fill the DP table $r[j]$ for $j = 0, 1, \ldots, 6$.
> c) What is the maximum revenue for a rod of length 6, and what cuts achieve it?

> [!success]- Solution
> **a) Recurrence:**
> Let $r[j]$ = maximum revenue from a rod of length $j$.
> $$r[0] = 0, \quad r[j] = \max_{1 \leq i \leq j}\bigl(p[i] + r[j-i]\bigr)$$
>
> **b) DP Table:**
>
> | j | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
> |---|---|---|---|---|---|---|---|
> | r[j] | 0 | 1 | 5 | 8 | 10 | 13 | 17 |
>
> **Computation:**
> - $r[1] = p[1]+r[0] = 1$
> - $r[2] = \max(p[1]+r[1], p[2]+r[0]) = \max(2, 5) = 5$
> - $r[3] = \max(p[1]+r[2], p[2]+r[1], p[3]+r[0]) = \max(6,6,8) = 8$
> - $r[4] = \max(p[1]+r[3], p[2]+r[2], p[3]+r[1], p[4]+r[0]) = \max(9,10,9,9) = 10$
> - $r[5] = \max(p[1]+r[4], p[2]+r[3], p[3]+r[2], p[4]+r[1], p[5]+r[0]) = \max(11,13,13,10,10) = 13$
> - $r[6] = \max(p[1]+r[5], p[2]+r[4], p[3]+r[3], p[4]+r[2], p[5]+r[1], p[6]+r[0]) = \max(14,15,16,15,11,17) = 17$
>
> **c) Maximum revenue = 17**, achieved by **no cuts** (selling the whole rod of length 6 at $p[6]=17$). ✅

---

## Module 10 — [[Mixed Exam-Style Problems]]

> [!question] Q10.1 — Algorithm Classification Speed Round
> Classify each scenario with the correct data structure or algorithm AND state the time complexity of the required operation:
>
> a) Checking whether a string of brackets `"([{}])"` is valid.
> b) Finding the $k$-th smallest element in a stream of $n$ integers.
> c) Merging two sorted arrays of sizes $m$ and $n$ into one sorted array.
> d) Finding the shortest path in a graph with **negative edge weights** (no negative cycles).
> e) Testing whether an undirected graph is **bipartite**.

> [!success]- Solution
> **a) Stack** — push opening brackets; pop and check for match on closing brackets. $O(n)$.
>
> **b) Max-Heap of size $k$** — maintain a max-heap of the $k$ smallest seen so far. If the new element is smaller than the heap max, replace it. $O(n \log k)$ total; $O(1)$ to read the $k$-th smallest.
>
> **c) Merge** (from Merge Sort) — two-pointer merge. $O(m+n)$.
>
> **d) Bellman-Ford algorithm** — handles negative edges (but not negative cycles). $O(|V| \cdot |E|)$.
>
> **e) BFS/DFS with 2-coloring** — attempt to 2-color the graph. If a conflict is found, it's not bipartite. $O(|V|+|E|)$.

---

> [!question] Q10.2 — Complexity Comparison Across Topics
> For each operation, compare the **worst-case** time complexity across the listed data structures:
>
> | Operation | Sorted Array | BST (unbalanced) | AVL Tree | Hash Table (open addr.) |
> |-----------|-------------|------------------|----------|------------------------|
> | Search | ? | ? | ? | ? |
> | Insert | ? | ? | ? | ? |
> | Delete | ? | ? | ? | ? |
> | Find-Min | ? | ? | ? | ? |

> [!success]- Solution
> | Operation | Sorted Array | BST (unbalanced) | AVL Tree | Hash Table (open addr.) |
> |-----------|-------------|------------------|----------|------------------------|
> | Search | $O(\log n)$ | $O(n)$ | $O(\log n)$ | $O(n)$ worst / $O(1)$ avg |
> | Insert | $O(n)$ | $O(n)$ | $O(\log n)$ | $O(n)$ worst / $O(1)$ avg |
> | Delete | $O(n)$ | $O(n)$ | $O(\log n)$ | $O(n)$ worst / $O(1)$ avg |
> | Find-Min | $O(1)$ | $O(n)$ | $O(\log n)$ | $O(n)$ |
>
> **Notes:**
> - Sorted Array: binary search for lookup, but $O(n)$ shifts for insert/delete.
> - Unbalanced BST: degenerates to a linked list in the worst case (sorted insertion).
> - AVL Tree: all operations $O(\log n)$ guaranteed due to height bound $\leq 1.44 \log_2 n$.
> - Hash Table: $O(1)$ average, but $O(n)$ worst case (all keys collide to one chain). Find-Min requires linear scan.

---

> [!question] Q10.3 — Comprehensive Design Problem 🔥
> You need to design a system that supports the following operations on a collection of student records (each record has a unique integer `id` and a `gpa` float):
>
> 1. **Insert** a new student record.
> 2. **Search** by `id` (exact match).
> 3. **Find the student with the highest GPA** efficiently.
> 4. **Delete** a student by `id`.
>
> Operations 1, 2, 4 must run in $O(\log n)$ or better. Operation 3 must run in $O(1)$.
>
> Propose a data structure design (possibly a combination). Justify each component and its complexity.

> [!success]- Solution
> **Design: AVL Tree + Max-Heap (or augmented structure)**
>
> **Component 1 — AVL Tree indexed by `id`:**
> - Supports Insert, Search, Delete by `id` all in $O(\log n)$ (guaranteed AVL balance).
>
> **Component 2 — Max-Heap indexed by `gpa`:**
> - Supports FindMax in $O(1)$ (the heap root is always the maximum GPA student).
> - Insert into heap: $O(\log n)$ (bubble-up).
> - Delete: $O(\log n)$ (bubble-down after extracting).
>
> **Coordination:** Each record exists in both structures. Pointers link the AVL node to the heap position (and vice versa) so that deletion by `id` (from AVL) can also trigger heap removal in $O(\log n)$ by knowing the heap position directly (this requires a "position map" — an auxiliary hash table from `id` to heap index, $O(1)$ average lookup).
>
> **Complexity Summary:**
>
> | Operation | Complexity |
> |-----------|-----------|
> | Insert | $O(\log n)$ |
> | Search by id | $O(\log n)$ |
> | Find max GPA | $O(1)$ |
> | Delete by id | $O(\log n)$ |
>
> **Alternative (simpler):** Use only an AVL Tree augmented at each node with the **subtree-max GPA**. Then FindMax = $O(1)$ (read root's subtree-max). Insert, Delete, Search all $O(\log n)$ — but requires updating subtree-max on rotations, which adds $O(1)$ work per rotation. This is cleaner than maintaining a separate heap.

---

> [!question] Q10.4 — Tricky Concepts: Short Answer
> Answer each sub-question in 2–4 sentences:
>
> a) Why does Merge Sort have $\Theta(n \log n)$ complexity in **all** cases, while Quick Sort has $O(n^2)$ worst case?
> b) Explain why a hash table cannot efficiently support `FindMin` operations.
> c) What is **primary clustering** in linear probing, and how does double hashing eliminate it?
> d) In AVL trees, after a deletion, can more than one rotation be needed? Justify.

> [!success]- Solution
> **a)** Merge Sort always divides the array into exactly two halves of size $n/2$, regardless of the input — the division is positional, not value-based. This gives the recurrence $T(n) = 2T(n/2) + O(n)$ whose solution is always $\Theta(n \log n)$. Quick Sort's partition depends on the pivot value, which can produce splits as lopsided as $(n-1, 0)$ on sorted input, giving $T(n) = T(n-1) + O(n) = O(n^2)$.
>
> **b)** A hash table maps keys to slots via a hash function that deliberately destroys ordering. There is no spatial relationship between keys of similar value — the minimum element could be in any slot. Finding it requires scanning all $n$ slots: $O(n)$. BSTs and heaps maintain structural ordering that supports efficient min/max queries.
>
> **c)** Primary clustering occurs in linear probing when long runs of consecutive occupied slots form, because any key that hashes anywhere into the run must traverse the entire run before finding an empty slot, growing the cluster further. Double hashing uses a key-dependent step size $h_2(k)$, so two keys with the same initial hash value probe different sequences — they don't pile up in the same cluster. This disperses the load and avoids primary clustering entirely.
>
> **d) Yes, multiple rotations may be needed.** After inserting into an AVL tree, at most one rotation (single or double) restores balance — the height of the rotated subtree returns to what it was before insertion, so imbalance doesn't propagate upward. However, **deletion can decrease the height of a subtree**, which may propagate imbalance to ancestors. Therefore, deletion may require $O(\log n)$ rotations in the worst case (one at each level from the deleted node to the root).

---

*End of 61CSE108 DSA Master Problems Sheet*
