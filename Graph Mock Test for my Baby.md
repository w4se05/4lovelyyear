**Question 1: Resource Conflict Scheduling (Graph Modeling & Coloring)** You have been appointed as the operations lead at the Lingzhi Tech Conference. You must schedule 6 highly anticipated workshops ($V_1$ through $V_6$). Because many attendees have registered for multiple workshops, certain sessions cannot be scheduled during the same time slot without forcing attendees to miss out.

The attendee overlap dictates the following conflicts:

- $V_1$ cannot run concurrently with $V_2, V_3$, or $V_5$.
    
- $V_2$ cannot run concurrently with $V_1, V_3, V_4$, or $V_6$.
    
- $V_3$ cannot run concurrently with $V_1, V_2, V_5$, or $V_6$.
    
- $V_4$ cannot run concurrently with $V_2$ or $V_6$.
    
- $V_5$ cannot run concurrently with $V_1, V_3$, or $V_6$.
    
- $V_6$ cannot run concurrently with $V_2, V_3, V_4$, or $V_5$.
    

**Tasks:**

1. Model this scheduling scenario as a graph problem. Explicitly state what your vertices and edges represent in this context.
    
2. By applying vertex coloring principles, determine the absolute minimum number of time slots required to host all 6 workshops without any attendee conflicts.
    
3. Provide a valid, optimal schedule mapping each workshop to a specific time slot (e.g., Slot 1, Slot 2, etc.).
    

---

**Question 2: Multi-Source Spread Tracking (Breadth-First Search)**

An automated warehouse is conceptually divided into a $5 \times 5$ grid of storage areas. At Day 0, a hazardous chemical spill occurs simultaneously at two distinct origin cells: coordinate $(1, 1)$ at the top-left, and coordinate $(4, 3)$.

The hazardous material spreads exclusively to adjacent areas (up, down, left, right—not diagonally) taking exactly 1 full day to infect the neighboring cell. The time an area is reached is the smallest time among all sources.

**Tasks:**

1. Draw the $5 \times 5$ grid and populate every single cell with the exact day number it becomes compromised by the spill.
    
2. Identify the exact coordinates of the cell (or cells) that will be the last to be compromised. Exactly how many days will it take for the entire warehouse to be 100% infected?
    
3. Explain how a queue-based Breadth-First Search (BFS) implementation naturally accommodates multiple simultaneous starting locations without requiring separate, parallel graph traversals.
    

---

**Question 3: Network Resilience (Kruskal's Algorithm)** An Internet Service Provider is designing a regional fiber-optic backbone to connect 7 districts ($A, B, C, D, E, F, G$). The feasible links and their construction costs (in millions of USD) are:

- $(A, B): 4, (A, C): 8, (A, D): 12$
    
- $(B, C): 9, (B, E): 10$
    
- $(C, D): 6, (C, E): 7, (C, F): 11$
    
- $(D, F): 5$
    
- $(E, F): 8, (E, G): 14$
    
- $(F, G): 15$
    

**Tasks:**

1. Apply Kruskal’s Algorithm to determine the Minimum Spanning Tree (MST) for this network. Write down your sorted edge list and explicitly mark which edges are added to the MST and which are rejected (and why).
    
2. What is the total minimum cost to connect all 7 districts?
    
3. **Stress Test:** Suppose geological surveys conclude that the link $(C, E)$ is impossible to build. Identify the new edges that would form the updated MST and calculate the revised total cost.
    

---

**Question 4: Automated Routing (Dijkstra's Algorithm)** You are programming the navigation logic for an autonomous vehicle. The facility consists of 6 checkpoints ($S, A, B, C, D, T$). The traversal times (in seconds) between the checkpoints are given as undirected weighted edges:

- $(S, A): 4, (S, B): 2$
    
- $(A, B): 1, (A, C): 5, (A, D): 3$
    
- $(B, C): 8, (B, D): 10$
    
- $(C, D): 2, (C, T): 6$
    
- $(D, T): 6$
    

**Tasks:**

1. Use Dijkstra’s Algorithm to find the shortest path from the starting checkpoint $S$ to the target checkpoint $T$.
    
2. Provide a step-by-step trace table. For each iteration, you must display:
    
    - The vertex currently being processed.
        
    - The state of the Fringe ($F$) vertices.
        
    - The updated cost labels $c(u)$ for all fringe vertices.
        
3. State the final shortest path sequence (the exact checkpoints visited) and the minimum traversal time.
    

---

**Question 5: Traversal Verification (Adjacency Matrix Walk Counting)** A factory's rail system is modeled as a simple directed graph containing 3 transfer stations: $v_1, v_2, v_3$. The adjacency matrix $A$ dictating the number of physical directed tracks between stations is:

$$A = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 2 \\ 2 & 1 & 0 \end{bmatrix}$$

**Tasks:**

1. Calculate the resulting matrix $A^2$.
    
2. What does the integer located in the 3rd row, 1st column of $A^2$ represent in the real world? Write out the exact, specific sequences of stations that correspond to this integer.
    
3. By utilizing the properties of adjacency matrices, compute the exact number of valid tracks/walks of **length 3** starting specifically from station $v_2$ and ending at station $v_3$. Show the specific row-by-column matrix multiplication required to isolate this value.