## I. Conceptual Section (Teach Mode)

### 1. Basic Notions & Divisibility
Number theory primarily deals with the integers, denoted by $\mathbb{Z}$.

> [!Definition] Divisibility
> Let $a, b \in \mathbb{Z}$ with $a \neq 0$. We say **$a$ divides $b$** (denoted $a \mid b$) if there exists an integer $m$ such that:
> $$b = m \cdot a$$
> * $b$ is a **multiple** of $a$.
> * $a$ is a **factor** or **divisor** of $b$.

> [!Theorem] The Division Algorithm
> Given $a, b \in \mathbb{Z}$ with $a > 0$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that:
> $$b = a \cdot q + r, \quad 0 \leq r < a$$
> * **Notation:** $q = b \text{ div } a$ and $r = b \mod a$.

### 2. Primes and GCD

> [!Definition] Prime & Composite
> An integer $p > 1$ is **prime** if its only positive divisors are $1$ and $p$. Otherwise, it is **composite**.

> [!Theorem] Fundamental Theorem of Arithmetic
> Every integer $n > 1$ can be represented **uniquely** as a product of prime powers:
> $$n = p_1^{e_1} p_2^{e_2} \dots p_k^{e_k}$$
> * Note: Prime factorization is computationally hard (NP-hard), which forms the basis of RSA cryptography.

> [!Definition] GCD and LCM
> * **Greatest Common Divisor (GCD):** $\gcd(a, b)$ is the largest integer $d$ such that $d \mid a$ and $d \mid b$.
> * **Least Common Multiple (LCM):** $\text{lcm}(a, b)$ is the smallest positive integer $m$ such that $a \mid m$ and $b \mid m$.
> * **Relation:** $\gcd(a,b) \cdot \text{lcm}(a,b) = |a \cdot b|$.

### 3. Euclidean Algorithms

> [!Algorithm] Euclidean Algorithm (EA)
> To find $\gcd(r_0, r_1)$:
> 1.  Apply successive division: $r_{i-2} = q_{i-1} r_{i-1} + r_i$
> 2.  Stop when the remainder is $0$. The last non-zero remainder is the GCD.
> 3.  Complexity: $O(\log(\min(a,b)))$.

> [!Theorem] Bezout's Identity
> For any integers $a, b$, there exist integers $s, t$ such that:
> $$\gcd(a, b) = s \cdot a + t \cdot b$$
> These coefficients $s, t$ are found using the **Extended Euclidean Algorithm (EEA)**.

> [!ABSTRACT] Algorithm: Extended Euclidean Algorithm (EEA)
> 
> To find $s$ and $t$, we run the Euclidean algorithm while maintaining two sequences $s_i$ and $t_i$.
> 
> We set initial values:
> 
> - $s_0 = 1, s_1 = 0$
>     
> - $t_0 = 0, t_1 = 1$
>     
> 
> For each step $i \geq 2$, calculate the quotient $q_i$ and update:
> 
> $$s_i = s_{i-2} - q_i \cdot s_{i-1}$$
> 
> $$t_i = t_{i-2} - q_i \cdot t_{i-1}$$
> 
> At the end, $\gcd(a, b) = s_k a + t_k b$.

---

### Modular Arithmetic

> [!INFO] Definition: Arithmetic Modulo $n$
> 
> Let $Z_n = \{0, 1, \dots, n-1\}$ be the set of all possible remainders when dividing a number by $n$.
> 
> We define operations on $Z_n$:
> * **Addition:** $i +_n j = (i + j) \mod n$
> * **Multiplication:** $i \cdot_n j = (i \cdot j) \mod n$

> [!Property] Modular Arithmetic Operations
> * $(a + b) \mod n = ((a \mod n) + (b \mod n)) \mod n$
> * $(a \cdot b) \mod n = ((a \mod n) \cdot (b \mod n)) \mod n$
> * $a^m \mod n = ((a \mod n)^m) \mod n$

---
### Modular Inverses & Linear Congruences

Solving equations in modular arithmetic requires the concept of an inverse, analogous to $1/a$ in real numbers.

> [!INFO] Definition: Modular Inverse
> 
> An integer $\bar{a}$ is the modular multiplicative inverse of $a$ modulo $n$ if:
> 
> $$a\bar{a} \equiv 1 \pmod n$$
> 
> **Condition:** The inverse $a^{-1}$ exists **if and only if** $\gcd(a, n) = 1$ (i.e., $a$ and $n$ are coprime).

> [!NOTE] Groups and Multiplicative Inverses
> 
> * $(Z_n, +_n)$ forms a **group**.
> * $(Z_n, \cdot_n)$ is **not** a group because $0$ is not invertible.
> * **Multiplicative Group $Z_n^\times$**: The set of invertible elements in $Z_n$. An element $a$ is invertible iff $\gcd(n, a) = 1$.
> * **Inverse:** If $a \in Z_n^\times$, there exists a unique $a^{-1}$ such that $a \cdot_n a^{-1} = 1$.

> [!NOTE] Properties of Congruence
> 
> 1. **Reflexive:** $a \equiv a \pmod n$
>     
> 2. **Symmetric:** If $a \equiv b \pmod n$, then $b \equiv a \pmod n$
>     
> 3. **Transitive:** If $a \equiv b \pmod n$ and $b \equiv c \pmod n$, then $a \equiv c \pmod n$
>     
> 4. **Arithmetic Preservation:** If $a \equiv b \pmod n$ and $c \equiv d \pmod n$:
>     
>     - $a + c \equiv b + d \pmod n$
>         
>     - $ac \equiv bd \pmod n$
      
To find the inverse, we use the EEA to solve $ax + ny = 1$. Then $ax \equiv 1 \pmod n$, so the coefficient $x$ is the inverse.

> [!TIP] Theorem: Solving Linear Congruences
> 
> To solve $ax \equiv b \pmod n$:
> 
> 1. Calculate $d = \gcd(a, n)$.
>     
> 2. **Check Solubility:**
>     
>     - If $d \nmid b$: **No solution**.
>         
>     - If $d \mid b$: There are exactly $d$ distinct solutions modulo $n$.
>         
> 3. **Method:**
>     
>     - Reduce the equation by dividing $a, b, n$ by $d$.
>         
>     - Find the inverse of the reduced $a'$.
>         
>     - Multiply through to isolate $x$.
>         

---
### 5. Euler's Totient & Important Theorems

>[!Definition] 
>Let $a,b \in Z$
>We say that $a$ & $b$ are *co-prime* or *relatively prime* if 
>$$gcd(a,b)=1$$

> [!Definition] Euler's Totient Function $\phi(n)$
> $\phi(n)$ is the count of positive integers less than $n$ that are relatively prime to $n$.
> * If $p$ is prime: $\phi(p) = p - 1$.
> * If $n = p \cdot q$ (distinct primes): $\phi(n) = (p-1)(q-1)$.
> * General formula: $\phi(n) = n \prod_{p|n} (1 - \frac{1}{p})$.
> 
>If $\gcd(a, n) = 1$, then:
> $$a^{\phi(n)} \equiv 1 \pmod n$$
> where $\phi(n)$ is **Euler's totient function** (the number of positive integers $\le n$ relatively prime to $n$).

> [!Theorem] Key Theorems
> 1.  **Fermat's Little Theorem:** If $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod p$.
> 2.  **Euler's Theorem:** If $\gcd(a, n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod n$.

### 6. Cryptography
### 6.1. Classical & Block Ciphers

> [!Concept] Shift & Affine Ciphers
> * **Caesar:** $E(x) = (x + k) \pmod{26}$.
> * **Affine:** $E(x) = (ax + b) \pmod n$.
>   * **Requirement:** $\gcd(a, n) = 1$.
>   * **Decryption:** $D(y) = a^{-1}(y - b) \pmod n$.

> [!Concept] Turing's Ciphers (from Course Exercises)
> * **Version 1 (Prime Product):** $y = m \cdot k$.
>   * **Attack:** If you have two ciphertexts $y_1, y_2$ encrypted with the same key $k$, then $k = \gcd(y_1, y_2)$.
> * **Version 2 (Multiplicative Modulo):** $y = x \cdot e \pmod n$.
>   * **Requirement:** $\gcd(e, n) = 1$.
>   * **Decryption:** $x = y \cdot e^{-1} \pmod n$.

> [!Concept] Transposition Cipher
> Encrypts by rearranging the *positions* of the plaintext within a block of size $L$.
> * **Key:** A permutation $\sigma$ of $\{1, \dots, L\}$.
> * **Encryption:** The character at plaintext position $i$ moves to ciphertext position $\sigma(i)$.
> * **Decryption:** Requires the **inverse permutation** $\sigma^{-1}$.
>   * If $\sigma(i) = j$, then $\sigma^{-1}(j) = i$.
>   * To decrypt, place the character from ciphertext position $j$ back into plaintext position $\sigma^{-1}(j)$.

### 6.2. Error Detection & Public Key Crypto

> [!Fact] ISBN-10 Check Digit
> A 10-digit ISBN $x_1 x_2 \dots x_{10}$ is valid if:
> $$\sum_{i=1}^{10} (11-i)x_i \equiv 0 \pmod{11}$$
> * The weights descend from 10 down to 1.
> * The character 'X' represents the value 10.

> [!Algorithm] RSA Cryptosystem
> * **Setup:**
>     1. Choose primes $p, q$. Compute $n = pq$.
>     2. Compute $\phi(n) = (p-1)(q-1)$.
>     3. Choose public $e$ such that $\gcd(e, \phi(n)) = 1$.
>     4. Calculate private $d$ such that $d \cdot e \equiv 1 \pmod{\phi(n)}$.
> * **Encryption:** $y = x^e \pmod n$.
> * **Decryption:** $x = y^d \pmod n$.
> * **Dangerous Messages:** If a message $m$ shares a factor with $n$ (i.e., $\gcd(m, n) = p$ or $q$), the system is broken.

> [!Concept] Diffie-Hellman Key Exchange
> A method for two parties to agree on a secret key over an insecure channel.
> 1.  **Public:** Prime $p$, generator $q$.
> 2.  **Private:** Alice has $a$, Bob has $b$.
> 3.  **Exchange:** Alice sends $A = q^a \pmod p$. Bob sends $B = q^b \pmod p$.
> 4.  **Secret:** Shared key $K = B^a = A^b = q^{ab} \pmod p$.
> * **Security:** Relies on the **Discrete Logarithm Problem** (it is hard to find $a$ given only $q^a$ and $p$).

---
### Example 1: Extended Euclidean Algorithm

_(Using: Euclidean Algorithm, Bézout's Identity)_

**Problem:** Find $d = \gcd(240, 46)$ and integers $x, y$ such that $240x + 46y = d$.

**Solution:**

**Step 1: Standard Euclidean Algorithm (Forward Pass)**

$$\begin{aligned} 240 &= 46(5) + 10 \\ 46 &= 10(4) + 6 \\ 10 &= 6(1) + 4 \\ 6 &= 4(1) + 2 \\ 4 &= 2(2) + 0 \end{aligned}$$

The last non-zero remainder is **2**. Thus, $\gcd(240, 46) = 2$.

Step 2: Back-Substitution (Finding $x, y$)

Express the remainder 2 in terms of previous remainders:

$$\begin{aligned} 2 &= 6 - 4(1) \\ &\quad \text{(Substitute } 4 = 10 - 6(1) \text{)} \\ 2 &= 6 - (10 - 6(1))(1) \\ 2 &= 6(2) - 10(1) \\ &\quad \text{(Substitute } 6 = 46 - 10(4) \text{)} \\ 2 &= (46 - 10(4))(2) - 10(1) \\ 2 &= 46(2) - 10(8) - 10(1) \\ 2 &= 46(2) - 10(9) \\ &\quad \text{(Substitute } 10 = 240 - 46(5) \text{)} \\ 2 &= 46(2) - (240 - 46(5))(9) \\ 2 &= 46(2) - 240(9) + 46(45) \\ 2 &= 240(-9) + 46(47) \end{aligned}$$

Result:

$$x = -9, \quad y = 47$$

$$240(-9) + 46(47) = -2160 + 2162 = 2 \quad \checkmark$$

---

### Example 2: Finding a Modular Inverse

_(Using: EEA, Coprimality)_

**Problem:** Find the inverse of $67$ modulo $119$, i.e., solve $67x \equiv 1 \pmod{119}$.

Solution:

We need to find $x, y$ such that $67x + 119y = \gcd(67, 119)$. If GCD is 1, the inverse exists.

Table Method for EEA:

$a = 119, b = 67$.

|   Step   | Quotient ($q$)    | Remainder ($r$) | $s$ (coeff of 119)        | $t$ (coeff of 67)         |
| :------: | :---------------- | :-------------: | :------------------------ | :------------------------ |
| **Init** | -                 |       119       | $1$                       | $0$                       |
| **Init** | -t                |       67        | $0$                       | $1$                       |
|  **1**   | $119 \div 67 = 1$ |       52        | $1 - 1(0) = \mathbf{1}$   | $0 - 1(1) = \mathbf{-1}$  |
|  **2**   | $67 \div 52 = 1$  |       15        | $0 - 1(1) = \mathbf{-1}$  | $1 - 1(-1) = \mathbf{2}$  |
|  **3**   | $52 \div 15 = 3$  |        7        | $1 - 3(-1) = \mathbf{4}$  | $-1 - 3(2) = \mathbf{-7}$ |
|  **4**   | $15 \div 7 = 2$   |        1        | $-1 - 2(4) = \mathbf{-9}$ | $2 - 2(-7) = \mathbf{16}$ |

Since remainder is 1, $\gcd(67, 119)=1$.

The equation is: $119(-9) + 67(16) = 1$.

Taking this modulo 119:

$$\begin{aligned} 119(-9) + 67(16) &\equiv 1 \pmod{119} \\ 0 + 67(16) &\equiv 1 \pmod{119} \end{aligned}$$

Result:

The inverse is 16.

---

### Example 3: Solving Linear Congruence

_(Using: Solubility Check, Modular Inverse)_

**Problem:** Solve $15x \equiv 12 \pmod{21}$.


**Solution:**

1. Check Solubility:

Calculate $d = \gcd(15, 21)$.

$$21 = 15(1) + 6$$

$$15 = 6(2) + 3$$

$$6 = 3(2) + 0 \implies d = 3$$

Therefore, there are $d=3$ distinct solutions modulo 21.

2. Reduce the Equation:

Divide the entire equation (including modulus) by $d=3$:

$$\begin{aligned} \frac{15x}{3} &\equiv \frac{12}{3} \pmod{\frac{21}{3}} \\ 5x &\equiv 4 \pmod 7 \end{aligned}$$

3. Solve Reduced Equation:

Find $5^{-1} \pmod 7$.

By inspection: $5 \times 3 = 15 \equiv 1 \pmod 7$.

So, inverse is 3.

Multiply reduced equation by 3:

$$\begin{aligned} 3(5x) &\equiv 3(4) \pmod 7 \\ x &\equiv 12 \pmod 7 \\ x &\equiv 5 \pmod 7 \end{aligned}$$

4. Find All Solutions:

The solutions modulo 21 are given by $x = x_0 + k \cdot \frac{n}{d}$ for $k = 0, 1, 2$.

Base solution $x_0 = 5$. Step size $= \frac{21}{3} = 7$.

- $k=0: x = 5$
    
- $k=1: x = 5 + 7 = 12$
    
- $k=2: x = 5 + 14 = 19$
    

Result:

$$x \in \{5, 12, 19\} \pmod{21}$$

---

## II. Application Section (Exam Mode)

### 📘 Examples & Applications

#### Example 1: Extended Euclidean Algorithm
**(Using: Euclidean Algorithm, Bezout's Identity)**
Find $\gcd(973, 301)$ and express it as $s \cdot 973 + t \cdot 301$.

**Solution:**
1.  **Forward Pass (Euclidean Algo):**
    $$973 = 3 \cdot 301 + 70$$
    $$301 = 4 \cdot 70 + 21$$
    $$70 = 3 \cdot 21 + 7$$
    $$21 = 3 \cdot 7 + 0$$
    $\implies \gcd(973, 301) = 7$.

2.  **Backward Pass (Substitution):**
    $$7 = 70 - 3(21)$$
    Substitute $21 = 301 - 4(70)$:
    $$7 = 70 - 3(301 - 4 \cdot 70) = 70 - 3 \cdot 301 + 12 \cdot 70 = 13 \cdot 70 - 3 \cdot 301$$
    Substitute $70 = 973 - 3 \cdot 301$:
    $$7 = 13(973 - 3 \cdot 301) - 3 \cdot 301$$
    $$7 = 13 \cdot 973 - 39 \cdot 301 - 3 \cdot 301$$
    $$7 = 13 \cdot 973 - 42 \cdot 301$$
    
    Thus, $s = 13, t = -42$.

#### Example 2: Finding Multiplicative Inverse
**(Using: Modular Arithmetic, EEA)**
Find $4^{-1} \pmod 9$.

**Solution:**
We need $x$ such that $4x \equiv 1 \pmod 9$. This is equivalent to finding $4x + 9y = 1$.
Using EEA on 9 and 4:
$$9 = 2 \cdot 4 + 1$$
$$1 = 9 - 2 \cdot 4$$
Taking mod 9:
$$1 \equiv -2 \cdot 4 \pmod 9$$
$$1 \equiv 7 \cdot 4 \pmod 9$$
Thus, $4^{-1} \equiv -2 \equiv 7 \pmod 9$.

#### Example 3: RSA Encryption/Decryption
**(Using: RSA Algorithm, Fast Exponentiation)**
Let $p=7, q=11$. Choose public key $e=7$.
1.  Find $n$ and $\phi(n)$.
2.  Find private key $d$.
3.  Encrypt message $M=5$.

**Solution:**
1.  $n = p \cdot q = 77$.
    $\phi(n) = (7-1)(11-1) = 6 \cdot 10 = 60$.
2.  Find $d$ such that $e \cdot d \equiv 1 \pmod{60}$, i.e., $7d \equiv 1 \pmod{60}$.
    Using EEA: $60 = 8 \cdot 7 + 4 \to 7 = 1 \cdot 4 + 3 \to 4 = 1 \cdot 3 + 1$.
    Back substitute:
    $1 = 4 - 3 = 4 - (7 - 4) = 2 \cdot 4 - 7 = 2(60 - 8 \cdot 7) - 7 = 2 \cdot 60 - 17 \cdot 7$.
    So, $-17 \cdot 7 \equiv 1 \pmod{60}$.
    $d \equiv -17 \equiv 43 \pmod{60}$.
3.  Encrypt $M=5$:
    $C = M^e \pmod n = 5^7 \pmod{77}$.
    Using Fast Exponentiation ($7 = 111_2 = 4+2+1$):
    $5^1 \equiv 5$
    $5^2 \equiv 25$
    $5^4 \equiv 25^2 = 625 = 8 \cdot 77 + 9 \equiv 9$.
    $5^7 = 5^4 \cdot 5^2 \cdot 5^1 \equiv 9 \cdot 25 \cdot 5 = 9 \cdot 125 \equiv 9 \cdot 48 \pmod{77} \dots = 47$.