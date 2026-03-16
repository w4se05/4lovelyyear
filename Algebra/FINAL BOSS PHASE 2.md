# VGU - Final Exam: Algebra (FINAL BOSS LEVEL)

### 1. Conceptual Verification (5 pts)

**A. True or False (Deep Cuts)**
Evaluate the following assertions. Circle **t** (true) or **f** (false).
*(Scoring: +1 for correct, -1 for false, 0 for no answer)*

1.  **[ t / f ]** If $A$ is a $5 \times 3$ matrix, the set of solutions to $Ax = b$ can be a single point.
2.  **[ t / f ]** The set of all singular (non-invertible) $2 \times 2$ matrices forms a subspace of $M_{2 \times 2}$.
3.  **[ t / f ]** If $\det(A) = 0$, then the rows of $A$ are linearly dependent, but the columns might be linearly independent.
4.  **[ t / f ]** In an RSA system, if the message $m$ satisfies $\gcd(m, n) \neq 1$, encryption is impossible.
5.  **[ t / f ]** If a relation $R$ is symmetric and transitive, it is automatically reflexive.

**B. Abstract Calculation**

Let $u, v, w$ be vectors in a vector space $V$.
If $\{u, v, w\}$ is a linearly independent set, determine if the set $\{u-v, v-w, w-u\}$ is linearly independent. **Show calculation.**
__________________________________________________________________
__________________________________________________________________

---

### 2. Advanced Number Theory (5 pts)

**(a) Chinese Remainder Theorem Application**
A certain computer system identifies files by a numerical ID $x$.
* When divided by 3, the ID leaves a remainder of 2.
* When divided by 5, the ID leaves a remainder of 3.
* When divided by 7, the ID leaves a remainder of 2.
Find the **smallest positive integer** ID $x$.



**(b) RSA Vulnerability**
In an RSA setup, the modulus is $n = p \cdot q$.
A "Dangerous Message" is a message $m \in \mathbb{Z}_n$ such that $\gcd(m, n) = p$.
Estimate the **fraction** of messages in $\mathbb{Z}_n$ that are dangerous (assume $p, q$ are very large primes).



---

### 3. Symbolic Determinants & Block Matrices (4 pts)

**(a)** Compute the determinant of the following $4 \times 4$ matrix containing parameters $a, b$:
$$
A = \begin{pmatrix}
a & 0 & 0 & b \\
0 & a & b & 0 \\
0 & b & a & 0 \\
b & 0 & 0 & a
\end{pmatrix}
$$




**(b)** For which values of $a$ and $b$ is matrix $A$ **invertible**?



---

### 4. Vector Spaces: Polynomials (4 pts)

Let $P_2(t)$ be the vector space of polynomials of degree at most 2 (Basis: $\{1, t, t^2\}$).
Consider the subspace $W$ spanned by the polynomials:
$$p_1(t) = 1 + t$$
$$p_2(t) = 1 - t$$
$$p_3(t) = 2$$

**(a)** Determine if the set $\{p_1, p_2, p_3\}$ is **linearly dependent**. If so, express one as a linear combination of the others.



**(b)** Find the **dimension** of $W$.



**(c)** Determine if the polynomial $q(t) = 3 + 4t + t^2$ belongs to $W$.



---

### 5. Linear Maps on Matrix Spaces (4 pts)

Let $V = M_{2 \times 2}$ be the space of $2 \times 2$ matrices.
Consider the fixed matrix $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
Define the transformation $T: V \to V$ by $T(A) = AB - BA$.

**(a)** Find $T \left( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \right)$. Express the result as a single matrix.



**(b)** Find a **basis for the Kernel** (Null Space) of $T$. (i.e., find the matrices that commute with $B$).



---

### 6. Logic Proofs (4 pts)

**(a) Contraposition**
Prove the following statement by **contraposition**:
*"If the product of two positive real numbers $x$ and $y$ is greater than 100, then at least one of the numbers is greater than 10."*




**(b) Quantifier Negation**
Express the negation of the following statement using quantifiers, then simplify it into English:
*"For every student $S$ in the class, there exists a problem $P$ such that $S$ cannot solve $P$."*



---

### 7. Relations & Graphs (4 pts)

Let $A = \{1, 2, 3, 4, 6, 12\}$.
Define the relation $R$ on $A$ by $a R b \iff a \text{ divides } b$ (i.e., $a|b$).

**(a)** Draw the **Hasse Diagram** for this Partial Ordering.




**(b)** Identification:
* Identify all **minimal elements**.
* Identify all **maximal elements**.
* Does this poset have a **Greatest Element**? If yes, what is it?



---