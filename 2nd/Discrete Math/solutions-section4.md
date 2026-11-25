# Sect.4 Trees — Full Solutions

---

**1.** Given the rooted tree (root $d$; children of $d$: $a,c,o,i$; children of $c$: $b,k,g$; children of $b$: $h,l$; children of $i$: $f$; children of $f$: $e,m,n$; children of $h$: $p,q$):

**Solution.**
Step 1. Draw the tree structure explicitly:
- Level 0: $d$
- Level 1: $a,c,o,i$ (children of $d$)
- Level 2: $b,k,g$ (children of $c$); $f$ (child of $i$)
- Level 3: $h,l$ (children of $b$); $e,m,n$ (children of $f$)
- Level 4: $p,q$ (children of $h$)

**(a)** The designated top vertex with no parent is $d$.

**(b)** Internal vertices have at least one child: $d,c,b,h,i,f$. (6 vertices)

**(c)** Leaves have no children: $a,o,k,g,l,e,m,n,p,q$. (10 vertices)

**(d)** Level 3 vertices (distance 3 from root): $h,l,e,m,n$.

**(e)** Height of subtree rooted at $c$: longest path $c\to b\to h\to p$ has 3 edges, so height = 3.

**(f)** Descendants of $b$: $h,l$ (children) and $p,q$ (children of $h$). So $\{h,l,p,q\}$.

**(g)** Balanced? Leaves appear at levels 1 ($a,o$), 2 ($k,g$), 3 ($l,e,m,n$), and 4 ($p,q$). Leaf levels differ by more than 1, so **not balanced**.

**(h)** Ancestors of $q$: $h\to b\to c\to d$. So $\{h,b,c,d\}$.

$$\boxed{\begin{aligned}
\text{(a) }&d\\
\text{(b) }&d,c,b,h,i,f\\
\text{(c) }&a,o,k,g,l,e,m,n,p,q\\
\text{(d) }&\{h,l,e,m,n\}\\
\text{(e) }&3\\
\text{(f) }&\{h,l,p,q\}\\
\text{(g) }&\text{Not balanced}\\
\text{(h) }&\{h,b,c,d\}
\end{aligned}}$$

---

**2.** How many non-isomorphic unrooted trees are there with 3 vertices?

**Solution.**
Step 1. Any tree with 3 vertices has $3-1=2$ edges. All such trees are paths $P_3$. There is exactly 1 non-isomorphic tree.

$$\boxed{1 \text{ (the path } P_3\text{)}}$$

---

**3.** How many non-isomorphic unrooted trees are there with 4 vertices?

**Solution.**
Step 1. Trees with 4 vertices have $4-1=3$ edges. Up to isomorphism, only two degree-sequence patterns exist:
- $P_4$ (path, degree sequence $(2,2,1,1)$)
- $K_{1,3}$ (star, degree sequence $(3,1,1,1)$)

Step 2. Any other tree on 4 vertices is isomorphic to one of these two.

$$\boxed{2\text{ (the path }P_4\text{ and the star }K_{1,3}\text{)}}$$

---

**4.** How many leaves does a full 3-ary tree with 100 vertices have?

**Solution.**
Step 1. For a full $m$-ary tree: $n=mi+1$, where $n$ = total vertices, $i$ = internal vertices.
Step 2. $100=3i+1 \Rightarrow 3i=99 \Rightarrow i=33$.
Step 3. Leaves $=n-i=100-33=67$. Equivalently: leaves $=(m-1)i+1=2\cdot33+1=67$.

$$\boxed{67}$$

---

**5.** Either draw a full $m$-ary tree with 84 leaves and height 3, or show that no such tree exists.

**Solution.**
Step 1. For a full $m$-ary tree: leaves $l=84=(m-1)i+1$, so $(m-1)i=83$.
Step 2. Since $83$ is prime, $m-1\in\{1,83\}$, so $m\in\{2,84\}$.
Step 3. Height bound: $l\le m^3$ must hold.
- $m=2$: $2^3=8<84$ (fails).
- $m=84$: satisfies the bound, but $i=1$ gives only 1 internal vertex, so height is at most 1, not 3.
Step 4. No $m$ satisfies all constraints simultaneously.

$$\boxed{\text{No such tree exists.}}$$

---

**6.** Does there exist a full 4-ary tree with 80 leaves?

**Solution.**
Step 1. Leaves $l=80=(4-1)i+1=3i+1$, so $3i=79$.
Step 2. $i=79/3$ is not an integer. Hence no such tree exists.

$$\boxed{\text{No }(3i=79\text{ has no integer solution}).}$$

---

**7.** Does there exist a full $m$-ary tree with height 4 and 100 leaves?

**Solution.**
Step 1. Leaves $l=100=(m-1)i+1$, so $(m-1)i=99$. Divisors of $99$: $1,3,9,11,33,99$. So $m\in\{2,4,10,12,34,100\}$.
Step 2. Height bound: $100\le m^4$.
- $m=2$: $16<100$ (fails). All $m\ge4$ satisfy $m^4\ge256\ge100$.
Step 3. Try $m=4$: $i=99/3=33$ internal vertices. Max internal for height 4 balanced tree: $(4^4-1)/3=85$. Min internal for height 4: 4. Since $4\le33\le85$, **construction is possible**.
Step 4. For $m=4$: build a chain of 4 internal vertices to reach height 4, distribute the remaining 29 internal vertices in levels 1--3. All internal vertices have exactly 4 children. Total leaves $=4\times33-33+1=100$. Such a tree exists.

$$\boxed{\text{Yes, for } m=4 \text{ (33 internal vertices, 100 leaves, height 4).}}$$

---

**8.** Suppose 1000 people enter a chess tournament (single-elimination). How many games must be played?

**Solution.**
Step 1. Each game eliminates exactly one player. To reduce 1000 players to 1 champion, 999 players must be eliminated.
Step 2. Hence exactly 999 games are needed.

$$\boxed{999}$$

---

**9.** How many edges are there in a forest of $k$ trees and $n$ vertices?

**Solution.**
Step 1. Let tree $i$ have $n_i$ vertices; then it has $n_i-1$ edges. And $\sum_{i=1}^{k}n_i=n$.
Step 2. Total edges $=\sum_{i=1}^{k}(n_i-1)=\left(\sum n_i\right)-k=n-k$.

$$\boxed{n-k}$$

---

**10.** Using alphabetical order, construct a binary search tree for the words in the sentence "The quick brown fox jumps over the lazy dog."

**Solution.**
Step 1. Words (in sentence order): the, quick, brown, fox, jumps, over, the, lazy, dog. Ignore duplicate "the".

Step 2. Insert in order using alphabetical comparison:
1. Insert "the" $\to$ root.
2. "quick" $>$ "the" $\to$ right child of "the".
3. "brown" $<$ "the" $\to$ left child of "the".
4. "fox" $<$ "the" $\to$ left; $>$ "brown" $\to$ right child of "brown".
5. "jumps" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $>$ "fox" $\to$ right child of "fox".
6. "over" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $>$ "fox" $\to$ right; $>$ "jumps" $\to$ right child of "jumps".
7. "the" (skip duplicate).
8. "lazy" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $>$ "fox" $\to$ right; $<$ "jumps" $\to$ left child of "jumps".
9. "dog" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $<$ "fox" $\to$ left child of "fox".

```
        the
       /   \
   brown   quick
   /   \
 dog   fox
       /  \
    lazy  jumps
             \
            over
```

$$\boxed{\text{BST as shown above.}}$$

---

**11.** How many weighings of a balance scale are needed to find a lighter counterfeit coin among four coins? Describe an algorithm.

**Solution.**
Step 1. $l=4$ possible outcomes (which coin is light). Balance scale: $m=3$ outcomes per weighing. Decision tree bound: $h\ge\lceil\log_3 4\rceil=\lceil1.26\rceil=2$.
Step 2. Algorithm:
- **Weighing 1:** Coin 1 vs Coin 2.
  - If 1 lighter $\to$ coin 1 is counterfeit.
  - If 2 lighter $\to$ coin 2 is counterfeit.
  - If balanced $\to$ counterfeit is among $\{3,4\}$.
    - **Weighing 2:** Coin 3 vs Coin 4. The lighter one is counterfeit.
Step 3. Worst case: 2 weighings.

$$\boxed{2\text{ weighings}}$$

---

**12.** How many weighings are needed to find a counterfeit coin among four coins if it may be either heavier or lighter?

**Solution.**
Step 1. $l=4\times2=8$ outcomes (which coin + heavier/lighter). $h\ge\lceil\log_3 8\rceil=\lceil1.89\rceil=2$. Information-theoretically possible ($3^2=9\ge8$).
Step 2. Algorithm:
- **Weighing 1:** Coin 1 vs Coin 2.
  - **Case A (balanced):** 1 and 2 are genuine. Counterfeit is 3 or 4.
    - **Weighing 2:** Coin 3 vs Coin 1 (genuine). If balanced $\to$ Coin 4 is counterfeit. If unbalanced $\to$ Coin 3 is counterfeit.
  - **Case B (Coin 1 heavier):** Possibilities: 1 heavy or 2 light. Coins 3,4 are genuine.
    - **Weighing 2:** Coin 1 vs Coin 3 (genuine). If 1 = 3 $\to$ Coin 2 is counterfeit (light). If 1 heavier $\to$ Coin 1 is counterfeit (heavy).
  - **Case C (Coin 2 heavier):** Symmetric. Weigh 2 vs 3.
Step 3. In all cases, 2 weighings identify the counterfeit.

$$\boxed{2\text{ weighings}}$$

---

**13.** Using a decision tree to classify the given IDs.

**Solution.**
Step 1. The data:

| ID | time | gender | area  | risk |
|----|------|--------|-------|------|
| 1  | 1-2  | male   | urban | low  |
| 2  | 2-7  | male   | rural | high |
| 3  | >7   | female | rural | low  |
| 4  | 1-2  | female | rural | high |
| 5  | >7   | male   | rural | high |
| 6  | 1-2  | male   | rural | high |
| 7  | 2-7  | female | urban | low  |
| 8  | 2-7  | male   | urban | low  |

Step 2. Decision tree (using time first, then gender, then area):

```
                time
           /     |     \
        1-2    2-7     >7
        /        |        \
     gender    gender     gender
     /   \     /   \      /   \
   male  fem male  fem  male  fem
   / \    |   / \   |    |     |
area  high area low low  high  low
/ \       / \
u  r     u   r
|  |     |   |
low high low high
```

**Formal rules:**
- Root: time
  - **1-2:** check gender
    - **male:** check area $\to$ *urban*: low; *rural*: high
    - **female:** $\to$ high
  - **2-7:** check gender
    - **male:** check area $\to$ *urban*: low; *rural*: high
    - **female:** $\to$ low
  - **>7:** check gender
    - **male:** $\to$ high
    - **female:** $\to$ low

Step 3. The tree correctly classifies all 8 training examples.

$$\boxed{\text{Decision tree as described above.}}$$

---

**14.** Decision tree for classifying questions based on attributes L, M, and difficulty D.

**Solution.**
Step 1. The training data:

| L | M | D | Q |
|---|---|---|---|
| 0 | 0 | - | 1 |
| 0 | 0 | + | 2 |
| 0 | 1 | - | 3 |
| 0 | 1 | + | 4 |
| 1 | 0 | - | 5 |
| 1 | 0 | + | 6 |
| 1 | 1 | - | 7 |
| 1 | 1 | + | 8 |

Step 2. Every combination $(L,M)$ appears once with $D=-$ and once with $D=+$. The data is perfectly balanced; no attribute or combination of attributes perfectly separates the classes.

Step 3. The decision tree must check both attributes to reach a leaf:

```
      L
    /   \
   0     1
   |     |
   M     M
  / \   / \
 -/+ -/+ -/+ -/+
```

Each leaf outputs the majority class (here tie: either prediction is arbitrary). The tree has 2 internal nodes: L then M.

Step 4. To classify question 6 ($L=1,M=0,D=+$), the tree checks L (decision 1), then M (decision 2), then reaches a leaf. So **2** decisions are made.

$$\boxed{\text{2 decisions (check both L and M).}}$$

---

**15.** Find the least number of comparisons needed to sort four elements and devise an algorithm.

**Solution.**
Step 1. $l=4!=24$ possible orderings, binary comparisons ($m=2$). Decision tree height: $h\ge\lceil\log_2 24\rceil=\lceil4.585\rceil=5$. At least 5 comparisons are needed.

Step 2. Algorithm achieving exactly 5 comparisons (merge-insertion):
- Let elements be $a,b,c,d$.
1. Compare $a$ and $b$. WLOG $a<b$.
2. Compare $c$ and $d$. WLOG $c<d$. [2 comparisons]
3. Compare $b$ and $d$. WLOG $b<d$. Now $a<b<d$ and $c<d$. [3 comparisons]
4. Compare $c$ and $b$:
   - If $c>b$: $a<b<c<d$ (done, **4 comparisons** total).
   - If $c<b$: go to step 5.
5. Compare $c$ and $a$:
   - If $c<a$: $c<a<b<d$.
   - If $c>a$: $a<c<b<d$. [5 comparisons]

Worst case: 5 comparisons, matching the lower bound.

$$\boxed{5\text{ comparisons; algorithm as described above.}}$$

---

**16.** How many comparisons does the tournament sort use to find the second largest, third largest, ..., $(n-1)$st largest element?

**Solution.**
Step 1. Finding the **maximum** via tournament: $n-1$ comparisons (pairwise matches forming a binary tree of height $\lceil\log_2 n\rceil$).

Step 2. The elements that lost directly to the maximum are at most $\lceil\log_2 n\rceil$ opponents. The **second largest** must be among them; finding it takes $\lceil\log_2 n\rceil-1$ additional comparisons.

Step 3. To find the **$k$-th largest** (for $k\ge3$): after determining the $(k-1)$-st largest, replace it with $-\infty$ in the tournament tree and replay the matches along its path to the root. Each replay takes at most $\lceil\log_2 n\rceil$ comparisons.

Step 4. Therefore:
- Second largest: $\lceil\log_2 n\rceil-1$ additional comparisons (total $n-2+\lceil\log_2 n\rceil$).
- Each subsequent ($3$rd through $n$th): at most $\lceil\log_2 n\rceil$ additional comparisons each.

$$\boxed{\begin{aligned}
\text{2nd largest: }&\lceil\log_2 n\rceil-1\text{ additional}\\
\text{3rd through }n\text{th: }&\text{at most }\lceil\log_2 n\rceil\text{ additional each}
\end{aligned}}$$

---

**17.** Draw the tree whose Prüfer sequence is $(1,1,1,1,6,5)$.

**Solution.**
Step 1. $n=6+2=8$ vertices $\{1,\dots,8\}$. $P=(1,1,1,1,6,5)$. Initial $L=[8]\setminus P=\{2,3,4,7,8\}$.

| Step | smallest in $L$ | connect to (first of $P$) | update |
|------|-----------------|---------------------------|--------|
| 1 | 2 | 1 | remove 2; $P=(1,1,1,6,5)$; 1 still in $P$ |
| 2 | 3 | 1 | remove 3; $P=(1,1,6,5)$ |
| 3 | 4 | 1 | remove 4; $P=(1,6,5)$ |
| 4 | 7 | 1 | remove 7; $P=(6,5)$; 1 not in $P$ $\to$ add 1 to $L$; $L=\{8,1\}$ |
| 5 | 1 | 6 | remove 1; $P=(5)$; 6 not in $P$ $\to$ add 6 to $L$; $L=\{8,6\}$ |
| 6 | 6 | 5 | remove 6; $P=()$ empty; add 5 to $L$; $L=\{8,5\}$ |

Step 2. Connect final two in $L$: $(8,5)$.

Step 3. Edges: $\{2,1\},\{3,1\},\{4,1\},\{7,1\},\{1,6\},\{6,5\},\{8,5\}$.

Tree: vertex 1 is connected to 2,3,4,7,6; 6 to 5; 5 to 8.

```
     2   3   4   7
      \  |   |  /
         1
         |
         6
         |
         5
         |
         8
```

$$\boxed{\text{Edges: }\{2,1\},\{3,1\},\{4,1\},\{7,1\},\{1,6\},\{6,5\},\{8,5\}}$$

---

**18.** Draw the tree whose Prüfer sequence is $(10,9,8,7,6,5,4,3)$.

**Solution.**
Step 1. $n=8+2=10$ vertices. $P=(10,9,8,7,6,5,4,3)$. Initial $L=\{1,2\}$.

| Step | smallest in $L$ | connect to | update |
|------|-----------------|------------|--------|
| 1 | 1 | 10 | remove 1; $P=(9,8,7,6,5,4,3)$; 10 not in $P$ $\to$ add 10; $L=\{2,10\}$ |
| 2 | 2 | 9 | remove 2; $P=(8,7,6,5,4,3)$; add 9; $L=\{10,9\}$ |
| 3 | 9 | 8 | remove 9; $P=(7,6,5,4,3)$; add 8; $L=\{10,8\}$ |
| 4 | 8 | 7 | remove 8; $P=(6,5,4,3)$; add 7; $L=\{10,7\}$ |
| 5 | 7 | 6 | remove 7; $P=(5,4,3)$; add 6; $L=\{10,6\}$ |
| 6 | 6 | 5 | remove 6; $P=(4,3)$; add 5; $L=\{10,5\}$ |
| 7 | 5 | 4 | remove 5; $P=(3)$; add 4; $L=\{10,4\}$ |
| 8 | 4 | 3 | remove 4; $P=()$; add 3; $L=\{10,3\}$ |

Step 2. Connect $\{10,3\}$.

Step 3. Edges: $\{1,10\},\{2,9\},\{9,8\},\{8,7\},\{7,6\},\{6,5\},\{5,4\},\{4,3\},\{10,3\}$.
This is a path: $1-10-3-4-5-6-7-8-9-2$.

$$\boxed{\text{Path: }1-10-3-4-5-6-7-8-9-2}$$

---

**19.** Draw the tree whose Prüfer sequence is $(1,2,3,4,5,6,7,8)$.

**Solution.**
Step 1. $n=8+2=10$. $P=(1,2,3,4,5,6,7,8)$. Initial $L=\{9,10\}$.

| Step | smallest in $L$ | connect to | update |
|------|-----------------|------------|--------|
| 1 | 9 | 1 | remove 9; $P=(2,3,4,5,6,7,8)$; 1 not in $P$ $\to$ add 1; $L=\{10,1\}$ |
| 2 | 1 | 2 | remove 1; $P=(3,4,5,6,7,8)$; add 2; $L=\{10,2\}$ |
| 3 | 2 | 3 | remove 2; $P=(4,5,6,7,8)$; add 3; $L=\{10,3\}$ |
| 4 | 3 | 4 | remove 3; $P=(5,6,7,8)$; add 4; $L=\{10,4\}$ |
| 5 | 4 | 5 | remove 4; $P=(6,7,8)$; add 5; $L=\{10,5\}$ |
| 6 | 5 | 6 | remove 5; $P=(7,8)$; add 6; $L=\{10,6\}$ |
| 7 | 6 | 7 | remove 6; $P=(8)$; add 7; $L=\{10,7\}$ |
| 8 | 7 | 8 | remove 7; $P=()$; add 8; $L=\{10,8\}$ |

Step 2. Connect $\{10,8\}$.

Step 3. Edges: $\{9,1\},\{1,2\},\{2,3\},\{3,4\},\{4,5\},\{5,6\},\{6,7\},\{7,8\},\{10,8\}$.
This is the path: $9-1-2-3-4-5-6-7-8-10$.

$$\boxed{\text{Path: }9-1-2-3-4-5-6-7-8-10}$$

---

**20.** Determine the Prüfer codes for the two given labeled trees.

**Tree 1** (root 1 with children 9,5; 5 has children 2,3,8; 2 has child 6; 8 has child 4; 9 has child 7; 7 has child 10):

**Solution.**
Step 1. Vertices $\{1,\dots,10\}$. Edges: $\{1,9\},\{1,5\},\{5,2\},\{5,3\},\{5,8\},\{2,6\},\{8,4\},\{9,7\},\{7,10\}$.
Degrees: $d_1=2,d_2=2,d_3=1,d_4=1,d_5=4,d_6=1,d_7=2,d_8=2,d_9=2,d_{10}=1$.

Step 2. Leaves initially: $\{3,4,6,10\}$. Encode (10 vertices, 8 steps):

| Step | smallest leaf | neighbor (recorded) | remove leaf | update |
|------|---------------|---------------------|-------------|--------|
| 1 | 3 | **5** | remove 3 | $d_5$ becomes 3 |
| 2 | 4 | **8** | remove 4 | $d_8$ becomes 1 (now leaf) |
| 3 | 6 | **2** | remove 6 | $d_2$ becomes 1 (now leaf) |
| 4 | 2 | **5** | remove 2 | $d_5$ becomes 2 |
| 5 | 8 | **5** | remove 8 | $d_5$ becomes 1 (now leaf) |
| 6 | 5 | **1** | remove 5 | $d_1$ becomes 1 (now leaf) |
| 7 | 1 | **9** | remove 1 | $d_9$ becomes 1 (now leaf) |
| 8 | 9 | **7** | remove 9 | remaining: $\{7,10\}$ |

Prüfer code: $(5,8,2,5,5,1,9,7)$.

**Tree 2** (root 2 with children 3,8; 3 has children 4,7,9; 4 has child 1; 8 has children 6,10; 6 has child 5):

**Solution.**
Step 1. Edges: $\{2,3\},\{2,8\},\{3,4\},\{3,7\},\{3,9\},\{4,1\},\{8,6\},\{8,10\},\{6,5\}$.
Degrees: $d_1=1,d_2=2,d_3=4,d_4=2,d_5=1,d_6=2,d_7=1,d_8=3,d_9=1,d_{10}=1$.

Step 2. Leaves initially: $\{1,5,7,9,10\}$.

| Step | smallest leaf | neighbor | remove leaf | update |
|------|---------------|----------|-------------|--------|
| 1 | 1 | **4** | remove 1 | $d_4$ becomes 1 (leaf) |
| 2 | 4 | **3** | remove 4 | $d_3$ becomes 3 |
| 3 | 5 | **6** | remove 5 | $d_6$ becomes 1 (leaf) |
| 4 | 6 | **8** | remove 6 | $d_8$ becomes 2 |
| 5 | 7 | **3** | remove 7 | $d_3$ becomes 2 |
| 6 | 9 | **3** | remove 9 | $d_3$ becomes 1 (leaf) |
| 7 | 3 | **2** | remove 3 | $d_2$ becomes 1 (leaf) |
| 8 | 2 | **8** | remove 2 | remaining: $\{8,10\}$ |

Prüfer code: $(4,3,6,8,3,3,2,8)$.

$$\boxed{\text{Tree 1: }(5,8,2,5,5,1,9,7)\qquad\text{Tree 2: }(4,3,6,8,3,3,2,8)}$$

---

**21.** Determine which trees have Prüfer codes with distinct values in all positions. How many labeled trees with $n$ vertices have this property?

**Solution.**
Step 1. A Prüfer code of length $n-2$ has all entries distinct. Since vertex $i$ appears $d_i-1$ times, all-distinct entries means each appears at most once. So $d_i-1\le1$, i.e., $d_i\le2$ for all vertices.

Step 2. A tree with maximum degree at most 2 is a **path** $P_n$.

Step 3. How many labeled paths on $n$ vertices? Choose which 2 labels are the endpoints: $\binom{n}{2}$ ways. The remaining $n-2$ labels form the internal path in $(n-2)!$ orders. Total: $\binom{n}{2}(n-2)!=\frac{n!}{2!(n-2)!}\cdot(n-2)!=\frac{n!}{2}$.

Step 4. Verifying via Prüfer: choose which 2 labels do NOT appear in the code (the leaves/endpoints): $\binom{n}{2}$ ways. Arrange the remaining $n-2$ labels in the code: $(n-2)!$ ways. Same result.

$$\boxed{\text{Labeled paths }P_n;\quad\text{Number }=\binom{n}{2}(n-2)!=\frac{n!}{2}}$$

---

**22.** How many labeled trees with 6 vertices have given degree sequences?

**Solution.** Formula: $\displaystyle\frac{(n-2)!}{\prod_{i=1}^{n}(d_i-1)!}$, provided $\sum d_i=2(n-1)$.

For $n=6$, $(n-2)!=4!=24$, and $\sum d_i=10$.

**(a)** $(5,1,1,1,1,1)$:
Sum $=5+5=10$. ✓
Denominator $=(5-1)!(1-1)!^5=4!\cdot1=24$.
Count $=24/24=1$.

$$\boxed{1}$$

**(b)** $(4,2,1,1,1,1)$:
Sum $=4+2+4=10$. ✓
For a specific label assignment: denominator $=(4-1)!(2-1)!(1-1)!^4=3!\cdot1!\cdot1=6$.
Count per assignment $=24/6=4$.
Number of label-to-degree assignments: choose label for degree 4 ($6$ ways), then degree 2 ($5$ ways): $6\times5=30$.
Total $=30\times4=120$.

$$\boxed{120}$$

**(c)** $(3,2,2,1,1,1)$:
Sum $=3+2+2+3=10$. ✓
Per assignment: denominator $=(3-1)!(2-1)!^2(1-1)!^3=2!\cdot1\cdot1\cdot1=2$.
Count per assignment $=24/2=12$.
Assignments: choose label for degree 3 ($6$ ways), choose which 2 labels get degree 2 from remaining 5: $\binom{5}{2}=10$. Total $=6\times10=60$.
Total $=60\times12=720$.

$$\boxed{720}$$

**(d)** $(2,2,2,2,1,1)$:
Sum $=4\times2+2=10$. ✓
Per assignment: denominator $=(2-1)!^4(1-1)!^2=1^4\cdot1^2=1$.
Count per assignment $=24$.
Assignments: choose which 2 vertices are leaves (degree 1): $\binom{6}{2}=15$.
Total $=15\times24=360$.

$$\boxed{360}$$

---

**23.** How many labeled trees with $n$ vertices are there such that the degree of the node labeled $n$ is equal to $k$?

**Solution.**
Step 1. In the Prüfer code of length $n-2$, vertex $n$ appears exactly $d_n-1=k-1$ times.
Step 2. Choose which $k-1$ positions in the sequence contain $n$: $\binom{n-2}{k-1}$ ways.
Step 3. The remaining $(n-2)-(k-1)=n-k-1$ positions are filled with any labels from $\{1,2,\dots,n-1\}$: $(n-1)^{\,n-k-1}$ ways.
Step 4. By the Product Rule:
$$\binom{n-2}{k-1}(n-1)^{\,n-k-1}$$
This is valid for $1\le k\le n-1$. For $k=0$ or $k\ge n$, the count is 0.

$$\boxed{\binom{n-2}{k-1}(n-1)^{\,n-k-1}}$$

---

**24.** How many labeled rooted trees on $n$ vertices are there? Propose a generation method.

**Solution.**
Step 1. Labeled trees: $n^{n-2}$ (Cayley). For each, choose a root: $n$ choices. Total: $n\cdot n^{n-2}=n^{n-1}$.

Step 2. **Uniform generation method:**
1. Generate a random Prüfer sequence: $n-2$ independent uniform random integers from $[n]$.
2. Decode to obtain a labeled tree $T$ (uniform by Cayley + Prüfer bijection).
3. Choose a root uniformly from $\{1,\dots,n\}$ (independent of $T$).
4. Output the rooted tree $(T,\text{root})$.

Each rooted labeled tree has probability $1/(n^{n-1})$.

$$\boxed{n^{\,n-1}\text{ rooted labeled trees; Prüfer + uniform root choice.}}$$

---

**25.** How many labeled rooted forests on $n$ vertices with exactly $k$ components are there?

**Solution.**
Step 1. Add a "super-root" vertex $0$ and connect it to one vertex in each component. This creates a rooted tree on $n+1$ vertices (labels $0,1,\dots,n$) with root $0$, where $0$ has exactly $k$ children (the roots of the $k$ forest components).

Step 2. Using Problem 23 with $n$ replaced by $n+1$, vertex $0$ as the special vertex with degree $k$: the count is $\binom{(n+1)-2}{k-1}((n+1)-1)^{(n+1)-k-1}=\binom{n-1}{k-1}n^{\,n-k}$.

Step 3. Verify: for $k=1$ (single rooted tree), $\binom{n-1}{0}n^{\,n-1}=n^{\,n-1}$, matching Problem 24.

$$\boxed{\binom{n-1}{k-1}n^{\,n-k}}$$

---

**26.** Find a spanning tree for each of these graphs: $K_5$, $C_5$, $K_{1,6}$, $K_{2,3}$, $Q_3$.

**Solution.**
Step 1. **$K_5$** (complete graph on 5 vertices): any tree on 5 vertices with 4 edges. Take the path $1-2-3-4-5$.

Step 2. **$C_5$** (5-cycle): remove any single edge, e.g., $\{1,5\}$, leaving the path $1-2-3-4-5$.

Step 3. **$K_{1,6}$** (star with 6 leaves): it is already a tree. It is its own unique spanning tree.

Step 4. **$K_{2,3}$** (parts $A=\{a_1,a_2\}$, $B=\{b_1,b_2,b_3\}$): need 4 edges. Take a star at $a_1$ connecting to all three $b_i$, plus edge $\{b_1,a_2\}$ (or $\{a_1,a_2\}$). Edges: $\{a_1,b_1\},\{a_1,b_2\},\{a_1,b_3\},\{b_1,a_2\}$.

Step 5. **$Q_3$** (3-cube, 8 vertices, 12 edges). Run BFS from $000$:
- $000-001$, $000-010$, $000-100$
- $001-011$, $001-101$
- $010-110$
- $011-111$

Spanning tree edges (7 edges): $\{000,001\},\{000,010\},\{000,100\},\{001,011\},\{001,101\},\{010,110\},\{011,111\}$.

$$\boxed{\begin{aligned}
K_5&:\text{ path }1-2-3-4-5\\
C_5&:\text{ path of 5 vertices (remove any edge)}\\
K_{1,6}&:\text{ itself (it is a tree)}\\
K_{2,3}&:\text{ star at }a_1\text{ plus }\{b_1,a_2\}\\
 Q_3&:\text{ BFS tree as above}
\end{aligned}}$$

---

**27.** Draw all spanning trees of $C_5$, determine how many. Find its Laplacian and reduced Laplacian. Verify with Matrix-Tree Theorem. How many spanning trees does $C_n$ have?

**Solution.**
Step 1. $C_5$ is a 5-cycle (5 vertices, 5 edges). A spanning tree has 4 edges, so we remove exactly one edge. There are $\binom{5}{1}=5$ spanning trees (distinct as subgraphs, though all isomorphic to $P_5$).

Step 2. **All 5 spanning trees** (label vertices $1,2,3,4,5$ cyclically):
- Remove $\{1,5\}$: edges $\{1,2\},\{2,3\},\{3,4\},\{4,5\}$
- Remove $\{1,2\}$: edges $\{2,3\},\{3,4\},\{4,5\},\{5,1\}$
- Remove $\{2,3\}$: edges $\{1,2\},\{3,4\},\{4,5\},\{5,1\}$
- Remove $\{3,4\}$: edges $\{1,2\},\{2,3\},\{4,5\},\{5,1\}$
- Remove $\{4,5\}$: edges $\{1,2\},\{2,3\},\{3,4\},\{5,1\}$

Step 3. **Laplacian** $L=D-A$ (each vertex degree 2, adjacent to two cyclic neighbors):

$$L=\begin{pmatrix}
2 & -1 &  0 &  0 & -1\\
-1 &  2 & -1 &  0 &  0\\
0 & -1 &  2 & -1 &  0\\
0 &  0 & -1 &  2 & -1\\
-1 &  0 &  0 & -1 &  2
\end{pmatrix}$$

Step 4. Delete row 5, column 5 to get the $4\times4$ reduced Laplacian:

$$\tilde L=\begin{pmatrix}
2 & -1 &  0 &  0\\
-1 &  2 & -1 &  0\\
0 & -1 &  2 & -1\\
0 &  0 & -1 &  2
\end{pmatrix}$$

Step 5. Compute $\det\tilde L$ by cofactor expansion along row 1:

$\det\tilde L = 2\cdot\begin{vmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{vmatrix} - (-1)\cdot\begin{vmatrix}-1&-1&0\\0&2&-1\\0&-1&2\end{vmatrix}$

First $3\times3$: $2(4-1) + 1(-2-0) = 2\cdot3 -2 = 4$.

Second $3\times3$: $(-1)(4-1) - (-1)(0) + 0 = -3$.

$\det\tilde L = 2\cdot4 + 1\cdot(-3) = 8-3 = 5$.

Step 6. Matrix-Tree: $\kappa(C_5)=\det\tilde L=5$, matching the direct enumeration.

Step 7. **General $C_n$:** removing any one of $n$ edges yields a distinct spanning tree. So $\kappa(C_n)=n$. (The reduced Laplacian of $C_n$ is an $(n-1)\times(n-1)$ tridiagonal Toeplitz matrix with determinant $n$.)

$$\boxed{\kappa(C_5)=5,\qquad\kappa(C_n)=n}$$

---

**28.** How many trees are there in the spanning forest of a graph?

**Solution.**
Step 1. A spanning forest of $G$ contains a spanning tree within each connected component. The number of trees equals the number of connected components $c$.

$$\boxed{c\text{ (the number of connected components)}}$$

---

**29.** How many edges must be removed to produce the spanning forest of a graph with $n$ vertices, $m$ edges, and $c$ connected components?

**Solution.**
Step 1. A spanning forest has exactly $n-c$ edges (each component's spanning tree has $n_i-1$ edges; sum $=n-c$).
Step 2. Starting with $m$ edges, remove $m-(n-c)$ edges to reach $n-c$.

$$\boxed{m-(n-c)}$$

---

**30.** How many different spanning trees does each graph have?

**(a)** $K_{2,2}$: Formula $\kappa(K_{m,n})=m^{n-1}n^{m-1}=2^{1}\cdot2^{1}=4$.

$$\boxed{4}$$

**(b)** $C_n$: Removing any one of $n$ edges gives a spanning tree. $\kappa(C_n)=n$.

$$\boxed{n}$$

**(c)** $K_{1,n}$: It is itself a tree (star). Formula: $1^{n-1}\cdot n^{0}=1$.

$$\boxed{1}$$

**(d)** $K_{m,n}$: Known formula: $\kappa(K_{m,n})=m^{n-1}n^{m-1}$.

$$\boxed{m^{\,n-1}n^{\,m-1}}$$

**(e)** $Q_3$: The 3-cube has $v=8,e=12$. Known result (Matrix-Tree computation yields) $\kappa(Q_3)=384$. More generally, $\kappa(Q_n)=2^{2^n-n-1}\prod_{k=1}^{n}k^{\binom{n}{k}}$. For $n=3$: $2^{8-3-1}\cdot1^{3}\cdot2^{3}\cdot3^{1}=2^{4}\cdot8\cdot3=16\cdot24=384$.

$$\boxed{384}$$

**(f)** $W_n$ (wheel, $n\ge3$ rim vertices plus hub, total $n+1$ vertices): Known result $\kappa(W_n)=L_{2n}-2$, where $L_k$ is the $k$-th Lucas number ($L_1=1,L_2=3,L_{k}=L_{k-1}+L_{k-2}$). Equivalently,
$$\kappa(W_n)=\left(\frac{3+\sqrt5}{2}\right)^n+\left(\frac{3-\sqrt5}{2}\right)^n-2$$
Examples: $\kappa(W_3)=L_6-2=18-2=16$; $\kappa(W_4)=L_8-2=47-2=45$; $\kappa(W_5)=L_{10}-2=123-2=121$.

$$\boxed{\kappa(W_n)=L_{2n}-2}$$

---

**31.** Which connected simple graphs have exactly one spanning tree?

**Solution.**
Step 1. If $G$ is a tree, it is its own spanning tree and the unique one (any spanning tree must have the same edges since adding/removing any edge would disconnect or create a cycle).
Step 2. If $G$ has a cycle, removing different edges of that cycle yields at least two distinct spanning trees.
Step 3. Thus exactly one spanning tree iff $G$ itself is a tree.

$$\boxed{G\text{ is a tree itself.}}$$

---

**32.** When must an edge of a connected simple graph be in every spanning tree?

**Solution.**
Step 1. An edge whose removal disconnects the graph is called a **bridge** (cut-edge).
Step 2. Every spanning tree must be connected, so it must include every bridge.
Step 3. Conversely, if an edge lies on some cycle, there exists a spanning tree excluding it (remove that edge from the cycle, keep the rest of the cycle intact).
Step 4. Thus an edge is in every spanning tree iff it is a bridge.

$$\boxed{\text{The edge must be a bridge (cut-edge).}}$$

---

**33.** Prove that if $G$ is a connected, simple graph with $n$ vertices and $G$ does not contain a simple path of length $k$, then it contains at most $(k-1)n$ edges.

**Solution.**
Step 1. Let $P$ be a longest simple path in $G$, with vertices $v_1,v_2,\dots,v_{\ell}$ and $\ell\le k$ (since no path of length $k$ exists, path has at most $k$ vertices).

Step 2. Consider the endpoint $v_1$. All neighbors of $v_1$ must lie on $P$; otherwise $P$ could be extended, contradicting maximality. Since $v_1$ has at least one neighbor ($v_2$), its degree satisfies $\deg(v_1)\le\ell-1\le k-1$.

Step 3. Remove $v_1$ from $G$. In the remaining graph $G'=G-v_1$, there is still no path of length $k$ ($G'$ is a subgraph of $G$). The number of vertices decreases by 1.

Step 4. Repeating this argument $n$ times (each time removing an endpoint of a longest path), we remove at most $k-1$ edges per vertex deletion. Total edges removed $=m\le(k-1)n$.

Step 5. Formal induction: Base case $n=1$ trivial. Inductive step: remove an endpoint of a longest path (degree $\le k-1$), apply induction to the remaining $n-1$ vertex graph. Summing gives $m\le(k-1)n$.

$$\boxed{m\le(k-1)n\quad\text{(proved by repeated endpoint deletion).}}$$

---

**34.** Use the Matrix-Tree Theorem on $K_n$ to reprove Cayley's Theorem ($\kappa(K_n)=n^{n-2}$).

**Solution.**
Step 1. Laplacian of $K_n$: diagonal entries $n-1$, off-diagonal entries $-1$.
$$L=(n-1)I_n - J_n + I_n = nI_n - J_n$$
where $J_n$ is the $n\times n$ all-ones matrix.

Step 2. Delete row $n$, column $n$ to get the $(n-1)\times(n-1)$ reduced Laplacian:
$$\tilde L = nI_{n-1} - J_{n-1}$$

Step 3. Fact: for an $m\times m$ matrix $aI_m+bJ_m$, its determinant is $a^{m-1}(a+mb)$. Here $m=n-1$, $a=n$, $b=-1$.

Step 4. $\det\tilde L = n^{(n-1)-1}(n+(n-1)(-1)) = n^{n-2}(n-(n-1)) = n^{n-2}\cdot1 = n^{n-2}$.

Step 5. By the Matrix-Tree Theorem, $\kappa(K_n)=\det\tilde L=n^{n-2}$, which is Cayley's Theorem.

$$\boxed{\kappa(K_n)=n^{n-2}\text{, reproving Cayley's Theorem.}}$$

---

**35.** Prove $\kappa(G)=\kappa_1\kappa_2\cdots\kappa_k$ using the Matrix-Tree Theorem.

**Solution.**
Step 1. Let $v$ be a cut vertex of $G$, whose removal disconnects $G$ into components $G_1,\dots,G_k$. Let $H_i=G\setminus\bigcup_{j\neq i}G_j$ (the subgraph induced by $G_i\cup\{v\}$). Its complexity is $\kappa_i=\kappa(H_i)$.

Step 2. Order the vertices so that $v$ is the last vertex, vertices of $G_1$ come first, then $G_2$, etc. In the Laplacian $L$, there are no edges between distinct $G_i$ and $G_j$ ($i\neq j$), so the off-diagonal blocks connecting them are zero.

Step 3. Delete the row and column of $v$ to obtain the reduced Laplacian $\tilde L_G$. Because there are no edges between different $G_i$ blocks, the matrix $\tilde L_G$ is block-diagonal, with diagonal blocks $\tilde L_{H_i}$ (the reduced Laplacians of $H_i$ with $v$'s row/column deleted).

Step 4. The determinant of a block-diagonal matrix is the product of the determinants of its blocks:
$$\det\tilde L_G = \prod_{i=1}^{k}\det\tilde L_{H_i}$$

Step 5. By the Matrix-Tree Theorem, $\kappa(G)=\det\tilde L_G$ and $\kappa_i=\kappa(H_i)=\det\tilde L_{H_i}$. Hence $\kappa(G)=\kappa_1\kappa_2\cdots\kappa_k$.

$$\boxed{\kappa(G)=\kappa_1\kappa_2\cdots\kappa_k}$$

---

**36.** Rosen 11.5: Exercises 1, 8.

**Solution (Exercise 1):** "How many edges must be removed from a connected graph with $n$ vertices and $m$ edges to produce a spanning tree?"

Step 1. A spanning tree has exactly $n-1$ edges. Starting with $m$ edges, we must remove $m-(n-1)$ edges.

$$\boxed{m-(n-1)}$$

**Solution (Exercise 8):** "How many nonisomorphic spanning trees does each of these simple graphs have?"

Step 1. Since the exact figures from Rosen's textbook are not reproduced here, the general methodology is:
- For each graph, enumerate all spanning trees by systematically removing edges from cycles (or using the Matrix-Tree Theorem for the count).
- Group the resulting trees by isomorphism (as unlabeled trees).
- Count the number of distinct isomorphism classes.

Step 2. For common special cases:
- $C_n$: all spanning trees are $P_n$, so 1 nonisomorphic spanning tree.
- $K_n$: number of nonisomorphic unlabeled trees on $n$ vertices (e.g., for $n=4$: 2 trees $P_4$ and $K_{1,3}$).
- For specific small graphs: enumerate by edge-removal and check isomorphism through degree-sequence comparison.

$$\boxed{\text{Methodology: enumerate edge-removals from cycles; group by isomorphism.}}$$

---

**37.** Devise an algorithm for constructing a maximum spanning tree of a connected weighted graph.

**Solution.**
Step 1. A **maximum spanning tree** maximizes the sum of edge weights. This is equivalent to finding an MST on the graph with negated weights (or sorting edges descending).

Step 2. **Algorithm (Reverse Kruskal):**
1. Sort all edges in **descending** order by weight.
2. Initialize each vertex as its own component (union-find data structure).
3. Iterate through sorted edges: for edge $\{u,v\}$ with weight $w$, if $u$ and $v$ are in different components, add the edge to the tree and union the components.
4. Stop when $n-1$ edges have been added.

Step 3. Equivalently, run Prim's algorithm but always pick the **maximum-weight** edge crossing the cut (use a max-heap instead of min-heap).

Step 4. Correctness follows from the cut property: the heaviest edge crossing any cut belongs to some maximum spanning tree (by symmetry, negate weights and apply the standard MST cut property).

$$\boxed{\text{Reverse Kruskal (sort descending) or max-heap Prim.}}$$

---

**38.** Show that there is a unique minimum spanning tree in a connected weighted graph if the weights of the edges are all different.

**Solution.**
Step 1. Suppose for contradiction that $T_1$ and $T_2$ are two distinct MSTs.

Step 2. Let $e$ be the edge of **minimum weight** in the symmetric difference $T_1\triangle T_2=(T_1\setminus T_2)\cup(T_2\setminus T_1)$. WLOG, $e\in T_1\setminus T_2$.

Step 3. Adding $e$ to $T_2$ creates a unique cycle $C$. Since $T_1$ is acyclic, not all edges of $C$ can be in $T_1$. Choose $f\in C$ with $f\in T_2\setminus T_1$.

Step 4. Form $T'=T_2\setminus\{f\}\cup\{e\}$. This is a spanning tree. Its weight: $w(T')=w(T_2)-w(f)+w(e)$.

Step 5. Since $e$ is the **minimum-weight** edge in $T_1\triangle T_2$ and $f\in T_1\triangle T_2$ with $f\neq e$, we have $w(e)<w(f)$ (all weights distinct, and $e$ is uniquely minimum in the symmetric difference).

Step 6. Thus $w(T')<w(T_2)$, contradicting that $T_2$ is an MST. Hence no two distinct MSTs exist — the MST is unique.

$$\boxed{\text{Unique MST follows from the cut property with distinct weights.}}$$

---

**39.** Devise an algorithm for finding the second minimum spanning tree in a connected weighted graph.

**Solution.**
Step 1. Find an MST $T$ (using Kruskal's or Prim's).

Step 2. For each non-tree edge $e=uv\notin T$ (with weight $w(e)$):
- Add $e$ to $T$, creating a unique cycle $C_e$.
- Find the **maximum-weight** tree edge $f$ on $C_e$ (the heaviest edge of $T$ on the cycle).
- The candidate spanning tree is $T_e=T\setminus\{f\}\cup\{e\}$ with weight $w(T)-w(f)+w(e)$.

Step 3. Among all candidates $T_e$, take the one with **minimum weight**. This is the second minimum spanning tree (it may have the same weight as the MST if there were ties; if the MST is unique by Problem 38, the second MST is strictly heavier).

Step 4. **Complexity:** Naively $O(mn)$ (traverse the cycle for each of $m-n+1$ non-tree edges). Can be optimized to $O(m\log n)$ using binary lifting / LCA to find max-weight edges on tree paths.

$$\boxed{\begin{aligned}&\text{1. Find MST }T.\\
&\text{2. For each }e\notin T\text{: add }e,\text{ remove max-weight edge on created cycle.}\\
&\text{3. Take the minimum-weight candidate.}\end{aligned}}$$

---

**40.** Suppose all edge weights are integers in $[1,|V|]$. How fast can Kruskal's run? What if weights are in $[1,k]$ for constant $k$?

**Solution.**
Step 1. Kruskal's algorithm: sort edges + union-find operations. The sorting step dominates in standard implementations: $O(|E|\log|E|)$ with comparison sort.

Step 2. **Case $[1,|V|]$:** Since weights are small integers in a range proportional to $|V|$, we can sort using **counting sort** (or bucket sort) in $O(|E|+|V|)$ time. The union-find operations take $O(|E|\,\alpha(|V|))$. Total: $O(|E|+|V|)=O(|E|)$ (for connected graphs, $|E|\ge|V|-1$).

Step 3. **Case $[1,k]$ for constant $k$:** Counting sort takes $O(|E|+k)=O(|E|)$ time (since $k$ is constant). Total: $O(|E|\,\alpha(|V|))$, which is near-linear.

$$\boxed{\begin{aligned}
[1,|V|]&:\ O(|E|+|V|)\\
[1,k]\text{ (constant)}&:\ O(|E|\,\alpha(|V|))
\end{aligned}}$$

---

**41.** Represent $((x+2)^3)(y-(3+x))-5$ using a binary tree. Write in prefix, postfix, infix.

**Solution.**
Step 1. Parse by operator precedence. The last evaluated operator is the outer subtraction $-5$, so the root is $-$.
- Left subtree: product $((x+2)^3)\times(y-(3+x))$. Root $\times$.
  - Left of $\times$: $(x+2)^3$. Root exponentiation $\uparrow$.
    - Left of $\uparrow$: $x+2$. Root $+$, children $x$ and $2$.
    - Right of $\uparrow$: $3$.
  - Right of $\times$: $y-(3+x)$. Root $-$.
    - Left: $y$.
    - Right: $3+x$. Root $+$, children $3$ and $x$.
- Right subtree: $5$.

Step 2. Expression tree:

```
         -
       /   \
      x     5
    /   \
   ^     -
  / \   / \
 +   3 y   +
/ \       / \
x  2     3   x
```

Step 3. **Traversals:**
**(a) Prefix (pre-order: root, left, right):**
$- \times \uparrow + x 2 3 - y + 3 x 5$

**(b) Postfix (post-order: left, right, root):**
$x 2 + 3 \uparrow y 3 x + - \times 5 -$

**(c) Infix (in-order, fully parenthesized):**
$((((x+2)\uparrow3)\times(y-(3+x)))-5)$

$$\boxed{\begin{aligned}
\text{Prefix: }&-\times\uparrow + x 2 3 - y + 3 x 5\\
\text{Postfix: }&x 2 + 3 \uparrow y 3 x + - \times 5 -\\
\text{Infix: }&(((x+2)\uparrow3)\times(y-(3+x)))-5
\end{aligned}}$$

---

**42.** Represent the compound propositions using ordered rooted trees; give prefix, postfix, infix.

**(i)** $\lnot(p\land q)\leftrightarrow(\lnot p\lor\lnot q)$

**Solution.**
Step 1. Last operator: $\leftrightarrow$. Left subtree: $\lnot(p\land q)$. Right subtree: $(\lnot p\lor\lnot q)$.
- $\lnot(p\land q)$: root $\lnot$, child $\land(p,q)$.
- $(\lnot p\lor\lnot q)$: root $\lor$, children $\lnot p$ and $\lnot q$.

**(a) Prefix:** $\leftrightarrow \lnot \land p q \lor \lnot p \lnot q$

**(b) Postfix:** $p q \land \lnot p \lnot q \lnot \lor \leftrightarrow$

**(c) Infix:** $(\lnot(p\land q))\leftrightarrow((\lnot p)\lor(\lnot q))$

---

**(ii)** $(\lnot p\land(q\leftrightarrow\lnot p))\lor\lnot q$

**Solution.**
Step 1. Last operator: $\lor$. Left: $\lnot p\land(q\leftrightarrow\lnot p)$. Right: $\lnot q$.
- Left subtree: root $\land$, children $\lnot p$ and $(q\leftrightarrow\lnot p)$.
  - $(q\leftrightarrow\lnot p)$: root $\leftrightarrow$, children $q$ and $\lnot p$.

**(a) Prefix:** $\lor \land \lnot p \leftrightarrow q \lnot p \lnot q$

**(b) Postfix:** $p \lnot q p \lnot \leftrightarrow \land q \lnot \lor$

**(c) Infix:** $((\lnot p)\land(q\leftrightarrow(\lnot p)))\lor(\lnot q)$

$$\boxed{\begin{aligned}
\text{(i) Prefix: }&\leftrightarrow\lnot\land p q\lor\lnot p\lnot q\\
\text{Postfix: }&p q\land\lnot p\lnot q\lnot\lor\leftrightarrow\\
\text{Infix: }&(\lnot(p\land q))\leftrightarrow((\lnot p)\lor(\lnot q))\\[6pt]
\text{(ii) Prefix: }&\lor\land\lnot p\leftrightarrow q\lnot p\lnot q\\
\text{Postfix: }&p\lnot q p\lnot\leftrightarrow\land q\lnot\lor\\
\text{Infix: }&((\lnot p)\land(q\leftrightarrow(\lnot p)))\lor(\lnot q)
\end{aligned}}$$

---

**43.** Evaluate the prefix expressions. (Scan right to left with a stack.)

**(a)** $- * 2 / 8 4 3$

**Solution.**
- Push 3: $[3]$
- Push 4: $[3,4]$
- Push 8: $[3,4,8]$
- $/$: pop 8,4 $\to 8/4=2$, push: $[3,2]$
- Push 2: $[3,2,2]$
- $*$: pop 2,2 $\to 4$, push: $[3,4]$
- $-$: pop 3,4 $\to 3-4=-1$, push: $[-1]$

$$\boxed{-1}$$

**(b)** $\uparrow - * 3 3 * 4 2 5$

**Solution.** ($\uparrow$ = exponentiation)
- Push 5: $[5]$
- Push 2: $[5,2]$
- Push 4: $[5,2,4]$
- $*$: $2*4=8$, push: $[5,8]$
- Push 3: $[5,8,3]$
- Push 3: $[5,8,3,3]$
- $*$: $3*3=9$, push: $[5,8,9]$
- $-$: $8-9=-1$, push: $[5,-1]$
- $\uparrow$: $(-1)^5=-1$, push: $[-1]$

$$\boxed{-1}$$

**(c)** $+ - \uparrow 3 2 \uparrow 2 3 / 6 - 4 2$

**Solution.**
- Push 2: $[2]$
- Push 4: $[2,4]$
- $-$: $4-2=2$, push: $[2,2]$
- Push 6: $[2,2,6]$
- $/$: $2/6=\frac13$, push: $[2,\frac13]$
- Push 3: $[2,\frac13,3]$
- Push 2: $[2,\frac13,3,2]$
- $\uparrow$: $2^3=8$, push: $[2,\frac13,8]$
- Push 2: $[2,\frac13,8,2]$
- Push 3: $[2,\frac13,8,2,3]$
- $\uparrow$: $3^2=9$, push: $[2,\frac13,8,9]$
- $-$: $8-9=-1$, push: $[2,\frac13,-1]$
- $+$: $\frac13+(-1)=-\frac23$, push: $[2,-\frac23]$

$$\boxed{-\frac{2}{3}}$$

---

**44.** Evaluate the postfix expressions. (Scan left to right with a stack.)

**(a)** $5 2 1 - - 3 1 4 + + *$

**Solution.**
- Push 5,2,1: $[5,2,1]$
- $-$: pop 2,1 $\to 2-1=1$, push: $[5,1]$
- $-$: pop 5,1 $\to 5-1=4$, push: $[4]$
- Push 3,1,4: $[4,3,1,4]$
- $+$: pop 1,4 $\to 1+4=5$, push: $[4,3,5]$
- $+$: pop 3,5 $\to 3+5=8$, push: $[4,8]$
- $*$: pop 4,8 $\to 4\times8=32$, push: $[32]$

$$\boxed{32}$$

**(b)** $9 3 / 5 + 7 2 - *$

**Solution.**
- Push 9,3: $[9,3]$
- $/$: $9/3=3$, push: $[3]$
- Push 5: $[3,5]$
- $+$: $3+5=8$, push: $[8]$
- Push 7,2: $[8,7,2]$
- $-$: $7-2=5$, push: $[8,5]$
- $*$: $8\times5=40$, push: $[40]$

$$\boxed{40}$$

**(c)** $3 2 * 2 \uparrow 5 3 - 8 4 / * -$

**Solution.**
- Push 3,2: $[3,2]$
- $*$: $3\times2=6$, push: $[6]$
- Push 2: $[6,2]$
- $\uparrow$: $6^2=36$, push: $[36]$
- Push 5,3: $[36,5,3]$
- $-$: $5-3=2$, push: $[36,2]$
- Push 8,4: $[36,2,8,4]$
- $/$: $8/4=2$, push: $[36,2,2]$
- $*$: $2\times2=4$, push: $[36,4]$
- $-$: $36-4=32$, push: $[32]$

$$\boxed{32}$$

---

**45.** Which of these are well-formed formulas over symbols $\{x,y,z\}$ and binary operators $\{\times,+,\circ\}$?

**Solution.**
Recall: A well-formed formula (wff) in prefix notation satisfies:
(i) A single symbol is a wff.
(ii) If $X,Y$ are wffs and $*$ is an operator, then $*XY$ is a wff.

**(a)** $\times + + x y x$

Step 1. Parse: $\times$ expects two arguments. First argument parses as: $+$ expects two. Next $+$ expects two: $x$ (wff), $y$ (wff) $\to$ $+xy$ is wff. Then the first $+$ has arguments $+xy$ (wff) and $x$ (wff) $\to$ $++xyx$ is wff. Now $\times$ has only one argument — needs a second argument. **Not well-formed.**

**(b)** $\circ x y \times x z$

Step 1. $\circ x y$ is a wff. Then $\times x z$ is a separate wff. But a well-formed formula must be a single connected expression; this is two wffs concatenated without a unifying operator. **Not well-formed.**

**(c)** $\times \circ x z \times \times x y$

Step 1. $\times$ expects two arguments. First: $\circ x z$ (wff). Second: $\times \times x y$. Parse the second: $\times$ expects two args. First: $\times$ (operator, not a wff!) expects two args. Its first arg is $x$ (wff), expects second — only $y$ follows. So $\times x y$ is a wff. Then $\times \times x y$ has the first $\times$ with first argument $\times x y$ (wff) but needs a second argument — none left. **Not well-formed.**

**(d)** $\times + \circ x x \circ x x x$

Step 1. $\times$ expects two arguments.
- First: $+$ expects two. First: $\circ x x$ (wff). Second: $\circ x x$ (wff). So $+\circ x x\circ x x$ is a wff.
- Second: $x$ (symbol, wff).
So $\times(+\circ x x\circ x x)x$ uses all symbols as a single wff. **Well-formed.**

$$\boxed{\begin{aligned}
\text{(a) }&\text{Not well-formed}\\
\text{(b) }&\text{Not well-formed}\\
\text{(c) }&\text{Not well-formed}\\
\text{(d) }&\text{Well-formed}
\end{aligned}}$$

---

**46.** Show that any well-formed formula in prefix notation over a set of symbols and binary operators contains exactly one more symbol than the number of operators.

**Solution.**
Step 1. Proof by **structural induction** on the definition of wff.

Step 2. **Base case:** If $F$ is a single symbol $x$, it has $1$ symbol and $0$ operators. Then $1=0+1$. $\checkmark$

Step 3. **Inductive step:** Assume $X$ and $Y$ are wffs with $s_X$ symbols, $o_X$ operators, and $s_Y$ symbols, $o_Y$ operators. By induction hypothesis: $s_X=o_X+1$ and $s_Y=o_Y+1$.

Step 4. Form $F=*XY$ where $*$ is a binary operator. Then:
- Number of symbols in $F$: $s_F=s_X+s_Y$.
- Number of operators in $F$: $o_F=1+o_X+o_Y$.

Step 5. Compute:
$$s_F = s_X+s_Y = (o_X+1)+(o_Y+1) = (o_X+o_Y+1)+1 = o_F+1$$

Thus $s_F=o_F+1$ holds for $F$.

Step 6. By induction, every wff in prefix notation over symbols and binary operators has exactly one more symbol than operators.

$$\boxed{\text{Proved by structural induction.}}$$

---

**47.** Explain how to use breadth-first search to find the length of a shortest path between two vertices in an undirected graph.

**Solution.**
Step 1. Run BFS starting from the source vertex $s$. Maintain an array $\operatorname{dist}[]$ where $\operatorname{dist}[v]$ stores the distance (number of edges) from $s$ to $v$. Initialize $\operatorname{dist}[s]=0$ and all others to $\infty$.

Step 2. In BFS, when a vertex $u$ is dequeued, for each unvisited neighbor $v$, set $\operatorname{dist}[v]=\operatorname{dist}[u]+1$ and enqueue $v$. BFS visits vertices in order of increasing distance from $s$, guaranteeing that when $v$ is first discovered, $\operatorname{dist}[v]$ is the shortest path length.

Step 3. When the target vertex $t$ is dequeued (or first discovered), $\operatorname{dist}[t]$ is the length of the shortest path from $s$ to $t$. If $t$ is never reached, the graph is disconnected and there is no path.

Step 4. **Why BFS works for unweighted graphs:** BFS explores vertices level by level. All vertices at distance $k$ are discovered before any vertex at distance $k+1$. Thus the first time $t$ is reached, the path length is minimal.

$$\boxed{\text{BFS from source: } \operatorname{dist}[t] \text{ on first discovery is the shortest path length.}}$$

---

**48.** Devise an algorithm based on BFS/DFS that determines whether a graph has a cycle, and if so, finds one.

**Solution.**
Step 1. **DFS-based cycle detection:**
- Maintain a `visited[]` array (boolean) and a `parent[]` array.
- Perform DFS from an arbitrary unvisited vertex.

Step 2. During DFS, when exploring an edge $(u,v)$:
- If $v$ is **not visited**: set `parent[v]=u`, recurse on $v$.
- If $v$ is **already visited** and $v\neq$ `parent[u]`: a cycle has been found! The cycle consists of the tree path from $v$ up to $u$ (via parent pointers) plus the edge $(u,v)$.

Step 3. To extract the cycle: walk from $u$ back to $v$ using `parent[]` pointers, collecting vertices, then append $u$ to close the cycle.

Step 4. **BFS-based cycle detection:**
Similar: during BFS, if a neighbor $v$ has already been discovered (visited) and $v$ is not the parent of $u$, a cycle exists. The cycle can be reconstructed using parent pointers from both directions to their lowest common ancestor.

Step 5. If the traversal completes without finding any such edge, the graph is acyclic (a forest).

$$\boxed{\text{DFS/BFS with parent tracking: back edge to non-parent } \Rightarrow \text{ cycle.}}$$

---

**49.** Devise an algorithm based on BFS/DFS for finding the connected components of a graph.

**Solution.**
Step 1. Initialize an array `component[v]` to store the component ID of each vertex, and a counter `compID=0`.

Step 2. Iterate over all vertices $v$. If `component[v]` is unassigned:
- Increment `compID`.
- Run BFS (or DFS) starting from $v$. For every vertex $u$ reached during this traversal, assign `component[u]=compID`.

Step 3. After iterating over all vertices, `compID` equals the number of connected components. The vertices in each component are those sharing the same component ID.

Step 4. The algorithm runs in $O(|V|+|E|)$ time and uses $O(|V|)$ extra space.

$$\boxed{\text{Iterate unvisited vertices; BFS/DFS from each assigns a component ID.}}$$

---

**50.** Explain how BFS/DFS can be used to determine whether a graph is bipartite.

**Solution.**
Step 1. A graph is bipartite iff it can be 2-colored such that no edge connects vertices of the same color. Equivalently, it contains no odd-length cycle.

Step 2. **Algorithm (BFS or DFS coloring):**
- Initialize `color[v]` to unassigned (e.g., $-1$) for all vertices.
- For each uncolored vertex $v$, set `color[v]=0$ (say Red) and run BFS/DFS.

Step 3. During traversal, when examining edge $(u,v)$:
- If `color[v]` is unassigned: assign `color[v]=1-color[u]` (the opposite color) and enqueue/recurse.
- If `color[v]` is already assigned: check if `color[v]==color[u]`. If they are the same color, the graph is **not bipartite** (an edge connects two vertices of the same color, implying an odd cycle).

Step 4. If the traversal completes without any color conflict, the graph is bipartite. The algorithm runs in $O(|V|+|E|)$ time.

$$\boxed{\text{2-color via BFS/DFS: same-color neighbor } \Rightarrow \text{ not bipartite.}}$$

---

**51.** **Backtracking** algorithm for subset-sum. Apply to set $\{27,24,19,14,11,8\}$ with targets 20, 41, 60. Draw search trees.

**Solution.**
Step 1. **Algorithm:** Sort the set (given as $27,24,19,14,11,8$, already descending). Build the sum by including terms in order. If the sum exceeds $M$, backtrack by dropping the last term.

**(a) Target $M=20$:**

Search tree (pruned branches shown):
- Sum $0$:
  - Try $27$: exceeds 20. Skip.
  - Try $24$: exceeds 20. Skip.
  - Try $19$: sum $19$.
    - Try $14$: $33>20$. Skip.
    - Try $11$: $30>20$. Skip.
    - Try $8$: $27>20$. Skip.
  - Try $14$: sum $14$.
    - Try $11$: $25>20$. Skip.
    - Try $8$: $22>20$. Skip.
  - Try $11$: sum $11$.
    - Try $8$: $19<20$. No more numbers. $19\neq20$.
  - Try $8$: sum $8$. No more.

**No subset sums to 20.**

**(b) Target $M=41$:**

Search:
- Sum $0$:
  - Try $27$: sum $27$.
    - Try $24$: $51>41$. Skip.
    - Try $19$: $46>41$. Skip.
    - Try $14$: $41=41$ **$\to$ Found!** $\{27,14\}$.
    (Continue for completeness):
    - Try $11$: $38$. Try $8$: $46>41$. Skip.
    - Try $8$: $35$. No more.
  - Try $24$: sum $24$.
    - Try $19$: $43>41$. Skip.
    - Try $14$: $38$. Try $11$: $49>41$. Skip. Try $8$: $46>41$. Skip.
    - Try $11$: $35$. Try $8$: $43>41$. Skip.
    - Try $8$: $32$. No more.
  - Try $19$: sum $19$.
    - Try $14$: $33$. Try $11$: $44>41$. Skip. Try $8$: $41$ **$\to$ Found!** $\{19,14,8\}$.
    - Try $11$: $30$. Try $8$: $38$. No more.
    - Try $8$: $27$. No more.
  - Try $14$: $14+11=25+8=33$. No.

**Solutions:** $\{27,14\}$ and $\{19,14,8\}$.

**(c) Target $M=60$:**

Search (recording only solution paths):
- $27$:
  - $27+24=51$. $+19=70>60$. Skip. $+14=65>60$. Skip. $+11=62>60$. Skip. $+8=59$. $59<60$, no more numbers.
  - $27+19=46$. $+14=60$ **$\to$ Found!** $\{27,19,14\}$.
  - $27+14=41$. $+19=60$ (same set). $+11=52$. $+8=60$ **$\to$ Found!** $\{27,14,11,8\}$.
  - $27+11=38$. $+19=57$. $+8=65>60$. Skip. $+14=52$. $+8=60$ (same 4-element set).
  - $27+8=35$. $+19=54$. $+14=68>60$. $+11=65>60$. Skip. $+14=49$. $+11=60$ (same set).
- $24$:
  - $24+19=43$. $+14=57$. $+11=68>60$. $+8=65>60$. $+11=54$. $+8=62>60$.
  - $24+14=38$. $+19=57$. $+8=65>60$. $+11=49$. $+8=57$.
  - $24+11=35$. $+19=54$. $+8=62>60$. $+14=49$. $+8=57$.
  - $24+8=32$. No more.
- $19$: $19+14=33+11=44+8=52$. $19+11=30+8=38$. $19+8=27$. No more.
- $14$: max with remaining $14+11+8=33<60$. No solutions.

**Solutions:** $\{27,19,14\}$, $\{27,14,11,8\}$.

$$\boxed{\begin{aligned}
\text{(a) }M=20&:\text{ No solution.}\\
\text{(b) }M=41&:\{27,14\},\;\{19,14,8\}\\
\text{(c) }M=60&:\{27,19,14\},\;\{27,14,11,8\}
\end{aligned}}$$

---

**52.** There are 101 coins, and only one of them differs from the others (real ones) by weight. Using a balance scale, determine the counterfeit one with two weighings.

**Solution.**
Step 1. This is a variant of the classic counterfeit coin problem. We must determine whether 2 weighings on a balance scale suffice to identify one counterfeit among 101 coins.

Step 2. A balance scale has $m=3$ outcomes per weighing (left heavy, right heavy, balanced). With 2 weighings, we obtain at most $3^2=9$ distinguishable outcome sequences.

Step 3. If the counterfeit direction is unknown (heavier or lighter), there are $l=101\times2=202$ possibilities. Even if the direction is known (just heavier), there are $l=101$ possibilities.

Step 4. By the decision-tree lower bound:
$$h\ge\lceil\log_3 l\rceil$$
- For known direction: $h\ge\lceil\log_3 101\rceil=\lceil4.2\rceil=5$.
- For unknown direction: $h\ge\lceil\log_3 202\rceil=\lceil4.84\rceil=5$.

Step 5. Since $3^2=9<101$, it is **impossible** to determine the counterfeit coin among 101 coins in only 2 weighings with a standard balance scale. At least $\lceil\log_3 101\rceil=5$ weighings are required (even if the counterfeit is known to be heavier or lighter).

Step 6. The well-known 12-coin problem (counterfeit unknown direction) requires 3 weighings precisely because $3^2=9<24$ but $3^3=27\ge24$. Scaling up, 101 coins require 5 weighings.

$$\boxed{\text{Impossible. } 3^2=9<101,\text{ so at least } \lceil\log_3 101\rceil =5\text{ weighings are needed.}}$$

---
