---
aliases: [DSA Exam Procedures, Quiz Cheatsheet]
tags: [DSA, exam, procedures, VGU]
---

# 🧠 DSA Exam — Procedure-Only Cheatsheet

> **Format:** Step-by-step procedures + cases + worked examples from your actual quizzes. No theory, no proofs.

---

## 📌 Table of Contents

1. [[#Binary Search — Descending Array]]
2. [[#Merge Two Ascending Arrays]]
3. [[#Asymptotic Complexity — Identifying Big-O]]
4. [[#Heap Construction (Max-Heap)]]
5. [[#Heap Sort]]
6. [[#QuickSort — Median-of-Three Pivot + Partition]]
7. [[#Stack — Postfix to Infix + Evaluation]]
8. [[#Linked List — Find Middle Node (Fast/Slow)]]
9. [[#Hashing — Linear, Quadratic, Double Hashing]]
10. [[#BST — Traversals]]
11. [[#AVL Tree — Insert + Rotation]]
12. [[#AVL Tree — Delete]]
13. [[#Graph — Degree Sequences]]
14. [[#Graph — Prim's MST]]
15. [[#Graph — Dijkstra's Shortest Path]]

---

## 1. Binary Search — Descending Array

> Array is sorted **descending**. `mid = (left + right) / 2` (integer division).

### Procedure

1. Set `left = 0`, `right = n−1`.
2. Compute `mid = (left + right) / 2`.
3. **If** `arr[mid] == target` → found. Count this step.
4. **If** `arr[mid] > target` → search right half: `left = mid + 1`.
5. **If** `arr[mid] < target` → search left half: `right = mid − 1`.
6. Repeat until found or `left > right`.

> [!tip] Counting steps
> Each iteration = 1 step. "Most steps" = element that requires the most iterations = deepest path in the search tree.

### Worked Example (Quiz 2, P1)

Array (indices 0–9): `95 83 77 74 63 51 40 32 11 5`

**Question a: which element(s) take most steps?**

```
Step 1: mid = (0+9)/2 = 4 → arr[4] = 63
Step 2: mid = (5+9)/2 = 7 → arr[7] = 32  OR  mid = (0+3)/2 = 1 → arr[1] = 83
Step 3: mid = (8+9)/2 = 8 → arr[8] = 11  OR  mid = (5+6)/2 = 5 → arr[5] = 51 ...
Step 4: mid = (9+9)/2 = 9 → arr[9] = 5   OR  mid = (2+3)/2 = 2 → arr[2] = 77
```
Elements at max depth (4 steps): **77, 11, 5, 51** — any element that requires 4 comparisons.
Your paper correctly identified 77, 11, 51.

**Question b: searching for 38 — how many iterations?**
- Step 1: mid=4, arr[4]=63 > 38 → go right, left=5
- Step 2: mid=7, arr[7]=32 < 38 → go left, right=6
- Step 3: mid=5, arr[5]=51 > 38 → go right, left=6
- Step 4: mid=6, arr[6]=40 > 38 → go right, left=7
- Now left > right → not found.
**Answer: 4 iterations** (your paper wrote 4 — correct ✓)

---

## 2. Merge Two Ascending Arrays

### Procedure

Given arrays A[0..m−1] and B[0..n−1], merge into C. Use pointers `i=0, j=0, k=0`.

1. While `i < m` AND `j < n`:
   - If `A[i] <= B[j]`: `C[k++] = A[i++]`
   - Else: `C[k++] = B[j++]`
2. Copy remaining elements of A or B into C.

**Time complexity: O(m + n)**

### Worked Example (Quiz 2, P2b)

A: `1,2,3,5,8,13,21` | B: `4,9,15,16,25,36`

Trace until C gets 7 elements:
```
1<4  → i=1, C=[1]
2<4  → i=2, C=[1,2]
3<4  → i=3, C=[1,2,3]
5>4  → j=1, C=[1,2,3,4]
5<9  → i=4, C=[1,2,3,4,5]
8<9  → i=5, C=[1,2,3,4,5,8]
13>9 → j=2, C=[1,2,3,4,5,8,9]  ← 7 elements
```
**Answer: i=5, j=2** ✓

---

## 3. Asymptotic Complexity — Identifying Big-O

### Cases to memorize

| Code pattern | Big-O |
|---|---|
| Single recursion `f(n) = f(n-1) + O(1)` | O(n) |
| Single `for` loop 1..n | O(n) |
| Nested `for` loops 1..n each | O(n²) |
| Outer loop i=0..n, inner loop j=i..n | O(n²) |

### Worked Example (Quiz 1, Q2)

- F1 (recursion, sum 1 to n): each call does O(1), n calls → **O(n)**
- F2 (single for loop): **O(n)**
- F3 (two nested for loops, both 1..n): **O(n²)**

---

## 4. Heap Construction (Max-Heap)

### Procedure — `HeapConstruction` algorithm

Given array A[0..n−1]:
1. Start from last non-leaf: index `i = floor(n/2) − 1`, go down to `i = 0`.
2. For each `i`, call **MaxHeapify(A, i, n)**:
   - `largest = i`
   - If `left = 2i+1 < n` and `A[left] > A[largest]`: `largest = left`
   - If `right = 2i+2 < n` and `A[right] > A[largest]`: `largest = right`
   - If `largest ≠ i`: swap `A[i]` ↔ `A[largest]`, recurse on `largest`

### Worked Example (Quiz 2, P3a)

Input: `1, 30, 3, 12, 53, 62, 14, 32, 41, 49` (indices 0–9)

Last non-leaf = index 4. Process i=4,3,2,1,0 with heapify.

Result (from your paper): `[62, 53, 14, 41, 49, 3, 1, 32, 12, 30]`

### Check if array is max-heap (P3b)

Algorithm: For each node `i` from 0 to `floor(n/2)−1`, check:
- `A[i] >= A[2i+1]` (if left child exists)
- `A[i] >= A[2i+2]` (if right child exists)

If all pass → max-heap. **Time: O(n)**

---

## 5. Heap Sort

### Procedure

Starting from a max-heap:
1. Swap `A[0]` (max) with `A[heap_size − 1]`.
2. Decrease `heap_size` by 1 (last element is "placed").
3. Call `MaxHeapify(A, 0, heap_size)` to restore heap.
4. Repeat until `heap_size = 1`.

> [!note] The sorted portion grows from the right end. The heap portion shrinks from the right.

### Worked Example (Quiz 2, P3c)

Start from heap: `[62, 53, 14, 41, 49, 3, 1, 32, 12, 30]`

Goal: last 3 elements = 49, 53, 62 (ascending).

- Swap 62↔30, heapify → 53 rises → last element placed: **62**
- Swap 53↔12, heapify → 49 rises → **53** placed
- Swap 49↔..., heapify → **49** placed

After these 3 extractions: `..., 49, 53, 62` ✓

Your paper answer: `62, 53, 14, 41, 49, 3, 1, 32, 12, 30` → that's the initial heap before sort steps. The final state after extracting 3 maxima has the last 3 positions = 49, 53, 62.

---

## 6. QuickSort — Median-of-Three Pivot + Partition

### Median-of-Three Pivot Selection

1. Take `A[0]`, `A[mid]`, `A[n−1]`.
2. Sort these 3, pick the **middle value** as pivot.

### Worked Example (Quiz 2, P4a)

Array: `1, 30, 3, 12, 53, 62, 14, 32, 41, 49`
- A[0]=1, A[4]=53, A[9]=49
- Sorted: 1, 49, 53 → middle = **49** ✓

### Partition Procedure (pivot = 49)

Use two-pointer scan. Elements < pivot stay left, elements > pivot move right.

Array after partition with pivot 49:
```
1, 30, 3, 12, 14, 32, 41, [49], 53, 62
```
Your paper traced each element:
- 1,30,3,12 < 49 → stay
- 53 > 49 → move right
- 62 > 49 → move right
- 14,32,41 < 49 → stay
- Pivot 49 placed at index 7

**Result: `1, 30, 3, 12, 14, 32, 41, 49, 53, 62`** ✓

---

## 7. Stack — Postfix to Infix + Evaluation

### Postfix → Infix Procedure

Use a **string stack**. For each token:
- **Operand** → push it as string
- **Operator** → pop two operands `b` then `a`, push `"(a op b)"`

### Evaluation Procedure

Use a **number stack**. For each token:
- **Operand** → push number
- **Operator** → pop `b` then `a`, compute `a op b`, push result

### Worked Example (Quiz 3, Q9)

Expression: `18 3 / 7 5 2 + * + 4 6 * − 9 +`

Infix (from your paper): `((18/3) + 7*(5+2)) − 24 + 4*6 + 9`
Value: **40** ✓

Trace:
```
18 → push 18
3  → push 3
/  → pop 3,18 → push 18/3 = 6
7  → push 7
5  → push 5
2  → push 2
+  → pop 2,5 → push 7
*  → pop 7,7 → push 49
+  → pop 49,6 → push 55
4  → push 4
6  → push 6
*  → pop 6,4 → push 24
−  → pop 24,55 → push 31
9  → push 9
+  → pop 9,31 → push 40
```
**Answer: 40** ✓

---

## 8. Linked List — Find Middle Node (Fast/Slow Pointers)

### Procedure

```
slow = head
fast = head
while (fast != null AND fast->next != null):
    slow = slow->next
    fast = fast->next->next
return slow  // slow is at middle
```

**Cases:**
- Odd length n: returns exact middle.
- Even length n: returns the **second** middle node (as required by the problem).

### Edge case
- If `head == null` → return `null`

### Worked Example (Quiz 3, Q11)

List: `{1}→{2}→{3}→{4}→{5}` → middle = node 3 ✓
List: `{1}→{2}→{3}→{4}→{5}→{6}` → middle = node 4 (second middle) ✓

---

## 9. Hashing — Linear, Quadratic, Double Hashing

**Setup:** Table size m=13, h(k) = k mod m.

### Linear Probing

Collision at slot s → try `s+1, s+2, s+3, ...` (mod m)

### Quadratic Probing

`h(k,i) = h(k) + 2i² + 1` (note: your quiz used this specific formula, not the standard one)

Try i=0,1,2,3... until empty slot found.

### Double Hashing

`h₂(k) = 7 − (k mod 7)`
On collision: next slot = `(h(k) + i * h₂(k)) mod m`

### Worked Example (Quiz 3 part 3, P1a)

Insert sequence: 40, 31, 53, 44, 66, 77, 17, 90, 30, 102

Base slots: 40→1, 31→5, 53→1(col!), 44→5(col!), 66→1(col!), 77→12, 17→4, 90→12(col!), 30→4(col!), 102→11

**Linear Probing result (from your paper):**
```
0:90  1:40  2:53  3:66  4:17  5:31  6:44  7:30  11:102  12:77
```

### Probe Count Procedure

To **find** key k: count how many slots you probe until you hit k.
- Start at `h(k)`, count = 1.
- Each collision = +1 probe.

To **insert** key k after deletions:
- Deleted slots are marked (tombstone).
- During insert, you **skip over** tombstones (they count as probes).
- During search, you also pass through tombstones.

> [!warning] After deleting keys, probe count for insert increases because tombstones must be traversed.

### Worked Example (Quiz 3 part 3, P1d–f)

**Find 28 (not in table):**
- Linear: probe until empty → 7 probes
- Quadratic: 5 probes
- Double: 1 probe (your paper: 1, 17)

**Insert 43 after removing 44, 77, 18:**
- Linear: 1 probe
- Quadratic: 2 probes
- Double: 2 probes

**Insert 56 (h(56)=56 mod 13 = 4):**
- Linear: 13 probes
- Quadratic: 6 probes
- Double: 4 probes

---

## 10. BST — Traversals

| Traversal | Order | Mnemonic |
|---|---|---|
| Preorder | Root → Left → Right | **R-L-Right** |
| Inorder | Left → Root → Right | sorted output |
| Postorder | Left → Right → Root | **L-R-Root** |

### Worked Example (Quiz 5, P1)

BST:
```
        6
       / \
      3   9
     / \   \
    1   4   12
     \   \   \
      2   5   10
```

**Preorder:** 6, 3, 1, 2, 4, 5, 9, 12, 10 ✓ (your paper)

**Post-order traversal (Quiz 5, P4a):**

Tree with nodes 50, x₁, x₃, 20, 40, 60, x₂, 25, 70, x₄, 90.
Post-order given: `15, 25, 20, 40, 35, 70, 60, 90, 85, 75, 50`

Reading post-order left-to-right, the **last element** is always the root.
- x₁ = 35 (between 25,20 and 40 in post-order structure)
- x₂ = 15
- x₃ = 75
- x₄ = 85 ✓

---

## 11. AVL Tree — Insert + Rotation

### Insertion Procedure

1. Insert using normal BST insert.
2. Walk back up to root, updating heights.
3. At first unbalanced node (|balance| > 1), apply rotation.

### Balance Factor = height(left) − height(right)

### 4 Rotation Cases

| Case | Condition | Fix |
|---|---|---|
| Left-Left (LL) | BF > 1, new node in left-left | Right rotation at unbalanced node |
| Right-Right (RR) | BF < −1, new node in right-right | Left rotation |
| Left-Right (LR) | BF > 1, new node in left-right | Left rotate left child, then right rotate |
| Right-Left (RL) | BF < −1, new node in right-left | Right rotate right child, then left rotate |

### Right Rotation (LL case)

```
    z                y
   / \             /   \
  y   T4   →    x       z
 / \           / \     / \
x   T3        T1  T2  T3  T4
```

### Worked Example (Quiz 5, P5)

Insert sequence: 10, 25, 35, 5, 8, 15, 17, 13, 12, 7, 13, 11, 40

At each rotation point, identify case and apply. Your final tree:
```
        15
       /  \
     10    25
    /  \   / \
   7   12 17  35
  /   / \  \    \
 5   8  13  ?   40
```
(Your paper drew this correctly with 10 points earned ✓)

---

## 12. AVL Tree — Delete

### Procedure

1. **Find the node** to delete.
2. **Delete it** using BST delete rules:
   - Leaf: just remove.
   - One child: replace with child.
   - Two children: replace with **inorder successor** (smallest in right subtree), then delete the successor.
3. **Walk up** from deletion point, check balance factors.
4. At each unbalanced node, apply the appropriate rotation (same 4 cases as insert).

### Worked Example (Quiz 5, P3)

AVL tree, delete node 33:
```
Step 1: Delete 33 → inorder successor = 53 (smallest in right subtree)
         Replace 33 with 53, delete original 53 node
Step 2: Check balance at 53 (now root): BF = 2 → Left-Left violation
Step 3: Right rotation at 53... 
         BUT left child (13) has right-heavy left subtree → Left-Right case
         → Left rotate at 13, then right rotate at 53
```
Your paper: "Left-Left → Right rotation" — ✓ direction correct.

---

## 13. Graph — Degree Sequences

### Erdős–Gallai condition (simplified exam version)

A sequence is a valid degree sequence **if and only if:**
1. **Total degree is even** (sum of all degrees must be even, since each edge contributes 2).
2. The sequence can actually be realized (check by trying to construct the graph).

> [!tip] Quick filter: if sum is odd → immediately **No**.

### Worked Example (Quiz 6, P2)

| Sequence | Sum | Verdict |
|---|---|---|
| 6,5,4,2,1,1,1,1 | 21 | **No** — odd sum |
| 7,6,5,4,3,2,1 | 28 | **Yes** — even, realizable |
| 6,6,6,6,3,3,2,2 | 34 | **Yes** — even |
| 7,6,6,4,4,3,2,2 | 34 | **Yes** — even |
| 8,7,7,6,4,2,1,1 | 36 | **Yes** — even |

✓ matches your paper.

---

## 14. Graph — Prim's MST

### Procedure

Start from given vertex. Maintain set of **visited vertices** and **candidate edges**.

1. Mark start vertex visited.
2. Add all edges from start to candidate list.
3. Pick the **minimum weight edge** that connects a visited vertex to an unvisited vertex.
4. Mark the new vertex visited. Add its edges to candidates.
5. Repeat until all vertices visited.

> [!tip] At each step, always pick the globally cheapest edge that doesn't form a cycle (i.e., goes to an unvisited node).

### Worked Example (Quiz 6, P3b)

Graph: 9 vertices, 13 edges. Start = F. x = 8 (so edge B-I = 8).

Prim's steps:
```
Start: F
(F,G)=5 ✓  visited: {F,G}
(G,H)=5 ✓  visited: {F,G,H}
(H,I)=5 ✓  visited: {F,G,H,I}
(H,A)=6 ✓  visited: {F,G,H,I,A}
(F,E)=7 ✓  visited: {F,G,H,I,A,E}
(E,D)=8 ✓  visited: {F,G,H,I,A,E,D}
(A,B)=8 ✓  visited: {F,G,H,I,A,E,D,B}
(B,C)=7 ✓  visited: {F,G,H,I,A,E,D,B,C}
```
Total = 5+5+5+6+7+8+8+7 = **51** ✓

---

## 15. Graph — Dijkstra's Shortest Path

### Procedure

1. Set dist[source] = 0, all others = ∞.
2. Use a table: columns = all vertices, rows = iterations.
3. Each iteration: pick unvisited vertex u with minimum dist[u].
4. For each neighbor v of u: if `dist[u] + w(u,v) < dist[v]`, update `dist[v] = dist[u] + w(u,v)`.
5. Mark u as visited (cross it out).
6. Repeat until all visited.

> [!tip] The column for a vertex stops updating once it's **visited** (crossed out). The final answer for that vertex is the value when it was crossed out.

### Worked Example (Quiz 6, P3c)

Source = A. Find shortest paths to all vertices.

Your table (reading from paper):
```
Initial: A=0, rest=∞
Visit A: update B=8, H=6 (via A-H)
Visit H: update I=11, G=11 (H-G costs 5, H-I=5)
Visit G: update F=16 (G-F=5)
Visit I: update F=11 (I-F better), B=15 (not better)
...
```

**Vertices NOT affected by x (Quiz 6c):**
Vertices whose shortest path from A doesn't use any edge with weight x.
- From your analysis: **A, B, C, D, H, I, G** are not affected.
- Only **F and E** are affected if x=1 makes A→H→I→F cheaper than alternative.

---

## 🚨 Common Exam Traps

> [!warning] Watch out for these

- **Binary search on descending array**: when `arr[mid] > target`, go RIGHT (not left). Opposite of ascending.
- **Heap index**: array is 0-indexed. Left child = `2i+1`, right = `2i+2`. Parent = `(i-1)/2`.
- **Postfix eval**: pop order matters. Pop `b` first, then `a`. Compute `a op b` (not `b op a`). Matters for `/` and `−`.
- **AVL rotation case**: check where the NEW node is relative to the UNBALANCED node, not the parent.
- **Hashing probe count**: count starts at 1 (the initial probe), not 0.
- **Prim's vs Kruskal's**: Prim = grow from one vertex. Kruskal = sort all edges, add if no cycle.
- **Degree sequence**: odd sum → instantly No, no need to draw.
- **Fast/slow pointer**: returns SECOND middle for even-length lists.

---

*Generated from Quiz 1–6 handwritten answers | 61CSE108 Data Structures and Algorithms | VGU*
