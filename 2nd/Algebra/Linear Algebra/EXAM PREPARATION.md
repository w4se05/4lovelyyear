## Section 1: Systems of Linear Equations & Matrices (20 Points)

![[Unit_circle_angles.svg.png]]

### Question 1.1 (10 Points)

**Problem:** Given the matrix $A = \begin{pmatrix} -2 & 1 & 0 \\ 1 & -2 & 1 \\ 0 & 1 & -2 \end{pmatrix}$.
(a) Find $A^{-1}$.
(b) Solve the system $A\mathbf{x} = \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix}$.

**Solution:**

**(a) Find $A^{-1}$ using Gauss-Jordan elimination.**

We form $[A|I]$ and row reduce to $[I|A^{-1}]$.
$$
\left[ \begin{array}{ccc|ccc}
-2 & 1 & 0 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 & 1 & 0 \\
0 & 1 & -2 & 0 & 0 & 1
\end{array} \right] \xrightarrow{R_1 \leftrightarrow R_2}
\left[ \begin{array}{ccc|ccc}
1 & -2 & 1 & 0 & 1 & 0 \\
-2 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & -2 & 0 & 0 & 1
\end{array} \right]
$$
$$
\xrightarrow{R_2 \to R_2+2R_1}
\left[ \begin{array}{ccc|ccc}
1 & -2 & 1 & 0 & 1 & 0 \\
0 & -3 & 2 & 1 & 2 & 0 \\
0 & 1 & -2 & 0 & 0 & 1
\end{array} \right] \xrightarrow{R_2 \leftrightarrow R_3}
\left[ \begin{array}{ccc|ccc}
1 & -2 & 1 & 0 & 1 & 0 \\
0 & 1 & -2 & 0 & 0 & 1 \\
0 & -3 & 2 & 1 & 2 & 0
\end{array} \right]
$$
$$
\xrightarrow{R_3 \to R_3+3R_2}
\left[ \begin{array}{ccc|ccc}
1 & -2 & 1 & 0 & 1 & 0 \\
0 & 1 & -2 & 0 & 0 & 1 \\
0 & 0 & -4 & 1 & 2 & 3
\end{array} \right] \xrightarrow{R_3 \to -1/4 R_3}
\left[ \begin{array}{ccc|ccc}
1 & -2 & 1 & 0 & 1 & 0 \\
0 & 1 & -2 & 0 & 0 & 1 \\
0 & 0 & 1 & -1/4 & -1/2 & -3/4
\end{array} \right]
$$
Now, clear the entries above the pivots.
$$
\xrightarrow{\substack{R_1 \to R_1 - R_3 \\ R_2 \to R_2 + 2R_3}}
\left[ \begin{array}{ccc|ccc}
1 & -2 & 0 & 1/4 & 3/2 & 3/4 \\
0 & 1 & 0 & -1/2 & -1 & -1/2 \\
0 & 0 & 1 & -1/4 & -1/2 & -3/4
\end{array} \right] \xrightarrow{R_1 \to R_1+2R_2}
\left[ \begin{array}{ccc|ccc}
1 & 0 & 0 & -3/4 & -1/2 & -1/4 \\
0 & 1 & 0 & -1/2 & -1 & -1/2 \\
0 & 0 & 1 & -1/4 & -1/2 & -3/4
\end{array} \right]
$$
$$
\therefore A^{-1} = -\frac{1}{4} \begin{pmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}
$$

**(b) Solve $A\mathbf{x}=\mathbf{b}$**.
The solution is $\mathbf{x} = A^{-1}\mathbf{b}$.
$$
\mathbf{x} = -\frac{1}{4} \begin{pmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix} = -\frac{1}{4} \begin{pmatrix} 3(1)+2(2)+1(5) \\ 2(1)+4(2)+2(5) \\ 1(1)+2(2)+3(5) \end{pmatrix} = -\frac{1}{4} \begin{pmatrix} 12 \\ 20 \\ 20 \end{pmatrix} = \begin{pmatrix} -3 \\ -5 \\ -5 \end{pmatrix}
$$
**Final Answer:**
(a) $A^{-1} = -\frac{1}{4} \begin{pmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}$
(b) $\mathbf{x} = \begin{pmatrix} -3 \\ -5 \\ -5 \end{pmatrix}$

### Question 1.2 (10 Points)

**Problem:** Determine the parameters $a, b, c$ such that the matrix $M = \begin{pmatrix} 2 & a-2b+2c & 2a+b+c \\ 3 & 5 & a+c \\ 0 & -2 & 0 \end{pmatrix}$ is symmetric.

**Solution:**
For $M$ to be symmetric, $M=M^T$, which requires $m_{ij}=m_{ji}$. This yields the system:
1.  $a - 2b + 2c = 3$
2.  $2a + b + c = 0$
3.  $a + c = -2 \implies c = -a-2$

Substitute (3) into (1) and (2):
$a - 2b + 2(-a-2) = 3 \implies -a - 2b = 7 \implies a+2b=-7$
$2a + b + (-a-2) = 0 \implies a + b = 2$

We solve the resulting $2 \times 2$ system:
$$
\begin{cases}
a+2b = -7 \\
a+b = 2
\end{cases}
$$
Subtracting the second equation from the first gives $b = -9$.
Substituting $b=-9$ into $a+b=2$ gives $a-9=2 \implies a=11$.
Finally, $c = -a-2 = -11-2 = -13$.

**Final Answer:** The parameters are $a=11, b=-9, c=-13$.

---

## Section 2: Determinants, Invertibility & Cramer's Rule (30 Points)

### Question 2.1 (10 Points)

**Problem:** Determine the parameter $\lambda$ such that the matrix $A = \begin{pmatrix} 2 & 1 & 2 \\ 0 & 3 & -1 \\ 4 & 1 & 2\lambda \end{pmatrix}$ is invertible.

**Solution:**
$A$ is invertible if and only if $\det(A) \neq 0$. We compute the determinant by cofactor expansion along the first column.
$$
\det(A) = 2 \begin{vmatrix} 3 & -1 \\ 1 & 2\lambda \end{vmatrix} - 0 + 4 \begin{vmatrix} 1 & 2 \\ 3 & -1 \end{vmatrix}
$$
$$
= 2(6\lambda - (-1)) + 4(-1 - 6)
$$
$$
= 2(6\lambda+1) + 4(-7) = 12\lambda + 2 - 28 = 12\lambda - 26
$$
For invertibility, $12\lambda - 26 \neq 0 \implies 12\lambda \neq 26 \implies \lambda \neq \frac{13}{6}$.

**Final Answer:** $A$ is invertible for all $\lambda \in \mathbb{R}$ such that $\lambda \neq \frac{13}{6}$.

### Question 2.2 (10 Points)

**Problem:** Knowing that the area of the parallelogram spanned by vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^2$ is 10, what is the area of the parallelogram spanned by $2\mathbf{u}$ and $-2\mathbf{u}+\mathbf{v}$?

**Solution:**
The area of a parallelogram is the absolute value of the determinant of the matrix formed by its spanning vectors.
Given: Area($\mathbf{u}, \mathbf{v}$) = $|\det([\mathbf{u} \ \mathbf{v}])| = 10$.
We want to compute: Area($2\mathbf{u}, -2\mathbf{u}+\mathbf{v}$) = $|\det([2\mathbf{u} \ -2\mathbf{u}+\mathbf{v}])|$.

Using the properties of determinants (linearity in each column):
$$
\det([2\mathbf{u} \ -2\mathbf{u}+\mathbf{v}]) = 2 \det([\mathbf{u} \ -2\mathbf{u}+\mathbf{v}])
$$
By column operations ($C_2 \to C_2 + 2C_1$), the determinant is unchanged:
$$
= 2 \det([\mathbf{u} \ (-2\mathbf{u}+\mathbf{v}) + 2\mathbf{u}]) = 2 \det([\mathbf{u} \ \mathbf{v}])
$$
The new area is $|2 \det([\mathbf{u} \ \mathbf{v}])| = 2 |\det([\mathbf{u} \ \mathbf{v}])| = 2 \cdot 10 = 20$.

**Final Answer:** The new area is 20.

### Question 2.3 (10 Points)

**Problem:** Use Cramer's Rule to solve for $x_3$ in the system:
$$
\begin{alignedat}{1}
2x_1 + x_2 &= 3 \\
x_1 + 2x_2 + x_3 &= 70 \\
x_2 + 2x_3 &= 0
\end{alignedat}
$$

**Solution:**
The system is $A\mathbf{x}=\mathbf{b}$ where $A=\begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$ and $\mathbf{b}=\begin{pmatrix} 3 \\ 70 \\ 0 \end{pmatrix}$.
By Cramer's Rule, $x_3 = \frac{\det(A_3)}{\det(A)}$, where $A_3$ is the matrix $A$ with its third column replaced by $\mathbf{b}$.

1.  **Calculate $\det(A)$:**
    $$
    \det(A) = 2 \begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix} - 1 \begin{vmatrix} 1 & 1 \\ 0 & 2 \end{vmatrix} + 0 = 2(4-1) - 1(2-0) = 2(3) - 2 = 4
    $$
2.  **Calculate $\det(A_3)$:**
    $$
    A_3 = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 2 & 70 \\ 0 & 1 & 0 \end{pmatrix}
    $$
    Expand along the third row for simplicity:
    $$
    \det(A_3) = 0 - 1 \begin{vmatrix} 2 & 3 \\ 1 & 70 \end{vmatrix} + 0 = -1(2(70) - 3(1)) = -1(140-3) = -137
    $$
3.  **Find $x_3$:**
    $$
    x_3 = \frac{\det(A_3)}{\det(A)} = \frac{-137}{4}
    $$

**Final Answer:** $x_3 = -34.25$.

---

## Section 3: Vector Spaces, Basis & Independence (25 Points)

### Question 3.1 (10 Points)

**Problem:** Are the vectors $\mathbf{u}=(1,1,1)$, $\mathbf{v}=(1,0,1)$, and $\mathbf{t}=(2,0,2)$ linearly independent or dependent? Justify your answer.

**Solution:**
The vectors are linearly dependent if a non-trivial linear combination equals the zero vector. By inspection, $\mathbf{t} = 2\mathbf{v}$.
This gives the non-trivial combination $0\mathbf{u} + 2\mathbf{v} - 1\mathbf{t} = \mathbf{0}$.
Alternatively, the matrix $A = [\mathbf{u} \ \mathbf{v} \ \mathbf{t}]$ has linearly dependent columns if $\det(A)=0$.
$$
\det\begin{pmatrix} 1 & 1 & 2 \\ 1 & 0 & 0 \\ 1 & 1 & 2 \end{pmatrix} = 0
$$
because the first and third rows are identical.

**Final Answer:** The vectors are **linearly dependent** because $\mathbf{t}=2\mathbf{v}$.

### Question 3.2 (15 Points)

**Problem:** Show that $T: \mathbb{R}^3 \to \mathbb{R}^2$ given by $T(x,y,z) = (2x+y, 2y-z)$ is a linear map, and find a basis for its kernel.

**Solution:**
**Linearity:** Let $\mathbf{u}=(x_1, y_1, z_1), \mathbf{v}=(x_2, y_2, z_2)$ and $c \in \mathbb{R}$.
1.  **Additivity:**
    $T(\mathbf{u}+\mathbf{v}) = T(x_1+x_2, y_1+y_2, z_1+z_2)$
    $= (2(x_1+x_2)+(y_1+y_2), 2(y_1+y_2)-(z_1+z_2))$
    $= (2x_1+y_1, 2y_1-z_1) + (2x_2+y_2, 2y_2-z_2) = T(\mathbf{u}) + T(\mathbf{v})$.
2.  **Homogeneity:**
    $T(c\mathbf{u}) = T(cx_1, cy_1, cz_1) = (2cx_1+cy_1, 2cy_1-cz_1) = c(2x_1+y_1, 2y_1-z_1) = cT(\mathbf{u})$.
Both properties hold, so T is linear.

**Kernel:** The kernel is the solution space of $T(\mathbf{x})=\mathbf{0}$.
$$
\begin{cases}
2x+y=0 \implies y=-2x \\
2y-z=0 \implies z=2y
\end{cases}
$$
Let $x=t$ be the free parameter. Then $y=-2t$ and $z=2(-2t)=-4t$.
The solution vector is $\mathbf{x} = (t, -2t, -4t) = t(1, -2, -4)$.
The kernel is the span of the vector $(1, -2, -4)$.

**Final Answer:** A basis for ker($T$) is $\{ \begin{pmatrix} 1 \\ -2 \\ -4 \end{pmatrix} \}$.

---

## Section 4: Linear Transformations (25 Points)

### Question 4.1 (12 Points)

**Problem:** Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be the counterclockwise rotation by $\theta = \frac{\pi}{2}$.
(a) Find the standard matrix for $T$.
(b) Find the standard matrix for the composite map $T^2$. Is $T^2$ a rotation? If so, by what angle?

**Solution:**
**(a) Standard Matrix for T**
The rotation matrix is $A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$. For $\theta=\frac{\pi}{2}$, $\cos(\frac{\pi}{2})=0$ and $\sin(\frac{\pi}{2})=1$.
$$ A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} $$

**(b) Composite Map $T^2$**
The matrix for $T^2$ is $A^2$.
$$ A^2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} $$
This matrix has the form of a rotation matrix where $\cos\phi = -1$ and $\sin\phi = 0$, which corresponds to a rotation angle of $\phi = \pi$.

**Final Answer:**
(a) $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
(b) The matrix for $T^2$ is $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$. It represents a rotation by $\pi$ radians ($180^\circ$).

### Question 4.2 (13 Points)

**Problem:**
(a) Find $\lambda$ such that $\mathbf{v}=(2\lambda, 1, -\lambda, -1)$ is orthogonal to $\mathbf{w}=(1, 2, 3, 4)$.
(b) Find the image of $\mathbf{x}=(-2, 3)$ under a counterclockwise rotation by $45^\circ$.

**Solution:**
**(a) Orthogonality**
$\mathbf{v} \cdot \mathbf{w} = 0 \implies 2\lambda(1) + 1(2) - \lambda(3) - 1(4) = 0$.
$2\lambda+2-3\lambda-4=0 \implies -\lambda-2=0 \implies \lambda=-2$.

**(b) Rotation**
The rotation matrix for $\theta=45^\circ$ is $A = \begin{pmatrix} \cos 45^\circ & -\sin 45^\circ \\ \sin 45^\circ & \cos 45^\circ \end{pmatrix} = \frac{\sqrt{2}}{2} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$.
The image is $A\mathbf{x}$:
$$
T(-2,3) = \frac{\sqrt{2}}{2} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} -2 \\ 3 \end{pmatrix} = \frac{\sqrt{2}}{2} \begin{pmatrix} -2-3 \\ -2+3 \end{pmatrix} = \frac{\sqrt{2}}{2} \begin{pmatrix} -5 \\ 1 \end{pmatrix} = \begin{pmatrix} -5\sqrt{2}/2 \\ \sqrt{2}/2 \end{pmatrix}
$$

**Final Answer:**
(a) $\lambda = -2$.
(b) The image is $(-\frac{5\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$.

## Expanded Section: Advanced Conceptual Problems

# Proofs of Theorem 2 — Properties of Inverse Matrices

## Property 1 — $(A^{T})^{-1} = (A^{-1})^{T}$

Since $A$ is invertible,
$$
AA^{-1} = I.
$$

Take transpose:
$$
(AA^{-1})^{T} = I^{T}
\quad\Rightarrow\quad
(A^{-1})^{T}A^{T} = I.
$$

Also transpose $A^{-1}A = I$:
$$
(A^{-1}A)^{T} = I^{T}
\quad\Rightarrow\quad
A^{T}(A^{-1})^{T} = I.
$$

Thus $(A^{-1})^{T}$ is both a left and right inverse of $A^{T}$, so
$$
(A^{T})^{-1} = (A^{-1})^{T}.
$$

---

## Property 2 — $(A^{-1})^{-1} = A$

From invertibility:
$$
AA^{-1} = A^{-1}A = I.
$$

So $A$ serves as the inverse of $A^{-1}$, giving
$$
(A^{-1})^{-1} = A.
$$

---

## Property 3 — $(AB)^{-1} = B^{-1}A^{-1}$

Check left multiplication:
$$
(AB)(B^{-1}A^{-1})
= A(BB^{-1})A^{-1}
= AIA^{-1}
= AA^{-1}
= I.
$$

Check right multiplication:
$$
(B^{-1}A^{-1})(AB)
= B^{-1}(A^{-1}A)B
= B^{-1}IB
= B^{-1}B
= I.
$$

Thus,
$$
(AB)^{-1} = B^{-1}A^{-1}.
$$

---

## Property 4 — $(\lambda A)^{-1} = \frac{1}{\lambda}A^{-1}$ for $\lambda \neq 0$

Compute:
$$
(\lambda A)\left(\frac{1}{\lambda}A^{-1}\right)
= \left(\lambda\frac{1}{\lambda}\right)AA^{-1}
= I.
$$

And:
$$
\left(\frac{1}{\lambda}A^{-1}\right)(\lambda A)
= \frac{1}{\lambda}\lambda A^{-1}A
= I.
$$

Hence,
$$
(\lambda A)^{-1} = \frac{1}{\lambda}A^{-1}.
$$

---

## Follow-Up Questions

**Q1:** How do I prove that $(A^{k})^{-1} = (A^{-1})^{k}$ for all integers $k$?  
**Q2:** Which parts of these proofs break if the matrices are not square?  
**Q3:** How can these inverse identities simplify solving chained systems like $A_1A_2x = b$?  


### Problem 1: Properties of a System from Incomplete Information

_Using: Rank-Nullity Theorem, Column Space, Null Space, System Consistency._

**Problem:** Let $A$ be a $4 \times 6$ matrix. Suppose that the dimension of the null space of $A$ is 2. Let $\mathbf{b}$ be any vector in $\mathbb{R}^4$.

(a) What is the rank of $A$?
(b) Explain why the system $A\mathbf{x} = \mathbf{b}$ must be consistent.
(c) If the system is consistent, can it have a unique solution? Explain your reasoning.

**Solution:**

**(a) Rank of A**
We use the Rank-Nullity Theorem, which states that for an $m \times n$ matrix, $\text{rank}(A) + \text{dim}(\text{Nul } A) = n$.
Here, $A$ is a $4 \times 6$ matrix, so $n=6$. We are given $\text{dim}(\text{Nul } A) = 2$.
$$ \text{rank}(A) + 2 = 6 $$
$$ \text{rank}(A) = 4 $$

**(b) Consistency of the System**
The system $A\mathbf{x}=\mathbf{b}$ is consistent if and only if $\mathbf{b}$ is in the column space of $A$, i.e., $\mathbf{b} \in \text{Col } A$.
The column space of $A$ is a subspace of $\mathbb{R}^4$.
From part (a), we know that the dimension of the column space is $\text{dim}(\text{Col } A) = \text{rank}(A) = 4$.
The only 4-dimensional subspace of $\mathbb{R}^4$ is $\mathbb{R}^4$ itself.
Therefore, $\text{Col } A = \mathbb{R}^4$.
Since $\mathbf{b}$ is any vector in $\mathbb{R}^4$, it must be in the column space of $A$. Thus, the system $A\mathbf{x}=\mathbf{b}$ is always consistent.

**(c) Uniqueness of the Solution**
A solution to $A\mathbf{x}=\mathbf{b}$ is unique if and only if the corresponding homogeneous system $A\mathbf{x}=\mathbf{0}$ has only the trivial solution. This is equivalent to the condition that $\text{Nul } A = \{\mathbf{0}\}$, or $\text{dim}(\text{Nul } A) = 0$.
We are given that $\text{dim}(\text{Nul } A) = 2$.
Since the dimension of the null space is greater than 0, there are infinitely many solutions to the homogeneous equation. If $\mathbf{x}_p$ is a particular solution to $A\mathbf{x}=\mathbf{b}$, the general solution is $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_h$, where $\mathbf{x}_h$ is any vector in the 2-dimensional null space.
Because there are infinitely many choices for $\mathbf{x}_h$, the system cannot have a unique solution.

**Final Answer:**
(a) The rank of A is 4.
(b) The system is always consistent because the rank of A is 4, which means its column space is all of $\mathbb{R}^4$.
(c) The system can never have a unique solution because the null space has dimension 2, meaning there are infinitely many solutions for any consistent system.

---

### Problem 2: Linear Transformations on Matrix Spaces

_Using: Abstract Vector Spaces, Kernel, Basis, Rank-Nullity Theorem._

**Problem:** Let $V=M_{2 \times 2}$ be the vector space of all $2 \times 2$ matrices. Consider the transformation $T: V \to V$ defined by $T(A) = A - A^T$.

(a) Find a basis for the kernel of $T$.
(b) Find the dimension of the range of $T$.

**Solution:**

**(a) Basis for the Kernel**
The kernel of $T$, ker($T$), is the set of all matrices $A \in V$ such that $T(A) = \mathbf{0}$, where $\mathbf{0}$ is the $2 \times 2$ zero matrix.
$$ T(A) = A - A^T = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} $$
This condition simplifies to $A = A^T$.
The kernel of $T$ is therefore the set of all $2 \times 2$ symmetric matrices.

A general $2 \times 2$ symmetric matrix has the form:
$$ A = \begin{pmatrix} a & b \\ b & c \end{pmatrix} $$
where $a, b, c$ are arbitrary real numbers. To find a basis, we can express this general form as a linear combination of constant matrices:
$$ \begin{pmatrix} a & b \\ b & c \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} $$
The set of matrices $\{ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \}$ spans the kernel and is linearly independent.

**Basis for ker(T):** $\{ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \}$
This also tells us that $\text{dim}(\text{ker } T) = 3$.

**(b) Dimension of the Range**
We use the Rank-Nullity Theorem for linear transformations: $\text{dim}(V) = \text{dim}(\text{ker } T) + \text{dim}(\text{ran } T)$.
The vector space is $V = M_{2 \times 2}$. The dimension of this space is 4 (a basis is $\{ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \}$).
From part (a), we know $\text{dim}(\text{ker } T) = 3$.
$$ 4 = 3 + \text{dim}(\text{ran } T) $$
$$ \text{dim}(\text{ran } T) = 1 $$
### Problem 4: Linear Independence of Abstract Vectors

_Using: Definition of Linear Independence, Properties of Abstract Vector Spaces._

**Problem:** (Inspired by Q12) Let $\{\mathbf{w}_1, \mathbf{w}_2, \mathbf{w}_3\}$ be a set of linearly independent vectors in a vector space $V$. Consider a new set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ where:
$$
\begin{alignedat}{1}
\mathbf{v}_1 &= \mathbf{w}_1 - \mathbf{w}_2 \\
\mathbf{v}_2 &= \mathbf{w}_2 - \mathbf{w}_3 \\
\mathbf{v}_3 &= \mathbf{w}_3 - \mathbf{w}_1
\end{alignedat}
$$
Determine if the set $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is linearly independent or dependent. If dependent, find a non-zero linear combination that equals the zero vector.

**Solution:**

1.  **Set up the test for linear independence.** We examine the vector equation:
    $$ c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0} $$
    Our goal is to determine if this equation has non-trivial solutions for $c_1, c_2, c_3$.

2.  **Substitute the definitions of $\mathbf{v}_i$ in terms of $\mathbf{w}_i$.**
    $$ c_1(\mathbf{w}_1 - \mathbf{w}_2) + c_2(\mathbf{w}_2 - \mathbf{w}_3) + c_3(\mathbf{w}_3 - \mathbf{w}_1) = \mathbf{0} $$

3.  **Group the terms by the vectors $\mathbf{w}_i$.**
    $$ (c_1 - c_3)\mathbf{w}_1 + (-c_1 + c_2)\mathbf{w}_2 + (-c_2 + c_3)\mathbf{w}_3 = \mathbf{0} $$

4.  **Use the given information.** We are given that $\{\mathbf{w}_1, \mathbf{w}_2, \mathbf{w}_3\}$ is a linearly independent set. By definition, this means the only way their linear combination can equal the zero vector is if all scalar coefficients are zero.
    This gives us a system of linear equations:
    $$
    \begin{cases}
    c_1 - c_3 = 0 \\
    -c_1 + c_2 = 0 \\
    -c_2 + c_3 = 0
    \end{cases}
    $$

5.  **Solve the system.**
    From the first equation, $c_1 = c_3$.
    From the second equation, $c_1 = c_2$.
    Therefore, $c_1 = c_2 = c_3$. Let $c_1 = t$ for any scalar $t$. Then $c_2=t$ and $c_3=t$ is a solution for any $t \in \mathbb{R}$.

6.  **Conclusion.**
    Since the system has non-trivial solutions (for example, we can choose $t=1$, giving $c_1=c_2=c_3=1$), the set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is **linearly dependent**.

7.  **Find a non-zero linear combination.**
    Using the solution $c_1=c_2=c_3=1$, we can write the specific linear combination:
    $$ 1\mathbf{v}_1 + 1\mathbf{v}_2 + 1\mathbf{v}_3 = \mathbf{0} $$
    We can verify this: $(\mathbf{w}_1 - \mathbf{w}_2) + (\mathbf{w}_2 - \mathbf{w}_3) + (\mathbf{w}_3 - \mathbf{w}_1) = \mathbf{0}$.

**Final Answer:** The set is linearly dependent. A non-zero linear combination is $\mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3 = \mathbf{0}$.

---

### Problem 5: A Proof on Kernels and Linear Independence

_Using: Definition of Linear Transformation, Kernel, Linear Independence._

**Problem:** (Inspired by Q7) Let $T: V \to W$ be a linear map between two vector spaces $V$ and $W$. Prove that if the kernel of $T$ is the trivial subspace, ker($T$) = $\{\mathbf{0}_V\}$, then $T$ preserves linear independence. That is, if $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is a linearly independent set in $V$, then the set of images $\{T(\mathbf{v}_1), \dots, T(\mathbf{v}_k)\}$ is a linearly independent set in $W$.

**Solution:**

1.  **State the assumptions and the goal.**
    **Assume:**
    (i) $T$ is a linear map.
    (ii) ker($T$) = $\{\mathbf{0}_V\}$.
    (iii) $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is linearly independent in $V$.
    **Goal:** Prove that $\{T(\mathbf{v}_1), \dots, T(\mathbf{v}_k)\}$ is linearly independent in $W$.

2.  **Start with the definition of linear independence for the target set.**
    Consider the equation for the images in $W$:
    $$ c_1 T(\mathbf{v}_1) + c_2 T(\mathbf{v}_2) + \dots + c_k T(\mathbf{v}_k) = \mathbf{0}_W $$
    To prove the set is linearly independent, we must show that this equation necessarily implies $c_1 = c_2 = \dots = c_k = 0$.

3.  **Use the linearity of T (Assumption i).**
    Since $T$ is linear, we can combine the terms on the left side:
    $$ T(c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k) = \mathbf{0}_W $$

4.  **Use the property of the kernel (Assumption ii).**
    The equation from step 3 says that the vector $\mathbf{u} = c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k$ (which is in $V$) is mapped to the zero vector in $W$. By definition of the kernel, this means $\mathbf{u}$ must be an element of ker($T$).
    We assumed ker($T$) = $\{\mathbf{0}_V\}$, so the only vector in the kernel is the zero vector of $V$. Therefore:
    $$ c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k = \mathbf{0}_V $$

5.  **Use the linear independence of the original set (Assumption iii).**
    We are given that the set $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is linearly independent in $V$. By definition, this means the only solution to the equation from step 4 is the trivial solution.
    Therefore, $c_1 = c_2 = \dots = c_k = 0$.

6.  **Conclusion.**
    We started with the linear combination of the images equaling zero and have shown that this forces all the scalar coefficients to be zero. This is the definition of linear independence for the set $\{T(\mathbf{v}_1), \dots, T(\mathbf{v}_k)\}$. The proof is complete.

---

### Problem 6: The Vandermonde Determinant

_Using: Properties of Determinants, Row/Column Operations, Connection to Linear Dependence._

**Problem:** (Inspired by Determinant problem g) Let $a, b, c$ be distinct real numbers.
(a) Consider the Vandermonde matrix $V = \begin{pmatrix} 1 & 1 & 1 \\ a & b & c \\ a^2 & b^2 & c^2 \end{pmatrix}$. Show that $\det(V) = (b-a)(c-a)(c-b)$.
(b) Explain why the columns of $V$ are linearly independent.

**Solution:**

**(a) Calculating the Determinant**
We use column operations to create zeros in the first row. These operations do not change the value of the determinant.
Let $C_2 \to C_2 - C_1$ and $C_3 \to C_3 - C_1$.
$$
\det(V) = \det \begin{pmatrix} 1 & 1-1 & 1-1 \\ a & b-a & c-a \\ a^2 & b^2-a^2 & c^2-a^2 \end{pmatrix} = \det \begin{pmatrix} 1 & 0 & 0 \\ a & b-a & c-a \\ a^2 & (b-a)(b+a) & (c-a)(c+a) \end{pmatrix}
$$
Now, perform a cofactor expansion along the first row:
$$
\det(V) = 1 \cdot \det \begin{pmatrix} b-a & c-a \\ (b-a)(b+a) & (c-a)(c+a) \end{pmatrix}
$$
We can factor out $(b-a)$ from the first column and $(c-a)$ from the second column:
$$
\det(V) = (b-a)(c-a) \det \begin{pmatrix} 1 & 1 \\ b+a & c+a \end{pmatrix}
$$
Now compute the determinant of the remaining $2 \times 2$ matrix:
$$
= (b-a)(c-a) [1(c+a) - 1(b+a)]
$$
$$
= (b-a)(c-a) (c+a-b-a) = (b-a)(c-a)(c-b)
$$
The identity is proven.

**(b) Explaining Linear Independence**
The columns of a square matrix are linearly independent if and only if its determinant is non-zero.
From part (a), we have the determinant:
$$ \det(V) = (b-a)(c-a)(c-b) $$
We are given that $a, b, c$ are **distinct** real numbers. This means:
-   $b \neq a \implies (b-a) \neq 0$
-   $c \neq a \implies (c-a) \neq 0$
-   $c \neq b \implies (c-b) \neq 0$

Since the determinant is the product of three non-zero numbers, $\det(V) \neq 0$.
Because the determinant is non-zero, the columns of the matrix $V$ are linearly independent.

**Final Answer:**
(a) The derivation using column operations shows $\det(V) = (b-a)(c-a)(c-b)$.
(b) Since $a, b, c$ are distinct, all factors in the determinant are non-zero, making $\det(V) \neq 0$. Therefore, the columns are linearly independent.