# Exam Cheat Sheet: Logic, Relations, & Number Theory

## 🧠 Part 1: Logic & Proofs
**Focus:** Handling implications, valid arguments, and quantifiers without massive truth tables.

### 1. The "Implication" Shortcuts
Many exercises ask you to negate statements or check validity involving "If... then..." (e.g., Ex 1, 5).

> [!Tip] The Golden Equivalence
> Always remember that $p \rightarrow q \equiv \neg p \vee q$.
> * **Why?** It makes negation easy.
> * **The Mistake:** Do not say "If p then not q".
> * **The Correct Negation:** $\neg (p \rightarrow q) \equiv \neg(\neg p \vee q) \equiv p \wedge \neg q$.

**Example:**
* *Statement:* "If it rains, I stay home."
* *Negation:* "It rained **AND** I did not stay home."

### 2. Validity Checks (The "Lazy" Method)
For arguments like "If Joe studies hard..." (Ex 8-10), you don't always need a massive truth table.

> [!Abstract] The Invalidity Test
> An argument is **Invalid** ONLY if:
> **All Premises are TRUE** AND **Conclusion is FALSE**.

**Algorithm:**
1. Assume the **Conclusion is False**.
2. Work backward to see if you can force the **Premises to be True**.
3. If you *can* do this $\rightarrow$ **Invalid**.
4. If you hit a contradiction $\rightarrow$ **Valid**.

### 3. Quantifier Negation (De Morgan for Quantifiers)
When negating sentences with "All", "Some", or "None" (Ex 15):

> [!Note] The Flip Trick
> Flip the quantifier symbol and negate the predicate verb.
> * $\neg (\forall x, P(x)) \iff \exists x, \neg P(x)$
> * $\neg (\exists x, P(x)) \iff \forall x, \neg P(x)$

**Example:**
* *Statement:* "Some old dogs can learn new tricks."
* *Negation:* "No old dogs can learn new tricks" (or "All old dogs cannot learn new tricks").

---

## 🔗 Part 2: Relations & Matrices
**Focus:** Identifying properties quickly from matrices and calculating closures.

### 1. Matrix Inspection Tricks
Given a matrix $M_R$, check properties visually (Ex 13, 14, 25):

> [!Tip] Visual Checks
> * **Reflexive:** Look at the **Main Diagonal**. If **all** entries are $1$, it is Reflexive.
> * **Symmetric:** Fold the matrix along the diagonal. If $M_{ij} = M_{ji}$ everywhere, it is Symmetric.
> * **Antisymmetric:** If $M_{ij} = 1$ (where $i \neq j$), then $M_{ji}$ **MUST** be $0$. You cannot have $1$s mirroring each other.

### 2. Warshall’s Algorithm (Manual Shortcut)
For Transitive Closure (Ex 19, 20).

> [!Algorithm] The Column-Row Scan
> When processing node $k$:
> 1. Look at **Column $k$**. Identify rows $i$ that have a $1$.
> 2. Look at **Row $k$**. Identify columns $j$ that have a $1$.
> 3. Draw a $1$ at every intersection $(i, j)$ of those rows and columns.

### 3. Equivalence Classes
> [!Note] Identification Shortcut
> Any relation defined by:
> * $x \equiv y \pmod m$
> * "x and y share the same property" (e.g., same number of 1s)
>
> ...is **always** an Equivalence Relation.

---

## 🔢 Part 3: Number Theory
**Focus:** Calculating modulo without calculators and solving RSA.

### 1. Fast Modular Exponentiation
For problems like "Find $7^{121} \pmod{13}$" (Ex 3). **Do NOT compute the huge number.**

> [!Tip] Reduction Theorems
> **1. Fermat’s Little Theorem:**
> If $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.
> * *Usage:* Reduce the exponent modulo $(p-1)$.
>
> **2. Euler's Theorem:**
> For composite $n$, $a^{\phi(n)} \equiv 1 \pmod n$.

**Example ($7^{121} \pmod{13}$):**
* $13$ is prime. $7^{12} \equiv 1 \pmod{13}$.
* Exponent $121 = 12 \times 10 + 1$.
* Result: $1^{10} \cdot 7^1 \equiv 7 \pmod{13}$.

### 2. Finding the Last Digit
> [!Note] Meaning
> "Find the last digit" = **Calculate modulo 10**.

### 3. Finding Inverses (Linear Congruence)
To solve $ax \equiv 1 \pmod n$ (Ex 16):

> [!Algorithm] Extended Euclidean Algorithm (Table Method)
> Write $1 = s \cdot a + t \cdot n$.
> * The inverse $a^{-1} \equiv s \pmod n$.
> * **Check:** If $\gcd(a, n) \neq 1$, no inverse exists.

### 4. RSA Decryption Routine
For "Textbook RSA" problems (Ex 21):

> [!Example] The Workflow
> **Given:** Public key $(e, n)$. **Task:** Decrypt $C$.
> 1. **Factor:** $n \to p \times q$.
> 2. **Phi:** $\phi(n) = (p-1)(q-1)$.
> 3. **Private Key ($d$):** Solve $e \cdot d \equiv 1 \pmod{\phi(n)}$ (use Inverse method above).
> 4. **Decrypt:** $M = C^d \pmod n$.