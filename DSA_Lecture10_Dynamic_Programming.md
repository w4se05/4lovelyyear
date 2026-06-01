---
tags: [DSA, dynamic-programming, exam-prep, VGU, 61CSE108]
aliases: [DP cheatsheet, Lecture 10]
---

# Lecture 10 — Dynamic Programming: Exam Procedure Guide

> **Covered problems:** Matrix-Chain Multiplication · 0-1 Knapsack · Longest Common Subsequence · Linear Programming (formulation only)

---

## 0. DP General Recipe

> [!tip] Every DP problem follows this skeleton
> 1. **Define subproblem** — what does `dp[...][...]` represent?
> 2. **Write recurrence** — how does a cell depend on smaller cells?
> 3. **Identify base cases** — boundary rows/columns (usually 0).
> 4. **Fill table bottom-up** — smallest subproblems first.
> 5. **Read answer** — usually the bottom-right or top-right corner.
> 6. **Traceback** — walk the table backwards to recover the actual solution.

---

## 1. Matrix-Chain Multiplication (MCM)

### The core idea

> [!tip] Mental model
> You have $n$ matrices in a row. You can place brackets wherever you want — the order of multiplication doesn't change the final answer, but it massively changes the number of operations. Your job is to find the cheapest bracket placement.
>
> **The question for every chunk $M_i \cdots M_j$:** "Where should the *last* multiplication happen?"
> If the last split is at position $k$, you compute $(\underbrace{M_i \cdots M_k}_{\text{left}})(\underbrace{M_{k+1} \cdots M_j}_{\text{right}})$. The final multiply of those two results costs $p_{i-1} \cdot p_k \cdot p_j$.

### Input format

You are always given a size array $p_0, p_1, \ldots, p_n$ where **matrix $M_i$ has dimensions $p_{i-1} \times p_i$**.

### Two tables

| Table | Meaning | How to fill |
|-------|---------|-------------|
| $m[i][j]$ | Min multiplications for $M_i \cdots M_j$ | Try all split points, take min |
| $s[i][j]$ | The $k$ that gave the minimum in $m[i][j]$ | Record whenever you update $m[i][j]$ |

### Table structure (n = 4 example)

The table is an upper triangle. Diagonals correspond to window size $\ell$:

| | $j=1$ | $j=2$ | $j=3$ | $j=4$ |
|---|---|---|---|---|
| $i=1$ | 0 | ← $\ell=2$ | ← $\ell=3$ | ← $\ell=4$ ✓ answer |
| $i=2$ | — | 0 | ← $\ell=2$ | ← $\ell=3$ |
| $i=3$ | — | — | 0 | ← $\ell=2$ |
| $i=4$ | — | — | — | 0 |

**Fill order: left-to-right along each diagonal, starting from $\ell=2$.**

### Procedure for each cell $m[i][j]$

> [!important] For a window of matrices $M_i \cdots M_j$, try every possible last split point $k$:
>
> $$\text{cost}(k) = \underbrace{m[i][k]}_{\text{left chunk}} + \underbrace{m[k+1][j]}_{\text{right chunk}} + \underbrace{p_{i-1} \cdot p_k \cdot p_j}_{\text{final multiply}}$$
>
> Pick $k$ that minimises this. Set $m[i][j] = \min$ cost, $s[i][j] = \text{best } k$.

**Which three $p$ values go into the final-multiply term?**

```
p[i-1]  ←  the row count of M_i (leftmost matrix in window)
p[k]    ←  the column of the left piece = row of the right piece
p[j]    ←  the column count of M_j (rightmost matrix in window)
```

Both $m[i][k]$ and $m[k+1][j]$ must already be filled before you compute $m[i][j]$ — guaranteed because their windows are shorter.

### Step-by-step procedure

```
1. Set m[i][i] = 0 for all i  (base: single matrix, zero cost)

2. For ℓ = 2 to n:                     ← window size
     For i = 1 to n−ℓ+1:
       j = i + ℓ − 1
       m[i][j] = ∞
       For k = i to j−1:               ← try every split
         q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
         if q < m[i][j]:
           m[i][j] = q
           s[i][j] = k

3. Answer = m[1][n]
```

### Traceback (reconstruct the parenthesisation)

```
print(s, i, j):
  if i == j:
    output "M_i"
  else:
    output "("
    print(s, i, s[i][j])       ← recurse on left chunk
    print(s, s[i][j]+1, j)     ← recurse on right chunk
    output ")"

Call: print(s, 1, n)
```

### Worked example

> $n = 4$, dimensions: $p = [5, 4, 6, 2, 7]$
> → $M_1{:}\ 5{\times}4$, $M_2{:}\ 4{\times}6$, $M_3{:}\ 6{\times}2$, $M_4{:}\ 2{\times}7$

**Base:** $m[1][1]=m[2][2]=m[3][3]=m[4][4]=0$

---

**$\ell=2$ — all pairs (one $k$ each, so no real choice):**

| Cell | $k$ | $m[i][k]$ | $m[k+1][j]$ | $p_{i-1} \cdot p_k \cdot p_j$ | Cost | Winner |
|------|-----|-----------|-------------|-------------------------------|------|--------|
| $m[1][2]$ | 1 | 0 | 0 | $p_0 \cdot p_1 \cdot p_2 = 5\cdot4\cdot6$ | **120** | $s[1][2]=1$ |
| $m[2][3]$ | 2 | 0 | 0 | $p_1 \cdot p_2 \cdot p_3 = 4\cdot6\cdot2$ | **48** | $s[2][3]=2$ |
| $m[3][4]$ | 3 | 0 | 0 | $p_2 \cdot p_3 \cdot p_4 = 6\cdot2\cdot7$ | **84** | $s[3][4]=3$ |

---

**$\ell=3$ — triples (two $k$ values each):**

For $m[1][3]$: $p_{i-1}=p_0=5$, $p_j=p_3=2$

| $k$ | $m[1][k]$ | $m[k+1][3]$ | $5 \cdot p_k \cdot 2$ | Total |
|-----|-----------|-------------|----------------------|-------|
| 1 | $m[1][1]=0$ | $m[2][3]=48$ | $5\cdot4\cdot2=40$ | **88** ← min |
| 2 | $m[1][2]=120$ | $m[3][3]=0$ | $5\cdot6\cdot2=60$ | 180 |

→ $m[1][3]=88$, $s[1][3]=1$

For $m[2][4]$: $p_{i-1}=p_1=4$, $p_j=p_4=7$

| $k$ | $m[2][k]$ | $m[k+1][4]$ | $4 \cdot p_k \cdot 7$ | Total |
|-----|-----------|-------------|----------------------|-------|
| 2 | $m[2][2]=0$ | $m[3][4]=84$ | $4\cdot6\cdot7=168$ | 252 |
| 3 | $m[2][3]=48$ | $m[4][4]=0$ | $4\cdot2\cdot7=56$ | **104** ← min |

→ $m[2][4]=104$, $s[2][4]=3$

---

**$\ell=4$ — the full chain (three $k$ values):**

For $m[1][4]$: $p_{i-1}=p_0=5$, $p_j=p_4=7$

| $k$ | $m[1][k]$ | $m[k+1][4]$ | $5 \cdot p_k \cdot 7$ | Total |
|-----|-----------|-------------|----------------------|-------|
| 1 | 0 | $m[2][4]=104$ | $5\cdot4\cdot7=140$ | 244 |
| 2 | $m[1][2]=120$ | $m[3][4]=84$ | $5\cdot6\cdot7=210$ | 414 |
| 3 | $m[1][3]=88$ | $m[4][4]=0$ | $5\cdot2\cdot7=70$ | **158** ← min |

→ $m[1][4]=\mathbf{158}$, $s[1][4]=3$

---

**Traceback:** `print(s, 1, 4)`
- $s[1][4]=3$ → split: left = $(1,3)$, right = $(4,4)$
  - $s[1][3]=1$ → split: left = $(1,1)=M_1$, right = $(2,3)$
    - $s[2][3]=2$ → split: left = $(2,2)=M_2$, right = $(3,3)=M_3$
  - Right: $M_4$

**Result: $((M_1(M_2 M_3))M_4)$, cost = 158**

> [!warning] Common mistakes
> - Using $p_i$ instead of $p_{i-1}$ for the left row count → always use $p_{i-1}$ (the index before $i$).
> - Looking up $m[k][j]$ instead of $m[k+1][j]$ for the right chunk.
> - Filling cells in row order instead of diagonal order — you'll try to look up values not yet computed.

---

## 2. 0-1 Knapsack

### Problem
$n$ items, each with weight $w_k$ and value $v_k$. Knapsack capacity $W$. Maximise total value without exceeding $W$. Each item: take it (1) or leave it (0).

### Table
$V[k][w]$ = max value using items $1 \ldots k$ with capacity $w$.

### Procedure

**Step 1 — Base cases**
$$V[0][w] = 0 \quad \forall w, \qquad V[k][0] = 0 \quad \forall k$$

**Step 2 — Fill row by row, $k = 1 \ldots n$, $w = 1 \ldots W$**

> [!important] The single decision rule
> $$V[k][w] = \begin{cases} V[k-1][w] & \text{if } w_k > w \quad \text{(no room)} \\ \max\bigl(V[k-1][w],\; v_k + V[k-1][w-w_k]\bigr) & \text{otherwise} \end{cases}$$

- **Case A** (`wt[k] > w`): can't fit item $k$ → copy value from row above.
- **Case B** (`wt[k] <= w`): take the better of (skip $k$) vs (take $k$ + best of remaining capacity).

**Step 3 — Answer**
$V[n][W]$ is the maximum value.

**Step 4 — Traceback (find which items)**
```
k = n, w = W
while k > 0 and w > 0:
    if V[k][w] != V[k-1][w]:    ← item k IS taken
        mark item k
        w = w - wt[k]
        k = k - 1
    else:                        ← item k NOT taken
        k = k - 1
```

### Worked Example

> $n=4$, $W=5$, items: (2,3), (3,4), (4,5), (5,6) → (weight, value)

**Filled table:**

| $k \backslash w$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | **3** | 3 | 3 | 3 |
| 2 | 0 | 0 | 3 | **4** | 4 | **7** |
| 3 | 0 | 0 | 3 | 4 | **5** | 7 |
| 4 | 0 | 0 | 3 | 4 | 5 | 7 |

**Traceback from $V[4][5]=7$:**
- $k=4$: $V[4][5]=7 = V[3][5]=7$ → skip item 4
- $k=3$: $V[3][5]=7 = V[2][5]=7$ → skip item 3
- $k=2$: $V[2][5]=7 \ne V[1][5]=3$ → **take item 2**, $w = 5-3 = 2$
- $k=1$: $V[1][2]=3 \ne V[0][2]=0$ → **take item 1**, $w = 2-2 = 0$

**Result:** Items $\{1, 2\}$, total value = 7.

> [!warning] Common mistake
> When `wt[k] <= w`, you must still check whether taking the item is actually better. The `max(...)` handles this — don't just always take the item.

---

## 3. Longest Common Subsequence (LCS)

### Problem
Given strings $X = x_1 \ldots x_m$ and $Y = y_1 \ldots y_n$, find the length (and the actual subsequence) of the longest string that is a subsequence of both.

### Table
$L[i][j]$ = length of LCS of $X_i = x_1 \ldots x_i$ and $Y_j = y_1 \ldots y_j$.

### Procedure

**Step 1 — Base cases**
$$L[i][0] = 0 \quad \forall i, \qquad L[0][j] = 0 \quad \forall j$$

**Step 2 — Fill row by row, $i = 1 \ldots m$, $j = 1 \ldots n$**

> [!important] The two cases
> $$L[i][j] = \begin{cases} 1 + L[i-1][j-1] & \text{if } x_i = y_j \quad \text{(match!)} \\ \max\bigl(L[i-1][j],\; L[i][j-1]\bigr) & \text{if } x_i \ne y_j \end{cases}$$

- **Match:** diagonal jump + 1.
- **No match:** take the larger of the cell above or the cell to the left.

**Step 3 — Answer**
$L[m][n]$ is the LCS length.

**Step 4 — Traceback (recover actual LCS)**

Start at $L[m][n]$, recurse:
```
LCS_print(i, j):
    if i == 0 or j == 0: return
    if L[i][j] == L[i-1][j]:       ← go up
        LCS_print(i-1, j)
    else if L[i][j] == L[i][j-1]:  ← go left
        LCS_print(i, j-1)
    else:                           ← diagonal (match)
        LCS_print(i-1, j-1)
        print x[i]                  ← print AFTER the recursive call
```

> [!note] The `print` is after the recursive call, so characters come out in correct order automatically.

### Worked Example

> $X = \text{ABCB}$ ($m=4$), $Y = \text{BDCAB}$ ($n=5$)

**Filled table:**

| $i \backslash j$ | 0 | B | D | C | A | B |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 0 | 0 | 0 | **1** | 1 |
| B | 0 | **1** | 1 | 1 | 1 | **2** |
| C | 0 | 1 | 1 | **2** | 2 | 2 |
| B | 0 | 1 | 1 | 2 | 2 | **3** |

**Traceback from $L[4][5]=3$:**
- $(4,5)$: $X[4]=B = Y[5]=B$ → **match B**, go to $(3,4)$
- $(3,4)$: $X[3]=C \ne Y[4]=A$; $L[3][4]=2 = L[3][3]=2$ → go left to $(3,3)$
- $(3,3)$: $X[3]=C = Y[3]=C$ → **match C**, go to $(2,2)$
- $(2,2)$: $X[2]=B \ne Y[2]=D$; $L[2][2]=1 = L[1][2]=0$? No. $L[2][2]=1 = L[2][1]=1$ → go left to $(2,1)$
- $(2,1)$: $X[2]=B = Y[1]=B$ → **match B**, go to $(1,0)$ → return

Print order (post-order): B, C, B → **LCS = BCB** ✓

> [!tip] Reading the traceback
> - Same as row above → move **up**
> - Same as cell to left → move **left**
> - Neither → **diagonal match**, print that character

---

## 4. Linear Programming (LP) — Formulation Only

> [!info] This topic is likely tested as a formulation problem, not an algorithm

### Steps to formulate an LP

1. **Identify decision variables** — name them $x_1, x_2, \ldots$, label what each represents.
2. **Write the objective function** — what are you maximising or minimising? Express it as a linear combination of the variables.
3. **Write constraints:**
   - *Explicit* constraints from the problem statement (resource limits, budgets, capacities).
   - *Implicit* (non-negativity): $x_i \ge 0$ for all $i$.

### Example

> Nature Connection: 80 ha forest, 20 ha park, \$120K budget. Cost: \$1K/ha (forest), \$4K/ha (park). Visiting hours: 10/ha (forest), 20/ha (park). **Maximise** visiting hours.

| Step | Result |
|------|--------|
| Variables | $x_1$ = ha allocated to forest, $x_2$ = ha allocated to park |
| Objective | $\max\ 10x_1 + 20x_2$ |
| Constraint 1 | $x_1 \le 80$ (forest land limit) |
| Constraint 2 | $x_2 \le 20$ (park land limit) |
| Constraint 3 | $x_1 + 4x_2 \le 120$ (budget) |
| Non-negativity | $x_1 \ge 0,\ x_2 \ge 0$ |

> [!note] For an exam
> The feasible region is the intersection of all constraints. The optimal solution is always at a **corner (vertex)** of the feasible region. Enumerate corners and evaluate the objective.

---

## 5. Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Matrix-Chain Mult | $O(n^3)$ | $O(n^2)$ |
| 0-1 Knapsack | $O(nW)$ | $O(nW)$ |
| LCS | $O(mn)$ | $O(mn)$ |

---

## 6. Exercises (from the lecture)

### MCM
1. $n=4$, $p = [5,10,15,20,25]$
2. $n=6$, $p = [30,35,15,5,10,20,25]$
3. $n=6$, $p = [5,7,10,6,9,8,8]$

### Knapsack ($W=6$)
Items: $(w,v)$ = $(3,25),(2,20),(1,15),(4,40)$ → optimal: items $\{1,2,3\}$, value 60  
Add item $(5,50)$ → optimal: items $\{3,5\}$, value 65  
Add item $(2,25)$ → optimal: items $\{3,5\}$, value 65

### LCS
1. $X=\text{ABCBDAB}$, $Y=\text{BDCABA}$
2. $X=\text{TACBMEF DG}$, $Y=\text{ABCDEDG}$
3. $X=\text{AACBABCCBA}$, $Y=\text{AAACBABBCA}$
