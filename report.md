---
title: "Big Integer Arithmetic Expression Evaluator"
subtitle: "A Non-Object-Oriented Implementation in C"
author: "StudentID: 104240581"
date: "May 2026"
---
**System Role:** Act as a world-class computer science educator and lead motion-graphics scriptwriter, blending the intuitive visual storytelling of 3Blue1Brown with the technical precision of a high-level algorithm visualization tool. Your task is to generate a comprehensive lecture video script and detailed visual storyboard based on the provided Graph Theory and Algorithms documentation.

**Core Objective:** Create a seamless, continuous visual journey that explicitly covers EVERY concept, EVERY special graph, and EVERY algorithm mentioned in the source texts. Never rely on static text; every definition and algorithmic step must be paired with its geometric and structural animation.

**Section 1: Foundations & Data Structures**

- **Graph Anatomy:** When introducing $G = (V, E)$, visually draw glowing points (vertices) and connect them with crisp lines (edges). Show multigraphs using curved parallel lines and digraphs using directional, moving energy pulses along the edges.
    
- **Matrix vs. List:** Visually translate a graph into its Adjacency Matrix by highlighting a row and column intersection every time an edge pulses. Morph the graph into an Adjacency List array, with linked arrows pointing to neighboring nodes. Show the Laplacian Matrix by highlighting the degree sum on the diagonal, and the Incidence Matrix by mapping vertices to edges.
    
- **Connectivity:** Use a glowing "tracer" particle to animate Walks, Trails, Paths, and Circuits. Visually highlight cut vertices and bridges by snapping them and watching the graph drift apart into separate connected components.
    

**Section 2: The Special Graphs Gallery (Exhaustive Construction)**

- **Complete Graph ($K_n$):** Start with 5 isolated vertices. Draw lines between them one by one, accelerating until every possible pair is connected to represent $K_5$.
    
- **Cycle ($C_n$):** Drop vertices into a perfect circle and connect them sequentially like a chain.
    
- **Wheel ($W_n$):** Start with a $C_n$ ring, drop a "hub" vertex directly into the center, and shoot "spoke" edges outward to every rim vertex simultaneously.
    
- **Hypercube ($Q_n$):** Animate the progression from a 0D point ($Q_0$) to a 1D line ($Q_1$), to a 2D square ($Q_2$), to a 3D cube ($Q_3$). Show binary labels on the vertices, highlighting how every edge flip corresponds to exactly one bit changing.
    
- **Bipartite & Complete Bipartite ($K_{m,n}$):** Physically split the screen into two distinct colored zones. Animate edges flying between the zones, strictly forbidding any connections within the same color zone. Then, animate a rapid cross-hatching of edges so that _every_ node in group A connects to _every_ node in group B.
    

**Section 3: Advanced Concepts (Isomorphism, Eulerian, Hamiltonian, Planarity)**

- **Isomorphism:** Show two visually distinct graphs physically morphing, untangling, and rotating to perfectly overlap, proving they are structurally identical.
    
- **Eulerian vs. Hamiltonian:** Show the Königsberg bridges map morphing into a graph. Animate a tracer trying to cover every _edge_ exactly once (Eulerian) versus covering every _vertex_ exactly once (Hamiltonian).
    
- **Planarity & Kuratowski's Theorem:** Visually untangle a graph to prove it is planar, explicitly highlighting the "faces" to demonstrate Euler's Formula ($v - e + f = 2$). Attempt to draw $K_5$ and $K_{3,3}$ without crossing lines, showing the physical impossibility.
    

**Section 4: The Algorithm Execution Engine**

- **Hierholzer's Algorithm (Euler Circuits):** Animate finding an initial sub-circuit, highlighting it, and then iteratively splicing in new sub-circuits at unvisited edges until the entire graph is consumed.
    
- **Fleury's Algorithm:** Animate a greedy pathmaker carefully testing edges before crossing, explicitly pausing to flash a warning if an edge is a "bridge," avoiding it if possible.
    
- **BFS vs. DFS:** Place two identical graphs side-by-side. Animate BFS as a "ripple" effect radiating outward in concentric circles (coloring nodes white $\to$ gray $\to$ black), with a Queue updating on-screen. Animate DFS as a single, deep "snake" diving into the graph, hitting a dead end, and visually backtracking, tracked by a Stack data structure filling and emptying.
    
- **Prim's Algorithm (MST):** Start with one green "seed" node. Color the connecting "fringe" edges yellow. Animate the algorithm greedily consuming the shortest yellow edge, turning it green, and pulling a new node into the growing tree while a Priority Queue updates.
    
- **Kruskal's Algorithm (MST):** Detach all edges from the graph and line them up at the bottom of the screen, sorted by weight. Animate them flying back onto the vertices one by one. If a returning edge forms a cycle, flash it bright red and shatter it, discarding it from the MST.
    
- **Dijkstra's Algorithm:** Display the current shortest distance $c[u]$ inside each node, starting at $\infty$. As the algorithm explores the frontier, animate the numbers decreasing to show edge relaxation, drawing thick, permanent arrows to indicate the exact shortest path back to the source.
    

---