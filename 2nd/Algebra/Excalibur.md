### 1. Binary Choice & Complex Calculations (5 pts)

**A. True or False**

1.  **True**
    * **Explanation:** Let $b_1$ and $b_3$ be columns 1 and 3 of matrix $B$. We are given $b_1 = b_3$.
    * The columns of $AB$ are $A b_1$ and $A b_3$.
    * Since $b_1 = b_3$, it follows that $A b_1 = A b_3$. Thus, the columns are identical.

2.  **True**
    * **Explanation:** We need a matrix $A$ such that $A^2 = -I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$.
    * Consider the rotation matrix by $90^\circ$: $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
    * Calculation: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$.

3.  **True**
    * **Explanation:** This is a standard property of Mersenne numbers. Proof by contraposition: If $n$ is composite ($n=ab$), then $2^n - 1 = (2^a)^b - 1$, which is divisible by $2^a - 1$. Thus, for $2^n-1$ to be prime, $n$ must be prime.

4.  **False**
    * **Counterexample:** Let $A = I$ (Identity) and $B = -I$. Both are invertible.
    * $A+B = I + (-I) = 0$ (Zero matrix), which is **not** invertible.

5.  **True**
    * **Explanation:** Let $m = 2k+1$ and $n = 2j+1$.
    * $m \cdot n = (2k+1)(2j+1) = 4kj + 2k + 2j + 1 = 2(2kj + k + j) + 1$.
    * The result is in the form $2x+1$, so it is odd.

**B. Advanced Calculations**

1.  **Last Digit Calculation:**
    * We need the sum modulo 10.
    * The terms are $a_1=1, a_2=11, a_3=111, \dots, a_{100}=\underbrace{11\dots1}_{100}$.
    * For every term $a_k$, the last digit is $1$.
    * Therefore, $a_k \equiv 1 \pmod{10}$.
    * Consequently, $(a_k)^{10} \equiv 1^{10} \equiv 1 \pmod{10}$.
    * Sum $S \equiv \sum_{k=1}^{100} 1 \pmod{10} \equiv 100 \pmod{10} \equiv 0$.
    * **Answer:** 0.

2.  **Modular Power:**
    * We calculate $2^{2016} \pmod 9$.
    * Euler's Totient Theorem: $a^{\phi(n)} \equiv 1 \pmod n$ if $\gcd(a,n)=1$.
    * $\phi(9) = 9(1 - 1/3) = 6$.
    * Exponent reduction: $2016 \pmod 6$. Since $2016 = 6 \times 336$, the remainder is $0$.
    * Thus, $2^{2016} \equiv 2^0 \pmod 9 \equiv 1$.
    * **Answer:** 1.

---

### 2. Linear Systems with Parameters (5 pts)

**Augmented Matrix Reduction:**
$$
\begin{pmatrix} 1 & 2 & -3 & | & 4 \\ 3 & -1 & 5 & | & 2 \\ 4 & 1 & a^2-14 & | & a+2 \end{pmatrix}
$$
1. $R_2 \leftarrow R_2 - 3R_1$: $\begin{pmatrix} 0 & -7 & 14 & | & -10 \end{pmatrix}$
2. $R_3 \leftarrow R_3 - 4R_1$: $\begin{pmatrix} 0 & -7 & a^2-2 & | & a-14 \end{pmatrix}$
3. $R_3 \leftarrow R_3 - R_2$: $\begin{pmatrix} 0 & 0 & (a^2-2)-14 & | & (a-14)-(-10) \end{pmatrix}$
   $$\Rightarrow \begin{pmatrix} 0 & 0 & a^2-16 & | & a-4 \end{pmatrix}$$

**Analysis of Pivot Equation:** $(a^2 - 16)z = a - 4$
Factorized: $(a-4)(a+4)z = a-4$

**(a) No Solution:**
* Condition: LHS $= 0$ and RHS $\neq 0$.
* $a^2 - 16 = 0 \implies a = 4$ or $a = -4$.
* If $a = -4$: LHS $= 0$, RHS $= -8$. ($0 \neq -8$, Inconsistent).
* **Answer:** $a = -4$.

**(b) Exactly One Solution:**
* Condition: Pivot is non-zero (LHS $\neq 0$).
* $a^2 - 16 \neq 0 \implies a \neq 4$ and $a \neq -4$.
* **Answer:** $a \in \mathbb{R} \setminus \{4, -4\}$.

**(c) Infinitely Many Solutions:**
* Condition: LHS $= 0$ and RHS $= 0$ (Free variable).
* If $a = 4$: LHS $= 0$, RHS $= 0$.
* **Answer:** $a = 4$.

---

### 3. Subspaces & Orthogonality (4 pts)

**(a) Finding the Basis:**
* We search for vectors $\vec{x} = (x_1, x_2, x_3, x_4)$ such that $\vec{x} \cdot \vec{u} = 0$ and $\vec{x} \cdot \vec{v} = 0$.
* System of equations:
  1. $x_1 + x_2 + 0x_3 + x_4 = 0$
  2. $x_1 + 0x_2 + x_3 + x_4 = 0$
* Subtract (2) from (1): $x_2 - x_3 = 0 \implies x_2 = x_3$.
* Substitute into (1): $x_1 = -x_2 - x_4$.
* Free variables: $x_2$ and $x_4$. Let $x_2 = s, x_4 = t$.
* Vector form: $\begin{pmatrix} -s-t \\ s \\ s \\ t \end{pmatrix} = s\begin{pmatrix} -1 \\ 1 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} -1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$.
* **Answer:** Basis = $\left\{ \begin{pmatrix} -1 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right\}$.

**(b) Dimension:**
* Since the basis contains 2 vectors, the dimension is 2.
* **Answer:** 2.

---

### 4. Abstract Linear Maps (4 pts)

**(a) Proof of Linearity:**
* To prove linearity, we must show $L(cA + B) = cL(A) + L(B)$.
* $L(cA + B) = \frac{(cA+B) - (cA+B)^T}{2}$
* $= \frac{cA + B - cA^T - B^T}{2}$ (Transposition is linear)
* $= c \frac{A - A^T}{2} + \frac{B - B^T}{2}$
* $= cL(A) + L(B)$. Q.E.D..

**(b) Kernel:**
* $\text{Ker}(L) = \{ A \in M_{n \times n} \mid L(A) = 0 \}$.
* $\frac{A - A^T}{2} = 0 \implies A - A^T = 0 \implies A = A^T$.
* **Answer:** The kernel consists of all **Symmetric Matrices**.

**(c) Image:**
* Let $Y = L(A) = \frac{A - A^T}{2}$.
* Check transpose of image: $Y^T = (\frac{A - A^T}{2})^T = \frac{A^T - A}{2} = - \frac{A - A^T}{2} = -Y$.
* **Answer:** The image consists of all **Skew-Symmetric Matrices**.

---

### 5. Logical Validity (4 pts)

**Variables:**
* $J$: Joe affords it.
* $S$: Joe asks Sally.
* $B$: Bill pays Joe.

**Premises:**
1. $J \Rightarrow S$
2. $B \Rightarrow J$
3. $\neg S$

**Goal:** Prove $\neg B$.

**Derivation:**
1. From Premise 1 ($J \Rightarrow S$) and Premise 3 ($\neg S$), we apply **Modus Tollens**:
   $\neg S \wedge (J \Rightarrow S) \implies \neg J$. (Joe cannot afford it).
2. From Premise 2 ($B \Rightarrow J$) and the derived fact ($\neg J$), we apply **Modus Tollens** again:
   $\neg J \wedge (B \Rightarrow J) \implies \neg B$.
3. **Conclusion:** Bill did not pay Joe.
* **Answer:** The argument is **Valid**.

---

### 6. Closures of Relations (4 pts)

Relation $R = \{(1,2), (2,1), (2,3), (3,4), (4,1)\}$.

**(a) Reflexive Closure:**
* Add all $(a,a)$ pairs.
* **Answer:** $R \cup \{(1,1), (2,2), (3,3), (4,4)\}$.

**(b) Symmetric Closure:**
* Add inverse pairs for any missing directions.
* Current inverses needed: $(3,2)$ for $(2,3)$, $(4,3)$ for $(3,4)$, $(1,4)$ for $(4,1)$. $((1,2)$ and $(2,1)$ already exist).
* **Answer:** $R \cup \{(3,2), (4,3), (1,4)\}$.

**(c) Transitive Closure:**
* Observe the cycle: $1 \to 2 \to 3 \to 4 \to 1$.
* Since all elements $\{1, 2, 3, 4\}$ are part of a strongly connected cycle, every element can reach every other element.
* For example: $1 \to 2 \to 3$ implies $(1,3)$. $1 \to 2 \to 3 \to 4$ implies $(1,4)$, etc.
* **Answer:** The transitive closure is the **Universal Relation** (all 16 pairs in $A \times A$).

---

### 7. Number Theory & Turing's Cipher (4 pts)

**(a) Modular Equation:**
* $5x \equiv 8 \pmod{11}$.
* Find inverse of $5 \pmod{11}$:
  * $5 \times 9 = 45 = 4 \times 11 + 1$.
  * The inverse is $9$.
* Multiply both sides by 9:
  * $x \equiv 8 \times 9 \pmod{11}$
  * $x \equiv 72 \pmod{11}$
  * $72 = 6 \times 11 + 6 \implies x \equiv 6$.
* **Answer:** $x = 6$.

**(b) Turing's Cipher (Multiplicative Cipher):**
**Modulus:** $n=30$.

1.  **Smallest non-trivial valid private key:**
    * A valid key $k$ must satisfy $\gcd(k, 30) = 1$.
    * $30 = 2 \times 3 \times 5$.
    * Check integers $>1$:
      * 2 (divides 30) - No.
      * 3 (divides 30) - No.
      * 4 (divisible by 2) - No.
      * 5 (divides 30) - No.
      * 6 (divisible by 2) - No.
      * 7 (prime, not factor of 30) - **Yes**.
    * **Answer:** Key $e = 7$.

2.  **Decrypt $y=19$:**
    * We need to solve $x \cdot e \equiv y \pmod{30}$, so $x \cdot 7 \equiv 19 \pmod{30}$.
    * Find inverse of $7 \pmod{30}$ using Extended Euclidean:
      * $30 = 4(7) + 2$
      * $7 = 3(2) + 1 \implies 1 = 7 - 3(2)$
      * Substitute 2: $1 = 7 - 3(30 - 4(7)) = 13(7) - 3(30)$.
      * Inverse is $13$.
    * Calculate $x$:
      * $x \equiv 19 \times 13 \pmod{30}$
      * $19 \times 13 = 247$
      * $247 \div 30 = 8$ remainder $7$ ($240 + 7$).
    * **Answer:** Decrypted message $x = 7$.