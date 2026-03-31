---
tags: [discrete-mathematics, basic-counting, combinations, permutations, multiset, stirling-numbers, partitions]
topic: "Basic Counting Rules"
course: "DISCRETE MATHEMATICS"
---

> [!Note] 💡 Notation Conventions
> - $[n] = \{1, 2, \ldots, n\}$ — the set of the first $n$ positive integers; e.g. $[3] = \{1,2,3\}$.
> - $n! = 1 \cdot 2 \cdots n$ — $n$ factorial, with $0! = 1$.
> - $|X|$ — the **cardinality** (number of elements) of set $X$.
> - $P(n,k) = \dfrac{n!}{(n-k)!}$ — number of **$k$-permutations** of $n$ (ordered selection of $k$ from $n$, no repetition).
> - $C(n,k) = \dbinom{n}{k} = C_n^k = \dfrac{n!}{k!\,(n-k)!}$ — number of **$k$-combinations** of $n$ (unordered, no repetition). All three notations are used in the source; $C(n,k)$ is used throughout these notes.
> - $P(n,k) = C(n,k) = 0$ when $k > n$.
> - $\mathcal{B}_n$ — the set of all binary strings of length $n$; $b_n = |\mathcal{B}_n|$.
> - $\mathcal{P}_n$ — the power set of $[n]$ (set of all subsets); $p_n = |\mathcal{P}_n|$.
> - $S(n,k)$ — **Stirling number of the second kind**: number of partitions of $[n]$ into $k$ non-empty blocks.
> - $B(n) = \sum_{k=1}^n S(n,k)$ — the **Bell number**: total number of partitions of $[n]$.
> - $\{\!\{ \cdot \}\!\}$ — **double braces** denote a multiset.
> - An **$n$-tuple** $(x_1, x_2, \ldots, x_n)$ is an ordered list; a **set** $\{x_1,\ldots,x_n\}$ is unordered.

---

# Basic Counting Rules

---

## 1. Motivating Objects

Before stating the rules, the source introduces the central objects that counting techniques apply to.

### 1.1 Binary Strings

> [!Definition] 📖 Binary String of Length $n$
> A **binary string** of length $n$ is a sequence $s_1 s_2 \cdots s_n$ where each $s_i \in \{0,1\}$.
> $\mathcal{B}_n$ denotes the set of all binary strings of length $n$, and $b_n = |\mathcal{B}_n|$.

> [!Property] ⚙️ Count of Binary Strings
> By the **Product Rule** (Section 2.2): each position has 2 choices independently, so:
> $$b_n = \underbrace{2 \cdot 2 \cdots 2}_{n} = 2^n$$
> Special cases: $b_0 = 1$ (the empty string $\varepsilon$), $b_1 = 2$, $b_2 = 4$.

> [!Property] ⚙️ Binary Strings with At Least One 1
> Let $\mathcal{B}_n'$ = binary strings of length $n$ containing at least one occurrence of $1$.
> The only string of length $n$ **not** in $\mathcal{B}_n'$ is $\underbrace{00\cdots0}_{n}$.
> By the **Addition Rule** (complement method):
> $$b_n' = |\mathcal{B}_n| - 1 = 2^n - 1$$

### 1.2 Subsets of $[n]$ — The Power Set

> [!Definition] 📖 Power Set
> The **power set** $\mathcal{P}_n$ of $[n]$ is the collection of **all subsets** of $[n]$, including $\emptyset$ and $[n]$ itself. Its size is $p_n = |\mathcal{P}_n|$.

> [!Theorem] 📌 Size of the Power Set
> $$p_n = 2^n$$

> [!Proof] 🔷 Bijection Proof
> There is a bijection between subsets $A \subseteq [n]$ and binary strings of length $n$:
> $$A \longleftrightarrow x_1 x_2 \cdots x_n, \quad \text{where } x_i = \begin{cases} 0 & \text{if } i \notin A \\ 1 & \text{if } i \in A \end{cases}$$
> **Example for $n=2$:**
>
> | Subset | Binary string |
> |---|---|
> | $\emptyset$ | $00$ |
> | $\{1\}$ | $10$ |
> | $\{2\}$ | $01$ |
> | $\{1,2\}$ | $11$ |
>
> Since there are $2^n$ binary strings of length $n$, there are $2^n$ subsets of $[n]$. $\blacksquare$
>
> **Larger example:** $\{3,4,6,8\} \subseteq [8]$ corresponds to $00110101$ (positions 3,4,6,8 have a $1$).

### 1.3 Arrangements in a Line (Permutations)

> [!Definition] 📖 $k$-Permutation and Permutation
> Let $n, k \in \mathbb{N}$.
> **a)** An **ordered** arrangement of $k$ objects from $[n]$ is called a **$k$-permutation of $n$**.
> **b)** An **unordered** arrangement of $k$ objects from $[n]$ is called a **$k$-combination of $n$**.
>
> The set of all permutations of $[n]$ (i.e., all $n$-permutations) is $\mathfrak{S}_n$, and $|\mathfrak{S}_n| = P(n,n) = n!$.

> [!Property] ⚙️ Formulas
> $$P(n,k) = n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!}, \quad k \leq n$$
> $$C(n,k) = \frac{P(n,k)}{k!} = \frac{n!}{k!\,(n-k)!}, \quad k \leq n$$
> $$P(n,k) = C(n,k) = 0 \quad \text{if } k > n$$

> [!Note] 💡 Why divide by $k!$ for combinations?
> Each $k$-combination $\{x_1, x_2, \ldots, x_k\}$ corresponds to exactly $k!$ different $k$-permutations (the $k!$ orderings of the same set). So: $C(n,k) = P(n,k)/k!$.

> [!Theorem] 📌 Arrangements in a Line
> The number of ways to arrange $n$ people in a line is $P(n) = n!$.

### 1.4 Arrangements at a Round Table

> [!Theorem] 📌 Circular Permutations
> The number of ways to arrange $n$ people at a **round table** is:
> $$(n-1)! = \frac{n!}{n}$$

> [!Proof] 🔷 Division Rule Proof
> Each linear arrangement $x_1 x_2 \cdots x_n$ gives the **same** circular arrangement as its $n$ rotations:
> $$x_1 x_2 \cdots x_n \;\sim\; x_2 x_3 \cdots x_n x_1 \;\sim\; \cdots \;\sim\; x_n x_1 \cdots x_{n-1}$$
> So $n!$ linear arrangements fall into blocks of size $n$ (each block = 1 circular arrangement).
> By the Division Rule: $\#\text{circular arrangements} = n!/n = (n-1)!$. 

---

## 2. Basic Counting Rules

### 2.1 The Sum Rule

> [!Theorem] 📌 Sum Rule (Addition Rule)
> Given $k$ **mutually disjoint** sets $S_1, S_2, \ldots, S_k$ (i.e., $S_i \cap S_j = \emptyset$ for all $i \neq j$):
> $$|S_1 \cup S_2 \cup \cdots \cup S_k| = |S_1| + |S_2| + \cdots + |S_k|$$
> **Special case (2 sets):** If $A \cap B = \emptyset$, then $|A \cup B| = |A| + |B|$.

> [!Note] 💡 Complement Method (Addition Rule applied)
> To count objects satisfying a property $P$: count **all** objects, then subtract those **not** satisfying $P$:
> $$|\{P\}| = |\text{total}| - |\{\text{not } P\}|$$

### 2.2 The Product Rule

> [!Theorem] 📌 Product Rule
> Given $k$ sets $A_1, A_2, \ldots, A_k$:
> $$|A_1 \times A_2 \times \cdots \times A_k| = |A_1| \cdot |A_2| \cdots |A_k|$$
> **Task interpretation:** If a procedure consists of $k$ sequential tasks with $m_1, m_2, \ldots, m_k$ ways to perform each task (independently), then the total number of ways to complete the procedure is $m_1 \cdot m_2 \cdots m_k$.

### 2.3 The Division Rule

> [!Theorem] 📌 Division Rule
> If a set of $n$ objects can be partitioned into $m$ blocks, each of size $r$ (i.e., $n = m \cdot r$), then the number of distinct blocks is:
> $$m = \frac{n}{r}$$
> Equivalently: if every object is counted exactly $r$ times in an overcounting, divide by $r$.

### 2.4 The Bijection Rule

> [!Theorem] 📌 Bijection Rule
> Given two finite sets $A$ and $B$. If there exists a **bijection** (one-to-one and onto function) between $A$ and $B$, then:
> $$|A| = |B|$$

> [!Note] 💡 Double Counting / Counting in Two Ways
> The bijection rule and "counting in two ways" are equivalent techniques for proving combinatorial identities: show that both sides count the same set via two different methods.

---

## 3. Permutations and Combinations — Formulas

> [!Theorem] 📌 Key Counting Formulas
> **1.** $P(n,k) = n(n-1)\cdots(n-k+1) = \dfrac{n!}{(n-k)!}$ — $k$-permutations of $n$.
>
> **2.** $C(n,k) = \dfrac{n!}{k!\,(n-k)!}$ — $k$-combinations of $n$.
>
> **3.** Binary strings of length $n$ with exactly $k$ ones $= C(n,k)$ (choose $k$ positions out of $n$ for the 1s; no ordering among the positions).
>
> **4.** $C(n,k) = C(n, n-k)$ — **symmetry**: choosing $k$ elements is equivalent to choosing which $n-k$ elements to **leave out** (bijection $A \mapsto [n]\setminus A$).

### 3.1 Pascal's Theorem

> [!Theorem] 📌 Pascal's Identity
> For $n, k \in \mathbb{N}$:
> $$C(n,k) = C(n-1,k) + C(n-1,k-1)$$

> [!Proof] 🔷 Combinatorial Proof (Counting in Two Ways)
> **LHS** = number of ways to choose $k$ elements from $[n]$.
>
> Consider element $n$. Every $k$-subset of $[n]$ either:
> - **does not contain $n$:** choose all $k$ elements from $[n-1]$ → $C(n-1,k)$ ways.
> - **contains $n$:** choose the remaining $k-1$ elements from $[n-1]$ → $C(n-1,k-1)$ ways.
>
> These cases are disjoint and exhaustive. By the sum rule: $C(n,k) = C(n-1,k) + C(n-1,k-1)$. $\blacksquare$

### 3.2 Pascal's Triangle

> [!Property] ⚙️ Pascal's Triangle
> Pascal's triangle lists $C(n,k)$ for rows $n = 0, 1, 2, \ldots$ and columns $k = 0, 1, \ldots, n$.
> Each entry is the sum of the two entries diagonally above it.
>
> $$\begin{array}{ccccccccccccc}
> n=0: & & & & & & 1 \\
> n=1: & & & & & 1 & & 1 \\
> n=2: & & & & 1 & & 2 & & 1 \\
> n=3: & & & 1 & & 3 & & 3 & & 1 \\
> n=4: & & 1 & & 4 & & 6 & & 4 & & 1 \\
> n=5: & 1 & & 5 & & 10 & & 10 & & 5 & & 1 \\
> n=6: & 1 & & 6 & & 15 & & 20 & & 15 & & 6 & & 1
> \end{array}$$

### 3.3 Binomial Theorem

> [!Theorem] 📌 Binomial Theorem
> For any $x, y$ and $n \in \mathbb{N}$:
> $$(x+y)^n = \sum_{k=0}^{n} C(n,k)\, x^k y^{n-k}$$
> **Interpretation:** Expanding $(x+y)(x+y)\cdots(x+y)$ ($n$ factors), the coefficient of $x^k y^{n-k}$ equals $C(n,k)$ = number of ways to choose $k$ factors from which to take $x$ (the rest contribute $y$).

> [!Property] ⚙️ Corollary — Sum of Binomial Coefficients
> Setting $x = y = 1$:
> $$C(n,0) + C(n,1) + \cdots + C(n,n) = 2^n$$
> (All subsets of $[n]$ counted by size.)

---

## 4. Finite Functions

> [!Definition] 📖 Finite Function
> A **function** $f: [m] \to [n]$ assigns each element of $[m]$ (the domain, $m$ elements) to exactly one element of $[n]$ (the codomain, $n$ elements).

> [!Theorem] 📌 Counts of Functions $[m] \to [n]$
>
> | Type | Count | Reason |
> |---|---|---|
> | All functions | $n^m$ | Product rule: $n$ choices for each of $m$ inputs |
> | Injective (one-to-one) | $P(n,m) = \dfrac{n!}{(n-m)!}$ | $n$ choices for $f(1)$, then $n-1$, …, $n-m+1$ |
> | Injective, $m > n$ | $0$ | Impossible by pigeonhole |
> | Surjective (onto) | $n!\, S(m,n)$ | (see Section 6 below) |

---

## 5. Multisets and Permutations with Repetition

### 5.1 Multisets

> [!Definition] 📖 Multiset
> A **multiset** is a collection of unordered elements where an element may appear **more than once**.
> **1.** The number of times an element appears is its **multiplicity**.
> **2.** The **size** of a multiset is the sum of all multiplicities.
> **Notation:** Double braces $\{\!\{ \cdot \}\!\}$ denote multisets.
>
> **Example:** $A = \{\!\{R, R, B, B, B\}\!\}$; multiplicity of $R$ is 2, of $B$ is 3; size of $A$ is 5.

> [!Definition] 📖 Permutation with Repetition
> An **ordered** arrangement of all elements of a multiset is called a **permutation with repetition**.
>
> **Example:** From $A = \{\!\{R,R,B,B,B\}\!\}$: the arrangements $RBRBБ$ and $BBRBR$ are both permutations with repetition.

> [!Theorem] 📌 Count of Permutations with Repetition
> Let $A$ be a multiset of size $n$ with $k$ distinct element types of multiplicities $n_1, n_2, \ldots, n_k$ (so $n_1 + n_2 + \cdots + n_k = n$). The number of permutations with repetition on $A$ is:
> $$\frac{n!}{n_1!\, n_2!\, \cdots\, n_k!}$$

> [!Proof] 🔷 Proof Sketch (Division Rule)
> Treat all $n$ objects as distinct: $n!$ arrangements.
> Each arrangement is overcounted $n_1!$ times (permutations of the $n_1$ identical objects of type 1), times $n_2!$ for type 2, etc.
> Dividing by the overcount gives the formula. $\blacksquare$

> [!Property] ⚙️ Multinomial Coefficient Corollary
> The coefficient of $x_1^{r_1} x_2^{r_2} \cdots x_m^{r_m}$ in the expansion of $(x_1 + x_2 + \cdots + x_m)^n$, where $r_1 + r_2 + \cdots + r_m = n$, equals:
> $$\frac{n!}{r_1!\, r_2!\, \cdots\, r_m!}$$

### 5.2 $k$-Combinations with Repetition

> [!Definition] 📖 $k$-Combination with Repetition
> Given a set $A$ of $n$ elements. A **$k$-combination with repetition** of $A$ is a **multiset of size $k$** whose elements are in $A$. Equivalently, it is a way to choose $k$ elements **with replacement** from $n$ elements (order does not matter).

> [!Theorem] 📌 Count of $k$-Combinations with Repetition
> The number of $k$-combinations with repetition from $n$ elements is:
> $$C(n+k-1,\, k)$$

> [!Proof] 🔷 Stars and Bars Bijection
> Count non-negative integer solutions to $x_1 + x_2 + \cdots + x_n = k$ (where $x_i$ = multiplicity of element $i$).
>
> **Stars and bars model:** represent $k$ stars (objects) and $n-1$ bars (dividers between elements). A placement of $k$ stars into $n$ groups (separated by $n-1$ bars) corresponds bijectively to a solution.
>
> Total objects: $k + (n-1) = k+n-1$.
> Choose positions for the $k$ stars (equivalently, for the $n-1$ bars):
> $$\#\ \text{ solutions} = C(n+k-1,\, k) = C(n+k-1,\, n-1) \qquad \blacksquare$$

> [!Note] 💡 Equivalent Formulations
> The following all count the same thing $$= C(n+k-1,k)$$
> **1.** Non-negative integer solutions to $x_1 + x_2 + \cdots + x_n = k$.
> **2.** $k$-combinations with repetition from $n$ elements.
> **3.** Ways to distribute $k$ identical objects to $n$ people.
> **4.** Ways to place $k$ identical books onto $n$ shelves.

---

## 6. Partitions of a Set and Stirling Numbers (2nd Kind)

### 6.1 Set Partitions

> [!Definition] 📖 Partition of a Set into $k$ Blocks
> A **partition** of a set $A$ into $k$ **blocks** is a collection of $k$ non-empty, mutually disjoint sets $A_1, A_2, \ldots, A_k$ such that:
> $$A = A_1 \cup A_2 \cup \cdots \cup A_k, \quad A_i \cap A_j = \emptyset \;\forall i\neq j, \quad A_i \neq \emptyset \;\forall i$$

> [!Example] 📘 Partitions of $[3]$ into 2 Blocks
> **Using:** Definition of set partition
>
> $A = [3] = \{1,2,3\}$. All partitions into 2 blocks:
> **1.** $\{1\},\;\{2,3\}$
> **2.** $\{2\},\;\{1,3\}$
> **3.** $\{3\},\;\{1,2\}$
>
> Total: $S(3,2) = 3$.

### 6.2 Stirling Numbers of the Second Kind

> [!Definition] 📖 Stirling Number of the Second Kind $S(n,k)$
> $S(n,k)$ is the number of **partitions of $[n]$ into exactly $k$ non-empty blocks** (unordered).
> The **Bell number** $B(n) = \sum_{k=1}^{n} S(n,k)$ counts all partitions of $[n]$.

> [!Theorem] 📌 Special Values of $S(n,k)$
> **1.** $S(n,2) = 2^{n-1} - 1$ — partitions of $[n]$ into exactly 2 blocks.
> **2.** $S(n,n) = 1$ — only one partition into $n$ blocks (each element alone).
> **3.** $S(n,n-1) = C(n,2)$ — exactly one block of size 2, rest singletons.
> **4.** $S(n,1) = 1$ — only one partition into 1 block ($A$ itself).

> [!Proof] 🔷 Proof of $S(n,2) = 2^{n-1}-1$
> A partition of $[n]$ into 2 blocks is an unordered pair $\{A_1, A_2\}$ where $A_1, A_2 \neq \emptyset$ and $A_1 \cup A_2 = [n]$.
> For each non-empty proper subset $A_1 \subsetneq [n]$, $A_2 = [n]\setminus A_1$ is determined.
> Non-empty proper subsets of $[n]$: $2^n - 2$ (exclude $\emptyset$ and $[n]$).
> Each partition is counted twice (once as $\{A_1, A_2\}$, once as $\{A_2, A_1\}$).
> $$S(n,2) = \frac{2^n - 2}{2} = 2^{n-1} - 1 \qquad \blacksquare$$

> [!Theorem] 📌 Recurrence for $S(n,k)$
> $$S(n,k) = S(n-1,k-1) + k \cdot S(n-1,k)$$
> with boundary conditions $S(n,n)=1$, $S(n,1)=1$, $S(n,k)=0$ for $k>n$.

> [!Proof] 🔷 Proof
> $S(n,k)$ counts partitions of $[n]$ into $k$ blocks. Consider element $n$:
>
> **Case 1:** $\{n\}$ is a block by itself. The remaining $n-1$ elements partition into $k-1$ blocks: $S(n-1, k-1)$ ways.
>
> **Case 2:** $n$ is **not** a singleton block. First partition $[n-1]$ into $k$ blocks ($S(n-1,k)$ ways), then insert $n$ into one of the $k$ existing blocks: $k$ choices.
>
> By the sum rule: $S(n,k) = S(n-1,k-1) + k \cdot S(n-1,k)$. $\blacksquare$

> [!Note] 💡 No Explicit Formula for $S(n,k)$
> There is no simple closed-form expression for $S(n,k)$ in general (the source states this explicitly). The recurrence and special cases are the primary tools.

### 6.3 Surjective Functions and $S(n,k)$

> [!Theorem] 📌 Surjective Functions $[m] \to [n]$
> The number of surjective (onto) functions from $[m]$ to $[n]$ is:
> $$n! \cdot S(m,n)$$

> [!Proof] 🔷 Proof
> A surjection $f:[m]\to[n]$ induces a partition of $[m]$ into the preimage sets $B_i = \{x: f(x) = i\}$, $i=1,\ldots,n$.
> These sets are non-empty (surjectivity), disjoint, and cover $[m]$ — forming an **ordered** partition into $n$ blocks.
>
> The number of ordered partitions = (number of unordered partitions) $\times$ (number of ways to label blocks $1,\ldots,n$) $= S(m,n) \times n!$. $\blacksquare$

---

## 📘 Examples & Applications

> [!Example] 📘 Example 1: Tournament Problem (Sum Rule)
> **Using:** Sum Rule
>
> **Problem:** Given $n$ football teams. Each team plays every other team exactly once. How many matches are there in total?
>
> Teams: $T_1, T_2, \ldots, T_n$.
>
> Matches involving $T_1$: $n-1$ (against $T_2, \ldots, T_n$).
> Matches involving $T_2$ (with teams not yet counted): $n-2$.
> $\vdots$
> Matches involving $T_{n-1}$: $1$.
>
> By the Sum Rule (all match sets are disjoint):
> $$\text{Total} = (n-1) + (n-2) + \cdots + 1 = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$$

> [!Example] 📘 Example 2: Passwords (Product Rule + Complement)
> **Using:** Product Rule, Addition Rule (complement)
>
> **(i) Passwords of 8 characters from $\{$lowercase letters, uppercase letters, digits$\}$:**
> Each character has $26 + 26 + 10 = 62$ choices. By the product rule:
> $$62^8$$
>
> **(ii) Passwords of 8 characters with at least 1 capital letter:**
>
> Total passwords (no restriction): $62^8$.
> Passwords with **no** capital letter: each character chosen from $\{$lowercase, digits$\} = 36$ options:
> $$36^8$$
>
> By the complement (Addition Rule):
> $$\text{Answer} = 62^8 - 36^8$$

> [!Example] 📘 Example 3: Circular Arrangement (Division Rule)
> **Using:** Division Rule, Circular Permutations
>
> **Problem:** How many different strings can be made from the letters of MISSISSIPPI?
>
> Letters: M(1), I(4), S(4), P(2). Total letters: $1+4+4+2 = 11$... 

> [!Warning] ⚠️ Possible Gap
> The source writes "MISSISSIPI" (one P, which gives 10 letters), but standard MISSISSIPPI has 11 letters (M×1, I×4, S×4, P×2). The source formula shown is $\dfrac{10!}{4!\,4!}$ (using 10 letters, 4 I's, 4 S's, treating all other letters as distinct). The notes follow the source's formula.

> The source works with the word as having 10 letters total (MISSISSIPI), with 4 I's and 4 S's repeated:
> $$\frac{10!}{4!\,4!}$$
> The $10!$ = # permutations of 10 elements treating all as distinct; divide by $4!$ for the identical I's and $4!$ for the identical S's.

> [!Example] 📘 Example 4: Anagrams of EXCEED (Permutations with Repetition)
> **Using:** Permutation with Repetition formula, Addition Rule (complement)
>
> EXCEED has letters: E(3), X(1), C(1), D(1). Total = 6 letters.
>
> **(a) No restriction — total distinct strings:**
> $$\frac{6!}{3!\,1!\,1!\,1!} = \frac{720}{6} = 120$$
>
> **(b) Strings with no 3 consecutive E's:**
>
> Treat EEE as a single "super-letter." Now arrange $\{\!\{C, X, D, EEE\}\!\}$ — 4 distinct objects:
> $$\frac{4!}{1!\,1!\,1!\,1!} = 24$$
>
> By the Addition Rule (complement):
> $$\text{Strings with no 3 consecutive E's} = \frac{6!}{3!\,1!\,1!\,1!} - \frac{4!}{1!\,1!\,1!\,1!} = 120 - 24 = 96$$

> [!Example] 📘 Example 5: Binomial Coefficient Extraction
> **Using:** Binomial Theorem
>
> **Problem:** Find the coefficient of $x^i$ in the expansion of $\left(x + \dfrac{1}{x}\right)^{100}$.
>
> By the Binomial Theorem:
> $$\left(x + \frac{1}{x}\right)^{100} = \sum_{k=0}^{100} C(100,k)\, x^k \cdot \left(\frac{1}{x}\right)^{100-k} = \sum_{k=0}^{100} C(100,k)\, x^{2k-100}$$
>
> The exponent of $x$ in the $k$-th term is $2k - 100$. Setting $2k - 100 = i$:
> $$k = \frac{i+100}{2}$$
> This is an integer only when $i$ is even. So:
> $$\text{Coefficient of } x^i = \begin{cases} C\!\left(100,\, \dfrac{i+100}{2}\right) & \text{if } i \in \{-100, -98, \ldots, 0, 2, \ldots, 100\} \\ 0 & \text{otherwise} \end{cases}$$

> [!Example] 📘 Example 6: Multinomial Coefficient
> **Using:** Multinomial Coefficient Corollary
>
> **Problem:** Find the coefficient of $x^{25} y^{25} z^{50}$ in $(x + y + 2z)^{100}$.
>
> We need $r_1 = 25$ (for $x$), $r_2 = 25$ (for $y$), $r_3 = 50$ (for $2z$), with $r_1+r_2+r_3 = 100$. ✓
>
> The term comes from choosing $x$ 25 times, $y$ 25 times, and $2z$ 50 times:
> $$\text{Coefficient} = \frac{100!}{25!\,25!\,50!} \cdot 2^{50}$$
> (The $2^{50}$ comes from the coefficient 2 in $2z$, raised to the power 50.)

> [!Example] 📘 Example 7: Distributing Candies (Stars and Bars)
> **Using:** $k$-combinations with repetition, Stars and Bars
>
> **Problem:** How many ways to distribute 10 identical candies to 7 children with no restriction?
>
> This equals the number of non-negative integer solutions to $x_1 + x_2 + \cdots + x_7 = 10$:
> $$C(10+7-1, 10) = C(16,10) = C(16,6)$$

> [!Example] 📘 Example 8: Non-Negative Integer Solutions to an Inequality
> **Using:** Stars and Bars, Bijection Rule
>
> **Problem:** How many non-negative integer solutions does $x_1 + x_2 + x_3 \leq 11$ have?
>
> **Trick:** Introduce a slack variable $x_4 \geq 0$ so the inequality becomes an equation:
> $$x_1 + x_2 + x_3 + x_4 = 11, \quad x_i \geq 0$$
> This is a bijection between solution sets (map $(x_1,x_2,x_3)$ to $(x_1,x_2,x_3, 11-x_1-x_2-x_3)$).
>
> Number of solutions $= C(11+4-1, 11) = C(14, 11) = C(14,3)$.

> [!Example] 📘 Example 9: Painting Chairs (Permutations with Repetition)
> **Using:** Permutation with Repetition formula
>
> **Problem:** How many ways to paint 10 distinct chairs so that exactly 3 are blue, 3 are red, and 4 are white?
>
> This is equivalent to distributing the 10 distinct chairs into colour groups — a multinomial:
> $$\frac{10!}{3!\,3!\,4!}$$

> [!Example] 📘 Example 10: Surjections from $[m]$ to $[2]$
> **Using:** Surjection formula, $S(m,2)$
>
> **Problem:** How many surjective functions from $[m]$ to $[2]$ are there?
>
> By the surjection formula: $2! \cdot S(m, 2)$.
> Using $S(m,2) = 2^{m-1} - 1$:
> $$2! \cdot (2^{m-1}-1) = 2(2^{m-1}-1) = 2^m - 2$$
>
> **Direct verification:** All functions $[m]\to[2]$: $2^m$. Non-surjective (constant): 2. Surjective: $2^m - 2$. ✓

---

## 🗂️ Summary

- **Sum Rule:** $|S_1 \cup \cdots \cup S_k| = \sum|S_i|$ when the $S_i$ are mutually disjoint. Use the complement method ($|\text{total}| - |\text{not } P|$) to count via exclusion.
- **Product Rule:** Sequential tasks with independent choices multiply: $m_1 \cdot m_2 \cdots m_k$.
- **Division Rule:** If $n$ objects form $m$ equal blocks of size $r$, then $m = n/r$. Used to convert linear to circular arrangements.
- **Bijection Rule:** $|A| = |B|$ whenever a bijection $A \leftrightarrow B$ exists; underpins double counting.
- **Subsets of $[n]$:** $2^n$, proved by bijection with binary strings of length $n$.
- **Arrangements in a line:** $P(n) = n!$. **Circular arrangements:** $(n-1)!$ (division rule, divide by $n$ rotations).
- **$k$-permutations:** $P(n,k) = \dfrac{n!}{(n-k)!}$. **$k$-combinations:** $C(n,k) = \dfrac{n!}{k!(n-k)!}$.
- **Symmetry:** $C(n,k) = C(n,n-k)$. **Pascal:** $C(n,k) = C(n-1,k) + C(n-1,k-1)$.
- **Binomial Theorem:** $(x+y)^n = \sum_{k=0}^n C(n,k) x^k y^{n-k}$; sum of all $C(n,k) = 2^n$.
- **Binary strings with $k$ ones:** $C(n,k)$.
- **All functions $[m]\to[n]$:** $n^m$. **Injective:** $P(n,m)$. **Surjective:** $n!\cdot S(m,n)$.
- **Permutations with repetition** (multiset of size $n$, types with multiplicities $n_1,\ldots,n_k$): $\dfrac{n!}{n_1!\cdots n_k!}$.
- **Multinomial coefficient:** coefficient of $x_1^{r_1}\cdots x_m^{r_m}$ in $(x_1+\cdots+x_m)^n$ is $\dfrac{n!}{r_1!\cdots r_m!}$ (when $\sum r_i = n$).
- **$k$-combinations with repetition from $n$:** $C(n+k-1, k)$ — same as solutions to $x_1+\cdots+x_n=k$ in non-negative integers.
- **Stirling (2nd kind):** $S(n,k)$ = partitions of $[n]$ into $k$ blocks; recurrence $S(n,k)=S(n-1,k-1)+k\cdot S(n-1,k)$.
- **Special values:** $S(n,2) = 2^{n-1}-1$; $S(n,n)=1$; $S(n,n-1)=C(n,2)$; $S(n,1)=1$.
- **Bell number:** $B(n) = \sum_{k=1}^n S(n,k)$ = total partitions of $[n]$; no simple closed form.
- **Inequality trick (Stars and Bars):** solutions to $x_1+\cdots+x_n \leq k$ biject to solutions to $x_1+\cdots+x_n+x_{n+1}=k$ (add slack variable), giving $C(k+n, k)$.
