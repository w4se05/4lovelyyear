---
tags: [discrete-math, graphs, connectivity, euler, hamilton, planar-graphs]
topic: "Chapter 10: Graphs — Part 2 (Connectivity, Euler/Hamilton Paths, Planar Graphs)"
course: "DISCRETE MATHEMATICS"
---

# Chapter 10: Graphs — Part 2

> [!Note] 💡 Notation Conventions
> - $G = (V, E)$: graph with vertex set $V$, edge set $E$.
> - $n = |V|$ (vertices), $e = |E|$ (edges), $f$ (faces in a planar embedding).
> - **Path of length $k$**: sequence of $k$ edges (vertices need not be distinct unless stated).
> - **Simple path/circuit**: no repeated **edges**.
> - **deg$(v)$**: degree of $v$; **deg$^+(v)$**, **deg$^-(v)$**: out/in-degree.
> - $c$: number of connected components.
> - Default: "graph" = simple undirected graph unless stated otherwise.

---

## 1. Paths and Circuits

> [!Definition] 📖 Path, Circuit, Simple
> Let $G = (V, E)$ be a (di)graph.
>
> **1. Path of length $n$** from $u$ to $v$: a sequence of edges
> $$(x_0, x_1),\ (x_1, x_2),\ \ldots,\ (x_{n-1}, x_n)$$
> where $x_0 = u$, $x_n = v$. Vertices $x_i$ need not be distinct. When there are no multiple edges, a path is written as its vertex sequence $x_0, x_1, \ldots, x_n$.
>
> **2. Circuit (cycle)**: a path of length $> 0$ that **starts and ends at the same vertex** ($x_0 = x_n$).
>
> **3. Simple path / simple circuit**: does **not** traverse the same **edge** more than once.

> [!Warning] ⚠️ Simple Path vs. Simple Circuit
> "Simple" here means no repeated **edges** — vertices may still repeat. This is the lecture's definition. (Some textbooks use "simple" to mean no repeated vertices — be careful with terminology.)

---

## 2. Connectivity

### 2.1 Undirected Graphs

> [!Definition] 📖 Connected Graph & Components
> Let $G = (V, E)$ be a (multi)graph.
>
> **1. Connected**: there exists a path between **every** pair of distinct vertices.
>
> **2. Connected component**: a **maximal connected subgraph** — not a proper subgraph of any other connected subgraph of $G$.
>
> If $G$ is disconnected, it decomposes into $c \geq 2$ disjoint connected components whose union is $G$.

> [!Definition] 📖 Cut Vertex & Cut Edge (Bridge)
> Let $G = (V, E)$ be an undirected graph.
>
> **1. Cut vertex (articulation point)**: a vertex $v$ such that removing $v$ and all edges incident to it increases the number of connected components.
>
> **2. Cut edge (bridge)**: an edge $e$ such that removing $e$ increases the number of connected components.

---

### 2.2 Directed Graphs

> [!Definition] 📖 Strong and Weak Connectivity
> Let $G = (V, E)$ be a digraph.
>
> **1. Strongly connected**: for every ordered pair $(u, v)$, there is a **directed path** from $u$ to $v$ **and** from $v$ to $u$.
>
> **2. Weakly connected**: the **underlying undirected graph** (obtained by ignoring edge directions) is connected.
>
> **3. Strongly connected component (SCC)**: a maximal strongly connected subgraph of $G$.
>
> Note: strongly connected $\Rightarrow$ weakly connected, but not conversely.

> [!Example] 📘 Strong vs. Weak Connectivity
> **Using:** Directed path existence, underlying undirected graph.
>
> Digraph with vertices $A, B, C, D, E, F$ and directed edges:
> $A \to B$, $B \to C$, $B \to D$, $C \to D$, $D \to E$, $E \to A$, $F \to A$, $F \to B$, $F \to C$, $F \to E$.
>
> **Is it strongly connected?**
> Try to reach $F$ from any vertex. There is no edge pointing **to** $F$, so $\deg^-(F) = 0$ — no directed path from any other vertex to $F$.
> $\Rightarrow$ **Not strongly connected.**
>
> **Is it weakly connected?**
> Ignoring directions: all vertices are reachable from each other.
> $\Rightarrow$ **Weakly connected.**
>
> **SCCs:** $\{A, B, C, D, E\}$ (all mutually reachable via directed paths) and $\{F\}$ (isolated in directed sense).
> $\Rightarrow$ **2 strongly connected components.**

---

## 3. Eulerian Paths and Circuits

> [!Definition] 📖 Eulerian Path and Circuit
> Let $G$ be a connected multigraph.
>
> **Eulerian circuit**: a **simple circuit** that contains **every edge** of $G$ exactly once.
>
> **Eulerian path**: a **simple path** that contains **every edge** of $G$ exactly once.
>
> (Both visit all edges; the circuit returns to its starting vertex, the path does not.)

> [!Theorem] 📌 Existence of Eulerian Circuits and Paths
> Let $G$ be a **connected multigraph**. Then:
>
> **1.** $G$ has an **Eulerian circuit** $\iff$ every vertex has **even degree**.
>
> **2.** $G$ has an **Eulerian path** (but no Eulerian circuit) $\iff$ $G$ has **exactly two vertices of odd degree**.
> (The path starts at one odd-degree vertex and ends at the other.)

> [!Warning] ⚠️ Directed Graph Conditions
> For a **connected digraph**, Eulerian circuit exists iff $\deg^+(v) = \deg^-(v)$ for every vertex $v$. Eulerian path exists iff exactly one vertex has $\deg^+(v) - \deg^-(v) = 1$ (start) and exactly one has $\deg^-(v) - \deg^+(v) = 1$ (end), with all others balanced.

> [!Property] ⚙️ Euler Paths/Circuits for Special Graphs
> | Graph | Eulerian Circuit? | Eulerian Path? |
> |---|---|---|
> | $K_n$ | Yes iff $n$ is odd ($n \geq 3$) | Yes iff $n$ is even ($n \geq 2$) |
> | $C_n$ | Yes (all degrees = 2) | No |
> | $W_n$ | Only if all degrees even: hub has degree $n$, rim vertices degree 3 — never all even for $n \geq 3$ | Rarely; check case-by-case |
> | $Q_n$ | Yes iff $n$ is even (all degrees $= n$) | Yes iff $n$ is odd |
> | $K_{m,n}$ | Yes iff both $m, n$ are even | Yes iff exactly one of $m, n$ is odd (and both $\geq 1$) |

> [!Example] 📘 The Seven Bridges of Königsberg
> **Using:** Eulerian circuit existence theorem, degree counting.
>
> Model the city as a multigraph: 4 landmasses = vertices; 7 bridges = edges.
> Degrees of the 4 vertices: **3, 3, 5, 3** (all odd).
>
> For an Eulerian circuit: all vertices must have even degree. Here **none** do.
> For an Eulerian path: exactly 2 odd-degree vertices required. Here **all 4** are odd.
>
> $\Rightarrow$ **No Eulerian path or circuit exists.** It is impossible to cross all 7 bridges exactly once.

> [!Example] 📘 Determining Euler Paths/Circuits
> **Using:** Degree parity check.
>
> **Graph 1** (from lecture, $K_{2,3}$-like, 5 vertices $a,b,c,d,e$):
> Degrees: $a:2,\ b:2,\ c:3,\ d:2,\ e:3$ — two odd-degree vertices ($c, e$).
> $\Rightarrow$ **Eulerian path** exists (from $c$ to $e$), **no Eulerian circuit**.
>
> **Graph 2** (square with diagonals, 5 vertices):
> Degrees: $a:3,\ b:2,\ c:3,\ d:3,\ e:3$ — four odd-degree vertices.
> $\Rightarrow$ **Neither** Eulerian path nor circuit.
>
> **Graph 3** ($a,b,c,d,e$ with edges $ab, ac, bd, be, cd, de$):
> Degrees: $a:2,\ b:3,\ c:2,\ d:2,\ e:2$... check: odd-degree count depends on exact edges.
>
> > [!Warning] ⚠️ Possible Gap
> > The exact edge lists for all three graphs in the lecture's "Examples I" slide were partially obscured in the PDF. Apply the degree-parity rule to the actual figures in your notes.

---

## 4. Hamiltonian Paths and Circuits

> [!Definition] 📖 Hamiltonian Path and Circuit
> **Hamiltonian path**: a simple path that passes through **every vertex exactly once**.
>
> **Hamiltonian circuit**: a simple circuit that passes through **every vertex exactly once** (returns to start).
>
> Key difference from Euler: Euler covers all **edges**; Hamilton covers all **vertices**.

> [!Theorem] 📌 Sufficient Conditions (Dirac & Ore)
> Let $G$ be a simple graph with $n \geq 3$ vertices.
>
> **Dirac's Theorem:** If $\deg(v) \geq \dfrac{n}{2}$ for every vertex $v$, then $G$ has a Hamiltonian circuit.
>
> **Ore's Theorem:** If $\deg(u) + \deg(v) \geq n$ for every pair of **non-adjacent** vertices $u, v$, then $G$ has a Hamiltonian circuit.
>
> **Important:** Both are **sufficient, not necessary** conditions. A graph may have a Hamiltonian circuit even if neither condition holds.

> [!Warning] ⚠️ No Simple Characterization
> Unlike Eulerian circuits, **no known simple necessary-and-sufficient condition** exists for Hamiltonian circuits. This is related to the P vs. NP problem.

> [!Property] ⚙️ Hamilton Paths/Circuits for Special Graphs
> | Graph | Hamilton Circuit? | Hamilton Path? |
> |---|---|---|
> | $K_n$, $n \geq 3$ | Yes | Yes |
> | $C_n$ | Yes (the cycle itself) | Yes |
> | $W_n$ | Yes (use rim cycle, include hub) | Yes |
> | $Q_n$ | Yes for $n \geq 2$ | Yes |
> | $K_{m,n}$ | Yes iff $m = n$ | Yes iff $|m - n| \leq 1$ |

> [!Example] 📘 Finding Hamiltonian Paths/Circuits
> **Using:** Definition, vertex-visit tracking.
>
> Three ladder graphs from the lecture:
>
> **Graph 1** (2×2 grid, 4 vertices):
> Vertices: top-left $a$, top-right $b$, bottom-left $c$, bottom-right $d$.
> Edges: $ab, ac, bd, cd$.
> Hamilton circuit: $a \to b \to d \to c \to a$. ✓
>
> **Graph 2** (2×3 grid, 6 vertices):
> Hamilton path exists: traverse top row left-to-right, then bottom row right-to-left.
> Hamilton circuit: check if top-right and bottom-left can close the loop — yes for this grid.
>
> **Graph 3** (2×4 grid, 8 vertices):
> Hamilton circuit exists: snake pattern covers all 8 vertices and returns to start. ✓

> [!Example] 📘 Petersen Graph Has No Hamiltonian Circuit
> **Using:** Structural argument, degree constraints.
>
> The Petersen graph has 10 vertices, each of degree 3.
>
> **Proof sketch (by contradiction):**
> Assume a Hamiltonian circuit $C$ exists. $C$ uses 10 edges (one per vertex). The remaining $15 - 10 = 5$ edges form a set $S$ of "chords."
>
> The Petersen graph has no triangle ($C_3$) and no $C_4$. Since $C$ is a 10-cycle, every chord in $S$ must connect vertices at distance $\geq 3$ along $C$. Each vertex has degree 3: 2 edges in $C$, 1 chord. So $S$ is a perfect matching (5 edges, each vertex in exactly one chord).
>
> The 5 chords of a 10-cycle with no two adjacent and no $C_4$ — exhaustive case analysis shows this forces a $C_4$ or a $C_3$ in the Petersen graph, contradiction.
> $\Rightarrow$ **No Hamiltonian circuit exists.** $\blacksquare$

> [!Note] 💡 Applications
> - **Traveling Salesman Problem (TSP):** find the minimum-weight Hamiltonian circuit in a weighted graph.
> - **Gray codes:** list all $n$-bit binary strings so consecutive strings differ in exactly one bit — equivalent to a Hamiltonian path on $Q_n$.

---

## 5. Planar Graphs

### 5.1 Definition

> [!Definition] 📖 Planar Graph
> A graph $G$ is **planar** if it can be drawn in the plane with **no edges crossing** (edges may only intersect at shared endpoints). Such a drawing is called a **planar representation** or **planar embedding**.

> [!Property] ⚙️ Monotonicity of Planarity
> - If $G$ is **planar**, then any subgraph of $G$ (obtained by removing vertices or edges) is also planar.
> - If $G$ is **non-planar**, then any graph containing $G$ as a subgraph is also non-planar.
> - To show planarity: exhibit a planar drawing.
> - To show non-planarity: use Euler's formula bounds or Kuratowski's Theorem.

> [!Property] ⚙️ Known Planar / Non-Planar Graphs
> **Planar:** $P_n$ (paths), all trees, $C_n$, $W_n$, $K_1, K_2, K_3, K_4$, $Q_3$, $K_{2,5}$, $K_{2,4}$, Dodecahedron, Antiprism.
>
> **Non-planar:** $K_5$, $K_{3,3}$, Petersen graph (and any graph containing these as a subgraph/minor).

---

### 5.2 Faces and Euler's Formula

> [!Definition] 📖 Faces of a Planar Graph
> A planar embedding partitions the plane into **faces** (regions). There is always exactly one **unbounded (exterior/infinite) face**.
>
> The **degree of a face** $F$, written $d(F)$, is the number of edges on the boundary of $F$. An edge shared by two faces contributes 1 to each; a **bridge** (cut edge) contributes 2 to the same face.

> [!Theorem] 📌 Handshaking Lemma for Faces
> For a planar graph with $m$ edges:
> $$\sum_{\text{faces } F} d(F) = 2m$$
>
> **Proof:** Each edge borders exactly two faces (or borders one face twice if it's a bridge), so each edge is counted exactly twice in the sum. $\blacksquare$

> [!Theorem] 📌 Euler's Formula
> Let $G$ be a **connected planar simple graph** with $v$ vertices, $e$ edges, and $f$ faces in any planar embedding. Then:
> $$\boxed{v - e + f = 2}$$
> equivalently $f = e - v + 2$.

> [!Proof] 🔷 Euler's Formula (by induction on $e$)
> **Base case:** $e = 0$. $G$ is a single vertex ($v = 1$), one face (the whole plane, $f = 1$). $1 - 0 + 1 = 2$. ✓
>
> **Inductive step:** Assume the formula holds for all connected planar graphs with fewer than $e$ edges.
>
> *Case 1: $G$ is a tree.* A tree with $v$ vertices has $e = v-1$ edges and $f = 1$ face (no bounded regions). Then $v - (v-1) + 1 = 2$. ✓
>
> *Case 2: $G$ has a cycle.* Pick an edge $e^*$ on a cycle. Removing $e^*$ keeps $G$ connected (since $e^*$ is not a bridge) and reduces edges by 1 and faces by 1 (the two faces separated by $e^*$ merge). By induction on $G - e^*$: $v - (e-1) + (f-1) = 2$, which gives $v - e + f = 2$. ✓ $\blacksquare$

> [!Theorem] 📌 Euler's Formula — Disconnected Version
> For a planar graph with $c$ connected components:
> $$v - e + f = 1 + c$$

> [!Example] 📘 Applying Euler's Formula
> **Using:** $f = e - v + 2$.
>
> Graph $G$: vertices $a,b,c,d,e,f$ (6 vertices); edges $ab, ad, bc, bd, be, cd, ef$ (7 edges).
>
> $$f = e - v + 2 = 7 - 6 + 2 = 3 \text{ faces}$$
>
> Verify: two bounded faces (cycles $abcda$ and $cefbc$) and one unbounded face. ✓

---

### 5.3 Consequences of Euler's Formula

> [!Theorem] 📌 Edge Bound for Simple Planar Graphs
> If $G$ is a **connected simple planar graph** with $v \geq 3$ vertices and $e$ edges, then:
> $$e \leq 3v - 6$$

> [!Proof] 🔷 Edge Bound
> Each face has degree $\geq 3$ (no multi-edges or loops in a simple graph, so no face of degree 1 or 2). By the Handshaking Lemma for Faces:
> $$2e = \sum_F d(F) \geq 3f \implies f \leq \frac{2e}{3}$$
> Substitute into Euler's formula $f = e - v + 2$:
> $$e - v + 2 \leq \frac{2e}{3} \implies \frac{e}{3} \leq v - 2 \implies e \leq 3v - 6 \quad \blacksquare$$

> [!Theorem] 📌 Edge Bound for Triangle-Free Planar Graphs
> If $G$ is a **connected simple planar graph** with $v \geq 3$, **no cycles of length 3**, then:
> $$e \leq 2v - 4$$

> [!Proof] 🔷 Triangle-Free Edge Bound
> No triangles means every face has degree $\geq 4$. So $2e \geq 4f$, i.e., $f \leq e/2$. Substituting into Euler's formula:
> $$e - v + 2 \leq \frac{e}{2} \implies \frac{e}{2} \leq v - 2 \implies e \leq 2v - 4 \quad \blacksquare$$

> [!Corollary] ⚙️ $K_5$ and $K_{3,3}$ Are Non-Planar
> **$K_5$:** $v = 5$, $e = 10$. Check: $3v - 6 = 9 < 10 = e$. Violates edge bound $\Rightarrow$ **non-planar**.
>
> **$K_{3,3}$:** $v = 6$, $e = 9$. $K_{3,3}$ is bipartite $\Rightarrow$ no triangles. Check: $2v - 4 = 8 < 9 = e$. Violates triangle-free edge bound $\Rightarrow$ **non-planar**.

> [!Theorem] 📌 Minimum Degree in Planar Graphs
> Every connected planar graph has at least one vertex of degree $\leq 5$.
>
> **Proof:** Suppose all vertices have degree $\geq 6$. Then $2e = \sum \deg(v) \geq 6v$, so $e \geq 3v$. But the edge bound gives $e \leq 3v - 6 < 3v$. Contradiction. $\blacksquare$

---

### 5.4 Kuratowski's Theorem

> [!Definition] 📖 Subdivision
> A **subdivision** of a graph $G$ is obtained by inserting new vertices of degree 2 into the edges of $G$ (replacing an edge $uv$ with a path $u - w_1 - w_2 - \cdots - v$).

> [!Theorem] 📌 Kuratowski's Theorem
> A graph is **non-planar** if and only if it contains a **subdivision of $K_5$** or a **subdivision of $K_{3,3}$** as a subgraph.
>
> (Self-study — this gives a complete characterization of non-planar graphs.)

---

## 📘 Examples & Applications

> [!Example] 📘 Euler Path/Circuit — Special Graphs
> **Using:** Degree parity, Euler circuit/path theorem.
>
> For each graph, check all vertex degrees:
>
> **$K_n$:**
> All degrees $= n-1$.
> - Eulerian circuit: need all even $\Rightarrow$ $n-1$ even $\Rightarrow$ $n$ odd.
> - Eulerian path (no circuit): need exactly 2 odd $\Rightarrow$ impossible if all degrees equal, unless $n=2$ ($K_2$ is a single edge, Eulerian path).
>
> **$C_n$:** All degrees $= 2$ (even) $\Rightarrow$ **Eulerian circuit always** exists.
>
> **$W_n$:** Hub degree $= n$; rim vertices degree $= 3$ (odd). Odd-degree count $= n$.
> - Eulerian circuit: need $n = 0$ (impossible). **Never** has Eulerian circuit.
> - Eulerian path: need exactly 2 odd-degree vertices $\Rightarrow$ $n = 2$, but $W_2$ not defined ($n \geq 3$). **Never** has Eulerian path for standard $W_n$.
>
> **$Q_n$:** All degrees $= n$.
> - Eulerian circuit: $n$ even. Eulerian path: $n$ odd ($n \geq 1$).
>
> **$K_{m,n}$:** All vertices in part 1 have degree $n$; all in part 2 have degree $m$.
> - Eulerian circuit: both $m$ and $n$ even.
> - Eulerian path: exactly one of $m, n$ is odd (so exactly 2 odd-degree vertices come from the set whose degree is odd).

> [!Example] 📘 Hamilton Paths/Circuits — Special Graphs
> **Using:** Hamilton definitions, degree conditions.
>
> **$K_n$, $n \geq 3$:** Every vertex adjacent to all others — Hamilton circuit trivially exists. ✓
>
> **$C_n$:** The cycle itself is a Hamilton circuit. ✓
>
> **$W_n$:** Hamilton circuit: go around rim $v_1 \to v_2 \to \cdots \to v_n \to v_1$ — this is $C_n$ on the rim, a Hamilton circuit if hub is visited. Actually route: $h \to v_1 \to v_2 \to \cdots \to v_n \to h$. ✓
>
> **$Q_n$, $n \geq 2$:** Hamilton circuit exists (Gray code gives a Hamiltonian path on $Q_n$, and for $n \geq 2$ it closes to a circuit). ✓
>
> **$K_{m,n}$:** Any Hamilton circuit alternates between the two parts, requiring $m = n$. Hamilton path requires $|m - n| \leq 1$.

> [!Example] 📘 Proving $K_5$ is Non-Planar
> **Using:** Edge bound $e \leq 3v - 6$.
>
> $K_5$: $v = 5$, $e = \binom{5}{2} = 10$.
>
> $$3v - 6 = 3(5) - 6 = 9$$
>
> Since $e = 10 > 9 = 3v - 6$, the edge bound is violated.
> $\Rightarrow$ $K_5$ is **non-planar**. $\blacksquare$

> [!Example] 📘 Proving $K_{3,3}$ is Non-Planar
> **Using:** Triangle-free edge bound $e \leq 2v - 4$.
>
> $K_{3,3}$: $v = 6$, $e = 9$. $K_{3,3}$ is bipartite $\Rightarrow$ contains no odd cycles $\Rightarrow$ no triangles.
>
> $$2v - 4 = 2(6) - 4 = 8$$
>
> Since $e = 9 > 8 = 2v - 4$, the triangle-free edge bound is violated.
> $\Rightarrow$ $K_{3,3}$ is **non-planar**. $\blacksquare$

> [!Example] 📘 Proving Petersen Graph is Non-Planar
> **Using:** Edge bound, or $K_{3,3}$ subdivision.
>
> Petersen graph: $v = 10$, $e = 15$.
>
> **Method 1 (edge bound):** $3v - 6 = 24 \geq 15$ — bound not violated, so this alone doesn't prove non-planarity.
>
> **Method 2 (contains $K_{3,3}$ subdivision):** One can exhibit a subgraph of the Petersen graph that is a subdivision of $K_{3,3}$. Label the outer pentagon $a,b,c,d,e$ and inner pentagram $f,g,h,i,j$. Take:
> - Part 1: $\{a, c, h\}$
> - Part 2: $\{b, g, j\}$
>
> All 9 required connections can be traced through the Petersen graph using paths (introducing subdivision vertices). $\Rightarrow$ **Non-planar** by Kuratowski's Theorem. $\blacksquare$

> [!Example] 📘 Face Count for a Tree
> **Using:** Euler's formula.
>
> A tree on $n$ vertices has $e = n - 1$ edges and is connected ($c = 1$).
>
> $$f = e - v + 2 = (n-1) - n + 2 = 1$$
>
> A tree always has exactly **1 face** (the unbounded exterior). ✓ (Trees have no cycles, so no bounded faces.)

> [!Example] 📘 Faces in a 3-Regular Connected Planar Graph with 20 Vertices
> **Using:** Handshaking theorem, Euler's formula.
>
> Given: $v = 20$, every vertex has degree 3, $G$ connected and planar.
>
> **Step 1:** Find $e$.
> $$\sum \deg(v) = 2e \implies 20 \times 3 = 2e \implies e = 30$$
>
> **Step 2:** Find $f$.
> $$f = e - v + 2 = 30 - 20 + 2 = 12$$
>
> The planar representation splits the plane into **12 regions**.

> [!Example] 📘 Can Six Houses Connect to Two Utilities Without Crossing?
> **Using:** $K_{6,2}$ edge bound check.
>
> This is $K_{6,2}$: $v = 8$, $e = 12$.
>
> Check edge bound: $3v - 6 = 18 \geq 12$. Bound not violated.
>
> Check triangle-free bound: $K_{6,2}$ is bipartite (no triangles). $2v - 4 = 12 \geq 12$. Bound satisfied (with equality).
>
> $K_{6,2}$ **is planar** (it is a subgraph of $K_{2,6}$ which has a planar drawing). So yes — six houses can connect to two utilities without crossings.

> [!Example] 📘 Are $Q_4$, $Q_5$, $Q_6$ Planar?
> **Using:** Edge bound for planar graphs.
>
> $Q_n$: $v = 2^n$, $e = n \cdot 2^{n-1}$.
>
> Check $e \leq 3v - 6$:
>
> **$Q_4$:** $v = 16$, $e = 32$. $3(16) - 6 = 42 \geq 32$. Bound not violated — **possibly planar.** (In fact $Q_4$ is **non-planar** — requires Kuratowski argument.)
>
> **$Q_5$:** $v = 32$, $e = 80$. $3(32) - 6 = 90 \geq 80$. Bound not violated — but $Q_5$ contains $Q_4$ as a subgraph, and since $Q_4$ is non-planar, $Q_5$ is also **non-planar**.
>
> **$Q_6$:** $v = 64$, $e = 192$. $3(64) - 6 = 186 < 192$. Edge bound **violated** $\Rightarrow$ $Q_6$ is **non-planar**.
>
> > [!Warning] ⚠️ Note
> > The edge bound is a necessary condition for planarity, not sufficient. For $Q_4$ and $Q_5$, the bound alone is inconclusive — non-planarity follows from the $K_{3,3}$ or $K_5$ subdivision argument.

---

## 🗂️ Summary

**Connectivity**
- **Connected graph**: path exists between every pair of vertices.
- **Cut vertex / bridge**: removal increases connected component count.
- **Strongly connected** (digraph): directed path in both directions for every pair.
- **Weakly connected** (digraph): underlying undirected graph is connected.

**Eulerian Paths/Circuits** (covers all edges)
- Eulerian **circuit**: all vertices have **even degree**.
- Eulerian **path**: exactly **2 vertices** have odd degree (path runs between them).
- For digraphs: circuit requires $\deg^+(v) = \deg^-(v)$ for all $v$.

**Hamiltonian Paths/Circuits** (covers all vertices)
- **No simple iff condition** — NP-hard problem.
- Sufficient: Dirac ($\deg(v) \geq n/2$) or Ore ($\deg(u)+\deg(v) \geq n$ for non-adjacent $u,v$).
- $K_{m,n}$ has Hamilton circuit iff $m=n$; Hamilton path iff $|m-n| \leq 1$.
- Petersen graph: **no** Hamilton circuit.

**Planar Graphs**
- Euler's formula: $v - e + f = 2$ (connected); $v - e + f = 1 + c$ (general).
- Handshaking for faces: $\sum d(F) = 2e$.
- Edge bounds (necessary for planarity):
  - General: $e \leq 3v - 6$ (for $v \geq 3$).
  - Triangle-free: $e \leq 2v - 4$.
- $K_5$ non-planar ($e=10 > 9=3v-6$); $K_{3,3}$ non-planar ($e=9 > 8=2v-4$).
- Every planar graph has a vertex of degree $\leq 5$.
- **Kuratowski:** $G$ non-planar $\iff$ $G$ contains a subdivision of $K_5$ or $K_{3,3}$.
