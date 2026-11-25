# 🧮 Matrix  

## [[Definition]] 📏
A **matrix** is a rectangular array of numbers arranged in rows and columns.

A matrix of size $m \times n$ (m rows, n columns) is written as:
$$
A =
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n}\\
a_{21} & a_{22} & \dots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$

Each entry $a_{ij}$ is the element in the *i*-th row and *j*-th column.  
We denote the set of all $m \times n$ matrices by $M_{m\times n}$.

> 💡 When $m=n$, the matrix is **square**.  

---

## [[Matrix Equality]] 🟰
Two matrices $A=(a_{ij})$ and $B=(b_{ij})$ are **equal** if:
- They have the same size, and  
- $a_{ij}=b_{ij}$ for all $i,j$.

---

## [[Matrix Operations]] ⚙️

### 1️⃣ Scalar Multiplication  
If $\lambda \in \mathbb{R}$ and $A=(a_{ij})$,  
$$
\lambda A = (\lambda a_{ij})
$$  

**Example:**
$$
A=\begin{bmatrix}1&2\\3&4\end{bmatrix}, \; \lambda=2 \Rightarrow
2A=\begin{bmatrix}2&4\\6&8\end{bmatrix}
$$

---

### 2️⃣ Matrix Addition  
Possible only when $A,B$ have the same dimensions.  
$$
A+B=(a_{ij}+b_{ij})
$$

**Example:**
$$
A=\begin{bmatrix}2&3\\4&5\end{bmatrix},\;
B=\begin{bmatrix}1&2\\-1&0\end{bmatrix}
\Rightarrow
A+B=\begin{bmatrix}3&5\\3&5\end{bmatrix}
$$

---

### 3️⃣ Matrix Multiplication 🔁  
Defined if the **number of columns** of $A$ equals the **number of rows** of $B$.

If $A=(a_{ij})_{m\times n}$ and $B=(b_{ij})_{n\times p}$,  
then $C=AB=(c_{ij})_{m\times p}$ where  
$$
c_{ij} = \sum_{k=1}^n a_{ik}b_{kj}
$$

> ⚠️ Not commutative: $AB \neq BA$ (in general)

---

### 🧩 Example 1 — Matrix Multiplication (Exam-Level)
Let  
$$
A=\begin{bmatrix}2&1&0\\-1&3&2\\4&0&5\end{bmatrix}, \;
B=\begin{bmatrix}1&2&3\\0&-1&4\\2&1&0\end{bmatrix}
$$
Compute $AB$.

**Solution:**
$$
AB=\begin{bmatrix}
2(1)+1(0)+0(2)&2(2)+1(-1)+0(1)&2(3)+1(4)+0(0)\\
(-1)(1)+3(0)+2(2)&(-1)(2)+3(-1)+2(1)&(-1)(3)+3(4)+2(0)\\
4(1)+0(0)+5(2)&4(2)+0(-1)+5(1)&4(3)+0(4)+5(0)
\end{bmatrix}
$$
$$
=\boxed{
\begin{bmatrix}
2&3&10\\
3&-1&9\\
14&13&12
\end{bmatrix}}
$$

✅ Check: $(3\times3)(3\times3)\Rightarrow(3\times3)$ ✔️

---

## [[Transpose of a Matrix]] 🔄
For $A=(a_{ij})_{m\times n}$, its **transpose** $A^T$ is obtained by swapping rows and columns:
$$
A^T=(a_{ji})_{n\times m}
$$

**Example:**
$$
A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}
\Rightarrow
A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}
$$

---

## [[Properties of Matrix Operations]] 🧠

For $A,B,C \in M_{m\times n}$ and $\alpha,\beta \in \mathbb{R}$:

| Property | Formula |
|-----------|----------|
| Commutativity (Add.) | $A+B=B+A$ |
| Associativity (Add.) | $A+(B+C)=(A+B)+C$ |
| Associativity (Mult.) | $(AB)C=A(BC)$ |
| Distributivity | $A(B+C)=AB+AC$ |
| Scalar Multiplication | $(\alpha+\beta)A=\alpha A+\beta A$ |
| Transpose | $(A^T)^T=A$ |
| Transpose of sum | $(A+B)^T=A^T+B^T$ |
| Transpose of product | $(AB)^T=B^T A^T$ |

---

## [[Special Matrices]] 🔹

1️⃣ **Zero Matrix** — all entries = 0  
2️⃣ **Identity Matrix** $I_n$:  
$$
I_n = 
\begin{bmatrix}
1 & 0 & \dots & 0\\
0 & 1 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \dots & 1
\end{bmatrix}
$$  
3️⃣ **Diagonal Matrix:** only diagonal entries may be nonzero.  
4️⃣ **Symmetric Matrix:** $A=A^T$.  
5️⃣ **Upper/Lower Triangular:** all entries below/above diagonal are zero.

---

## [[Matrix Representation of Linear Systems]] 📊

A **system of linear equations** can be written as:
$$
A\vec{x} = \vec{b}
$$
where
$$
A=\begin{bmatrix}
a_{11}&a_{12}&\dots&a_{1n}\\
a_{21}&a_{22}&\dots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{m1}&a_{m2}&\dots&a_{mn}
\end{bmatrix},
\quad
\vec{x}=\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix},
\quad
\vec{b}=\begin{bmatrix}b_1\\b_2\\\vdots\\b_m\end{bmatrix}
$$

Augmented matrix representation:
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

### 🧩 Example 2 — System Representation
Given:
$$
\begin{cases}
x+2y+z=2\\
2x+3y+z=4\\
x+y+2z=3
\end{cases}
$$
Then:
$$
A=\begin{bmatrix}1&2&1\\2&3&1\\1&1&2\end{bmatrix}, \quad
\vec{x}=\begin{bmatrix}x\\y\\z\end{bmatrix}, \quad
\vec{b}=\begin{bmatrix}2\\4\\3\end{bmatrix}
$$
$$
\Rightarrow A\vec{x}=\vec{b}, \quad
(A|\vec{b})=\begin{bmatrix}1&2&1&|&2\\2&3&1&|&4\\1&1&2&|&3\end{bmatrix}
$$

---

## [[Row Operations and Equivalence]] 🔁

**Elementary Row Operations:**
1. Swap two rows: $R_i \leftrightarrow R_j$
2. Multiply a row by a nonzero constant: $kR_i$
3. Add a multiple of one row to another: $R_i + kR_j$

Two matrices are **row equivalent** if one can be obtained from the other using a sequence of such operations.

> 💡 Row operations preserve the *solution set* of the associated linear system.

---

### 🧩 Example 3 — Row Reduction

$$
A=\begin{bmatrix}
1&2&1\\
2&3&1\\
1&1&2
\end{bmatrix}
$$
Perform $R_2-2R_1$, $R_3-R_1$:
$$
\Rightarrow
\begin{bmatrix}
1&2&1\\
0&-1&-1\\
0&-1&1
\end{bmatrix}
$$
Then $R_3-R_2$:
$$
\Rightarrow
\begin{bmatrix}
1&2&1\\
0&-1&-1\\
0&0&2
\end{bmatrix}
$$

✅ Triangular → ready for back substitution.

---

## [[Matrix Rank (Preview)]] 🎯
The **rank** of a matrix is the number of **nonzero rows** in its row echelon form.  
It indicates the **dimension of the image** of the corresponding linear transformation.

> Rank links directly to **consistency** and **invertibility** — see `[[Linear_Equation_System]]` and `[[Inverse_Matrix]]`.

---

## [[Summary Table]] 📚

| Concept | Symbol | Key Insight |
|----------|--------|-------------|
| Transpose | $A^T$ | Swaps rows & columns |
| Identity | $I_n$ | Neutral in multiplication |
| Symmetric | $A=A^T$ | Mirror along diagonal |
| Rank | $r(A)$ | # of independent rows/cols |
| Inverse | $A^{-1}$ | Exists iff $\det(A)\neq0$ |
| LES Form | $A\vec{x}=\vec{b}$ | Matrix form of equations |

---

## [[Exam Tips]] 🧠  

✅ Label your operations (e.g. $R_2-3R_1$).  
✅ Verify multiplication dimensions before computing.  
✅ For proofs, always name the property you use.  
✅ Cleanly box your final matrix or reduced form.  
✅ Relate results: *“Since $\det(A)\neq0$, $A$ is invertible.”*  

> 🧩 Matrix algebra = structure + clarity. Don’t skip intermediate logic — every step can earn credit.
