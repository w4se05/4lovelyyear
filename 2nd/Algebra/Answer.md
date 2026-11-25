# Answer Key: VGU Final Exam - Algebra (WS25/26)

**Note to Students:** This key provides the correct answers along with step-by-step explanations. In the actual exam, ensure you show your work clearly to receive full credit.

---

### 1. Binary Choice & Short Calculations (5 pts)

**A. True or False**

1.  **False**
    * **Reasoning:** To form a basis for $\mathbb{R}^3$, three vectors must be linearly independent.
    * Let's check independence: $c_1(1,0,1) + c_2(0,1,0) + c_3(1,1,1) = (0,0,0)$.
    * From the second component: $c_2 + c_3 = 0$.
    * From the first component: $c_1 + c_3 = 0$.
    * From the third component: $c_1 + c_3 = 0$.
    * If we set $c_3 = 1$, then $c_1 = -1$ and $c_2 = -1$.
    * Since non-zero scalars exist (e.g., $(-1, -1, 1)$), the vectors are linearly dependent. Thus, they cannot be a basis.

2.  **False**
    * **Reasoning:** Determinants are multiplicative, not additive. The property is $\det(AB) = \det(A)\det(B)$.
    * **Counterexample:** Let $A = I$ and $B = I$. $\det(A)=1, \det(B)=1$. $A+B = 2I$. $\det(2I) = 2^n \neq 1+1$.

3.  **False**
    * **Reasoning:** An equivalence relation must be Reflexive, Symmetric, and Transitive.
    * Let's check **Symmetry**: If $(1, 2) \in R$ (because $1 \le 2$), is $(2, 1) \in R$? No, because $2 \not\le 1$. Therefore, it is not symmetric.

4.  **True**
    * **Reasoning:** The definition of modular congruence $a \equiv b \pmod n$ is $n | (a-b)$, which implies $a$ and $b$ have the same remainder when divided by $n$.

5.  **True**
    * **Reasoning:** For RSA, the public exponent $e$ must be coprime to $\phi(n)$.
    * $n = 55 = 5 \times 11$.
    * $\phi(55) = (5-1)(11-1) = 4 \times 10 = 40$.
    * Check $\gcd(e, \phi(n)) = \gcd(7, 40)$. Since 7 is prime and does not divide 40, $\gcd(7, 40) = 1$. Thus, it is valid.

**B. Short Calculations**

1.  **Inner Product:**
    * $\vec{u} = (1, -2, 3)$, $\vec{v} = (2, 0, -1)$
    * $\vec{u} \cdot \vec{v} = (1)(2) + (-2)(0) + (3)(-1) = 2 + 0 - 3 = -1$.
    * **Answer:** $-1$.

2.  **Matrix Calculation:**
    * $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \Rightarrow A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
    * $2I_2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$.
    * $A^T - 2I_2 = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} - \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} -1 & 3 \\ 2 & 2 \end{pmatrix}$.
    * **Answer:** $\begin{pmatrix} -1 & 3 \\ 2 & 2 \end{pmatrix}$.

---

### 2. Linear Systems (5 pts)

**(a) Matrices**
* **Coefficient Matrix A:**
    $$A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & \lambda & 2 \\ 1 & 1 & \lambda \end{pmatrix}$$
* **Augmented Matrix:**
    $$\begin{pmatrix} 1 & 1 & 1 & | & 1 \\ 1 & \lambda & 2 & | & 2 \\ 1 & 1 & \lambda & | & 3 \end{pmatrix}$$.

**(b) Determinant & Uniqueness**
* **Calculate $\det(A)$:**
    Using cofactor expansion along the first row:
    $$\det(A) = 1(\lambda^2 - 2) - 1(\lambda - 2) + 1(1 - \lambda)$$
    $$= \lambda^2 - 2 - \lambda + 2 + 1 - \lambda$$
    $$= \lambda^2 - 2\lambda + 1$$
    $$= (\lambda - 1)^2$$
* **Condition for Unique Solution:**
    A system has a unique solution if and only if $\det(A) \neq 0$.
    $(\lambda - 1)^2 \neq 0 \Rightarrow \lambda \neq 1$.
    **Answer:** The system has a unique solution for all $\lambda \in \mathbb{R} \setminus \{1\}$.

**(c) Cramer's Rule ($\lambda = 2$)**
* **Step 1: Calculate Determinant of A ($\det(A)$)**
    Since $\det(A) = (\lambda - 1)^2$ and $\lambda = 2$:
    $\det(A) = (2 - 1)^2 = 1$.
* **Step 2: Calculate Determinant of $A_y$ ($\det(A_y)$)**
    Replace the second column (y-column) with the results vector $b = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$.
    $$A_y = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 3 & 2 \end{pmatrix}$$
    (Note: $\lambda=2$ is substituted into the matrix entries).
    $$\det(A_y) = 1(4 - 6) - 1(2 - 2) + 1(3 - 2)$$
    $$= 1(-2) - 0 + 1(1) = -2 + 1 = -1$$
* **Step 3: Solve for y**
    $$y = \frac{\det(A_y)}{\det(A)} = \frac{-1}{1} = -1$$
    **Answer:** $y = -1$.

---

### 3. Matrix Operations & Subspaces (4 pts)

**Matrix A:**
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ -1 & -2 & 0 & -1 \end{pmatrix}$$

**(a) Row Echelon Form**
1.  $R_2 \leftarrow R_2 - 2R_1$:
    $$\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ -1 & -2 & 0 & -1 \end{pmatrix}$$
2.  $R_3 \leftarrow R_3 + R_1$:
    $$\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
    **Answer:** The matrix is now in Row Echelon Form.

**(b) Rank**
* **Pivot Columns:** Columns 1 and 3 (the columns with leading entries).
* **Rank:** The number of pivots is 2.
    **Answer:** Rank = 2.

**(c) Null Space Basis**
* We solve $Ax = 0$ using the reduced form:
    1.  $x_1 + 2x_2 + x_4 = 0$
    2.  $x_3 + 2x_4 = 0$
* **Free Variables:** $x_2$ and $x_4$ (columns without pivots).
* Express pivot variables in terms of free variables:
    * $x_3 = -2x_4$
    * $x_1 = -2x_2 - x_4$
* **Vector form:**
    $$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = x_2 \begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + x_4 \begin{pmatrix} -1 \\ 0 \\ -2 \\ 1 \end{pmatrix}$$
    **Answer:** Basis = $\left\{ \begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ -2 \\ 1 \end{pmatrix} \right\}$.

---

### 4. Linear Transformations (4 pts)

**Map:** $T(x,y) = (x+y, x-y)$

**(a) Images of Basis Vectors**
* $T(1,0) = (1+0, 1-0) = (1, 1)$
* $T(0,1) = (0+1, 0-1) = (1, -1)$
    **Answer:** $T(e_1) = (1,1), T(e_2) = (1, -1)$.

**(b) Matrix Representation**
* The matrix columns are the images of the basis vectors.
    **Answer:** $M = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

**(c) Pre-image Calculation**
* We need to solve $M\vec{v} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$.
    $$\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$$
* System:
    1.  $x + y = 4$
    2.  $x - y = 2$
* Add equations: $2x = 6 \Rightarrow x = 3$.
* Subtract equations: $2y = 2 \Rightarrow y = 1$.
    **Answer:** $\vec{v} = (3, 1)$.

---

### 5. Propositional Logic (4 pts)

**(a) Truth Table**
Formula: $\neg p \wedge (p \Rightarrow q)$

| p | q | $\neg p$ | $p \Rightarrow q$ | $\neg p \wedge (p \Rightarrow q)$ |
| :---: | :---: | :---: | :---: | :---: |
| T | T | F | T | **F** |
| T | F | F | F | **F** |
| F | T | T | T | **T** |
| F | F | T | T | **T** |


**(b) Logical Equivalence**
Expression: $\neg(p \vee q) \vee (\neg p \wedge q)$
1.  **De Morgan's Law:** $\neg(p \vee q) \equiv \neg p \wedge \neg q$.
2.  Substitute back: $(\neg p \wedge \neg q) \vee (\neg p \wedge q)$.
3.  **Distributive Law:** Pull out $\neg p$:
    $\neg p \wedge (\neg q \vee q)$.
4.  **Inverse Law:** $(\neg q \vee q)$ is always True (T).
5.  **Identity Law:** $\neg p \wedge T \equiv \neg p$.
    **Proof Complete**.

**(c) Negation**
* **Original:** "If it rains today, I will not go to the park." ($P \Rightarrow Q$)
* **Structure:** $P \Rightarrow Q \equiv \neg P \vee Q$.
* **Negation:** $\neg (\neg P \vee Q) \equiv P \wedge \neg Q$.
* **English:** "It rains today **and** I will go to the park."
    **Answer:** It rains today and I will go to the park.

---

### 6. Relations (4 pts)

**Set:** $A = \{1, 2, 3, 4\}$
**Relation:** $R = \{(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)\}$

**(a) Matrix Representation**
Rows/Cols correspond to 1, 2, 3, 4.
$$M_R = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$
.

**(b) Properties**
* **Reflexive:** **Yes**.
    * *Reason:* Every diagonal element $(1,1), (2,2), (3,3), (4,4)$ is present.
* **Symmetric:** **Yes**.
    * *Reason:* The matrix is symmetric ($M_R^T = M_R$). Specifically, $(1,2)$ is in R and $(2,1)$ is in R.
* **Transitive:** **Yes**.
    * *Justification:* The only non-trivial transitions are between 1 and 2.
    * $(1,2)$ and $(2,1)$ are in R $\Rightarrow (1,1)$ must be in R (It is).
    * $(2,1)$ and $(1,2)$ are in R $\Rightarrow (2,2)$ must be in R (It is).
    * All other elements interact only with themselves.

**(c) Equivalence & Partition**
* **Is it an equivalence relation?** Yes (since it satisfies all 3 properties above).
* **Partition:** We group elements that are related to each other.
    * 1 is related to 1 and 2.
    * 2 is related to 1 and 2.
    * 3 is only related to 3.
    * 4 is only related to 4.
    **Answer:** Partition = $\{\{1, 2\}, \{3\}, \{4\}\}$.

---

### 7. RSA Encryption (4 pts)

**Parameters:** $n = 33$ ($p=3, q=11$)

**(a) Euler's Totient $\phi(n)$**
* Formula: $\phi(n) = (p-1)(q-1)$.
* Calculation: $(3-1)(11-1) = 2 \times 10 = 20$.
    **Answer:** $\phi(n) = 20$.

**(b) Validity of $e=3$**
* Requirement: $\gcd(e, \phi(n)) = 1$.
* Check: $\gcd(3, 20) = 1$.
* **Answer:** Yes, it is valid because 3 and 20 are coprime.

**(c) Finding Private Key $d$ (for $e=7$)**
* Equation: $d \cdot e \equiv 1 \pmod{\phi(n)} \Rightarrow 7d \equiv 1 \pmod{20}$.
* **Extended Euclidean Algorithm:**
    * $20 = 2(7) + 6$
    * $7 = 1(6) + 1$
* **Back Substitution:**
    * $1 = 7 - 1(6)$
    * $1 = 7 - 1(20 - 2(7))$
    * $1 = 7 - 1(20) + 2(7)$
    * $1 = 3(7) - 1(20)$
* Thus, $3(7) \equiv 1 \pmod{20}$.
* $d = 3$.
    **Answer:** $d = 3$.

**(d) Encryption**
* Message $m = 2$, Public Key $(33, 7)$.
* Formula: $c = m^e \pmod n$.
* Calculation: $c = 2^7 \pmod{33}$.
    * $2^5 = 32 \equiv -1 \pmod{33}$.
    * $2^7 = 2^5 \times 2^2 = (-1) \times 4 = -4$.
    * $-4 \equiv 29 \pmod{33}$.
    **Answer:** $c = 29$.