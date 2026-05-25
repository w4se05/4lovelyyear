---
tags: [graphs, discrete-math, 61CSE108, algorithms, cheatsheet]
topic: "Graph Theory — Master Cheatsheet"
sources: "Lecture 9 (61CSE108) + DM Chapter 10 Parts 1 & 2"
---

# 📊 Graph Theory — Master Cheatsheet

> [!Note] 💡 Notation Conventions
> - $G = (V, E)$, $n = |V|$ (vertices), $m = e = |E|$ (edges), $f$ (faces in planar graph)
> - Undirected edge: $\{u,v\}$ or $uv$; Directed edge: $(u,v)$
> - $\deg(v)$ — degree; $\deg^+(v)$ — out-degree; $\deg^-(v)$ — in-degree
> - $w(u,v)$ — edge weight; $c[u]$ — shortest-path cost estimate to $u$ (Dijkstra)
> - $T$ — spanning tree under construction; $\bar{T} = V \setminus T$ — vertices not yet in $T$

---

## 1. Definitions

> [!Definition] 📖 Graph Types
> | Type | Multiple edges? | Loops? | Directed? |
> |---|---|---|---|
> | Simple graph | No | No | No |
> | Multigraph | Yes | Yes | No |
> | Simple digraph | No | No | Yes |
> | Multidigraph | Yes | Yes | Yes |
>
> - **Loop**: edge from a vertex to itself
> - **Adjacent**: vertices sharing an edge; **Incident**: vertex touching an edge
> - **Isolated**: vertex with no incident edges

> [!Definition] 📖 Degree
> - **Undirected:** $\deg(v) =$ number of incident edges (loops count **twice**)
> - **Directed:** $\deg^+(v)$ = out-edges, $\deg^-(v)$ = in-edges
> - **Neighborhood:** $N(v) = \{u \mid uv \in E\}$

> [!Theorem] 📌 Handshake Theorem
> $$\sum_{v \in V} \deg(v) = 2|E|$$
> **Digraph version:** $\displaystyle\sum_v \deg^+(v) = \sum_v \deg^-(v) = |E|$
>
> **Corollaries:** Total degree is always even. Number of odd-degree vertices is always **even**.

---

## 2. Special Graphs

> [!Property] ⚙️ Edge Counts
> | Graph | $V$ | $E$ | Every degree | Bipartite? |
> |---|---|---|---|---|
> | $K_n$ | $n$ | $\dfrac{n(n-1)}{2}$ | $n-1$ | iff $n \leq 2$ |
> | $C_n$ | $n$ | $n$ | $2$ | iff $n$ even |
> | $W_n$ | $n+1$ | $2n$ | hub: $n$, rim: $3$ | Never |
> | $Q_n$ | $2^n$ | $n \cdot 2^{n-1}$ | $n$ | Always |
> | $K_{m,n}$ | $m+n$ | $mn$ | $V_1$: $n$, $V_2$: $m$ | Always |

> [!Note] 💡 Bipartiteness Rules
> - **Bipartite** ↔ 2-colorable ↔ no **odd-length** cycles
> - $Q_n$: partition by parity of number of 1-bits in binary label
> - $K_{1,n}$ is the **star graph** (hub + $n$ leaves)

---

## 3. Walk / Trail / Path Hierarchy

| Type | Repeated edge? | Repeated vertex? | Starts = Ends? |
|---|---|---|---|
| Walk | ✅ | ✅ | Optional |
| Trail | ❌ | ✅ | Optional |
| Path | ❌ | ❌ | No |
| Closed walk | ✅ | ✅ | Yes |
| Circuit | ❌ | ✅ | Yes, ≥1 edge |
| Simple circuit | ❌ | ❌ (except endpoints) | Yes |

> [!Warning] ⚠️ Terminology varies by textbook — always check definitions.

---

## 4. Connectivity

> [!Definition] 📖 Connected Graphs
> - **Connected** (undirected): path exists between every pair of vertices
> - **Connected component**: maximal connected subgraph
> - **Cut vertex** (articulation point): removing it increases component count
> - **Bridge** (cut edge): removing it increases component count

> [!Definition] 📖 Directed Connectivity
> - **Strongly connected**: directed path from $u$ to $v$ AND $v$ to $u$, for all pairs
> - **Weakly connected**: underlying undirected graph is connected
> - **SCC** (strongly connected component): maximal strongly connected subgraph
> - Strongly connected ⟹ weakly connected (not converse)

> [!Property] ⚙️ Connectivity Facts
> 1. Connected ⟹ any two vertices joinable by a **path**
> 2. Vertices on a circuit stay connected after removing one circuit edge
> 3. Connected graph with a circuit: removing one circuit edge stays connected

---

## 5. Eulerian Paths & Circuits

> [!Theorem] 📌 Eulerian Circuit ↔ all vertices even degree (connected graph)
> $$G \text{ has Euler circuit} \iff G \text{ connected and every } \deg(v) \text{ even}$$

> [!Theorem] 📌 Eulerian Path (no circuit): exactly 2 vertices have odd degree
> - Path runs **between** the two odd-degree vertices

> [!Warning] ⚠️ Digraph conditions
> - Circuit: $\deg^+(v) = \deg^-(v)$ for every vertex
> - Path: exactly one vertex with $\deg^+ - \deg^- = 1$ (start), one with $\deg^- - \deg^+ = 1$ (end)

> [!Property] ⚙️ Euler Paths/Circuits for Special Graphs
> | Graph | Euler Circuit? | Euler Path (no circuit)? |
> |---|---|---|
> | $K_n$ | Yes iff $n$ odd ($n \geq 3$) | Yes iff $n$ even ($n \geq 2$) |
> | $C_n$ | Always (all deg = 2) | No |
> | $W_n$ | Never | Never (for standard $n \geq 3$) |
> | $Q_n$ | Yes iff $n$ even | Yes iff $n$ odd |
> | $K_{m,n}$ | Yes iff both $m,n$ even | Yes iff exactly one of $m,n$ odd |

### Algorithms

> [!Definition] 📖 Hierholzer's Algorithm — $O(V+E)$ ⭐ (preferred)
> 1. Find initial circuit $R_1$; mark its edges
> 2. If all edges marked → done
> 3. Find vertex $v_i$ on $R_i$ with an unmarked edge; build sub-circuit $Q_i$ from $v_i$
> 4. Splice $Q_i$ into $R_i$ at $v_i$ → $R_{i+1}$; repeat

> [!Definition] 📖 Fleury's Algorithm — $O(E^2)$ (educational only)
> At each step: traverse any non-bridge edge if possible; otherwise traverse a bridge. Mark traversed edges.

---

## 6. Hamiltonian Paths & Circuits

> [!Definition] 📖 Hamiltonian
> - **Hamiltonian path**: visits every **vertex** exactly once
> - **Hamiltonian circuit**: visits every vertex exactly once and returns to start
> - **Key contrast:** Euler covers all **edges**; Hamilton covers all **vertices**

> [!Warning] ⚠️ No known simple necessary-and-sufficient condition — NP-hard (related to TSP)

> [!Theorem] 📌 Sufficient Conditions (not necessary)
> For simple graph $G$ with $n \geq 3$ vertices:
> - **Dirac:** $\deg(v) \geq \dfrac{n}{2}$ for all $v$ ⟹ Hamilton circuit exists
> - **Ore:** $\deg(u) + \deg(v) \geq n$ for every non-adjacent pair ⟹ Hamilton circuit exists

> [!Property] ⚙️ Hamilton for Special Graphs
> | Graph | Hamilton Circuit? | Hamilton Path? |
> |---|---|---|
> | $K_n$, $n \geq 3$ | ✅ | ✅ |
> | $C_n$ | ✅ (the cycle itself) | ✅ |
> | $W_n$ | ✅ ($h \to v_1 \to \cdots \to v_n \to h$) | ✅ |
> | $Q_n$, $n \geq 2$ | ✅ (Gray code) | ✅ |
> | $K_{m,n}$ | ✅ iff $m = n$ | ✅ iff $\|m-n\| \leq 1$ |
> | Petersen graph | ❌ | — |

> [!Note] 💡 Necessary Conditions for Hamilton Circuit (Proposition 1)
> If $G$ has a Hamilton circuit, $G$ has a subgraph $H$ where: all vertices included, $H$ connected, $|E(H)| = |V(H)|$, every vertex in $H$ has degree 2. Use **contrapositive** to disprove.

---

## 7. Graph Representations

> [!Definition] 📖 Adjacency Matrix
> $A_{ij} = w(i,j)$ if edge exists, else $0$ (or $\infty$ for weighted)
> - Undirected: $A$ is **symmetric**; Directed: $A$ may be asymmetric
> - Row sum = $\deg(v_i)$ (undirected) / $\deg^+(v_i)$ (directed)
> - Column sum (directed) = $\deg^-(v_j)$
> - **Space:** $O(V^2)$
>
> **Walks via powers:** $(A^r)_{ij}$ = number of walks of length $r$ from $v_i$ to $v_j$
>
> **Disconnected graphs** → block-diagonal $A$

> [!Definition] 📖 Adjacency List
> Each vertex stores list of neighbors (+ weights). **Space:** $O(V+E)$ — preferred for sparse graphs.

> [!Definition] 📖 Laplacian Matrix $L = D - A$
> $$L_{ij} = \begin{cases} \deg(v_i) & i = j \\ -1 & v_iv_j \in E \\ 0 & \text{otherwise} \end{cases}$$
> All row sums = 0; $L$ is symmetric.

> [!Definition] 📖 Incidence Matrix $M$ ($n \times m$)
> $m_{ij} = 1$ if vertex $v_i$ incident to edge $e_j$, else $0$.
> Column sums = 2 for each edge; row sums = degrees.

---

## 8. Graph Isomorphism

> [!Definition] 📖 Isomorphism
> $G \cong G'$ iff there exists a bijection $f: V(G) \to V(G')$ such that:
> $$\{u,v\} \in E(G) \iff \{f(u), f(v)\} \in E(G')$$

> [!Property] ⚙️ Isomorphism Invariants (use to **disprove** quickly)
> - $|V|$, $|E|$, degree sequence, number of connected components
> - Existence of $k$-cycles, Euler circuit, Hamilton circuit, connectivity

> [!Warning] ⚠️ To **prove** isomorphism: must explicitly construct $f$ and verify all edges preserved. To **disprove**: find one invariant that differs.

---

## 9. BFS & DFS

> [!Definition] 📖 BFS — Queue, $O(V+E)$
> ```
> BFS(G, start):
>   dist[u] ← ∞; colour[u] ← white  ∀u
>   dist[start] ← 0; colour[start] ← gray; Q ← [start]
>   while Q ≠ ∅:
>     u ← Q.pop()
>     for v in neighbors(u):
>       if colour[v] = white:
>         dist[v] ← dist[u] + 1; colour[v] ← gray; Q.push(v)
>     colour[u] ← black
> ```
> **Finds:** shortest path (fewest edges) from source. White = unvisited, gray = queued, black = done.
>
> **Applications:** connectedness check, find components, cycle detection, multi-source shortest path (init queue with all sources at dist 0)

> [!Definition] 📖 DFS — Stack/Recursion, $O(V+E)$
> ```
> DFS(v):
>   Mark v as visited
>   for each unvisited u adjacent to v: DFS(u)
> ```
> **Explores** deep before backtracking. Path to vertex may not be shortest.

> [!Property] ⚙️ BFS vs DFS
> | | BFS | DFS |
> |---|---|---|
> | Data structure | Queue | Stack / recursion |
> | Path found | Shortest (fewest edges) | Not necessarily shortest |
> | Style | Level-order | Deep-first |

---

## 10. Minimum Spanning Trees (MST)

> [!Definition] 📖 MST
> Spanning tree with **minimum total edge weight**. Has exactly $|V|-1$ edges. Exists iff graph is connected.

> [!Property] ⚙️ Cut Property (MST Lemma)
> For any cut $(S, V-S)$: the **minimum-weight crossing edge** belongs to some MST.

> [!Definition] 📖 Prim's Algorithm — $O((V+E) \log V)$ with heap
> ```
> Start from arbitrary vertex r
> Repeatedly add: min-weight edge {u,v} where u ∈ T, v ∉ T
> ```
> Vertex-based. Best for **dense** graphs. Uses priority queue.

> [!Definition] 📖 Kruskal's Algorithm — $O(E \log E)$
> ```
> Sort all edges by weight
> For each edge e (in order): add to T if it doesn't form a cycle
> Stop when |T| = |V| - 1
> ```
> Edge-based. Best for **sparse** graphs. Uses Union-Find for cycle detection.

> [!Property] ⚙️ Prim's vs Kruskal's
> | | Kruskal's | Prim's |
> |---|---|---|
> | Approach | Edge-based | Vertex-based |
> | Best for | Sparse | Dense |
> | Data structure | Union-Find | Heap |
> | Time | $O(E \log E)$ | $O((V+E) \log V)$ |

---

## 11. Dijkstra's Shortest Paths

> [!Definition] 📖 Dijkstra's Algorithm — $O(V^2)$ naive, $O((V+E)\log V)$ with heap
> ```
> DIJKSTRA(G, s):
>   c[s] ← 0; c[u] ← ∞ ∀u ≠ s; T ← {s}
>   while vertices remain outside T:
>     F ← fringe (neighbors of T not in T)
>     for u in Adj(v) \ T:
>       if c[v] + w(v,u) < c[u]:
>         c[u] ← c[v] + w(v,u); previous[u] ← v
>     x ← argmin_{p ∈ F} c[p]; add x to T
> ```
> **Update rule:** if $c[v] + w(v,u) < c[u]$, update $c[u]$ and $\text{previous}[u]$

> [!Warning] ⚠️ Dijkstra requires **non-negative** edge weights only.

> [!Property] ⚙️ Key Concepts
> - $T$: shortest-path tree; $F = \bar{T}$ neighbors = fringe
> - At each step: add fringe vertex with **minimum** $c$ value
> - After adding $v$ to $T$: only update $c$ for neighbors of $v$ not yet in $T$

---

## 12. Planar Graphs

> [!Definition] 📖 Planar Graph
> Can be drawn in the plane with **no edge crossings**. A planar embedding partitions the plane into **faces** (one is unbounded).
>
> **Monotonicity:** subgraph of planar → planar; supergraph of non-planar → non-planar.

> [!Theorem] 📌 Euler's Formula (connected planar graph)
> $$\boxed{v - e + f = 2}$$
> General (with $c$ components): $v - e + f = 1 + c$

> [!Theorem] 📌 Face Handshake Lemma
> $$\sum_{\text{faces}} d(F) = 2e$$

> [!Theorem] 📌 Edge Bounds (necessary for planarity, $v \geq 3$)
> - **General:** $e \leq 3v - 6$
> - **Triangle-free (no $C_3$):** $e \leq 2v - 4$
>
> Violation ⟹ **non-planar** (sufficient but not necessary to conclude planarity)

> [!Property] ⚙️ Planarity of Special Graphs
> **Planar:** paths, trees, $C_n$, $W_n$, $K_1$–$K_4$, $Q_3$, $K_{2,n}$ for small $n$
> **Non-planar:** $K_5$, $K_{3,3}$, Petersen graph, $Q_n$ for $n \geq 4$

> [!Property] ⚙️ Non-planarity Proofs
> - $K_5$: $v=5, e=10$; $3v-6 = 9 < 10$ ✗ → **non-planar**
> - $K_{3,3}$: $v=6, e=9$; bipartite (no triangles) → $2v-4 = 8 < 9$ ✗ → **non-planar**
> - $Q_6$: $v=64, e=192$; $3v-6 = 186 < 192$ ✗ → **non-planar**
> - $Q_4, Q_5$: bound not violated but non-planar via Kuratowski (contains $K_{3,3}$ subdivision)

> [!Theorem] 📌 Kuratowski's Theorem
> $G$ is non-planar $\iff$ $G$ contains a **subdivision of $K_5$** or **subdivision of $K_{3,3}$** as a subgraph.
>
> A **subdivision** = replace edges with paths (insert degree-2 vertices).

> [!Theorem] 📌 Minimum Degree in Planar Graphs
> Every connected planar graph has at least one vertex of degree $\leq 5$.

---

## 🗂️ Master Quick-Reference

**Handshake Theorem:** $\sum \deg = 2|E|$; always even; even number of odd-degree vertices.

**Euler circuit:** connected + all even degree. **Euler path:** connected + exactly 2 odd-degree vertices.

**Hamilton:** no simple iff condition (NP-hard). Sufficient: Dirac ($\deg \geq n/2$) or Ore ($\deg(u)+\deg(v) \geq n$).

**MST:** Prim (dense, heap), Kruskal (sparse, Union-Find). Both $O(E \log E)$-class.

**Dijkstra:** non-negative weights only; update rule $c[v] + w(v,u) < c[u]$.

**Planar:** $v-e+f=2$; edge bound $e \leq 3v-6$; triangle-free $e \leq 2v-4$; Kuratowski.

**Matrices:** Adjacency ($A^r$ = walks of length $r$); Laplacian $L = D-A$ (row sums = 0); Incidence $M$ ($n \times m$, col sums = 2).

**Isomorphism:** bijection preserving adjacency; use invariants (deg sequence, $|V|$, $|E|$, cycles) to disprove.
