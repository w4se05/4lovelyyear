## 1. Fundamentals of Counting

### 1.1 The Sum Rule

The sum rule is used when a task can be performed in several ways that are mutually exclusive (cannot happen at the same time).

> [!Theorem] **Sum Rule** 
> Given $A$ and $B$ as two disjoint sets (where $A \cap B = \emptyset$), the number of ways to choose an element from $A$ or $B$ is $|A \cup B| = |A| + |B|$.
> 
> **Generalization:** If $\{S_1, S_2, \dots, S_k\}$ are mutually disjoint sets ($S_i \cap S_j = \emptyset$ for $i \neq j$), then:
> 
> $$|S_1 \cup S_2 \cup \dots \cup S_k| = |S_1| + |S_2| + \dots + |S_k|$$

### 1.2 The Product Rule

The product rule is applied when a procedure can be broken down into a sequence of tasks.

> [!Theorem] **Product Rule**
> 
> If a procedure consists of $k$ tasks such that the first task can be done in $m_1$ ways, the second in $m_2$ ways, and the $k$-th task in $m_k$ ways, then the total number of ways to complete the procedure is:
> 
> $$m_1 \cdot m_2 \cdot \dots \cdot m_k$$

### 1.3 The Division Rule

The division rule is used when there are $n$ ways to do a task, but those ways are organized into $m$ groups (blocks), each containing $d$ equivalent outcomes.

> [!Theorem] **Division Rule** 
> There are $n/d$ ways to do a task if it can be done using a procedure that can be carried out in $n$ ways, and for every way $w$, there are exactly $d$ ways that correspond to the same outcome.

### 1.4 The Bijection Rule

>[!Theorem] **Bijection Rule**
Bijection Rule Given two finite sets $A$ and $B$, if there exists a bijection between $A$ and $B$, then $|A| = |B|$

---

## 2. Permutations and Combinations

### 2.1 Permutations

A permutation is an **ordered** arrangement of elements from a set.

> [!Definition] **k-Permutation** 
> An ordered arrangement of $k$ objects from a set of $n$ elements is called a $k$-permutation. 
> - **Notation:** $P(n, k)$ or $P_k^n$.
> 
> - **Formula:** For $k \le n$:
>     
>     $$P(n, k) = n(n-1)\dots(n-k+1) = \frac{n!}{(n-k)!}$$
>     
>     - **Full Permutation:** If $k=n$, the number of arrangements is $n!$.
>     

### 2.2 Combinations

A combination is an **unordered** selection of elements from a set.

> [!Definition] **k-Combination** 
> An unordered arrangement of $k$ objects from a set of $n$ elements. 
> - **Notation:** $C(n, k)$, $\binom{n}{k}$, or $C_n^k$.
> 
> - **Formula:** Using the division rule (removing the internal order of $k!$ elements):
>     
>     $$C(n, k) = \frac{P(n, k)}{k!} = \frac{n!}{k!(n-k)!}$$
>     

---

## 3. Advanced Counting & Identities

### 3.1 Binomial Theorem and Pascal's Identity

Combinatorial identities can be proven through algebraic derivation or combinatorial proofs (counting the same thing in two different ways).

> [!Theorem] **Pascal's Theorem**
> 
> For $n, k \in \mathbb{N}$:
> 
> $$C(n, k) = C(n-1, k) + C(n-1, k-1)$$

> [!Theorem] **Binomial Theorem**
> 
> $$(x+y)^n = \sum_{k=0}^n C(n, k) x^k y^{n-k}$$
> 
> The coefficient of the monomial $x^k y^{n-k}$ is $C(n, k)$.

### 3.2 Counting with Repetition (Multisets)

When elements can be chosen more than once, we use repetition rules.

> [!Property] **k-Combinations with Repetition**
> 
> The number of $k$-combinations of $n$ elements where repetition is allowed is:
> 
> $$C(n+k-1, k)$$
> 
This is mathematically equivalent to the number of non-negative integer solutions to the equation $x_1 + x_2 + \dots + x_n = k$.
>
> _Commonly modeled using the **Stars and Bars** method_.

> [!Theorem] **Permutations with Repetition** 
> The number of permutations of $n$ objects of $k$ different types, where $n_i$ is the multiplicity of type $i$:
> 
> $$\frac{n!}{n_1! n_2! \dots n_k!}$$

---

## 4. Stirling Numbers and Partitions

### 4.1 Stirling Numbers of the Second Kind

Used to count the number of ways to partition a set of $n$ distinct elements into $k$ non-empty, unordered subsets (blocks).

> [!Definition] **Stirling Number $S(n, k)$**
>  - **Recurrence:** $S(n, k) = S(n-1, k-1) + k \cdot S(n-1, k)$.
> 
> - **Application:** The number of surjective (onto) functions from a set of $m$ elements to $n$ elements is $n! \cdot S(m, n)$.
>     

### 4.2 Partitions of an Integer

Counting the ways to write a positive integer $n$ as a sum of positive integers where the order of summands does not matter.

> [!Note] **Notation**
> 
> $p(n, k)$ denotes the number of partitions of $n$ into exactly $k$ components. 
> **Recurrence:** $p(n, k) = p(n-1, k-1) + p(n-k, k)$.

---

## 📘 Examples & Applications

### Example 1: Password Complexity

**Question:** How many 8-character passwords can be formed using digits, lowercase letters, and uppercase letters if at least one uppercase letter must be included?

**Solution:**

_(Using: Product Rule and Complementary Counting)_

1. **Total possible characters:** $10 \text{ (digits)} + 26 \text{ (lowercase)} + 26 \text{ (uppercase)} = 62$.
    
2. **Total passwords (no restriction):** $62^8$.
    
3. **Passwords with NO uppercase letters:** $(10 + 26)^8 = 36^8$.
    
4. **Result:** Total minus unrestricted = $62^8 - 36^8$.

### Example 2: Permutations with Repetition

**Question:** How many different strings can be made from the letters of the word "MISSISSIPPI"?

**Solution:** _(Using: Permutations with Repetition)_

1. **Total letters ($n$):** 11.
    
2. **Multiplicities:** M (1), I (4), S (4), P (2).
    
3. **Formula:** $\frac{n!}{n_1!n_2!n_3!n_4!}$
    
4. **Calculation:** $\frac{11!}{1! 4! 4! 2!}$.
    

### Example 3: Integer Solutions (Stars and Bars)

**Question:** How many non-negative integer solutions exist for the equation $x_1 + x_2 + x_3 \le 11$?

**Solution:**

_(Using: Bijection Rule and k-combinations with repetition)_

1. **Transform Inequality to Equality:** Introduce a slack variable $x_4 \ge 0$ such that $x_1 + x_2 + x_3 + x_4 = 11$.
    
2. **Apply Stars and Bars:** Here $n = 4$ variables and $k = 11$.
    
3. **Formula:** $C(n+k-1, k) = C(4+11-1, 11) = C(14, 11)$.
    

---

## Summary for Revision

- **Ordered Selection:** Use $P(n, k)$.
    
- **Unordered Selection:** Use $C(n, k)$.
    
- **Circular Arrangement:** $(n-1)!$.
    
- **Identical Objects into Distinct Boxes:** Use Stars and Bars $C(n+k-1, k)$.
    
- **Distinct Objects into Distinct Boxes (Surjective):** $n! S(m, n)$.
    
- **Distinct Objects into Identical Boxes (Partition):** $S(n, k)$.
    
- **Identical Objects into Identical Boxes:** $p(n, k)$.
    