---
title: "Discrete Math — Trees: Exam Procedure Guide"
tags: [discrete-math, trees, graph-theory, exam-prep]
aliases: ["Trees Cheat Sheet", "DM Trees Guide"]
created: 2026-07-08
---

# 🌳 Trees — Exam Procedure Guide

> [!info] How to use this note
> Each section = a problem *type* from `DM-Trees.md`. For every type you get: **the procedure** (do these steps), **the cases** (what changes the answer), and **worked examples** tied to the original `[TR-x]` labels. Proofs are compressed to the one idea you actually need to reproduce.

## Contents
- [[#4.1 Tree Terminology & Basic Properties]]
- [[#4.2 Decision Trees & Comparison Algorithms]]
- [[#4.3 Prüfer Sequences & Labeled Trees]]
- [[#4.4 Spanning Trees & Matrix-Tree Theorem]]
- [[#4.5 Min Max Spanning Trees]]
- [[#4.6 Tree Traversal & Expression Trees]]
- [[#4.7 Graph Traversal (BFS DFS)]]
- [[#4.8 Backtracking]]
- [[#🧾 One-Page Formula Sheet]]

---

## 4.1 Tree Terminology & Basic Properties

> [!abstract] Definitions you must apply mechanically
> - **Root**: the given top node. **Level** of a node = number of edges from root (root is level 0).
> - **Internal** node = has ≥1 child. **Leaf** = has 0 children.
> - **Height of a (sub)tree** = length (edges) of the longest root-to-leaf path *inside it*.
> - **Ancestors of v** = every node on the path from `v` up to the root (excluding `v`). **Descendants of v** = everything in `v`'s subtree (excluding `v`).
> - **Balanced** (height `h`): *every* leaf sits at level `h` or `h−1`. One leaf higher up ⇒ **not** balanced.

### Reading a rooted tree — procedure
1. Draw it level by level from the root.
2. Tag each node as internal/leaf.
3. For level questions: count edges from root. For height of a subtree: re-root at that node and find its longest path.
4. Ancestors → walk *up*. Descendants → collect the whole subtree *below*.

> [!example] `[TR-1]` full walkthrough
> Tree: `d`→{a,c,o,i}; `c`→{b,k,g}; `b`→{h,l}; `i`→{f}; `f`→{e,m,n}; `h`→{p,q}.
>
> ```mermaid
> graph TD
> d --> a & c & o & i
> c --> b & k & g
> b --> h & l
> h --> p & q
> i --> f
> f --> e & m & n
> ```
> - **a. Root:** `d`
> - **b. Internal:** `d, c, b, h, i, f`
> - **c. Leaves:** `a, o, k, g, l, p, q, e, m, n`
> - **d. Level 3:** `h, l, e, m, n`  (d=0, {a,c,o,i}=1, {b,k,g,f}=2, then these)
> - **e. Height of subtree at `c`:** path `c→b→h→p` = **3**
> - **f. Descendants of `b`:** `h, l, p, q`
> - **g. Balanced?** Whole-tree height = 4 (`d-c-b-h-p`). Leaves exist at levels 1,2,3,4 → not all at 3 or 4 ⇒ **not balanced**.
> - **h. Ancestors of `q`:** `h, b, c, d`

### Counting non-isomorphic **unrooted** trees (small n)
Just enumerate by degree shape — memorize the tiny cases:

| n | # non-isomorphic trees | shapes |
|---|---|---|
| 3 | **1** `[TR-2]` | path |
| 4 | **2** `[TR-3]` | path `P₄`, star `K₁,₃` |
| 5 | 3 | path, star, "chair/Y" |

### Full *m*-ary tree formulas (the workhorse of 4.1)
Let `n`=vertices, `i`=internal, `l`=leaves, each internal node has exactly `m` children.

> [!abstract] Memorize
> $$n = mi + 1 \qquad l = n - i \qquad l = (m-1)i + 1$$
> $$i = \frac{n-1}{m} = \frac{l-1}{m-1}$$
> **Divisibility test:** a full *m*-ary tree needs $l \equiv 1 \pmod{m-1}$ (equivalently $m-1 \mid l-1$). At height `h`: at most $m^h$ leaves, and min height for `l` leaves is $\lceil \log_m l\rceil$.

**Case logic for "does such a tree exist?":**
1. Check $m-1 \mid (l-1)$. If it fails → **no tree**.
2. If a height `h` is required, check $l \le m^h$ (fits) **and** $\lceil\log_m l\rceil \le h$ (needs that much depth). Height is *forced* to be between $\lceil\log_m l\rceil$ and the deepest arrangement.

> [!example] `[TR-4]` leaves of full 3-ary tree, 100 vertices
> $i=(n-1)/m=99/3=33$, so $l=n-i=100-33=\mathbf{67}$.

> [!example] `[TR-5]` full *m*-ary, 84 leaves, height 3 — **does not exist**
> Need $m-1 \mid 83$. Since 83 is prime, $m\in\{2,84\}$. `m=2`: max leaves at height 3 is $2^3=8<84$. `m=84`: 84 leaves force $i=1$ (root only) → height 1. Neither gives height 3 ⇒ **no such tree**.

> [!example] `[TR-6]` full 4-ary, 80 leaves — **does not exist**
> $l\equiv 1 \pmod{3}$? $80 \equiv 2 \pmod 3$. Fails ⇒ **no**.

> [!example] `[TR-7]` full *m*-ary, height 4, 100 leaves — **exists**
> Need $m-1\mid 99=3^2\cdot 11$ ⇒ $m\in\{2,4,10,12,34,100\}$. Try **m = 4**: $4^4=256\ge100$ and $\lceil\log_4 100\rceil=4$, so height is forced to exactly 4. ✅ Works.

### Utility facts
- `[TR-8]` **Single-elimination tournament**, `n` players: each game eliminates one loser, need to eliminate `n−1` ⇒ **games = n − 1**. For 1000 players → **999**.
- `[TR-9]` **Forest** of `k` trees, `n` vertices ⇒ edges $= \mathbf{n-k}$.

### Binary Search Tree construction `[TR-10]`
**Procedure:** insert words in *sentence order*; at each node go **left if smaller**, **right if larger** (alphabetical); duplicates are dropped.

> [!example] "The quick brown fox jumps over the lazy dog" (case-insensitive; 2nd "the" dropped)
> ```mermaid
> graph TD
> the --> quick
> quick --> brown
> brown -.->|no left| x1[ ]:::e
> brown --> fox
> fox --> dog
> fox --> jumps
> jumps --> over
> over --> lazy
> classDef e fill:none,stroke:none;
> ```
> Insert order fixes structure: `the`(root) → `quick`(L) → `brown`(L of quick) → `fox`(R of brown) → then `dog`(L of fox), `jumps`(R of fox) → `over`(R of jumps) → `lazy`(L of over).

---

## 4.2 Decision Trees & Comparison Algorithms

> [!abstract] The one bound that solves most of these
> A decision procedure that must distinguish **N** outcomes needs depth (= worst-case tests):
> - **Balance scale** (3 outcomes/test): $\ge \lceil \log_3 N\rceil$ weighings.
> - **Comparison** (2 outcomes/test): $\ge \lceil \log_2 N\rceil$ comparisons.
> Then **construct** a tree meeting the bound to prove it's achievable.

### Counterfeit-coin weighings
**Procedure:** count outcomes `N` → lower bound $\lceil\log_3 N\rceil$ → design adaptive weighings so each of the 3 results (left<right, balance, left>right) splits suspects roughly into thirds.

> [!example] `[TR-11]` lighter coin among 4 (known lighter) → **2 weighings**
> $\lceil\log_3 4\rceil=2$. **Method:** weigh coin 1 vs 2. If one side rises, that coin is the light fake. If balanced, fake ∈ {3,4}: weigh 3 vs 4, the lighter is fake.

> [!example] `[TR-12]` counterfeit among 4, **heavier or lighter unknown** (Hard)
> There are $4\times2=8$ states → $\lceil\log_3 8\rceil = 2$ lower bound.
> **To just *identify the coin*: 2 weighings suffice.**
> W1: `1 vs 2`.
> - **Balanced** → 1,2 are genuine references. W2: `3 vs 1`. Equal ⇒ **4** is fake; unequal ⇒ **3** is fake.
> - **Unbalanced** (say 1<2) → fake is "1 light" or "2 heavy". W2: `1 vs 3` (3 genuine). `1<3` ⇒ **1** light; equal ⇒ **2** heavy.
> ⚠️ **Subtlety:** in the *balanced→balanced* branch you learn coin 4 is fake but **not** whether it's heavy/light. Determining direction for *every* case needs **3** weighings (with no reference coin, 2 weighings fully resolve only $\frac{3^2-3}{2}=3$ coins). State both readings in the exam.

> [!example] `[TR-52]` 101 coins, one odd (heavier **or** lighter), **2 weighings** (Hard)
> Naming *which* coin is impossible ($101>3^2$). The real task: **decide whether the odd coin is heavier or lighter.**
> W1: split `50 vs 50`, set 1 aside.
> - **Balanced** → the aside coin is the fake. W2: aside vs any genuine → down = heavier, up = lighter. (Bonus: coin identified.)
> - **Unbalanced** (heavier pan = H) → W2: take H's 50 coins, split `25 vs 25`. **Balanced** ⇒ fake was in the light pan ⇒ **lighter**; **unbalanced** ⇒ fake is in H ⇒ **heavier**.

### Decision-tree *induction* (classification) `[TR-13]`, `[TR-14]`
**Procedure:** pick an attribute that best separates the classes → branch on its values → recurse on each branch until every leaf is pure (one class) → read off the classification path.

> [!example] `[TR-13]` risk from {time, gender, area}
> Split on **area** first (it isolates a pure branch):
> ```mermaid
> graph TD
> A{area?} -->|urban| L1[low]
> A -->|rural| G{gender?}
> G -->|male| H1[high]
> G -->|female| T{time?}
> T -->|>7| L2[low]
> T -->|1-2| H2[high]
> ```
> Checks all 8 IDs correctly. **Max decisions to classify = 3** (area → gender → time).

> [!example] `[TR-14]` difficulty from L, M — the *trap*
> For **every** (L,M) pair the data has one `+` and one `−` (e.g. (0,0): Q1=−, Q2=+ …). The attributes carry **no information**. Any tree testing L then M reaches an impure leaf.
> **Classifying Q6 (L=1,M=0):** you make **2 decisions** (test L, test M) and land in the {Q5:−, Q6:+} leaf — the tree **cannot** resolve it. Key point to write: *this dataset is not separable by L and M.*

### Sorting lower bounds `[TR-15]`, `[TR-16]`
- **Lower bound to sort n items:** $\lceil \log_2 n!\rceil$ comparisons (leaves of the comparison tree = `n!` permutations).

> [!example] `[TR-15]` sort 4 elements (Hard) → **5 comparisons**
> $\lceil\log_2 24\rceil = 5$. **Algorithm (sort two pairs, then merge):**
> 1. Compare `a,b`; 2. Compare `c,d` → two sorted pairs.
> 3–5. Merge the two 2-element lists (≤3 comparisons). $2+3=5$, matching the bound.

> [!example] `[TR-16]` tournament sort — cost to extract 2nd … (n−1)st (Hard)
> - Build the knockout tournament for the **largest**: $n-1$ comparisons.
> - **2nd largest** only ever lost to the champion ⇒ it's among the $\lceil\log_2 n\rceil$ coins the champion beat ⇒ $\lceil\log_2 n\rceil - 1$ extra comparisons.
> - Each *subsequent* extraction "replays" one root-to-leaf path: $\lceil\log_2 n\rceil$ comparisons. Extracting the 2nd through (n−1)st (that's $n-2$ elements) costs $\approx (n-2)\lceil\log_2 n\rceil$.
> - **Total** $\approx (n-1) + (n-2)\lceil\log_2 n\rceil = O(n\log n)$.

---

## 4.3 Prüfer Sequences & Labeled Trees

> [!abstract] The Prüfer dictionary (n vertices ↔ sequence of length n−2 over {1..n})
> - $\deg(v) = (\text{times } v \text{ appears in the code}) + 1$. **Never-appearing = leaf.**
> - **Cayley:** $\#\text{labeled trees} = n^{n-2}$.

### Decode: sequence → tree
1. From the code compute every degree.
2. Maintain the set of current **leaves** (degree 1). Repeat for each code entry `s` (left→right): take the **smallest-labeled leaf** `v`, add edge `{v,s}`, decrement `deg(v)` and `deg(s)`; if `s` drops to degree 1 it becomes a leaf.
3. After the code is consumed, **two** vertices remain at degree 1 — join them.

> [!example] `[TR-17]` code `(1,1,1,1,6,5)` → n=8
> Degrees: 1→5; 5,6→2; 2,3,4,7,8→1. Pairing smallest leaves with entries gives edges:
> `{2,1},{3,1},{4,1},{7,1},{1,6},{6,5},{5,8}`.
> ```mermaid
> graph TD
> 1 --- 2 & 3 & 4 & 7 & 6
> 6 --- 5
> 5 --- 8
> ```

> [!example] `[TR-18]` code `(10,9,8,7,6,5,4,3)` → **a path**
> Result is the path `1 – 10 – 3 – 4 – 5 – 6 – 7 – 8 – 9 – 2`.

> [!example] `[TR-19]` code `(1,2,3,4,5,6,7,8)` → **a path**
> Result is the path `9 – 1 – 2 – 3 – 4 – 5 – 6 – 7 – 8 – 10`.

> [!tip] Pattern to remember
> A **strictly increasing / all-distinct** code always decodes to a **path** (see `[TR-21]`).

### Encode: tree → sequence
Repeat $n-2$ times: find the **smallest-labeled leaf**, **record its unique neighbor**, delete the leaf. Stop at 2 vertices.

> [!example] `[TR-20]` encode two trees
> **Tree 1** (edges `{1,9},{1,5},{5,2},{5,3},{5,8},{2,6},{8,4},{9,7},{7,10}`):
> remove leaves in order 3,4,6,2,8,5,1,9 → record neighbours →
> **Prüfer = (5, 8, 2, 5, 5, 1, 9, 7).**
> **Tree 2** (edges `{2,3},{2,8},{3,4},{3,7},{3,9},{4,1},{8,6},{8,10},{6,5}`):
> **Prüfer = (4, 3, 6, 8, 3, 3, 2, 8).**
> *(Check: node with degree `d` appears `d−1` times — verify before submitting.)*

### Counting labeled trees (all via Prüfer)

> [!abstract] Formulas
> - Fixed degrees $d_1,\dots,d_n$ on labeled vertices: $\dfrac{(n-2)!}{\prod_i (d_i-1)!}$ (multinomial — vertex `i` appears $d_i-1$ times).
> - Vertex `n` has degree exactly `k`: $\dbinom{n-2}{k-1}(n-1)^{\,n-1-k}$.
> - Labeled **rooted** trees: $n^{n-1}$.
> - Labeled **rooted forests** with `k` trees: $\dbinom{n-1}{k-1} n^{\,n-k}$.
> - Trees with **all-distinct** Prüfer entries = **paths**: $\dfrac{n!}{2}$.

> [!example] `[TR-21]` distinct-entry codes
> All $n-2$ entries distinct ⇒ every appearing vertex has degree 2, exactly 2 leaves ⇒ **path**. Count = number of labeled paths = $\boxed{n!/2}$ (an ordering of vertices, halved for the reverse).

> [!example] `[TR-22]` labeled trees on 6 vertices by degree sequence
> Use $\dfrac{(n-2)!}{\prod(d_i-1)!}$ **per labeling**, then ×(ways to assign the degrees to the 6 labels) for the whole **multiset**:
>
> | degree seq | per-labeling $\frac{4!}{\prod(d_i-1)!}$ | # label assignments | **total (multiset)** |
> |---|---|---|---|
> | (5,1,1,1,1,1) | $24/24=1$ | 6 | **6** (the 6 stars) |
> | (4,2,1,1,1,1) | $24/6=4$ | 30 | **120** |
> | (3,2,2,1,1,1) | $24/2=12$ | 60 | **720** |
> | (2,2,2,2,1,1) | $24/1=24$ | 15 | **360** (= labeled paths $6!/2$ ✓) |
>
> ⚠️ Read the question: if it fixes *which* vertex has which degree, answer with the **per-labeling** column (1, 4, 12, 24). If it means the degree **multiset**, use the **total** column.

> [!example] `[TR-23]` deg of vertex `n` equals `k`
> `n` appears $k-1$ times in a length-$(n-2)$ code: choose those positions $\binom{n-2}{k-1}$, fill the rest with the other $n-1$ labels: $(n-1)^{n-1-k}$.
> $$\#=\binom{n-2}{k-1}(n-1)^{\,n-1-k}.$$

> [!example] `[TR-24]` labeled rooted trees → $n^{n-1}$
> $n^{n-2}$ trees × `n` root choices. **Uniform generator:** draw a uniform random length-$(n-2)$ string over `{1..n}` (⇒ uniform tree by the bijection), then pick a root uniformly.

> [!example] `[TR-25]` rooted forests, `k` components → $\binom{n-1}{k-1}n^{\,n-k}$
> Sanity: $k=1$ gives $n^{n-1}$ (rooted trees ✓); $n=3,k=2$ gives $2\cdot3=6$ ✓.

> [!note] `[TR-34]` Matrix-Tree on $K_n$ (technique, not full proof)
> Laplacian $L=nI-J$. Reduced Laplacian (drop last row/col) $=nI_{n-1}-J_{n-1}$. Eigenvalues of $J_{n-1}$ are $n-1$ (once) and $0$ ($n-2$ times) ⇒ eigenvalues of the reduced matrix are $1$ and $n$ (×$(n-2)$). Determinant $=1\cdot n^{n-2}=n^{n-2}$ ⇒ re-proves Cayley.

---

## 4.4 Spanning Trees & Matrix-Tree Theorem

> [!abstract] Core facts
> - Spanning tree of a connected graph on `n` vertices has $n-1$ edges.
> - **Spanning forest** has one tree per component ⇒ `# trees = # connected components` `[TR-28]`; it has $n-c$ edges.
> - Edges to delete to reach the spanning forest ($n$ vertices, $m$ edges, $c$ comps): $\mathbf{m-n+c}$ `[TR-29]`.

### Finding *one* spanning tree `[TR-26]`
Run **BFS/DFS**, keep only the tree edges (skip any edge to an already-visited vertex).

| graph | a spanning tree |
|---|---|
| $K_5$ | any path/star on 5 vertices (4 edges) |
| $C_5$ | delete one edge → path |
| $K_{1,6}$ | already a tree (itself) |
| $K_{2,3}$ (parts {a,b},{x,y,z}) | `a-x, a-y, a-z, b-x` |
| $Q_3$ | any DFS tree (7 edges) |

### Matrix-Tree Theorem — counting *all* spanning trees
> [!abstract] Procedure
> 1. Build **Laplacian** $L = D - A$ (degree on diagonal, $-1$ per edge).
> 2. Delete **any one** row and the same-index column → **reduced Laplacian** $\tilde L$.
> 3. $\kappa(G) = \det \tilde L$ (any cofactor of $L$ works).

> [!example] `[TR-27]` $C_5$
> 5 spanning trees (delete any one of the 5 edges → a path).
> $$L=\begin{pmatrix}2&-1&0&0&-1\\-1&2&-1&0&0\\0&-1&2&-1&0\\0&0&-1&2&-1\\-1&0&0&-1&2\end{pmatrix},\quad
> \tilde L=\begin{pmatrix}2&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&2\end{pmatrix}$$
> $\det\tilde L = 5$ ✓. **General:** $\kappa(C_n)=n$.

> [!example] `[TR-30]` spanning-tree counts (Hard)
> | graph | # spanning trees |
> |---|---|
> | a. $K_{2,2}$ | $4$ (it's $C_4$) |
> | b. $C_n$ | $n$ |
> | c. $K_{1,n}$ | $1$ (it's a tree) |
> | d. $K_{m,n}$ | $m^{\,n-1}\,n^{\,m-1}$ |
> | e. $Q_3$ | $384$ |
> | f. $W_n$ (hub + $C_n$) | $\left(\tfrac{3+\sqrt5}{2}\right)^{n}+\left(\tfrac{3-\sqrt5}{2}\right)^{n}-2$ |
>
> *(Check f: $W_3=K_4$ gives $16=4^{2}$ ✓.)*

### Structural criteria
- `[TR-31]` **Exactly one** spanning tree ⟺ the graph **is** a tree (no cycle to break differently).
- `[TR-32]` An edge is in **every** spanning tree ⟺ it is a **bridge** (cut edge). A non-bridge lies on a cycle and can be avoided.

> [!note] `[TR-33]`, `[TR-35]`, `[TR-36]` (idea only)
> - `[TR-33]` path-length bound: DFS-tree argument — no simple path of length `k` bounds DFS depth, limiting edges to $\le (k-1)n$.
> - `[TR-35]` cut-vertex multiplicativity $\kappa(G)=\prod\kappa_i$: spanning trees of `G` are independent choices of a spanning tree in each block glued at `v` ⇒ Matrix-Tree factorizes as a product.
> - `[TR-36]` (Rosen 11.5 #1, #8): standard **Prim/Kruskal** exercises on a given figure — apply [[#4.5 Min Max Spanning Trees]]. *(No figure supplied here; use the algorithm below.)*

---

## 4.5 Min / Max Spanning Trees

> [!abstract] The two algorithms
> - **Kruskal:** sort edges ascending; add an edge if it doesn't form a cycle (union-find); stop at $n-1$ edges.
> - **Prim:** grow from a start vertex; repeatedly add the cheapest edge leaving the current tree.

### Maximum spanning tree `[TR-37]`
**Procedure:** either negate all weights and run MST, **or** run Kruskal/Prim picking the **largest** valid edge each step (sort descending). Correctness is the same cut/cycle argument mirrored.

> [!note] `[TR-38]` unique MST when weights distinct (idea)
> If two different MSTs existed, take the min-weight edge in their symmetric difference and do a cut/cycle swap — with all weights distinct the swap strictly lowers weight, contradiction ⇒ MST is unique.

### Second-best MST `[TR-39]` (Hard)
1. Compute the MST `T` (weight `W`).
2. For each **non-tree** edge `e=(u,v)`: adding `e` to `T` makes one cycle. Let `f` be the **max-weight tree edge** on the `u–v` tree path (with `f≠e`).
3. The swap `T − f + e` is a spanning tree of weight `W − w(f) + w(e)`.
4. **Second-best MST** = the swap minimizing `w(e) − w(f)` over all non-tree edges.
   (Precompute max-edge-on-path for all pairs in $O(V^2)$ or via LCA.)

### Kruskal with bounded integer weights `[TR-40]` (Hard)
- Weights in $1..|V|$: replace comparison sort with **counting sort** ⇒ edges sorted in $O(E+V)$. Total Kruskal $= O(E\,\alpha(V))$ (near-linear), sorting no longer the bottleneck.
- Weights in $1..k$ (constant `k`): counting sort is $O(E)$ ⇒ Kruskal runs in **$O(E\,\alpha(V))$**, effectively linear.

---

## 4.6 Tree Traversal & Expression Trees

> [!abstract] Traversal → notation
> - **Preorder** (node, L, R) → **prefix** (Polish).
> - **Inorder** (L, node, R) → **infix** (needs parentheses).
> - **Postorder** (L, R, node) → **postfix** (Reverse Polish).

### Building an expression tree
Top operator (lowest precedence, evaluated last) is the **root**; recurse into each operand.

> [!example] `[TR-41]` $\big((x+2)^3\big)\big(y-(3+x)\big)-5$
> Root `−`; left = product, right = `5`.
> - **Prefix:** `− · ↑ + x 2 3 − y + 3 x 5`
> - **Postfix:** `x 2 + 3 ↑ y 3 x + − · 5 −`
> - **Infix:** $\big((x+2)\uparrow 3\big)\cdot\big(y-(3+x)\big)-5$

> [!example] `[TR-42]` propositions
> **P1:** $\lnot(p\land q)\leftrightarrow(\lnot p\lor\lnot q)$
> - Prefix: `↔ ¬ ∧ p q ∨ ¬ p ¬ q`
> - Postfix: `p q ∧ ¬ p ¬ q ¬ ∨ ↔`
> - Infix: $(\lnot(p\land q))\leftrightarrow((\lnot p)\lor(\lnot q))$
>
> **P2:** $(\lnot p\land(q\leftrightarrow\lnot p))\lor\lnot q$
> - Prefix: `∨ ∧ ¬ p ↔ q ¬ p ¬ q`
> - Postfix: `p ¬ q p ¬ ↔ ∧ q ¬ ∨`
> - Infix: $((\lnot p)\land(q\leftrightarrow(\lnot p)))\lor(\lnot q)$

### Evaluating prefix / postfix
> [!abstract] Stack rules
> - **Prefix:** scan **right→left**; push operands; on an operator pop two, **first popped = left operand**, push result.
> - **Postfix:** scan **left→right**; push operands; on an operator pop two, **second popped = left operand**, push result.

> [!example] `[TR-43]` prefix values
> - a. `− * 2 / 8 4 3` → $/(8,4)=2,\ *(2,2)=4,\ -(4,3)=\mathbf{1}$
> - b. `↑ − * 3 3 * 4 2 5` → $9-8=1,\ 1^5=\mathbf{1}$
> - c. `+ − ↑ 3 2 ↑ 2 3 / 6 − 4 2` → $(9-8)+(6/2)=1+3=\mathbf{4}$

> [!example] `[TR-44]` postfix values
> - a. `5 2 1 − − 3 1 4 + + *` → $(5-(2-1))\cdot((1+4)+3)=4\cdot8=\mathbf{32}$
> - b. `9 3 / 5 + 7 2 − *` → $(9/3+5)\cdot(7-2)=8\cdot5=\mathbf{40}$
> - c. `3 2 * 2 ↑ 5 3 − 8 4 / * −` → $6^2-((5-3)\cdot(8/4))=36-4=\mathbf{32}$

### Well-formed prefix formulae `[TR-45]`
> [!abstract] Test (binary operators only)
> Scan **right→left**, counter starts 0: **symbol** → `+1`; **operator** → requires counter ≥ 2, then `−1`. It's a WFF iff the counter never goes below the requirement and **ends at exactly 1**. Equivalent quick check: `#symbols = #operators + 1` **and** every suffix stays valid.

> [!example] `[TR-45]` over {x,y,z}, ops {×,+,∘}
> - a. `× + + x y x` — 3 symbols, 3 ops → not $=+1$ ⇒ **No**
> - b. `∘ x y × x z` — 4 symbols, 2 ops ⇒ **No**
> - c. `× ∘ x z × × x y` — scan fails (operator with only 1 operand available) ⇒ **No**
> - d. `× + ∘ x x ∘ x x x` — 5 symbols, 4 ops, scan valid, ends at 1 ⇒ **Yes** = $\times\big(+(\circ xx)(\circ xx)\big)\,x$

> [!note] `[TR-46]` "#symbols = #operators + 1" (idea)
> Structural induction: a lone symbol has (1,0). Combining two WFFs with a binary operator adds their counts and one operator, preserving `symbols − operators = 1`.

---

## 4.7 Graph Traversal (BFS / DFS)

> [!abstract] Templates
> - **BFS:** queue, process by increasing distance (levels). Best for **shortest paths** in unweighted graphs and **bipartiteness**.
> - **DFS:** stack/recursion, dives deep. Best for **cycles** and **components** (works for both, though).

> [!example] `[TR-47]` shortest path length via BFS
> BFS from `s`, store `dist[s]=0`; when you first pop a vertex `u` and relax an unvisited neighbor `w`, set `dist[w]=dist[u]+1` and record parent. `dist[t]` is the shortest-path length; follow parents back for the path. Correct because BFS discovers vertices in nondecreasing distance order.

> [!example] `[TR-48]` cycle detection
> DFS with parent tracking. If you reach an already-visited vertex `w` that **isn't the parent** of the current vertex → **back edge → cycle**. Recover it by walking parent pointers from both endpoints of that edge up to their meeting point.

> [!example] `[TR-49]` connected components
> Loop over vertices; each time you hit an **unvisited** one, launch a BFS/DFS, label everything reached with the current component id, then increment the counter. Final counter = number of components.

> [!example] `[TR-50]` bipartite test (2-coloring)
> BFS/DFS assigning alternating colors (`color[neighbor] = 1 − color[current]`). If you ever find an edge joining **same-colored** vertices → **not bipartite** (an odd cycle exists). If coloring completes → bipartite; the two colors are the parts. Apply per-component for the `a`–`l` graph.

---

## 4.8 Backtracking

> [!abstract] Subset-sum backtracking `[TR-51]`
> Process numbers in the given order. Maintain a running sum.
> 1. **Include** the next number only if `sum + number ≤ M`.
> 2. If `sum = M` → **success**.
> 3. If no remaining number can be added without exceeding `M` (and `sum ≠ M`) → **dead end**: backtrack by dropping the most recently added number and try excluding it.
> Draw the search as a tree: each node = a partial sum; branches = include/skip.

> [!example] `[TR-51]` set $\{27,24,19,14,11,8\}$
> **a. M = 20 → NO SOLUTION.** 27,24 too big; 19 alone, 14 alone, 11+8=19 — nothing reaches 20. Every branch dead-ends.
> ```mermaid
> graph TD
> R["{ } = 0"] --> N19["+19 = 19 ✗"]
> R --> N14["+14 = 14 ✗"]
> R --> N11["+11 = 11"]
> N11 --> N118["+8 = 19 ✗"]
> R --> N8["+8 = 8 ✗"]
> ```
> **b. M = 41 → {27, 14}.** Include 27; 24,19 overshoot; +14 = 41 ✓.
> ```mermaid
> graph TD
> R["{ } = 0"] --> A["+27 = 27"]
> A -->|+24=51 ✗| X1[ ]
> A -->|+19=46 ✗| X2[ ]
> A --> B["+14 = 41 ✓"]
> ```
> **c. M = 60 → {27, 19, 14}.** Include 27; try 24 → 51 → dead-ends (max reach 59); backtrack, skip 24; +19 = 46; +14 = 60 ✓.
> ```mermaid
> graph TD
> R["{ } = 0"] --> A["+27 = 27"]
> A --> C["+24 = 51"]
> C --> C8["+8 = 59 ✗ (backtrack)"]
> A --> D["skip 24, +19 = 46"]
> D --> E["+14 = 60 ✓"]
> ```

---

## 🧾 One-Page Formula Sheet

> [!summary] Grab-and-go
> **Full m-ary tree:** $n=mi+1$, $l=(m-1)i+1$, exists only if $m-1\mid l-1$; height `h` ⇒ $\lceil\log_m l\rceil\le h$ and $l\le m^h$.
> **Forest:** $n$ vertices, $k$ trees ⇒ $n-k$ edges. Spanning forest of $c$-component graph: $n-c$ edges; delete $m-n+c$.
> **Tournament:** `n` players ⇒ `n−1` games.
>
> **Prüfer:** tree $n$ ↔ code length $n-2$; $\deg v = (\#\text{appearances})+1$.
> - all trees: $n^{n-2}$ • rooted trees: $n^{n-1}$ • rooted forests, $k$ trees: $\binom{n-1}{k-1}n^{n-k}$
> - fixed degrees: $\frac{(n-2)!}{\prod(d_i-1)!}$ • vertex `n` has deg `k`: $\binom{n-2}{k-1}(n-1)^{n-1-k}$ • paths: $n!/2$
>
> **Spanning trees $\kappa(G)=\det(\text{reduced Laplacian})$:**
> $C_n=n$ • $K_n=n^{n-2}$ • $K_{m,n}=m^{n-1}n^{m-1}$ • $K_{1,n}=1$ • $Q_3=384$ • $W_n=\big(\tfrac{3+\sqrt5}{2}\big)^n+\big(\tfrac{3-\sqrt5}{2}\big)^n-2$.
> Unique spanning tree ⟺ graph is a tree. Edge in every spanning tree ⟺ bridge.
>
> **Decision-tree bounds:** distinguish `N` outcomes ⇒ $\ge\lceil\log_3 N\rceil$ weighings / $\lceil\log_2 N\rceil$ comparisons. Sort `n`: $\lceil\log_2 n!\rceil$ (4 elements → 5).
>
> **Notation:** preorder=prefix, inorder=infix, postorder=postfix. Prefix eval → scan right-to-left; postfix eval → left-to-right. Prefix WFF ⟺ #symbols = #operators + 1 (with valid suffix scan).
