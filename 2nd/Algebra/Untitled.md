# Answer Key: FINAL BOSS Exam

**Note:** This key uses strict citation from the provided source files where applicable.

---

### 1. Conceptual Verification (5 pts)

**A. True or False**

1.  **True**
    * *Re-evaluation:* Yes, it **can** be a single point.
    * *However*, usually T/F questions on overdetermined systems check for "always". Let's assume standard "always/never" logic. Actually, looking at `Exercise_LinearAlgebra.pdf`, solvability depends on $b$.
    * *Final decision based on standard linear algebra contexts:* **True**. (An overdetermined system can have a unique solution).

2.  **False**.
    * **Reasoning:** asks about this. Consider $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$. Both are singular ($\det=0$). Their sum $A+B = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ is invertible ($\det=1$). Thus, it is not closed under addition.

3.  **False**.
    * **Reasoning:** Determinant is only defined for square matrices. If $A$ is square and $\det(A)=0$, both rows AND columns are linearly dependent. Row rank equals column rank.

4.  **False**.
    * **Reasoning:** Encryption is $c = m^e \pmod n$. This calculation is always possible regardless of $\gcd(m,n)$. Decryption might fail or be insecure, but encryption works.

5.  **False**.
    * **Reasoning:** Standard counterexample: $R = \{(1,1)\}$ on set $\{1,2\}$.
    * Symmetric? Yes. Transitive? Yes.
    * Reflexive? No, $(2,2)$ is missing.

**B. Abstract Calculation**
* Set $\{u-v, v-w, w-u\}$.
* Check: $c_1(u-v) + c_2(v-w) + c_3(w-u) = 0$
* $u(c_1 - c_3) + v(c_2 - c_1) + w(c_3 - c_2) = 0$
* Since $u,v,w$ are independent, coefficients must be 0:
    1. $c_1 - c_3 = 0 \implies c_1 = c_3$
    2. $c_2 - c_1 = 0 \implies c_2 = c_1$
    3. $c_3 - c_2 = 0 \implies c_3 = c_2$
* Solution: $c_1 = c_2 = c_3 = 1$ is a non-trivial solution.
* **Answer:** **Linearly Dependent**.

---

### 2. Advanced Number Theory (5 pts)

**(a) CRT Application**
* System:
    1. $x \equiv 2 \pmod 3$
    2. $x \equiv 3 \pmod 5$
    3. $x \equiv 2 \pmod 7$
* Observation: Equations (1) and (3) both have remainder 2.
    * $x \equiv 2 \pmod{\text{lcm}(3,7)}$
    * $x \equiv 2 \pmod{21}$
* New System:
    1. $x \equiv 2 \pmod{21} \implies x = 21k + 2$
    2. $x \equiv 3 \pmod 5$
* Substitute: $21k + 2 \equiv 3 \pmod 5$
    * $1k + 2 \equiv 3 \pmod 5$
    * $k \equiv 1 \pmod 5$
* Let $k = 1$.
* $x = 21(1) + 2 = 23$.
* Check: $23 \equiv 2 (3)$, $23 \equiv 3 (5)$, $23 \equiv 2 (7)$.
* **Answer:** $x = 23$.

**(b) RSA Vulnerability**
* A message is dangerous if $\gcd(m, n) = p$.
* $m$ must be a multiple of $p$ ($1p, 2p, \dots$) but not a multiple of $q$ (otherwise $\gcd = n$).
* Total elements in $\mathbb{Z}_n = p \cdot q$.
* Multiples of $p$: $p, 2p, \dots, qp$. There are $q$ such multiples.
* One of them is $n$ (which is $0 \pmod n$), usually excluded or $\gcd=n$.
* Dangerous messages are multiples of $p$ strictly less than $n$. There are $q-1$ such messages.
* Fraction $\approx \frac{q}{pq} = \frac{1}{p}$.
* **Answer:** $\frac{1}{p}$ (or more accurately $\frac{1}{p} + \frac{1}{q}$).identifies $\gcd(m,n)=p$ as dangerous. The estimate is roughly $1/p$ or $1/q$.

---

### 3. Symbolic Determinants & Block Matrices (4 pts)

**(a) Determinant**
Matrix $A$:
$$
\begin{vmatrix}
a & 0 & 0 & b \\
0 & a & b & 0 \\
0 & b & a & 0 \\
b & 0 & 0 & a
\end{vmatrix}
$$
* Laplace Expansion along Row 1:
    $= a \begin{vmatrix} a & b & 0 \\ b & a & 0 \\ 0 & 0 & a \end{vmatrix} - b \begin{vmatrix} 0 & a & b \\ 0 & b & a \\ b & 0 & 0 \end{vmatrix}$
* Term 1: $a [ a(a^2 - 0) ] = a^2(a^2 - b^2)$ ... Wait, middle minor is $\det \begin{pmatrix} a & b \\ b & a \end{pmatrix} \cdot a = (a^2-b^2)a$.
    So Term 1 = $a^2(a^2-b^2)$.
* Term 2: $b [ b(a^2 - b^2) ] = b^2(a^2 - b^2)$.
    *Wait, sign of minor*: Minor for row 1, col 4 is negative? $(-1)^{1+4} = -1$. Correct.
    *Determinant of $\begin{pmatrix} 0 & a & b \\ 0 & b & a \\ b & 0 & 0 \end{pmatrix}$*: Expand along Col 1: $b(a^2 - b^2)$.
    So Term 2 = $-b [ b(a^2 - b^2) ] = -b^2(a^2 - b^2)$.
* Total: $(a^2 - b^2)(a^2 - b^2) = (a^2 - b^2)^2$.
* **Answer:** $(a^2 - b^2)^2$.

**(b) Invertibility**
* Invertible if $\det \neq 0$.
* $(a^2 - b^2)^2 \neq 0 \implies a^2 \neq b^2 \implies a \neq \pm b$.
* **Answer:** $a \neq b$ and $a \neq -b$.

---

### 4. Vector Spaces: Polynomials (4 pts)

**(a) Dependence**
* $p_1 = 1+t$
* $p_2 = 1-t$
* $p_3 = 2$
* Observe: $p_1 + p_2 = (1+t) + (1-t) = 2 = p_3$.
* Linear combination: $p_3 = 1 \cdot p_1 + 1 \cdot p_2$.
* **Answer:** Yes, dependent. $p_3 = p_1 + p_2$.

**(b) Dimension**
* Since $p_3$ is dependent, we remove it.
* $\{p_1, p_2\}$ are linearly independent (one is not a scalar multiple of the other).
* **Answer:** Dimension = 2.

**(c) Membership**
* Is $q(t) = 3 + 4t + t^2$ in $W = \text{span}(1, t)$? (Note: $p_1, p_2$ span polynomials of degree 1).
* $W$ contains only polynomials of degree $\le 1$.
* $q(t)$ has degree 2.
* **Answer:** No.

---

### 5. Linear Maps on Matrix Spaces (4 pts)

**Map:** $T(A) = AB - BA$, with $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.

**(a) Transformation**
Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
* $AB = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} a & 0 \\ c & 0 \end{pmatrix}$.
* $BA = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & b \\ 0 & 0 \end{pmatrix}$.
* $T(A) = AB - BA = \begin{pmatrix} a-a & 0-b \\ c-0 & 0-0 \end{pmatrix} = \begin{pmatrix} 0 & -b \\ c & 0 \end{pmatrix}$.

**(b) Kernel**
* We need $T(A) = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
* $\begin{pmatrix} 0 & -b \\ c & 0 \end{pmatrix} = \mathbf{0} \implies b = 0, c = 0$.
* $a$ and $d$ are free.
* Kernel matrices form: $\begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix}$.
* **Basis:** $\left\{ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \right\}$.

---

### 6. Logic Proofs (4 pts)

**(a) Contraposition**
* **Statement $P \implies Q$:** "If $xy > 100$, then ($x > 10$ or $y > 10$)."
* **Contrapositive $\neg Q \implies \neg P$:** "If ($x \le 10$ and $y \le 10$), then $xy \le 100$."
* **Proof:**
    Assume $x \le 10$ and $y \le 10$.
    Since $x, y$ are positive real numbers, we can multiply inequalities:
    $x \cdot y \le 10 \cdot 10$
    $xy \le 100$.
    [cite_start]This proves the contrapositive, thus the original statement is true. [cite: 32]

**(b) Quantifier Negation**
* **Statement:** $\forall S, \exists P, (\neg \text{Solve}(S, P))$.
* **Negation:** $\neg [\forall S, \exists P, (\neg \text{Solve}(S, P))]$
    $\equiv \exists S, \forall P, \text{Solve}(S, P)$.
* [cite_start]**English:** "There exists a student $S$ who can solve every problem $P$." [cite: 38-44]

---

### 7. Relations & Graphs (4 pts)

Set $A = \{1, 2, 3, 4, 6, 12\}$. Relation: divisibility.

**(a) Hasse Diagram**
* 1 divides everything. (Bottom)
* 2 and 3 are prime in this set (divide by 1).
* 4 divides by 2. 6 divides by 2 and 3.
* 12 divides by 4 and 6.
* **Structure:**
    * 12 is at the top.
    * 4 and 6 are below 12.
    * 2 is below 4 and 6. 3 is below 6.
    * 1 is below 2 and 3.

**(b) Identification**
* **Minimal:** 1 (Nothing divides it except itself).
* **Maximal:** 12 (Divides nothing else).
* **Greatest Element:** 12 (Every element divides 12).