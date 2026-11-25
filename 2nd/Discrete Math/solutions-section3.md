# Sect.3 Graphs — Full Solutions

---

**1.** Investigate the existence of an Eulerian/Hamiltonian cycle on $C_n$, $W_n$, $K_n$, $K_{m,n}$, $Q_n$.

**Solution.**

**Recall (Euler's Theorem).** Let $G$ be a connected graph.
- $G$ has an **Eulerian circuit** iff every vertex has even degree.
- $G$ has an **Eulerian path** (non-circuit) iff exactly two vertices have odd degree (the path starts at one odd-degree vertex and ends at the other).
- If more than two vertices have odd degree, $G$ has **neither**.

**Recall (Hamiltonian sufficient conditions — Dirac, Ore).**
- **Dirac's Theorem:** If $G$ is a simple graph on $n\ge3$ vertices and $\deg(v)\ge n/2$ for every vertex $v$, then $G$ has a Hamiltonian circuit.
- **Ore's Theorem:** If $G$ is a simple graph on $n\ge3$ vertices and for every pair of non-adjacent vertices $u,v$, $\deg(u)+\deg(v)\ge n$, then $G$ has a Hamiltonian circuit.
- These are sufficient but not necessary. For special graphs we can often construct cycles directly or derive necessary conditions.

We now examine each graph family.

---

**$C_n$ (Cycle on $n$ vertices, $n\ge3$).**

Step 1. $v=n$, $e=n$. Every vertex has degree $2$ (even).

Step 2. **Eulerian:** All degrees even $\Rightarrow$ Eulerian circuit **always exists** (the cycle itself). Eulerian path also always exists (every circuit is a path).

Step 3. **Hamiltonian:** $C_n$ **is** a Hamiltonian cycle, so a Hamiltonian circuit (and path) **always exists**.

$$\boxed{\begin{aligned}C_n &: \text{Euler circuit: } \textbf{always} &&\text{Euler path (non-circuit): } \textbf{never}\\
&\text{Hamilton circuit: } \textbf{always} &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**$W_n$ (Wheel on $n+1$ vertices, $n\ge3$).**

Step 1. $v=n+1$, $e=2n$. Structure: one hub vertex $h$ connected to all $n$ rim vertices $r_1,\dots,r_n$, and the rim forms an $n$-cycle $r_1\mdash r_2\mdash\cdots\mdash r_n\mdash r_1$.

Step 2. Degrees: $\deg(h)=n$, $\deg(r_i)=3$ for all $i$ (connected to two rim neighbors and the hub).

Step 3. **Eulerian:** Every rim vertex has odd degree $3$. So there are $n$ odd-degree rim vertices. Additionally, if $n$ is odd, $h$ also has odd degree, giving $n+1$ odd vertices. In all cases for $n\ge3$, the number of odd-degree vertices is at least $n\ge3>2$. Hence **no Eulerian circuit or path exists** for $W_n$ when $n\ge3$.
(For $n=2$, $W_2\cong K_3$, which has $3$ vertices all degree $2$; $K_3$ has an Eulerian circuit because all degrees are even. But $W_n$ is standard for $n\ge3$.)

Step 4. **Hamiltonian:** The wheel always has a Hamiltonian circuit: start at $h$, go around all rim vertices $r_1\to r_2\to\cdots\to r_n$, and return to $h$. Thus a Hamiltonian circuit and path **always exist** for $W_n$ ($n\ge3$).

$$\boxed{\begin{aligned}W_n &: \text{Euler circuit: } \textbf{never }(n\ge3) &&\text{Euler path (non-circuit): } \textbf{never }(n\ge3)\\
&\text{Hamilton circuit: } \textbf{always} &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**$K_n$ (Complete graph on $n$ vertices).**

Step 1. $v=n$, $e=C(n,2)$. Every vertex has degree $n-1$.

Step 2. **Eulerian:**
- Eulerian circuit: all degrees $n-1$ must be even $\Rightarrow$ $n$ is **odd** ($n=1,3,5,\dots$). For $n=1$, the trivial graph has an Eulerian circuit (a walk of length $0$).
- Eulerian path (non-circuit): exactly $2$ odd-degree vertices needed. Since all vertices have the same degree, this requires $n=2$ ($K_2$ has two vertices both degree $1$, exactly $2$ odd $\Rightarrow$ path exists, not circuit).
- For $n\ge4$ and $n$ even: $n$ odd-degree vertices, $n\ge4$, so **neither** exists.

Summary:
- $K_n$ has Euler circuit iff $n$ is odd.
- $K_n$ has Euler path (non-circuit) iff $n=2$.
- Otherwise ($n\ge4$ even), neither exists.

Step 3. **Hamiltonian:** For $n\ge3$, $K_n$ obviously contains a Hamiltonian circuit (any permutation of vertices forms one). For $n=1,2$: $K_1$ has a trivial Hamiltonian circuit; $K_2$ has a Hamiltonian path but only a circuit if we allow returning along the same edge (not in a simple graph, so $K_2$ has no Hamiltonian circuit in the strict cycle sense, but $K_2$ does have a Hamiltonian path). For $n\ge3$, both circuit and path always exist.

$$\boxed{\begin{aligned}K_n &: \text{Euler circuit: } n \text{ is odd} &&\text{Euler path (non-circuit): } n=2\\
&\text{Hamilton circuit: } \textbf{always }(n\ge3) &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**$K_{m,n}$ (Complete bipartite graph).**

Step 1. $v=m+n$, $e=mn$. Vertices in part $A$ (size $m$) each have degree $n$; vertices in part $B$ (size $n$) each have degree $m$.

Step 2. **Eulerian:**
- Every vertex in $A$ has degree $n$; every vertex in $B$ has degree $m$.
- Eulerian circuit: all degrees even $\Rightarrow$ $m$ even **and** $n$ even.
- Eulerian path (non-circuit): exactly $2$ odd-degree vertices.
  - If $n$ is even and $m$ is odd: the $n$ vertices in part $B$ each have odd degree $m$. So there are $n$ odd-degree vertices. For exactly $2$, we need $n=2$. Thus $K_{m,2}$ with $m$ odd has an Eulerian path.
  - If $m$ is even and $n$ is odd: similarly, $m$ odd-degree vertices in $A$ $\Rightarrow$ need $m=2$. Thus $K_{2,n}$ with $n$ odd has an Eulerian path.
  - If both $m,n$ are odd: $m+n$ odd-degree vertices (all vertices are odd). $m+n$ is even. For exactly $2$, $m+n=2$, i.e. $m=n=1$ ($K_{1,1}\cong K_2$), which is already covered.
- Otherwise, more than $2$ odd-degree vertices $\Rightarrow$ **neither**.

Summary for Eulerian:
- Circuit: $m$ even **and** $n$ even.
- Path (non-circuit): $\{m=2,\;n\text{ odd}\}$ or $\{n=2,\;m\text{ odd}\}$.
- Neither: otherwise.

Step 3. **Hamiltonian:**
- $K_{m,n}$ is bipartite. A Hamiltonian circuit must alternate between the two partite sets, so necessarily $|A|=|B|$, i.e. $m=n$.
  - If $m=n\ge2$, a Hamiltonian circuit exists: label vertices $a_1,\dots,a_n$ and $b_1,\dots,b_n$, trace $a_1\mdash b_1\mdash a_2\mdash b_2\mdash\cdots\mdash a_n\mdash b_n\mdash a_1$.
  - If $m=n=1$, $K_{1,1}\cong K_2$: a Hamiltonian path exists but no circuit (simple graph requires at least $3$ vertices for a cycle).
- Hamiltonian path: must alternate, so the part sizes can differ by at most $1$. Thus $|m-n|\le 1$ is necessary and sufficient.
  - If $|m-n|\le 1$, a Hamiltonian path exists.
  - If $|m-n|\ge 2$, no Hamiltonian path (you would run out of vertices in one part before alternating completes).

$$\boxed{\begin{aligned}K_{m,n} &: \text{Euler circuit: } m,n \text{ both even} &&\text{Euler path (non-circuit): } \{m=2,n\text{ odd}\}\cup\{n=2,m\text{ odd}\}\\
&\text{Hamilton circuit: } m=n\ge2 &&\text{Hamilton path: } |m-n|\le 1\end{aligned}}$$

---

**$Q_n$ ($n$-dimensional hypercube).**

Step 1. $v=2^n$, $e=n\cdot2^{n-1}$. Every vertex has degree $n$.

Step 2. **Eulerian:**
- All $2^n$ vertices share the same degree $n$.
- Eulerian circuit: all degrees even $\Rightarrow$ $n$ **even** ($n=2,4,6,\dots$).
- Eulerian path (non-circuit): exactly $2$ odd-degree vertices. This requires $2^n=2$, i.e. $n=1$ ($Q_1\cong K_2$). For $n\ge3$ odd, $2^n\ge8>2$ odd-degree vertices, so **neither**.
- For $n=0$, $Q_0$ is a single vertex (trivial, has Eulerian circuit of length $0$).

Step 3. **Hamiltonian:**
- For $n\ge2$, $Q_n$ always has a Hamiltonian circuit (well-known; construable via Gray codes). For $n=1$, $Q_1=K_2$ has a Hamiltonian path but no circuit ($v=2$). For $n=0$, trivial.

$$\boxed{\begin{aligned}Q_n &: \text{Euler circuit: } n \text{ even} &&\text{Euler path (non-circuit): } n=1\\
&\text{Hamilton circuit: } \textbf{always }(n\ge2) &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**2.** Propose an algorithm for finding an Eulerian circuit of a given graph. What is the complexity of that algorithm?

**Solution.**

We present **Hierholzer's Algorithm**, which is more efficient.

**Theorem (Euler).** A connected graph has an Eulerian circuit iff every vertex has even degree. Hierholzer's algorithm assumes this condition holds.

**Algorithm (Hierholzer, 1873):**

Step 1. Choose any starting vertex $v_0$. Initialize a stack $S$ and a list $C$ (the circuit).

Step 2. Push $v_0$ onto $S$. While $S$ is non-empty:
- Let $u$ be the top vertex of $S$.
- If $\deg(u)>0$ (i.e., $u$ still has unused incident edges):
  - Choose any incident edge $e=\{u,w\}$.
  - Remove $e$ from the graph.
  - Push $w$ onto $S$.
- Else ($\deg(u)=0$):
  - Pop $u$ from $S$ and append $u$ to $C$.

Step 3. When the stack is empty, $C$ contains the vertices in the order of an Eulerian circuit (in reverse). Reverse $C$ to obtain the circuit starting at $v_0$.

**Complexity:** $O(|V|+|E|)$. Each edge is traversed and removed exactly once; each vertex is pushed and popped at most once.

**Fleury's Algorithm (alternative, $O(|E|^2)$ naive):**
At each step, traverse an edge that is **not a bridge** in the remaining graph (unless no other choice exists). This avoids disconnecting the graph prematurely. Fleury's algorithm can be implemented in $O(|E|^2)$ with naive bridge-detection, or $O(|E|\log|V|)$ with more sophisticated data structures.

**Complexity comparison:** Hierholzer's algorithm runs in linear time $O(|V|+|E|)$ and is the preferred method.

$$\boxed{\text{Hierholzer's Algorithm: } O(|V|+|E|);\quad \text{Fleury's Algorithm: } O(|E|^2)}$$

---

**3.** Show that a bipartite graph with an odd number of vertices does not have a Hamiltonian cycle.

**Solution.**

Step 1. Let $G=(V,E)$ be a bipartite graph with bipartition $(V_1,V_2)$, so $V=V_1\cup V_2$, $V_1\cap V_2=\emptyset$, and every edge joins a vertex of $V_1$ to a vertex of $V_2$.

Step 2. Suppose for contradiction that $G$ has a Hamiltonian cycle $C$. A Hamiltonian cycle visits every vertex exactly once and returns to the start.

Step 3. Along the cycle $C$, vertices must **alternate** between $V_1$ and $V_2$, because every edge of $G$ (hence every edge of $C$) joins a vertex from $V_1$ to a vertex from $V_2$.

Step 4. Alternation forces the cycle to have equal numbers of vertices from each part: $|V_1|=|V_2|$.

Step 5. Therefore $|V|=|V_1|+|V_2|=2|V_1|$ is **even**. This contradicts the hypothesis that $|V|$ is odd.

Step 6. Hence no Hamiltonian cycle can exist.

$$\boxed{\text{A bipartite graph with an odd number of vertices has no Hamiltonian cycle.}}$$

---

**4.** A diagnostic message can be sent out over a computer network to perform tests over all links and in all devices. What sort of paths should be used to test
a. all links?
b. all devices?

**Solution.**

**(a) Testing all links (edges):**
Testing every link exactly once corresponds to traversing every edge of the network graph exactly once — this is an **Eulerian path** (or Eulerian circuit if the walk returns to the start). The test message should follow an Eulerian trail that traverses each communication link exactly once.

**(b) Testing all devices (vertices):**
Testing every device exactly once corresponds to visiting every vertex of the network graph exactly once — this is a **Hamiltonian path** (or Hamiltonian circuit if returning to start). The test message should follow a Hamiltonian path that visits each device exactly once.

$$\boxed{\begin{aligned}\text{(a) All links: } &\textbf{Eulerian path (or circuit)}\\
\text{(b) All devices: } &\textbf{Hamiltonian path (or circuit)}\end{aligned}}$$

---

**5.** Investigate the existence of a Hamiltonian cycle/path on graphs in Exercises 30–36 (Chapter 10.5, Rosen's textbook).

**Solution.**

*General methodology for investigating Hamiltonian existence:*

Step 1. Compute $n=|V|$, the degree of each vertex, and check sufficient conditions:

- **Dirac's Theorem:** If every vertex has $\deg(v)\ge n/2$, a Hamiltonian circuit exists.
- **Ore's Theorem:** If for every pair of non-adjacent $u,v$, $\deg(u)+\deg(v)\ge n$, a Hamiltonian circuit exists.
- If either condition holds, the answer is **yes**.

Step 2. If neither sufficient condition holds, attempt **direct construction**:
- Try to trace a cycle visiting all vertices exactly once. For small graphs, this is feasible by inspection.
- For bipartite graphs: check partite set sizes. If $|V_1|\neq|V_2|$, no Hamiltonian circuit exists; a Hamiltonian path requires $||V_1|-|V_2||\le 1$.

Step 3. To prove **non-existence** when construction fails:
- Look for a **cut-vertex** whose removal disconnects the graph into $k\ge2$ components — a Hamiltonian cycle would need to enter and leave each component, which is impossible if a vertex is visited only once.
- Look for a **degree obstruction**: if any vertex has degree $1$, it cannot be on a Hamiltonian circuit (though it could be an endpoint of a Hamiltonian path).

Step 4. For the specific graphs in Rosen Exercises 30–36 (Chapter 10.5), apply the above methodology to each. The typical graphs include variations of grids, bipartite graphs, and graphs with degree patterns that require case-by-case analysis. For bipartite graphs with unequal parts, no Hamiltonian circuit exists; check $|m-n|\le 1$ for Hamiltonian path.

$$\boxed{\text{Methodology: Dirac/Ore sufficient conditions } \to \text{ direct construction } \to \text{ structural obstruction}}$$

---

**6.** Investigate the existence of an Eulerian cycle/path on graphs in Exercises 13–14, 18–22 (Chapter 10.5, Rosen's textbook).

**Solution.**

*General methodology for investigating Eulerian existence:*

Step 1. Compute the degree of every vertex in the graph.

Step 2. Apply **Euler's Theorem**:
- If **every** vertex has even degree, an **Eulerian circuit** exists (start anywhere).
- If **exactly two** vertices have odd degree, an **Eulerian path** (non-circuit) exists and must start at one odd-degree vertex and end at the other.
- If more than two vertices have odd degree, **neither** exists.

Step 3. Additionally, the graph must be **connected** (or all edges must belong to a single connected component — isolated vertices with no edges are irrelevant). If the graph is disconnected and edges exist in multiple components, no Eulerian trail covering all edges exists.

Step 4. For directed graphs: Eulerian circuit exists iff $\deg^+(v)=\deg^-(v)$ for every vertex $v$; Eulerian path exists iff exactly one vertex has $\deg^+-\deg^-=1$ (start) and exactly one has $\deg^--\deg^+=1$ (end), with all others balanced.

Step 5. Apply this check to each of the graphs in Rosen Exercises 13–14, 18–22: compute degree sequences, count odd-degree vertices, and conclude.

$$\boxed{\text{Methodology: count odd-degree vertices; } 0 \Rightarrow \text{circuit, } 2 \Rightarrow \text{path, } >2 \Rightarrow \text{neither}}$$

---

**7.** Construct a Gray code of $n$ contacts.

**Solution.**

A Gray code of $n$ bits is a cyclic ordering of all $2^n$ binary strings of length $n$ such that consecutive strings differ in exactly one bit. Equivalently, it is a Hamiltonian circuit on $Q_n$.

**Construction by induction on $n$:**

Step 1. **Base case $n=1$:** The Gray code of $1$ bit is $[0,\;1]$. Consecutive strings differ in exactly one bit, and we may cyclically close by noting $1$ and $0$ differ in one bit.

Step 2. **Induction hypothesis:** Assume we have a Gray code $G_{n-1}=[g_1,g_2,\dots,g_{2^{n-1}}]$ for $n-1$ bits, where each $g_i$ is an $(n-1)$-bit string, consecutive strings differ in one bit, and $g_1$ and $g_{2^{n-1}}$ differ in one bit.

Step 3. **Induction step:** Construct $G_n$ from $G_{n-1}$ as follows:
- **Forward pass:** Prepend a $0$ to each string in $G_{n-1}$. This gives the first half: $[0g_1,\;0g_2,\;\dots,\;0g_{2^{n-1}}]$.
- **Reverse pass:** Prepend a $1$ to each string in the **reverse** of $G_{n-1}$ (i.e., $[g_{2^{n-1}},\dots,g_2,g_1]$). This gives the second half: $[1g_{2^{n-1}},\;\dots,\;1g_2,\;1g_1]$.

The concatenated sequence has length $2\cdot2^{n-1}=2^n$, covering all $n$-bit strings.

Step 4. **Verification of the one-bit-difference property:**
- Within each half, consecutive strings differ in one bit (by induction hypothesis, since the same prefix bit is attached).
- At the **junction** between the two halves: $0g_{2^{n-1}}$ and $1g_{2^{n-1}}$ differ only in the first (new) bit.
- At the **cyclic junction** (wrap-around from $1g_1$ back to $0g_1$): these differ only in the first bit.
- At the **middle junction** within the second half (where the reversal happens), consecutiveness is preserved because $G_{n-1}$ was reversed, maintaining the one-bit-difference property in reverse order.

Step 5. By induction, a Gray code exists for all $n\ge1$.

**Example ($n=3$):**
$G_1=[0,1]$.
$G_2=[00,01,11,10]$ (prepend $0$ to $[0,1]$, then prepend $1$ to $[1,0]$).
$G_3=[000,001,011,010,110,111,101,100]$.

$$\boxed{\text{Gray code constructed by induction: } G_n = [0G_{n-1}]\;||\;[1\,\text{rev}(G_{n-1})]}$$

---

**8.** How many faces are there in a tree of $n$ vertices?

**Solution.**

Step 1. A tree $T$ with $n$ vertices is a connected acyclic graph, hence planar (it can be drawn in the plane without edge crossings).

Step 2. For a tree: $|V|=n$, $|E|=n-1$. The tree is connected, so $c=1$.

Step 3. By **Euler's formula** for connected planar graphs: $v-e+f=2$.

Step 4. Substitute: $n-(n-1)+f=2 \;\Longrightarrow\; 1+f=2 \;\Longrightarrow\; f=1$.

Step 5. The single face is the **outer (unbounded) face**. A tree has no cycles, so it cannot enclose any bounded region.

$$\boxed{f=1 \text{ (the outer face)}}$$

---

**9.** Can six houses be connected to two utilities without connections crossing?

**Solution.**

Step 1. Model six houses and two utilities as a complete bipartite graph $K_{6,2}$, where houses are one partite set ($m=6$) and utilities are the other ($n=2$).

Step 2. Compute parameters: $v=m+n=6+2=8$, $e=mn=6\times2=12$.

Step 3. $K_{6,2}$ is bipartite, thus **triangle-free** (no cycle of length $3$ is possible in a bipartite graph). Apply the triangle-free planar edge bound:

$$e\le 2v-4$$

Step 4. Compute $2v-4=2\cdot8-4=16-4=12$. Since $e=12\le12$, the bound is **not violated**.

Step 5. The bound is necessary but not sufficient. However, $K_{n,2}$ is known to be planar for **all** $n$. We can draw it: place the $2$ utility vertices on a horizontal line, place the $6$ houses in an arc above (or on both sides), and connect each house to each utility without crossings (all edges are straight-line segments if houses are positioned appropriately).

Step 6. Thus six houses **can** be connected to two utilities without crossings.

$$\boxed{\text{Yes; } K_{6,2} \text{ is planar (e.g. via a planar embedding of } K_{n,2} \text{ for any } n)}$$

---

**10.** Are $Q_4$, $Q_5$, $Q_6$ planar?

**Solution.**

Recall for $Q_n$ (the $n$-dimensional hypercube): $v=2^n$, $e=n\cdot2^{n-1}$.

**$Q_4$:**

Step 1. $v=2^4=16$, $e=4\cdot2^3=32$.

Step 2. Apply the general planar edge bound: $e\le3v-6$.

$$3v-6=3\cdot16-6=48-6=42.$$

Since $e=32\le42$, the bound is **not violated** — the bound test is inconclusive.

Step 3. By **Kuratowski's Theorem**, a graph is non-planar iff it contains a subdivision of $K_5$ or $K_{3,3}$. It is a known result that $Q_4$ contains a subdivision of $K_{3,3}$ (for example, vertices $\{0000,0011,0101,0110\}$ can be shown to form one part with paths through the hypercube to vertices in another appropriately chosen set). Therefore $Q_4$ is **non-planar**.

Step 4. Alternatively, $Q_4$ has genus $1$ (requires a torus for embedding without crossings), which directly implies non-planarity.

Thus $Q_4$ is **not planar**.

**$Q_5$:**

Step 1. $Q_5$ contains $Q_4$ as a subgraph (by fixing any one coordinate). Since $Q_4$ is non-planar, any supergraph is also non-planar.

Step 2. Alternatively, $v=2^5=32$, $e=5\cdot2^4=80$. Bound: $3v-6=96-6=90\ge80$ — inconclusive, but the subgraph argument suffices.

Thus $Q_5$ is **not planar**.

**$Q_6$:**

Step 1. $v=2^6=64$, $e=6\cdot2^5=6\cdot32=192$.

Step 2. Apply the edge bound: $3v-6=3\cdot64-6=192-6=186$.

Step 3. $e=192>186$. The bound is **violated**. By the necessary condition for planarity, $Q_6$ is **non-planar**.

$$\boxed{\begin{aligned}Q_4 &: \textbf{Not planar} \text{ (contains } K_{3,3} \text{ subdivision)}\\
Q_5 &: \textbf{Not planar} \text{ (contains } Q_4 \text{ as subgraph)}\\
Q_6 &: \textbf{Not planar} \text{ (} e=192 > 3v-6=186 \text{)}\end{aligned}}$$

---

**11.** Prove that if $G$ is a connected and planar graph, then $G$ has a vertex of degree not exceeding five.

**Solution.**

Step 1. Let $G$ be a connected planar simple graph with $v\ge3$ vertices and $e$ edges. By the general planar edge bound:

$$e\le 3v-6.$$

Step 2. By the **Handshaking Lemma**:

$$\sum_{i=1}^{v}\deg(v_i)=2e.$$

Step 3. Suppose, for contradiction, that every vertex has degree at least $6$, i.e., $\deg(v_i)\ge6$ for all $i=1,\dots,v$.

Step 4. Then:

$$2e=\sum_{i=1}^{v}\deg(v_i)\ge\sum_{i=1}^{v}6=6v\;\Longrightarrow\;e\ge3v.$$

Step 5. Combine with the planar bound:

$$3v\le e\le 3v-6\;\Longrightarrow\;3v\le3v-6\;\Longrightarrow\;0\le-6,$$

which is a contradiction.

Step 6. Therefore, the assumption that all vertices have degree $\ge6$ is false. Hence $G$ must have at least one vertex of degree $\le5$.

(For $v=1,2$, the statement is trivially true as the maximum possible degree is $v-1\le1$.)

$$\boxed{\text{Every connected planar graph has a vertex of degree } \le 5.}$$

---

**12.** Suppose that a connected planar graph has 20 vertices, each of degree 3. Into how many regions does a representation of this planar graph split the plane?

**Solution.**

Step 1. Given: $v=20$ vertices, each of degree $3$. The graph is connected and planar.

Step 2. By the **Handshaking Lemma**:

$$\sum_{v\in V}\deg(v)=2e\;\Longrightarrow\;20\cdot3=60=2e\;\Longrightarrow\;e=30.$$

Step 3. By **Euler's formula** for a connected planar graph:

$$v-e+f=2.$$

Step 4. Substitute:

$$20-30+f=2\;\Longrightarrow\;-10+f=2\;\Longrightarrow\;f=12.$$

Step 5. Thus the representation splits the plane into $12$ regions (faces).

$$\boxed{f=12 \text{ regions}}$$

---

**13.** Is the Petersen graph planar?

**Solution.**

Step 1. The Petersen graph has $v=10$ vertices and $e=15$ edges.

Step 2. Apply the edge bound: $3v-6=3\cdot10-6=24$. Since $e=15\le24$, the bound is **not violated** — the test is inconclusive.

Step 3. Use **Kuratowski's Theorem**: a graph is non-planar iff it contains a subdivision of $K_5$ or $K_{3,3}$.

Step 4. The Petersen graph is well-known to contain a subdivision of $K_{3,3}$. One explicit construction:

Label the outer $5$-cycle vertices as $a_1,a_2,a_3,a_4,a_5$ (in cyclic order) and the inner $5$-star (pentagram) vertices as $b_1,b_2,b_3,b_4,b_5$, where $b_i$ is connected to $a_i$, $b_{i+2}$ (mod $5$), and $b_{i+1}$ (mod $5$) in the pentagram arrangement.

Then identify two sets of three vertices, e.g. $\{a_1,a_3,b_2\}$ and $\{a_2,a_4,b_5\}$. One can find six internally vertex-disjoint paths connecting each vertex of the first set to each vertex of the second set, forming a $K_{3,3}$ subdivision.

Step 5. Since the Petersen graph contains a $K_{3,3}$ subdivision, by Kuratowski's Theorem it is **non-planar**.

$$\boxed{\text{The Petersen graph is } \textbf{not planar} \text{ (contains a } K_{3,3} \text{ subdivision)}.}$$

---

**14.** Are $K_{3,4}$, $K_6$ planar?

**Solution.**

**$K_{3,4}$:**

Step 1. $K_{3,4}$ has $v=3+4=7$ vertices, $e=3\cdot4=12$ edges.

Step 2. $K_{3,4}$ is bipartite, hence **triangle-free** (containing no $3$-cycle). Apply the triangle-free planar edge bound:

$$e\le 2v-4.$$

Step 3. Compute: $2v-4=2\cdot7-4=14-4=10$. Since $e=12>10$, the bound is **violated**.

Step 4. Therefore $K_{3,4}$ is **non-planar** (by violation of a necessary condition for planarity of triangle-free graphs).

**$K_6$:**

Step 1. $K_6$ has $v=6$ vertices, $e=C(6,2)=15$ edges.

Step 2. Apply the general planar edge bound: $e\le 3v-6$.

Step 3. Compute: $3v-6=3\cdot6-6=18-6=12$. Since $e=15>12$, the bound is **violated**.

Step 4. Therefore $K_6$ is **non-planar**.

$$\boxed{\begin{aligned}K_{3,4} &: \textbf{Not planar} \text{ (} e=12 > 2v-4=10 \text{)}\\
K_6 &: \textbf{Not planar} \text{ (} e=15 > 3v-6=12 \text{)}\end{aligned}}$$

---

**15.** Show that any connected triangle-free planar graph (i.e., it has no simple cycle of length three) has at least one vertex of degree not exceeding three.

**Solution.**

Step 1. Let $G$ be a connected, triangle-free, planar simple graph with $v\ge3$ vertices and $e$ edges. Since $G$ is triangle-free, every face in any planar embedding is bounded by at least $4$ edges. Consequently, the tighter planar edge bound applies:

$$e\le 2v-4.$$

Step 2. By the **Handshaking Lemma**:

$$\sum_{i=1}^{v}\deg(v_i)=2e.$$

Step 3. Suppose, for contradiction, that every vertex has degree at least $4$, i.e., $\deg(v_i)\ge4$ for all $i=1,\dots,v$.

Step 4. Then:

$$2e=\sum_{i=1}^{v}\deg(v_i)\ge\sum_{i=1}^{v}4=4v\;\Longrightarrow\;e\ge 2v.$$

Step 5. Combine with the triangle-free planar bound:

$$2v\le e\le 2v-4\;\Longrightarrow\;2v\le2v-4\;\Longrightarrow\;0\le-4,$$

which is a contradiction.

Step 6. Therefore, the assumption that all vertices have degree $\ge4$ is false. Hence $G$ must have at least one vertex of degree $\le3$.

(For $v=1,2$, the statement holds trivially as maximum degree is at most $1$.)

$$\boxed{\text{Every connected triangle-free planar graph has a vertex of degree } \le 3.}$$

---

**16.** Prove by induction on the number of vertices that any connected triangle-free planar graph is $4$-colorable.

**Solution.**

Step 1. **Theorem statement:** Every connected, triangle-free, planar graph $G$ is $4$-colorable (i.e., its vertices can be colored with at most $4$ colors such that adjacent vertices receive different colors).

Step 2. **Base case:** For $v=1$, a single vertex requires only $1$ color. For $v=2$, two adjacent vertices require at most $2$ colors. All small cases ($v\le4$) are trivially $4$-colorable.

Step 3. **Induction hypothesis:** Assume that every connected, triangle-free, planar graph with fewer than $n$ vertices is $4$-colorable.

Step 4. **Induction step:** Let $G$ be a connected, triangle-free, planar graph with $n$ vertices ($n\ge3$). By **Problem 15**, $G$ contains a vertex $v_0$ with $\deg(v_0)\le 3$.

Step 5. Delete $v_0$ (and all incident edges) to obtain $G' = G - v_0$. The graph $G'$:
- Is planar (subgraph of a planar graph).
- Is triangle-free (removing vertices cannot create new $3$-cycles; in fact, a triangle in $G'$ would also be a triangle in $G$, contradicting that $G$ is triangle-free).
- May be disconnected. However, we can apply the induction hypothesis to each connected component of $G'$ separately (each has $< n$ vertices) and combine the colorings. If $G'$ is connected, the induction hypothesis applies directly.

Step 6. By the induction hypothesis, $G'$ is $4$-colorable. Fix a $4$-coloring of $G'$ using colors $\{1,2,3,4\}$.

Step 7. Consider $v_0$ in $G$. Its neighbors in $G$ are at most $3$ vertices (since $\deg(v_0)\le3$). These neighbors are all in $G'$, so they have been colored. At most $3$ colors appear among the neighbors of $v_0$.

Step 8. Since only $4$ colors are available and at most $3$ are used by $v_0$'s neighbors, there is at least one color $c\in\{1,2,3,4\}$ **not** used by any neighbor of $v_0$. Assign color $c$ to $v_0$.

Step 9. This extends the $4$-coloring of $G'$ to a valid $4$-coloring of $G$, completing the induction.

**Remark.** The stronger statement — that every connected triangle-free planar graph is **$3$-colorable** — is **Grötzsch's Theorem** (a deep result). The problem asks only for $4$-colorability, which follows easily from the existence of a vertex of degree $\le3$ (Problem 15) and induction.

$$\boxed{\text{Proved by induction: delete a vertex of degree } \le 3, \text{ 4-color the remainder, and color the deleted vertex.}}$$
