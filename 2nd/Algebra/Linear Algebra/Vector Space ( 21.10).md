## [[1. Definition and Structure]] 🧭  

A **vector space** (also called *linear space*) $V$ over the real numbers $\mathbb{R}$ is a non-empty set whose elements are called **vectors** (denoted $\vec{u}, \vec{v}, \vec{w}, \dots$).  
It is equipped with two operations:

1. **Vector Addition:** for any $\vec{u}, \vec{v}\in V$, their sum $\vec{u}+\vec{v}\in V$.  
2. **Scalar Multiplication:** for any real number (called **scalar**) $\alpha\in\mathbb{R}$ and vector $\vec{u}\in V$, the product $\alpha\vec{u}\in V$.

These must satisfy the following **axioms** for all $\vec{u},\vec{v},\vec{w}\in V$ and scalars $\alpha,\beta\in\mathbb{R}$:

| Property | Expression |
|-----------|-------------|
| Additive commutativity | $\vec{u}+\vec{v}=\vec{v}+\vec{u}$ |
| Additive associativity | $(\vec{u}+\vec{v})+\vec{w}=\vec{u}+(\vec{v}+\vec{w})$ |
| Existence of zero vector | $\exists\,\vec{0}\in V:\vec{u}+\vec{0}=\vec{u}$ |
| Existence of additive inverse | $\forall\,\vec{u}\in V,\exists\,(-\vec{u})\in V$ |
| Distributivity of scalar over addition | $\alpha(\vec{u}+\vec{v})=\alpha\vec{u}+\alpha\vec{v}$ |
| Distributivity of scalar addition | $(\alpha+\beta)\vec{u}=\alpha\vec{u}+\beta\vec{u}$ |
| Associativity of scalar multiplication | $\alpha(\beta\vec{u})=(\alpha\beta)\vec{u}$ |
| Multiplicative identity | $1\cdot\vec{u}=\vec{u}$ |

---

## [[2. Common Vector Spaces]] 🧮  

| Vector Space | Typical Element | Meaning |
|---------------|----------------|-------------|
| $\mathbb{R}^n$ | $(x_1,\dots,x_n)$ | *n*-dimensional space of real vectors |
| $M_{m\times n}$ | $(a_{ij})$ | set of all $m\times n$ real matrices |
| $\mathbb{P}_n$ | $a_0+a_1x+\dots+a_nx^n$ | real polynomials of degree ≤ *n* |
| $C[a,b]$ | $f(x)$ | all continuous real-valued functions on $[a,b]$ |

---

## [[3. Subspaces]] ⚙️  

A **subspace** $U$ of $V$ (written $U\subseteq V$) is a subset that is itself a vector space under the same operations.  

To verify $U$ is a subspace:
1. The **zero vector** $\vec{0}$ belongs to $U$.  
2. If $\vec{u},\vec{v}\in U$, then $\vec{u}+\vec{v}\in U$ (closed under addition).  
3. If $\alpha\in\mathbb{R}$ and $\vec{u}\in U$, then $\alpha\vec{u}\in U$ (closed under scalar multiplication).

The intersection of subspaces is also a subspace.  
The union of subspaces is not necessarily a subspace.

---

## [[4. Linear Combination, Span, and Independence]] 🧱  

- A **linear combination** of vectors $\vec{v}_1,\dots,\vec{v}_k\in V$ is any vector  
  $$
  \vec{v}=c_1\vec{v}_1+\dots+c_k\vec{v}_k
  $$
  where $c_i\in\mathbb{R}$ are called **coefficients**.  

- The **span** of $\{\vec{v}_1,\dots,\vec{v}_k\}$, written $\text{span}\{\vec{v}_1,\dots,\vec{v}_k\}$,  
  is the set of all linear combinations of those vectors.  
  This span forms a subspace of $V$.  

- The vectors $\vec{v}_1,\dots,\vec{v}_k$ are **linearly independent** if  
  $$
  c_1\vec{v}_1+\dots+c_k\vec{v}_k=\vec{0}\Rightarrow c_1=\dots=c_k=0
  $$  
  Otherwise, they are **dependent**.

---

## [[5. Basis and Dimension]] 🧩  

A **basis** $\mathcal{B}=\{\vec{v}_1,\dots,\vec{v}_n\}$ of a vector space $V$ satisfies:
1. $\mathcal{B}$ is linearly independent.  
2. $\text{span}(\mathcal{B})=V$.

The **dimension** of $V$, written $\dim(V)$, is the number of vectors in any basis.  
Every vector $\vec{x}\in V$ can be uniquely expressed as a linear combination of basis vectors.

> Example: The standard basis of $\mathbb{R}^3$ is $\{e_1=(1,0,0),e_2=(0,1,0),e_3=(0,0,1)\}$.

---

## [[6. Coordinates Relative to a Basis]] 🧾  

Given a basis $\mathcal{B}=\{\vec{v}_1,\dots,\vec{v}_n\}$ of $V$, any vector $\vec{x}\in V$ can be written  
$$
\vec{x}=a_1\vec{v}_1+\dots+a_n\vec{v}_n
$$
The column vector  
$$
[\vec{x}]_\mathcal{B}=
\begin{bmatrix}
a_1\\a_2\\\vdots\\a_n
\end{bmatrix}
$$
is called the **coordinate vector** of $\vec{x}$ relative to $\mathcal{B}$.

---

## [[7. Row, Column, and Null Spaces]] 📊  

For a matrix $A=(a_{ij})_{m\times n}$:

| Subspace | Definition | Dimension |
|-----------|-------------|------------|
| **Row Space** | span of the row vectors of $A$ | rank($A$) |
| **Column Space** | span of the column vectors of $A$ | rank($A$) |
| **Null Space** (or **kernel**) | $\{\vec{x}\in\mathbb{R}^n\mid A\vec{x}=\vec{0}\}$ | $n-\text{rank}(A)$ |

Here $\vec{x}$ is an *n*-dimensional vector, and $\vec{0}$ denotes the zero vector.  

---

## [[8. Linear Transformations]] 🔄  

A **linear transformation** (also called *linear map*) is a function $T:V\to W$ between vector spaces satisfying:
1. $T(\vec{u}+\vec{v})=T(\vec{u})+T(\vec{v})$  
2. $T(c\vec{u})=cT(\vec{u})$ for all $c\in\mathbb{R}$.

The **kernel** of $T$, written $\ker(T)$, is the set $\{\vec{x}\in V\mid T(\vec{x})=\vec{0}\}$.  
The **image** of $T$, written $\text{Im}(T)$, is $\{T(\vec{x})\mid\vec{x}\in V\}$.  
Both are subspaces of $V$ and $W$, respectively.

If $V=\mathbb{R}^n$ and $W=\mathbb{R}^m$, then $\exists A\in M_{m\times n}$ (a matrix) such that  
$$
T(\vec{x})=A\vec{x}
$$

---

## [[9. Rank–Nullity Theorem]] 🧮  

For any linear transformation $T:V\to W$:  
$$
\dim(V)=\text{rank}(T)+\text{nullity}(T)
$$  
where:
- **rank**($T$) = $\dim(\text{Im}(T))$,  
- **nullity**($T$) = $\dim(\ker(T))$.

---

## [[10. Change of Basis]] 🔁  

Given two bases $\mathcal{B}=\{\vec{v}_1,\dots,\vec{v}_n\}$ and $\mathcal{B}'=\{\vec{v}'_1,\dots,\vec{v}'_n\}$ of $V$,  
the **change of basis matrix** $P_{\mathcal{B}\to\mathcal{B}'}$ satisfies:
$$
[\vec{x}]_{\mathcal{B}'} = P_{\mathcal{B}\to\mathcal{B}'}[\vec{x}]_\mathcal{B}
$$
Each column of $P_{\mathcal{B}\to\mathcal{B}'}$ is the coordinate vector of $\vec{v}'_i$ expressed in basis $\mathcal{B}$.

$P$ is invertible, and  
$$
P_{\mathcal{B}'\to\mathcal{B}}=P_{\mathcal{B}\to\mathcal{B}'}^{-1}
$$

---

## [[11. Eigenvalues and Eigenvectors (Preview)]] 🔹  

For a square matrix $A\in M_{n\times n}$, a **nonzero vector** $\vec{v}$ satisfying  
$$
A\vec{v}=\lambda\vec{v}
$$  
is called an **eigenvector**, and the scalar $\lambda$ is its **eigenvalue**.

To find eigenvalues:
$$
\det(A-\lambda I_n)=0
$$  
Each **eigenspace** = $\ker(A-\lambda I_n)$, a subspace of $\mathbb{R}^n$.

---

## [[📘 Examples and Applications]]

Each example states which definitions and theorems it uses.  

---

### 🧩 Example 1 — Subspace Check  
*(Using: Subspace definition + closure properties)*  

$U=\{(x,y,z)\in\mathbb{R}^3\mid x+2y+z=0\}$  
→ Verify closure:  
✅ $\vec{0}=(0,0,0)\in U$  
✅ Sum of any two elements stays in $U$  
✅ Scalar multiple of any element stays in $U$  
✅ $\Rightarrow$ $U$ is a **subspace of $\mathbb{R}^3$**.

---

### 🧩 Example 2 — Linear Independence  
*(Using: Linear independence + Gaussian elimination)*  

$\vec{v}_1=(1,2,3),\;\vec{v}_2=(2,4,6),\;\vec{v}_3=(1,0,1)$

Form matrix of column vectors:
$$
A=
\begin{bmatrix}
1&2&1\\
2&4&0\\
3&6&1
\end{bmatrix}
\rightarrow
\begin{bmatrix}
1&2&1\\
0&0&-2\\
0&0&-2
\end{bmatrix}
$$
⟹ rank$(A)=2<3\Rightarrow$ **dependent set**.

---

### 🧩 Example 3 — Basis and Dimension  
*(Using: Basis definition + span + rank)*  

$V=\text{span}\{(1,1,0),(2,0,1),(3,1,1)\}$  
$\Rightarrow$ form matrix and row-reduce:  
rank$(A)=3$ → **independent**, hence these vectors form a **basis** of $V$  
$\dim(V)=3$.

---

### 🧩 Example 4 — Null Space  
*(Using: Null space + Rank–Nullity Theorem)*  

$A=\begin{bmatrix}1&2&1\\2&4&2\end{bmatrix}$  
rank$(A)=1$  
Solve $A\vec{x}=\vec{0}$:
$$
x_1=-2x_2-x_3
\Rightarrow
\vec{x}=s(-2,1,0)+t(-1,0,1)
$$
✅ Basis for $\ker(A)$: $\{(-2,1,0),(-1,0,1)\}$  
✅ dim$(\ker A)=2=n-\text{rank}(A)$.

---

### 🧩 Example 5 — Linear Transformation and Kernel  
*(Using: Matrix representation of $T$ + kernel as null space)*  

$T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x+y,2y+z)$  
Matrix:
$$
A=\begin{bmatrix}1&1&0\\0&2&1\end{bmatrix}
$$
Solve $A\vec{x}=\vec{0}$:
$x=-y,\;z=-2y$
⟹ $\ker(T)=\text{span}\{(-1,1,-2)\}$, dim$(\ker T)=1$

---

### 🧩 Example 6 — Change of Basis  
*(Using: Coordinate transformation + invertible change matrix)*  

$\mathcal{B}=\{(1,0),(0,1)\}$, $\mathcal{B}'=\{(1,1),(1,-1)\}$  
Let $\vec{x}=(a,b)$  
$$
P_{\mathcal{B}\to\mathcal{B}'}=
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix},
\;
P^{-1}=\frac{1}{2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
$$
$$
[\vec{x}]_{\mathcal{B}'}=P^{-1}[\vec{x}]_\mathcal{B}=\frac{1}{2}
\begin{bmatrix}
a+b\\
a-b
\end{bmatrix}
$$
✅ Coordinates in new basis: $(\frac{a+b}{2},\frac{a-b}{2})$

---

## [[Summary and Key Facts]] 🧠  

| Concept | Symbol / Expression | Meaning |
|----------|--------------------|-----------|
| Vector | $\vec{v}$ | Element of vector space $V$ |
| Scalar | $\alpha,\beta$ | Real number in $\mathbb{R}$ |
| Subspace | $U\subseteq V$ | Closed under + and scalar mult |
| Span | $\text{span}\{\vec{v}_i\}$ | All linear combinations |
| Basis | $\mathcal{B}$ | Independent spanning set |
| Dimension | $\dim(V)$ | # of basis vectors |
| Null Space | $\ker(A)$ | $\{\vec{x}:A\vec{x}=0\}$ |
| Image | $\text{Im}(T)$ | $\{T(\vec{x})\mid\vec{x}\in V\}$ |
| Rank–Nullity | $\dim(V)=r+\text{nullity}$ | Key theorem |
| Change of Basis | $[\vec{x}]_{\mathcal{B}'}=P_{\mathcal{B}\to\mathcal{B}'}[\vec{x}]_\mathcal{B}$ | Basis transformation |
| Eigenpair | $(\lambda,\vec{v})$ | $A\vec{v}=\lambda\vec{v}$ |

---

## [[Exam Insights]] 🎯  

✅ Always check closure when testing subspaces.  
✅ For independence: form matrix, row-reduce, count pivots.  
✅ Dimension = number of pivots (rank).  
✅ Null space basis vectors correspond to free variables.  
✅ For linear maps, represent $T$ as matrix $A$.  
✅ $\det(A)\neq0 \Rightarrow$ columns form a basis of $\mathbb{R}^n$.  
✅ For coordinate/basis transformations, always specify both bases.

---

🔗 **See also:**
- [[Matrix]] → algebraic operations  
- [[Linear_Equation_System]] → Gaussian elimination  
- [[Determinant]] → invertibility and independence  
- [[Inverse_Matrix]] → change of basis and transformations  
