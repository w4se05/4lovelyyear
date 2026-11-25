---
tags: [61CSE108, search]
topic: "Lecture 3: Search"
course: "61CSE108: Algorithms and Data Structures"
---

# Search

> [!Note] 💡 Notation Conventions
> - $A[0..n-1]$: array of $n$ elements, 0-indexed.
> - $k$: the **search key** (target value).
> - $n$: the **problem size** (number of elements in the array).
> - $m$: number of occurrences of key $k$ in the array (used in randomized search).
> - Return value $-1$ (or equivalently $n$) signals "not found".

---

## 1. Overview

> [!Definition] 📖 Search Problem
> **Input:** An array $A$ of $n$ elements and a search key $k$.
> **Output:** The index $i$ such that $A[i] = k$, or $-1$ if $k$ does not exist in $A$.

Search is a fundamental operation needed in many scenarios: checking membership, looking up records by key (e.g. finding a student by ID), and as a subroutine in larger algorithms.

### Complexity Summary

| Algorithm | Best | Worst | Average | Extra Requirements |
|---|:---:|:---:|:---:|---|
| Linear search | $O(1)$ | $O(n)$ | $O(n)$ | None |
| Linear search with sentinel | $O(1)$ | $O(n)$ | $O(n)$ | One extra slot at end of array |
| Binary search | $O(1)$ | $O(\log_2 n)$ | $O(\log_2 n)$ | Array must be **sorted** beforehand |
| Randomized search | $O(1)$ | $O(n^{0.9})$ | $O(n/m)$ (probabilistic) | Probabilistic method; $m$ = occurrences of key |

---

## 2. Linear Search

> [!Definition] 📖 Linear Search
> Scan the array from left to right, comparing each element to $k$. Return the index on a match, or $-1$ after exhausting the array.

### Algorithm

```
LinearSearch(A, n, k):
    position ← -1
    for i ← 0 to n-1 do
        if A[i] = k then
            position ← i
            break
    return position
```

### Trace — array $[7,2,1,5,3,6,19,9]$, $k = 6$

| Step | $i$ | $A[i]$ | $A[i] = k$? |
|---|---|---|---|
| 1 | 0 | 7 | False |
| 2 | 1 | 2 | False |
| 3 | 2 | 1 | False |
| 4 | 3 | 5 | False |
| 5 | 4 | 3 | False |
| 6 | 5 | 6 | **True → return 5** |

### Complexity Analysis

> [!Property] ⚙️ Linear Search Complexity
> - **Best case $O(1)$:** $k$ is the first element ($k = A[0]$).
> - **Worst case $O(n)$:** $k$ is last, or absent — all $n$ elements inspected.
> - **Average case $O(n)$:** Assume $k$ is equally likely to be any element or absent. Each of $n+1$ outcomes has probability $\frac{1}{n+1}$:
> $$\mathbb{E}[T] = \sum_{i=1}^{n+1} i \cdot \Pr[k = A[i]] = \frac{1}{n+1} \sum_{i=1}^{n} i + 1 = \frac{n+3}{2} = O(n).$$

---

## 3. Linear Search with Sentinel

> [!Definition] 📖 Sentinel
> A **sentinel** is a dummy copy of the key $k$ placed at position $A[n]$ (one past the end). Its purpose is to **guarantee** the loop always terminates on a match, eliminating the separate boundary check `i < n` inside each iteration — reducing two checks per iteration to one.

### Algorithm

```
SentinelLinearSearch(A, n, k):
    A[n] ← k          // place sentinel at end (array has size n+1)
    i ← 0
    while A[i] ≠ k do
        i ← i + 1
    if i < n then
        return i       // found a real element
    return -1          // only found the sentinel → not in original array
```

> [!Warning] ⚠️ Extra Memory
> This algorithm requires the array to have **at least one extra slot** allocated beyond position $n-1$.

### Complexity Analysis

> [!Property] ⚙️ Sentinel Search Complexity
> - **Best / Worst / Average:** Same asymptotic classes as plain linear search — $O(1)$, $O(n)$, $O(n)$.
> - **Practical advantage:** In practice, approximately **25% faster** than plain linear search because each loop iteration performs only one comparison instead of two.

---

## 4. Binary Search

> [!Definition] 📖 Binary Search
> Exploits the fact that the array is **sorted** to eliminate half the remaining search space at each step. Compare $k$ with the middle element $A[\text{mid}]$:
> - If $A[\text{mid}] = k$: found, return $\text{mid}$.
> - If $k > A[\text{mid}]$: search the **right** half ($[\text{mid}+1, \text{right}]$).
> - If $k < A[\text{mid}]$: search the **left** half ($[\text{left}, \text{mid}-1]$).

### Algorithm (Recursive)

```
BinarySearch(A, left, right, k):
    if left > right then
        return -1
    mid ← (left + right) / 2
    if A[mid] = k then
        return mid
    if k > A[mid] then
        return BinarySearch(A, mid + 1, right, k)
    return BinarySearch(A, left, mid - 1, k)
```

### Algorithm (Iterative)

```
BinarySearch(A, n, k):
    result ← -1
    left ← 0
    right ← n - 1
    while left ≤ right do
        mid ← (left + right) / 2
        if A[mid] = k then
            result ← mid
            break
        if k > A[mid] then
            left ← mid + 1
        else
            right ← mid - 1
    return result
```

### Trace — sorted array $[1,2,3,5,6,7,9,19]$, $k = 6$

| Step | left | right | mid | $A[\text{mid}]$ | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 7 | 3 | 5 | $6 > 5$ → search right |
| 2 | 4 | 7 | 5 | 7 | $6 < 7$ → search left |
| 3 | 4 | 4 | 4 | 6 | **Match → return 4** |

### Complexity Analysis

> [!Property] ⚙️ Binary Search Complexity
> Each comparison halves the search space. Starting from $n$ elements, after $t$ steps at most $\lceil n/2^t \rceil$ elements remain. The search terminates when $\lceil n/2^t \rceil = 1$, i.e. $t = \lceil \log_2 n \rceil$.
> - **Best case $O(1)$:** $k$ is the middle element on the first comparison.
> - **Worst / Average case $O(\log_2 n)$:** at most $\lceil \log_2 n \rceil$ comparisons.
> - **Example:** with $10^9$ elements, binary search needs at most $\approx 30$ comparisons.

> [!Warning] ⚠️ Prerequisite
> The input array **must be sorted** before calling binary search. If the array is unsorted, results are incorrect.

---

## 5. Randomized Search

> [!Definition] 📖 Randomized Search
> Instead of scanning sequentially, **randomly sample** an index and check if it matches $k$. Repeat up to $n^{0.9}$ times before declaring "not found". This is a **probabilistic** (Las Vegas-style) algorithm.

### Algorithm

```
RandomizedSearch(A, n, k):
    i ← Random(0, n-1)
    count ← 0
    while count < n^0.9 do
        if A[i] = k then
            return i
        i ← Random(0, n-1)
        count ← count + 1
    return -1
```

> [!Note] 💡 Why use `Random()` even if it may repeat?
> Allowing repetition keeps each draw **independent and uniform**, which is required for the probabilistic analysis to hold. Tracking previously-visited indices would add overhead and complicate the algorithm.

### Complexity Analysis

> [!Property] ⚙️ Best and Worst Case
> - **Best $O(1)$:** Key found on the first random draw.
> - **Worst $O(n^{0.9})$:** Loop exhausts all $n^{0.9}$ tries without finding the key.

> [!Property] ⚙️ Average Case — Geometric Distribution
> Suppose there are $m$ copies of $k$ in the array ($m \geq 1$).
>
> **Step 1.** Probability of a single draw hitting $k$:
> $$p = \frac{m}{n}.$$
>
> **Step 2.** The number of draws until success follows a **geometric distribution**. Expected number of draws to find $k$:
> $$\mathbb{E}[\text{draws}] = \frac{1}{p} = \frac{n}{m} = O\!\left(\frac{n}{m}\right).$$
>
> **Step 3.** Probability that $k$ is **not** found after $\text{count}$ draws:
> $$(1-p)^{\text{count}} = \left(1 - \frac{m}{n}\right)^{\text{count}} \leq \exp\!\left(-\frac{m}{n} \cdot \text{count}\right).$$
>
> **Step 4.** Substituting $\text{count} = n^{0.9}$:
> $$(1-p)^{n^{0.9}} \leq \exp\!\left(-m \cdot n^{-0.1}\right).$$
>
> **Step 5.** Probability $k$ **is** found within $n^{0.9}$ draws is at least:
> $$1 - \exp(-m \cdot n^{-0.1}).$$
>
> **Numerical example:** $m = 1$, $n = 100$, $\text{count} = 63 \Rightarrow$ success probability $\geq 0.4$.

---

## 📘 Examples & Applications

### Example 1 — Linear Search Trace (Not Found)

> [!Example] 📘 Search for $k = 55$ in $[7,2,1,5,3,6,19,9]$
> **Using:** Linear search algorithm.
>
> **Step 1.** Initialise `position ← -1`.
> **Step 2.** Loop $i = 0$ to $7$: compare each $A[i]$ with $55$. None match.
> **Step 3.** Loop exits without break.
> **Step 4.** Return $-1$ (not found).

---

### Example 2 — Binary Search: Why Sorted Order Matters

> [!Example] 📘 Show binary search fails on unsorted input
> **Using:** Binary search algorithm, counterexample.
>
> Array $[7,2,1,5,3,6,19,9]$, $k = 2$.
>
> **Step 1.** $\text{mid} = 3$, $A[3] = 5$. Since $2 < 5$, search left: $[\text{left}=0, \text{right}=2]$.
> **Step 2.** $\text{mid} = 1$, $A[1] = 2$. Match — returns index $1$. (Lucky in this case.)
>
> Now search for $k = 3$:
> **Step 1.** $\text{mid} = 3$, $A[3] = 5$. Since $3 < 5$, search left: $[\text{left}=0, \text{right}=2]$.
> **Step 2.** $\text{mid} = 1$, $A[1] = 2$. Since $3 > 2$, search right: $[\text{left}=2, \text{right}=2]$.
> **Step 3.** $\text{mid} = 2$, $A[2] = 1$. Since $3 > 1$, search right: $[\text{left}=3, \text{right}=2]$.
> **Step 4.** $\text{left} > \text{right}$ → return $-1$. **Incorrect!** ($3$ is at index $4$.)

---

### Example 3 — Counting Average-Case Steps: Linear vs Binary

> [!Example] 📘 For $n = 10^9$, compare worst-case steps
> **Using:** Complexity results for linear and binary search.
>
> **Linear search worst case:** $10^9$ comparisons.
>
> **Binary search worst case:** $\lceil \log_2(10^9) \rceil = \lceil 29.9 \rceil = 30$ comparisons.
>
> Binary search needs roughly **33 million times fewer** comparisons in the worst case.

---

### Example 4 — Randomized Search: Probability Calculation

> [!Example] 📘 $m=1$, $n=100$: what is the success probability after 63 draws?
> **Using:** Average case analysis of randomized search.
>
> **Step 1.** $p = 1/100$.
>
> **Step 2.** Probability of failure after 63 draws:
> $$(1 - 0.01)^{63} = (0.99)^{63} \approx e^{-63 \times 0.01} = e^{-0.63} \approx 0.532.$$
>
> **Step 3.** Success probability $\approx 1 - 0.532 = 0.468 \geq 0.4$. $\checkmark$

---

### Exam-Style Combined Problem

> [!Example] 📘 Choose the right algorithm
> **Using:** All four search algorithms and their properties.
>
> For each scenario, state which algorithm is best and justify:
>
> **a)** Array of $10^6$ integers, unsorted, search performed once.
> → **Linear search.** No preprocessing cost; unsorted means binary search cannot be used; single query means randomized overhead not worth it.
>
> **b)** Array of $10^6$ integers, sorted, $10^5$ queries to answer.
> → **Binary search.** $O(\log n)$ per query vs $O(n)$ for linear; array already sorted.
>
> **c)** Array of $10^6$ integers, unsorted, $m = 500$ copies of key, single query.
> → **Randomized search.** Average cost $O(n/m) = O(2000)$, much better than $O(n) = O(10^6)$ in the average case.
>
> **d)** Array of size $8$ (tiny), unsorted.
> → **Linear search.** Constant difference; no benefit from complexity advantage of binary search at this scale.

---

## 🗂️ Summary

- The **search problem** finds the index of key $k$ in array $A$, returning $-1$ if absent.
- **Linear search** ($O(n)$ average/worst) scans left-to-right; no preprocessing required.
- **Sentinel linear search** is asymptotically identical to linear search but saves ~25% in practice by eliminating the boundary check inside the loop.
- **Binary search** achieves $O(\log_2 n)$ worst/average case but requires a **sorted** array. With $10^9$ elements, it needs at most 30 comparisons.
- **Randomized search** has $O(n^{0.9})$ worst case and $O(n/m)$ expected case (where $m$ is the number of key occurrences). Uses uniform random sampling with replacement; the geometric distribution governs its expected cost.
- When the array is unsorted and queries are few, prefer **linear** or **randomized** search. When the array is sorted and queries are many, prefer **binary search**.
