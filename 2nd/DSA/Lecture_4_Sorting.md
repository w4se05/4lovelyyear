---
tags: [61CSE108, sorting]
topic: "Lecture 4: Sorting"
course: "61CSE108: Algorithms and Data Structures"
---

# Sorting

> [!Note] 💡 Notation Conventions
> - $A[0..n-1]$: array of $n$ elements, 0-indexed.
> - **In-place:** uses only $O(1)$ or $O(\log n)$ extra memory beyond the input array.
> - **Stable:** equal elements preserve their original relative order after sorting.
> - **Det.:** deterministic — same input always produces same output.
> - **Rnd.:** randomized — output may vary due to random choices.
> - $d$: number of digits per element (Radix Sort).
> - $k$: digit range, i.e. base (Radix Sort).

---

## Sorting Summary Table

| Algorithm | Design | Run Time (avg) | In-place | Stable |
|---|:---:|:---:|:---:|:---:|
| Selection Sort | Det. | $O(n^2)$ | Yes | No |
| Insertion Sort | Det. | $O(n^2)$ | Yes | Yes |
| Heap Sort | Det. | $O(n \log n)$ | Yes | No |
| Merge Sort | Det. | $\Theta(n \log n)$ | No | Yes |
| Quick Sort | Rnd. | $O(n \log n)$ | Yes | No |
| Radix Sort | Det. | $O(d(n+k))$ | No | Yes |

> [!Definition] 📖 In-place Sorting
> A sorting algorithm is **in-place** if it sorts the array using only $O(1)$ or $O(\log n)$ extra space. It modifies the original array directly rather than allocating a separate data structure.

> [!Definition] 📖 Stable Sorting
> A sorting algorithm is **stable** if elements with equal keys maintain their original relative order after sorting.
> **Example:** sorting $[(3,A),(1,B),(4,C),(3,D),(2,E)]$ by the first component gives $[(1,B),(2,E),(3,A),(3,D),(4,C)]$ — note $(3,A)$ still precedes $(3,D)$.

---

## 1. Selection Sort

### Idea

> [!Definition] 📖 Selection Sort
> Maintain a sorted prefix $A[0..i-1]$ and an unsorted suffix $A[i..n-1]$. At each step:
> **1.** Find the index of the **minimum** element in the unsorted suffix $A[i..n-1]$.
> **2.** **Swap** that minimum with $A[i]$.
> **3.** Advance the boundary: $i \leftarrow i + 1$.
> **4.** Repeat until the entire array is sorted.

### Algorithm

```
SelectionSort(A, n):
    for i ← 0 to n-1 do
        min ← FindMin(A, i, n)
        Swap(A, i, min)

FindMin(A, low, n):
    min ← low
    for i ← low+1 to n-1 do
        if A[i] < A[min] then
            min ← i
    return min

Swap(A, i, j):
    tmp ← A[i]
    A[i] ← A[j]
    A[j] ← tmp
```

### Trace — $[7,2,1,5,3,6,19,9]$

| $i$ | Min found | Array after swap |
|---|---|---|
| 0 | $A[2]=1$ | $[1,2,7,5,3,6,19,9]$ |
| 1 | $A[1]=2$ | $[1,2,7,5,3,6,19,9]$ |
| 2 | $A[4]=3$ | $[1,2,3,5,7,6,19,9]$ |
| 3 | $A[3]=5$ | $[1,2,3,5,7,6,19,9]$ |
| 4 | $A[5]=6$ | $[1,2,3,5,6,7,19,9]$ |
| 5 | $A[5]=7$ | $[1,2,3,5,6,7,19,9]$ |
| 6 | $A[7]=9$ | $[1,2,3,5,6,7,9,19]$ |
| 7 | $A[7]=19$ | $[1,2,3,5,6,7,9,19]$ ✓ |

### Correctness

> [!Proof] 🔷 Correctness of Selection Sort (Loop Invariant)
> **Invariant:** At the start of iteration $i$, $A[0..i-1]$ is sorted and contains the $i$ smallest elements.
>
> **Initialization ($i=0$):** The prefix is empty — trivially sorted.
>
> **Maintenance:** `FindMin` returns the index of the minimum of $A[i..n-1]$. After `Swap`, $A[i]$ is the smallest element of the original $A[i..n-1]$, and $A[0..i]$ is sorted. The invariant holds for $i+1$.
>
> **Termination ($i=n$):** $A[0..n-1]$ is sorted. $\square$

### Complexity

> [!Property] ⚙️ Selection Sort Complexity
> At iteration $i$, `FindMin` scans $n-i$ elements, costing $\Theta(n-i)$ comparisons and assignments. Summing over all $n$ iterations:
>
> $$\text{Total cost} = \sum_{i=0}^{n-1} \Theta(n-i) = \sum_{j=1}^{n} \Theta(j) = \Theta\!\left(\frac{n(n+1)}{2}\right) = \Theta(n^2).$$
>
> More precisely:
> $$\geq \sum_{i=0}^{n-1} (3(n-i) + 3) = \Omega(n^2), \qquad \leq \sum_{i=0}^{n-1} (4(n-i) + 3) = O(n^2).$$
>
> Therefore the run time is $\Theta(n^2)$ in **all cases** (best, average, worst).

> [!Property] ⚙️ Pros and Cons
> - **Con:** Slow for large arrays — $O(n^2)$ regardless of input order.
> - **Pro:** Performance is **input-independent** — sorted and reverse-sorted arrays take the same time.

---

## 2. Insertion Sort

### Idea

> [!Definition] 📖 Insertion Sort
> Build a sorted prefix one element at a time, like sorting playing cards:
> **1.** Start with $A[0]$ as a sorted prefix of length 1.
> **2.** For each new element $A[i]$ (the **key**), shift all larger elements in the sorted prefix one position right.
> **3.** Insert the key in the correct position.
> **4.** Repeat until $i = n-1$.

### Algorithm

```
InsertionSort(A, n):
    for i ← 1 to n-1 do
        key ← A[i]
        j ← i - 1
        while j ≥ 0 and A[j] > key do
            A[j+1] ← A[j]
            j ← j - 1
        A[j+1] ← key
```

### Trace — $[7,2,1,5,3,6,19,9]$

| $i$ | key | Array after insertion |
|---|---|---|
| 1 | 2 | $[2,7,1,5,3,6,19,9]$ |
| 2 | 1 | $[1,2,7,5,3,6,19,9]$ |
| 3 | 5 | $[1,2,5,7,3,6,19,9]$ |
| 4 | 3 | $[1,2,3,5,7,6,19,9]$ |
| 5 | 6 | $[1,2,3,5,6,7,19,9]$ |
| 6 | 19 | $[1,2,3,5,6,7,19,9]$ |
| 7 | 9 | $[1,2,3,5,6,7,9,19]$ ✓ |

### Correctness

> [!Proof] 🔷 Correctness of Insertion Sort
> **Claim:** At the start of iteration $i$, $A[0..i-1]$ is sorted.
>
> Suppose the while loop stops at $j^*$. Then:
> **1.** Every element in $A[0..j^*]$ is $\leq$ key.
> **2.** Every element in $A[j^*+1..i-1]$ is $>$ key.
> The loop shifts $A[j^*+1..i-1]$ one position right. Then `A[j*+1] ← key` inserts the key in its correct position, making $A[0..i]$ sorted.
>
> When $i = n-1$, the whole array is sorted. $\square$

### Complexity

> [!Property] ⚙️ Insertion Sort Complexity
> - **Best case $O(n)$:** Array already sorted — the while loop never executes; only $n-1$ iterations of the outer for loop.
> - **Worst case $O(n^2)$:** Array in reverse order — at iteration $i$, the while loop runs $i$ times. Total:
> $$\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = O(n^2).$$
> - **Average case $O(n^2)$:** Each iteration $i$ contributes at most $4i - 1$ operations:
> $$\sum_{i=1}^{n-1} (4i-1) = O(n^2).$$

---

## 3. Heap Sort

### Heap: Definition and Properties

> [!Definition] 📖 Max-Heap
> A **max-heap** is a collection $(a_0, a_1, \ldots, a_{n-1})$ satisfying the **heap property**: for every $i$ with $0 \leq i \leq \lfloor n/2 \rfloor - 1$:
> $$a_i \geq a_{2i+1} \quad \text{and} \quad a_i \geq a_{2i+2} \quad (\text{if } 2i+2 < n).$$
> The root $a_0$ is the **maximum** element.

> [!Property] ⚙️ Array-Tree Correspondence
> A heap is stored as a linear array but viewed as a nearly-complete binary tree:
> - **Root:** $A[0]$
> - **Left child of $A[i]$:** $A[2i+1]$
> - **Right child of $A[i]$:** $A[2i+2]$
> - **Parent of $A[i]$:** $A[\lfloor(i-1)/2\rfloor]$
>
> Leaves occupy indices $\lfloor n/2 \rfloor$ through $n-1$ and are trivially max-heaps.

### Idea

> [!Definition] 📖 Heap Sort
> **Phase 1 — Build max-heap:** Convert the array into a max-heap by calling `Heapify` on each non-leaf node from right to left (indices $\lfloor n/2 \rfloor - 1$ down to $0$).
>
> **Phase 2 — Extract-sort:** Repeatedly swap the root (maximum) with the last element of the current heap, shrink the heap by 1, and restore the heap property by calling `Heapify` on the new root.

### Algorithm

```
HeapSort(A, n):
    // Phase 1: Build max-heap
    for i ← floor(n/2) - 1 downto 0 do
        Heapify(A, n, i)

    // Phase 2: Extract elements in sorted order
    for i ← n-1 downto 1 do
        Swap(A, 0, i)         // move current max to end
        Heapify(A, i, 0)      // restore heap on reduced array A[0..i-1]

Heapify(A, n, i):
    largest ← i
    left    ← 2*i + 1
    right   ← 2*i + 2
    if left < n and A[left] > A[largest] then
        largest ← left
    if right < n and A[right] > A[largest] then
        largest ← right
    if largest ≠ i then
        Swap(A, i, largest)
        Heapify(A, n, largest)    // recursively fix the affected subtree
```

### Heapify Trace — $[2,9,3,5]$, call `Heapify(A, 4, 0)`

```
Initial:    [2, 9, 3, 5]   largest = 0 (root = 2)
            left=1 (A[1]=9 > A[0]=2)  → largest = 1
            right=2 (A[2]=3 < A[1]=9) → largest stays 1
            Swap(A, 0, 1): [9, 2, 3, 5]
            Heapify(A, 4, 1):
                left=3 (A[3]=5 > A[1]=2) → largest = 3
                right=4 (out of range)
                Swap(A, 1, 3): [9, 5, 3, 2]
                Heapify(A, 4, 3):
                    left=7, right=8 (both out of range) → STOP
Result: [9, 5, 3, 2]  ✓ max-heap
```

### Correctness

> [!Proof] 🔷 Correctness of HeapSort — Build Phase (Loop Invariant)
> **Invariant:** At the start of each iteration $i$ of the build loop, every node $i+1, i+2, \ldots, n-1$ is the **root of a max-heap**.
>
> **Initialization:** Before the first iteration, $i = \lfloor n/2 \rfloor - 1$. Nodes $\lfloor n/2 \rfloor, \ldots, n-1$ are all leaves and trivially roots of max-heaps. ✓
>
> **Maintenance:** The children of node $i$ are both roots of max-heaps (by invariant). `Heapify(A, n, i)` makes node $i$ the root of a max-heap while preserving the invariant for higher-numbered nodes.
>
> **Termination ($i = -1$):** Every node is the root of a max-heap, so $A[0]$ is the global maximum. $\square$

> [!Note] 💡 Why does the tree indexing work?
> By induction, a balanced binary tree with root at index 0, left child at $2i+1$, right child at $2i+2$ assigns consecutive indices $0$ to $n-1$ — no gaps. This guarantees `Heapify`'s recursive calls always land on valid array positions.

### Complexity

> [!Property] ⚙️ Heapify Complexity
> `Heapify` may recurse down a path from root to leaf. The height of a heap with $n$ elements is $\lfloor \log_2 n \rfloor$. Therefore:
> $$\text{Cost}(\texttt{Heapify on array of size } m) = O(\log m).$$

> [!Property] ⚙️ HeapSort Complexity
> Let $T(n)$ be the total cost.
>
> $$T(n) \leq \underbrace{\sum_{i=0}^{\lfloor n/2\rfloor - 1} O(\log(n-i+1))}_{\text{Phase 1: build}} + \underbrace{\sum_{i=1}^{n-1} \left(3 + O(\log i)\right)}_{\text{Phase 2: extract}} = O(n \log n).$$
>
> Both phases contribute $O(n \log n)$, so the total run time is $O(n \log n)$ in **all cases**.

---

## 4. Merge Sort

### Idea

> [!Definition] 📖 Merge Sort (Divide and Conquer)
> **1. Divide:** Split $A[\text{left}..\text{right}]$ at the midpoint $\text{mid} = \text{left} + \lfloor(\text{right}-\text{left})/2\rfloor$. An array with 0 or 1 element is already sorted (base case).
> **2. Conquer:** Recursively sort $A[\text{left}..\text{mid}]$ and $A[\text{mid}+1..\text{right}]$.
> **3. Merge:** Combine the two sorted halves into one sorted array using an auxiliary array.

### Algorithm

```
MergeSort(A, left, right):
    if left < right then
        mid ← left + (right - left) / 2
        MergeSort(A, left, mid)
        MergeSort(A, mid + 1, right)
        Merge(A, left, mid, right)

Merge(A, left, mid, right):
    i ← left
    j ← mid + 1
    k ← 0
    temp ← array of size (right - left + 1)

    while i ≤ mid and j ≤ right do
        if A[i] ≤ A[j] then
            temp[k] ← A[i];  i ← i + 1
        else
            temp[k] ← A[j];  j ← j + 1
        k ← k + 1

    while i ≤ mid do          // copy remaining left half
        temp[k] ← A[i];  i ← i + 1;  k ← k + 1

    while j ≤ right do         // copy remaining right half
        temp[k] ← A[j];  j ← j + 1;  k ← k + 1

    for x ← 0 to k-1 do       // copy back to original array
        A[left + x] ← temp[x]
```

### Trace — $[7,2,1,5,3,6,19,9]$

```
Divide:
    [7,2,1,5] | [3,6,19,9]
    [7,2]|[1,5] | [3,6]|[19,9]
    [7]|[2]|[1]|[5] | [3]|[6]|[19]|[9]

Conquer + Merge (bottom-up):
    [2,7] | [1,5] | [3,6] | [9,19]
    [1,2,5,7] | [3,6,9,19]
    [1,2,3,5,6,7,9,19]  ✓
```

### Correctness

> [!Proof] 🔷 Correctness of Merge Sort
> **Claim:** If `Merge` correctly produces a sorted subarray from two sorted halves, then `MergeSort` correctly sorts any subarray.
>
> **Base case:** A subarray of size 0 or 1 is already sorted. ✓
>
> **Inductive step:** By induction, `MergeSort(A, left, mid)` and `MergeSort(A, mid+1, right)` produce sorted halves. `Merge` then combines two sorted halves into one sorted array (standard merge procedure). ✓
>
> Setting `left = 0`, `right = n-1` sorts the entire array. $\square$

### Complexity

> [!Proof] 🔷 Complexity of Merge Sort — Recurrence and Level Analysis
> Let $T(n)$ be the cost of sorting $n$ elements.
>
> $$T(n) = 2\,T(n/2) + O(n), \qquad T(1) = O(1).$$
>
> **Level analysis** (for $n = 2^k$):
>
> | Level | # Calls | Work per call | Total work |
> |---|---|---|---|
> | 1 | 1 | $O(n)$ | $O(n)$ |
> | 2 | 2 | $O(n/2)$ | $O(n)$ |
> | 3 | 4 | $O(n/4)$ | $O(n)$ |
> | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
> | $\log n$ | $n$ | $O(1)$ | $O(n)$ |
>
> There are $\log n$ levels, each contributing $O(n)$ work. Therefore:
> $$T(n) = \Theta(n \log n).$$

---

## 5. Quick Sort

### Idea

> [!Definition] 📖 Quick Sort (Divide and Conquer)
> Like Merge Sort, Quick Sort uses divide-and-conquer, but the "hard work" is in the divide step (partitioning), and the combine step is trivial (concatenation):
>
> **1. Divide:** Choose a **pivot** element $p$ from $A$. Partition $A \setminus \{p\}$ into:
> $$A_{<} = \{x \in A \setminus \{p\} : x < p\}, \qquad A_{\geq} = \{x \in A \setminus \{p\} : x \geq p\}.$$
>
> **2. Conquer:** Recursively sort $A_{<}$ and $A_{\geq}$.
>
> **3. Combine:** Concatenate sorted $A_{<}$, then $p$, then sorted $A_{\geq}$ — no extra work needed.

### Algorithm

```
QuickSort(A, low, high):
    if low < high then
        pivotIndex ← Partition(A, low, high)
        QuickSort(A, low, pivotIndex - 1)
        QuickSort(A, pivotIndex + 1, high)

Partition(A, low, high):
    pivot ← A[high]          // choose last element as pivot
    i ← low - 1
    for j ← low to high - 1 do
        if A[j] < pivot then
            i ← i + 1
            Swap(A, i, j)
    Swap(A, i+1, high)        // place pivot in correct position
    return i + 1
```

> [!Note] 💡 Comparison with Merge Sort
> ```
> QuickSort(A, left, right):          MergeSort(A, left, right):
>     pivot ← Partition(...)              mid ← divide(...)
>     QuickSort(left, pivot-1)            MergeSort(left, mid)
>     QuickSort(pivot+1, right)           MergeSort(mid+1, right)
>     // combine: nothing to do           Merge(left, mid, right)
> ```
> Quick Sort does work **before** recursing; Merge Sort does work **after**.

### Partition Trace — $[7,2,1,5,3,6,19,9]$, `low=0`, `high=7`, `pivot=9`

```
i = -1
j=0: A[0]=7 < 9 → i=0, Swap(A,0,0): [7,2,1,5,3,6,19,9]
j=1: A[1]=2 < 9 → i=1, Swap(A,1,1): [7,2,1,5,3,6,19,9]
j=2: A[2]=1 < 9 → i=2, Swap(A,2,2): [7,2,1,5,3,6,19,9]
j=3: A[3]=5 < 9 → i=3, Swap(A,3,3): [7,2,1,5,3,6,19,9]
j=4: A[4]=3 < 9 → i=4, Swap(A,4,4): [7,2,1,5,3,6,19,9]
j=5: A[5]=6 < 9 → i=5, Swap(A,5,5): [7,2,1,5,3,6,19,9]
j=6: A[6]=19 ≥ 9 → no swap
Swap(A, 6, 7): [7,2,1,5,3,6,9,19]
return 6

Result: A[0..5]=[7,2,1,5,3,6] all < 9; A[6]=9; A[7]=19 ≥ 9  ✓
```

### Pivot Selection

> [!Property] ⚙️ Pivot Strategies
> - **First element:** Simple, but $O(n^2)$ on already-sorted or reverse-sorted input (all elements fall into one partition).
> - **Random element:** Generally safe; avoids worst-case on sorted inputs. Random number generation adds small overhead.
> - **Median-of-three:** Good practical choice; select median of first, middle, last elements.

> [!Warning] ⚠️ In-place Partition
> In-place partitioning is efficient but tricky to implement correctly. Even minor deviations can produce incorrect results or degrade performance. It is also **not stable** — it does not preserve the relative order of equal elements.

### Correctness

> [!Proof] 🔷 Correctness of Quick Sort (Mathematical Induction)
> **Base case ($n=1$):** A single-element array is sorted. ✓
>
> **Inductive hypothesis:** Quick Sort is correct on all arrays of size $< n$.
>
> **Inductive step:** After `Partition`, pivot $p$ is placed at index $q \in \{0,\ldots,n-1\}$ such that:
> **1.** All elements of $A[0..q-1]$ are $< p$.
> **2.** All elements of $A[q+1..n-1]$ are $\geq p$.
> By the inductive hypothesis, both sub-arrays are sorted correctly. The final array $A[0..q-1] \cdot p \cdot A[q+1..n-1]$ is sorted. $\square$

### Complexity

> [!Property] ⚙️ Worst Case $O(n^2)$
> If the pivot is always the minimum or maximum (e.g. sorted array + first-element pivot), one partition has $n-1$ elements and the other is empty. The recurrence becomes:
> $$T(n) = T(n-1) + O(n) \;\Rightarrow\; T(n) = O(n^2).$$

> [!Proof] 🔷 Average Case $O(n \log n)$ — Indicator Random Variable Argument
> Let $b_1 < b_2 < \cdots < b_n$ be the sorted order of $A$. Define indicator variable $X_{ij}$ ($i < j$):
> $$X_{ij} = \begin{cases}1 & \text{if } b_i \text{ and } b_j \text{ are compared at any point}\\ 0 & \text{otherwise}\end{cases}$$
>
> **Total comparisons:**
> $$X = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} X_{ij}, \qquad \mathbb{E}[X] = \sum_{i=1}^{n-1}\sum_{j=i+1}^{n} \Pr[X_{ij}=1].$$
>
> **Key observation:** $b_i$ and $b_j$ are compared iff one of them is the first pivot chosen from the set $Y_{ij} = \{b_i, b_{i+1}, \ldots, b_j\}$. Since pivots are chosen uniformly at random, and $|Y_{ij}| = j - i + 1$:
> $$\Pr[X_{ij} = 1] = \frac{2}{j - i + 1}.$$
>
> **Computing the expectation:**
> $$\mathbb{E}[X] = \sum_{i=1}^{n-1}\sum_{j=i+1}^{n} \frac{2}{j-i+1} = \sum_{i=1}^{n-1}\sum_{k=2}^{n-i+1} \frac{2}{k} \leq 2(n+1) H_n - 2(n-1),$$
> where $H_n = \sum_{i=1}^{n} \frac{1}{i} = \ln n + \Theta(1)$ is the $n$-th harmonic number.
>
> Therefore $\mathbb{E}[X] = O(n \ln n) = O(n \log n)$. $\square$

---

## 6. Radix Sort

### Idea

> [!Definition] 📖 Radix Sort
> A **non-comparison-based** sorting algorithm that sorts integers by processing one digit at a time, from the **least significant digit (LSD)** to the **most significant digit (MSD)**.
>
> For each digit position, elements are grouped by their digit value and recombined in order. The algorithm relies on a **stable** sub-sort (Counting Sort) for each digit pass.

### Algorithm

```
RadixSort(A, n, d):
    // d = number of digits, processed from rightmost (position 1) to leftmost (position d)
    for j ← 1 to d do
        StableCountingSort(A, n, j)    // sort by j-th digit (1 = rightmost)

CountingSort(A, n, exp):
    // exp = 1, 10, 100, ... (the digit place value)
    output ← array of size n
    count  ← array of size 10, initialised to 0

    // Count occurrences of each digit
    for i ← 0 to n-1 do
        digit ← (A[i] / exp) mod 10
        count[digit] ← count[digit] + 1

    // Prefix sums (cumulative counts = actual positions)
    for i ← 1 to 9 do
        count[i] ← count[i] + count[i-1]

    // Build output in stable sorted order (traverse in reverse for stability)
    for i ← n-1 downto 0 do
        digit ← (A[i] / exp) mod 10
        output[count[digit] - 1] ← A[i]
        count[digit] ← count[digit] - 1

    // Copy output back to A
    for i ← 0 to n-1 do
        A[i] ← output[i]
```

### Trace — $[7,2,1,5,3,6,19,9]$, $d = 2$, $k = 10$

Treat all numbers as 2-digit: $07, 02, 01, 05, 03, 06, 19, 09$.

**Pass 1 — sort by units digit:**

| Bucket | Elements |
|---|---|
| 1 | 01 |
| 2 | 02 |
| 3 | 03 |
| 5 | 05 |
| 6 | 06 |
| 7 | 07 |
| 9 | 19, 09 |

After pass 1: $[01, 02, 03, 05, 06, 07, 19, 09]$

**Pass 2 — sort by tens digit:**

| Bucket | Elements |
|---|---|
| 0 | 01, 02, 03, 05, 06, 07, 09 |
| 1 | 19 |

After pass 2: $[1, 2, 3, 5, 6, 7, 9, 19]$ ✓

### Correctness

> [!Proof] 🔷 Correctness of Radix Sort (Induction on digit passes)
> **Base case:** After pass 1 (units digit), the array is sorted by its least significant digit. ✓
>
> **Inductive hypothesis:** After $k$ passes, the array is sorted by the $k$ least significant digits.
>
> **Inductive step:** Pass $k+1$ sorts by the $(k+1)$-th digit. Since `CountingSort` is **stable**, elements with the same $(k+1)$-th digit maintain their relative order from the previous $k$ passes (i.e. they are ordered correctly by the $k$ less significant digits). Therefore the array is sorted by $k+1$ digits. ✓
>
> After all $d$ passes, the array is fully sorted. $\square$

### Complexity

> [!Property] ⚙️ Radix Sort Complexity
> - Each `CountingSort` pass costs $O(n + k)$, where $n$ is the number of elements and $k$ is the digit range (base, typically 10).
> - There are $d$ passes (one per digit).
> - **Total: $O(d(n + k))$** in best, average, and worst case.
> - **Space: $O(n + k)$** for the auxiliary array (not in-place).
> - **Stable:** Yes — relies on the stability of `CountingSort`.

> [!Note] 💡 When is Radix Sort faster than comparison-based sorts?
> When $d$ is small and $k$ is small relative to $n$, Radix Sort beats $O(n \log n)$ comparison sorts. For example, sorting $n$ 32-bit integers with $d = 4$ passes (base $2^8 = 256$): cost is $O(4(n + 256)) = O(n)$.

---

## 📘 Examples & Applications

### Example 1 — Selection Sort vs Insertion Sort on the Same Input

> [!Example] 📘 Sort $[13, 4, 2, 7, 34, 1]$ using both algorithms
> **Using:** Selection Sort and Insertion Sort algorithms.
>
> **Selection Sort (ascending):**
>
> | $i$ | Min | Array |
> |---|---|---|
> | 0 | $A[5]=1$ | $[1, 4, 2, 7, 34, 13]$ |
> | 1 | $A[2]=2$ | $[1, 2, 4, 7, 34, 13]$ |
> | 2 | $A[2]=4$ | $[1, 2, 4, 7, 34, 13]$ |
> | 3 | $A[3]=7$ | $[1, 2, 4, 7, 34, 13]$ |
> | 4 | $A[5]=13$ | $[1, 2, 4, 7, 13, 34]$ |
> | 5 | — | $[1, 2, 4, 7, 13, 34]$ ✓ |
>
> **Insertion Sort (ascending):**
>
> | $i$ | key | Array |
> |---|---|---|
> | 1 | 4 | $[4, 13, 2, 7, 34, 1]$ |
> | 2 | 2 | $[2, 4, 13, 7, 34, 1]$ |
> | 3 | 7 | $[2, 4, 7, 13, 34, 1]$ |
> | 4 | 34 | $[2, 4, 7, 13, 34, 1]$ |
> | 5 | 1 | $[1, 2, 4, 7, 13, 34]$ ✓ |

---

### Example 2 — Heap Construction (Heapify) Step-by-Step

> [!Example] 📘 Build a max-heap from $[13, 4, 2, 7, 34, 1]$
> **Using:** `Heapify` called from index $\lfloor 6/2 \rfloor - 1 = 2$ down to $0$.
>
> **Step 1.** `Heapify(A, 6, 2)`: Node $2$ has value $2$, left child $A[5]=1$. $2 > 1$ → no swap. Array: $[13, 4, 2, 7, 34, 1]$.
>
> **Step 2.** `Heapify(A, 6, 1)`: Node $1$ has value $4$, left $A[3]=7$, right $A[4]=34$. Largest is $34$ at index $4$. Swap $A[1]$ and $A[4]$: $[13, 34, 2, 7, 4, 1]$. Recurse on index $4$: no children in range → STOP.
>
> **Step 3.** `Heapify(A, 6, 0)`: Node $0$ has value $13$, left $A[1]=34$, right $A[2]=2$. Largest is $34$ at index $1$. Swap $A[0]$ and $A[1]$: $[34, 13, 2, 7, 4, 1]$. Recurse on index $1$: left $A[3]=7$, right $A[4]=4$. $13 > 7 > 4$ → no swap. STOP.
>
> **Max-heap result:** $[34, 13, 2, 7, 4, 1]$ ✓

---

### Example 3 — Merge Sort Trace

> [!Example] 📘 Sort $[13, 4, 2, 7, 34, 1]$ using Merge Sort
> **Using:** `MergeSort` and `Merge` algorithms.
>
> **Divide phase:**
> ```
> [13, 4, 2, 7, 34, 1]
> → [13, 4, 2]  |  [7, 34, 1]
> → [13][4,2]   |  [7][34,1]
> → [13][4][2]  |  [7][34][1]
> ```
>
> **Merge phase:**
> ```
> [4,2] → Merge([4],[2]) = [2,4]
> [34,1] → Merge([34],[1]) = [1,34]
> [13,4,2] → Merge([13],[2,4]) = [2,4,13]
> [7,34,1] → Merge([7],[1,34]) = [1,7,34]
> Final → Merge([2,4,13],[1,7,34]) = [1,2,4,7,13,34]  ✓
> ```

---

### Example 4 — Quick Sort Worst Case vs Average Case

> [!Example] 📘 Demonstrate the worst case of Quick Sort
> **Using:** Quick Sort with last-element pivot on a sorted array.
>
> Input: $[1, 2, 3, 4, 5]$, pivot = last element.
>
> **Pass 1:** pivot $= 5$. Partition gives $A_{<} = [1,2,3,4]$, $A_{\geq} = []$. Depth of recursion: $n-1 = 4$.
> **Pass 2:** pivot $= 4$. Partition gives $A_{<} = [1,2,3]$, $A_{\geq} = []$.
> ... and so on.
>
> Total comparisons: $(n-1) + (n-2) + \cdots + 1 = \frac{n(n-1)}{2} = O(n^2)$.
>
> **Fix:** Use a **random pivot** to avoid this degenerate case.

---

### Example 5 — Radix Sort with Larger Input

> [!Example] 📘 Sort $[1, 56, 3, 6, 9, 8, 30, 24, 17, 7]$ using Radix Sort
> **Using:** Radix Sort, $d=2$, $k=10$. Represent all as 2-digit: $01,56,03,06,09,08,30,24,17,07$.
>
> **Pass 1 — units digit:**
>
> | Bucket | Elements collected |
> |---|---|
> | 0 | 30 |
> | 1 | 01 |
> | 3 | 03 |
> | 4 | 24 |
> | 6 | 56, 06 |
> | 7 | 17, 07 |
> | 8 | 08 |
> | 9 | 09 |
>
> After pass 1: $[30, 01, 03, 24, 56, 06, 17, 07, 08, 09]$
>
> **Pass 2 — tens digit:**
>
> | Bucket | Elements collected |
> |---|---|
> | 0 | 01, 03, 06, 07, 08, 09 |
> | 1 | 17 |
> | 2 | 24 |
> | 3 | 30 |
> | 5 | 56 |
>
> After pass 2: $[1, 3, 6, 7, 8, 9, 17, 24, 30, 56]$ ✓

---

## 🗂️ Summary

- **Selection Sort** ($\Theta(n^2)$, in-place, not stable): always performs the same number of comparisons regardless of input order. Simple but slow.
- **Insertion Sort** ($O(n)$ best, $O(n^2)$ worst, in-place, stable): efficient on nearly-sorted data; the inner while loop is skipped when input is sorted.
- **Heap Sort** ($O(n \log n)$ all cases, in-place, not stable): uses a max-heap. Phase 1 builds the heap in $O(n)$ amortised time; Phase 2 extracts elements in $O(n \log n)$.
- **Merge Sort** ($\Theta(n \log n)$ all cases, not in-place, stable): guaranteed $\Theta(n \log n)$ via recurrence $T(n) = 2T(n/2) + O(n)$; requires $O(n)$ auxiliary space.
- **Quick Sort** ($O(n \log n)$ average, $O(n^2)$ worst, in-place, not stable): average case proven using indicator random variables and harmonic numbers. Worst case occurs on sorted input with first-element pivot; use random pivot to avoid this.
- **Radix Sort** ($O(d(n+k))$, not in-place, stable): non-comparison-based; beats $O(n \log n)$ when $d$ and $k$ are small. Correctness relies on the stability of the underlying Counting Sort.
- **Stability matters** when records have multiple keys — Radix Sort and Insertion Sort are stable; Selection Sort, Heap Sort, and Quick Sort are not.
- **Space trade-off:** Merge Sort and Radix Sort require $O(n)$ extra memory; the others are in-place.
