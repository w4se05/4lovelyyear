
> [!Definition] What is a Determinant?  
> Let $A = [a_{ij}]$ be a **square matrix** of size $n \times n$ (that is, $A \in M_{n \times n}$ — the set of all $n \times n$ matrices).  
> The **determinant** of $A$, denoted $\det(A)$ or $|A|$, is a scalar value associated with $A$ that encodes essential information about its properties (e.g., invertibility, area/volume, and linear dependence).

---

## 🧮 Basic Determinant Forms

> [!Example] Base Cases  
> - **$1\times1$ Matrix**  
>   $$A = [a_{11}] \Rightarrow \det(A) = a_{11}.$$
>
> - **$2\times2$ Matrix**  
>   $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad \det(A) = ad - bc.$$
>
> - **$3\times3$ Matrix**  
>   $$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$  
>   $$\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31}).$$

---

## 🧠 Cofactors and Minors

> [!Definition] Minor and Cofactor  
> - The **minor** of $a_{ij}$, denoted $M_{ij}$, is the determinant of the submatrix obtained by deleting row $i$ and column $j$ of $A$.  
> - The **cofactor** of $a_{ij}$ is $C_{ij} = (-1)^{i+j} M_{ij}$.
>
> Using these, we can expand $\det(A)$ along any row or column:  
> $$\det(A) = \sum_{k=1}^{n} a_{ik}C_{ik} = \sum_{k=1}^{n} a_{kj}C_{kj}.$$

---

## ⚙️ Properties of Determinants

> [!Property] Core Properties  
> For any $A, B \in M_{n\times n}$ and $k \in \mathbb{R}$:
>
> 1. $\det(I_n) = 1$ where $I_n$ is the identity matrix.  
> 2. $\det(A^T) = \det(A)$ (transpose doesn’t change determinant).  
> 3. $\det(kA) = k^n \det(A)$ (scalar multiple rule).  
> 4. $\det(AB) = \det(A)\det(B)$ (multiplicative rule).  
> 5. If two rows (or columns) of $A$ are equal or proportional, $\det(A) = 0$.  
> 6. Swapping two rows (or columns) changes the sign of $\det(A)$.  
> 7. Adding a multiple of one row (or column) to another doesn’t change $\det(A)$.

---

## 🔁 Determinant and Row Operations

> [!Note] Row Operation Effects  
> - $R_i \leftrightarrow R_j$ → $\det(A)$ changes **sign**.  
> - $R_i \to kR_i$ → $\det(A)$ multiplies by **$k$**.  
> - $R_i \to R_i + kR_j$ → $\det(A)$ **unchanged**.
>
> 💡 Efficient computation tip: factor out constants during row reduction before expansion.

---

## 🧩 Determinant and Invertibility

> [!Theorem] Determinant-Invertibility Relationship  
> A square matrix $A$ is **invertible** (non-singular) if and only if $\det(A) \neq 0$.  
>  
> If $\det(A) = 0$, $A$ is **singular** → no inverse exists.  
>  
> $$A^{-1} \text{ exists } \iff \det(A) \neq 0.$$

---

## 📊 Determinant Relations

| Operation | Property |
|------------|-----------|
| $\det(AB)$ | $\det(A)\det(B)$ |
| $\det(A^T)$ | $\det(A)$ |
| $\det(A^{-1})$ | $\dfrac{1}{\det(A)}$ |
| $\det(kA)$ | $k^n \det(A)$ |

---

## 📐 Geometric Interpretation

> [!Tip] Geometry Insight  
> - In $\mathbb{R}^2$, $\det(A)$ gives the **signed area** of the parallelogram spanned by the column vectors of $A$.  
> - In $\mathbb{R}^3$, $\det(A)$ gives the **signed volume** of the parallelepiped spanned by the columns of $A$.  
>
> The **sign** indicates orientation (positive = right-hand, negative = left-hand).

---

## 🧮 Cramer’s Rule

> [!Definition] Solving Linear Systems Using Determinants  
> For a system $A\vec{x} = \vec{b}$ with $A \in M_{n\times n}$ and $\det(A)\neq0$:  
> $$x_i = \frac{\det(A_i)}{\det(A)},$$  
> where $A_i$ is obtained from $A$ by replacing its $i$-th column with $\vec{b}$.

---

# 🧾 Examples & Applications

---

> [!Example] Example 1 — Compute $\det(A)$ (Using Laplace Expansion)  
> $$A = \begin{pmatrix} 2 & 1 & -3 \\ 0 & 4 & 5 \\ 1 & -2 & 3 \end{pmatrix}$$  
>
> Expanding along the first row:  
> $$\det(A) = 2\begin{vmatrix}4 & 5 \\ -2 & 3\end{vmatrix} - 1\begin{vmatrix}0 & 5 \\ 1 & 3\end{vmatrix} - 3\begin{vmatrix}0 & 4 \\ 1 & -2\end{vmatrix}$$  
>
> Compute minors:  
> $M_{11}=22,\; M_{12}=-5,\; M_{13}=-4.$  
>
> $$\Rightarrow \det(A) = 2(22) - 1(-5) + (-3)(-4) = 61.$$  
> ✅ $\boxed{\det(A) = 61}$

---

> [!Example] Example 2 — Check Invertibility (Using $\det(A)\neq0$)  
> $$B = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & -1 & 0 \end{pmatrix}$$  
>
> $$\det(B) = 1(4\cdot0 - 6(-1)) - 2(2\cdot0 - 6(1)) + 3(2(-1) - 4(1)) = 0.$$  
>
> ✅ $\boxed{\det(B)=0 \Rightarrow B \text{ is singular (no inverse).}}$

---

> [!Example] Example 3 — Solve via Cramer’s Rule (Using Cramer’s Formula)  
> $$
> \begin{cases}
> x + y + z = 3,\\
> 2x - y + 3z = 7,\\
> x + 4y + 2z = 10.
> \end{cases}
> $$  
>
> $$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -1 & 3 \\ 1 & 4 & 2 \end{pmatrix}, \quad 
> \vec{b} = \begin{pmatrix} 3 \\ 7 \\ 10 \end{pmatrix}.$$
>
> $$\det(A) = -6,$$  
> and by replacement:
>
> $$\det(A_1)=-18,\quad \det(A_2)=-6,\quad \det(A_3)=-18.$$
>
> $$x = \frac{-18}{-6}=3,\quad y = \frac{-6}{-6}=1,\quad z = \frac{-18}{-6}=3.$$  
> ✅ $\boxed{(x,y,z)=(3,1,3)}$

---

> [!Example] Example 4 — Geometry Meaning (Using 2×2 Determinant)  
> Given $\vec{u}=(3,1)$ and $\vec{v}=(2,4)$,  
> $$\det\begin{pmatrix}3 & 2 \\ 1 & 4\end{pmatrix} = 10.$$  
> ✅ The area of the parallelogram spanned by $\vec{u}$ and $\vec{v}$ is **10**.

---

# 🧭 Summary

> [!Note] Quick Review  
> - $\det(A)$ measures **volume scaling** by transformation $A$.  
> - $\det(A)=0$ ⇔ **columns (or rows) linearly dependent**.  
> - $\det(AB)=\det(A)\det(B)$ ⇒ determinant behaves multiplicatively.  
> - Invertibility, area/volume, and Cramer’s Rule all stem from this single scalar invariant.
