# ⚙️ Linear Equation System (LES)

---

## [[Definition]] 🧮

A **linear equation in n variables** $x_1, x_2, \dots, x_n$ is of the form  
$$
a_1x_1 + a_2x_2 + \dots + a_nx_n = b
$$  
where  
- $a_1, a_2, \dots, a_n \in \mathbb{R}$ are **coefficients**,  
- $b \in \mathbb{R}$ is the **right-hand side** (RHS).

---

## [[Linear Equation System]] 🔢

A **system of m linear equations** in n variables is written:
$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
\end{cases}
$$

---

## [[Matrix Form of LES]] 🧱
We can represent this system compactly as:
$$
A\vec{x} = \vec{b}
$$
where:
$$
A = [a_{ij}]_{m\times n}, \quad
\vec{x} = 
\begin{bmatrix}
x_1\\x_2\\\vdots\\x_n
\end{bmatrix}, \quad
\vec{b} =
\begin{bmatrix}
b_1\\b_2\\\vdots\\b_m
\end{bmatrix}
$$

and the **augmented matrix** is written:
$$
(A|\vec{b}) =
\begin{bmatrix}
a_{11}&a_{12}&\dots&a_{1n}&|&b_1\\
a_{21}&a_{22}&\dots&a_{2n}&|&b_2\\
\vdots&\vdots&\ddots&\vdots&|&\vdots\\
a_{m1}&a_{m2}&\dots&a_{mn}&|&b_m
\end{bmatrix}
$$

---

## [[Solution Set]] 🎯

A **solution** to $A\vec{x} = \vec{b}$ is an assignment  
$(x_1, x_2, \dots, x_n)$ satisfying all equations simultaneously.

We denote the solution vector:
$$
\vec{x} =
\begin{bmatrix}
x_1\\x_2\\\vdots\\x_n
\end{bmatrix}
=
\begin{bmatrix}
s_1\\s_2\\\vdots\\s_n
\end{bmatrix}
$$

---

## [[Consistency of a LES]] ⚖️

A system $A\vec{x}=\vec{b}$ is:

- **Consistent** → has at least one solution.  
- **Inconsistent** → has no solution.

---

## [[Equivalent Systems]] 🔄
Two LES are **equivalent** if they share the same solution set.

**Elementary Row Operations (EROs)** preserve equivalence:
1. Swap two rows: $R_i \leftrightarrow R_j$
2. Multiply a row by a nonzero constant: $kR_i$
3. Add a multiple of one row to another: $R_i + kR_j$

> 🧩 EROs are the backbone of **Gaussian elimination**.

---

## [[Row Echelon Form (REF)]] 🔺

A matrix is in **row echelon form** if:
1. All-zero rows are at the bottom.
2. The pivot (first nonzero element of each row) is to the right of the pivot above it.
3. All entries below a pivot are zero.

---

### [[Reduced Row Echelon Form (RREF)]] ✨

A matrix is in **reduced row echelon form** if, in addition:
4. Each pivot = 1.
5. Each pivot is the *only nonzero entry* in its column.

> 💡 RREF makes back-substitution immediate.

---

## [[Gaussian Elimination]] 🔽

Transforms $(A|\vec{b})$ → upper triangular (REF)  
→ back-substitution to solve for unknowns.

**Process:**
1. Select the leftmost nonzero column as the **pivot column**.
2. Use EROs to create zeros *below* each pivot.
3. Continue until the matrix is triangular.
4. Back-substitute to find solutions.

---

### 🧩 Example 1 — Gaussian Elimination (Exam Level)

Solve:
$$
\begin{cases}
x + 2y + z = 2\\
2x + 3y + z = 4\\
x + y + 2z = 3
\end{cases}
$$

**Step 1:** Write the augmented matrix:
$$
\left[
\begin{array}{ccc|c}
1 & 2 & 1 & 2\\
2 & 3 & 1 & 4\\
1 & 1 & 2 & 3
\end{array}
\right]
$$

**Step 2:** Eliminate $x$ below $R_1$:
- $R_2 \to R_2 - 2R_1$
- $R_3 \to R_3 - R_1$

$$
\Rightarrow
\begin{bmatrix}
1&2&1&|&2\\
0&-1&-1&|&0\\
0&-1&1&|&1
\end{bmatrix}
$$

**Step 3:** Eliminate below $R_2$:  
$R_3 \to R_3 - R_2$
$$
\Rightarrow
\begin{bmatrix}
1&2&1&|&2\\
0&-1&-1&|&0\\
0&0&2&|&1
\end{bmatrix}
$$

**Step 4:** Back-substitute:
$$
\begin{cases}
2z = 1 \Rightarrow z = 0.5\\
-y - z = 0 \Rightarrow y = -z = -0.5\\
x + 2y + z = 2 \Rightarrow x = 2
\end{cases}
$$

✅ Final Answer:
$$
\boxed{x=2,\; y=-0.5,\; z=0.5}
$$

---

## [[Gauss–Jordan Elimination]] ♻️

Extends Gaussian elimination by also making *zeros above* each pivot — producing the **Reduced Row Echelon Form (RREF)**.

Used to:
- Find **unique**, **infinite**, or **no solution** cases easily.
- Compute **matrix inverses** (see [[Inverse_Matrix]]).

---

### 🧩 Example 2 — Gauss–Jordan Elimination (RREF Form)

$$
\left[
\begin{array}{ccc|c}
1 & 2 & -1 & 3\\
2 & 4 & 1 & 7\\
-1 & -2 & 5 & 1
\end{array}
\right]
$$

**Step 1:** $R_2 \to R_2 - 2R_1$, $R_3 \to R_3 + R_1$
$$
\Rightarrow
\begin{bmatrix}
1&2&-1&|&3\\
0&0&3&|&1\\
0&0&4&|&4
\end{bmatrix}
$$

**Step 2:** $R_3 \to R_3 - \frac{4}{3}R_2$
$$
\Rightarrow
\begin{bmatrix}
1&2&-1&|&3\\
0&0&3&|&1\\
0&0&0&|&\frac{8}{3}-\frac{4}{3}= \frac{4}{3}
\end{bmatrix}
$$

❌ Inconsistency detected: last row $\Rightarrow 0= \frac{4}{3}$  
Hence, **no solution** → system **inconsistent**.

---

## [[Rank and Solution Type]] 📊

Let:
- $r(A)$ = rank of coefficient matrix,
- $r(A|\vec{b})$ = rank of augmented matrix,
- $n$ = number of variables.

| Condition | Solution Type |
|------------|----------------|
| $r(A) = r(A|\vec{b}) = n$ | Unique solution |
| $r(A) = r(A|\vec{b}) < n$ | Infinitely many solutions |
| $r(A) < r(A|\vec{b})$ | No solution (inconsistent) |

---

### 🧩 Example 3 — Rank & Solution Type

$$
(A|\vec{b}) =
\begin{bmatrix}
1 & 2 & 3 & | & 4\\
2 & 4 & 6 & | & 8\\
1 & 1 & 1 & | & 2
\end{bmatrix}
$$

$R_2 \to R_2 - 2R_1$ →  
$$
\Rightarrow
\begin{bmatrix}
1 & 2 & 3 & | & 4\\
0 & 0 & 0 & | & 0\\
1 & 1 & 1 & | & 2
\end{bmatrix}
$$

$R_3 \to R_3 - R_1$:
$$
\Rightarrow
\begin{bmatrix}
1 & 2 & 3 & | & 4\\
0 & 0 & 0 & | & 0\\
0 & -1 & -2 & | & -2
\end{bmatrix}
$$

$r(A)=2,\; r(A|\vec{b})=2,\; n=3$

✅ $\Rightarrow$ **Infinitely many solutions** (one free variable).

---

## [[Tips & Insights]] 🧠

- Label EROs clearly — partial credit depends on clarity.  
- Always check **consistency** before substitution.  
- The number of **free variables = n − r(A)**.  
- Write final answer as vector:
  $$
  \vec{x} = \vec{x_p} + t_1\vec{x_1} + t_2\vec{x_2} + \dots
  $$
- If $\det(A)\neq0$, the system has a **unique** solution.

---

## [[Summary Table]] 🧾

| Concept            | Symbol         | Meaning                         |
| ------------------ | -------------- | ------------------------------- |
| Coefficient Matrix | $A$            | Holds coefficients $a_{ij}$     |
| Augmented Matrix   | $A\| \vec{b}$  | Includes RHS                    |
| Rank               | $r(A)$         | # of pivots / independent rows  |
| REF                | Triangular     | Used for back substitution      |
| RREF               | Canonical form | All pivots = 1, zeros elsewhere |
| Consistent         | –              | Has ≥1 solution                 |
| Inconsistent       | –              | No solution                     |


---

🔗 **See also:**
- [[Matrix]] → Operations and structure  
- [[Inverse_Matrix]] → Solving $A\vec{x}=\vec{b}$ via $A^{-1}$  
- [[Determinant]] → Check invertibility  
