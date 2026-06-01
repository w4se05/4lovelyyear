---
title: "DSA Final Exam Prep: Procedures & Examples"
tags: [dsa, algorithms, study-guide, final-exam]
---

# 🚀 DSA Final Exam Master Guide

This guide strips away theory and proofs, focusing exclusively on the step-by-step execution procedures, edge cases, and worked examples required to ace your Data Structures and Algorithms final exam.

---

## 1. Hash Table Collision Resolution

**Goal:** Insert elements into a hash table of size $m$ when collisions occur.

### Step-by-Step Procedure
1. Calculate the base hash: $h(k) = k \pmod m$.
2. If the slot $h(k)$ is empty, insert the element.
3. If the slot is occupied (a collision), calculate the probe sequence using a step variable $i = 1, 2, 3, \dots$ until an empty slot is found.
    * **Linear Probing:** $h(k, i) = (h(k) + i) \pmod m$
    * **Quadratic Probing:** $h(k, i) = (h(k) + c_1 i + c_2 i^2) \pmod m$
    * **Double Hashing:** $h(k, i) = (h(k) + i \cdot h_2(k)) \pmod m$

> [!warning] Edge Cases & Traps
> * **Zero Step in Double Hashing:** Ensure $h_2(k) 
\neq 0$. If $h_2(k)$ evaluates to 0, it creates an infinite loop. The formula usually prevents this (e.g., $R - (k \pmod R)$).
> * **Table Size:** Always apply $\pmod m$ at the very end of your calculation to wrap around the table.

### 📝 Worked Example
**Given:** $m = 13$, Insert `53`. 
Formulas: Base $h(k) = k \pmod{13}$. 
Linear: $+ i$. Quadratic: $+ 2i^2 + 1$. Double: $h_2(k) = 7 - (k \pmod 7)$.
Assume slots `1` and `2` are already occupied.

* **Base Hash:** $53 \pmod{13} = 1$. (Collision: slot 1 is full).
* **Linear ($i=1$):** $(1 + 1) \pmod{13} = 2$. (Collision).
* **Linear ($i=2$):** $(1 + 2) \pmod{13} = 3$. (Empty! Insert at 3).
* **Quadratic ($i=1$):** $(1 + 2(1^2) + 1) \pmod{13} = 4$. (Empty! Insert at 4).
* **Double ($i=1$):** $h_2(53) = 7 - (53 \pmod 7) = 7 - 4 = 3$. 
  Probe: $(1 + 1 \cdot 3) \pmod{13} = 4$. (Empty! Insert at 4).

---

## 2. AVL Tree Insertions & Deletions

**Goal:** Maintain a self-balancing Binary Search Tree where the height difference between left and right subtrees (Balance Factor) is at most 1.

### Step-by-Step Procedure
1. **Insert/Delete** the node using standard BST rules.
2. **Backtrack** from the modified node up to the root, updating heights.
3. Calculate **Balance Factor (BF)** for each node: `Height(Left) - Height(Right)`.
4. If $BF > 1$ or $BF < -1$, the tree is unbalanced at this node (let's call it $Z$). Identify the path of the heavy subtrees to determine the rotation case.

### The 4 Rotation Cases
Let $Z$ be the first unbalanced node found while tracking up. Let $Y$ be its heavy child, and $X$ be the heavy child of $Y$.

> [!info] 1. Left-Left (LL) Case -> Right Rotation
> * **Condition:** $Z$ is left-heavy, $Y$ is left-heavy.
> * **Action:** Rotate Right around $Z$. $Y$ becomes the new root of this subtree, $Z$ becomes $Y$'s right child. $Y$'s old right child becomes $Z$'s left child.

> [!info] 2. Right-Right (RR) Case -> Left Rotation
> * **Condition:** $Z$ is right-heavy, $Y$ is right-heavy.
> * **Action:** Rotate Left around $Z$. $Y$ becomes the new root, $Z$ becomes $Y$'s left child. $Y$'s old left child becomes $Z$'s right child.

> [!info] 3. Left-Right (LR) Case -> Left-Right Rotation
> * **Condition:** $Z$ is left-heavy, $Y$ is right-heavy.
> * **Action:** First, Rotate Left around $Y$ (turns it into an LL case). Then, Rotate Right around $Z$.

> [!info] 4. Right-Left (RL) Case -> Right-Left Rotation
> * **Condition:** $Z$ is right-heavy, $Y$ is left-heavy.
> * **Action:** First, Rotate Right around $Y$ (turns it into an RR case). Then, Rotate Left around $Z$.

### 📝 Worked Example (Deletion)
**Task:** Delete node `33` from a valid AVL tree where `33` is the root, and its in-order successor is `53`.
1. **Standard BST Delete:** Replace `33` with `53`. Delete the original `53` leaf node.
2. **Backtrack & Check BF:** Moving up from the deleted leaf, update heights. 
3. **Identify Violation:** The new root `53` has a left subtree of height 3 and a right subtree of height 1. $BF = 3 - 1 = 2$.
4. **Determine Case:** The left child of `53` is `13` (heavy), and the left child of `13` is `9` (heavy). This is an **LL Case**.
5. **Rotate:** Perform a single Right Rotation around `53`. `13` becomes the new root, `9` remains its left child, and `53` becomes its right child.

---

## 3. Max-Heap Construction & Heapsort

**Goal:** Convert an unordered array into a Max-Heap, then sort it.

### Step-by-Step Procedure: Heap Construction
1. Identify the last non-leaf node: `index = floor(n/2) - 1` (assuming 0-indexed array).
2. Loop backwards from this index down to `0`.
3. For each node, perform `sift-down` (Heapify):
    * Compare the node with its left child `2i + 1` and right child `2i + 2`.
    * Swap the node with the **largest** of its children.
    * If a swap occurred, recursively `sift-down` the affected subtree.

### Step-by-Step Procedure: Heapsort
1. Build a Max-Heap (see above).
2. Swap the root (index `0`, max value) with the last element in the heap.
3. Reduce the heap size by 1 (ignoring the newly placed max element at the end).
4. Call `sift-down` on the new root (index `0`) to restore the Max-Heap property.
5. Repeat steps 2-4 until the heap size is 1.

> [!warning] Edge Cases & Traps
> * **0-indexed vs 1-indexed:** Be extremely careful on exams. 
>   * *0-indexed:* Left child is `2i + 1`, Right is `2i + 2`. Parent is `floor((i-1)/2)`.
>   * *1-indexed:* Left child is `2i`, Right is `2i + 1`. Parent is `floor(i/2)`.
> * **Sift-down propagation:** Don't stop after one swap. You must follow the swapped node down the tree until it's larger than both children or becomes a leaf.

---

## 4. Graph Algorithms: Prim's (MST) & Dijkstra's (Shortest Path)

### Prim's Algorithm (Minimum Spanning Tree)
**Goal:** Find a subset of edges that connects all vertices with the minimum total edge weight.

1. **Initialize:** Create a set of visited vertices `V = {}`. Pick an arbitrary starting vertex and add it to `V`.
2. **Iterate:** Look at all edges connecting any vertex *inside* `V` to any vertex *outside* `V`.
3. **Select:** Pick the edge with the absolute lowest weight. 
4. **Update:** Add the destination vertex to `V` and add the edge to your MST.
5. **Repeat:** Continue until all vertices are in `V`.

### Dijkstra's Algorithm (Shortest Path)
**Goal:** Find the shortest path from a starting node to all other nodes.

1. **Initialize Table:** Create a table with columns: `Vertex`, `Shortest Distance from Source`, `Previous Vertex`. Set distance to Source as `0` and all others to `Infinity`. 
2. **Current Node:** Mark all nodes unvisited. Set the source node as the "current node".
3. **Relax Edges:** For the current node, look at all unvisited neighbors. Calculate the tentative distance: `Distance to Current Node` + `Edge Weight`.
    * If `tentative distance` < `current known distance` for that neighbor, update the table with the new distance and set `Previous Vertex` to the current node.
4. **Mark Visited:** Once all neighbors are checked, mark the current node as visited. (It will never be checked again).
5. **Select Next:** Pick the unvisited node with the smallest `Shortest Distance` in your table. Set it as the new current node and go back to step 3.

> [!warning] Edge Cases & Traps
> * Dijkstra's **cannot** handle negative edge weights.
> * In Dijkstra's, you only update the distance if the *cumulative* path is shorter, not just the single edge.

---

## 5. Quick Sort (Median-of-Three Partitioning)

**Goal:** Partition an array around a pivot such that left elements are smaller and right elements are larger.

### Step-by-Step Procedure
1. **Find Pivot:** Look at the First, Middle, and Last elements of the array (or sub-array). Sort these three elements. The median value becomes the Pivot.
2. **Hide Pivot:** Swap the Pivot with the element at the `Second-to-Last` position (this gets it out of the way for the partition logic).
3. **Initialize Pointers:** * `i` starts at the second element (`left + 1`).
    * `j` starts at the third-to-last element (`right - 2`).
4. **Partition Loop:**
    * Move `i` right while `array[i] < pivot`.
    * Move `j` left while `array[j] > pivot`.
    * If `i < j`, swap `array[i]` and `array[j]`. Move `i` right and `j` left.
    * If `i >= j`, stop the loop.
5. **Restore Pivot:** Swap the Pivot (at `right - 1`) with `array[i]`. `i` is now the final, correct position of the Pivot.

### 📝 Worked Example
**Array:** `[1, 30, 3, 12, 53, 62, 14, 32, 41, 49]`
1. **Candidates:** First (1), Mid (53), Last (49). 
2. **Median:** 49. (Pivot = 49).
3. **Hide Pivot:** Swap 49 to the end (or second to last, depending on textbook implementation. If standard exam traces just put it at the end, swap 49 and 49 — it's already there).
4. **Partition:** Compare elements from left to right against 49.
    * 1 < 49 (stay)
    * 30 < 49 (stay)
    * 3 < 49 (stay)
    * 12 < 49 (stay)
    * 53 > 49 (needs to move right)
    * 62 > 49 (needs to move right)
    * 14 < 49 (stay/swap with left elements)
    * 32 < 49 (stay/swap)
    * 41 < 49 (stay/swap)
5. **Resulting split:** Values less than 49 group on the left, values greater group on the right. Pivot 49 goes in the middle.
