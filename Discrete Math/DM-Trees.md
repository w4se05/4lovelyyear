---
tags: [discrete-mathematics, trees, graph-theory, spanning-trees, prufer-sequence, MST]
topic: "Chapter 11 — Trees"
course: "Discrete Mathematics"
---

> [!Note] 💡 Notation Conventions
> - $G = (V, E)$ — a graph with vertex set $V$ and edge set $E$
> - $|V|$ — number of vertices (also written $n$); $|E|$ — number of edges (also written $m$)
> - $\deg(v)$ — degree of vertex $v$
> - $[n] = \{1, 2, \ldots, n\}$
> - $T$ always denotes a tree (or spanning tree when context is clear)
> - $\kappa(G)$ — number of spanning trees of $G$ (complexity of $G$)
> - $L$ — Laplacian matrix; $\tilde{L}_j$ — reduced Laplacian (row and column $j$ deleted)
> - $w(e)$ — weight of edge $e$; $w(T) = \sum_{e \in T} w(e)$ — total weight of tree $T$

---

## 1. Introduction and Terminologies

> [!Definition] 📖 Tree, Leaf, Internal Node, Forest
> **1.** A simple undirected graph is a **tree** if it is **connected** and **acyclic** (contains no cycles).
>
> **2.** In a tree, a vertex with $\deg(v) = 1$ is called a **leaf**. A vertex that is not a leaf is called an **internal node**.
>
> **3.** A **forest** is a simple graph with no cycles (a disjoint union of trees).

> [!Note] 💡
> A graph with no cycles is also called an **acyclic graph**.

---

## 2. Properties of Trees

> [!Theorem] 📌 Lemma
> Let $G$ be a simple graph.
>
> **i.** If every vertex in $G$ has degree $\geq 2$, then $G$ contains a cycle.
>
> **ii.** Every tree with at least 2 vertices has at least one leaf. Removing that leaf yields again a tree.

> [!Theorem] 📌 Vertex–Edge Relation
> Let $T = (V, E)$ be a tree. Then:
> $$|V| = |E| + 1$$

> [!Theorem] 📌 Equivalent Characterisations of Trees
> Let $G = (V, E)$ be a simple graph. The following are equivalent:
>
> **1.** $G$ is a tree.
>
> **2.** $G$ is connected and $|V| = |E| + 1$.
>
> **3.** $G$ is acyclic and $|V| = |E| + 1$.
>
> **4.** For any two vertices $u, v \in V$, there exists **exactly one** simple path from $u$ to $v$.
>
> **5.** $G$ is **minimally connected**: $G$ is connected and removing any edge disconnects it (every edge is a cut edge).
>
> **6.** $G$ is **maximally acyclic**: $G$ is acyclic and adding any additional edge creates a cycle.

---

## 3. Rooted Trees and Terminologies

> [!Definition] 📖 Rooted Tree
> A **rooted tree** is a tree in which one vertex is designated as the **root** and every edge is directed away from the root.
>
> Theoretically a rooted tree is a digraph, but it is drawn with the root at the top and arrow directions are usually omitted.

> [!Definition] 📖 Rooted Tree Terminology
> Given a rooted tree with edge directed from $u$ to $v$:
>
> - **Parent / Child:** $u$ is the *parent* of $v$; $v$ is a *child* of $u$.
> - **Siblings:** Vertices sharing the same parent.
> - **Ancestors of $v$:** All vertices on the path from the root to $v$, excluding $v$ itself.
> - **Descendants of $v$:** All vertices for which $v$ is an ancestor.
> - **Leaves:** Vertices with no children.
> - **Internal vertices:** Vertices that have at least one child.
> - **Subtree rooted at $a$:** The subgraph consisting of $a$, all its descendants, and all incident edges.

> [!Example] 📘 Rooted Tree Illustration
> **Using:** Rooted tree terminology
>
> Tree with root $2$:
> ```
>         2
>        / \
>       3   8
>      /|\ / | \
>     4 7 9 6   10
>     |       |
>     1       5
> ```
> - Root: $2$
> - Siblings: $4, 7, 9$ (children of $3$); $6, 10$ (children of $8$)
> - Parent of $5$ is $6$; $6$ is a child of $8$
> - Ancestors of $1$: $\{4, 3, 2\}$
> - Descendants of $8$: $\{6, 10, 5\}$
> - Leaves: $1, 7, 9, 5, 10$
> - Internal vertices: $2, 3, 4, 8, 6$

---

## 4. $m$-ary Trees

> [!Definition] 📖 $m$-ary Trees
> **1.** A rooted tree is an **$m$-ary tree** if each vertex has **at most** $m$ children.
>
> **2.** A rooted tree is a **full $m$-ary tree** if each *internal* vertex has **exactly** $m$ children.
>
> **3.** A **binary tree** is a $2$-ary tree. A **full binary tree** is a full $2$-ary tree.
>
> **4.** A **complete $m$-ary tree** is a full $m$-ary tree where all levels except possibly the last are completely filled, and the last level has all nodes pushed to the left.

> [!Theorem] 📌 Enumeration on Full $m$-ary Trees
> Let $n$ = total number of vertices, $i$ = number of internal vertices of a full $m$-ary tree. Then:
>
> $$n = mi + 1$$
>
> Number of leaves $= n - i = (m-1)i + 1$

> [!Proof] 🔷
> Each internal vertex contributes exactly $m$ children (edges downward), so the total number of edges $= mi$. By $|V| = |E| + 1$: $n = mi + 1$. Leaves $= n - i = mi + 1 - i = (m-1)i + 1$.

> [!Property] ⚙️ Corollary — Full Binary Trees
> A full binary tree has an **odd** number $2n+1$ of vertices, with $n$ internal nodes and $n+1$ leaves, for some $n \geq 0$.

---

## 5. Level, Height, and Balanced Trees

> [!Definition] 📖 Level, Height, Balanced Tree
> **1.** The **level** of a vertex $v$ in a rooted tree is the length of the unique path from the root to $v$. The root has level $0$.
>
> **2.** The **height** of a rooted tree is the maximum level among all vertices.
>
> **3.** An $m$-ary tree of height $h$ is **balanced** if every leaf has level $h$ or $h-1$.

> [!Theorem] 📌 Height–Leaves Bound
> **1.** In an $m$-ary tree with height $h$ and $l$ leaves:
> $$l \leq m^h \implies h \geq \lceil \log_m l \rceil$$
>
> **2.** In a **balanced full** $m$-ary tree:
> $$h = \lceil \log_m l \rceil$$

---

## 6. Ordered Rooted Trees

> [!Definition] 📖 Ordered Rooted Tree
> An **ordered rooted tree** is a rooted tree where the children of each internal node are ordered (left to right). They are drawn so children appear in order from left to right.

---

## 7. Decision Trees and Sorting Lower Bounds

> [!Definition] 📖 Decision Tree
> A **decision tree** is a rooted tree where:
> - Each **internal node** represents a decision with a subtree for each possible outcome.
> - Each **leaf** represents a possible solution.
> - A solution corresponds to a **path from root to leaf**.

> [!Theorem] 📌 Sorting Lower Bound
> A sorting algorithm based on binary comparisons requires at least $\lceil \log(n!) \rceil$ comparisons.
> $$\log(n!) = \log 1 + \log 2 + \cdots + \log n = \Theta(n \log n)$$

> [!Proof] 🔷
> **1.** Each binary comparison has 2 outcomes → the decision tree is a **binary tree**.
>
> **2.** There are $n!$ possible orderings of $n$ distinct numbers → the tree has at least $n!$ leaves.
>
> **3.** In an $m$-ary tree with $l$ leaves: $h \geq \lceil \log_m l \rceil$. For binary ($m=2$), $l = n!$:
> $$h \geq \lceil \log(n!) \rceil$$

> [!Theorem] 📌 Comparisons to Locate an Element
> The least number of comparisons to locate an element in a binary search tree of a list of length $n$ is $\lceil \log(n+1) \rceil$.

> [!Proof] 🔷
> Construct a full binary tree $U$ from the search tree $T$ by adding null nodes so every keyed vertex has two children. $U$ has $n$ internal nodes, so $n+1$ leaves. A balanced full binary tree of $n+1$ leaves has height $\lceil \log(n+1) \rceil$.

---

## 8. Prefix Codes and Huffman Coding

> [!Definition] 📖 Prefix Code
> A **prefix code** is a set of bit strings used to encode letters such that **no codeword is a prefix of another**. This guarantees unambiguous decoding.

> [!Property] ⚙️ Prefix Code from a Binary Tree
> Given a binary tree with letters at leaves:
> - Assign $0$ to each left-child edge, $1$ to each right-child edge.
> - The codeword of a letter = sequence of edge labels on the path from root to that leaf.
> - To **decode**: start at root, follow bits until a leaf is reached; repeat.

> [!Definition] 📖 Huffman Coding
> **Huffman coding** is a greedy algorithm producing an optimal prefix code (minimum total bits):
>
> **Step 1.** List all distinct letters with their frequencies. Treat each letter as a one-vertex tree with weight = frequency.
>
> **Step 2.** Repeatedly combine the two trees of **smallest weight** by adding a new root; new weight = sum of the two weights.
>
> **Step 3.** Stop when a single tree remains.

---

## 9. Tree Traversals

> [!Definition] 📖 Three Traversal Orders
> For a rooted ordered tree with subtrees $T_1, T_2, \ldots, T_n$ (left to right):
>
> **Pre-order:** Visit root → traverse $T_1, T_2, \ldots, T_n$ pre-order recursively.
>
> **In-order (binary trees):** Traverse $T_1$ in-order → visit root → traverse $T_2, \ldots, T_n$ in-order.
>
> **Post-order:** Traverse $T_1, T_2, \ldots, T_n$ post-order → visit root.

> [!Note] 💡 Traversal Applications
> For a **binary search tree**, in-order traversal yields elements in **sorted (ascending) order**.

> [!Property] ⚙️ Infix / Prefix / Postfix Notation
> For expression trees (internal nodes = operators, leaves = operands):
>
> - **Infix:** In-order traversal → human-readable (e.g., $x + y$)
> - **Prefix (Polish):** Pre-order traversal → machine-friendly
> - **Postfix (Reverse Polish):** Post-order traversal → stack-based evaluation
>
> **Evaluating postfix:** scan left-to-right; apply operator to the two preceding operands.
>
> **Evaluating prefix:** scan right-to-left; apply operator to the two following operands.

---

## 10. Labeled Trees and Cayley's Theorem

> [!Definition] 📖 Labeled Tree
> A **labeled tree** on $n$ vertices assigns unique labels from $\{1, 2, \ldots, n\}$ to vertices. Two labeled trees are **identical** iff the identity bijection $[n] \to [n]$ preserves adjacency.

> [!Theorem] 📌 Cayley's Theorem
> The number of labeled trees on $n$ vertices is:
> $$\tau(n) = n^{n-2}$$
>
> Known values: $\tau(2) = 1,\ \tau(3) = 3,\ \tau(4) = 16,\ \tau(5) = 125$.

> [!Property] ⚙️ Corollaries
> **1.** Number of **rooted** labeled trees on $n$ vertices: $n^{n-1}$ (multiply by $n$ choices of root).
>
> **2.** Number of labeled trees on $n$ vertices with a given degree sequence $(d_1, d_2, \ldots, d_n)$:
> $$\frac{(n-2)!}{(d_1 - 1)!\,(d_2 - 1)!\,\cdots\,(d_n - 1)!}$$
> where $d_i$ is the degree of the vertex labeled $i$.

---

## 11. Prüfer Sequences

> [!Definition] 📖 Prüfer Sequence
> A **Prüfer sequence** of a labeled tree on $n$ vertices is a sequence of length $n-2$ with each element in $[n]$. There is a **bijection** between labeled trees on $n$ vertices and the set $[n]^{n-2}$ (which has $n^{n-2}$ elements) — proving Cayley's Theorem.

### 11.1 Tree → Prüfer Sequence

> [!Property] ⚙️ Algorithm: Labeled Tree → Prüfer Sequence
> **Input:** Labeled tree $T_0 = T$ on $n$ vertices. **Output:** Sequence $L = (a_1, \ldots, a_{n-2})$.
>
> **Step 1.** Initialize $L = \emptyset$, current tree $T_0 = T$.
>
> **Step 2.** Pick the leaf $u$ with the **smallest label** in the current tree. Let $a$ = label of $u$'s unique neighbor. Append $a$ to $L$. Remove $u$ from the tree.
>
> **Step 3.** Repeat Step 2 until exactly **2 vertices** remain. $L$ now has length $n-2$.

> [!Property] ⚙️ Key Lemma
> **1.** If vertex $i$ has degree $d_i$ in a labeled tree $T$, then $i$ appears exactly $d_i - 1$ times in its Prüfer sequence.
>
> **2.** **Leaves** of a labeled tree do **not** appear in the Prüfer sequence.

### 11.2 Prüfer Sequence → Tree

> [!Property] ⚙️ Algorithm: Prüfer Sequence → Labeled Tree
> **Input:** Prüfer sequence $P_0 = (a_1, \ldots, a_{n-2})$, $n$ labeled vertices. **Output:** Labeled tree.
>
> **Step 1.** Draw $n$ isolated vertices $\{1, \ldots, n\}$. Set leaf set $L_0 = [n] \setminus P_0$.
>
> **Step 2.** Connect smallest element of $L_0$ to first entry of $P_0$.
>
> **Step 3.** Update:
> $$P_i = P_{i-1} \setminus \{\text{first entry of } P_{i-1}\}$$
> $$L_i = (L_{i-1} \setminus \{\text{smallest leaf}\}) \cup \{\text{first entry of } P_{i-1} \text{ if not in } P_i\}$$
>
> **Step 4.** Repeat until $P_i = \emptyset$. Connect the two remaining nodes in $L_i$.

---

## 12. Spanning Trees

> [!Definition] 📖 Spanning Tree
> Let $G = (V, E)$ be an undirected simple graph. A subgraph $T = (V, E')$ is a **spanning tree** if it is a tree that contains **every vertex** of $V$.

> [!Theorem] 📌 Existence of Spanning Tree
> A graph $G$ is **connected** if and only if it has a spanning tree.

### 12.1 Generating Spanning Trees

> [!Property] ⚙️ Method 1: Remove Edges from Cycles
> Repeatedly find a simple cycle and remove one edge until no cycles remain. The resulting subgraph is a spanning tree.
>
> **Drawback:** Identifying cycles is expensive; not practical for large graphs.

> [!Property] ⚙️ Method 2: Depth-First Search (DFS)
> **i.** Choose a root vertex.
> **ii.** Extend a path as far as possible using edges to unvisited vertices.
> **iii.** If stuck, **backtrack** to the last vertex with unvisited neighbors and continue.
> **iv.** Repeat until all vertices are visited.
>
> Time complexity: $O(|V|^2)$ (or $O(|E|)$ with adjacency lists).

> [!Property] ⚙️ Method 3: Breadth-First Search (BFS)
> **i.** Choose a root.
> **ii.** Add all edges from root to neighbors (level 1).
> **iii.** For each level-$k$ vertex, add edges to unvisited neighbors (level $k+1$).
> **iv.** Repeat until all vertices are visited.
>
> Time complexity: $O(|V|^2)$ (or $O(|E|)$ with adjacency lists).

---

## 13. Counting Spanning Trees: Matrix-Tree Theorem

> [!Definition] 📖 Complexity of a Graph
> The **complexity** $\kappa(G)$ of a graph $G$ is its number of spanning trees.
>
> By Cayley's Theorem: $\kappa(K_n) = n^{n-2}$.

> [!Definition] 📖 Laplacian Matrix
> Let $G = (V, E)$ with $V = \{v_1, \ldots, v_n\}$. The **Laplacian matrix** $L$ is the $n \times n$ matrix:
> $$L_{ij} = \begin{cases} \deg(v_i) & \text{if } i = j \\ -1 & \text{if } i \neq j \text{ and } (v_i, v_j) \in E \\ 0 & \text{otherwise} \end{cases}$$
>
> Equivalently, $L = D - A$, where $D$ is the diagonal degree matrix ($D_{ii} = \deg(v_i)$) and $A$ is the adjacency matrix.
>
> **Remark:** $L$ is symmetric ($L = L^t$) and singular ($\det L = 0$).

> [!Theorem] 📌 Kirchhoff's Matrix-Tree Theorem (1847)
> Let $G$ be an undirected simple graph with Laplacian $L$. Then:
> $$\kappa(G) = \det \tilde{L}_j$$
> where $\tilde{L}_j$ is the matrix obtained from $L$ by deleting the $j$-th row and column (any $j$ gives the same result).

> [!Definition] 📖 Spanning Forest
> A **spanning forest** of $G$ is a forest (acyclic subgraph) that contains every vertex of $G$, such that two vertices are in the same tree of the forest iff there is a path between them in $G$.

> [!Property] ⚙️ Spanning Forest Facts
> - Number of trees in a spanning forest = number of connected components $c$ of $G$.
> - Edges to remove to produce a spanning forest from $G$ with $n$ vertices, $m$ edges, $c$ connected components: $m - (n - c)$.

---

## 14. Minimum Spanning Trees (MST)

> [!Definition] 📖 Weighted Graph and MST
> Given a graph $G = (V, E)$ and edge weight function $w: E \to \mathbb{R}$:
>
> - Weight of spanning tree $T$: $w(T) = \sum_{e \in T} w(e)$
> - A **minimum spanning tree (MST)** is a spanning tree with minimum total weight.
> - Every connected graph has an MST.

### 14.1 Cuts and Safe Edges

> [!Definition] 📖 Cut and Light Edge
> - A **cut** $(S, V \setminus S)$ partitions $V$ into two non-empty sets.
> - An edge **crosses** the cut if its endpoints are in different sets.
> - A **light edge** for a cut is a crossing edge with minimum weight.
> - A cut **respects** $A \subseteq E$ if no edge in $A$ crosses it.
> - A **safe edge** for $A$: if $A \subseteq$ some MST, then $uv$ is safe for $A$ iff $A \cup \{uv\}$ is also $\subseteq$ some MST.

> [!Lemma] 📌
> Let all edge weights be distinct. Let $X \subseteq V$. The smallest-weight edge connecting $X$ to $V \setminus X$ is in every MST.

> [!Theorem] 📌 Safe Edge Theorem
> Let $A \subseteq E$ be included in some MST. Let $(S, V \setminus S)$ be a cut that **respects** $A$, and let $uv$ be a **light edge** crossing the cut. Then $uv$ is **safe** for $A$.

### 14.2 Prim's Algorithm

> [!Property] ⚙️ Prim's Algorithm
> **Idea:** Grow a single tree from a start vertex by repeatedly adding the minimum-weight edge that connects the current tree to an outside vertex.
>
> **Algorithm:**
> **1.** Start: $T = \{s\}$ for arbitrary $s \in V$. Set $\text{key}(v) = \infty$ for all $v$; $\text{key}(s) = 0$.
>
> **2.** While $|T| < n$:
> - Find vertex $v \notin T$ with minimum $\text{key}(v)$.
> - Add $v$ to $T$, add edge $(\text{parent}(v), v)$ to tree.
> - For each neighbor $u$ of $v$ with $u \notin T$: if $w(v,u) < \text{key}(u)$, set $\text{key}(u) = w(v,u)$ and $\text{parent}(u) = v$.
>
> **Data structure:** Min-priority queue (min-heap or Fibonacci heap).
>
> **Correctness:** Based on the Safe Edge Theorem applied to the cut $(T, V \setminus T)$.

### 14.3 Kruskal's Algorithm

> [!Property] ⚙️ Kruskal's Algorithm
> **Idea:** Build MST by adding edges in non-decreasing weight order, skipping those that create a cycle.
>
> **Algorithm:**
> **1.** Sort all edges $E$ by weight (non-decreasing).
>
> **2.** Initialize: $T = \emptyset$. For each $v \in V$, $\text{MakeSet}(v)$.
>
> **3.** For each edge $e = uv$ in sorted order:
> - If $\text{FindSet}(u) \neq \text{FindSet}(v)$: add $e$ to $T$, call $\text{Union}(u,v)$.
>
> **4.** Stop when $|T| = n-1$. Return $T$.
>
> **Data structure:** Disjoint-set (union-find) structure.
>
> **Loop invariant:** Before each iteration, $T$ is a subset of some MST.

> [!Note] 💡 Prim vs Kruskal
> Both are **greedy** algorithms maintaining the invariant: *$T$ is a subset of some MST at every step*. Prim grows one connected component; Kruskal merges components.

---

## 📘 Examples & Applications

### Example 1 — Full $m$-ary Enumeration: 80 Leaves in 4-ary Tree

**Using:** Full $m$-ary tree enumeration theorem, $n = mi + 1$, leaves $= (m-1)i + 1$

Does there exist a full 4-ary tree with 80 leaves?

$$\text{Leaves} = (m-1)i + 1 = 3i + 1 = 80 \implies 3i = 79$$

Since $79$ is not divisible by $3$, $i$ is not an integer.

$$\boxed{\text{No full 4-ary tree with exactly 80 leaves exists.}}$$

---

### Example 2 — Chain Letter Game

**Using:** Full $m$-ary tree enumeration; $m = 4$, leaves $= 100$

Each person either sends to 4 others (internal node) or to no one (leaf). This is a **full 4-ary tree** ($m = 4$).

Leaves $= (m-1)i + 1 \implies 100 = 3i + 1 \implies i = 33$.

- Internal vertices (persons who sent letters): $i = 33$
- Total persons: $n = mi + 1 = 4 \cdot 33 + 1 = \mathbf{133}$
- Persons who received but did not send (leaves): $\mathbf{100}$

$$\boxed{133 \text{ persons received the letter total; } 33 \text{ sent it out.}}$$

---

### Example 3 — Decision Tree: Counterfeit Coin

**Using:** $m$-ary tree height bound; $l \leq m^h \implies h \geq \lceil \log_m l \rceil$

8 coins, 1 counterfeit (lighter). Balance scale has 3 outcomes per weighing.

- Outcomes per weighing: $m = 3$
- Possible solutions (which coin is fake): $l = 8$
- Minimum weighings: $h \geq \lceil \log_3 8 \rceil = \lceil 1.89 \rceil = 2$

**Construction:** Weigh coins $\{1,2,3\}$ vs $\{4,5,6\}$:
- Left lighter → fake is in $\{1,2,3\}$; weigh $1$ vs $2$: lighter is fake, or fake is $3$.
- Right lighter → symmetric.
- Balanced → fake is $7$ or $8$; weigh $7$ vs $8$.

$$\boxed{2 \text{ weighings are both necessary and sufficient.}}$$

---

### Example 4 — Sorting 3 Elements: Decision Tree Complexity

**Using:** Binary decision tree, $\lceil \log(n!) \rceil$ lower bound

$n = 3$: $\lceil \log(3!) \rceil = \lceil \log 6 \rceil = \lceil 2.58 \rceil = 3$.

The decision tree for 3 elements has 3 levels (height 3), confirming **3 comparisons worst-case**.

---

### Example 5 — Huffman Coding

**Using:** Huffman coding greedy algorithm

Letters with frequencies:
$$A: 0.08,\quad B: 0.10,\quad C: 0.12,\quad D: 0.15,\quad E: 0.20,\quad F: 0.35$$

**Step-by-step merging:**

| Step | Merged | New Weight | Remaining weights |
|------|--------|------------|-------------------|
| 1 | $A+B$ | $0.18$ | $0.12, 0.15, 0.18, 0.20, 0.35$ |
| 2 | $C+D$ | $0.27$ | $0.18, 0.20, 0.27, 0.35$ |
| 3 | $0.18+0.20$ | $0.38$ | $0.27, 0.35, 0.38$ |
| 4 | $0.27+0.35$ | $0.62$ | $0.38, 0.62$ |
| 5 | $0.38+0.62$ | $1.00$ | done |

Resulting codes: $A: 111,\quad B: 110,\quad C: 011,\quad D: 010,\quad E: 10,\quad F: 00$

Average bits per letter:
$$0.08 \times 3 + 0.10 \times 3 + 0.12 \times 3 + 0.15 \times 3 + 0.20 \times 2 + 0.35 \times 2$$
$$= 0.24 + 0.30 + 0.36 + 0.45 + 0.40 + 0.70 = \mathbf{2.45 \text{ bits}}$$

---

### Example 6 — Traversals

**Using:** Pre-order, in-order, post-order definitions

Tree:
```
        d
      / | \
     c  o   i
     |  |   |
     b  k   g   f
    / \     |  /|\
   h   l    e m  n
```

- **Pre-order:** $d, c, b, h, l, k, g, o, i, f, e, m, n$
- **In-order:** $h, b, l, c, k, g, d, o, e, f, m, n, i$
- **Post-order:** $h, l, b, k, g, c, o, e, m, n, f, i, d$

---

### Example 7 — Prefix and Postfix Evaluation

**Using:** Postfix/prefix evaluation rules, expression trees

**(a) Evaluate postfix:** $7\ 2\ 3 * - 4 \uparrow 9\ 3 / +$

| Step | Operation | Stack |
|------|-----------|-------|
| Push $7,2,3$ | — | $7,2,3$ |
| $*$: $2 \times 3 = 6$ | pop $2,3$ | $7,6$ |
| $-$: $7-6=1$ | pop $7,6$ | $1$ |
| Push $4$ | — | $1,4$ |
| $\uparrow$: $1^4 = 1$ | pop $1,4$ | $1$ |
| Push $9,3$ | — | $1,9,3$ |
| $/$: $9/3=3$ | pop $9,3$ | $1,3$ |
| $+$: $1+3=4$ | pop $1,3$ | $4$ |

$$\boxed{4}$$

**(b) Evaluate prefix:** $+\ -\ *\ 2\ 3\ 5\ /\ \uparrow\ 2\ 3\ 4$

Scan right to left, evaluate when operator followed by two operands:
- $2 \uparrow 3 = 8$; $8/4 = 2$
- $2 \times 3 = 6$; $6-5 = 1$
- $1 + 2 = 3$

$$\boxed{3}$$

Postfix: $2\ 3\ *\ 5\ -\ 2\ 3\ \uparrow\ 4\ /\ +$

---

### Example 8 — Prüfer Sequence from Labeled Tree

**Using:** Prüfer encoding algorithm

Tree (as in lecture):
```
        1
      / | \
     4  2   6
    /|\ |  /|\
   5  3 7 8   (leaves below)
   |           \
  10             9
```

Step-by-step (remove smallest leaf each time, record its neighbor):

| Step | Smallest leaf removed | Neighbor recorded |
|------|-----------------------|-------------------|
| 1 | $2$ | $1$ |
| 2 | $3$ | $4$ |
| 3 | $7$ | $6$ |
| 4 | $9$ | $8$ |
| 5 | $8$ | $6$ |
| 6 | $6$ | $1$ |
| 7 | $1$ | $4$ |
| 8 | $4$ | $5$ |

Stop (two vertices remain: $5, 10$).

$$\boxed{\text{Prüfer sequence} = (1, 4, 6, 8, 6, 1, 4, 5)}$$

---

### Example 9 — Laplacian and Matrix-Tree Theorem

**Using:** Laplacian matrix definition, Kirchhoff's theorem

Graph $G$: vertices $\{a, b, c, d\}$ with edges $ab, ac, bc, bd, cd$.

Degree sequence: $\deg(a)=2, \deg(b)=3, \deg(c)=3, \deg(d)=1$ (adjust per actual graph in notes).

For the graph in the lecture ($a$–$b$, $b$–$c$, $c$–$d$, $a$–$c$):

$$L = \begin{pmatrix} 2 & -1 & -1 & 0 \\ -1 & 2 & -1 & 0 \\ -1 & -1 & 3 & -1 \\ 0 & 0 & -1 & 1 \end{pmatrix}$$

Delete row/column 1:
$$\tilde{L}_1 = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 3 & -1 \\ 0 & -1 & 1 \end{pmatrix}$$

$$\kappa(G) = \det \tilde{L}_1 = 2(3\cdot1 - (-1)(-1)) - (-1)((-1)\cdot1 - (-1)\cdot0)$$
$$= 2(3-1) + 1(-1) = 4 - 1 = \mathbf{3}$$

---

### Example 10 — Kruskal's Algorithm Trace

**Using:** Kruskal's algorithm, union-find

Given graph with vertices $\{a,b,c,d,e,f,g,h,i\}$ and sorted edges (from lecture table):

| Edge | Weight | Action |
|------|--------|--------|
| $hg$ | 1 | Add |
| $gf$ | 2 | Add |
| $ic$ | 2 | Add |
| $ab$ | 4 | Add |
| $cf$ | 4 | Add (connects $\{i,c\}$ and $\{h,g,f\}$) |
| $hi$ | 7 | Skip ($h,i$ same component) |
| $cd$ | 7 | Add |
| $ah$ | 8 | Add (connects $\{a,b\}$ and big component) |
| $bc$ | 8 | Skip |
| $de$ | 9 | Add |

Final MST: $T = \{hg, gf, ic, ab, cf, cd, ah, de\}$, total 8 edges for 9 vertices. ✓

---

## 🗂️ Summary

**Trees — Fundamentals**
- Tree: connected + acyclic; $|V| = |E| + 1$
- 6 equivalent characterizations (connected, acyclic, unique paths, minimally connected, maximally acyclic)
- Every tree with $\geq 2$ vertices has at least one leaf

**$m$-ary Trees**
- Full $m$-ary: $n = mi + 1$; leaves $= (m-1)i + 1$
- Full binary tree: $2n+1$ vertices, $n$ internal, $n+1$ leaves
- Height bound: $l \leq m^h$, so $h \geq \lceil \log_m l \rceil$; equality holds for balanced full $m$-ary trees

**Decision Trees / Algorithmic Lower Bounds**
- Sorting: $\geq \lceil \log(n!) \rceil = \Theta(n \log n)$ comparisons
- Search in BST of length $n$: $\lceil \log(n+1) \rceil$ comparisons minimum

**Prefix Codes / Huffman**
- Prefix code: no codeword is prefix of another → unambiguous decode
- Huffman: greedy merge of two smallest weights; optimal prefix code

**Traversals / Expression Trees**
- Pre/in/post-order defined recursively
- In-order on BST = sorted order
- Prefix ↔ pre-order; postfix ↔ post-order; infix ↔ in-order

**Labeled Trees / Prüfer Sequences**
- Cayley: $n^{n-2}$ labeled trees on $n$ vertices
- Rooted: $n^{n-1}$; with degree sequence: $\frac{(n-2)!}{\prod (d_i-1)!}$
- Prüfer: bijection $\{\text{labeled trees}\} \leftrightarrow [n]^{n-2}$
- Vertex $i$ appears $d_i - 1$ times in Prüfer sequence; leaves don't appear

**Spanning Trees**
- $G$ connected $\iff$ has spanning tree
- DFS / BFS both generate spanning trees in $O(|V|^2)$
- $\kappa(G) = \det \tilde{L}_j$ (Kirchhoff, any $j$)
- Laplacian: $L = D - A$, symmetric, singular

**Minimum Spanning Trees**
- Safe edge theorem: light edge across any cut respecting $A \subseteq$ MST is safe
- **Prim:** grow one tree from a root, always add minimum key vertex; uses min-priority queue
- **Kruskal:** sort edges, add if connects different components; uses union-find
- Both greedy; invariant: current edge set $\subseteq$ some MST
