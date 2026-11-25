### 1. Binary Choice & Complex Calculations (5 pts)

**A. True or False** Evaluate the following assertions. Circle **t** (true) or **f** (false).
*(Scoring: +1 for correct, -1 for false, 0 for no answer)*

1.  **[ t / f ]** If columns 1 and 3 of matrix $B$ are the same, then columns 1 and 3 of $AB$ are also the same.
2.  **[ t / f ]** There exists a $2 \times 2$ matrix $A$ with real entries such that $A^2 = -I$.
3.  **[ t / f ]** If $2^n - 1$ is prime, then $n$ is prime.
4.  **[ t / f ]** If $A$ and $B$ are invertible matrices, then $A+B$ is always invertible.
5.  **[ t / f ]** The product of two odd integers is odd.

**B. Advanced Calculations**

1.  Find the **last digit** of the following sum:
    $S = 1 + 11^{10} + 111^{10} + \dots + \underbrace{11\dots1}_{100 \text{ times}}$.
    __________________________________________________________________

2.  Compute the value: $2^{2016} \pmod 9$.
    __________________________________________________________________

---

### 2. Linear Systems with Parameters (5 pts)

Consider the system of equations with parameter $a \in \mathbb{R}$:

$$
\begin{cases}
x + 2y - 3z = 4 \\
3x - y + 5z = 2 \\
4x + y + (a^2 - 14)z = a + 2
\end{cases}
$$

**(a)** Determine the values of $a$ for which the system has **no solution*



**(b)** Determine the values of $a$ for which the system has **exactly one solution**.



**(c)** Determine the values of $a$ for which the system has **infinitely many solutions**.



---

### 3. Subspaces & Orthogonality (4 pts)

Consider the vector space $\mathbb{R}^4$.

**(a)** Find a basis for the subspace of all vectors that are **perpendicular** (orthogonal) to both $\vec{u} = (1, 1, 0, 1)$ and $\vec{v} = (1, 0, 1, 1)$.




**(b)** Find the dimension of the subspace found in part (a).



---

### 4. Abstract Linear Maps (4 pts)

Let $L: M_{n \times n} \rightarrow M_{n \times n}$ be a map defined by $L(A) = \frac{A - A^T}{2}$.

**(a)** Prove that $L$ is a **linear map**.



**(b)** Describe the **Kernel** (Null Space) of $L$. What specific type of matrices are in the kernel?



**(c)** Describe the **Image** (Range) of $L$.



---

### 5. Logical Validity (4 pts)

Determine the validity of the following argument using a truth table or formal logical derivation :

1.  If Joe can afford it, he will ask Sally to go out on a date.
2.  If Bill pays Joe the money he owes him, then Joe can afford to go out on a date.
3.  Joe does **not** ask Sally to go out on a date.
4.  **Therefore:** Bill did **not** pay Joe the money he owes him.





---

### 6. Closures of Relations (4 pts)

Given the relation $R = \{(1,2), (2,1), (2,3), (3,4), (4,1)\}$ on the set $A = \{1, 2, 3, 4\}$.

**(a)** Find the **Reflexive Closure** of $R$.



**(b)** Find the **Symmetric Closure** of $R$.



**(c)** Find the **Transitive Closure** of $R$ (You may use Warshall’s algorithm or logical deduction).



---

### 7. Number Theory & Turing's Cipher (4 pts)

**(a)** Solve the equation for $x$ in $\mathbb{Z}_{11}$:
    $$5 \cdot_{11} x = 8$$
    .



**(b)** In Turing's Cipher (Version 2), given the modulus $n = 30$:
    1.  Find the **non-trivial smallest valid private key**.
    2.  **Decrypt** the message $y = 19$.


