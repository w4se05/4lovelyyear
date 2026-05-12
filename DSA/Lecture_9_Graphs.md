---
tags: [61CSE108, graphs, BFS, DFS, MST, Dijkstra, data-structures]
topic: "Lecture 9: Graphs"
course: "61CSE108 – Algorithms and Data Structures"
---

> [!Note] 💡 Notation Conventions
> - $G = (V, E)$ — a graph with vertex set $V$ and edge set $E$.
> - $|V| = n$ — number of vertices; $|E| = m$ — number of edges.
> - $\deg(v)$ — degree of vertex $v$.
> - $w(u,v)$ or $w(e)$ — weight of edge $(u,v)$ or edge $e$.
> - $c(u)$ — current shortest-path cost estimate to vertex $u$ in Dijkstra's algorithm.
> - $T$ — the spanning tree under construction (Prim's / Dijkstra's).
> - $\bar{T} = V \setminus T$ — vertices not yet in $T$.
> - Undirected edge written $\{u,v\}$; directed edge written $(u,v)$.
> - $O(V)$ and $O(E)$ abbreviate $O(|V|)$ and $O(|E|)$.

---

# Lecture 9 — Graphs

## 1. Introduction & Motivation

Graphs model pairwise relationships between objects. Applications include map colouring, network routing, circuit design, maze generation, and shortest-path navigation.

**Historical origin:** Euler (1736) solved the Königsberg bridges problem using graph reasoning — the first published result in graph theory.

**Königsberg problem:** Is there a walk through Königsberg crossing each of the 7 bridges exactly once and returning to the start? Answer: **No** (proven via Euler circuits; all four vertices have odd degree).

---

## 2. Definitions and Basic Properties

> [!Definition] 📖 Graph (Definition 1.1)
> A **graph** $G$ consists of:
> - A nonempty set $V(G)$ of **vertices** (also called nodes).
> - A set $E(G)$ of **edges**, where each edge is associated with a set of one or two vertices called its **endpoints**.
>
> We write $G = (V, E)$ and $e = \{v, w\}$ for an edge $e$ incident on vertices $v$ and $w$.
>
> - Two vertices connected by an edge are **adjacent**.
> - An edge whose two endpoints are the same vertex is a **loop**.
> - Two or more edges connecting the same pair of vertices are **parallel edges**.
> - A vertex with no incident edges is **isolated**.

> [!Definition] 📖 Directed Graph (Definition 1.2)
> A **directed graph (digraph)** $G$ consists of vertices $V(G)$ and **directed edges** $D(G)$, where each edge is an **ordered pair** $(v, w)$ — the edge goes **from** $v$ **to** $w$.

> [!Definition] 📖 Simple Graph
> A **simple graph** is an undirected graph with **no loops and no parallel edges**.

> [!Definition] 📖 Complete Graph $K_n$
> A **complete graph** $K_n$ ($n > 0$) is a simple graph with $n$ vertices and exactly **one edge between every pair of distinct vertices**.
> Total edges: $\binom{n}{2} = \frac{n(n-1)}{2}$.

> [!Definition] 📖 Complete Bipartite Graph $K_{m,n}$ (Definition 1.3)
> $K_{m,n}$ is a simple graph with vertices $v_1, \ldots, v_m$ and $w_1, \ldots, w_n$ satisfying:
> **1.** There is an edge from each $v_i$ to each $w_j$.
> **2.** No edge between any two $v_i$'s.
> **3.** No edge between any two $w_j$'s.

> [!Definition] 📖 Subgraph (Definition 1.4)
> $H$ is a **subgraph** of $G$ if every vertex and edge of $H$ is also in $G$ with the same endpoints.

> [!Definition] 📖 Degree (Definition 1.5)
> The **degree** of a vertex $v$, written $\deg(v)$, equals the number of edges incident on $v$, with **loops counted twice**.
> The **total degree** of $G$ is $\sum_{v \in V} \deg(v)$.

> [!Theorem] 📌 Theorem 1.1 — Handshake Theorem
> For any graph $G$ with vertices $v_1, \ldots, v_n$:
> $$\sum_{i=1}^{n} \deg(v_i) = 2|E|.$$

> [!Proof] 🔷 Proof sketch
> Each edge contributes exactly 2 to the total degree sum (one for each endpoint). $\blacksquare$

> [!Property] ⚙️ Corollaries of the Handshake Theorem
> - **Corollary 1.1:** The total degree of any graph is even.
> - **Corollary 1.2:** In any graph, there are an **even number** of vertices of odd degree.

---

## 3. Walks, Trails, Paths, Circuits

> [!Definition] 📖 Walk, Trail, Path (Definition 1.6)
> Let $G$ be a graph, $v, w \in V(G)$.
> - A **walk** from $v$ to $w$: a finite alternating sequence $v_0 e_1 v_1 e_2 \cdots e_n v_n$ where $v_0 = v$, $v_n = w$, and $e_i$ connects $v_{i-1}$ to $v_i$. The **trivial walk** from $v$ to $v$ is just $v$.
> - A **trail**: a walk with **no repeated edges**.
> - A **path**: a trail with **no repeated vertices**.

> [!Definition] 📖 Closed Walk, Circuit, Simple Circuit (Definition 1.7)
> - **Closed walk**: starts and ends at the same vertex.
> - **Circuit (cycle)**: a closed walk with at least one edge and **no repeated edge**.
> - **Simple circuit (simple cycle)**: a circuit with **no repeated vertex** except first = last.

| Type | Repeated edge? | Repeated vertex? | Starts = Ends? | ≥ 1 edge? |
|---|---|---|---|---|
| Walk | Allowed | Allowed | Allowed | No |
| Trail | No | Allowed | Allowed | No |
| Path | No | No | No | No |
| Closed walk | Allowed | Allowed | Yes | No |
| Circuit | No | Allowed | Yes | Yes |
| Simple circuit | No | First & last only | Yes | Yes |

> [!Warning] ⚠️ Terminology Warning
> Graph theory terminology is **not standardized** across sources. Some sources use "path" for what this course calls "trail", "simple path" for "path", and "cycle" for "simple circuit". Always verify definitions when consulting other resources.

---

## 4. Connectedness

> [!Definition] 📖 Connected Graph (Definition 1.8)
> Two vertices $v$ and $w$ are **connected** if there exists a walk from $v$ to $w$.
> A graph $G$ is **connected** iff for every pair of vertices $v, w \in V(G)$, there exists a walk from $v$ to $w$.

> [!Definition] 📖 Connected Component (Definition 1.9)
> A **connected component** of $G$ is a subgraph $H$ such that:
> **1.** $H$ is a subgraph of $G$.
> **2.** $H$ is connected.
> **3.** No connected subgraph of $G$ properly contains $H$.

> [!Definition] 📖 Bridge and Vertex Cut (Definition 1.10)
> - An edge $e$ is a **bridge** if removing it disconnects $G$.
> - A vertex $v$ is a **vertex cut** if removing it (and all its incident edges) disconnects $G$.

> [!Property] ⚙️ Lemma 1.1 — Useful Connectivity Facts
> **1.** If $G$ is connected, any two distinct vertices can be connected by a **path**.
> **2.** If vertices $v, w$ are part of a circuit and one edge of the circuit is removed, there still exists a trail from $v$ to $w$.
> **3.** If $G$ is connected and contains a circuit, one edge of the circuit can be removed without disconnecting $G$.

---

## 5. Euler Circuits and Trails

> [!Definition] 📖 Euler Circuit (Definition 1.11)
> An **Euler circuit** for $G$ is a circuit that contains every vertex and every edge of $G$ exactly once, starting and ending at the same vertex.

> [!Theorem] 📌 Theorem 1.2 — Necessary Condition
> If $G$ has an Euler circuit, then **every vertex has positive even degree**.

> [!Theorem] 📌 Theorem 1.3 — Sufficient Condition
> If $G$ is connected and **every vertex has positive even degree**, then $G$ has an Euler circuit.

> [!Theorem] 📌 Theorem 1.4 — IFF Condition (Euler Circuit)
> $G$ has an Euler circuit $\iff$ $G$ is connected and every vertex has **positive even degree**.

> [!Definition] 📖 Euler Trail (Definition 1.12)
> An **Euler trail** from $v$ to $w$ ($v \neq w$) is a sequence of adjacent edges/vertices that starts at $v$, ends at $w$, passes through every vertex at least once, and traverses every edge exactly once.

> [!Property] ⚙️ Corollary 1.3 — Euler Trail Condition
> There is an Euler trail from $v$ to $w$ $\iff$ $G$ is connected, $v$ and $w$ have **odd degree**, and all other vertices have **positive even degree**.

### 5.1 Hierholzer's Algorithm

> [!Definition] 📖 Hierholzer's Algorithm
> Given a connected graph $G$ with all even-degree vertices:
>
> **1.** Find an initial circuit $R_1$. Mark its edges. Set $i = 1$.
> **2.** If $R_i$ contains all edges of $G$, stop ($R_i$ is the Euler circuit).
> **3.** Otherwise, find a vertex $v_i$ on $R_i$ incident with an unmarked edge $e_i$.
> **4.** Build a new circuit $Q_i$ starting at $v_i$ using $e_i$. Mark edges of $Q_i$.
> **5.** Create $R_{i+1}$ by splicing $Q_i$ into $R_i$ at $v_i$. Increment $i$, go to Step 2.
>
> **Complexity:** $O(V + E)$ (each step costs: $O(E)$ for finding initial circuit, $O(V)$ for finding vertex with unmarked edge, $O(E)$ for building sub-circuit, $O(1)$ for splicing with linked lists).

### 5.2 Fleury's Algorithm

> [!Definition] 📖 Fleury's Algorithm
> Given an Euler graph $G$ with all edges unmarked, choose any starting vertex $v$:
>
> **1.** Choose vertex $v$ as the "lead vertex."
> **2.** If all edges are marked, stop.
> **3.** Among edges incident on the lead vertex, choose — if possible — one that is **not a bridge** of the subgraph of unmarked edges. If no such choice exists, use any edge. Mark it; let its other endpoint be the new lead.
> **4.** Go to Step 2.
>
> **Complexity:** Up to $O(E^2)$ due to repeated bridge checking.

| Feature | Hierholzer's | Fleury's |
|---|---|---|
| Approach | Circuit patching | Greedy, avoid bridges |
| Time | $O(V+E)$ | $O(E^2)$ |
| Bridge check | Not needed | Required each step |
| Practical use | Preferred (efficient) | Educational only |

---

## 6. Hamiltonian Circuits

> [!Definition] 📖 Hamiltonian Circuit (Definition 1.13)
> A **Hamiltonian circuit** for $G$ is a **simple circuit** that includes every vertex of $G$ exactly once (except first = last).

> [!Warning] ⚠️ Key Contrast with Euler Circuits
> - Euler circuit: visits every **edge** exactly once; may repeat vertices.
> - Hamiltonian circuit: visits every **vertex** exactly once; may omit edges.
> - No known efficient algorithm (analogous to Theorem 1.4) exists for Hamiltonian circuits.

> [!Property] ⚙️ Proposition 1 — Necessary Conditions for Hamiltonian Circuit
> If $G$ has a Hamiltonian circuit, then $G$ has a subgraph $H$ with:
> **1.** $H$ contains every vertex of $G$.
> **2.** $H$ is connected.
> **3.** $H$ has the same number of edges as vertices.
> **4.** Every vertex of $H$ has degree 2.
>
> The **contrapositive** is used to show a graph does **not** have a Hamiltonian circuit.

> [!Note] 💡 Travelling Salesman Problem (TSP)
> The TSP asks: find a Hamiltonian circuit of minimum total weight.
> - For $n = 30$: approximately $4.4 \times 10^{30}$ circuits to check.
> - The TSP is **NP-complete** — no known polynomial-time exact algorithm.
> - Efficient **approximation algorithms** exist.

---

## 7. Graph Representations

### 7.1 Adjacency Matrix

> [!Definition] 📖 Adjacency Matrix
> For a graph with $n$ vertices, the **adjacency matrix** $A$ is an $n \times n$ matrix where:
> $$A_{ij} = \begin{cases} w & \text{if edge } (i,j) \text{ exists with weight } w \\ 0 \text{ (or } \infty\text{)} & \text{otherwise} \end{cases}$$
>
> - **Undirected graph:** $A$ is **symmetric** ($A_{ij} = A_{ji}$).
> - **Directed graph:** $A$ may be **asymmetric**.
> - **Space cost:** $O(V^2)$.

> [!Theorem] 📌 Walks of Length $n$
> If $A$ is the adjacency matrix of graph $G$ with vertices $v_1, \ldots, v_m$, then for each positive integer $n$ and all $i, j$:
> $$\text{The } (i,j)\text{-th entry of } A^n = \text{number of walks of length } n \text{ from } v_i \text{ to } v_j.$$

> [!Theorem] 📌 Block Diagonal Form
> If $G$ has connected components $G_1, G_2, \ldots, G_k$ with $n_i$ vertices each (numbered consecutively), then:
> $$A = \begin{pmatrix} A_1 & O & \cdots & O \\ O & A_2 & \cdots & O \\ \vdots & & \ddots & \vdots \\ O & O & \cdots & A_k \end{pmatrix}$$
> where $A_i$ is the adjacency matrix of $G_i$ and $O$ denotes zero matrices.

### 7.2 Adjacency List

> [!Definition] 📖 Adjacency List
> Each vertex stores a list of its neighbors (and edge weights if applicable).
> - **Space cost:** $O(V + E)$ — preferred for **sparse graphs**.

**Undirected example (vertex A with neighbors B (weight 6) and C (weight 2)):**
```
A → B,6 → C,2
B → A,6 → C,7 → D,1 → E,4 → F,5
```

**Directed:** each vertex only lists vertices it has **outgoing** edges to.

---

## 8. Graph Isomorphism

> [!Definition] 📖 Graph Isomorphism
> Graphs $G$ and $G'$ are **isomorphic** iff there exist one-to-one correspondences $g: V(G) \to V(G')$ and $h: E(G) \to E(G')$ such that for all $v \in V(G)$ and $e \in E(G)$:
> $$v \text{ is an endpoint of } e \iff g(v) \text{ is an endpoint of } h(e).$$
>
> For **simple graphs**, this reduces to: $\{u,v\} \in E(G) \iff \{g(u), g(v)\} \in E(G')$.

> [!Theorem] 📌 Isomorphism is an Equivalence Relation
> Graph isomorphism is reflexive, symmetric, and transitive on any set of graphs.

> [!Definition] 📖 Isomorphism Invariant
> A property $P$ is an **isomorphism invariant** if: $G$ has $P$ and $G \cong G'$ implies $G'$ has $P$.

> [!Theorem] 📌 Isomorphism Invariants
> The following are all isomorphism invariants ($n, m, k$ non-negative integers):
> **1.** Has $n$ vertices.
> **2.** Has a vertex of degree $k$.
> **3.** Has a circuit of length $k$.
> **4.** Has $m$ simple circuits of length $k$.
> **5.** Has an Euler circuit.
> **6.** Has $m$ edges.
> **7.** Has $m$ vertices of degree $k$.
> **8.** Has a simple circuit of length $k$.
> **9.** Is connected.
> **10.** Has a Hamiltonian circuit.

> [!Warning] ⚠️ Isomorphism is Hard
> Checking isomorphism in general requires up to $n! \cdot m!$ function-pair checks. For $n = m = 25$: $\approx 2.4 \times 10^{50}$ pairs — infeasible. Use invariants to **disprove** isomorphism quickly.

---

## 9. Graph Traversals

### 9.1 Breadth-First Search (BFS)

> [!Definition] 📖 BFS Algorithm
> **BFS** starts at a source vertex, visits all neighbors at distance 1, then distance 2, etc. Uses a **queue**.
>
> ```
> BFS(G, start):
>   dist[u] ← ∞  for all u
>   colour[u] ← white  for all u
>   dist[start] ← 0
>   colour[start] ← gray
>   Q ← [start]
>   while Q ≠ ∅:
>     u ← Q.pop()
>     for v in neighbors(u):
>       if colour[v] = white:
>         dist[v] ← dist[u] + 1
>         colour[v] ← gray
>         Q.push(v)
>     colour[u] ← black
> ```
>
> **Complexity:** $O(V + E)$ time and space.

> [!Property] ⚙️ BFS Properties
> - Finds the **shortest path** (fewest edges) from the source to every reachable vertex.
> - Vertex colours: white = unvisited, gray = discovered/queued, black = fully explored.

**BFS Applications:**

**1. Check connectedness:** Run BFS from any node. If no node has $\text{dist} = \infty$, the graph is connected.

**2. Find connected components:**
```
label[1..n] ← 0;  id ← 1
for u ← 1 to n:
  if label[u] = 0:
    Q ← [u];  label[u] ← id
    while Q ≠ ∅:
      v ← Q.pop()
      for w in neighbors(v):
        if label[w] = 0:
          label[w] ← id;  Q.push(w)
    id ← id + 1
```

**3. Detect cycles:** During BFS, if a discovered (gray) neighbor is encountered, a cycle exists.

**4. Compute multi-source shortest distance:** Initialize the queue with all source vertices at distance 0, then run BFS normally. Each cell receives the distance from its nearest source.

### 9.2 Depth-First Search (DFS)

> [!Definition] 📖 DFS — Recursive
> **DFS** explores as far as possible along each branch before backtracking.
>
> ```
> DFS(v):
>   Mark v as visited
>   for each unvisited vertex u adjacent to v:
>     DFS(u)
> ```

> [!Definition] 📖 DFS — Stack-based
> ```
> DFS(v):
>   s ← new empty stack
>   s.push(v);  Mark v as visited
>   while s is not empty:
>     if no unvisited vertices adjacent to top(s):
>       s.pop()
>     else:
>       u ← an unvisited neighbor of top(s)
>       s.push(u);  Mark u as visited
> ```

> [!Property] ⚙️ BFS vs DFS
> - **BFS** uses a queue; finds shortest paths (fewest edges); explores by level.
> - **DFS** uses a stack (or recursion); explores deeply before backtracking; path to a vertex may not be shortest.

---

## 10. Minimum Spanning Trees (MST)

> [!Definition] 📖 Spanning Tree and MST
> A **spanning tree** of a connected graph $G$ is a subgraph that:
> - Includes **all vertices** of $G$.
> - Is a **tree** (connected, no cycles).
>
> A **minimum spanning tree (MST)** is a spanning tree with **minimum total edge weight**.
>
> An MST of a graph with $|V|$ vertices has exactly $|V| - 1$ edges.

> [!Note] 💡 When MSTs exist
> An MST exists iff the graph is **connected** and **weighted**.

> [!Property] ⚙️ MST Cut Property (Lemma 1)
> Given a connected weighted undirected graph $G = (V, E)$ and a cut $(S, V - S)$, let $e = \{u,v\}$ be an edge crossing the cut ($u \in S$, $v \in V-S$). Then:
> **1.** If $e$ has strictly minimum weight among all crossing edges, $e$ is in **every** MST of $G$.
> **2.** If multiple edges tie for minimum weight crossing the cut, at least one is in **some** MST of $G$.

> [!Proof] 🔷 Proof of Part 1 (by contradiction)
> Suppose MST $M^*$ does not contain $e = \{u,v\}$. Since $M^*$ connects $S$ and $V-S$, there is a path in $M^*$ from $u$ to $v$, which must cross the cut via some edge $\{x,y\}$.
>
> By assumption, $w(e) < w(\{x,y\})$. Form $M' = M^* \cup \{e\} \setminus \{\{x,y\}\}$. This is still a spanning tree. Then:
> $$w(M') = w(M^*) - w(\{x,y\}) + w(e) < w(M^*).$$
> This contradicts $M^*$ being an MST. $\blacksquare$

### 10.1 Prim's Algorithm

> [!Definition] 📖 Prim's Algorithm
> Grows the MST one vertex at a time from an arbitrary start vertex.
>
> ```
> PrimMST(V, E, start r):
>   inTree[r] := true;  parent[r] := r
>   Q := min-heap of edges from r
>   while Q not empty:
>     (w, u, v) := Q.extractMin()
>     if not inTree[v]:
>       inTree[v] := true;  parent[v] := u
>       for each edge (v, z):
>         if not inTree[z]:
>           Q.insert((weight(v,z), v, z))
>   return parent
> ```
>
> At each step: pick the minimum-weight edge $\{u,v\}$ with $u \in T$ and $v \notin T$; add $v$ to $T$.
>
> **Complexity:** $O((V + E) \log V)$ with a binary heap.

> [!Proof] 🔷 Correctness of Prim's (by induction on $|V|$)
> - **Base case:** correct for $|V| = 2, 3$.
> - **Inductive step:** Consider a cut $(S, V-S)$ with $|V-S| = 1$, vertex $u$. Let $F$ be all edges with one endpoint $u$. Let $e \in F$ be the minimum-weight edge. By the Cut Property, $e$ is in some MST. The inductive hypothesis applies to $G_S$ (induced subgraph on $S$). The tree $T \cup \{e\}$ is an MST of $G$. $\blacksquare$

> [!Property] ⚙️ Prim's: Best for dense graphs; uses adjacency list or matrix + priority queue.

### 10.2 Kruskal's Algorithm

> [!Definition] 📖 Kruskal's Algorithm
> Greedily adds edges sorted by weight, skipping those that would create a cycle.
>
> ```
> KruskalMST(V, E):
>   Sort all edges by weight (non-decreasing)
>   T := ∅
>   for each edge e in sorted order:
>     if e does not create a cycle in T:
>       T := T ∪ {e}
>     if |T| = |V| - 1: stop
>   return T
> ```
>
> Cycle detection uses a **Union-Find** (Disjoint Set Union) data structure.
>
> **Complexity:** $O(E \log E) = O(E \log V)$ (sorting dominates).

> [!Proof] 🔷 Correctness of Kruskal's (loop invariant)
> **Loop invariant:** every edge added to $T$ is part of some MST.
>
> The cycle check ensures $T$ is always acyclic. Since Kruskal's always picks the minimum-weight edge that doesn't form a cycle, by the Cut Property, each selected edge belongs to some MST. At termination, $T$ has $|V|-1$ edges (spanning tree) with minimum total weight. $\blacksquare$

| Feature | Kruskal's | Prim's |
|---|---|---|
| Approach | Edge-based | Vertex-based |
| Best for | Sparse graphs | Dense graphs |
| Data structure | Union-Find | Priority Queue (Heap) |
| Time | $O(E \log E)$ | $O((V+E) \log V)$ |
| Input format | Edge list | Adjacency list/matrix |

---

## 11. Shortest Paths: Dijkstra's Algorithm

> [!Definition] 📖 Dijkstra's Problem
> Given a connected weighted undirected graph $G = (V, E)$ with non-negative edge weights and a source vertex $s$, find for each vertex $u$ the shortest-weight path from $s$ to $u$.

> [!Definition] 📖 Dijkstra's Algorithm
> Like Prim's, but the priority is the **cumulative path cost** from $s$, not the edge weight alone.
>
> ```
> DIJKSTRA(G, s):
>   T := ({s}, ∅)
>   c[s] := 0;  c[u] := ∞  for all u ≠ s
>   v := s;  F := {s}
>   while all vertices not in T:
>     F := (∪_{k ∈ V(T)} Adj(k)) \ V(T)        // fringe
>     for u in Adj(v) \ V(T):
>       if c[v] + w(v,u) < c[u]:
>         c[u] := c[v] + w(v,u)
>         previous[u] := v
>     x := argmin_{p ∈ F} c[p]                 // fringe min
>     V(T) := V(T) ∪ {x}
>     E(T) := E(T) ∪ {{previous[x], x}}
>     v := x
>   return c
> ```
>
> **Complexity:** $O(V^2)$ with the above (adjacency-matrix style, no heap). With a binary heap and adjacency list: $O((V+E) \log V)$.

> [!Property] ⚙️ Dijkstra Key Concepts
> - **Tree $T$**: shortest-path tree under construction, starting from $s$.
> - **Fringe $F$**: vertices adjacent to $T$ but not yet in $T$.
> - **$c[u]$**: current best cost from $s$ to $u$.
> - **$\text{previous}[u]$**: the predecessor of $u$ on the current shortest path.
> - At each step, the fringe vertex with **minimum $c$ value** is added to $T$.
> - After adding $v$ to $T$, only update costs for neighbors of $v$ not yet in $T$.

> [!Warning] ⚠️ Dijkstra requires non-negative edge weights. It does NOT work with negative weights.

---

## 📘 Examples & Applications

### Example 1 — Handshake Theorem

**Using:** Theorem 1.1, degree sum.

**Problem:** A graph has 6 vertices with degrees 3, 3, 3, 3, 2, 2. How many edges does it have?

**Solution:**
$$\text{Total degree} = 3+3+3+3+2+2 = 16 = 2|E| \implies |E| = 8.$$

---

### Example 2 — Euler Circuit Check

**Using:** Theorem 1.4.

**Graph (1):** All 6 vertices have even degree → **has an Euler circuit**.

**Graph (3):** Two vertices have odd degree → **no Euler circuit, but has an Euler trail** between those two odd-degree vertices (Corollary 1.3).

---

### Example 3 — Hierholzer's Algorithm

**Using:** Hierholzer's algorithm, Euler circuit.

**Graph:** vertices $\{a, b, c, d, e, f, g, h, i, j\}$ with edges forming a connected graph where all degrees are even.

**Starting circuit:** $R_1 = e, g, h, i, e$.

**Step 1:** Vertex $e$ has unmarked edges. Build $Q_1 = e, f, h, j, e$.
Splice: $R_2 = e, f, h, j, e, g, h, i, e$.

**Step 2:** Vertex $e$ has unmarked edges. Build $Q_2 = e, c, a, b, d, e$.
Splice: $R_3 = e, c, a, b, d, e, f, h, j, e, g, h, i, e$.

**Step 3:** Vertex $c$ has unmarked edges. Build $Q_3 = c, d, h, c$.
Splice: $R_4 = e, c, d, h, c, a, b, d, e, f, h, j, e, g, h, i, e$. **Stop.**

---

### Example 4 — BFS Shortest Distance

**Using:** BFS, graph-as-grid model.

**Problem:** A virus starts at one cell in a grid. Each day it spreads to all adjacent cells (up/down/left/right). How many days until all cells are infected?

**Solution:** Model cells as vertices, adjacency as edges. Run BFS from the source. $\text{dist}[c]$ = day cell $c$ gets infected. Answer = maximum distance from source.

**With obstacles:** simply do not enqueue fire/ocean cells.

**With multiple virus sources:** initialize queue with all sources at distance 0. BFS naturally computes each cell's distance to its nearest source.

---

### Example 5 — Prim's MST (Networking Problem)

**Using:** Prim's algorithm, MST.

**Graph:** 10 data centers A–J with weighted edges. Find MST starting from $h$.

**Execution trace (edges selected in order):**

| Step | Edge Added | Cost $L$ |
|---|---|---|
| 1 | $\{h,j\}$, weight 6 | 6 |
| 2 | $\{j,i\}$, weight 7 | 13 |
| 3 | $\{i,g\}$, weight 9 | 22 |
| 4 | $\{g,d\}$, weight 7 | 29 |
| 5 | $\{d,a\}$, weight 1 | 30 |
| 6 | $\{a,b\}$, weight 2 | 32 |
| 7 | $\{b,c\}$, weight 3 | 35 |
| 8 | $\{a,e\}$, weight 6 | 41 |
| 9 | $\{g,f\}$, weight 8 | **49** |

**MST edges:** $\{h,j\}, \{j,i\}, \{i,g\}, \{g,d\}, \{d,a\}, \{a,b\}, \{b,c\}, \{a,e\}, \{g,f\}$ — **Total cost: 49**.

---

### Example 6 — Kruskal's MST

**Using:** Kruskal's algorithm, cycle detection, MST.

**Same 10-node graph.** Edges sorted by weight:

$$1,2,3,4,5,6,6,7,7,8,9,9,9,10,11,12,14$$

Edges added (no cycle formed):
$(A,D), (A,B), (B,C), (A,E), (H,J), (D,G), (I,J), (F,G)$ — 8 edges.

Skipped edges (would form cycles): $(C,D), (A,C), (G,I), (H,I), (D,E), (G,H), (D,H), (F,I)$.

**Total cost: 49.** Same MST as Prim's (MST not always unique, but cost is).

---

### Example 7 — Dijkstra's Shortest Paths

**Using:** Dijkstra's algorithm, shortest-path tree.

**Graph:** 10 vertices A–J, source = A. Full trace condensed to final table:

| Step | $A$ | $B$ | $C$ | $D$ | $E$ | $F$ | $G$ | $H$ | $I$ | $J$ | $V(T)$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0,A | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | $\{A\}$ |
| 1 | 0,A | 2,A | 5,A | 1,A | 6,A | ∞ | ∞ | ∞ | ∞ | ∞ | $\{A\}$ |
| 2 | 0,A | 2,A | 5,A | 1,A | 6,A | ∞ | 8,D | 13,D | ∞ | ∞ | $\{A,D\}$ |
| 3 | 0,A | 2,A | 5,A | 1,A | 6,A | ∞ | 8,D | 13,D | ∞ | ∞ | $\{A,D,B\}$ |
| 4 | 0,A | 2,A | 5,A | 1,A | 6,A | ∞ | 8,D | 13,D | ∞ | ∞ | $\{A,D,B,C\}$ |
| 5 | 0,A | 2,A | 5,A | 1,A | 6,A | 15,E | 8,D | 13,D | ∞ | ∞ | $\{A,D,B,C,E\}$ |
| 6 | 0,A | 2,A | 5,A | 1,A | 6,A | 15,E | 8,D | 13,D | 17,G | ∞ | $\{A,D,B,C,E,G\}$ |
| 7 | 0,A | 2,A | 5,A | 1,A | 6,A | 15,E | 8,D | 13,D | 17,G | 19,H | $\{A,D,B,C,E,G,H\}$ |
| 8 | 0,A | 2,A | 5,A | 1,A | 6,A | 15,E | 8,D | 13,D | 17,G | 19,H | $\{A,D,B,C,E,G,H,F\}$ |
| 9 | 0,A | 2,A | 5,A | 1,A | 6,A | 15,E | 8,D | 13,D | 17,G | 19,H | $\{A,...,I\}$ |

**Final shortest-path tree edges:** $(A,D), (A,B), (A,C), (A,E), (D,G), (G,H), (G,F), (G,I), (H,J)$.

**Shortest distances from A:** A=0, B=2, C=5, D=1, E=6, F=15, G=8, H=13, I=17, J=19.

---

### Example 8 — Isomorphism Invariant Check

**Using:** Isomorphism invariants, contrapositive of Proposition.

**Problem:** Show two graphs are NOT isomorphic.

**Method:** Find an invariant one graph has and the other lacks. For example:
- Graph 1 has 5 vertices all of degree 3. Graph 2 has 5 vertices with degrees 2, 2, 3, 3, 4. They differ on "has $m$ vertices of degree $k$" → **not isomorphic**.

---

## 🗂️ Summary

**Graph basics:**
- $G = (V, E)$; undirected or directed. Key terms: adjacent, incident, loop, parallel edge, isolated.
- Simple graph: no loops, no parallel edges.
- $K_n$: $\binom{n}{2}$ edges. $K_{m,n}$: $m \times n$ edges, bipartite.

**Degrees:** $\sum \deg(v) = 2|E|$ (Handshake Theorem); total degree always even; even number of odd-degree vertices.

**Walk/Trail/Path/Circuit hierarchy:**
Walk ⊇ Trail (no repeated edge) ⊇ Path (no repeated vertex).
Closed walk ⊇ Circuit (no repeated edge, ≥1 edge) ⊇ Simple circuit (no repeated vertex except endpoints).

**Euler circuit:** exists $\iff$ connected + all vertices even degree.
**Euler trail** ($v$ to $w$, $v \neq w$): exists $\iff$ connected + exactly $v, w$ have odd degree.
**Hierholzer:** $O(V+E)$. **Fleury:** $O(E^2)$.

**Hamiltonian circuit:** visits every vertex once; no efficient general algorithm; NP-complete (TSP).

**Representations:**
- Adjacency matrix: $O(V^2)$ space; symmetric for undirected; $A^n_{ij}$ counts walks of length $n$.
- Adjacency list: $O(V+E)$ space; preferred for sparse graphs.
- Connected components → block-diagonal adjacency matrix.

**Isomorphism:** $G \cong G'$ via bijective vertex/edge maps preserving adjacency. Invariants: $|V|$, $|E|$, degree sequence, circuit lengths, connectivity, Euler/Hamiltonian circuits.

**BFS:** $O(V+E)$; shortest paths (fewest edges); level-order exploration; queue.
**DFS:** $O(V+E)$; deep exploration; stack or recursion.

**MST:** spanning tree with minimum total weight. Has $|V|-1$ edges.
- **Cut Property:** minimum-weight crossing edge belongs to some MST.
- **Prim's:** vertex-based; $O((V+E) \log V)$ with heap; dense graphs.
- **Kruskal's:** edge-based; $O(E \log E)$; sparse graphs; Union-Find.

**Dijkstra:** shortest paths from source; $O(V^2)$ naive, $O((V+E)\log V)$ with heap; non-negative weights only.
Key update rule: if $c[v] + w(v,u) < c[u]$, update $c[u]$ and $\text{previous}[u]$.
