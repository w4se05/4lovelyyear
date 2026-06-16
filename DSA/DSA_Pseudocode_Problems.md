---
tags: [dsa, pseudocode-problems, 61CSE108, applied-algorithms]
aliases: [DSA Pseudocode Bank]
topic: "Pseudocode Problems — 61CSE108: Algorithms and Data Structures"
course: "61CSE108: Algorithms and Data Structures"
created: 2026-06-03
---

# ✍️ DSA Pseudocode Problems

> [!info] How to Use This Sheet
> Every problem requires you to **write pseudocode** — not just recall facts. Cover the solution block, attempt on paper, then expand. For each solution, complexity analysis is given separately so you can check your algorithm before checking the cost. Notation follows the lecture: 0-indexed arrays, `NULL` for empty pointers, and language-agnostic pseudocode.

---

## 🧱 Module 1 — [[Stack and Queue]]

### Using a Stack

> [!question] Q1.1 — Reverse a Linked List Using a Stack
> You are given a singly linked list with head pointer `pHead`. Write pseudocode to **reverse** the list **in-place** using a stack as auxiliary storage. Do **not** allocate new nodes.
>
> **Prototype:** `ReverseWithStack(pHead) → pHead`
>
> **Example:** `1 → 2 → 3 → 4 → NULL` becomes `4 → 3 → 2 → 1 → NULL`

> [!success]- Solution
> **Idea:** Push all node pointers onto a stack. Pop them in reverse order, relinking the `pNext` pointers.
>
> ```
> ReverseWithStack(pHead):
>     if pHead = NULL or pHead.pNext = NULL:
>         return pHead
>
>     s ← empty Stack
>     p ← pHead
>     while p ≠ NULL:
>         s.push(p)
>         p ← p.pNext
>
>     newHead ← s.pop()
>     cur ← newHead
>     while s is not empty:
>         cur.pNext ← s.pop()
>         cur ← cur.pNext
>     cur.pNext ← NULL        // former head must point to NULL
>
>     return newHead
> ```
>
> **Complexity:** $O(n)$ time, $O(n)$ space (stack holds $n$ pointers).
>
> > [!note] The key trap is the last step — `cur.pNext ← NULL`. Without it, the former head still points to its old successor, creating a cycle.

---

> [!question] Q1.2 — Check Palindrome Using a Stack
> Write pseudocode to determine whether a singly linked list of characters forms a **palindrome** (reads the same forwards and backwards).
>
> **Prototype:** `IsPalindrome(pHead) → Boolean`
>
> **Example:** `a → b → c → b → a` → `True` &nbsp;|&nbsp; `a → b → c` → `False`

> [!success]- Solution
> **Idea:** Push all characters onto a stack. Then traverse the list again from the head; at each step, compare the current node's value with the popped value from the stack.
>
> ```
> IsPalindrome(pHead):
>     s ← empty Stack
>     p ← pHead
>     while p ≠ NULL:
>         s.push(p.Info)
>         p ← p.pNext
>
>     p ← pHead
>     while p ≠ NULL:
>         if p.Info ≠ s.pop():
>             return False
>         p ← p.pNext
>
>     return True
> ```
>
> **Complexity:** $O(n)$ time, $O(n)$ space.
>
> **Optimised variant (only push half):** Find the midpoint with the fast/slow pointer trick (see Q4.1), push only the second half, compare with the first half → $O(n)$ time, $O(n/2)$ space.

---

### Building Queues from Stacks

> [!question] Q1.3 — Implement a Queue Using Two Stacks ⭐
> Using **only two stacks** `S1` and `S2` (each with standard `push`, `pop`, `peek`, `isEmpty`), implement a queue with operations `Enqueue(x)` and `Dequeue()`.
>
> **Constraints:** No other data structures. Both stacks hold integers.

> [!success]- Solution
> **Idea:**
> - `S1` is the **inbox** — all enqueues go here.
> - `S2` is the **outbox** — all dequeues come from here.
> - When `S2` is empty and a dequeue is requested, dump the entirety of `S1` into `S2` (this reverses the order, making the oldest element the new top of `S2`).
>
> ```
> Enqueue(x):
>     S1.push(x)
>
> Dequeue():
>     if S2.isEmpty():
>         if S1.isEmpty():
>             error "Queue is empty"
>         while not S1.isEmpty():
>             S2.push(S1.pop())
>     return S2.pop()
>
> Peek():
>     if S2.isEmpty():
>         if S1.isEmpty():
>             error "Queue is empty"
>         while not S1.isEmpty():
>             S2.push(S1.pop())
>     return S2.peek()
>
> IsEmpty():
>     return S1.isEmpty() and S2.isEmpty()
> ```
>
> **Complexity:**
> - `Enqueue`: $O(1)$ always.
> - `Dequeue`: $O(n)$ worst case (when `S2` is empty and `S1` has $n$ elements), but **amortised $O(1)$** — each element is pushed and popped exactly once across both stacks.

---

> [!question] Q1.4 — Implement a Stack Using Two Queues ⭐
> Using **only two queues** `Q1` and `Q2` (each with standard `Enqueue`, `Dequeue`, `Peek`, `IsEmpty`), implement a stack with `Push(x)` and `Pop()`.

> [!success]- Solution
> **Idea (Push-costly variant):**
> When pushing a new element, enqueue it into the empty `Q2`, then move all of `Q1` into `Q2`. Finally swap names: `Q1 ↔ Q2`. The front of `Q1` always holds the most recently pushed element.
>
> ```
> Push(x):
>     Q2.Enqueue(x)                  // new element goes to Q2 first
>     while not Q1.IsEmpty():
>         Q2.Enqueue(Q1.Dequeue())   // pour Q1 behind x
>     swap(Q1, Q2)                   // Q1 is now the "live" queue
>
> Pop():
>     if Q1.IsEmpty():
>         error "Stack is empty"
>     return Q1.Dequeue()
>
> Peek():
>     if Q1.IsEmpty():
>         error "Stack is empty"
>     return Q1.Peek()               // front of Q1 = top of stack
>
> IsEmpty():
>     return Q1.IsEmpty()
> ```
>
> **Complexity:**
> - `Push`: $O(n)$ — copies all $n$ existing elements.
> - `Pop` / `Peek`: $O(1)$.
>
> > [!note] **Alternative (Pop-costly):** Always enqueue into Q1. On pop, move all but the last element to Q2, dequeue the last from Q1, then swap. Pop = $O(n)$, Push = $O(1)$.

---

> [!question] Q1.5 — Min-Stack: Stack That Supports O(1) getMin()
> Design a stack that, in addition to standard `push` and `pop`, supports `getMin()` — returning the current minimum element — **all in $O(1)$ time**.

> [!success]- Solution
> **Idea:** Maintain a second "tracking" stack `minS` that mirrors the main stack but stores the **running minimum** at each level.
>
> ```
> Push(x):
>     mainS.push(x)
>     if minS.isEmpty() or x ≤ minS.peek():
>         minS.push(x)
>     else:
>         minS.push(minS.peek())     // duplicate current min
>
> Pop():
>     if mainS.isEmpty():
>         error "Stack is empty"
>     minS.pop()
>     return mainS.pop()
>
> getMin():
>     if mainS.isEmpty():
>         error "Stack is empty"
>     return minS.peek()
> ```
>
> **Example trace** pushing `[3, 5, 2, 4, 1]`:
>
> | Op | mainS | minS | getMin() |
> |----|-------|------|----------|
> | push(3) | [3] | [3] | 3 |
> | push(5) | [3,5] | [3,3] | 3 |
> | push(2) | [3,5,2] | [3,3,2] | 2 |
> | push(4) | [3,5,2,4] | [3,3,2,2] | 2 |
> | push(1) | [3,5,2,4,1] | [3,3,2,2,1] | 1 |
> | pop() | [3,5,2,4] | [3,3,2,2] | 2 |
>
> **Complexity:** All operations $O(1)$. Space $O(n)$ for `minS`.

---

## 🔗 Module 2 — [[Linked Lists]]

> [!question] Q2.1 — Detect a Cycle in a Linked List (Floyd's Algorithm) ⭐
> Write pseudocode to determine whether a singly linked list contains a **cycle** (i.e., some node's `pNext` points back to an earlier node). Return `True` if a cycle exists, `False` otherwise. **No extra memory allowed.**
>
> **Prototype:** `HasCycle(pHead) → Boolean`

> [!success]- Solution
> **Idea (Floyd's Tortoise and Hare):** Use two pointers — `slow` advances 1 step per iteration, `fast` advances 2. If they ever point to the **same node**, there is a cycle. If `fast` reaches `NULL`, there is no cycle.
>
> ```
> HasCycle(pHead):
>     if pHead = NULL or pHead.pNext = NULL:
>         return False
>
>     slow ← pHead
>     fast ← pHead
>
>     while fast ≠ NULL and fast.pNext ≠ NULL:
>         slow ← slow.pNext
>         fast ← fast.pNext.pNext
>         if slow = fast:
>             return True
>
>     return False
> ```
>
> **Complexity:** $O(n)$ time, $O(1)$ space.
>
> > [!note] **Why it works:** If there is a cycle of length $c$, once `fast` enters the cycle it gains 1 step on `slow` each iteration. They will meet within at most $c$ steps after both enter the cycle.

---

> [!question] Q2.2 — Merge Two Sorted Linked Lists
> Given two sorted singly linked lists with head pointers `pA` and `pB`, write pseudocode to merge them into a single sorted linked list. **Do not allocate new nodes** — reuse existing nodes by relinking.
>
> **Prototype:** `MergeSorted(pA, pB) → pHead`
>
> **Example:** `1→3→5` and `2→4→6` → `1→2→3→4→5→6`

> [!success]- Solution
> **Idea:** Use a dummy sentinel head node to avoid special-casing the first element. At each step, pick the smaller of `pA.Info` and `pB.Info`, attach it to the result list, and advance the chosen pointer.
>
> ```
> MergeSorted(pA, pB):
>     dummy ← new Node(0)    // sentinel; won't appear in output
>     cur ← dummy
>
>     while pA ≠ NULL and pB ≠ NULL:
>         if pA.Info ≤ pB.Info:
>             cur.pNext ← pA
>             pA ← pA.pNext
>         else:
>             cur.pNext ← pB
>             pB ← pB.pNext
>         cur ← cur.pNext
>
>     // Attach the remaining non-empty list
>     if pA ≠ NULL:
>         cur.pNext ← pA
>     else:
>         cur.pNext ← pB
>
>     return dummy.pNext
> ```
>
> **Complexity:** $O(m + n)$ time where $m = |A|$, $n = |B|$. $O(1)$ extra space (only the dummy node).

---

> [!question] Q2.3 — Remove All Occurrences of a Value from a Linked List
> Write pseudocode to remove **every node** whose `Info` equals a given value `k` from a singly linked list. Handle edge cases: value at head, multiple consecutive occurrences, value not present.
>
> **Prototype:** `RemoveAll(pHead, k) → pHead`

> [!success]- Solution
> **Idea:** Use a dummy sentinel before `pHead` to eliminate the special case for head deletion. Traverse with a `prev` pointer; skip nodes that match `k`.
>
> ```
> RemoveAll(pHead, k):
>     dummy ← new Node(0)
>     dummy.pNext ← pHead
>     prev ← dummy
>
>     while prev.pNext ≠ NULL:
>         if prev.pNext.Info = k:
>             toDelete ← prev.pNext
>             prev.pNext ← toDelete.pNext
>             delete toDelete          // free memory
>             // do NOT advance prev — new prev.pNext must also be checked
>         else:
>             prev ← prev.pNext
>
>     return dummy.pNext
> ```
>
> **Complexity:** $O(n)$ time, $O(1)$ space.

---

> [!question] Q2.4 — Find the Intersection Node of Two Linked Lists ⭐
> Two singly linked lists may **share a common tail** from some node onward (Y-shaped merge). Write pseudocode to find the **first shared node**. Return `NULL` if they do not intersect.
>
> **Prototype:** `FindIntersection(pA, pB) → Node`
>
> **Constraint:** $O(n)$ time, $O(1)$ space.

> [!success]- Solution
> **Idea:** If the lists have lengths $m$ and $n$ ($m \geq n$), advance the longer list's pointer by $|m - n|$ steps first, then walk both pointers in lockstep. The first node where they are equal is the intersection.
>
> ```
> FindIntersection(pA, pB):
>     if pA = NULL or pB = NULL:
>         return NULL
>
>     // Step 1: compute lengths
>     lenA ← 0;  p ← pA
>     while p ≠ NULL: lenA ← lenA + 1;  p ← p.pNext
>
>     lenB ← 0;  p ← pB
>     while p ≠ NULL: lenB ← lenB + 1;  p ← p.pNext
>
>     // Step 2: align starting positions
>     pCurA ← pA;  pCurB ← pB
>     while lenA > lenB:
>         pCurA ← pCurA.pNext;  lenA ← lenA - 1
>     while lenB > lenA:
>         pCurB ← pCurB.pNext;  lenB ← lenB - 1
>
>     // Step 3: walk in lockstep
>     while pCurA ≠ pCurB:
>         pCurA ← pCurA.pNext
>         pCurB ← pCurB.pNext
>
>     return pCurA     // NULL if no intersection
> ```
>
> **Complexity:** $O(m + n)$ time, $O(1)$ space.

---

## 🔢 Module 3 — [[Sorting Algorithms]]

> [!question] Q3.1 — Sort a Linked List Using Merge Sort
> Write pseudocode to **sort** a singly linked list in ascending order using **Merge Sort**. You may use the `MergeSorted` function from Q2.2.
>
> **Prototype:** `MergeSortList(pHead) → pHead`

> [!success]- Solution
> **Idea:** Find the midpoint (fast/slow pointers), split into two halves, recursively sort each half, then merge.
>
> ```
> MergeSortList(pHead):
>     // Base case: 0 or 1 node
>     if pHead = NULL or pHead.pNext = NULL:
>         return pHead
>
>     // Step 1: find mid and split
>     slow ← pHead
>     fast ← pHead.pNext      // offset by 1 so slow lands at LEFT mid
>     while fast ≠ NULL and fast.pNext ≠ NULL:
>         slow ← slow.pNext
>         fast ← fast.pNext.pNext
>     // slow is now the last node of the left half
>     mid ← slow.pNext
>     slow.pNext ← NULL        // cut the list in two
>
>     // Step 2: recursively sort both halves
>     leftSorted  ← MergeSortList(pHead)
>     rightSorted ← MergeSortList(mid)
>
>     // Step 3: merge
>     return MergeSorted(leftSorted, rightSorted)
> ```
>
> **Complexity:** $O(n \log n)$ time (same recurrence as array Merge Sort). $O(\log n)$ space for the recursion call stack.

---

> [!question] Q3.2 — Dutch National Flag — 3-Way Partition ⭐
> Given an array $A[0..n-1]$ containing only values `0`, `1`, and `2`, sort it **in-place in $O(n)$ time and $O(1)$ space** so all `0`s come first, then `1`s, then `2`s.
>
> **Prototype:** `DutchFlag(A, n)`
>
> **Example:** `[2,0,1,2,0,1,1]` → `[0,0,1,1,1,2,2]`

> [!success]- Solution
> **Idea (three-pointer invariant):**
> Maintain three regions: `[0..lo-1]` = all 0s, `[lo..mid-1]` = all 1s, `[hi+1..n-1]` = all 2s. The range `[mid..hi]` is unexplored.
>
> ```
> DutchFlag(A, n):
>     lo  ← 0
>     mid ← 0
>     hi  ← n - 1
>
>     while mid ≤ hi:
>         if A[mid] = 0:
>             Swap(A, lo, mid)
>             lo  ← lo  + 1
>             mid ← mid + 1
>         else if A[mid] = 1:
>             mid ← mid + 1
>         else:                      // A[mid] = 2
>             Swap(A, mid, hi)
>             hi ← hi - 1
>             // do NOT increment mid — the swapped element is unexamined
> ```
>
> **Complexity:** $O(n)$ time, $O(1)$ space. Each element is examined at most once.
>
> > [!note] This is essentially a 3-way Quick Sort partition. Notice that when swapping with `hi`, `mid` does **not** advance — the incoming element from position `hi` hasn't been examined yet.

---

> [!question] Q3.3 — K-th Largest Element Using a Min-Heap of Size K
> Write pseudocode to find the **$k$-th largest** element in an unsorted array $A[0..n-1]$ using a min-heap of maximum size $k$. You may use `HeapInsert(H, val)`, `ExtractMin(H)`, `HeapMin(H)`, and `HeapSize(H)`.
>
> **Prototype:** `KthLargest(A, n, k) → integer`

> [!success]- Solution
> **Idea:** Maintain a min-heap of the $k$ largest elements seen so far. For each new element, if it is larger than the current minimum (= `HeapMin`), evict the min and insert the new element. At the end, `HeapMin` is the $k$-th largest.
>
> ```
> KthLargest(A, n, k):
>     H ← empty min-heap
>
>     for i ← 0 to n-1:
>         if HeapSize(H) < k:
>             HeapInsert(H, A[i])
>         else if A[i] > HeapMin(H):
>             ExtractMin(H)
>             HeapInsert(H, A[i])
>
>     return HeapMin(H)
> ```
>
> **Complexity:** $O(n \log k)$ time — each of the $n$ elements triggers at most one `ExtractMin` + `HeapInsert`, each costing $O(\log k)$.

---

## 🗂️ Module 4 — [[Hashing]]

> [!question] Q4.1 — Check if Two Strings Are Anagrams Using Hashing
> Write pseudocode to determine if strings `s` and `t` are **anagrams** (same characters with the same frequencies, in any order) using a hash map as a frequency counter. Do not sort.
>
> **Prototype:** `IsAnagram(s, t) → Boolean`

> [!success]- Solution
> **Idea:** Use a hash map `freq` keyed by character. Increment for every char in `s`, decrement for every char in `t`. If all values are 0 at the end, they are anagrams.
>
> ```
> IsAnagram(s, t):
>     if length(s) ≠ length(t):
>         return False
>
>     freq ← empty hash map (default value 0)
>
>     for each character c in s:
>         freq[c] ← freq[c] + 1
>
>     for each character c in t:
>         freq[c] ← freq[c] - 1
>         if freq[c] < 0:
>             return False    // t has more of c than s
>
>     return True
> ```
>
> **Complexity:** $O(n)$ time where $n = |s| = |t|$. $O(\sigma)$ space where $\sigma$ = alphabet size (≤ 26 for lowercase Latin).

---

> [!question] Q4.2 — Two-Sum: Find Pair with Target Sum Using Hashing ⭐
> Given array $A[0..n-1]$ of integers and a target value `T`, write pseudocode to return the **indices** $(i, j)$ such that $A[i] + A[j] = T$ and $i \neq j$. Return $(-1, -1)$ if no such pair exists. Do **not** sort the array.
>
> **Prototype:** `TwoSum(A, n, T) → (int, int)`

> [!success]- Solution
> **Idea:** For each element $A[i]$, the required complement is `T - A[i]`. Use a hash map to store `value → index` for all previously seen elements.
>
> ```
> TwoSum(A, n, T):
>     seen ← empty hash map    // maps value → index
>
>     for i ← 0 to n-1:
>         complement ← T - A[i]
>         if complement exists in seen:
>             return (seen[complement], i)
>         seen[A[i]] ← i
>
>     return (-1, -1)
> ```
>
> **Example:** $A = [2, 7, 11, 15]$, $T = 9$
> - $i=0$: complement = 7, not in seen. seen = {2:0}
> - $i=1$: complement = 2, **found at index 0**. Return **(0, 1)**. ✓
>
> **Complexity:** $O(n)$ time, $O(n)$ space.

---

> [!question] Q4.3 — Find the First Non-Repeating Character
> Given a string `s`, find the **first character** that appears exactly once. Return the character, or `'\0'` if all characters repeat.
>
> **Prototype:** `FirstUnique(s) → char`

> [!success]- Solution
> **Idea:** Two-pass approach — first pass builds a frequency hash map, second pass finds the first character with frequency 1.
>
> ```
> FirstUnique(s):
>     freq ← empty hash map (default 0)
>
>     // Pass 1: count frequencies
>     for each character c in s:
>         freq[c] ← freq[c] + 1
>
>     // Pass 2: find first with freq = 1 (order preserved by iterating s)
>     for each character c in s:
>         if freq[c] = 1:
>             return c
>
>     return '\0'
> ```
>
> **Complexity:** $O(n)$ time, $O(\sigma)$ space.
>
> > [!note] Iterating `s` in Pass 2 (rather than the hash map) is essential — hash maps do **not** preserve insertion order in general. Iterating `s` gives the correct "first in string" ordering.

---

## 🌳 Module 5 — [[Trees]] and [[BST]] and [[AVL Trees]]

> [!question] Q5.1 — Level-Order (BFS) Traversal of a Binary Tree
> Write pseudocode to print all nodes of a binary tree **level by level**, left to right. Use a queue.
>
> **Prototype:** `LevelOrder(root)`
>
> **Example tree:**
> ```
>        1
>       / \
>      2   3
>     / \   \
>    4   5   6
> ```
> **Output:** `1 2 3 4 5 6`

> [!success]- Solution
> ```
> LevelOrder(root):
>     if root = NULL: return
>
>     Q ← empty Queue
>     Q.Enqueue(root)
>
>     while not Q.IsEmpty():
>         node ← Q.Dequeue()
>         print node.value
>
>         if node.left ≠ NULL:
>             Q.Enqueue(node.left)
>         if node.right ≠ NULL:
>             Q.Enqueue(node.right)
> ```
>
> **Complexity:** $O(n)$ time, $O(w)$ space where $w$ = maximum width of the tree (at most $n/2$ for a complete binary tree).

---

> [!question] Q5.2 — Print a Binary Tree Level by Level, One Line Per Level ⭐
> Extend Q5.1 so that nodes at each level are printed on a **separate line**.
>
> **Output for example above:**
> ```
> 1
> 2 3
> 4 5 6
> ```

> [!success]- Solution
> **Idea:** Track the **count of nodes in the current level**. Process exactly that many nodes before printing a newline and counting the next level.
>
> ```
> LevelOrderLines(root):
>     if root = NULL: return
>
>     Q ← empty Queue
>     Q.Enqueue(root)
>
>     while not Q.IsEmpty():
>         levelSize ← Q.Size()        // number of nodes in this level
>
>         for i ← 1 to levelSize:
>             node ← Q.Dequeue()
>             print node.value, " "
>
>             if node.left  ≠ NULL: Q.Enqueue(node.left)
>             if node.right ≠ NULL: Q.Enqueue(node.right)
>
>         print newline
> ```
>
> **Complexity:** $O(n)$ time, $O(w)$ space.

---

> [!question] Q5.3 — Check if a Binary Tree is a Valid BST ⭐
> Write pseudocode to determine whether a given binary tree satisfies the **BST ordering invariant** at every node (not just parent-child, but the full subtree constraint).
>
> **Prototype:** `IsValidBST(root) → Boolean`

> [!success]- Solution
> **Wrong approach (common mistake):** Only checking `node.left.value < node.value < node.right.value` at each node fails — a left-subtree node could still violate the global BST property.
>
> **Correct approach:** Pass valid `(min, max)` bounds down the tree. Each node must satisfy `min < node.value < max`.
>
> ```
> IsValidBST(root):
>     return CheckBST(root, -∞, +∞)
>
> CheckBST(node, minVal, maxVal):
>     if node = NULL:
>         return True
>     if node.value ≤ minVal or node.value ≥ maxVal:
>         return False
>     return CheckBST(node.left,  minVal,      node.value) and
>            CheckBST(node.right, node.value,  maxVal)
> ```
>
> **Complexity:** $O(n)$ time (visits every node once), $O(h)$ space for the recursion stack.
>
> > [!note] **Why bounds?** Consider:
> > ```
> >    5
> >   / \
> >  1   8
> >     / \
> >    6   9
> > ```
> > Node 6 satisfies `parent(8): 6 < 8` ✓ but violates the root constraint `6 > 5` ✓... actually this IS valid. Counter-example:
> > ```
> >    5
> >   / \
> >  1   8
> >     / \
> >    3   9    ← 3 < 5, violates BST
> > ```
> > Parent-only check would pass node 3 (3 < 8), but the bounds check catches it (3 must be > 5).

---

> [!question] Q5.4 — BST: Find Lowest Common Ancestor (LCA)
> Given a BST and two values `p` and `q` (both guaranteed to exist in the tree), find their **Lowest Common Ancestor** — the deepest node that is an ancestor of both `p` and `q`.
>
> **Prototype:** `LCA(root, p, q) → Node`

> [!success]- Solution
> **Idea:** Exploit the BST property. At any node:
> - If both `p` and `q` are less than `node.value` → LCA is in the left subtree.
> - If both are greater → LCA is in the right subtree.
> - Otherwise (one on each side, or one equals `node.value`) → current node IS the LCA.
>
> ```
> LCA(root, p, q):
>     node ← root
>     while node ≠ NULL:
>         if p < node.value and q < node.value:
>             node ← node.left
>         else if p > node.value and q > node.value:
>             node ← node.right
>         else:
>             return node     // split point = LCA
>     return NULL
> ```
>
> **Complexity:** $O(h)$ time where $h$ = height. $O(1)$ space (iterative).

---

> [!question] Q5.5 — Build a BST from a Sorted Array (Balanced)
> Given a **sorted** array $A[0..n-1]$, write pseudocode to build a **height-balanced BST** (i.e., a BST whose height is $\lfloor \log_2 n \rfloor$). Return the root.
>
> **Prototype:** `SortedArrayToBST(A, left, right) → Node`

> [!success]- Solution
> **Idea:** Always pick the **middle element** as the root. Recurse on the left and right halves. This guarantees the resulting BST has minimum height.
>
> ```
> SortedArrayToBST(A, left, right):
>     if left > right:
>         return NULL
>
>     mid ← (left + right) / 2
>     node ← new Node(A[mid])
>     node.left  ← SortedArrayToBST(A, left,   mid - 1)
>     node.right ← SortedArrayToBST(A, mid + 1, right)
>     return node
>
> // Caller:
> root ← SortedArrayToBST(A, 0, n-1)
> ```
>
> **Complexity:** $O(n)$ time (each element visited once), $O(\log n)$ space (call stack depth = tree height).

---

## 🕸️ Module 6 — [[Graphs]]

> [!question] Q6.1 — Iterative DFS Using a Stack
> Write pseudocode to perform an iterative (non-recursive) **DFS** of a graph $G = (V, E)$ represented as an adjacency list, starting from vertex `start`. Print each vertex when first visited.
>
> **Prototype:** `DFS_Iterative(G, start)`

> [!success]- Solution
> ```
> DFS_Iterative(G, start):
>     visited[v] ← False  for all v in V
>     S ← empty Stack
>
>     S.push(start)
>
>     while not S.isEmpty():
>         v ← S.pop()
>         if not visited[v]:
>             visited[v] ← True
>             print v
>             // push neighbors in reverse order to preserve natural DFS order
>             for each neighbor u of v in G (in reverse adjacency order):
>                 if not visited[u]:
>                     S.push(u)
> ```
>
> **Complexity:** $O(|V| + |E|)$ time, $O(|V|)$ space.
>
> > [!warning] The iterative version may visit nodes in a different order than the recursive version if neighbors are pushed without reversing. This is implementation-dependent but both are valid DFS traversals.

---

> [!question] Q6.2 — Detect a Cycle in a Directed Graph Using DFS ⭐
> Write pseudocode to detect whether a **directed** graph $G$ contains a cycle. Use DFS with a "recursion stack" to distinguish back-edges (which indicate cycles) from cross-edges.
>
> **Prototype:** `HasCycleDirected(G) → Boolean`

> [!success]- Solution
> **Idea:** DFS with three states per vertex: `WHITE` (unvisited), `GRAY` (in current DFS path / on recursion stack), `BLACK` (fully explored). A back-edge from a `GRAY` node's neighbor to another `GRAY` node indicates a cycle.
>
> ```
> HasCycleDirected(G):
>     color[v] ← WHITE  for all v in V
>
>     for each vertex v in V:
>         if color[v] = WHITE:
>             if DFSVisit(G, v, color):
>                 return True
>     return False
>
> DFSVisit(G, v, color):
>     color[v] ← GRAY           // mark as "on current path"
>
>     for each neighbor u of v:
>         if color[u] = GRAY:
>             return True        // back-edge → cycle found
>         if color[u] = WHITE:
>             if DFSVisit(G, u, color):
>                 return True
>
>     color[v] ← BLACK          // fully explored, remove from path
>     return False
> ```
>
> **Complexity:** $O(|V| + |E|)$ time, $O(|V|)$ space.

---

> [!question] Q6.3 — BFS Shortest Path — Reconstruct the Path ⭐
> Write pseudocode to find the **shortest path** (fewest edges) from vertex `src` to vertex `dst` in an **unweighted** graph. Return the path as a list of vertices, or an empty list if unreachable.
>
> **Prototype:** `BFSPath(G, src, dst) → List`

> [!success]- Solution
> **Idea:** Standard BFS, but additionally store a `parent[]` array to reconstruct the path by backtracking from `dst` to `src`.
>
> ```
> BFSPath(G, src, dst):
>     dist[v]   ← ∞    for all v
>     parent[v] ← NULL for all v
>     dist[src] ← 0
>
>     Q ← empty Queue
>     Q.Enqueue(src)
>
>     while not Q.IsEmpty():
>         v ← Q.Dequeue()
>         if v = dst: break
>         for each neighbor u of v:
>             if dist[u] = ∞:
>                 dist[u]   ← dist[v] + 1
>                 parent[u] ← v
>                 Q.Enqueue(u)
>
>     // Reconstruct path
>     if dist[dst] = ∞:
>         return []               // unreachable
>
>     path ← empty List
>     cur ← dst
>     while cur ≠ NULL:
>         path.prepend(cur)       // insert at front
>         cur ← parent[cur]
>     return path
> ```
>
> **Complexity:** $O(|V| + |E|)$ time, $O(|V|)$ space.

---

> [!question] Q6.4 — Topological Sort of a DAG Using DFS
> Write pseudocode to produce a **topological ordering** of a Directed Acyclic Graph (DAG). A topological order is a linear ordering of all vertices such that for every directed edge $(u, v)$, $u$ comes before $v$.
>
> **Prototype:** `TopologicalSort(G) → List`

> [!success]- Solution
> **Idea:** Run DFS; when a vertex is **fully explored** (all descendants visited), push it onto a stack. The final reverse of this stack (or popping the stack) gives the topological order.
>
> ```
> TopologicalSort(G):
>     visited[v] ← False  for all v
>     S ← empty Stack
>
>     for each vertex v in V:
>         if not visited[v]:
>             TopoVisit(G, v, visited, S)
>
>     result ← empty List
>     while not S.isEmpty():
>         result.append(S.pop())
>     return result
>
> TopoVisit(G, v, visited, S):
>     visited[v] ← True
>     for each neighbor u of v:
>         if not visited[u]:
>             TopoVisit(G, u, visited, S)
>     S.push(v)      // push AFTER all descendants are processed
> ```
>
> **Complexity:** $O(|V| + |E|)$ time, $O(|V|)$ space.

---

## ⚙️ Module 7 — [[Dynamic Programming]]

> [!question] Q7.1 — Fibonacci with Memoization vs Bottom-Up DP
> Write **both** a top-down (memoized recursive) and a bottom-up (iterative DP) pseudocode to compute the $n$-th Fibonacci number. Compare their complexities.
>
> **Prototype:** `Fib(n) → integer`

> [!success]- Solution
> **Top-Down (Memoization):**
> ```
> memo ← array of size n+1, initialized to -1
>
> FibMemo(n):
>     if n ≤ 1: return n
>     if memo[n] ≠ -1: return memo[n]
>     memo[n] ← FibMemo(n-1) + FibMemo(n-2)
>     return memo[n]
> ```
>
> **Bottom-Up (Tabulation):**
> ```
> FibDP(n):
>     if n ≤ 1: return n
>     dp ← array of size n+1
>     dp[0] ← 0;  dp[1] ← 1
>     for i ← 2 to n:
>         dp[i] ← dp[i-1] + dp[i-2]
>     return dp[n]
> ```
>
> **Space-Optimised Bottom-Up (only $O(1)$ space):**
> ```
> FibOptimal(n):
>     if n ≤ 1: return n
>     prev2 ← 0;  prev1 ← 1
>     for i ← 2 to n:
>         cur  ← prev1 + prev2
>         prev2 ← prev1
>         prev1 ← cur
>     return prev1
> ```
>
> | Version | Time | Space |
> |---------|------|-------|
> | Naïve recursion | $O(2^n)$ | $O(n)$ |
> | Top-down memo | $O(n)$ | $O(n)$ |
> | Bottom-up DP | $O(n)$ | $O(n)$ |
> | Space-optimised | $O(n)$ | $O(1)$ |

---

> [!question] Q7.2 — Coin Change: Minimum Coins (Unbounded) ⭐
> Given coins of denominations `coins[1..m]` and a target amount `T`, write pseudocode to find the **minimum number of coins** needed to make exactly `T`. Each coin can be used unlimited times. Return $\infty$ if impossible.
>
> **Prototype:** `MinCoins(coins, m, T) → integer`

> [!success]- Solution
> **Subproblem:** Let `dp[w]` = minimum coins needed to make amount `w`.
>
> **Recurrence:**
> $$dp[w] = \min_{1 \leq i \leq m,\; coins[i] \leq w} \bigl(1 + dp[w - coins[i]]\bigr)$$
>
> **Base case:** `dp[0] = 0`, `dp[w] = ∞` for `w > 0` initially.
>
> ```
> MinCoins(coins, m, T):
>     dp ← array of size T+1, initialized to ∞
>     dp[0] ← 0
>
>     for w ← 1 to T:
>         for i ← 1 to m:
>             if coins[i] ≤ w and dp[w - coins[i]] ≠ ∞:
>                 dp[w] ← min(dp[w], 1 + dp[w - coins[i]])
>
>     return dp[T]
> ```
>
> **Complexity:** $O(T \cdot m)$ time, $O(T)$ space.
>
> > [!note] To reconstruct which coins were used, maintain a `choice[w]` array storing the coin used at each step, then backtrack from `choice[T]`.

---

> [!question] Q7.3 — Longest Increasing Subsequence (LIS) ⭐
> Given array $A[0..n-1]$, write pseudocode to find the **length** of the longest strictly increasing subsequence.
>
> **Example:** $A = [10, 9, 2, 5, 3, 7, 101, 18]$ → LIS length = **4** (e.g., `2, 3, 7, 101`)
>
> **Prototype:** `LIS(A, n) → integer`

> [!success]- Solution
> **Subproblem:** Let `dp[i]` = length of the LIS **ending at index $i$**.
>
> **Recurrence:**
> $$dp[i] = 1 + \max_{j < i,\; A[j] < A[i]} dp[j] \quad \text{(or 1 if no such } j\text{)}$$
>
> **Answer:** $\max_{0 \leq i \leq n-1} dp[i]$
>
> ```
> LIS(A, n):
>     dp ← array of size n, all initialized to 1
>     // dp[i] = 1 means at minimum A[i] alone is a subsequence of length 1
>
>     for i ← 1 to n-1:
>         for j ← 0 to i-1:
>             if A[j] < A[i]:
>                 dp[i] ← max(dp[i], dp[j] + 1)
>
>     best ← 0
>     for i ← 0 to n-1:
>         best ← max(best, dp[i])
>     return best
> ```
>
> **Complexity:** $O(n^2)$ time, $O(n)$ space.
>
> > [!note] An $O(n \log n)$ solution exists using binary search + patience sorting, but this $O(n^2)$ DP formulation is the one directly derivable from the course's DP framework (same structure as LCS and Knapsack).

---

> [!question] Q7.4 — Edit Distance (Levenshtein Distance) ⭐⭐
> Given two strings $X$ of length $m$ and $Y$ of length $n$, write pseudocode to compute the **minimum number of single-character operations** (insert, delete, substitute) required to transform $X$ into $Y$.
>
> **Example:** `X = "kitten"`, `Y = "sitting"` → edit distance = **3**
>
> **Prototype:** `EditDistance(X, m, Y, n) → integer`

> [!success]- Solution
> **Subproblem:** Let `dp[i][j]` = edit distance between `X[1..i]` and `Y[1..j]`.
>
> **Recurrence:**
> $$dp[i][j] = \begin{cases} j & i = 0 \text{ (delete all of Y)} \\ i & j = 0 \text{ (delete all of X)} \\ dp[i-1][j-1] & X[i] = Y[j] \text{ (no op)} \\ 1 + \min(dp[i-1][j],\; dp[i][j-1],\; dp[i-1][j-1]) & X[i] \neq Y[j] \end{cases}$$
>
> The three choices in the mismatch case are: **delete** from X, **insert** into X (= delete from Y), **substitute**.
>
> ```
> EditDistance(X, m, Y, n):
>     dp ← (m+1) × (n+1) table
>
>     // Base cases
>     for i ← 0 to m: dp[i][0] ← i
>     for j ← 0 to n: dp[0][j] ← j
>
>     // Fill table
>     for i ← 1 to m:
>         for j ← 1 to n:
>             if X[i] = Y[j]:
>                 dp[i][j] ← dp[i-1][j-1]
>             else:
>                 dp[i][j] ← 1 + min(dp[i-1][j],     // delete X[i]
>                                     dp[i][j-1],     // insert Y[j] into X
>                                     dp[i-1][j-1])   // substitute
>
>     return dp[m][n]
> ```
>
> **Complexity:** $O(mn)$ time, $O(mn)$ space (reducible to $O(\min(m,n))$ with rolling array).

---

## 🔁 Module 8 — [[Search Algorithms]] + Cross-Structure

> [!question] Q8.1 — Binary Search on a Rotated Sorted Array ⭐
> A sorted array has been **rotated** at some unknown pivot (e.g., `[4,5,6,7,0,1,2]` was originally `[0,1,2,4,5,6,7]`). Write pseudocode to find the index of a target value `k` in $O(\log n)$ time. Return $-1$ if not found.
>
> **Prototype:** `SearchRotated(A, n, k) → integer`

> [!success]- Solution
> **Idea:** At each step, one half of the array is **guaranteed to be sorted**. Determine which half is sorted, then check if `k` falls in that range to decide which half to recurse into.
>
> ```
> SearchRotated(A, n, k):
>     left ← 0;  right ← n - 1
>
>     while left ≤ right:
>         mid ← (left + right) / 2
>
>         if A[mid] = k:
>             return mid
>
>         // Left half is sorted
>         if A[left] ≤ A[mid]:
>             if A[left] ≤ k < A[mid]:
>                 right ← mid - 1    // k in left half
>             else:
>                 left ← mid + 1     // k in right half
>         // Right half is sorted
>         else:
>             if A[mid] < k ≤ A[right]:
>                 left ← mid + 1     // k in right half
>             else:
>                 right ← mid - 1    // k in left half
>
>     return -1
> ```
>
> **Complexity:** $O(\log n)$ time, $O(1)$ space.

---

> [!question] Q8.2 — Count Occurrences of a Value in a Sorted Array
> Given a **sorted** array $A[0..n-1]$ and a key $k$, write pseudocode to count the number of times $k$ appears. Achieve $O(\log n)$ time.
>
> **Prototype:** `CountOccurrences(A, n, k) → integer`

> [!success]- Solution
> **Idea:** Binary search for the **leftmost** index of `k` (`firstPos`) and the **rightmost** index (`lastPos`). Count = `lastPos - firstPos + 1`.
>
> ```
> FindFirst(A, n, k):
>     left ← 0;  right ← n-1;  result ← -1
>     while left ≤ right:
>         mid ← (left + right) / 2
>         if A[mid] = k:
>             result ← mid
>             right ← mid - 1      // keep searching left
>         else if A[mid] < k:
>             left ← mid + 1
>         else:
>             right ← mid - 1
>     return result
>
> FindLast(A, n, k):
>     left ← 0;  right ← n-1;  result ← -1
>     while left ≤ right:
>         mid ← (left + right) / 2
>         if A[mid] = k:
>             result ← mid
>             left ← mid + 1       // keep searching right
>         else if A[mid] < k:
>             left ← mid + 1
>         else:
>             right ← mid - 1
>     return result
>
> CountOccurrences(A, n, k):
>     first ← FindFirst(A, n, k)
>     if first = -1: return 0
>     last ← FindLast(A, n, k)
>     return last - first + 1
> ```
>
> **Complexity:** $O(\log n)$ time (two binary searches), $O(1)$ space.

---

## 🧩 Module 9 — Mixed Design Challenges

> [!question] Q9.1 — Implement a Priority Queue Using a Sorted Linked List
> Design a priority queue (min-priority) where `Insert(x)` maintains sorted order and `ExtractMin()` removes the front. Write pseudocode for both operations.

> [!success]- Solution
> **Representation:** A sorted SLL where `pHead` holds the minimum.
>
> ```
> Insert(L, x):
>     newNode ← new Node(x)
>
>     // Case 1: empty list or x < head
>     if L.pHead = NULL or x ≤ L.pHead.Info:
>         newNode.pNext ← L.pHead
>         L.pHead ← newNode
>         return
>
>     // Case 2: find insertion point
>     prev ← L.pHead
>     while prev.pNext ≠ NULL and prev.pNext.Info < x:
>         prev ← prev.pNext
>     newNode.pNext ← prev.pNext
>     prev.pNext ← newNode
>
> ExtractMin(L):
>     if L.pHead = NULL:
>         error "Priority queue is empty"
>     minVal ← L.pHead.Info
>     temp ← L.pHead
>     L.pHead ← L.pHead.pNext
>     delete temp
>     return minVal
> ```
>
> **Complexity:** `Insert` = $O(n)$, `ExtractMin` = $O(1)$.

---

> [!question] Q9.2 — Check if a Binary Tree is Symmetric (Mirror of Itself) ⭐
> Write pseudocode to check if a binary tree is a **mirror image** of itself around its centre (i.e., structurally symmetric with equal values at mirror positions).
>
> **Prototype:** `IsSymmetric(root) → Boolean`

> [!success]- Solution
> **Idea:** The tree is symmetric iff the left and right subtrees are mirrors of each other. Define a helper `IsMirror(L, R)` that checks two subtrees simultaneously.
>
> ```
> IsSymmetric(root):
>     if root = NULL: return True
>     return IsMirror(root.left, root.right)
>
> IsMirror(L, R):
>     if L = NULL and R = NULL: return True
>     if L = NULL or R = NULL:  return False
>     return (L.value = R.value) and
>            IsMirror(L.left,  R.right) and
>            IsMirror(L.right, R.left)
> ```
>
> **Complexity:** $O(n)$ time, $O(h)$ space (recursion depth = tree height).

---

> [!question] Q9.3 — Serialize and Deserialize a BST ⭐⭐
> Write pseudocode to:
> - **Serialize:** Convert a BST to a string (or array) representation.
> - **Deserialize:** Reconstruct the original BST from that representation.
>
> **Constraint:** The reconstructed BST must be identical to the original.

> [!success]- Solution
> **Idea:** Use **preorder traversal** for serialization (root before children). During deserialization, the first element is always the root; use BST-insert to reconstruct.
>
> ```
> // --- SERIALIZE ---
> Serialize(root, output):
>     if root = NULL:
>         output.append("NULL")
>         return
>     output.append(root.value)
>     Serialize(root.left,  output)
>     Serialize(root.right, output)
>
> // --- DESERIALIZE (using a BST insert approach) ---
> Deserialize(data):
>     root ← NULL
>     for each value v in data:
>         if v ≠ "NULL":
>             root ← BSTInsert(root, v)
>     return root
>
> BSTInsert(node, v):
>     if node = NULL:
>         return new Node(v)
>     if v < node.value:
>         node.left  ← BSTInsert(node.left,  v)
>     else:
>         node.right ← BSTInsert(node.right, v)
>     return node
> ```
>
> **Why preorder works for BST:** The preorder sequence encodes the BST fully — any key inserted from a preorder sequence will always find its correct position because the root (first element) partitions subsequent elements into left/right subtrees by value.
>
> **Complexity:** Serialize $O(n)$; Deserialize $O(n \log n)$ average ($O(n^2)$ worst case for unbalanced BST).

---

> [!question] Q9.4 — Graph: Number of Connected Components Using Union-Find ⭐
> Given $n$ vertices (0-indexed) and a list of edges, write pseudocode using a **Union-Find (Disjoint Set Union)** structure to count the number of connected components.
>
> Implement `MakeSet(n)`, `Find(x)`, `Union(x, y)`, and `CountComponents(n, edges)`.

> [!success]- Solution
> ```
> // parent[i] = parent of node i (initially itself)
> // rank[i]   = tree depth hint for union by rank
>
> MakeSet(n):
>     parent ← array of size n
>     rank   ← array of size n, all 0
>     for i ← 0 to n-1:
>         parent[i] ← i
>
> Find(x):                          // with path compression
>     if parent[x] ≠ x:
>         parent[x] ← Find(parent[x])
>     return parent[x]
>
> Union(x, y):                      // union by rank
>     rootX ← Find(x)
>     rootY ← Find(y)
>     if rootX = rootY: return      // already in same set
>     if rank[rootX] < rank[rootY]:
>         parent[rootX] ← rootY
>     else if rank[rootX] > rank[rootY]:
>         parent[rootY] ← rootX
>     else:
>         parent[rootY] ← rootX
>         rank[rootX] ← rank[rootX] + 1
>
> CountComponents(n, edges):
>     MakeSet(n)
>     for each edge (u, v) in edges:
>         Union(u, v)
>
>     count ← 0
>     for i ← 0 to n-1:
>         if Find(i) = i:           // i is a root → one component
>             count ← count + 1
>     return count
> ```
>
> **Complexity:** Near $O(n + m \cdot \alpha(n))$ total where $\alpha$ is the inverse Ackermann function (effectively constant). Path compression + union by rank achieve this.

---

> [!question] Q9.5 — Running Median Using Two Heaps ⭐⭐
> You receive a stream of integers one by one. After each new integer, output the **median** of all integers seen so far. Design a data structure supporting `Insert(x)` and `GetMedian()`, both efficient.
>
> You may use `MaxHeap` and `MinHeap` with operations `Insert`, `ExtractMax`/`ExtractMin`, `PeekMax`/`PeekMin`, `Size`.

> [!success]- Solution
> **Idea:** Maintain two heaps:
> - `maxH` (max-heap): holds the **smaller half** of the numbers — its root is the largest of the small half.
> - `minH` (min-heap): holds the **larger half** — its root is the smallest of the large half.
>
> **Invariant:** `|maxH.Size - minH.Size| ≤ 1` and `maxH.PeekMax ≤ minH.PeekMin`.
>
> The median is either `maxH.PeekMax` (odd total) or the average of both roots (even total).
>
> ```
> Insert(x):
>     // Step 1: push to correct heap
>     if maxH.IsEmpty() or x ≤ maxH.PeekMax():
>         maxH.Insert(x)
>     else:
>         minH.Insert(x)
>
>     // Step 2: rebalance so sizes differ by at most 1
>     if maxH.Size() > minH.Size() + 1:
>         minH.Insert(maxH.ExtractMax())
>     else if minH.Size() > maxH.Size() + 1:
>         maxH.Insert(minH.ExtractMin())
>
> GetMedian():
>     if maxH.Size() = minH.Size():
>         return (maxH.PeekMax() + minH.PeekMin()) / 2.0
>     else if maxH.Size() > minH.Size():
>         return maxH.PeekMax()
>     else:
>         return minH.PeekMin()
> ```
>
> **Complexity:** `Insert` = $O(\log n)$, `GetMedian` = $O(1)$.
>
> > [!note] This problem combines **heap manipulation** with an **invariant maintenance** pattern — a favourite in interviews and a direct extension of the priority queue and heap sort material from Lecture 4/5.

---

## 🔢 Module 10 — [[Sorting Algorithms]] (Advanced Applications)

> [!question] Q10.1 — Sort an Array of 0s, 1s and 2s Without a Counting Pass
> The Dutch National Flag (Q3.2) is one approach. Now solve the same problem differently: implement it using **two passes of Counting Sort** (no comparisons between elements after counting).
>
> **Prototype:** `CountSort3(A, n)`

> [!success]- Solution
> **Idea:** Counting Sort with $k = 3$ buckets. Count occurrences, compute cumulative positions, write output.
>
> ```
> CountSort3(A, n):
>     count ← [0, 0, 0]           // count[0], count[1], count[2]
>
>     // Pass 1: count
>     for i ← 0 to n-1:
>         count[A[i]] ← count[A[i]] + 1
>
>     // Pass 2: overwrite in order
>     idx ← 0
>     for val ← 0 to 2:
>         for j ← 1 to count[val]:
>             A[idx] ← val
>             idx ← idx + 1
> ```
>
> **Complexity:** $O(n + k) = O(n)$ time (since $k = 3$ is constant), $O(k)$ space.
>
> **Comparison with Dutch National Flag:**
> | | Dutch Flag (Q3.2) | Counting Sort |
> |--|---|---|
> | Passes | 1 | 2 |
> | Space | $O(1)$ | $O(k)$ |
> | Stable | No | Yes |
> | Generalises to $k > 3$ | No (3-way only) | Yes |

---

> [!question] Q10.2 — External Sort: Merge K Sorted Arrays
> You have $K$ sorted arrays each of length $m$. Write pseudocode to merge them into a single sorted array of length $K \cdot m$ using a **min-heap** of size $K$.
>
> Each heap element tracks `(value, arrayIndex, elementIndex)`.
>
> **Prototype:** `MergeKSorted(arrays, K, m) → Array`

> [!success]- Solution
> **Idea:** Initialise the heap with the first element from each array. Repeatedly extract the minimum, append to output, and push the next element from the same array.
>
> ```
> MergeKSorted(arrays, K, m):
>     result ← empty array of size K*m
>     H ← empty min-heap (keyed by value)
>
>     // Initialise heap with first element of each array
>     for i ← 0 to K-1:
>         H.Insert( (arrays[i][0], i, 0) )
>
>     idx ← 0
>     while not H.IsEmpty():
>         (val, arrIdx, elemIdx) ← H.ExtractMin()
>         result[idx] ← val
>         idx ← idx + 1
>
>         // Push next element from the same array, if available
>         nextElem ← elemIdx + 1
>         if nextElem < m:
>             H.Insert( (arrays[arrIdx][nextElem], arrIdx, nextElem) )
>
>     return result
> ```
>
> **Complexity:** $O(Km \log K)$ time — each of the $Km$ elements is inserted and extracted once from a heap of size $\leq K$. $O(K)$ extra space for the heap.

---

> [!question] Q10.3 — Iterative Merge Sort (Bottom-Up)
> Write pseudocode for **bottom-up (iterative) Merge Sort** that avoids recursion entirely. Process the array in passes, doubling the subarray size each pass.
>
> **Prototype:** `MergeSortIterative(A, n)`

> [!success]- Solution
> **Idea:** Start with subarrays of size 1 (trivially sorted). Merge adjacent pairs into size-2 subarrays. Then merge size-2 pairs into size-4, and so on, until the whole array is sorted.
>
> ```
> MergeSortIterative(A, n):
>     width ← 1
>     while width < n:
>         left ← 0
>         while left < n:
>             mid   ← min(left + width - 1, n - 1)
>             right ← min(left + 2*width - 1, n - 1)
>
>             if mid < right:            // there is a right half to merge
>                 Merge(A, left, mid, right)
>
>             left ← left + 2 * width
>         width ← width * 2
>
> // Standard in-place merge using temp array:
> Merge(A, left, mid, right):
>     temp ← array of size (right - left + 1)
>     i ← left;   j ← mid + 1;   k ← 0
>
>     while i ≤ mid and j ≤ right:
>         if A[i] ≤ A[j]:
>             temp[k] ← A[i];  i ← i + 1
>         else:
>             temp[k] ← A[j];  j ← j + 1
>         k ← k + 1
>
>     while i ≤ mid:   temp[k] ← A[i];  i ← i+1;  k ← k+1
>     while j ≤ right: temp[k] ← A[j];  j ← j+1;  k ← k+1
>
>     for i ← 0 to k-1:
>         A[left + i] ← temp[i]
> ```
>
> **Complexity:** $O(n \log n)$ time, $O(n)$ space. $O(1)$ call-stack space (no recursion).

---

> [!question] Q10.4 — Quick Select: Find the K-th Smallest Element in O(n) Average ⭐
> Given an unsorted array $A[0..n-1]$, find the **$k$-th smallest** element (1-indexed) without fully sorting the array. Use the Quick Sort partition idea.
>
> **Prototype:** `QuickSelect(A, low, high, k) → integer`

> [!success]- Solution
> **Idea:** After partitioning around a pivot, the pivot lands at its final sorted position `p`. If `p+1 = k`, return it. If `k < p+1`, recurse left; else recurse right. Average case: only one half is processed each time.
>
> ```
> QuickSelect(A, low, high, k):
>     if low = high:
>         return A[low]
>
>     pivotIdx ← Partition(A, low, high)   // same as QuickSort's Partition
>     rank ← pivotIdx - low + 1            // 1-indexed rank within this subarray
>
>     if rank = k:
>         return A[pivotIdx]
>     else if k < rank:
>         return QuickSelect(A, low, pivotIdx - 1, k)
>     else:
>         return QuickSelect(A, pivotIdx + 1, high, k - rank)
>
> // Standard Lomuto partition (pivot = last element):
> Partition(A, low, high):
>     pivot ← A[high]
>     i ← low - 1
>     for j ← low to high - 1:
>         if A[j] ≤ pivot:
>             i ← i + 1
>             Swap(A, i, j)
>     Swap(A, i + 1, high)
>     return i + 1
> ```
>
> **Complexity:**
> - Average: $O(n)$ — recurrence $T(n) = T(n/2) + O(n)$ solves to $O(n)$.
> - Worst: $O(n^2)$ (same degenerate case as Quick Sort — use randomised pivot to avoid).

---

## 🗂️ Module 11 — [[Hashing]] (Advanced)

> [!question] Q11.1 — Implement Separate Chaining Hash Table
> Implement a hash table with **separate chaining** using linked lists. Write pseudocode for `Insert(key)`, `Search(key)`, and `Delete(key)`. Use $h(k) = k \bmod m$.
>
> **Prototype:** uses `table[0..m-1]`, each cell a linked list head.

> [!success]- Solution
> ```
> // table[0..m-1]: array of linked list heads, all initialised to NULL
>
> Insert(table, m, key):
>     slot ← key mod m
>     // Check for duplicate first
>     p ← table[slot]
>     while p ≠ NULL:
>         if p.Info = key: return      // already present
>         p ← p.pNext
>     // Prepend new node (O(1))
>     newNode ← new Node(key)
>     newNode.pNext ← table[slot]
>     table[slot] ← newNode
>
> Search(table, m, key) → Boolean:
>     slot ← key mod m
>     p ← table[slot]
>     while p ≠ NULL:
>         if p.Info = key: return True
>         p ← p.pNext
>     return False
>
> Delete(table, m, key):
>     slot ← key mod m
>     prev ← NULL
>     p ← table[slot]
>     while p ≠ NULL:
>         if p.Info = key:
>             if prev = NULL:
>                 table[slot] ← p.pNext     // deleting head of chain
>             else:
>                 prev.pNext ← p.pNext
>             delete p
>             return
>         prev ← p
>         p ← p.pNext
> ```
>
> **Complexity:** $O(1 + \alpha)$ average for all operations, where $\alpha = n/m$ is the load factor.

---

> [!question] Q11.2 — Open Addressing Delete with Tombstones ⭐
> In an open-addressing hash table (linear probing), you **cannot simply empty a slot** on deletion — this breaks subsequent searches. Write pseudocode for `Delete(key)` using **lazy deletion** (tombstone markers), and update `Insert` and `Search` to handle tombstones correctly.
>
> Slot states: `EMPTY`, `OCCUPIED`, `DELETED` (tombstone).

> [!success]- Solution
> **Key insight:**
> - `Search`: treat `DELETED` as occupied (keep probing past it).
> - `Insert`: treat `DELETED` as available (insert at first `DELETED` slot after confirming key is absent).
> - `Delete`: mark as `DELETED` (do not actually empty).
>
> ```
> Search(table, m, key) → index or -1:
>     slot ← key mod m
>     i ← 0
>     while i < m:
>         probe ← (slot + i) mod m
>         if table[probe].state = EMPTY:
>             return -1            // definitive absence
>         if table[probe].state = OCCUPIED and table[probe].key = key:
>             return probe
>         i ← i + 1
>     return -1
>
> Insert(table, m, key):
>     slot ← key mod m
>     firstDeleted ← -1
>     i ← 0
>     while i < m:
>         probe ← (slot + i) mod m
>         if table[probe].state = EMPTY:
>             insertAt ← (firstDeleted ≠ -1) ? firstDeleted : probe
>             table[insertAt] ← {key, OCCUPIED}
>             return
>         if table[probe].state = DELETED and firstDeleted = -1:
>             firstDeleted ← probe   // remember first tombstone
>         if table[probe].state = OCCUPIED and table[probe].key = key:
>             return                 // duplicate, do not insert
>         i ← i + 1
>     // table full — should trigger rehash
>     error "Table full"
>
> Delete(table, m, key):
>     idx ← Search(table, m, key)
>     if idx = -1: return            // key not found
>     table[idx].state ← DELETED    // tombstone
> ```
>
> **Complexity:** $O(1/(1-\alpha))$ average for each operation. Tombstones accumulate over time — periodic **rehashing** is needed to clean them up and maintain performance.

---

> [!question] Q11.3 — Group Anagrams Using a Hash Map ⭐
> Given an array of $n$ strings, group all **anagrams** together. Return a list of groups.
>
> **Example:** `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`
>
> **Prototype:** `GroupAnagrams(words, n) → List of Lists`

> [!success]- Solution
> **Idea:** Two strings are anagrams iff their **sorted character sequences are identical**. Use sorted form as the hash key.
>
> ```
> GroupAnagrams(words, n):
>     groups ← empty hash map    // sorted_word → List of original words
>
>     for i ← 0 to n-1:
>         key ← Sort(words[i])   // sort characters alphabetically, O(L log L)
>         if key not in groups:
>             groups[key] ← empty List
>         groups[key].append(words[i])
>
>     result ← empty List
>     for each (key, group) in groups:
>         result.append(group)
>     return result
> ```
>
> **Complexity:** $O(nL \log L)$ time where $L$ = max string length (sorting each string). $O(nL)$ space.
>
> > [!note] **Alternative key (no sorting, $O(L)$ per string):** Use a frequency vector of 26 integers as the key, encoded as a string `"1#0#2#..."`. This gives $O(nL)$ total time.

---

## 🌳 Module 12 — [[Trees]] (Advanced Operations)

> [!question] Q12.1 — Diameter of a Binary Tree ⭐
> The **diameter** of a binary tree is the length of the longest path between any two nodes (the path may or may not pass through the root). Write pseudocode returning the diameter (number of edges on the longest path).
>
> **Prototype:** `Diameter(root) → integer`

> [!success]- Solution
> **Key insight:** For any node $v$, the longest path through $v$ has length `height(left subtree) + height(right subtree) + 2`. Track a global maximum while computing heights.
>
> ```
> diameter ← 0      // global variable (or pass by reference)
>
> Diameter(root):
>     diameter ← 0
>     Height(root)
>     return diameter
>
> Height(node):     // returns height; updates diameter as a side effect
>     if node = NULL: return -1
>
>     leftH  ← Height(node.left)
>     rightH ← Height(node.right)
>
>     // Path through this node spans (leftH+1) + (rightH+1) edges
>     pathThrough ← leftH + rightH + 2
>     diameter ← max(diameter, pathThrough)
>
>     return 1 + max(leftH, rightH)
> ```
>
> **Complexity:** $O(n)$ time — visits every node exactly once.
>
> > [!warning] A naïve approach calling `Height(node.left) + Height(node.right)` at each node separately would be $O(n^2)$ due to repeated subtree traversals. Combining the diameter update inside the height computation achieves $O(n)$.

---

> [!question] Q12.2 — Flatten a Binary Tree to a Linked List (In-Place) ⭐
> Given a binary tree, flatten it into a singly linked list **in-place** using the **preorder traversal order**. Set every node's `left` to `NULL` and chain nodes via `right` pointers.
>
> ```
>       1              1
>      / \              \
>     2   5    →         2
>    / \   \              \
>   3   4   6              3
>                           \
>                            4
>                             \
>                              5
>                               \
>                                6
> ```
>
> **Prototype:** `Flatten(root)`

> [!success]- Solution
> **Idea (Morris-inspired, right-threading):** For each node with a left subtree, find the **rightmost node of the left subtree** and thread the right subtree onto it. Then move the entire left subtree to the right and null out `left`.
>
> ```
> Flatten(root):
>     cur ← root
>
>     while cur ≠ NULL:
>         if cur.left ≠ NULL:
>             // Find rightmost node in left subtree
>             rightmost ← cur.left
>             while rightmost.right ≠ NULL:
>                 rightmost ← rightmost.right
>
>             // Thread: rightmost.right → cur.right
>             rightmost.right ← cur.right
>
>             // Move left subtree to right
>             cur.right ← cur.left
>             cur.left  ← NULL
>
>         cur ← cur.right
> ```
>
> **Complexity:** $O(n)$ time, $O(1)$ extra space (iterative, no stack).

---

> [!question] Q12.3 — Reconstruct BST from Preorder Traversal ⭐
> Given the **preorder traversal** sequence of a BST (as an array), reconstruct the original BST. Return the root.
>
> **Example:** Preorder `[8, 5, 1, 7, 10, 12]` → reconstruct the BST.
>
> **Prototype:** `BSTFromPreorder(preorder, n) → Node`

> [!success]- Solution
> **Naive approach ($O(n^2)$):** Insert elements one by one using `BSTInsert`. Works but doesn't exploit the preorder structure.
>
> **Efficient approach ($O(n)$) — bound-based recursion:** The preorder sequence naturally splits at each node: elements $< \text{root}$ form the left subtree (appear consecutively after root in preorder), elements $> \text{root}$ form the right subtree.
>
> ```
> idx ← 0    // global index into preorder array
>
> BSTFromPreorder(preorder, n):
>     idx ← 0
>     return Build(preorder, n, -∞, +∞)
>
> Build(preorder, n, minVal, maxVal):
>     if idx = n: return NULL
>     val ← preorder[idx]
>     if val < minVal or val > maxVal:
>         return NULL           // this value doesn't belong in current subtree
>
>     node ← new Node(val)
>     idx ← idx + 1
>     node.left  ← Build(preorder, n, minVal, val)
>     node.right ← Build(preorder, n, val, maxVal)
>     return node
> ```
>
> **Trace for `[8, 5, 1, 7, 10, 12]`:**
>
> ```mermaid
> graph TD
>     8 --> 5
>     8 --> 10
>     5 --> 1
>     5 --> 7
>     10 --> 12
> ```
>
> **Complexity:** $O(n)$ time (each element processed once), $O(h)$ space for recursion stack.

---

## 🕸️ Module 13 — [[Graphs]] (Advanced Applications)

> [!question] Q13.1 — Dijkstra's Algorithm with Priority Queue ⭐⭐
> Implement Dijkstra's algorithm from scratch, using a **min-priority queue** (keyed by cost estimate). Output the shortest distance from `src` to all vertices.
>
> **Prototype:** `Dijkstra(G, src) → dist[]`

> [!success]- Solution
> ```
> Dijkstra(G, src):
>     n ← number of vertices in G
>     dist[v]    ← ∞    for all v
>     visited[v] ← False for all v
>     dist[src] ← 0
>
>     PQ ← empty min-priority queue    // stores (cost, vertex)
>     PQ.Insert( (0, src) )
>
>     while not PQ.IsEmpty():
>         (cost, u) ← PQ.ExtractMin()
>
>         if visited[u]: continue       // stale entry — skip
>         visited[u] ← True
>
>         for each neighbour v of u with edge weight w(u,v):
>             if not visited[v] and dist[u] + w(u,v) < dist[v]:
>                 dist[v] ← dist[u] + w(u,v)
>                 PQ.Insert( (dist[v], v) )   // lazy insertion of updated cost
>
>     return dist
> ```
>
> **Complexity:** $O((|V| + |E|) \log |V|)$ with a binary heap.
>
> > [!warning] The `if visited[u]: continue` check handles **stale entries** — when a vertex's distance is updated multiple times, old (higher-cost) entries remain in the PQ. Skipping already-visited vertices ensures correctness.
>
> **Reconstruct path:** add `prev[v] ← u` whenever `dist[v]` is updated. Backtrack from destination via `prev[]`.

---

> [!question] Q13.2 — Kruskal's MST with Union-Find ⭐⭐
> Implement Kruskal's algorithm using the Union-Find structure from Q9.4. Sort edges by weight and greedily add edges that don't form a cycle.
>
> **Prototype:** `KruskalMST(V, E) → List of edges`

> [!success]- Solution
> ```
> KruskalMST(V, E):
>     n ← |V|
>     MakeSet(n)                       // initialise Union-Find for n vertices
>     Sort E by weight (ascending)     // O(|E| log |E|)
>
>     MST ← empty List
>     totalWeight ← 0
>
>     for each edge (u, v, w) in sorted E:
>         if Find(u) ≠ Find(v):        // u and v are in different components
>             Union(u, v)
>             MST.append( (u, v, w) )
>             totalWeight ← totalWeight + w
>
>         if |MST| = n - 1: break      // MST complete (n-1 edges)
>
>     return MST
> ```
>
> **Complexity:** $O(|E| \log |E|)$ dominated by the sort. Union-Find operations are nearly $O(1)$ amortised.
>
> **Why it works:** By the MST Cut Property, the minimum-weight edge crossing any cut between two components is always safe to add. Kruskal's processes edges in weight order, and skips edges that would form cycles (same component), so every added edge satisfies the Cut Property.

---

> [!question] Q13.3 — Multi-Source BFS: Distance to Nearest Gate ⭐
> You are given an $m \times n$ grid. Cells contain either `WALL` (-1), `GATE` (0), or `EMPTY` (∞). Fill each `EMPTY` cell with its **shortest distance to the nearest gate**. Walls block movement (4-directional).
>
> **Prototype:** `WallsAndGates(grid, m, n)`

> [!success]- Solution
> **Idea:** Multi-source BFS — initialise the queue with **all gates simultaneously** at distance 0. BFS spreads outward from all gates in parallel, filling minimum distances naturally.
>
> ```
> WallsAndGates(grid, m, n):
>     Q ← empty Queue
>
>     // Enqueue all gates
>     for i ← 0 to m-1:
>         for j ← 0 to n-1:
>             if grid[i][j] = 0:         // GATE
>                 Q.Enqueue( (i, j) )
>
>     directions ← [(0,1), (0,-1), (1,0), (-1,0)]
>
>     while not Q.IsEmpty():
>         (r, c) ← Q.Dequeue()
>
>         for each (dr, dc) in directions:
>             nr ← r + dr;  nc ← c + dc
>             if 0 ≤ nr < m and 0 ≤ nc < n and grid[nr][nc] = ∞:
>                 grid[nr][nc] ← grid[r][c] + 1
>                 Q.Enqueue( (nr, nc) )
> ```
>
> **Complexity:** $O(mn)$ time — each cell is enqueued and dequeued at most once.
>
> > [!note] The multi-source BFS trick (Q6.3 note) is key. A naïve approach of running BFS from each gate separately would be $O(G \cdot mn)$ where $G$ = number of gates.

---

## 🧮 Module 14 — [[Dynamic Programming]] (Advanced)

> [!question] Q14.1 — 0-1 Knapsack with Item Recovery ⭐
> Extend the standard Knapsack DP (from the lecture) to also **identify which items** are included in the optimal solution. Return both the maximum value and the list of chosen item indices.
>
> **Prototype:** `KnapsackWithItems(n, v[], wt[], W) → (maxVal, itemList)`

> [!success]- Solution
> ```
> KnapsackWithItems(n, v[], wt[], W):
>     // Step 1: Fill DP table (standard)
>     V[0..n][0..W] ← 0
>     for k ← 1 to n:
>         for w ← 1 to W:
>             if wt[k] > w:
>                 V[k][w] ← V[k-1][w]
>             else:
>                 V[k][w] ← max(V[k-1][w], v[k] + V[k-1][w - wt[k]])
>
>     // Step 2: Backtrack to find chosen items
>     items ← empty List
>     k ← n;  w ← W
>     while k > 0 and w > 0:
>         if V[k][w] ≠ V[k-1][w]:      // item k was included
>             items.prepend(k)
>             w ← w - wt[k]
>         k ← k - 1
>
>     return (V[n][W], items)
> ```
>
> **Example verification:** For each item $k$ in the returned list, confirm $\sum \text{wt}[k] \leq W$ and $\sum v[k] = V[n][W]$.
>
> **Complexity:** $O(nW)$ time and space for the DP. $O(n)$ for backtracking.

---

> [!question] Q14.2 — Matrix Chain Multiplication with Parenthesization Recovery ⭐
> Implement the Matrix Chain Multiplication DP and add a `PrintOptimal` procedure that outputs the **fully parenthesized optimal form**.
>
> **Prototype:** `MatrixChain(p, n) → (minCost, s-table)` and `PrintOptimal(s, i, j)`

> [!success]- Solution
> ```
> MatrixChain(p[0..n], n):
>     // p[i-1] × p[i] = dimensions of matrix M_i
>     m[1..n][1..n] ← 0          // m[i][j] = min multiplications for M_i..M_j
>     s[1..n][1..n] ← 0          // s[i][j] = optimal split point
>
>     // l = chain length
>     for l ← 2 to n:
>         for i ← 1 to n - l + 1:
>             j ← i + l - 1
>             m[i][j] ← ∞
>
>             for k ← i to j - 1:
>                 cost ← m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
>                 if cost < m[i][j]:
>                     m[i][j] ← cost
>                     s[i][j] ← k
>
>     return (m[1][n], s)
>
>
> PrintOptimal(s, i, j):
>     if i = j:
>         print "M" + i
>         return
>     print "("
>     PrintOptimal(s, i, s[i][j])
>     PrintOptimal(s, s[i][j] + 1, j)
>     print ")"
> ```
>
> **Example for $n=4$, optimal $s(1,4)=3$, $s(1,3)=1$, $s(2,3)=2$:**
> `PrintOptimal(s, 1, 4)` outputs: `((M1(M2M3))M4)`
>
> **Complexity:** $O(n^3)$ time, $O(n^2)$ space.

---

> [!question] Q14.3 — LCS with Full Sequence Reconstruction ⭐
> Implement the LCS DP and add backtracking to **print one actual LCS string**, not just its length.
>
> **Prototype:** `LCSString(X, m, Y, n) → string`

> [!success]- Solution
> ```
> LCSString(X[1..m], m, Y[1..n], n):
>     // Step 1: Fill DP table
>     L[0..m][0..n] ← 0
>     for i ← 1 to m:
>         for j ← 1 to n:
>             if X[i] = Y[j]:
>                 L[i][j] ← 1 + L[i-1][j-1]
>             else:
>                 L[i][j] ← max(L[i-1][j], L[i][j-1])
>
>     // Step 2: Backtrack to reconstruct LCS
>     lcs ← empty string
>     i ← m;  j ← n
>     while i > 0 and j > 0:
>         if X[i] = Y[j]:
>             lcs.prepend(X[i])    // matching character — part of LCS
>             i ← i - 1
>             j ← j - 1
>         else if L[i-1][j] > L[i][j-1]:
>             i ← i - 1            // came from above
>         else:
>             j ← j - 1            // came from left
>
>     return lcs
> ```
>
> **Complexity:** $O(mn)$ time and space for the table. $O(m + n)$ for backtracking.

---

> [!question] Q14.4 — Word Break Problem ⭐
> Given a string `s` and a dictionary `dict` (hash set of words), determine if `s` can be **segmented** into a sequence of dictionary words.
>
> **Example:** `s = "leetcode"`, `dict = {"leet","code"}` → `True`
> **Example:** `s = "catsandog"`, `dict = {"cats","dog","sand","and","cat"}` → `False`
>
> **Prototype:** `WordBreak(s, n, dict) → Boolean`

> [!success]- Solution
> **Subproblem:** `dp[i]` = True if `s[0..i-1]` (the first $i$ characters) can be segmented using `dict`.
>
> **Recurrence:**
> $$dp[i] = \bigvee_{0 \leq j < i} \bigl(dp[j] \;\text{AND}\; s[j..i-1] \in \text{dict}\bigr)$$
>
> ```
> WordBreak(s, n, dict):
>     dp ← array of size n+1, all False
>     dp[0] ← True       // empty prefix is always "breakable"
>
>     for i ← 1 to n:
>         for j ← 0 to i-1:
>             if dp[j] and s[j..i-1] in dict:
>                 dp[i] ← True
>                 break           // no need to check other j values
>
>     return dp[n]
> ```
>
> **Complexity:** $O(n^2 \cdot L)$ time where $L$ = max word length (substring extraction + hash lookup). $O(n)$ space.

---

## 🔁 Module 15 — Comprehensive Cross-Structure Challenges

> [!question] Q15.1 — LRU Cache: O(1) Get and Put ⭐⭐
> Design a data structure for a **Least Recently Used (LRU) cache** of capacity $C$. Both `Get(key)` and `Put(key, value)` must run in $O(1)$.
>
> - `Get(key)`: return value if key exists, else -1. Mark as most recently used.
> - `Put(key, value)`: insert or update key. If cache is full, **evict the least recently used item**.

> [!success]- Solution
> **Idea:** Combine a **hash map** (for $O(1)$ key lookup) with a **doubly linked list** (for $O(1)$ insertion/removal of nodes, maintaining recency order).
>
> - DLL head = most recently used, tail = least recently used.
> - Hash map: `key → pointer to DLL node`.
>
> ```
> // Initialise
> LRUCache(capacity C):
>     cap ← C
>     map ← empty hash map       // key → DLL node pointer
>     dll ← empty Doubly Linked List
>     // Use sentinel head and tail nodes for convenience
>     dll.head ← new Node(-1, -1)
>     dll.tail ← new Node(-1, -1)
>     dll.head.next ← dll.tail
>     dll.tail.prev ← dll.head
>
> Get(key):
>     if key not in map: return -1
>     node ← map[key]
>     MoveToFront(node)           // mark as most recently used
>     return node.value
>
> Put(key, value):
>     if key in map:
>         node ← map[key]
>         node.value ← value
>         MoveToFront(node)
>     else:
>         if |map| = cap:
>             // Evict LRU: the node just before sentinel tail
>             lru ← dll.tail.prev
>             RemoveFromDLL(lru)
>             delete map[lru.key]
>         newNode ← new Node(key, value)
>         InsertAtFront(newNode)
>         map[key] ← newNode
>
> // DLL helpers:
> MoveToFront(node):
>     RemoveFromDLL(node)
>     InsertAtFront(node)
>
> InsertAtFront(node):
>     node.next ← dll.head.next
>     node.prev ← dll.head
>     dll.head.next.prev ← node
>     dll.head.next ← node
>
> RemoveFromDLL(node):
>     node.prev.next ← node.next
>     node.next.prev ← node.prev
> ```
>
> **Complexity:** `Get` and `Put` both $O(1)$. $O(C)$ space.

---

> [!question] Q15.2 — Validate Stack Sequences ⭐
> Given two sequences `pushed[0..n-1]` and `popped[0..n-1]`, determine if `popped` is a **valid pop sequence** of `pushed` when elements are pushed in order. (i.e., could `popped` be the output of a stack where `pushed` is the input stream?)
>
> **Example:** `pushed = [1,2,3,4,5]`, `popped = [4,5,3,2,1]` → **True**
> **Example:** `pushed = [1,2,3,4,5]`, `popped = [4,3,5,1,2]` → **False**
>
> **Prototype:** `ValidateStackSequences(pushed, popped, n) → Boolean`

> [!success]- Solution
> **Idea:** Simulate the process with an auxiliary stack. Push elements from `pushed` one by one; after each push, check if the stack top matches the current `popped` element — if yes, pop and advance the `popped` pointer.
>
> ```
> ValidateStackSequences(pushed, popped, n):
>     S ← empty Stack
>     popIdx ← 0
>
>     for i ← 0 to n-1:
>         S.push(pushed[i])
>
>         // Pop as many times as the sequence allows
>         while not S.isEmpty() and S.peek() = popped[popIdx]:
>             S.pop()
>             popIdx ← popIdx + 1
>
>     return S.isEmpty()      // valid iff stack is fully emptied
> ```
>
> **Trace for `pushed=[1,2,3,4,5]`, `popped=[4,5,3,2,1]`:**
> Push 1,2,3,4 → top=4 matches popped[0]=4 → pop. Push 5 → top=5 matches popped[1]=5 → pop. top=3 matches popped[2]=3 → pop. top=2 matches → pop. top=1 matches → pop. Stack empty → **True** ✓
>
> **Complexity:** $O(n)$ time, $O(n)$ space.

---

> [!question] Q15.3 — Sliding Window Maximum Using a Deque ⭐⭐
> Given array $A[0..n-1]$ and window size $k$, find the **maximum value in each sliding window** of size $k$ as it moves from left to right. Output the $n - k + 1$ maximums.
>
> **Example:** $A = [1,3,-1,-3,5,3,6,7]$, $k = 3$ → `[3,3,5,5,6,7]`
>
> **Prototype:** `SlidingWindowMax(A, n, k) → Array`

> [!success]- Solution
> **Idea:** Use a **monotonic deque** (double-ended queue) that stores **indices** and maintains elements in **decreasing order** of their values. The front is always the index of the current window's maximum.
>
> Invariants maintained after processing each element:
> 1. Deque front = index of current maximum.
> 2. Deque contains only indices within the current window.
> 3. Values at deque indices are in **decreasing order** front-to-back.
>
> ```
> SlidingWindowMax(A, n, k):
>     dq ← empty Deque         // stores indices, not values
>     result ← empty Array
>
>     for i ← 0 to n-1:
>         // Remove indices outside the current window from the front
>         while not dq.IsEmpty() and dq.Front() < i - k + 1:
>             dq.PopFront()
>
>         // Remove indices from the back whose values are ≤ A[i]
>         // (they can never be the maximum while A[i] is in the window)
>         while not dq.IsEmpty() and A[dq.Back()] ≤ A[i]:
>             dq.PopBack()
>
>         dq.PushBack(i)
>
>         // Window is full; record maximum (front of deque)
>         if i ≥ k - 1:
>             result.append(A[dq.Front()])
>
>     return result
> ```
>
> **Trace for `[1,3,-1,-3,5,3,6,7]`, $k=3$:**
>
> | $i$ | $A[i]$ | Deque (indices) | Deque (values) | Output |
> |-----|--------|-----------------|----------------|--------|
> | 0 | 1 | [0] | [1] | — |
> | 1 | 3 | [1] | [3] | — |
> | 2 | -1 | [1,2] | [3,-1] | **3** |
> | 3 | -3 | [1,2,3] | [3,-1,-3] | **3** |
> | 4 | 5 | [4] | [5] | **5** |
> | 5 | 3 | [4,5] | [5,3] | **5** |
> | 6 | 6 | [6] | [6] | **6** |
> | 7 | 7 | [7] | [7] | **7** |
>
> **Complexity:** $O(n)$ time — each element is pushed and popped at most once. $O(k)$ space for the deque.
