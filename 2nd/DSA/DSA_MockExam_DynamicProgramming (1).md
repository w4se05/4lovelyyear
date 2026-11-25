---
tags: [DSA, dynamic-programming, mock-exam, VGU, 61CSE108]
aliases: [DP mock exam]
---

# Mock Exam — Dynamic Programming
**Course:** 61CSE108 Algorithms & Data Structures  
**Estimated time:** 90 minutes | **Total: 100 marks**

> [!warning] Attempt each problem before expanding the solution.

---

## Problem 1 — Matrix-Chain Multiplication (30 marks)

You are given $n = 4$ matrices $M_1, M_2, M_3, M_4$ with the following dimension array:

$$p = [4,\ 3,\ 5,\ 2,\ 6]$$

So $M_1{:}\ 4\times3$, $M_2{:}\ 3\times5$, $M_3{:}\ 5\times2$, $M_4{:}\ 2\times6$.

**(a)** Fill in the $m[i][j]$ table. *(15 marks)*

**(b)** Fill in the $s[i][j]$ table. *(5 marks)*

**(c)** State the minimum cost $m[1][4]$ and write the optimal parenthesisation using the $s$ table. *(10 marks)*

---

> [!info]- SOLUTION — Problem 1 (expand after attempting)
>
> ### (a) & (b) Fill the tables
>
> **Input check:** $M_1{:}4\times3,\ M_2{:}3\times5,\ M_3{:}5\times2,\ M_4{:}2\times6$
>
> **Base cases:** $m[1][1]=m[2][2]=m[3][3]=m[4][4]=0$
>
> ---
>
> **$\ell=2$ (pairs, one $k$ each — no real choice):**
>
> $m[1][2]$: $p_{i-1}=p_0=4$, $p_j=p_2=5$
> 
> | $k$ | Left | Right | $p_0 \cdot p_k \cdot p_2$ | Total |
> |---|---|---|---|---|
> | 1 | $m[1][1]=0$ | $m[2][2]=0$ | $4\cdot3\cdot5=60$ | **60** |
>
> → $m[1][2]=60$, $s[1][2]=1$
>
> $m[2][3]$: $p_1=3$, $p_3=2$
> 
> | $k$ | Left | Right | $3 \cdot p_k \cdot 2$ | Total |
> |---|---|---|---|---|
> | 2 | 0 | 0 | $3\cdot5\cdot2=30$ | **30** |
>
> → $m[2][3]=30$, $s[2][3]=2$
>
> $m[3][4]$: $p_2=5$, $p_4=6$
> 
> | $k$ | Left | Right | $5 \cdot p_k \cdot 6$ | Total |
> |---|---|---|---|---|
> | 3 | 0 | 0 | $5\cdot2\cdot6=60$ | **60** |
>
> → $m[3][4]=60$, $s[3][4]=3$
>
> ---
>
> **$\ell=3$ (triples, two $k$ each):**
>
> $m[1][3]$: $p_0=4$, $p_3=2$
> 
> | $k$ | $m[1][k]$ | $m[k+1][3]$ | $4 \cdot p_k \cdot 2$ | Total |
> |---|---|---|---|---|
> | 1 | 0 | 30 | $4\cdot3\cdot2=24$ | **54** ← min |
> | 2 | 60 | 0 | $4\cdot5\cdot2=40$ | 100 |
>
> → $m[1][3]=54$, $s[1][3]=1$
>
> $m[2][4]$: $p_1=3$, $p_4=6$
> 
> | $k$ | $m[2][k]$ | $m[k+1][4]$ | $3 \cdot p_k \cdot 6$ | Total |
> |---|---|---|---|---|
> | 2 | 0 | 60 | $3\cdot5\cdot6=90$ | 150 |
> | 3 | 30 | 0 | $3\cdot2\cdot6=36$ | **66** ← min |
>
> → $m[2][4]=66$, $s[2][4]=3$
>
> ---
>
> **$\ell=4$ (full chain, three $k$ values):**
>
> $m[1][4]$: $p_0=4$, $p_4=6$
> | $k$ | $m[1][k]$ | $m[k+1][4]$ | $4 \cdot p_k \cdot 6$ | Total |
> |---|---|---|---|---|
> | 1 | 0 | 66 | $4\cdot3\cdot6=72$ | 138 |
> | 2 | 60 | 60 | $4\cdot5\cdot6=120$ | 240 |
> | 3 | 54 | 0 | $4\cdot2\cdot6=48$ | **102** ← min |
>
> → $m[1][4]=\mathbf{102}$, $s[1][4]=3$
>
> ---
>
> ### Completed tables
>
> **$m[i][j]$ table:**
>
> | | $j=1$ | $j=2$ | $j=3$ | $j=4$ |
> |---|---|---|---|---|
> | $i=1$ | 0 | 60 | 54 | **102** |
> | $i=2$ | — | 0 | 30 | 66 |
> | $i=3$ | — | — | 0 | 60 |
> | $i=4$ | — | — | — | 0 |
>
> **$s[i][j]$ table:**
>
> | | $j=2$ | $j=3$ | $j=4$ |
> |---|---|---|---|
> | $i=1$ | 1 | 1 | 3 |
> | $i=2$ | — | 2 | 3 |
> | $i=3$ | — | — | 3 |
>
> ---
>
> ### (c) Traceback
>
> `print(s, 1, 4)`:
> - $s[1][4]=3$ → left $(1,3)$, right $(4,4)=M_4$
>   - $s[1][3]=1$ → left $(1,1)=M_1$, right $(2,3)$
>     - $s[2][3]=2$ → left $(2,2)=M_2$, right $(3,3)=M_3$ → $(M_2 M_3)$
>   - → $(M_1(M_2 M_3))$
> - Full: $\boxed{((M_1(M_2 M_3))M_4),\ \text{cost} = 102}$
>
> **Verification:** $M_2 M_3$: $3\times5 \cdot 5\times2 = 30$ ops → result is $3\times2$.  
> $M_1(M_2 M_3)$: $4\times3 \cdot 3\times2 = 24$ ops → result is $4\times2$.  
> $(M_1(M_2 M_3))M_4$: $4\times2 \cdot 2\times6 = 48$ ops.  
> Total = $30+24+48 = \mathbf{102}$ ✓

---

## Problem 2 — 0-1 Knapsack (25 marks)

You have a knapsack with capacity $W = 7$ and $n = 5$ items:

| Item | Weight $w_k$ | Value $v_k$ |
|------|-------------|------------|
| 1 | 1 | 2 |
| 2 | 3 | 7 |
| 3 | 4 | 9 |
| 4 | 2 | 5 |
| 5 | 5 | 12 |

**(a)** Fill in the DP table $V[k][w]$ for $k = 0 \ldots 5$ and $w = 0 \ldots 7$. *(15 marks)*

**(b)** State the maximum value. *(2 marks)*

**(c)** Trace back through the table to identify exactly which items are in the optimal knapsack. *(8 marks)*

---

> [!info]- SOLUTION — Problem 2 (expand after attempting)
>
> **Recurrence:**
> $$V[k][w] = \begin{cases} V[k-1][w] & \text{if } w_k > w \\ \max(V[k-1][w],\ v_k + V[k-1][w-w_k]) & \text{otherwise} \end{cases}$$
>
> ### (a) Filled table
>
> | $k \backslash w$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> |---|---|---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | 1 (1,2) | 0 | **2** | 2 | 2 | 2 | 2 | 2 | 2 |
> | 2 (3,7) | 0 | 2 | 2 | **7** | **9** | 9 | 9 | 9 |
> | 3 (4,9) | 0 | 2 | 2 | 7 | 9 | **11** | 11 | **16** |
> | 4 (2,5) | 0 | 2 | **5** | 7 | 9 | **12** | **14** | 16 |
> | 5 (5,12) | 0 | 2 | 5 | 7 | 9 | 12 | 14 | **17** |
>
> Bolded entries are where a cell changed from the row above (i.e., the item was taken).
>
> **Selected fill steps (non-trivial cells):**
> - Row 1, $w=1$: $w_1=1 \le 1$ → $\max(V[0][1], 2+V[0][0])=\max(0,2)=2$
> - Row 2, $w=3$: $w_2=3 \le 3$ → $\max(V[1][3], 7+V[1][0])=\max(2,7)=7$
> - Row 2, $w=4$: $\max(V[1][4], 7+V[1][1])=\max(2,9)=9$
> - Row 3, $w=5$: $w_3=4 \le 5$ → $\max(V[2][5], 9+V[2][1])=\max(9,11)=11$
> - Row 3, $w=7$: $\max(V[2][7], 9+V[2][3])=\max(9,16)=16$
> - Row 4, $w=2$: $w_4=2 \le 2$ → $\max(V[3][2], 5+V[3][0])=\max(2,5)=5$
> - Row 4, $w=5$: $\max(V[3][5], 5+V[3][3])=\max(11,12)=12$
> - Row 5, $w=7$: $w_5=5 \le 7$ → $\max(V[4][7], 12+V[4][2])=\max(16,17)=17$
>
> ### (b) Maximum value
>
> $V[5][7] = \mathbf{17}$
>
> ### (c) Traceback
>
> Start at $k=5$, $w=7$:
>
> | Step | $k$ | $w$ | $V[k][w]$ | $V[k-1][w]$ | Same? | Action |
> |---|---|---|---|---|---|---|
> | 1 | 5 | 7 | 17 | 16 | ✗ | **Take item 5**, $w = 7-5=2$, $k=4$ |
> | 2 | 4 | 2 | 5 | 2 | ✗ | **Take item 4**, $w = 2-2=0$, $k=3$ |
> | 3 | — | 0 | — | — | — | $w=0$, stop |
>
> **Optimal items: $\{4, 5\}$, total weight $= 2+5=7$, total value $= 5+12 = \mathbf{17}$** ✓

---

## Problem 3 — Longest Common Subsequence (25 marks)

Given two strings:
$$X = \texttt{PRINT} \quad (m=5)$$
$$Y = \texttt{SPINE} \quad (n=5)$$

**(a)** Fill the DP table $L[i][j]$ for $i = 0 \ldots 5$, $j = 0 \ldots 5$. *(15 marks)*

**(b)** State the length of the LCS. *(2 marks)*

**(c)** Trace back through the table to write the actual LCS string. Show each step of your traceback. *(8 marks)*

---

> [!info]- SOLUTION — Problem 3 (expand after attempting)
>
> **Recurrence:**
> $$L[i][j] = \begin{cases} 0 & i=0 \text{ or } j=0 \\ 1 + L[i-1][j-1] & X[i]=Y[j] \\ \max(L[i-1][j],\ L[i][j-1]) & X[i]\ne Y[j] \end{cases}$$
>
> ### (a) Filled table
>
> Characters: $X=$ P(1) R(2) I(3) N(4) T(5), $Y=$ S(1) P(2) I(3) N(4) E(5)
>
> | $i \backslash j$ | 0 | S | P | I | N | E |
> |---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | P | 0 | 0 | **1** | 1 | 1 | 1 |
> | R | 0 | 0 | 1 | 1 | 1 | 1 |
> | I | 0 | 0 | 1 | **2** | 2 | 2 |
> | N | 0 | 0 | 1 | 2 | **3** | 3 |
> | T | 0 | 0 | 1 | 2 | 3 | 3 |
>
> **Key non-trivial cells:**
> - $L[1][2]$: $X[1]=P=Y[2]=P$ → match → $1+L[0][1]=1$
> - $L[3][3]$: $X[3]=I=Y[3]=I$ → match → $1+L[2][2]=2$
> - $L[4][4]$: $X[4]=N=Y[4]=N$ → match → $1+L[3][3]=3$
> - $L[5][4]$: $X[5]=T \ne Y[4]=N$ → $\max(L[4][4], L[5][3])=\max(3,2)=3$
> - $L[5][5]$: $X[5]=T \ne Y[5]=E$ → $\max(L[4][5], L[5][4])=\max(3,3)=3$
>
> ### (b) LCS length
>
> $L[5][5] = \mathbf{3}$
>
> ### (c) Traceback
>
> **Rules:** At $(i,j)$:
> - If $L[i][j] = L[i-1][j]$: go **up** (row $i-1$, same col)
> - Else if $L[i][j] = L[i][j-1]$: go **left** (same row, col $j-1$)
> - Else: it was a **match** → record $X[i]$, go **diagonal** $(i-1, j-1)$
>
> | $(i,j)$ | $X[i]$ | $Y[j]$ | $L[i][j]$ | $L[i-1][j]$ | $L[i][j-1]$ | Move | Record |
> |---|---|---|---|---|---|---|---|
> | (5,5) | T | E | 3 | 3 | 3 | ↑ up | — |
> | (4,5) | N | E | 3 | 2 | 3 | ← left | — |
> | (4,4) | N | N | 3 | 2 | 2 | ↖ diag | **N** |
> | (3,3) | I | I | 2 | 1 | 1 | ↖ diag | **I** |
> | (2,2) | R | P | 1 | 1 | 0 | ↑ up | — |
> | (1,2) | P | P | 1 | 0 | 0 | ↖ diag | **P** |
> | (0,1) | — | — | base | — | — | stop | — |
>
> Characters recorded in post-order (reverse-recursion order): P, I, N
>
> **LCS = $\texttt{PIN}$, length = 3** ✓
>
> Verify: $\texttt{PIN}$ in $X=\texttt{PRINT}$: P(1) I(3) N(4) ✓  
> $\texttt{PIN}$ in $Y=\texttt{SPINE}$: P(2) I(3) N(4) ✓

---

## Problem 4 — Linear Programming Formulation (20 marks)

A small furniture factory produces two products: **standard tables** and **deluxe tables**.

- A standard table requires **2 hours** of carpentry and **1 hour** of finishing. Profit: **\$30**.
- A deluxe table requires **3 hours** of carpentry and **2 hours** of finishing. Profit: **\$50**.
- The factory has **18 hours of carpentry** and **10 hours of finishing** available per week.

**(a)** Define the decision variables. *(2 marks)*

**(b)** Write the objective function. *(3 marks)*

**(c)** Write all constraints (including non-negativity). *(5 marks)*

**(d)** List all corner points of the feasible region and determine the optimal solution. *(10 marks)*

---

> [!info]- SOLUTION — Problem 4 (expand after attempting)
>
> ### (a) Decision variables
>
> - $x_1$ = number of standard tables produced per week
> - $x_2$ = number of deluxe tables produced per week
>
> ### (b) Objective function
>
> $$\max\ 30x_1 + 50x_2$$
>
> ### (c) Constraints
>
> | Constraint | Expression | Reason |
> |---|---|---|
> | Carpentry | $2x_1 + 3x_2 \le 18$ | 18 hours available |
> | Finishing | $x_1 + 2x_2 \le 10$ | 10 hours available |
> | Non-negativity | $x_1 \ge 0,\ x_2 \ge 0$ | Can't produce negative tables |
>
> ### (d) Corner points and optimal solution
>
> The feasible region is bounded by the two constraint lines and the axes. Corner points occur where pairs of constraints are tight (binding).
>
> **Find the intersection of the two constraint lines:**
> $$2x_1 + 3x_2 = 18 \quad \text{(i)}$$
> $$x_1 + 2x_2 = 10 \quad \text{(ii)}$$
>
> Multiply (ii) by 2: $2x_1 + 4x_2 = 20$.  
> Subtract (i): $x_2 = 2$.  
> Sub back into (ii): $x_1 = 10 - 4 = 6$.  
> → Intersection point: $(6, 2)$.
>
> **All four corner points:**
>
> | Corner | How obtained | Feasible? | Objective $30x_1+50x_2$ |
> |---|---|---|---|
> | $(0, 0)$ | Both axes | ✓ | 0 |
> | $(9, 0)$ | Carpentry: $2x_1=18$, $x_2=0$ | ✓ ($9\le10$) | 270 |
> | $(6, 2)$ | Both constraints binding | ✓ | $180+100=\mathbf{280}$ |
> | $(0, 5)$ | Finishing: $x_1=0$, $2x_2=10$ | ✓ ($15\le18$) | 250 |
>
> **Optimal solution: produce $x_1=6$ standard and $x_2=2$ deluxe tables per week, for a maximum profit of $\mathbf{\$280}$.**

---

## Quick Reference Card

| Problem | Table | Base case | Recurrence | Answer cell | Traceback trigger |
|---------|-------|-----------|------------|-------------|-------------------|
| MCM | $m[i][j]$ | $m[i][i]=0$ | $\min_k(m[i][k]+m[k+1][j]+p_{i-1}p_kp_j)$ | $m[1][n]$ | $s[i][j]$ to reconstruct |
| Knapsack | $V[k][w]$ | Row 0 and col 0 = 0 | $\max(\text{skip},\ v_k+V[k-1][w-w_k])$ | $V[n][W]$ | $V[k][w]\ne V[k-1][w]$ → item taken |
| LCS | $L[i][j]$ | Row 0 and col 0 = 0 | Match: $1+L[i-1][j-1]$; No match: $\max(\uparrow,\leftarrow)$ | $L[m][n]$ | Diagonal → match |
