---
tags: [dsa, practice-problems, master-sheet, 61CSE108]
aliases: [DSA Problem Bank]
topic: "Master Problems Sheet — 61CSE108: Algorithms and Data Structures"
course: "61CSE108: Algorithms and Data Structures"
created: 2026-06-01
---
> [!info] How to Use This Sheet
> 
> Each module maps to one lecture. Questions emulate exact exam mechanics from past quizzes. **Solution blocks are foldable** — attempt first, then expand. Mermaid diagrams are embedded inside solutions for all tree, graph, and list problems.

---

## 📐 Module 1 — [[Complexity Analysis]]

### Asymptotic Notation

> [!question] Q: Big-Oh Membership — Prove or Disprove
> 
> For each expression, state whether the relationship holds and justify with a witness pair $(c, x_0)$ or a contradiction:
> 
> a) $g(n) = n^2$ — is $g(n) \in O(n^2)$?
> 
> b) $g(n) = n^2$ — is $g(n) \in O(n)$?
> 
> c) $g(n) = n^3$ — is $g(n) \in O(n^2)$?
> 
> d) $g(n) = \log_2 n$ — is $g(n) \in O(n)$?
> 
> e) $g(n) = (\log_4 n)^5$ — what is the tightest asymptotic class?

> [!success]- Solution
> 
> **a)** $n^2 \in O(n^2)$: choose $c = 1$, $x_0 = 1$. Then $n^2 \leq 1 \cdot n^2$ for all $n \geq 1$. ✓
> 
> **b)** $n^2 \notin O(n)$: Assume $n^2 \leq cn$ for some $c, x_0$. Then $n \leq c$ for all $n \geq x_0$, which fails as $n \to \infty$. Contradiction. ✗
> 
> **c)** $n^3 \notin O(n^2)$: Same argument — $n^3 \leq c \cdot n^2 \Rightarrow n \leq c$, impossible for all large $n$. ✗
> 
> **d)** $\log_2 n \in O(n)$: choose $c = 1$, $x_0 = 1$. Since $\log_2 n \leq n$ for all $n \geq 1$. ✓
> 
> **e)** $(\log_4 n)^5 = \left(\frac{\log_2 n}{\log_2 4}\right)^5 = \frac{(\log_2 n)^5}{2^5}$. This is $O((\log n)^5)$, i.e., **polylogarithmic** — faster than any polynomial but slower than linear.

---

> [!question] Q: Classify Three Functions by Loop Structure
> 
> Three functions compute $\sum_{i=1}^{n} i$:
> 
> - **F1:** Uses recursion — `F1(n) = n + F1(n-1)`, base `F1(0) = 0`.
>     
> - **F2:** Uses a single `for` loop from `i=1` to `n`, accumulating sum.
>     
> - **F3:** Uses two nested `for` loops, outer `i = 1..n`, inner `j = 1..i`, counting iterations.
>     
> 
> Determine the time complexity of F1, F2, and F3.

> [!success]- Solution
> 
> **F1 — Recursion:**
> 
> $T(n) = T(n-1) + O(1)$, with $T(0) = O(1)$.
> 
> Unrolling: $T(n) = n \cdot O(1) = O(n)$.
> 
> $$\boxed{O(n)}$$
> 
> **F2 — Single loop:**
> 
> Executes exactly $n$ iterations of one comparison and one addition each.
> 
> $$\boxed{O(n)}$$
> 
> **F3 — Double loop:**
> 
> Total iterations $= \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)$.
> 
> $$\boxed{O(n^2)}$$
> 
> > [!note] Exam note (from Quiz 1)
> > 
> > F1 was marked $O(n^w)$ — verify with professor whether this means $O(n)$ or the grader intended $O(n)$.

---

> [!question] Q: Limit-Based Classification
> 
> Using $L = \lim_{n \to \infty} \frac{f(n)}{g(n)}$, classify the relationship between each pair:
> 
> a) $f(n) = 3n^2 + 7n$, $g(n) = n^2$
> 
> b) $f(n) = n \log n$, $g(n) = n^2$
> 
> c) $f(n) = 2^n$, $g(n) = n^{100}$

> [!success]- Solution
> 
> **a)** $L = \lim \frac{3n^2 + 7n}{n^2} = 3 \in (0, \infty)$ → $f = \Theta(g)$, so $f \in O(n^2)$ and $f \in \Omega(n^2)$.
> 
> **b)** $L = \lim \frac{n \log n}{n^2} = \lim \frac{\log n}{n} = 0$ → $f = o(g)$, so $n \log n \in O(n^2)$ but $n \log n \notin \Omega(n^2)$.
> 
> **c)** $L = \lim \frac{2^n}{n^{100}} = \infty$ (exponential dominates polynomial) → $f = \omega(g)$, so $2^n \notin O(n^{100})$.

---

### Algorithm Analysis

> [!question] Q: Iterative Algorithm — Summation Method
> 
> Analyse the exact number of comparisons in the following pseudocode and express as a $\Theta$ bound:
> 
> ```
> count ← 0
> for i ← 1 to n do
>     for j ← i to n do
>         count ← count + 1
> ```

> [!success]- Solution
> 
> For each fixed $i$, the inner loop runs $(n - i + 1)$ times.
> 
> $$\text{Total} = \sum_{i=1}^{n}(n - i + 1) = \sum_{k=1}^{n} k = \frac{n(n+1)}{2} = \Theta(n^2)$$

---

## 🔍 Module 2 — [[Search Algorithms]]

### Linear Search

> [!question] Q: Linear Search — Average Case Derivation
> 
> Given an array $A[0..n-1]$ and key $k$, assume $k$ is equally likely to be any element or absent (probability $\frac{1}{n+1}$ each). Derive $\mathbb{E}[T]$.

> [!success]- Solution
> 
> If $k = A[i]$ (0-indexed, found at position $i+1$ in 1-indexed loop), it takes $i+1$ comparisons.
> 
> If absent, takes $n$ comparisons.
> 
> $$\mathbb{E}[T] = \frac{1}{n+1}\left(\sum_{i=1}^{n} i\right) + \frac{1}{n+1} \cdot n = \frac{1}{n+1} \cdot \frac{n(n+1)}{2} + \frac{n}{n+1} = \frac{n}{2} + \frac{n}{n+1} \approx \frac{n}{2} = O(n)$$

---

### Binary Search

> [!question] Q: Binary Search Trace — Descending Array
> 
> _(From Quiz 2)_ Given the **descending** integer array:
> 
> |**idx**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|
> |---|---|---|---|---|---|---|---|---|---|---|
> |val|95|85|77|74|63|51|40|32|11|5|
> 
> Using $\text{mid} = \lfloor\frac{\text{left}+\text{right}}{2}\rfloor$:
> 
> **a)** Which element(s) require the most steps to find? Justify.
> 
> **b)** How many iterations does it take to search for **38** (not present)?

> [!success]- Solution
> 
> > [!warning] Binary search requires a **sorted** array — this array is sorted **descending**, so comparisons are reversed: if $k < A[\text{mid}]$, search **right**; if $k > A[\text{mid}]$, search **left**.
> 
> **a) Most steps — trace all midpoints:**
> 
> Step 1: mid = 4, $A[4] = 63$
> 
> Step 2: mid = 1, $A[1] = 85$ (left half) or mid = 7, $A[7] = 32$ (right half)
> 
> Step 3: mid = 0, $A[0] = 95$; mid = 2, $A[2] = 77$; mid = 5, $A[5] = 51$; or mid = 8, $A[8] = 11$
> 
> Step 4: mid = 3, $A[3] = 74$; mid = 6, $A[6] = 40$; or mid = 9, $A[9] = 5$
> 
> Elements requiring **most steps (4 iterations)**: **74, 40, 5** — those found deepest in the binary search tree of this array.
> 
> **b) Search for 38 (not present):**
> 
> |**Step**|**left**|**right**|**mid**|**A[mid]**|**Decision**|
> |---|---|---|---|---|---|
> |1|0|9|4|63|38 < 63 → search right (descending)|
> |2|5|9|7|32|38 > 32 → search left|
> |3|5|6|5|51|38 < 51 → search right|
> |4|6|6|6|40|38 < 40 → search right|
> |5|7|6|—|left > right → **not found**||
> 
> **Answer: 4 iterations** (plus final check). _(Quiz 2 answer: 4 iterations.)_

---

> [!question] Q: Binary Search Worst-Case Steps
> 
> For a sorted array of **32 elements**, what is the maximum number of comparisons Binary Search needs to conclude a key is **not present**?
> 
> A. 32    B. 16    C. 6    D. 5

> [!success]- Solution
> 
> Binary search halves the search space each step. Worst case: $\lceil \log_2 32 \rceil = \lceil 5 \rceil = 5$ comparisons.
> 
> But if the algorithm checks for equality AND direction each step, it uses **1 comparison per step** and terminates after $\lceil \log_2(n+1) \rceil$ steps.
> 
> For $n=32$: $\lceil \log_2 33 \rceil = 6$.
> 
> **Answer: C — 6**
> 
> > [!note] This matches Quiz 3 Q10: answer (C) 6. The key is "maximum steps to determine NOT present" counts the final failed boundary check.

---

> [!question] Q: Randomized Search — Probability Calculation
> 
> An array has $n = 100$ elements and $m = 1$ copy of key $k$. After 63 random draws (with replacement), what is the probability that $k$ has been found?

> [!success]- Solution
> 
> $p = \frac{m}{n} = \frac{1}{100} = 0.01$
> 
> Probability of failure after 63 draws:
> 
> $$(1 - 0.01)^{63} = (0.99)^{63} \approx e^{-63 \times 0.01} = e^{-0.63} \approx 0.532$$
> 
> **Success probability** $\approx 1 - 0.532 = \mathbf{0.468} \geq 0.4$ ✓

---

## 🔢 Module 3 — [[Sorting Algorithms]]

### Selection / Insertion Sort

> [!question] Q: Insertion Sort Trace
> 
> Trace Insertion Sort on array $A = [5, 3, 8, 1, 9, 2]$. Show the array state after each outer-loop iteration and count the total number of element shifts (not comparisons).

> [!success]- Solution
> 
> |**i**|**key**|**Shifts**|**Array after**|
> |---|---|---|---|
> |1|3|1|$[3,5,8,1,9,2]$|
> |2|8|0|$[3,5,8,1,9,2]$|
> |3|1|3|$[1,3,5,8,9,2]$|
> |4|9|0|$[1,3,5,8,9,2]$|
> |5|2|4|$[1,2,3,5,8,9]$|
> 
> **Total shifts = 1 + 0 + 3 + 0 + 4 = 8**

---

### Heap Sort

> [!question] Q: Heap Construction — Build Max-Heap
> 
> _(From Quiz 2)_ Given array (0-indexed): $[1, 30, 3, 12, 53, 62, 14, 32, 41, 49]$
> 
> **a)** Apply the `HeapConstruction` algorithm to build a max-heap. Show the resulting max-heap array.
> 
> **b)** Propose an algorithm to check whether a given array of $n$ elements is a max-heap. What is its time complexity?
> 
> **c)** Starting from your max-heap, demonstrate Heap Sort steps until the last 3 elements are 49, 53, 62 respectively.

> [!success]- Solution
> 
> **a) Build max-heap** — call `Heapify` from index $\lfloor 10/2 \rfloor - 1 = 4$ down to $0$:
> 
> Initial: $[1, 30, 3, 12, 53, 62, 14, 32, 41, 49]$
> 
> Heapify(4): node=53, left=idx9=49. 53>49, no swap. $[1, 30, 3, 12, 53, 62, 14, 32, 41, 49]$
> 
> Heapify(3): node=12, left=idx7=32, right=idx8=41. 41>12 → swap(3,8): $[1, 30, 3, 41, 53, 62, 14, 32, 12, 49]$
> 
> Heapify(2): node=3, left=idx5=62, right=idx6=14. 62>3 → swap(2,5): $[1, 30, 62, 41, 53, 3, 14, 32, 12, 49]$
> 
> Heapify(1): node=30, left=idx3=41, right=idx4=53. 53>30 → swap(1,4): $[1, 53, 62, 41, 30, 3, 14, 32, 12, 49]$. Then cascade to heapify(4): node=30, left=idx9=49. 49>30 → swap(4,9): $[1, 53, 62, 41, 49, 3, 14, 32, 12, 30]$.
> 
> Heapify(0): node=1, left=53, right=62. 62>1 → swap(0,2): $[62, 53, 1, 41, 49, 3, 14, 32, 12, 30]$. Then cascade to heapify(2): node=1, left=idx5=3, right=idx6=14. 14>1 → swap(2,6): $[62, 53, 14, 41, 49, 3, 1, 32, 12, 30]$. Cascade to heapify(6): no children.
> 
> **Result: $[62, 53, 14, 41, 49, 3, 1, 32, 12, 30]$** >
> 
> Đoạn mã
> 
> ```
> graph TD
>     62 --> 53
>     62 --> 14
>     53 --> 41
>     53 --> 49
>     14 --> 3
>     14 --> 1
>     41 --> 32
>     41 --> 12
>     49 --> 30
> ```
> 
> **b) Max-Heap Check Algorithm:**
> 
> ```
> IsMaxHeap(A, n):
>   for i = 0 to floor(n/2) - 1:
>     if left child (2i+1) < n and A[i] < A[2i+1]: return False
>     if right child (2i+2) < n and A[i] < A[2i+2]: return False
>   return True
> ```
> 
> **Time complexity: $O(n)$** — visits each non-leaf node exactly once.
> 
> **c) Heap Sort until last 3 = [49, 53, 62]:**
> 
> Extract-max swaps root with last, then heapifies:
> 
> - Swap A[0]↔A[9]: $[30, 53, 14, 41, 49, 3, 1, 32, 12, \mathbf{62}]$ → heapify(0,9) → $[53, 49, 14, 41, 30, 3, 1, 32, 12, \mathbf{62}]$
>     
> - Swap A[0]↔A[8]: $[12, 49, 14, 41, 30, 3, 1, 32, \mathbf{53}, \mathbf{62}]$ → heapify(0,8) → $[49, 41, 14, 32, 30, 3, 1, 12, \mathbf{53}, \mathbf{62}]$
>     
> - Swap A[0]↔A[7]: $[12, 41, 14, 32, 30, 3, 1, \mathbf{49}, \mathbf{53}, \mathbf{62}]$ → after heapify last 3 are $[..., \mathbf{49, 53, 62}]$ ✓
>     

---

### Quick Sort

> [!question] Q: Quick Sort — Median-of-Three Pivot & Partition
> 
> _(From Quiz 2)_ Given array (0-indexed): $[1, 30, 3, 12, 53, 62, 14, 32, 41, 49]$
> 
> **a)** What is the pivot when using **median-of-three** selection (first, middle, last)?
> 
> **b)** Assume 49 is chosen as the pivot. Show the array after the **first partition**.

> [!success]- Solution
> 
> **a) Median-of-three:**
> 
> - First = $A[0] = 1$, Middle = $A[4] = 53$, Last = $A[9] = 49$
>     
> - Sorted: $\{1, 49, 53\}$ → median = **49**
>     
> 
> **b) Partition with pivot = 49:**
> 
> Elements $< 49$: 1, 30, 3, 12, 14, 32, 41 → stay left
> 
> Elements $> 49$: 53, 62 → move right
> 
> Pivot 49 sits in the middle.
> 
> **Result:** $[1, 30, 3, 12, 14, 32, 41, \mathbf{49}, 53, 62]$
> 
> > [!note] The exact final left-partition order depends on the two-pointer implementation. The key invariant: all elements left of 49 are <49, all right are >49.

---

### Merge Sort

> [!question] Q: Merge — Counting Iterations
> 
> _(From Quiz 2)_ Arrays $A = [1,2,3,5,8,13,21]$ and $B = [4,9,15,16,25,36]$. Starting indices $i=0$ (for A) and $j=0$ (for B).
> 
> What are the values of $i$ and $j$ just after the merged array $C$ gets its **7th element**?

> [!success]- Solution
> 
> Merge trace (pick smaller of $A[i]$ vs $B[j]$ at each step):
> 
> |**Step**|**A[i]**|**B[j]**|**Pick**|**C so far**|**i**|**j**|
> |---|---|---|---|---|---|---|
> |1|1|4|1 (A)|[1]|1|0|
> |2|2|4|2 (A)|[1,2]|2|0|
> |3|3|4|3 (A)|[1,2,3]|3|0|
> |4|5|4|4 (B)|[1,2,3,4]|3|1|
> |5|5|9|5 (A)|[1,2,3,4,5]|4|1|
> |6|8|9|8 (A)|[1,2,3,4,5,8]|5|1|
> |7|13|9|9 (B)|[1,2,3,4,5,8,9]|5|2|
> 
> **After 7th element: $i = 5$, $j = 2$** ✓ _(matches Quiz 2 answer)_

---

> [!question] Q: Sorting Properties — Multiple Choice
> 
> Answer True/False and justify:
> 
> a) Merge Sort is in-place.
> 
> b) Quick Sort is always $O(n \log n)$.
> 
> c) Insertion Sort is stable.
> 
> d) Heap Sort is stable.
> 
> e) Selection Sort's time is input-independent.

> [!success]- Solution
> 
> |**#**|**Answer**|**Reason**|
> |---|---|---|
> |a|**False**|Merge Sort uses $O(n)$ auxiliary array for `temp`|
> |b|**False**|Worst case is $O(n^2)$ (e.g., already-sorted input with bad pivot choice)|
> |c|**True**|Shifts only elements strictly greater than `key`, preserving order of equals|
> |d|**False**|Heap operations break relative order of equal elements|
> |e|**True**|`FindMin` always scans $n-i$ elements regardless of input|

---

## 📦 Module 4 — [[Stack and Queue]]

### Conceptual Questions

> [!question] Q: Stack vs Queue — MCQ Battery
> 
> _(From Quiz 3)_ Answer each:
> 
> 1. Why is it necessary to maintain both a **head** and a **tail** pointer in a linked-list Queue?
>     
> 2. Why is deleting the **last node** of a Singly Linked List inefficient even with a tail pointer?
>     
> 3. What is the main disadvantage of implementing a Stack using a **static array** vs. a linked list?
>     
> 4. In a Queue, which operation goes at the **Front** and which at the **Rear**?
>     
> 5. Why is Binary Search generally impossible on a standard Singly Linked List?
>     
> 6. What happens when you `pop` from an **empty stack**?
>     
> 7. Which data structure follows the **LIFO** principle?
>     
> 8. In a linked-list Stack, where is `push` most efficient?
>     

> [!success]- Solution
> 
> 1. **B** — To avoid traversing the entire list when adding (enqueuing) a new item at the rear. Tail pointer gives $O(1)$ enqueue.
>     
> 2. **D** — Even with a tail pointer, to _delete_ the last node you must update the second-to-last node's `next` to `NULL`, which requires traversing the whole list ($O(n)$).
>     
> 3. **B** — Arrays suffer from **Stack Overflow** if the fixed capacity is exceeded; they cannot grow dynamically.
>     
> 4. **D** — Insert at **Rear** (enqueue), Remove from **Front** (dequeue). _(Note: Quiz 3 Q4 had B circled — that is incorrect; correct answer is D.)_
>     
> 5. **D** — We cannot jump to the middle index in $O(1)$; linked lists have no random access, making the halving step impossible.
>     
> 6. **C** — **Stack Underflow** error.
>     
> 7. **C** — **Stack** (Last-In-First-Out).
>     
> 8. **A** — Insert at the **head** — $O(1)$, no traversal needed.
>     

---

### Postfix Expression Evaluation

> [!question] Q: Postfix Evaluation — Stack Trace
> 
> _(From Quiz 3)_ Evaluate the postfix expression: `18 3 / 7 5 2 + * + 4 6 * - 9 +`
> 
> Show the stack state after each token and give the final value.

> [!success]- Solution
> 
> |**Token**|**Operation**|**Stack (bottom → top)**|
> |---|---|---|
> |18|push|[18]|
> |3|push|[18, 3]|
> |/|pop 3, pop 18; push 18/3=6|[6]|
> |7|push|[6, 7]|
> |5|push|[6, 7, 5]|
> |2|push|[6, 7, 5, 2]|
> |+|pop 2,5; push 7|[6, 7, 7]|
> |*|pop 7,7; push 49|[6, 49]|
> |+|pop 49,6; push 55|[55]|
> |4|push|[55, 4]|
> |6|push|[55, 4, 6]|
> |*|pop 6,4; push 24|[55, 24]|
> |-|pop 24,55; push 55-24=31|[31]|
> |9|push|[31, 9]|
> |+|pop 9,31; push 40|[40]|
> 
> **Infix:** $((18/3) + 7 \times (5+2)) - 4 \times 6 + 9$
> 
> **Value: 40** ✓ _(matches Quiz 3)_

---

### Linked List — Mid-Node Problem

> [!question] Q: Find Mid-Node of Singly Linked List
> 
> _(From Quiz 3 — 30 pts)_ Given the Node structure:
> 
> C++
> 
> ```
> struct Node { int value; Node* next; };
> ```
> 
> Implement `Node* findMidNode(Node* headRef)` that returns the middle node **without using extra memory** (no new lists or arrays). If two middle nodes exist, return the **second** one.
> 
> Examples:
> 
> - $1 \to 2 \to 3 \to 4 \to 5$: return node with value **3**
>     
> - $1 \to 2 \to 3 \to 4 \to 5 \to 6$: return node with value **4**
>     

> [!success]- Solution
> 
> **Algorithm:** Fast/Slow pointer (Floyd's tortoise-and-hare). `slow` advances 1 step, `fast` advances 2 steps. When `fast` reaches the end, `slow` is at the midpoint.
> 
> C++
> 
> ```
> Node* findMidNode(Node* headRef) {
>     if (headRef == nullptr) return nullptr;
>     Node* slow = headRef;
>     Node* fast = headRef;
>     while (fast != nullptr && fast->next != nullptr) {
>         slow = slow->next;
>         fast = fast->next->next;
>     }
>     return slow;
> }
> ```
> 
> **Trace for $[1,2,3,4,5,6]$:**
> 
> |**Step**|**slow**|**fast**|
> |---|---|---|
> |init|1|1|
> |1|2|3|
> |2|3|5|
> |3|4|null (fast->next->next goes past end)|
> 
> Returns node **4** ✓ (second of two midpoints)
> 
> **Complexity:** $O(n)$ time, $O(1)$ space.

---

## 🔗 Module 5 — [[Linked Lists]]

> [!question] Q: Linked List Operations — Conceptual Tradeoffs
> 
> Answer True/False and justify:
> 
> a) Insertion at a known position in a Linked List is $O(1)$.
> 
> b) Searching for a value in an unsorted Singly Linked List is $O(\log n)$.
> 
> c) A Circular Doubly Linked List allows both forward and backward traversal.
> 
> d) Deleting the tail of a Singly Linked List with only a `pHead` pointer is $O(1)$.

> [!success]- Solution
> 
> |**#**|**Answer**|**Reason**|
> |---|---|---|
> |a|**True**|Once position (pointer) is known, re-link is 2 pointer updates|
> |b|**False**|No random access → must scan linearly → $O(n)$|
> |c|**True**|`pNext` for forward, `pPrev` for backward; circular means no null sentinels|
> |d|**False**|Must find the node before the tail to update its `next` → $O(n)$ traversal|

---

> [!question] Q: Singly Linked List Insertion — Trace
> 
> Given SLL: $10 \to 20 \to 30 \to 40 \to \text{NULL}$. Insert value **25** after node with value **20**. Write the pointer operations and draw the result.

> [!success]- Solution
> 
> ```
> newNode = Node(25)
> newNode->pNext = node20->pNext   // newNode->pNext = 30
> node20->pNext = newNode           // 20 now points to 25
> ```
> 
> Đoạn mã
> 
> ```
> graph LR
>     H[pHead] --> N10[10]
>     N10 --> N20[20]
>     N20 --> N25[25]
>     N25 --> N30[30]
>     N30 --> N40[40]
>     N40 --> NUL[NULL]
> ```

---

## 🗂️ Module 6 — [[Hashing]]

### Hash Table Construction

> [!question] Q: Hash Table — All Three Collision Methods
> 
> _(From Quiz 3 — Hashing)_ Hash table size $m = 13$, hash function $h(k) = k \bmod 13$.
> 
> Insert keys in order: **40, 31, 53, 44, 66, 77, 17, 90, 30, 102**.
> 
> Use three collision methods in sequence (each method's table is the input for the next question below):
> 
> - **Linear probing:** $h(k,i) = h(k) + i$
>     
> - **Quadratic probing:** $h(k,i) = h(k) + 2i^2 + 1$
>     
> - **Double hashing:** $h_2(k) = 7 - (k \bmod 7)$, $h(k,i) = h(k) + i \cdot h_2(k)$
>     

> [!success]- Solution
> 
> **Primary hashes:** $h(k) = k \bmod 13$
> 
> - 40→1, 31→5, 53→1(collision!), 44→5(collision!), 66→1(collision!), 77→12, 17→4, 90→12(collision!), 30→4(collision!), 102→11
>     
> 
> **Linear Probing** ($h(k,i)=h(k)+i$):
> 
> |**Slot**|**Key**|
> |---|---|
> |0|90|
> |1|40|
> |2|53|
> |3|66|
> |4|17|
> |5|31|
> |6|44|
> |7|30|
> |11|102|
> |12|77|
> 
> **Quadratic Probing** ($h(k,i)=h(k)+2i^2+1$; probe sequence at $i=0$: slot, $i=1$: slot+3, $i=2$: slot+9...):
> 
> |**Slot**|**Key**|
> |---|---|
> |0|30|
> |1|40|
> |2|90|
> |4|53|
> |5|31|
> |7|17|
> |8|44|
> |10|66|
> |11|102|
> |12|77|
> 
> **Double Hashing** ($h_2(k)=7-(k\bmod 7)$):
> 
> |**Slot**|**Key**|
> |---|---|
> |0|90|
> |1|40|
> |4|53|
> |5|31|
> |6|30|
> |8|17|
> |9|66|
> |10|44|
> |11|102|
> |12|77|

---

> [!question] Q: Hash Probe Counting
> 
> _(From Quiz 3)_ Using the tables built in the previous question, answer:
> 
> **b)** How many probes to **find** 31?
> 
> **c)** How many probes to **find** 17?
> 
> **d)** How many probes to **find** 28 (not in table)?
> 
> **f)** How many probes to **insert** 56?

> [!success]- Solution
> 
> Answers depend on the exact table state. Based on Quiz 3 answers:
> 
> |**Query**|**Linear**|**Quadratic**|**Double Hashing**|
> |---|---|---|---|
> |Find 31|1|1|1|
> |Find 17|1|2|2|
> |Find 28 (absent)|7|5|1|
> |Insert 56|5|6|4|
> 
> > [!note] For "find absent key": probe until an **empty slot** is reached (open addressing). Count of probes = number of occupied slots probed + 1 (the empty slot). Linear probing suffers clustering, making absent-key lookups expensive.

---

> [!question] Q: Hash Function Selection — Conceptual
> 
> Explain why using $p = 2^n$ as the table size with the division method $h(k) = k \bmod p$ is a **bad** choice.

> [!success]- Solution
> 
> With $p = 2^n$, $k \bmod 2^n$ extracts only the **last $n$ bits** of $k$. This means:
> 
> - Keys differing only in higher-order bits always collide.
>     
> - The hash function ignores most of the key's information.
>     
> - Clustering is severe if lower bits of keys follow a pattern.
>     
> 
> **Best practice:** Choose $p$ to be a **prime** not close to a power of 2 or 10. Good primes include 13, 17, 29, 37, 41, 53, 97, 127.

---

## 🌳 Module 7 — [[Trees]] and [[AVL Trees]]

### BST Traversals

> [!question] Q: BST Traversal — Preorder
> 
> _(From Quiz 5)_ Given the following BST:
> 
> ```
>         6
>        / \
>       3   9
>      / \   \
>     1   4   12
>      \   \   \
>       2   5   10
> ```
> 
> Perform a **preorder** traversal (Root → Left → Right) and write the sequence.

> [!success]- Solution
> 
> **Preorder (Root → Left → Right):**
> 
> $6 \to 3 \to 1 \to 2 \to 4 \to 5 \to 9 \to 12 \to 10$
> 
> Đoạn mã
> 
> ```
> graph TD
>     6 --> 3
>     6 --> 9
>     3 --> 1
>     3 --> 4
>     1 --> 2
>     4 --> 5
>     9 --> 12
>     12 --> 10
> ```
> 
> > [!warning] Quiz 5 answer written as "6, 3, 1, 4, 2, 5, 9, 12, 10" — note node 2 is right-child of 1, so preorder visits 1 before 2. Correct sequence: **6, 3, 1, 2, 4, 5, 9, 12, 10**.

---

> [!question] Q: Post-Order Traversal — Identify Unknown Nodes
> 
> _(From Quiz 5 — Problem 4)_ Given the tree below, post-order traversal yields: **15, 25, 20, 40, 35, 70, 60, 90, 85, 75, 50**.
> 
> ```
>            50
>           /   \
>          x1    x3
>         / \   / \
>        3  40 60  x4
>       /  /   \     \
>      20 25   70    90
>     /  \       \
>   15   x2      35
>                   \
>                   85
>                     \
>                     75
> ```
> 
> Find $x_1, x_2, x_3, x_4$.

> [!success]- Solution
> 
> Post-order = Left → Right → Root.
> 
> Reading the given sequence: 15, 25, 20, 40, **35**, 70, 60, 90, **85**, **75**, 50
> 
> - $x_1$ is parent of 3 and 40. Post-order processes 3's subtree (15,25,20) then 40's subtree (35,25→40). So $x_1 = \mathbf{20}$ — wait, 20 has children 15 and x2. From sequence: 15 before x2 before 20 → $x_2 = \mathbf{25}$.
>     
> - $x_1$ = root of left subtree with post-order ending at 40 → $x_1 = \mathbf{35}$.
>     
> - $x_3$ = root of right subtree, has 60 and x4. Post-order of right: 70,60,...,90,x4,x3. → $x_3 = \mathbf{75}$, $x_4 = \mathbf{85}$.
>     
> 
> **Answer: $x_1 = 35,\ x_2 = 25,\ x_3 = 75,\ x_4 = 85$** ✓ _(matches Quiz 5)_

---

### AVL Tree

> [!question] Q: BST → AVL Tree Conversion
> 
> _(From Quiz 5)_ Convert the following BST to an AVL tree. Identify the violation and the rotation type.
> 
> ```
>       10
>      /  \
>     5    20
>    / \   / \
>   2   7 15  25
>  /   /
> 1   12
>    /
>   0
> ```

> [!success]- Solution
> 
> **Step 1 — Compute balance factors** (height(left) - height(right)):
> 
> - Node 7: left subtree has node 12 with child 0 → height=2. Right: empty → height=-1. BF = 3 → **violation at node 7**.
>     
> 
> Wait — rechecking: 7's left child is 12, 12's left child is 0.
> 
> - height(12) = 1 (has child 0), height(right of 7) = -1 → BF(7) = 2. **Left-Left case.**
>     
> 
> **Step 2 — Right rotation at node 7:**
> 
> 12 becomes the new root of this subtree; 7 becomes 12's right child; 0 stays 12's left child.
> 
> **Step 3 — Resulting AVL tree (after propagating up):**
> 
> Đoạn mã
> 
> ```
> graph TD
>     10 --> 5
>     10 --> 20
>     5 --> 2
>     5 --> 12
>     2 --> 1
>     12 --> 7
>     12 --> 0
>     20 --> 15
>     20 --> 25
> ```
> 
> _(Exact result depends on full balance-factor propagation — check each ancestor.)_

---

> [!question] Q: AVL Tree — Delete and Rebalance
> 
> _(From Quiz 5 — Problem 3)_ Given the AVL tree:
> 
> ```
>        33
>       /  \
>      13   53
>     / \     \
>    9  21    61
>   / \
>  8  11
> ```
> 
> Delete node **33**. Show each step including the rotation performed.

> [!success]- Solution
> 
> **Step 1 — Delete node 33:**
> 
> Node 33 has two children. Use **inorder successor** (smallest in right subtree) = **53**.
> 
> Replace 33's value with 53, then delete node 53 from the right subtree.
> 
> After deletion: 61 becomes right child of 33's position.
> 
> **Intermediate tree:**
> 
> ```
>        53
>       /  \
>      13   61
>     / \
>    9  21
>   / \
>  8  11
> ```
> 
> **Step 2 — Check balance factors:**
> 
> - Node 53: height(left subtree rooted at 13) = 3, height(right=61) = 0. BF = 3. **Violation at 53.**
>     
> - Left child 13: BF = height(9's subtree=2) - height(21=0) = 2 → **Left-Left case** at 53.
>     
> 
> **Step 3 — Right rotation at 53:**
> 
> 13 becomes new root; 53 becomes 13's right child; 21 moves to 53's left child.
> 
> **Resulting AVL tree:**
> 
> Đoạn mã
> 
> ```
> graph TD
>     13 --> 9
>     13 --> 53
>     9 --> 8
>     9 --> 11
>     53 --> 21
>     53 --> 61
> ```
> 
> **Rotation type: Left-Left → Right Rotation at node 53** ✓ _(matches Quiz 5)_

---

> [!question] Q: AVL Tree Construction — Step by Step
> 
> _(From Quiz 5 — Problem 5)_ Construct an AVL tree by inserting the following sequence:
> 
> **10, 25, 35, 5, 8, 15, 17, 13, 12, 7, 13, 11, 40**
> 
> Write the resulting tree structure. You only need to draw the result **after each rotation**.

> [!success]- Solution
> 
> Insert sequence with rotations noted:
> 
> After 10, 25, 35: **Right-Right violation at 10** → Left rotation → root=25, 10 left, 35 right.
> 
> After inserting 5, 8: **Left-Right at 10** (5→8 inserted) → LR rotation at 10 → 8 between 5 and 10.
> 
> After 15, 17: Right-Right at 25's right subtree → rotate.
> 
> After 13: no rotation. After 12: Left-Right at 15 or 13 → rotate.
> 
> **Final AVL tree (from Quiz 5):**
> 
> Đoạn mã
> 
> ```
> graph TD
>     15 --> 10
>     15 --> 25
>     10 --> 7
>     10 --> 12
>     7 --> 5
>     12 --> 11
>     12 --> 13
>     25 --> 17
>     25 --> 35
>     35 --> 40
> ```
> 
> > [!note] Exact structure verified against Quiz 5 sketch. Insert 13 twice has no effect (duplicate keys handled by ignoring or placing right).

---

## 🕸️ Module 8 — [[Graphs]]

### Graph Properties

> [!question] Q: Handshake Theorem — Degree Sequences
> 
> _(From Quiz 6)_ For each sequence (given in decreasing order), determine if it **can** be the degree sequence of a simple graph. If yes, draw a valid graph; if no, explain why.
> 
> A. 6, 5, 4, 2, 1, 1, 1, 1
> 
> B. 7, 6, 5, 4, 3, 2, 1
> 
> C. 6, 6, 6, 6, 3, 3, 2, 2
> 
> D. 7, 6, 6, 4, 4, 3, 2, 2
> 
> E. 8, 7, 7, 6, 4, 2, 1, 1

> [!success]- Solution
> 
> **Handshake Theorem & Havel-Hakimi:**
> 
> |**Seq**|**Sum**|**Verdict**|**Reason**|
> |---|---|---|---|
> |A|21|**No**|Total degree must be **even** (= $2|
> |B|28|**No**|Has 7 vertices, but maximum possible degree in a simple graph of 7 vertices is 6. Contains a vertex of degree 7.|
> |C|34|**No**|Fails the Havel-Hakimi theorem. Cannot construct without multiple edges or loops.|
> |D|34|**Yes**|Has 8 vertices (max degree 7), sum is even, passes Havel-Hakimi.|
> |E|36|**No**|Has 8 vertices, but contains a vertex with degree 8 (which would require 9 vertices).|

---

> [!question] Q: Graph True/False — Properties
> 
> _(From Quiz 6)_ Given undirected graph $G(V,E)$, determine True or False:
> 
> a) If $G$ is connected, then $G$ can only be a tree if and only if $|V| = |E| + 1$.
> 
> b) DFS and BFS on $G$ take $O(|V| + |E|)$ in **adjacency matrix** representation.
> 
> c) If $G$ is a complete graph and $|E|$ is odd, then $|V|$ is also odd.

> [!success]- Solution
> 
> **a) True.** A connected graph is a tree iff it has no cycles, which is equivalent to $|E| = |V| - 1$. Each edge in a tree connects exactly one new vertex to the existing tree.
> 
> **b) False.** $O(|V|+|E|)$ is the complexity for **adjacency list**. With an adjacency matrix, checking all neighbors of a vertex takes $O(|V|)$, giving total complexity $O(|V|^2)$.
> 
> **c) False.** Complete graph $K_n$ has $|E| = \binom{n}{2} = \frac{n(n-1)}{2}$. For $|E|$ to be odd, $\frac{n(n-1)}{2}$ must be odd, which can happen for $n \equiv 2$ or $3 \pmod 4$ (even $|V|$). Counterexample: $K_3$: $|E|=3$ (odd), $|V|=3$ (odd) — true here. $K_4$: $|E|=6$ (even). So it's **not always true** — the parity of $|V|$ doesn't determine parity of $|E|$ universally. _(Quiz 6: False — "2 vertices create 1 edge → possible with even |V|.")_

---

### Minimum Spanning Tree (Prim's)

> [!question] Q: Prim's Algorithm — Full Trace
> 
> _(From Quiz 6 — Problem 3)_ Given the weighted undirected graph with 9 vertices (A, B, C, D, E, F, G, H, I) and the following edges (from the quiz diagram):
> 
> Key edges: C-B=7, C-D=10, A-B=8, B-I=10, B-F=20, A-H=6, H-I=5, H-G=5, G-F=5, F-I=25 (approx), F-E=7, E-D=8, D-B=18, B-x=8 (approx)
> 
> Starting from vertex **F**, run Prim's algorithm. List the edges added to the MST in order and give the total weight.

> [!success]- Solution
> 
> _(Based on Quiz 6 solution — x=8 means edge with weight 8)_
> 
> **Prim's from F:**
> 
> |**Step**|**Edge Added**|**Weight**|**Reason**|
> |---|---|---|---|
> |1|(F, G)|5|Min edge from F|
> |2|(G, H)|5|Min edge from {F,G}|
> |3|(H, I)|5|Min from {F,G,H}|
> |4|(H, A)|6|Min from {F,G,H,I}|
> |5|(F, E)|7|Next min|
> |6|(E, D)|8|Next min|
> |7|(A, B)|8|Min to reach B|
> |8|(B, C)|7|Min to reach C|
> 
> **MST edges:** (F,G), (G,H), (H,I), (H,A), (F,E), (E,D), (A,B), (B,C)
> 
> **Total weight = 5+5+5+6+7+8+8+7 = 51** ✓ _(matches Quiz 6)_

---

### Dijkstra's Algorithm

> [!question] Q: Dijkstra — Unaffected Vertices Under Edge Weight Change
> 
> _(From Quiz 6)_ Using Dijkstra from vertex **A**, the path $A \to H \to I \to F \to E \to D$ has certain costs. If $x$ (weight of some edge) is a **positive integer**, which vertices have shortest paths to A that are **not affected** by $x$?

> [!success]- Solution
> 
> Run Dijkstra from A ignoring $x$ to find which shortest paths don't route through the $x$-weighted edge.
> 
> From the Quiz 6 solution: vertices **A, B, C, D, H, I, G** are not affected by $x$.
> 
> Only **F** and **E** are affected when $x$ becomes small enough that $A \to H \to I \to F$ and $A \to H \to I \to F \to E$ become cheaper than alternative paths through B and D.
> 
> **Not affected: {A, B, C, D, H, I, G}** ✓

---

## 🧮 Module 9 — [[Dynamic Programming]]

### Matrix Chain Multiplication

> [!question] Q: Matrix-Chain — Full Table Fill
> 
> Given 4 matrices with dimension sequence $p = [5, 4, 6, 2, 7]$ (i.e., $M_1: 5\times4$, $M_2: 4\times6$, $M_3: 6\times2$, $M_4: 2\times7$).
> 
> Fill the $m(i,j)$ table and $s(i,j)$ table. What is $m(1,4)$ and the optimal parenthesization?

> [!success]- Solution
> 
> **Base cases ($\ell=1$):** $m(i,i)=0$
> 
> **$\ell=2$:**
> 
> - $m(1,2) = 0+0+5\cdot4\cdot6 = 120$, $s(1,2)=1$
>     
> - $m(2,3) = 0+0+4\cdot6\cdot2 = 48$, $s(2,3)=2$
>     
> - $m(3,4) = 0+0+6\cdot2\cdot7 = 84$, $s(3,4)=3$
>     
> 
> **$\ell=3$:**
> 
> - $m(1,3)$: $k=1$: $0+48+5\cdot4\cdot2=88$; $k=2$: $120+0+5\cdot6\cdot2=180$ → $m(1,3)=88$, $s(1,3)=1$
>     
> - $m(2,4)$: $k=2$: $0+84+4\cdot6\cdot7=252$; $k=3$: $48+0+4\cdot2\cdot7=104$ → $m(2,4)=104$, $s(2,4)=3$
>     
> 
> **$\ell=4$:**
> 
> - $m(1,4)$: $k=1$: $0+104+5\cdot4\cdot7=244$; $k=2$: $120+84+5\cdot6\cdot7=414$; $k=3$: $88+0+5\cdot2\cdot7=158$ → $\mathbf{m(1,4)=158}$, $s(1,4)=3$
>     
> 
> **$m$ table:**
> 
> ||**1**|**2**|**3**|**4**|
> |---|---|---|---|---|
> |**1**|0|120|88|**158**|
> |**2**|—|0|48|104|
> |**3**|—|—|0|84|
> |**4**|—|—|—|0|
> 
> **Optimal parenthesization:** $s(1,4)=3$ → split $(M_1M_2M_3)(M_4)$. Then $s(1,3)=1$ → $(M_1)(M_2M_3)$.
> 
> **Result: $((M_1(M_2M_3))M_4)$** — cost 158 scalar multiplications.

---

### 0-1 Knapsack

> [!question] Q: 0-1 Knapsack — Full DP Table
> 
> 4 items: weights $[2, 3, 4, 5]$, values $[3, 4, 5, 6]$. Knapsack capacity $W = 8$.
> 
> Fill the $V(k, w)$ table and identify the optimal subset.

> [!success]- Solution
> 
> **Table $V(k,w)$** — rows = items 1–4, columns = capacity 0–8:
> 
> |**k\w**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|
> |---|---|---|---|---|---|---|---|---|---|
> |0|0|0|0|0|0|0|0|0|0|
> |1 (w=2,v=3)|0|0|3|3|3|3|3|3|3|
> |2 (w=3,v=4)|0|0|3|4|4|7|7|7|7|
> |3 (w=4,v=5)|0|0|3|4|5|7|8|9|9|
> |4 (w=5,v=6)|0|0|3|4|5|7|8|9|**10**|
> 
> **$V(4,8) = 10$**
> 
> **Backtrack:**
> 
> - $V(4,8)=10 \neq V(3,8)=9$ → item 4 included. Remaining $w=8-5=3$.
>     
> - $V(3,3)=4 \neq V(2,3)=4$... equal → item 3 not included. Stay at $w=3$.
>     
> - $V(2,3)=4 \neq V(1,3)=3$ → item 2 included. Remaining $w=3-3=0$.
>     
> - $w=0$, stop.
>     
> 
> **Optimal subset: {item 2 (w=3,v=4), item 4 (w=5,v=6)}** — total weight=8, total value=**10**.

---

### Longest Common Subsequence

> [!question] Q: LCS — Full Table and Backtrack
> 
> Given $X = \text{"ABCBDAB"}$ ($m=7$) and $Y = \text{"BDCABA"}$ ($n=6$). Fill the $L(i,j)$ table and find the LCS.

> [!success]- Solution
> 
> **$L(i,j)$ table** (rows = X chars, cols = Y chars):
> 
> ||**∅**|**B**|**D**|**C**|**A**|**B**|**A**|
> |---|---|---|---|---|---|---|---|
> |∅|0|0|0|0|0|0|0|
> |A|0|0|0|0|1|1|1|
> |B|0|1|1|1|1|2|2|
> |C|0|1|1|2|2|2|2|
> |B|0|1|1|2|2|3|3|
> |D|0|1|2|2|2|3|3|
> |A|0|1|2|2|3|3|4|
> |B|0|1|2|2|3|4|4|
> 
> **LCS length = 4**
> 
> **Backtrack from $L(7,6)=4$:**
> 
> Matching characters at diagonal moves: B(i=7,j=5), A(i=6,j=4), D(i=5,j=2)... → one valid LCS is **"BCBA"** or **"BDAB"**.
> 
> **One valid LCS: "BDAB"** (length 4)

---

> [!question] Q: DP Problem Identification
> 
> For each problem, state whether it has (a) optimal substructure, (b) overlapping subproblems, and whether DP is appropriate:
> 
> 1. Finding the shortest path in a DAG.
>     
> 2. Counting the number of ways to make change for $n$ cents.
>     
> 3. Sorting an array using Merge Sort.
>     

> [!success]- Solution
> 
> |**Problem**|**Optimal Substructure**|**Overlapping Subproblems**|**Use DP?**|
> |---|---|---|---|
> |Shortest path in DAG|✓|✓ (same sub-paths reused)|**Yes**|
> |Coin change|✓|✓ (same amounts recomputed)|**Yes**|
> |Merge Sort|✓|✗ (subproblems are disjoint)|No — D&C preferred|

---

## ⚡ Module 10 — Mixed / Exam-Style

> [!question] Q: Choose the Right Data Structure
> 
> For each scenario, identify the best data structure and justify in one sentence:
> 
> a) You need $O(1)$ average search, insert, delete but $O(n)$ find-min is acceptable.
> 
> b) You need $O(\log n)$ for all of: search, insert, delete, find-min.
> 
> c) You need $O(1)$ push and pop with LIFO access.
> 
> d) You process tasks in order of arrival, $O(1)$ enqueue and dequeue.
> 
> e) You need to repeatedly extract the maximum element efficiently.

> [!success]- Solution
> 
> |**Scenario**|**Best Structure**|**Reason**|
> |---|---|---|
> |a|**Hash table**|$O(1)$ avg for search/insert/delete; unordered|
> |b|**Balanced BST (AVL)**|All $O(\log n)$ guaranteed|
> |c|**Stack (array or LL)**|LIFO, $O(1)$ push/pop|
> |d|**Queue**|FIFO, $O(1)$ enqueue at rear, dequeue at front|
> |e|**Max-Heap**|$O(\log n)$ extract-max, $O(1)$ find-max|

---

> [!question] Q: Complexity Comparison — All Structures
> 
> Complete the table with average-case complexity for each operation:
> 
> |**Structure**|**Search**|**Insert**|**Delete**|**Find-min**|
> |---|---|---|---|---|
> |Unsorted array|?|?|?|?|
> |Sorted array|?|?|?|?|
> |Singly linked list|?|?|?|?|
> |Hash table|?|?|?|?|
> |Balanced BST (AVL)|?|?|?|?|

> [!success]- Solution
> 
> |**Structure**|**Search**|**Insert**|**Delete**|**Find-min**|
> |---|---|---|---|---|
> |Unsorted array|$O(n)$|$O(1)$|$O(n)$|$O(n)$|
> |Sorted array|$O(\log n)$|$O(n)$|$O(n)$|$O(1)$|
> |Singly linked list|$O(n)$|$O(1)$|$O(1)$*|$O(n)$|
> |Hash table|$O(1)$|$O(1)$|$O(1)$|$O(n)$|
> |Balanced BST (AVL)|$O(\log n)$|$O(\log n)$|$O(\log n)$|$O(\log n)$|
> 
> *Linked list delete: $O(1)$ if pointer to node is given; $O(n)$ if only value is given (must find node first).

---

> [!question] Q: Algorithm Design — When to Use Which Sort
> 
> Select the best sorting algorithm for each scenario and justify:
> 
> a) $n = 10^6$ integers, nearly sorted (at most $k$ positions out of place, $k \ll n$).
> 
> b) $n = 10^6$ integers, need stable sort, no extra memory available.
> 
> c) $n = 10^6$ integers, $d$-digit numbers in base $k$, need $O(n)$ sort.
> 
> d) $n = 10^6$ integers, average performance critical, willing to accept rare $O(n^2)$ worst case.

> [!success]- Solution
> 
> |**Scenario**|**Algorithm**|**Reason**|
> |---|---|---|
> |a|**Insertion Sort**|$O(nk)$ for nearly-sorted input; each element moves at most $k$ positions|
> |b|**Merge Sort**|Stable + $O(n \log n)$ but requires $O(n)$ extra — _if no extra memory strictly_: no in-place stable sort achieves $O(n \log n)$|
> |c|**Radix Sort**|$O(d(n+k))$ — linear when $d$ and $k$ are constants|
> |d|**Quick Sort**|$O(n \log n)$ average with low constant; worst case $O(n^2)$ rare with randomized pivot|

---

> [!question] Q: Euler vs Hamiltonian — Conditions
> 
> For each graph description, determine if an **Euler circuit**, **Euler trail**, **Hamiltonian circuit**, or **none** exists:
> 
> a) Graph where all vertices have even degree and it's connected.
> 
> b) Graph where exactly 2 vertices have odd degree, all others even, connected.
> 
> c) $K_5$ (complete graph on 5 vertices).
> 
> d) A path graph $P_n$ (a simple chain of $n$ vertices).

> [!success]- Solution
> 
> |**Graph**|**Euler Circuit**|**Euler Trail**|**Hamiltonian Circuit**|
> |---|---|---|---|
> |a (all even, connected)|**Yes** (Thm 1.4)|Yes (trivially, EC is also a trail)|Depends on structure|
> |b (exactly 2 odd, connected)|**No**|**Yes** (trail between the 2 odd-degree vertices)|Depends|
> |$K_5$ (all deg=4, even)|**Yes**|Yes|**Yes** (visit each vertex once)|
> |$P_n$ (chain)|No (end vertices have deg=1, odd)|**Yes** (trail from one end to the other)|No (open chain, can't return)|