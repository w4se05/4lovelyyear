## [[Inverse Matrix]] 🧮
Given a **square matrix** $A \in M_{n\times n}$, we say $A$ is **invertible** if there exists $B \in M_{n\times n}$ such that:
$$AB = BA = I_{n}$$  
We call $B$ the **inverse matrix** of $A$ and denote it by $A^{-1}$.

👉 **Only square matrices** can be invertible.

---

## [[Definition via Gaussian–Jordan Elimination]] ⚙️
Given $A \in M_{n\times n}$:

1. $A$ is invertible **iff** it can be reduced to $I_{n}$ using Gaussian–Jordan Elimination.  
2. If  
   $$(A|I_{n}) \xrightarrow{\text{G.J.E.}} (I_{n}|B)$$  
   then  
   $$A^{-1} = B$$  
3. For $Ax = b$, where $A \in M_{n\times n}$:  
   If $A$ is invertible, then the system has **one unique solution**  
   $$x = A^{-1}b$$

---

## [[Theorem 1 — Uniqueness of the Inverse]] 🔒
If the inverse matrix exists, it is **unique**.

**Proof:**  
Suppose $A \in M_{n\times n}$, and both $B_{1}$ and $B_{2}$ are inverses of $A$. Then:
$$
\begin{cases}
AB_{1} = B_{1}A = I_{n} \\
AB_{2} = B_{2}A = I_{n}
\end{cases}
$$
From $AB_{1} = I_{n}$:
$$B_{2}AB_{1} = B_{2}I_{n} \Rightarrow (B_{2}A)B_{1} = B_{2} \Rightarrow I_{n}B_{1} = B_{2} \Rightarrow B_{1}=B_{2}$$

Hence, the inverse is **unique**. ✅

---

## [[Theorem 2 — Properties of Inverse Matrices]] 🧠
Let $A, B \in M_{n\times n}$ be invertible matrices, and let $\lambda \in \mathbb{R}$, $\lambda \neq 0$.

1. If $A$ is invertible, then $A^{T}$ is invertible and  
   $$(A^{T})^{-1} = (A^{-1})^{T}$$  
2. If $A$ is invertible, then $A^{-1}$ is invertible and  
   $$(A^{-1})^{-1} = A$$  
3. If $A, B$ are invertible, then $AB$ is invertible and  
   $$(AB)^{-1} = B^{-1}A^{-1}$$  
4. If $A$ is invertible and $\lambda \neq 0$, then $\lambda A$ is invertible and  
   $$(\lambda A)^{-1} = \frac{1}{\lambda}A^{-1}$$  

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

# Theorem
Let A be an invertible matrix and let C be cofactor matrix of A,
i.e. $C_{ij}$ are cofactors of entries $a_{ij}$ . Then,
$$A^{-1} =\frac{1}{det(A)}C^T
$$

Remark: The matrix $C^T$ is called the adjoint matrix of A, denoted by adj(A).

🧩 **Summary Insight:**  
Invertibility links algebraic structure to geometric intuition — every invertible matrix corresponds to a **reversible linear transformation** (no information loss).

---

