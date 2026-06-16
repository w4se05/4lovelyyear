---
tags: [DSA, dynamic-programming, algorithms]
topic: "Lecture 10: Dynamic Programming"
course: "61CSE108 Algorithms and Data Structures"
---
x
> [!Note] 💡 Notation Conventions
> - $n$ — number of items / matrices / characters, depending on context
> - $m(i,j)$ — minimum scalar multiplications to compute matrix chain $\mathcal{M}_{i..j}$
> - $s(i,j)$ — optimal split index for matrix chain subproblem
> - $p_0, p_1, \ldots, p_n$ — dimension sequence; matrix $i$ has size $p_{i-1} \times p_i$
> - $V(k,w)$ — maximum value achievable using first $k$ items with knapsack capacity $w$
> - $v_i, w_i$ — value and weight of item $i$
> - $L(i,j)$ — length of LCS of prefix $X_i$ and prefix $Y_j$
> - $X_i = x_1 \ldots x_i$, $Y_j = y_1 \ldots y_j$ — string prefixes

---

# Dynamic Programming

## Part 1 — Conceptual Section

---

## 1. Core Idea

> [!Definition] 📖 Dynamic Programming (Informal)
> Dynamic programming (DP) is an algorithm design technique that solves problems by decomposing them into **overlapping subproblems**, solving each subproblem **once**, and storing the results to avoid redundant computation.
> - Achieves $O(n^2)$ or $O(n^3)$ time where naive recursion would be exponential.
> - Can be viewed as **recursion without repetition**.

> [!Property] ⚙️ Two Necessary Conditions for DP
> A problem is a good fit for DP if and only if it exhibits:
> **1.** **Optimal substructure** — an optimal solution to the problem contains optimal solutions to its subproblems.
> **2.** **Overlapping subproblems** — the subproblems needed to compute the optimal solution are reused (i.e., they are not independent).

> [!Note] 💡 Key Principle
> Express the solution via a **recurrence relation** linking the answer to sub-answers. Then evaluate the recurrence bottom-up (or top-down with memoization), filling a table in dependency order.

---

## 2. General Design Pattern

> [!Property] ⚙️ Four Steps to a DP Algorithm
> **1.** Identify a **family of subproblems** such that the final answer is a special case.
> **2.** Write a **recurrence** relating solutions to subproblems.
> **3.** Identify **base cases** for the recurrence.
> **4.** Form the algorithm:
>    - Fill a table of recurrence values in an order that respects dependencies.
>    - Extract the final answer from the table.

---

## 3. Memoization (Top-Down DP)

> [!Definition] 📖 Memoization (Memory Function Method)
> An alternative to bottom-up DP. Implement the recurrence **recursively**:
> - If a subproblem is **new**: compute its solution and **store** it.
> - If a subproblem has been **seen before**: **look up** the stored answer directly.
>
> Most useful when the recursion is natural and not all subproblems need to be solved.

---

## 4. Matrix-Chain Multiplication

### 4.1 Background

Multiplying an $a \times b$ matrix by a $b \times c$ matrix costs $\Theta(abc)$ scalar multiplications (each of the $ac$ output entries takes $\Theta(b)$ time).

Because matrix multiplication is **associative** — $(\mathcal{A}\mathcal{B})\mathcal{C} = \mathcal{A}(\mathcal{B}\mathcal{C})$ — different parenthesizations yield the same result but potentially very different costs.

> [!Definition] 📖 Matrix-Chain Multiplication Problem (Optimal Parenthesization)
> Given a sequence of dimension values $p_0, p_1, \ldots, p_n$ where matrix $i$ has size $p_{i-1} \times p_i$, find the parenthesization of $\mathcal{M}_1 \mathcal{M}_2 \cdots \mathcal{M}_n$ that minimizes the total number of scalar multiplications.

### 4.2 Subproblem Definition

Let $\mathcal{M}_{ij} = \mathcal{M}_i \mathcal{M}_{i+1} \cdots \mathcal{M}_j$ (the product of matrices $i$ through $j$).

$$m(i,j) = \text{minimum number of scalar multiplications to compute } \mathcal{M}_{ij}$$

**Base case:** $m(i,i) = 0$ (single matrix, no multiplication needed).

### 4.3 Recurrence

For any split at index $k$ ($i \leq k < j$), the last multiplication is:
$$\mathcal{M}_{ij} = \mathcal{M}_{i \ldots k} \cdot \mathcal{M}_{(k+1) \ldots j}$$

Both sub-chains must be optimally parenthesized (optimal substructure). The cost for a given $k$ is:
$$m(i,k) + m(k+1,j) + p_{i-1}\, p_k\, p_j$$

The $+\,p_{i-1} p_k p_j$ term accounts for the final multiplication of $\mathcal{M}_{i..k}$ (size $p_{i-1} \times p_k$) by $\mathcal{M}_{(k+1)..j}$ (size $p_k \times p_j$).

Choose the best $k$:

> [!Theorem] 📌 Matrix-Chain Recurrence
> $$m(i,j) = \begin{cases} 0 & \text{if } i = j \\ \displaystyle\min_{i \leq k < j}\bigl[m(i,k) + m(k+1,j) + p_{i-1}\,p_k\,p_j\bigr] & \text{if } i < j \end{cases}$$
>
> The optimal split is recorded as $s(i,j) = k_{\min}$, the minimizing $k$.

### 4.4 Fill Order

Subproblems are solved in order of increasing **chain length** $\ell = j - i + 1$:

$$\ell=1: m(1,1),\,m(2,2),\ldots$$
$$\ell=2: m(1,2),\,m(2,3),\ldots$$
$$\vdots$$
$$\ell=n: m(1,n)$$

### 4.5 Algorithm

```
MatrixChainMult(p[0..n], n):
  for i = 1 to n: m[i][i] = 0
  for l = 2 to n:
    for i = 1 to n-l+1:
      j = i + l - 1
      m[i][j] = ∞
      for k = i to j-1:
        q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
        if q < m[i][j]:
          m[i][j] = q
          s[i][j] = k
  return m, s
```

> [!Property] ⚙️ Complexity — Matrix-Chain Multiplication
> - **Time:** $O(n^3)$
> - **Space:** $\Theta(n^2)$

Reconstruct the optimal parenthesization recursively using $s(i,j)$: split at $s(1,n)$, then recurse on $s(1, s(1,n))$ and $s(s(1,n)+1, n)$.

---

## 5. 0-1 Knapsack

### 5.1 Problem Statement

> [!Definition] 📖 0-1 Knapsack Problem
> Given a knapsack of maximum capacity $W$ (integer) and $n$ items where item $i$ has integer weight $w_i$ and value $v_i$:
> Find a subset $T \subseteq \{1,\ldots,n\}$ that maximizes $\sum_{i \in T} v_i$ subject to $\sum_{i \in T} w_i \leq W$.
>
> Each item is **indivisible** — it is either fully taken (1) or not taken (0). Brute force over $2^n$ subsets runs in $O(2^n)$.

### 5.2 Subproblem and Recurrence

Let $V(k, w)$ = maximum value achievable using only items $\{1, \ldots, k\}$ with knapsack capacity $w$.

**Base cases:**
$$V(k, 0) = 0 \quad \forall k, \qquad V(0, w) = 0 \quad \forall w$$

**Recursive case** — two choices for item $k$:

| Condition | Rule |
|---|---|
| $w_k > w$ (item $k$ does not fit) | $V(k,w) = V(k-1,w)$ |
| $w_k \leq w$ (item $k$ fits) | $V(k,w) = \max\bigl(V(k-1,w),\; v_k + V(k-1,\, w-w_k)\bigr)$ |

> [!Theorem] 📌 Knapsack Recurrence
> $$V(k,w) = \begin{cases} 0 & k=0 \text{ or } w=0 \\ V(k-1,w) & w_k > w \\ \max\!\bigl(V(k-1,w),\; v_k + V(k-1,w-w_k)\bigr) & w_k \leq w \end{cases}$$

### 5.3 Table Fill Order

Fill row by row ($k = 1 \to n$), left to right ($w = 1 \to W$).

```
Knapsack(n, v[], wt[], W):
  V[0..n][0..W] initialized to 0
  for k = 1 to n:
    for w = 1 to W:
      if wt[k] > w:
        V[k][w] = V[k-1][w]
      else:
        V[k][w] = max(V[k-1][w], v[k] + V[k-1][w - wt[k]])
  return V[n][W]
```

> [!Property] ⚙️ Complexity — Knapsack
> - **Time:** $O(nW)$ (pseudo-polynomial)
> - **Space:** $\Theta(nW)$

### 5.4 Recovering the Optimal Subset

Trace back from $V(n, W)$:

```
k = n, w = W
while k > 0 and w > 0:
  if V[k][w] ≠ V[k-1][w]:
    include item k
    w = w - wt[k]
  k = k - 1
```

If $V(k,w) \neq V(k-1,w)$, item $k$ is in the knapsack (Case 3 fired). Otherwise it is not (Cases 1 or 2).

---

## 6. Longest Common Subsequence (LCS)

### 6.1 Definitions

> [!Definition] 📖 Subsequence
> A **subsequence** of string $X$ is obtained by deleting zero or more characters from $X$ (without reordering). Formally, if $X = x_1 \ldots x_m$ and $1 \leq i_1 < i_2 < \cdots < i_k \leq m$, then $x_{i_1} x_{i_2} \cdots x_{i_k}$ is a subsequence of $X$.

> [!Definition] 📖 Longest Common Subsequence (LCS) Problem
> Given strings $X = x_1 \ldots x_m$ and $Y = y_1 \ldots y_n$, find the longest string that is a subsequence of **both** $X$ and $Y$.
>
> Brute force: $O(n \cdot 2^m)$ — exponential. DP reduces this to $O(mn)$.

### 6.2 Subproblem and Recurrence

Let $L(i,j)$ = length of $\text{LCS}(X_i, Y_j)$ where $X_i = x_1 \ldots x_i$ and $Y_j = y_1 \ldots y_j$.

**Key observation:** if $x_i = y_j$, the LCS of $X_i$ and $Y_j$ ends with that symbol, so it extends the LCS of $X_{i-1}$ and $Y_{j-1}$.

> [!Theorem] 📌 LCS Recurrence
> $$L(i,j) = \begin{cases} 0 & i=0 \text{ or } j=0 \\ 1 + L(i-1,\, j-1) & x_i = y_j \\ \max\!\bigl(L(i-1,j),\; L(i,j-1)\bigr) & x_i \neq y_j \end{cases}$$

> [!Property] ⚙️ Complexity — LCS
> - **Time:** $O(mn)$
> - **Space:** $\Theta(mn)$

### 6.3 Recovering the Actual LCS

Trace back from $L(m,n)$ using the following recursive logic:

```
LCS_print(X, m, n, L):
  if m == 0 or n == 0: return
  if L[m][n] == L[m-1][n]:
    LCS_print(X, m-1, n, L)       // go up
  else if L[m][n] == L[m][n-1]:
    LCS_print(X, m, n-1, L)       // go left
  else:                            // diagonal: match
    LCS_print(X, m-1, n-1, L)
    print X[m]                     // print after recursive call
```

> [!Note] 💡 Backtracking Direction
> - **Equal to cell above** ($L[m][n] = L[m-1][n]$) → $x_m$ not in LCS, move up.
> - **Equal to cell left** ($L[m][n] = L[m][n-1]$) → $y_n$ not in LCS, move left.
> - **Neither** → $x_m = y_n$ is in LCS; print $x_m$ (after recursion so output is in correct order).

---

## 7. Linear Programming (LP) — Overview

> [!Definition] 📖 Optimization Problem (General)
> Minimize $f(x_1, \ldots, x_n)$ subject to constraints $g_i(x_1, \ldots, x_n) \;\{\geq, \leq, =\}\; b_i$ for $i = 1, \ldots, m$.

> [!Definition] 📖 Linear Programming
> An optimization problem where **all functions are linear**:
> - $f(x_1,\ldots,x_n) = c_1 x_1 + c_2 x_2 + \cdots + c_n x_n$ — **objective function** (linear)
> - Each constraint $g_i$ is also linear.
> - "Programming" here means **planning** (not computer programming).

> [!Property] ⚙️ Components of an LP Model
> **1.** **Decision variables** — the unknowns to be determined.
> **2.** **Objective function** — linear function to maximize or minimize.
> **3.** **Constraints** — explicit linear inequalities/equalities, plus **nonnegativity** (implicit constraints, e.g., $x_i \geq 0$).

> [!Note] 💡 Feasible Region
> The set of all points satisfying all constraints is the **feasible region**. The optimal solution lies at a vertex (corner) of this convex polytope.

---

## 📘 Examples & Applications

---

> [!Example] 📘 Matrix-Chain Multiplication — Full Worked Example
> **Using:** Matrix-chain recurrence, $m(i,j)$ table, $s(i,j)$ table, backtracking.
>
> **Problem:** $n = 4$ matrices with dimensions given by $p_0=5, p_1=4, p_2=6, p_3=2, p_4=7$.
> Find $m(1,4)$ and the optimal parenthesization.
>
> **Step 0 — Base cases ($\ell = 1$):**
> $$m(1,1) = m(2,2) = m(3,3) = m(4,4) = 0$$
>
> **Step 1 — $\ell = 2$: chains of length 2**
>
> $m(1,2)$: only $k=1$
> $$m(1,2) = m(1,1) + m(2,2) + p_0 p_1 p_2 = 0+0+5\cdot4\cdot6 = 120, \quad s(1,2)=1$$
>
> $m(2,3)$: only $k=2$
> $$m(2,3) = m(2,2) + m(3,3) + p_1 p_2 p_3 = 0+0+4\cdot6\cdot2 = 48, \quad s(2,3)=2$$
>
> $m(3,4)$: only $k=3$
> $$m(3,4) = m(3,3) + m(4,4) + p_2 p_3 p_4 = 0+0+6\cdot2\cdot7 = 84, \quad s(3,4)=3$$
>
> **Step 2 — $\ell = 3$: chains of length 3**
>
> $m(1,3)$: $k \in \{1,2\}$
> $$k=1:\; m(1,1)+m(2,3)+p_0 p_1 p_3 = 0+48+5\cdot4\cdot2 = 88$$
> $$k=2:\; m(1,2)+m(3,3)+p_0 p_2 p_3 = 120+0+5\cdot6\cdot2 = 180$$
> $$m(1,3) = 88, \quad s(1,3)=1$$
>
> $m(2,4)$: $k \in \{2,3\}$
> $$k=2:\; m(2,2)+m(3,4)+p_1 p_2 p_4 = 0+84+4\cdot6\cdot7 = 252$$
> $$k=3:\; m(2,3)+m(4,4)+p_1 p_3 p_4 = 48+0+4\cdot2\cdot7 = 104$$
> $$m(2,4) = 104, \quad s(2,4)=3$$
>
> **Step 3 — $\ell = 4$: full chain**
>
> $m(1,4)$: $k \in \{1,2,3\}$
> $$k=1:\; m(1,1)+m(2,4)+p_0 p_1 p_4 = 0+104+5\cdot4\cdot7 = 244$$
> $$k=2:\; m(1,2)+m(3,4)+p_0 p_2 p_4 = 120+84+5\cdot6\cdot7 = 414$$
> $$k=3:\; m(1,3)+m(4,4)+p_0 p_3 p_4 = 88+0+5\cdot2\cdot7 = 158$$
> $$\boxed{m(1,4) = 158}, \quad s(1,4)=3$$
>
> **Completed $m$ table:**
>
> | | $j=1$ | $j=2$ | $j=3$ | $j=4$ |
> |---|---|---|---|---|
> | $i=1$ | 0 | 120 | 88 | 158 |
> | $i=2$ | — | 0 | 48 | 104 |
> | $i=3$ | — | — | 0 | 84 |
> | $i=4$ | — | — | — | 0 |
>
> **Completed $s$ table:**
>
> | | $j=2$ | $j=3$ | $j=4$ |
> |---|---|---|---|
> | $i=1$ | 1 | 1 | 3 |
> | $i=2$ | — | 2 | 3 |
> | $i=3$ | — | — | 3 |
>
> **Optimal parenthesization reconstruction:**
> $s(1,4)=3 \Rightarrow (\mathcal{M}_{1..3})(\mathcal{M}_4)$
> $s(1,3)=1 \Rightarrow (\mathcal{M}_1)(\mathcal{M}_{2..3})$
> $s(2,3)=2 \Rightarrow (\mathcal{M}_2)(\mathcal{M}_3)$
>
> $$\mathcal{M} = \bigl((\mathcal{M}_1(\mathcal{M}_2 \mathcal{M}_3))\mathcal{M}_4\bigr)$$
> with cost **158 scalar multiplications**.

---

> [!Example] 📘 0-1 Knapsack — Full Worked Example
> **Using:** Knapsack recurrence, bottom-up table fill, backtracking.
>
> **Problem:** $n = 4$, $W = 5$.
>
> | Item | Weight $w_i$ | Value $v_i$ |
> |---|---|---|
> | 1 | 2 | 3 |
> | 2 | 3 | 4 |
> | 3 | 4 | 5 |
> | 4 | 5 | 6 |
>
> **Table $V(k,w)$ — filling row by row:**
>
> | $k \backslash w$ | 0 | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | 1 | 0 | 0 | 3 | 3 | 3 | 3 |
> | 2 | 0 | 0 | 3 | 4 | 4 | 7 |
> | 3 | 0 | 0 | 3 | 4 | 5 | 7 |
> | 4 | 0 | 0 | 3 | 4 | 5 | 7 |
>
> Row $k=1$ ($w_1=2, v_1=3$): for $w<2$, $V=V(0,w)=0$; for $w \geq 2$, $V = \max(0, 3+0) = 3$.
>
> Row $k=2$ ($w_2=3, v_2=4$): at $w=5$, $V = \max(V(1,5), 4+V(1,2)) = \max(3, 4+3) = 7$.
>
> Row $k=3$ ($w_3=4, v_3=5$): at $w=5$, $V = \max(V(2,5), 5+V(2,1)) = \max(7, 5+0) = 7$.
>
> Row $k=4$ ($w_4=5, v_4=6$): at $w=5$, $V = \max(V(3,5), 6+V(3,0)) = \max(7, 6) = 7$.
>
> **Optimal value: $V(4,5) = 7$.**
>
> **Backtrack to find items:**
> - $k=4, w=5$: $V(4,5)=7 = V(3,5)=7$ → item 4 **not** included. $k=3$.
> - $k=3, w=5$: $V(3,5)=7 = V(2,5)=7$ → item 3 **not** included. $k=2$.
> - $k=2, w=5$: $V(2,5)=7 \neq V(1,5)=3$ → item 2 **included**. $w = 5-3=2$, $k=1$.
> - $k=1, w=2$: $V(1,2)=3 \neq V(0,2)=0$ → item 1 **included**. $w=0$, $k=0$.
>
> **Optimal subset: $\{1, 2\}$**, total weight $= 2+3=5 \leq W$, total value $= 3+4 = 7$.

---

> [!Example] 📘 LCS — Full Worked Example
> **Using:** LCS recurrence, table fill, backtracking.
>
> **Problem:** $X = \text{ABCB}$ ($m=4$), $Y = \text{BDCAB}$ ($n=5$). Find LCS$(X,Y)$.
>
> **Table $L(i,j)$:**
>
> | $i \backslash j$ | 0 | B | D | C | A | B |
> |---|---|---|---|---|---|---|
> | 0 $X_i$ | 0 | 0 | 0 | 0 | 0 | 0 |
> | 1 A | 0 | 0 | 0 | 0 | 1 | 1 |
> | 2 B | 0 | 1 | 1 | 1 | 1 | 2 |
> | 3 C | 0 | 1 | 1 | 2 | 2 | 2 |
> | 4 B | 0 | 1 | 1 | 2 | 2 | 3 |
>
> **Selected cell derivations:**
> - $L(1,4)$: $x_1=A=y_4=A$ → $1 + L(0,3) = 1$.
> - $L(2,5)$: $x_2=B=y_5=B$ → $1 + L(1,4) = 2$.
> - $L(3,3)$: $x_3=C=y_3=C$ → $1 + L(2,2) = 2$.
> - $L(4,5)$: $x_4=B=y_5=B$ → $1 + L(3,4) = 3$.
>
> **LCS length: $L(4,5) = 3$.**
>
> **Backtrack:**
>
> ```
> (4,5): x4=B=y5=B → match! print after recurse → recurse(3,4)
> (3,4): x3=C≠y4=A → L(3,4)=2=L(2,4)=2 → go up → recurse(2,4)
> (2,4): x2=B≠y4=A → L(2,4)=1=L(2,3)=1 → go left → recurse(2,3)
> (2,3): x2=B≠y3=C → L(2,3)=1=L(1,3)=0? No. L(2,3)=1=L(2,2)=1 → go left → recurse(2,2)
> (2,2): x2=B=y2=D? No. x2=B≠y2=D → L(2,2)=1=L(1,2)=0? No. L(2,2)=1=L(2,1)=1 → go left → recurse(2,1)
> (2,1): x2=B=y1=B → match! recurse(1,0) → base case.  print X[2] = B
> Back at (2,2)→(2,3)→(2,4)→(3,4)→(4,5): print X[4] = B
> Between them, at (3,3) eventually print X[3]=C
> ```
>
> **LCS = BCB** (length 3). ✓

---

> [!Example] 📘 Linear Programming — Nature Connection
> **Using:** LP formulation (decision variables, objective function, constraints).
>
> **Problem:** Maximize visitor-hours for a forest ($x_1$ hectares, 10 hr/ha/day) and a hiking park ($x_2$ hectares, 20 hr/ha/day). Budget: \$120K/yr at \$1K/ha (forest) and \$4K/ha (park). Land limits: $x_1 \leq 80$, $x_2 \leq 20$.
>
> **Step 1 — Decision variables:**
> $x_1$ = hectares allocated to forested wilderness area.
> $x_2$ = hectares allocated to sightseeing and hiking park.
>
> **Step 2 — Objective function:**
> $$\max\; 10x_1 + 20x_2$$
>
> **Step 3 — Constraints:**
> $$x_1 \leq 80 \quad \text{(forest land limit)}$$
> $$x_2 \leq 20 \quad \text{(park land limit)}$$
> $$x_1 + 4x_2 \leq 120 \quad \text{(budget)}$$
> $$x_1 \geq 0,\; x_2 \geq 0 \quad \text{(nonnegativity)}$$
>
> The optimal solution lies at a vertex of the feasible region (convex polygon). Evaluating corners (e.g., $(80, 10)$: value $= 800+200=1000$; $(80,0)$: $800$; $(0,20)$: $400$) — the maximum is achieved at the intersection of $x_1+4x_2=120$ and $x_2=20$: $x_1=40, x_2=20$, value $= 400+400=800$... or at $x_1=80, x_2=10$: $800+200=1000$.
>
> > [!Warning] ⚠️ Possible Gap
> > The slides do not explicitly state the final numeric optimal solution; they show the feasible region graphically and a MATLAB `linprog` call. The LP section appears to be introductory motivation rather than a fully examinable DP algorithm. Confirm with lecturer which parts are examinable.

---

## 🗂️ Summary

### Big Picture
- DP applies when a problem has **optimal substructure** + **overlapping subproblems**.
- Design steps: subproblem family → recurrence → base cases → bottom-up table → extract answer.
- Memoization = top-down DP; useful when not all subproblems are needed.

### Matrix-Chain Multiplication
- Subproblem: $m(i,j)$ = min cost to compute $\mathcal{M}_{i..j}$.
- Recurrence: $m(i,j) = \min_{i \leq k < j}[m(i,k)+m(k+1,j)+p_{i-1}p_kp_j]$; base $m(i,i)=0$.
- Fill by increasing chain length $\ell$.
- Store $s(i,j)$ to reconstruct parenthesization.
- Time: $O(n^3)$; Space: $\Theta(n^2)$.

### 0-1 Knapsack
- Subproblem: $V(k,w)$ = max value using items $1..k$ with capacity $w$.
- Recurrence: $V(k,w) = V(k-1,w)$ if $w_k>w$; else $\max(V(k-1,w),\; v_k+V(k-1,w-w_k))$.
- Base: $V(0,w)=V(k,0)=0$.
- Fill row by row. Backtrack: if $V(k,w)\neq V(k-1,w)$ → item $k$ included.
- Time: $O(nW)$; Space: $\Theta(nW)$.

### LCS
- Subproblem: $L(i,j)$ = LCS length of $X_i$ and $Y_j$.
- Recurrence: if $x_i=y_j$: $1+L(i-1,j-1)$; else $\max(L(i-1,j), L(i,j-1))$.
- Base: $L(0,j)=L(i,0)=0$.
- Backtrack: diagonal = match (character in LCS); up or left = skip.
- Time: $O(mn)$; Space: $\Theta(mn)$.

### Linear Programming
- LP: linear objective + linear constraints; used for optimization (planning).
- Setup: identify decision variables → write objective → write explicit + nonnegativity constraints.
- Optimal solution at a vertex of the feasible (convex) region.

### Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Matrix-Chain Multiplication | $O(n^3)$ | $\Theta(n^2)$ |
| 0-1 Knapsack | $O(nW)$ | $\Theta(nW)$ |
| LCS | $O(mn)$ | $\Theta(mn)$ |
