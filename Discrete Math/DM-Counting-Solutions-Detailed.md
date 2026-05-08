---
tags: [discrete-mathematics, solutions, basic-counting, advanced-counting]
topic: "Complete Detailed Solutions — Basic & Advanced Counting"
course: "DISCRETE MATHEMATICS"
links:
  - "[[1- DM-Basic-Counting-Rules]]"
  - "[[2- DM-Advanced-Counting]]"
---

> [!Note] 📁 How to Use This File
> This file contains **step-by-step solutions** to every exercise in Sections 1 (Basic Counting) and 2 (Advanced Counting). Each solution:
> - States **which rule or theorem** is being used and **why**
> - Shows **every intermediate step**, not just the final answer
> - Includes **intuitive explanations** before the algebra
> - Highlights the **final answer** in a box
>
> **Knowledge files referenced:**
> - `[[1- DM-Basic-Counting-Rules]]` — Sum/Product/Division/Bijection rules, permutations, combinations, binomial theorem, stars-and-bars, Stirling numbers, partitions.
> - `[[2- DM-Advanced-Counting]]` — Generating functions, recurrence relations, permutation structure, PIE, derangements.

---

# Section 1 — Basic Counting Rules

---

## Problem 1 — 2-element subsets of $[n]$

**What is being asked:** How many unordered pairs can we choose from a set with $n$ elements?

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$k$-combinations formula]] $C(n,k) = \dfrac{n!}{k!(n-k)!}$

**Why combinations and not permutations?** The problem asks for *subsets*, which are unordered. Choosing $\{a, b\}$ is the same as choosing $\{b, a\}$. If order mattered, the answer would be $P(n,2) = n(n-1)$, but since it does not, we divide by $2! = 2$ to remove the double-counting.

**Step-by-step:**
- We want to choose exactly $k = 2$ elements from a set of $n$ elements.
- Number of ordered pairs: $n \times (n-1)$ (first element has $n$ choices, second has $n-1$).
- Each unordered pair $\{a,b\}$ gets counted twice in the ordered list (once as $(a,b)$, once as $(b,a)$), so divide by $2! = 2$.

$$C(n,2) = \frac{n(n-1)}{2!} = \frac{n(n-1)}{2}$$

> **Example check:** For $n=4$: $C(4,2) = 6$. List: $\{1,2\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}$. ✓

$$\boxed{C(n,2) = \dfrac{n(n-1)}{2}}$$

---

## Problem 2 — Subsets of $[100]$ with at most 2 elements

**What is being asked:** Count subsets of size 0, 1, or 2, then add them up.

**Rule used:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Sum Rule]] — the three cases (size 0, size 1, size 2) are mutually exclusive (a subset can't have two different sizes at once), so we add.

**Step-by-step:**

| Subset size | Count | Reasoning |
|---|---|---|
| 0 (empty set) | $C(100, 0) = 1$ | Only one empty set |
| 1 (singletons) | $C(100, 1) = 100$ | Pick any one of 100 elements |
| 2 (pairs) | $C(100, 2) = \dfrac{100 \times 99}{2} = 4950$ | Pick an unordered pair |

Adding all three cases together:

$$1 + 100 + 4950 = \boxed{5051}$$

---

## Problem 3 — Subsets of $[100]$ with MORE than 2 elements

**What is being asked:** Subsets of size 3, 4, 5, …, 100. Instead of summing 98 terms directly, we use the complement.

**Rule used:** [[1- DM-Basic-Counting-Rules#1.2 Subsets of $[n]$ — The Power Set|Power Set Theorem]] + [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement method]]

**Key insight:** Every subset either has at most 2 elements OR more than 2 elements — these two cases cover everything and never overlap. So:

$$\text{(subsets with} > 2 \text{ elements)} = \text{(all subsets)} - \text{(subsets with} \leq 2 \text{ elements)}$$

**Step-by-step:**
- Total subsets of $[100]$: $2^{100}$ (every element is either in or out — $2^{100}$ binary choices).
- Subsets with at most 2 elements: $5051$ (from Problem 2).

$$2^{100} - 5051$$

$$\boxed{2^{100} - 5051}$$

---

## Problem 4 — Total subsets of $[n]$

**What is being asked:** How many subsets does a set with $n$ elements have?

**Rule used:** [[1- DM-Basic-Counting-Rules#1.2 Subsets of $[n]$ — The Power Set|Power Set Theorem / Bijection with binary strings]]

**Intuition:** For each element, we make an independent binary decision: include it (1) or exclude it (0). There are $n$ such decisions, each with 2 options.

**Bijection proof:** Map each subset $A \subseteq [n]$ to the binary string $s_1 s_2 \cdots s_n$ where $s_i = 1$ if $i \in A$ and $s_i = 0$ if $i \notin A$. This is a one-to-one correspondence. Binary strings of length $n$: $2^n$.

**Example** ($n=3$): $\emptyset \leftrightarrow 000$, $\{1\} \leftrightarrow 100$, $\{2\} \leftrightarrow 010$, $\{1,2\} \leftrightarrow 110$, etc. — all $2^3 = 8$ subsets listed.

$$\boxed{2^n}$$

---

## Problem 5 — 5-character ASCII strings containing '@' at least once

**What is being asked:** How many length-5 strings (from the 128-character ASCII set) contain at least one '@'?

**Rule used:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement method]] + [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]]

**Why complement?** "At least one" problems are easier via complement: subtract the strings that have *zero* '@' characters.

**Step-by-step:**
1. **Total** 5-character strings: Each of 5 positions has 128 choices independently.
$$\text{Total} = 128^5$$

2. **Strings with NO '@':** Each position now has $128 - 1 = 127$ choices (any character except '@').
$$\text{No '@'} = 127^5$$

3. **Strings with AT LEAST ONE '@':**
$$128^5 - 127^5$$

$$\boxed{128^5 - 127^5}$$

> **Numerical check:** $128^5 = 34{,}359{,}738{,}368$ and $127^5 = 33{,}038{,}369{,}407$, so the answer is $1{,}321{,}368{,}961$.

---

## Problem 6 — Bit strings of length 5

**Setup:** A bit string of length 5 uses only 0s and 1s. Total strings: $2^5 = 32$. "Occurrences of 0" = how many positions have the value 0.

**Key insight:** Choosing *which positions* are 0 completely determines the string. Choosing $k$ positions out of 5 to be 0 = $C(5, k)$.

### (a) Exactly two 0s

**Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$C(n,k)$]]

Choose 2 of the 5 positions to be 0 (the other 3 are automatically 1).

$$C(5, 2) = \frac{5!}{2! \cdot 3!} = \frac{5 \times 4}{2} = \boxed{10}$$

*Listing:* 00111, 01011, 01101, 01110, 10011, 10101, 10110, 11001, 11010, 11100.

### (b) At most two 0s

**Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Sum Rule]] — add disjoint cases (0 zeros, 1 zero, 2 zeros).

| # of zeros | Count |
|---|---|
| 0 zeros (all 1s) | $C(5,0) = 1$ |
| Exactly 1 zero | $C(5,1) = 5$ |
| Exactly 2 zeros | $C(5,2) = 10$ |

$$1 + 5 + 10 = \boxed{16}$$

### (c) At least two 0s

**Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement]] — total minus (0 zeros + 1 zero).

$$2^5 - C(5,0) - C(5,1) = 32 - 1 - 5 = \boxed{26}$$

*Verification:* (b) + (c) = $16 + 26 - C(5,2) = 16 + 26 - 10 = 32 = 2^5$. ✓ (The "exactly 2 zeros" case is counted in both (b) and (c).)

---

## Problem 7 — Prove $\varphi(p^k) = p^k - p^{k-1}$

**What is being asked:** Euler's phi function $\varphi(n)$ counts integers in $\{1, 2, \ldots, n\}$ that are coprime to $n$. We must prove a formula for it when $n = p^k$ (a prime power).

**Rule used:** [[2- DM-Advanced-Counting#15.1 Euler's Phi Function|Complement counting / PIE]]

**Key observation:** An integer $m$ with $1 \leq m \leq p^k$ is NOT coprime to $p^k$ if and only if $\gcd(m, p^k) > 1$. Since $p$ is prime, the only prime factor of $p^k$ is $p$ itself. So $\gcd(m, p^k) > 1$ if and only if $p \mid m$.

**Step-by-step proof:**

1. Total integers from 1 to $p^k$: there are $p^k$ of them.
2. Integers in $\{1, \ldots, p^k\}$ divisible by $p$: these are $p, 2p, 3p, \ldots, p^{k-1} \cdot p$. There are exactly $p^{k-1}$ such integers.
3. Every other integer in $\{1, \ldots, p^k\}$ is coprime to $p^k$ (since it shares no factor of $p$).

Therefore:

$$\varphi(p^k) = p^k - p^{k-1} \qquad \blacksquare$$

> **Example:** $\varphi(8) = \varphi(2^3) = 8 - 4 = 4$. The coprimes to 8 in $\{1,\ldots,8\}$ are: 1, 3, 5, 7. ✓

---

## Problem 8 — Auditorium chair labels

**What is being asked:** Labels have the form (letter)(number). How many distinct labels exist?

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] — the letter choice and number choice are independent tasks.

**Step-by-step:**
- Task 1 (choose a letter): 26 uppercase English letters → 26 choices.
- Task 2 (choose a number): positive integer not exceeding 100 → 100 choices (namely 1, 2, …, 100).
- Since these are independent: multiply.

$$26 \times 100 = \boxed{2600}$$

---

## Problem 9 — License plates: 3 uppercase letters then 3 digits

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] — each of the 6 positions is chosen independently.

**Step-by-step:**

| Positions | Options per position | Count |
|---|---|---|
| 3 letters | 26 (A–Z, repetitions allowed) | $26^3 = 17{,}576$ |
| 3 digits | 10 (0–9, repetitions allowed) | $10^3 = 1{,}000$ |

Total (positions are independent):

$$26^3 \times 10^3 = 17{,}576 \times 1{,}000 = \boxed{17{,}576{,}000}$$

---

## Problem 10 — Passwords of 4–8 lower/upper case letters

**Rule used:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Sum Rule]] (add counts by length) + [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] (multiply per character)

**Setup:** There are $26 + 26 = 52$ possible characters (26 lowercase + 26 uppercase). Each character in the password is chosen independently from these 52 options.

**Step-by-step:** Passwords of exactly $k$ characters: $52^k$ (Product Rule). Lengths 4 through 8 are mutually exclusive (a password has exactly one length), so we use the Sum Rule:

$$\sum_{k=4}^{8} 52^k = 52^4 + 52^5 + 52^6 + 52^7 + 52^8$$

Computing each term:
- $52^4 = 7{,}311{,}616$
- $52^5 = 380{,}204{,}032$
- $52^6 = 19{,}770{,}609{,}664$
- $52^7 = 1{,}028{,}071{,}702{,}528$
- $52^8 = 53{,}459{,}728{,}531{,}456$

$$\boxed{54{,}507{,}385{,}159{,}296}$$

---

## Problem 11 — Club: president and 2-person advisory board (president excluded)

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] + [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Combinations]]

**Key constraint:** The president is **not** on the advisory board. So after choosing the president, we pick the board from the remaining members.

**Step-by-step:**
1. **Choose president:** 10 ways (any of the 10 club members).
2. **Choose advisory board:** We now have $10 - 1 = 9$ remaining members. We pick 2 (unordered, since the board has no internal ranking):
$$C(9, 2) = \frac{9 \times 8}{2} = 36 \text{ ways}$$
3. These two tasks are sequential and independent, so multiply:

$$10 \times 36 = \boxed{360}$$

---

## Problem 12 — Five-digit numbers

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] + Complement method

### Part 1: Total five-digit numbers

A five-digit number has the form $d_1 d_2 d_3 d_4 d_5$ where:
- $d_1 \in \{1, 2, \ldots, 9\}$ (cannot be 0, or it wouldn't be a 5-digit number): **9 choices**
- $d_2, d_3, d_4, d_5 \in \{0, 1, \ldots, 9\}$: **10 choices each**

$$9 \times 10 \times 10 \times 10 \times 10 = 9 \times 10^4 = \boxed{90{,}000}$$

### Part 2: No two consecutive digits equal

"No consecutive equal digits" means $d_i \neq d_{i+1}$ for each $i$.

- $d_1$: 9 choices (1–9).
- $d_2$: must differ from $d_1$ → 9 choices (0–9 minus $d_1$).
- $d_3$: must differ from $d_2$ → 9 choices.
- $d_4$: must differ from $d_3$ → 9 choices.
- $d_5$: must differ from $d_4$ → 9 choices.

$$9 \times 9 \times 9 \times 9 \times 9 = 9^5 = \boxed{59{,}049}$$

### Part 3: At least one pair of consecutive equal digits

By complement: (total) − (no two consecutive equal):

$$90{,}000 - 59{,}049 = \boxed{30{,}951}$$

---

## Problem 13 — All functions from $[3]$ to $[2]$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.1 All Functions|All functions $[m] \to [n]$: $n^m$]] — each element of the domain independently maps to any element of the codomain.

**Count:** $2^3 = 8$ functions total. Below is the complete list (written as $(f(1), f(2), f(3))$):

| $f(1)$ | $f(2)$ | $f(3)$ | Description |
|--------|--------|--------|---|
| 1 | 1 | 1 | Constant function → 1 |
| 1 | 1 | 2 | |
| 1 | 2 | 1 | |
| 1 | 2 | 2 | |
| 2 | 1 | 1 | |
| 2 | 1 | 2 | |
| 2 | 2 | 1 | |
| 2 | 2 | 2 | Constant function → 2 |

---

## Problem 14 — All one-to-one functions from $[2]$ to $[3]$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|Injective functions: $P(n,m) = \dfrac{n!}{(n-m)!}$]]

**Why $P(3,2)$?** Injective means no two domain elements map to the same codomain element — so we pick images *without repetition*. This is exactly counting ordered selections of 2 distinct values from $[3]$.

$$P(3, 2) = 3 \times 2 = 6$$

All 6 injections $\{1, 2\} \to \{1, 2, 3\}$ (written as $(f(1), f(2))$):

$$(1,2),\quad (1,3),\quad (2,1),\quad (2,3),\quad (3,1),\quad (3,2)$$

---

## Problem 15 — All bijections from $[3]$ to $[3]$

**Rule used:** [[1- DM-Basic-Counting-Rules#1.3 Arrangements in a Line (Permutations)|Permutations: $n! = 3! = 6$]]

A bijection from $[3]$ to $[3]$ is a permutation of $\{1,2,3\}$. There are $3! = 6$ such bijections (written in one-line notation $f(1)f(2)f(3)$):

$$123,\quad 132,\quad 213,\quad 231,\quad 312,\quad 321$$

---

## Problem 16 — Number of functions from $[m]$ to $[n]$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.1 All Functions|Product Rule: each domain element independently chooses an image]]

Each of the $m$ elements in the domain maps to any of the $n$ elements in the codomain, independently:

$$\underbrace{n \times n \times \cdots \times n}_{m \text{ times}} = \boxed{n^m}$$

---

## Problem 17 — One-to-one functions from $[2]$ to $[4]$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|$P(4,2) = 4 \times 3 = 12$]]

$f(1)$ maps to any of 4 values; $f(2)$ must differ from $f(1)$, so 3 remaining choices.

$P(4,2) = 12$. All 12 pairs $(f(1), f(2))$:

$$(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)$$

---

## Problem 18 — One-to-one functions from $[3]$ to $[5]$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|$P(n,m)$]]

$$P(5,3) = 5 \times 4 \times 3 = \boxed{60}$$

*Reasoning:* $f(1)$ has 5 choices; $f(2)$ must differ from $f(1)$ → 4 choices; $f(3)$ must differ from both → 3 choices.

---

## Problem 19 — One-to-one functions from $[m]$ to $[n]$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|$k$-permutations formula]]

Generalizing Problems 18–19: we assign distinct images from $[n]$ to $m$ domain elements.

$$P(n,m) = n \times (n-1) \times (n-2) \times \cdots \times (n-m+1) = \frac{n!}{(n-m)!}$$

If $m > n$: impossible (pigeonhole), so $P(n,m) = 0$.

$$\boxed{P(n,m) = \dfrac{n!}{(n-m)!}}$$

---

## Problem 20 — Drawing 1st, 2nd, 3rd card from 52 (ordered)

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$k$-permutations]]

We draw 3 cards in order (the 1st, 2nd, 3rd cards are distinct roles):
- 1st card: 52 choices
- 2nd card: 51 remaining choices
- 3rd card: 50 remaining choices

$$P(52, 3) = 52 \times 51 \times 50 = \boxed{132{,}600}$$

---

## Problem 21 — Drawing 2 cards (order does NOT matter)

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$k$-combinations: unordered selection]]

We want a *set* of 2 cards from 52. Since $\{A\heartsuit, K\spadesuit\}$ and $\{K\spadesuit, A\heartsuit\}$ are the same hand:

$$C(52, 2) = \frac{52 \times 51}{2} = \frac{2652}{2} = \boxed{1326}$$

---

## Problem 22 — Taking $k$ objects from $n$ distinct objects

### (a) Order matters → Permutations

We're choosing an ordered sequence of $k$ distinct objects from $n$:

$$\boxed{P(n,k) = \dfrac{n!}{(n-k)!}}$$

### (b) Order does NOT matter → Combinations

We're choosing an unordered subset of size $k$:

$$\boxed{C(n,k) = \dfrac{n!}{k!\,(n-k)!}}$$

**Relationship:** $C(n,k) = \dfrac{P(n,k)}{k!}$, because each unordered set of $k$ objects corresponds to $k!$ ordered sequences.

---

## Problem 23 — Pass out $k$ distinct fruits to $n$ children, no restriction

**Rule used:** [[1- DM-Basic-Counting-Rules#5.1 All Functions|All functions $[k] \to [n]$]]

Think of each fruit as an element of the domain and each child as an element of the codomain. Distributing fruit $i$ to a child is choosing $f(i)$. There are no restrictions:

- Each of the $k$ fruits independently goes to any of $n$ children.

$$\boxed{n^k}$$

---

## Problem 24 — Pass out $k$ distinct fruits, each child at most one

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|Injective functions]]

"Each child gets at most one fruit" means each child appears at most once as an image → this is an injection from fruits to children.

- **If $k \leq n$:** $P(n,k) = \dfrac{n!}{(n-k)!}$
- **If $k > n$:** There are more fruits than children; by the Pigeonhole Principle it's impossible for each child to receive at most one fruit. Answer: $\mathbf{0}$.

---

## Problem 25 — Pass out $k$ identical fruits, each child at most one

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Combinations]]

Since the fruits are identical, we only care about *which children* receive a fruit (not which specific fruit). We choose $k$ children from $n$ to receive one fruit each.

- **If $k \leq n$:** $C(n,k)$ ways.
- **If $k > n$:** Impossible. Answer: $\mathbf{0}$.

---

## Problem 26 — Bit strings of length $n$ with exactly $k$ zeros

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Combinations]]

A bit string of length $n$ is determined by which positions are 0. We choose $k$ of the $n$ positions to be 0; all others are 1 automatically:

$$\boxed{C(n,k) = \binom{n}{k}}$$

---

## Problem 27 — Tennis club: pairing $2n$ members for singles matches

**Rule used:** [[1- DM-Basic-Counting-Rules#2.3 The Division Rule|Division Rule]] + [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]]

### Part 1: Specify who plays whom (unordered pairs)

**Strategy:** First arrange all $2n$ players in a line, then pair them up consecutively. Then correct for overcounting.

- **Arrange all $2n$ players:** $(2n)!$ ways.
- **Form consecutive pairs:** $(1,2), (3,4), \ldots, (2n-1, 2n)$.
- **Overcounting to remove:**
  - Within each pair: we don't care if it's $(A, B)$ or $(B, A)$ → divide by $2^n$ (one factor of 2 per pair).
  - The order of the pairs themselves doesn't matter (pair #1 vs pair #2 is irrelevant) → divide by $n!$.

$$\frac{(2n)!}{2^n \cdot n!}$$

**Small example ($n=2$, 4 players $\{1,2,3,4\}$):** $\dfrac{4!}{2^2 \cdot 2!} = \dfrac{24}{8} = 3$. Pairings: $\{1,2\}\{3,4\}$; $\{1,3\}\{2,4\}$; $\{1,4\}\{2,3\}$. ✓

$$\boxed{\dfrac{(2n)!}{2^n \cdot n!}}$$

### Part 2: Also specify who serves first

Each of the $n$ pairs now has 2 orderings (player A serves vs. player B serves). Multiply by $2^n$:

$$\frac{(2n)!}{2^n \cdot n!} \times 2^n = \frac{(2n)!}{n!} = \boxed{P(2n, n) \cdot n! / n! \ldots = \dfrac{(2n)!}{n!}}$$

---

## Problem 28 — 3-digit numbers with pairwise different, strictly decreasing digits

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Combinations — choosing a set uniquely determines the number]]

**Key insight:** We need $d_1 > d_2 > d_3$ with $d_1, d_2, d_3$ all distinct digits from $\{0,1,\ldots,9\}$. Once we choose *which 3 digits* to use, there is **exactly one** way to arrange them in strictly decreasing order (the largest first, then middle, then smallest).

**Why the leading digit is automatically non-zero:** Since $d_1 > d_2 > d_3 \geq 0$, we must have $d_1 \geq 2$ (it's larger than two other distinct non-negative integers), so it's never 0.

**Count:** Choose any 3 distinct digits from 10:

$$C(10, 3) = \frac{10 \times 9 \times 8}{3!} = \frac{720}{6} = \boxed{120}$$

---

## Problem 29 — Bijection proving $C(n,k) = C(n, n-k)$

**Rule used:** [[1- DM-Basic-Counting-Rules#2.4 The Bijection Rule|Bijection Rule]]

**Bijection:** Define $f: \{k\text{-subsets of }[n]\} \to \{(n-k)\text{-subsets of }[n]\}$ by:
$$f(A) = [n] \setminus A \quad \text{(complement of } A \text{ in } [n]\text{)}$$

**Why this is a bijection:**
- *Well-defined:* If $|A| = k$, then $|[n] \setminus A| = n - k$. ✓
- *Injective:* If $f(A) = f(B)$, then $[n] \setminus A = [n] \setminus B$, which implies $A = B$. ✓
- *Surjective:* Given any $(n-k)$-subset $B$, let $A = [n] \setminus B$ (a $k$-subset), and $f(A) = B$. ✓
- *Its own inverse:* $f(f(A)) = [n] \setminus ([n] \setminus A) = A$.

Since a bijection exists between the two sets, they have equal cardinality:

$$C(n,k) = C(n, n-k) \qquad \blacksquare$$

---

## Problem 30 — Combinatorial identities (two proofs each)

> **General approach for combinatorial proofs:** Find a set or process that is counted by both sides of the equation.

---

### (a) $\dbinom{2n}{2} = 2\dbinom{n}{2} + n^2$

**Algebraic proof:**

$$\text{LHS} = \binom{2n}{2} = \frac{2n(2n-1)}{2} = n(2n-1) = 2n^2 - n$$

$$\text{RHS} = 2 \cdot \frac{n(n-1)}{2} + n^2 = n(n-1) + n^2 = n^2 - n + n^2 = 2n^2 - n \checkmark$$

**Combinatorial proof (double counting):**

*What are we counting?* 2-element subsets of a $2n$-element set. Split the $2n$ elements into two groups of $n$: group $A = \{1, \ldots, n\}$ and group $B = \{n+1, \ldots, 2n\}$.

- Both elements from $A$: $\binom{n}{2}$ ways
- Both elements from $B$: $\binom{n}{2}$ ways
- One from $A$, one from $B$: $n \times n = n^2$ ways

Total: $\binom{n}{2} + \binom{n}{2} + n^2 = 2\binom{n}{2} + n^2 = \binom{2n}{2}$ $\blacksquare$

---

### (b) $\dbinom{n}{1} + 2\dbinom{n}{2} + 3\dbinom{n}{3} + \cdots + n\dbinom{n}{n} = n \cdot 2^{n-1}$

**Algebraic proof (differentiation of Binomial Theorem):**

Start with the Binomial Theorem: $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$.

Differentiate both sides with respect to $x$:
$$n(1+x)^{n-1} = \sum_{k=1}^n k\binom{n}{k} x^{k-1}$$

Set $x = 1$:
$$n \cdot 2^{n-1} = \sum_{k=1}^n k\binom{n}{k} \checkmark$$

**Combinatorial proof (double counting):**

*What are we counting?* Ordered pairs (committee, designated chair) where the committee is a non-empty subset of $[n]$ and the chair is one member of the committee.

- **Count by committee size:** A committee of size $k$ can be chosen in $\binom{n}{k}$ ways, and any of the $k$ members can be chair → $k\binom{n}{k}$ pairs of this type. Summing over all sizes: $\sum_{k=1}^n k\binom{n}{k}$.

- **Count differently:** First pick the chair ($n$ choices), then the rest of the committee can be any subset of the remaining $n-1$ people (each is included or not: $2^{n-1}$ ways). Total: $n \cdot 2^{n-1}$.

Both expressions count the same thing → $\sum_{k=1}^n k\binom{n}{k} = n \cdot 2^{n-1}$ $\blacksquare$

---

### (c) $n\dbinom{n-1}{2} = \dbinom{n}{2}(n-2)$

**Algebraic proof:**

$$\text{LHS} = n \cdot \frac{(n-1)(n-2)}{2}$$

$$\text{RHS} = \frac{n(n-1)}{2} \cdot (n-2) = \frac{n(n-1)(n-2)}{2}$$

LHS = RHS $\checkmark$

**Combinatorial proof:**

*What are we counting?* Triples $(a, \{b,c\})$ where $a \in [n]$ and $\{b,c\}$ is a 2-element subset of $[n] \setminus \{a\}$.

- **Method 1:** Choose $a$ first ($n$ ways), then choose $\{b,c\}$ from the remaining $n-1$ elements ($\binom{n-1}{2}$ ways): total $n\binom{n-1}{2}$.
- **Method 2:** Choose $\{b,c\}$ first ($\binom{n}{2}$ ways), then choose $a$ from the $n-2$ elements not in $\{b,c\}$: total $\binom{n}{2}(n-2)$.

Both methods count the same set → $n\binom{n-1}{2} = \binom{n}{2}(n-2)$ $\blacksquare$

---

### (d) Pascal's Triangle: $C_n^k = C_{n-1}^k + C_{n-1}^{k-1}$

**Algebraic proof:**

$$C_{n-1}^{k-1} + C_{n-1}^k = \frac{(n-1)!}{(k-1)!(n-k)!} + \frac{(n-1)!}{k!(n-1-k)!}$$

Factor out $\dfrac{(n-1)!}{k!(n-k)!}$:

$$= \frac{(n-1)!}{k!(n-k)!}\big[k + (n-k)\big] = \frac{(n-1)! \cdot n}{k!(n-k)!} = \frac{n!}{k!(n-k)!} = C_n^k \checkmark$$

**Combinatorial proof:**

*What are we counting?* $k$-element subsets of $[n] = \{1, 2, \ldots, n\}$.

Focus on whether element $n$ is in the subset:
- **Subsets containing $n$:** Choose the remaining $k-1$ elements from $\{1, \ldots, n-1\}$: $C_{n-1}^{k-1}$ ways.
- **Subsets NOT containing $n$:** Choose all $k$ elements from $\{1, \ldots, n-1\}$: $C_{n-1}^k$ ways.

These two cases are disjoint and exhaustive → $C_n^k = C_{n-1}^{k-1} + C_{n-1}^k$ $\blacksquare$

---

### (e) $C_n^k \cdot C_k^j = C_n^j \cdot C_{n-j}^{k-j}$

**Algebraic proof:**

$$\text{LHS} = \frac{n!}{k!(n-k)!} \cdot \frac{k!}{j!(k-j)!} = \frac{n!}{j!(k-j)!(n-k)!}$$

$$\text{RHS} = \frac{n!}{j!(n-j)!} \cdot \frac{(n-j)!}{(k-j)!(n-k)!} = \frac{n!}{j!(k-j)!(n-k)!}$$

LHS = RHS $\checkmark$

**Combinatorial proof:**

*What are we counting?* Pairs (committee of $k$, sub-committee of $j$) chosen from $[n]$, where $j \leq k \leq n$.

- **Method 1:** Choose a $k$-committee from $[n]$ first ($C_n^k$ ways), then choose $j$ members of the sub-committee from the $k$-committee ($C_k^j$ ways): LHS.
- **Method 2:** Choose $j$ members for the sub-committee first ($C_n^j$ ways), then choose the remaining $k-j$ members of the full committee from the $n-j$ people not yet selected ($C_{n-j}^{k-j}$ ways): RHS.

$\blacksquare$

---

### (f) $C_n^k \cdot C_{n-k}^j = C_n^j \cdot C_{n-j}^k$

**Algebraic proof:**

$$\text{LHS} = \frac{n!}{k!(n-k)!} \cdot \frac{(n-k)!}{j!(n-k-j)!} = \frac{n!}{k!\,j!\,(n-k-j)!}$$

$$\text{RHS} = \frac{n!}{j!(n-j)!} \cdot \frac{(n-j)!}{k!(n-j-k)!} = \frac{n!}{j!\,k!\,(n-j-k)!}$$

LHS = RHS $\checkmark$

**Combinatorial proof:**

*What are we counting?* Ways to choose two **disjoint** subsets $A$ (size $k$) and $B$ (size $j$) from $[n]$.

- **Method 1:** Choose $A$ first from $[n]$ ($C_n^k$ ways), then choose $B$ from the $n-k$ remaining elements ($C_{n-k}^j$ ways): LHS.
- **Method 2:** Choose $B$ first from $[n]$ ($C_n^j$ ways), then choose $A$ from the $n-j$ remaining elements ($C_{n-j}^k$ ways): RHS.

$\blacksquare$

---

### (g) Vandermonde's Identity: $C_{m+n}^r = \displaystyle\sum_{i=0}^{r} C_m^i \cdot C_n^{r-i}$

**Algebraic proof (Binomial Theorem):**

Consider $(1+x)^{m+n} = (1+x)^m \cdot (1+x)^n$.

- Coefficient of $x^r$ on the left: $C_{m+n}^r$.
- On the right: coefficient of $x^r$ in the product of $\sum_{i} C_m^i x^i$ and $\sum_{j} C_n^j x^j$ is the **convolution** $\sum_{i=0}^r C_m^i \cdot C_n^{r-i}$.

Equating coefficients: $C_{m+n}^r = \sum_{i=0}^r C_m^i \cdot C_n^{r-i}$ $\checkmark$

**Combinatorial proof:**

*What are we counting?* $r$-element subsets of a set of $m+n$ elements, split into group $M$ (size $m$) and group $N$ (size $n$).

For each $i$ from 0 to $r$: choose $i$ elements from $M$ and $r-i$ elements from $N$. The cases (different values of $i$) are mutually exclusive and cover all possibilities:

$$C_{m+n}^r = \sum_{i=0}^r C_m^i \cdot C_n^{r-i} \qquad \blacksquare$$

---
## Problem 31 — Permutations of ABC12DE containing "BC1"

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Treat a forced block as a single element]]

**Setup:** The string "ABC12DE" has 7 distinct characters: A, B, C, 1, 2, D, E.

**Strategy:** Force "BC1" to appear as a consecutive substring by gluing B, C, 1 together into a single "super-character". Now our arrangement consists of:

$$\{\underbrace{A},\ \underbrace{[BC1]},\ \underbrace{2},\ \underbrace{D},\ \underbrace{E}\} \quad \leftarrow \text{5 distinct objects}$$

**Count:** Arrange 5 distinct objects in a line:

$$5! = 120$$

**Why this is correct:** Every arrangement of these 5 objects gives a 7-character string containing "BC1" consecutively (the super-character expands back into B, C, 1 in that order). Different arrangements give different strings. ✓

$$\boxed{120}$$

---

## Problem 32 — Alternating men and women in a row ($n$ men, $n$ women)

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] + [[1- DM-Basic-Counting-Rules#1.3 Arrangements in a Line (Permutations)|$n!$ permutations]]

**Two alternating patterns are possible:**
- **MWMWMW…** (man first, then woman, alternating)
- **WMWMWM…** (woman first, then man, alternating)

**For each pattern:**
- Arrange the $n$ men in the $n$ "man-slots": $n!$ ways
- Arrange the $n$ women in the $n$ "woman-slots": $n!$ ways

**Total:**

$$2 \times n! \times n! = \boxed{2(n!)^2}$$

**Example ($n=2$, 4 people M1, M2, W1, W2):** $2 \times 2! \times 2! = 8$ arrangements. ✓

---

## Problem 33 — Class of 25, choosing students for competitions

**Rule used:** Combinations vs. Permutations — the key question is whether the roles are distinguishable.

### Part 1: 3 students for Calculus (same competition, no roles)

The three students all participate in the same competition → their selection is **unordered**. Use combinations:

$$C(25, 3) = \frac{25 \times 24 \times 23}{3!} = \frac{13{,}800}{6} = \boxed{2300}$$

### Part 2: 3 students for 3 different competitions (distinct roles)

The three roles are different (Calculus, Algebra, Discrete Math) → selection is **ordered**. Use permutations:

$$P(25, 3) = 25 \times 24 \times 23 = \boxed{13{,}800}$$

**Why $P = 6 \times C$?** Each unordered group of 3 students can be assigned to the three competitions in $3! = 6$ ways, so $P(25,3) = 6 \times C(25,3)$.

---

## Problem 34 — Soccer team of 11 from 9 females + 20 males

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] + Complement method

### Part (a): Exactly 3 female students

- Choose 3 females from 9: $C(9, 3) = \dfrac{9 \times 8 \times 7}{6} = 84$
- Choose remaining $11 - 3 = 8$ players from 20 males: $C(20, 8) = 125{,}970$

$$84 \times 125{,}970 = \boxed{10{,}581{,}480}$$

### Part (b): At least 1 female student

**Use complement:** Total teams minus all-male teams.

- Total teams from $9 + 20 = 29$ people: $C(29, 11) = 20{,}030{,}010$
- All-male teams (11 males from 20): $C(20, 11) = 167{,}960$

$$20{,}030{,}010 - 167{,}960 = \boxed{19{,}862{,}050}$$

---

## Problem 35 — Bit strings of length 7: starts with 0 OR ends with 10

**Rule used:** [[2- DM-Advanced-Counting#13. Two-Set and Three-Set PIE|Inclusion-Exclusion Principle (PIE) for two sets]]

**Define:**
- $A$ = {bit strings of length 7 that start with 0}
- $B$ = {bit strings of length 7 that end with "10"}

**Count each set:**

| Set        | Fixed bits                   | Free bits              | Size       |
| ---------- | ---------------------------- | ---------------------- | ---------- |
| $A$        | position 1 = 0               | positions 2–7 (6 free) | $2^6 = 64$ |
| $B$        | positions 6–7 = "10"         | positions 1–5 (5 free) | $2^5 = 32$ |
| $A \cap B$ | pos 1 = 0 AND pos 6–7 = "10" | positions 2–5 (4 free) | $2^4 = 16$ |

**Apply PIE:**

$$|A \cup B| = |A| + |B| - |A \cap B| = 64 + 32 - 16 = \boxed{80}$$

---

## Problem 36 — Pascal's triangle: two rows after $\binom{10}{k}$

**Rule used:** [[1- DM-Basic-Counting-Rules#3.1 Pascal's Theorem|Pascal's Identity]]: $C(n,k) = C(n-1,k-1) + C(n-1,k)$

Each entry in the new row is the sum of the two entries directly above it.

**Row 10 (given):** $1\quad 10\quad 45\quad 120\quad 210\quad 252\quad 210\quad 120\quad 45\quad 10\quad 1$

**Row 11** (each entry = left-above + right-above):
$$1 \quad 11 \quad 55 \quad 165 \quad 330 \quad 462 \quad 462 \quad 330 \quad 165 \quad 55 \quad 11 \quad 1$$

*Verification:* $1+10=11$, $10+45=55$, $45+120=165$, $120+210=330$, $210+252=462$, $252+210=462$, … ✓

**Row 12:**
$$1 \quad 12 \quad 66 \quad 220 \quad 495 \quad 792 \quad 924 \quad 792 \quad 495 \quad 220 \quad 66 \quad 12 \quad 1$$

*Verification:* $1+11=12$, $11+55=66$, $55+165=220$, $165+330=495$, $330+462=792$, $462+462=924$, … ✓

---

## Problem 37 — Coefficient of $x^{101}y^{99}$ in $(2x - 3y)^{200}$

**Rule used:** [[1- DM-Basic-Counting-Rules#3.2 Binomial Theorem|Binomial Theorem]]: $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$

**Step-by-step:**

Write $(2x - 3y)^{200} = \sum_{k=0}^{200} \binom{200}{k}(2x)^k(-3y)^{200-k}$.

The general term is:

$$\binom{200}{k}(2)^k(-3)^{200-k} x^k y^{200-k}$$

We need $k = 101$ and $200 - k = 99$ for the term $x^{101}y^{99}$. Check: $101 + 99 = 200$ ✓.

$$\text{Coefficient} = \binom{200}{101}(2)^{101}(-3)^{99}$$

Since $(-3)^{99} < 0$ (odd power), the coefficient is **negative**:

$$\boxed{-\binom{200}{101} \cdot 2^{101} \cdot 3^{99}}$$

---

## Problem 38 — Coefficient of $x^k$ in $\left(x + \dfrac{1}{x}\right)^{100}$

**Rule used:** [[1- DM-Basic-Counting-Rules#3.2 Binomial Theorem|Binomial Theorem]]

**Step-by-step:**

$$\left(x + \frac{1}{x}\right)^{100} = \sum_{j=0}^{100} \binom{100}{j} x^j \cdot \left(\frac{1}{x}\right)^{100-j} = \sum_{j=0}^{100} \binom{100}{j} x^j \cdot x^{-(100-j)} = \sum_{j=0}^{100} \binom{100}{j} x^{2j-100}$$

The power of $x$ in term $j$ is $2j - 100$.

**Setting $2j - 100 = k$:** Solve for $j$: $j = \dfrac{k + 100}{2}$.

For $j$ to be a valid integer index ($0 \leq j \leq 100$), we need:
- $k + 100$ must be even, so $k$ must be **even**.
- $0 \leq \dfrac{k+100}{2} \leq 100 \Rightarrow -100 \leq k \leq 100$.

$$\text{Coefficient of } x^k = \begin{cases} \dbinom{100}{\frac{k+100}{2}} & \text{if } k \text{ is even and } -100 \leq k \leq 100 \\ 0 & \text{otherwise} \end{cases}$$

---

## Problem 39 — Coefficient of $x^{101}y^{99}z^{105}$ in $(2x-3y-z)^{305}$

**Rule used:** [[1- DM-Basic-Counting-Rules#3.3 Multinomial Theorem|Multinomial Theorem]]

The Multinomial Theorem states: the coefficient of $x_1^{r_1} x_2^{r_2} x_3^{r_3}$ in $(c_1 x_1 + c_2 x_2 + c_3 x_3)^n$ is:
$$\frac{n!}{r_1!\, r_2!\, r_3!} \cdot c_1^{r_1} \cdot c_2^{r_2} \cdot c_3^{r_3}$$

**Step-by-step:** Here $n = 305$, $r_1 = 101$ (for $x$), $r_2 = 99$ (for $y$), $r_3 = 105$ (for $z$). Check: $101 + 99 + 105 = 305$ ✓.

The coefficients: $c_1 = 2$, $c_2 = -3$, $c_3 = -1$.

$$\text{Coefficient} = \frac{305!}{101!\,99!\,105!} \cdot 2^{101} \cdot (-3)^{99} \cdot (-1)^{105}$$

**Sign:** $(-3)^{99}$ is negative (odd power); $(-1)^{105}$ is also negative (odd power). Negative × negative = **positive**. So:

$$\boxed{\frac{305!}{101!\,99!\,105!} \cdot 2^{101} \cdot 3^{99}}$$

---

## Problem 40 — Painting 10 distinct chairs: 3 green, 3 blue, 4 red

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient]]

**Intuition:** We're arranging 10 chairs where 3 are "identical green", 3 are "identical blue", and 4 are "identical red". This is like arranging the string GGGBBBRRRR.

**Formula:** Number of ways to partition $n$ distinct objects into groups of sizes $n_1, n_2, n_3$ (each group is interchangeable within itself):

$$\frac{10!}{3!\,3!\,4!}$$

**Computing:**
$$\frac{10!}{3!\,3!\,4!} = \frac{3{,}628{,}800}{6 \times 6 \times 24} = \frac{3{,}628{,}800}{864} = \boxed{4200}$$

---

## Problem 41 — Lattice paths from $(0,0)$ to $(m,n)$

**Rule used:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Choosing which steps are horizontal]]

**Setup:** Any path from $(0,0)$ to $(m,n)$ using unit steps consists of exactly:
- $m$ steps to the right (R), and
- $n$ steps up (U),

for a total of $m + n$ steps.

**Key insight:** The path is completely determined by *which of the $m+n$ steps are R* (the rest are automatically U). This is choosing $m$ positions out of $m+n$:

$$\binom{m+n}{m} = \binom{m+n}{n}$$

**Example:** $(m,n) = (2,2)$: paths are RRUU, RURU, RUUR, URRU, URUR, UURR → $C(4,2)=6$. ✓

$$\boxed{C(m+n,\,m)}$$

---

## Problem 42 — True or False: $\binom{n}{k} = \binom{n-2}{k-2} + \binom{n-2}{k-1} + \binom{n-2}{k}$

**Answer: FALSE** in general.

**Derivation of what the right formula is:** Apply Pascal's Identity ($C_{n}^k = C_{n-1}^{k-1} + C_{n-1}^k$) twice:

Step 1: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$

Step 2: Apply Pascal to each term:
$$\binom{n-1}{k-1} = \binom{n-2}{k-2} + \binom{n-2}{k-1}$$
$$\binom{n-1}{k} = \binom{n-2}{k-1} + \binom{n-2}{k}$$

Adding:
$$\binom{n}{k} = \binom{n-2}{k-2} + \mathbf{2}\binom{n-2}{k-1} + \binom{n-2}{k}$$

The correct formula has a coefficient of **2** on the middle term, not 1. So the stated identity is false.

**Counterexample:** $n=4$, $k=2$:
- LHS: $\binom{4}{2} = 6$
- RHS (as stated): $\binom{2}{0} + \binom{2}{1} + \binom{2}{2} = 1 + 2 + 1 = 4 \neq 6$. ✗

$$\boxed{\textbf{FALSE}}$$

---

## Problem 43 — Distinct strings from CASABLANCA

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient for repeated letters]]

**Step 1 — Count each letter:**
$$\text{C-A-S-A-B-L-A-N-C-A} \implies \text{A: 4, C: 2, S: 1, B: 1, L: 1, N: 1}$$

Total letters: $4 + 2 + 1 + 1 + 1 + 1 = 10$ ✓

**Step 2 — Apply the formula:** Divide total arrangements by the factorials of each letter's count:

$$\frac{10!}{4!\,2!\,1!\,1!\,1!\,1!} = \frac{3{,}628{,}800}{24 \times 2 \times 1 \times 1 \times 1 \times 1} = \frac{3{,}628{,}800}{48} = \boxed{75{,}600}$$

---

## Problem 44 — Distinct strings from SUCCESS

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient]]

**Step 1 — Count each letter:**
$$\text{S-U-C-C-E-S-S} \implies \text{S: 3, U: 1, C: 2, E: 1}$$

Total: $3 + 1 + 2 + 1 = 7$ ✓

**Step 2:**

$$\frac{7!}{3!\,1!\,2!\,1!} = \frac{5040}{6 \times 1 \times 2 \times 1} = \frac{5040}{12} = \boxed{420}$$

---

## Problem 45 — Coefficient of $x^3y^2z^5$ in $(2x - 3y - 2z)^{10}$

**Rule used:** [[1- DM-Basic-Counting-Rules#3.3 Multinomial Theorem|Multinomial Theorem]]

**Check powers:** $r_1 = 3$, $r_2 = 2$, $r_3 = 5$. Sum: $3+2+5=10$ ✓.

**Coefficients:** $c_1 = 2$, $c_2 = -3$, $c_3 = -2$.

**Applying the formula:**
$$\text{Coefficient} = \frac{10!}{3!\,2!\,5!} \cdot 2^3 \cdot (-3)^2 \cdot (-2)^5$$

**Computing each part:**
$$\frac{10!}{3!\,2!\,5!} = \frac{3{,}628{,}800}{6 \times 2 \times 120} = \frac{3{,}628{,}800}{1440} = 2520$$

$$2^3 = 8, \quad (-3)^2 = 9, \quad (-2)^5 = -32$$

$$2520 \times 8 \times 9 \times (-32) = 2520 \times 8 \times (-288) = 2520 \times (-2304) = \boxed{-5{,}806{,}080}$$

---

## Problem 46 — Lining up 3 red + 2 golden apples (identical within color)

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient]]

Since apples of the same color are identical, we only care about *where* each color goes:

$$\frac{(3+2)!}{3!\,2!} = \frac{5!}{3!\,2!} = \frac{120}{12} = \boxed{10}$$

*These 10 arrangements correspond to choosing 3 of the 5 positions for the red apples.*

---

## Problem 47 — Lining up 3 red + 2 golden + 4 green apples

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient]]

$$\frac{(3+2+4)!}{3!\,2!\,4!} = \frac{9!}{3!\,2!\,4!} = \frac{362{,}880}{6 \times 2 \times 24} = \frac{362{,}880}{288} = \boxed{1260}$$

---

## Problem 48 — Distribute $k$ indistinguishable apples to $n$ children

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars Theorem]]

**Translation to equation:** If child $i$ gets $x_i$ apples, then $x_1 + x_2 + \cdots + x_n = k$ where each $x_i \geq 0$.

**Stars and Bars:** Think of $k$ stars (apples) and $n-1$ dividers (bars) separating the $n$ groups. We arrange $k$ stars and $n-1$ bars in a line: $k + (n-1) = k+n-1$ total positions, choose which $k$ are stars:

$$\boxed{C(n+k-1,\,k)}$$

**Example:** $k=3$ apples, $n=2$ children: $C(4,3) = 4$ distributions: $(0,3),(1,2),(2,1),(3,0)$ ✓

---

## Problem 49 — Place $k$ indistinguishable books onto $n$ shelves

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars]]

Identical to Problem 48 — distributing $k$ identical objects into $n$ distinct bins with no restrictions:

$$\boxed{C(n+k-1,\,k)}$$

---

## Problem 50 — Non-negative solutions of $x_1 + x_2 + \cdots + x_n = k$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars Theorem]]

This is the same as distributing $k$ identical objects into $n$ bins. By Stars and Bars:

$$\boxed{C(n+k-1,\,k) = C(n+k-1,\,n-1)}$$

*(Both expressions are equal by the symmetry $C(N,k) = C(N, N-k)$.)*

---

## Problem 51 — Positive integer solutions of $x_1 + x_2 + \cdots + x_n = k$ ($x_i \geq 1$)

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]]

**Strategy:** Substitute $y_i = x_i - 1 \geq 0$ (shift each variable down by 1). Then:
$$\sum_{i=1}^n (y_i + 1) = k \implies \sum_{i=1}^n y_i = k - n$$

This is a non-negative integer equation with sum $k-n$. It has solutions only when $k \geq n$.

$$\text{Number of solutions} = C((k-n)+n-1, k-n) = C(k-1, n-1)$$

$$\boxed{C(k-1,\,n-1)} \quad \text{(valid only when } k \geq n\text{)}$$

---

## Problem 52 — Distribute $k$ identical apples to $n$ children, each gets $\geq 1$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Same substitution as Problem 51]]

Same calculation as Problem 51 (different wording, same math):

$$\boxed{C(k-1,\,n-1)} \quad \text{(valid only when } k \geq n \text{)}$$

---

## Problem 53 — Circular arrangement of $n$ red and $n+1$ black checkers

**Rule used:** [[1- DM-Basic-Counting-Rules#1.4 Arrangements at a Round Table|Circular permutations with identical objects]]

**Total checkers:** $n + (n+1) = 2n+1$.

**Fixing one to remove rotational equivalence:** In circular arrangements, rotations are considered the same. Fix one black checker's position (since all blacks are identical, this removes all rotational equivalences). Now arrange the remaining $2n$ checkers — consisting of $n$ red and $n$ black ones — in the remaining $2n$ positions:

$$\frac{(2n)!}{n!\,n!} = \boxed{C(2n,\,n)}$$

---

## Problem 54 — Solutions of $x_1+x_2+x_3+x_4+x_5=21$ with constraints

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]] + [[2- DM-Advanced-Counting#14. General PIE|PIE for upper bounds]]

### Part (a): $x_i \geq 1$ for all $i$

**Substitution:** Let $y_i = x_i - 1 \geq 0$. Then $\sum y_i = 21 - 5 = 16$.

$$C(16+4, 4) = C(20, 4) = \frac{20 \times 19 \times 18 \times 17}{4!} = \frac{116{,}280}{24} = \boxed{4845}$$

### Part (b): $x_i \geq 2$ for all $i$

**Substitution:** Let $y_i = x_i - 2 \geq 0$. Then $\sum y_i = 21 - 10 = 11$.

$$C(11+4, 4) = C(15, 4) = \frac{15 \times 14 \times 13 \times 12}{4!} = \frac{32{,}760}{24} = \boxed{1365}$$

### Part (c): $0 \leq x_1 \leq 10$ (others unrestricted, $x_i \geq 0$)

**Strategy:** Unconstrained count minus violations (where $x_1 \geq 11$).

**Unconstrained** ($x_i \geq 0$): $C(21+4, 4) = C(25, 4) = \dfrac{25 \times 24 \times 23 \times 22}{24} = 12{,}650$

**Violating** ($x_1 \geq 11$): Substitute $x_1' = x_1 - 11 \geq 0$, so $\sum x_i' = 10$:
$$C(10+4,4) = C(14,4) = \frac{14 \times 13 \times 12 \times 11}{24} = 1001$$

**Answer:**

$$12{,}650 - 1{,}001 = \boxed{11{,}649}$$

---

## Problem 55 — Non-negative solutions of $x_1+x_2+x_3 \leq 11$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with slack variable]]

**Trick:** Convert the inequality to an equation by introducing a "slack variable" $x_4 \geq 0$:
$$x_1 + x_2 + x_3 + x_4 = 11, \quad x_1, x_2, x_3, x_4 \geq 0$$

Each solution to the original inequality corresponds to exactly one solution here (with $x_4$ absorbing the "slack"). By Stars and Bars with $n=4$ variables and sum $= 11$:

$$C(11+3, 3) = C(14, 3) = \frac{14 \times 13 \times 12}{6} = \boxed{364}$$

---

## Problem 56 — Which collections are partitions of $\mathbb{R}$?

> **Partition of a set $X$:** A collection of non-empty subsets that are pairwise disjoint and whose union is all of $X$.

**(a)** Positive integers + negative integers: **NOT a partition** of $\mathbb{R}$.
- Missing all non-integers (e.g., $\sqrt{2}$, $0.5$) and missing $0$.

**(b)** Non-positive integers + non-negative integers: **NOT a partition** of $\mathbb{R}$.
- Both sets contain 0 (not disjoint). Also, non-integers like $0.5$ are missing entirely.

**(c)** Rationals + irrationals: **YES — this is a partition** of $\mathbb{R}$.
- Every real number is either rational or irrational (not both) — they cover all of $\mathbb{R}$ and are disjoint.

**(d)** Closed intervals $[n, n+1]$ for $n \in \mathbb{Z}$: **NOT a partition** of $\mathbb{R}$.
- Adjacent intervals overlap at endpoints: e.g., $1 \in [0,1]$ and $1 \in [1,2]$. So the collection is not disjoint.

**(e)** Half-open intervals $(n, n+1]$ for $n \in \mathbb{Z}$: **YES — this is a partition** of $\mathbb{R}$.
- Each real number $x$ belongs to exactly one interval $(n, n+1]$ where $n = \lfloor x \rfloor - 1$ if $x$ is an integer, and $n = \lfloor x \rfloor$ otherwise. (Specifically: $x \in (n, n+1]$ iff $n < x \leq n+1$.) They are disjoint (left endpoints are open) and cover all of $\mathbb{R}$.

---

## Problem 57 — All partitions of $[4]$; Stirling numbers; Bell number

**Rule used:** [[1- DM-Basic-Counting-Rules#6.1 Definitions: Partitions and Stirling Numbers|Stirling numbers $S(n,k)$ and Bell numbers]]

### $k = 1$ partition (all elements in one block):
$$\{\{1,2,3,4\}\} \quad \Rightarrow \quad S(4,1) = 1$$

### $k = 2$ partitions (7 total):
$$\{1\}|\{2,3,4\}, \quad \{2\}|\{1,3,4\}, \quad \{3\}|\{1,2,4\}, \quad \{4\}|\{1,2,3\}$$
$$\{1,2\}|\{3,4\}, \quad \{1,3\}|\{2,4\}, \quad \{1,4\}|\{2,3\}$$
$$S(4,2) = 7 = 2^{4-1} - 1 = 7 \checkmark$$

### $k = 3$ partitions (6 total — one pair + two singletons):
$$\{1,2\}|\{3\}|\{4\}, \quad \{1,3\}|\{2\}|\{4\}, \quad \{1,4\}|\{2\}|\{3\}$$
$$\{2,3\}|\{1\}|\{4\}, \quad \{2,4\}|\{1\}|\{3\}, \quad \{3,4\}|\{1\}|\{2\}$$
$$S(4,3) = 6 = C(4,2) = 6 \checkmark$$

### $k = 4$ partition (all singletons):
$$\{1\}|\{2\}|\{3\}|\{4\} \quad \Rightarrow \quad S(4,4) = 1$$

### 4th Bell number:
$$B(4) = S(4,1) + S(4,2) + S(4,3) + S(4,4) = 1 + 7 + 6 + 1 = \boxed{15}$$

---

## Problem 58 — General values $S(n,1)$, $S(n,n-1)$, $S(n,n)$

**Rule used:** [[1- DM-Basic-Counting-Rules#6.2 Recurrence and Special Values|Special values of Stirling numbers of the second kind]]

**$S(n,1) = 1$:** There is only one way to put all $n$ elements into 1 non-empty block — put all of them together.

**$S(n,n) = 1$:** There is only one way to partition $n$ elements into $n$ blocks — each element forms its own singleton block.

**$S(n, n-1) = C(n,2) = \dfrac{n(n-1)}{2}$:** If we need $n-1$ blocks from $n$ elements, exactly one block must have 2 elements (and the other $n-2$ blocks are singletons). We just choose which 2 elements are paired:

$$S(n, n-1) = \binom{n}{2}$$

---

## Problem 59 — Recurrence for $S(n,k)$ and closed form for $S(n,2)$

**Rule used:** [[1- DM-Basic-Counting-Rules#6.2 Recurrence and Special Values|Stirling number recurrence]]

### Recurrence derivation

Consider element $n$ in a partition of $[n]$ into $k$ blocks. Two cases:

- **Case 1:** $\{n\}$ is its own singleton block. The remaining $n-1$ elements form a partition of $[n-1]$ into $k-1$ blocks: $S(n-1, k-1)$ ways.
- **Case 2:** $n$ joins one of $k$ existing blocks of a partition of $[n-1]$ into $k$ blocks. There are $k$ existing blocks to add $n$ to, so: $k \cdot S(n-1, k)$ ways.

$$\boxed{S(n,k) = S(n-1, k-1) + k \cdot S(n-1, k)}$$

### Closed form for $S(n,2)$

Applying the recurrence with $k=2$:
$$S(n,2) = S(n-1, 1) + 2 \cdot S(n-1, 2) = 1 + 2 \cdot S(n-1, 2)$$

with $S(2,2) = 1$ (base case: partition $\{1\}|\{2\}$).

Solving the recurrence $a_n = 1 + 2a_{n-1}$, $a_2 = 1$:
- $a_3 = 1 + 2(1) = 3$
- $a_4 = 1 + 2(3) = 7$
- $a_5 = 1 + 2(7) = 15 = 2^4 - 1$

**General formula:** $S(n,2) = 2^{n-1} - 1$

*Formal proof:* Substitute $b_n = S(n,2) + 1$: then $b_n = 2b_{n-1}$, $b_2 = 2$, so $b_n = 2^{n-1}$, giving $S(n,2) = 2^{n-1} - 1$.

$$\boxed{S(n,2) = 2^{n-1} - 1}$$

---

## Problem 60 — Bijection: partitions of $[n]$ into 2 parts ↔ non-empty subsets of $[n-1]$

**Rule used:** [[1- DM-Basic-Counting-Rules#2.4 The Bijection Rule|Bijection Rule]]

**Goal:** Show $S(n,2) = 2^{n-1} - 1$ by giving an explicit bijection.

**Bijection:** Given a 2-partition $\{A, B\}$ of $[n]$, exactly one of $A$ or $B$ contains $n$. WLOG say $n \in A$. Map this partition to the set $B = [n] \setminus A$ (the block that does NOT contain $n$).

- $B$ is non-empty (because otherwise $A = [n]$ and the "other block" is empty, but we need two non-empty blocks).
- $B \subseteq [n-1]$ (since $n \in A$, $B$ contains no $n$).
- The map is invertible: given any non-empty $B \subseteq [n-1]$, define $A = [n] \setminus B$ (which contains $n$), and this gives a valid 2-partition $\{A, B\}$.

**Conclusion:** The number of 2-partitions of $[n]$ equals the number of non-empty subsets of $[n-1]$, which is $2^{n-1} - 1$. $\blacksquare$

---

## Problem 61 — Which collections are partitions of $\{1,2,3,4,5,6\}$?

**(a)** $\{1,2\},\ \{2,3,4\},\ \{4,5,6\}$: **NOT a partition**. Element 2 appears in both $\{1,2\}$ and $\{2,3,4\}$ (not disjoint); element 4 appears in $\{2,3,4\}$ and $\{4,5,6\}$ (not disjoint).

**(b)** $\{1\},\ \{2,3,6\},\ \{4\}$: **NOT a partition**. Element 5 is missing from the union.

**(c)** $\{2,4,6\},\ \{1,3,5\}$: **YES — a valid partition**. The two sets are disjoint, non-empty, and their union is $\{1,2,3,4,5,6\}$. ✓

**(d)** $\{1,4,5\},\ \{2,6\}$: **NOT a partition**. Element 3 is missing.

---

## Problem 62 — Place 4 distinct gifts into 3 identical boxes (some boxes may be empty)

**Rule used:** [[1- DM-Basic-Counting-Rules#6.1 Definitions: Partitions and Stirling Numbers|Stirling numbers of the second kind]]

**Key:** Boxes are identical → we're partitioning the 4 gifts into **at most 3** non-empty groups. (Empty boxes are allowed, so 1 or 2 boxes may be empty.)

$$\sum_{k=1}^{3} S(4,k) = S(4,1) + S(4,2) + S(4,3) = 1 + 7 + 6 = \boxed{14}$$

---

## Problem 63 — 4 distinct gifts into 3 identical boxes, each box has $\geq 1$ gift

**Rule used:** [[1- DM-Basic-Counting-Rules#6.1 Definitions: Partitions and Stirling Numbers|Stirling number $S(4,3)$]]

Now all 3 boxes must be non-empty → exactly 3 non-empty groups → $S(4,3)$.

$$S(4,3) = C(4,2) = 6$$

(One pair of gifts goes in one box; the other 2 gifts each go in separate boxes. Choose which pair: $C(4,2) = 6$.)

$$\boxed{6}$$

---

## Problem 64 — Place 4 identical gifts into 3 identical boxes (some empty ok)

**Rule used:** Integer partitions of 4 into **at most 3** parts

Since both gifts and boxes are identical, we only care about how many gifts are in each box, not which gifts or which boxes. This is equivalent to partitions of 4 using at most 3 parts:

| Distribution (sorted) | Partition |
|---|---|
| All in one box: $(4,0,0)$ | 4 |
| Split 3+1: $(3,1,0)$ | 3+1 |
| Split 2+2: $(2,2,0)$ | 2+2 |
| Split 2+1+1: $(2,1,1)$ | 2+1+1 |

$$\boxed{4 \text{ ways}}$$

Note: $(1,1,1,1)$ would need 4 boxes, so it's not included.

---

## Problem 65 — 4 identical gifts into 3 identical boxes, each box $\geq 1$

**Rule used:** Integer partitions of 4 into **exactly 3** positive parts

Each box must receive at least 1 gift. The parts must sum to 4 with all parts $\geq 1$:

$(2,1,1)$ is the only partition of 4 into exactly 3 positive parts.

*(Check: $(1+1+1 = 3 \neq 4)$; $(3+1+1 = 5 \neq 4)$; $(2+2+1 = 5 \neq 4)$; only $2+1+1=4$ ✓)*

$$\boxed{1 \text{ way}}$$

---

## Problem 66 — Place 15 distinct gifts into 10 distinct boxes (no restrictions)

**Rule used:** [[1- DM-Basic-Counting-Rules#5.1 All Functions|All functions: $n^k$]]

Each of 15 distinct gifts independently goes into any of 10 distinct boxes.

$$10^{15} = \boxed{10^{15}}$$

---

## Problem 67 — 15 distinct gifts into 10 distinct boxes, each box $\geq 1$

**Rule used:** [[2- DM-Advanced-Counting#15.2 Number of Onto (Surjective) Functions|Surjection formula (PIE)]]

Each box must have at least 1 gift = the distribution function is surjective (onto). Using PIE:

$$\text{Surjections from } [15] \to [10] = \sum_{j=0}^{10} (-1)^j \binom{10}{j}(10-j)^{15}$$

$$= \binom{10}{0}10^{15} - \binom{10}{1}9^{15} + \binom{10}{2}8^{15} - \cdots + (-1)^{10}\binom{10}{10}0^{15}$$

This equals $10! \cdot S(15, 10)$ where $S(15,10)$ is the Stirling number of the second kind.

$$\boxed{\sum_{j=0}^{10}(-1)^j \binom{10}{j}(10-j)^{15}}$$

---

## Problem 68 — 15 distinct gifts into 10 distinct boxes, each box $\leq 1$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|Injective functions / $P(n,k)$]]

"At most 1 gift per box" = the assignment is an **injection** from 15 gifts into 10 boxes.

But wait: $15 > 10$, so we cannot inject 15 elements into 10 boxes with each box having at most 1!

$$\boxed{0}$$

*(By the Pigeonhole Principle: 15 gifts but only 10 boxes — at least one box must have $\geq 2$ gifts.)*

---

## Problem 69 — 10 distinct gifts into 15 distinct boxes, each box $\leq 1$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|Injective functions / $P(n,k)$]]

"At most 1 gift per box" with $10 < 15$ = injection from 10 gifts into 15 boxes.

The number of injections from a 10-element set to a 15-element set:

$$P(15, 10) = 15 \times 14 \times 13 \times \cdots \times 6 = \frac{15!}{5!} = \boxed{\dfrac{15!}{5!}}$$

---

## Problem 70 — 100 identical gifts into 3 distinct boxes

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars]]

Identical gifts into distinct boxes, no restrictions. This is non-negative integer solutions to $x_1 + x_2 + x_3 = 100$:

$$C(100 + 2,\, 2) = C(102, 2) = \frac{102 \times 101}{2} = \boxed{5151}$$

---

## Problem 71 — 100 identical gifts into 10 distinct boxes, each box $\geq 5$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]]

**Substitution:** Let $y_i = x_i - 5 \geq 0$. Then $\sum y_i = 100 - 50 = 50$.

$$C(50 + 9,\, 9) = C(59, 9) = \boxed{C(59,9)}$$

*(Numerical value: $C(59,9) = 14{,}783{,}142{,}660$)*

---

## Problem 72 — All permutations of $[4]$ mapping $1 \to 3$

**Rule used:** Fix one value and freely permute the rest.

If $\sigma(1) = 3$ is fixed, then elements $\{2, 3, 4\}$ must map to $\{1, 2, 4\}$ in some order (since 3 is already used as the image of 1).

That gives $3! = 6$ permutations. In one-line notation (form: $3, \sigma(2), \sigma(3), \sigma(4)$):

| $\sigma(2)$ | $\sigma(3)$ | $\sigma(4)$ | One-line |
|---|---|---|---|
| 1 | 2 | 4 | 3124 |
| 1 | 4 | 2 | 3142 |
| 2 | 1 | 4 | 3214 |
| 2 | 4 | 1 | 3241 |
| 4 | 1 | 2 | 3412 |
| 4 | 2 | 1 | 3421 |

---

## Problem 73 — Permutations of $[5]$ with $\sigma(5) = 5$ and $\sigma(3) = 2$

**Strategy:** Two values are fixed. Determine what's left.

- $\sigma(5) = 5$ and $\sigma(3) = 2$ are fixed.
- Images used so far: $\{2, 5\}$.
- Remaining domain elements: $\{1, 2, 4\}$.
- Remaining available images: $\{1, 3, 4, 5\} \setminus \{5\} = \{1, 3, 4\}$ ... wait. Images $\{2, 5\}$ are taken, so remaining images from $\{1,2,3,4,5\}$ are $\{1, 3, 4\}$.
- Assign $\sigma(1), \sigma(2), \sigma(4)$ as a permutation of $\{1,3,4\}$: $3! = 6$ ways.

All 6 in two-line notation:

$$\begin{pmatrix}1&2&3&4&5\end{pmatrix}$$
$$\sigma(1) \in \{1,3,4\},\ \sigma(2) \in \{1,3,4\},\ \sigma(3)=2,\ \sigma(4) \in \{1,3,4\},\ \sigma(5)=5$$

| $\sigma(1)$ | $\sigma(2)$ | One-line $\sigma(1)\sigma(2)\ 2\ \sigma(4)\ 5$ |
|---|---|---|
| 1 | 3 | $1\ 3\ 2\ 4\ 5$ |
| 1 | 4 | $1\ 4\ 2\ 3\ 5$ |
| 3 | 1 | $3\ 1\ 2\ 4\ 5$ |
| 3 | 4 | $3\ 4\ 2\ 1\ 5$ |
| 4 | 1 | $4\ 1\ 2\ 3\ 5$ |
| 4 | 3 | $4\ 3\ 2\ 1\ 5$ |

---

## Problem 74 — Cycle notation, fixed points, inverse, square

> **How to find cycles:** Start at element 1, follow the map ($1 \to \sigma(1) \to \sigma(\sigma(1)) \to \ldots$) until you return to 1. Then pick the smallest unvisited element and repeat.

### (a) $\sigma = 36215847$ on $[8]$

Reading the one-line notation: $\sigma(1)=3, \sigma(2)=6, \sigma(3)=2, \sigma(4)=1, \sigma(5)=5, \sigma(6)=8, \sigma(7)=4, \sigma(8)=7$.

**Find cycles:**
- Start at 1: $1 \to 3 \to 2 \to 6 \to 8 \to 7 \to 4 \to 1$ → cycle $(1\ 3\ 2\ 6\ 8\ 7\ 4)$ (length 7)
- Next unvisited: 5 → $5 \to 5$ → fixed point $(5)$

**Cycle notation:** $(1\ 3\ 2\ 6\ 8\ 7\ 4)(5)$
**Fixed points:** $\{5\}$
**Number of cycles:** 2

**Inverse $\sigma^{-1}$:** Reverse each cycle:
$(1\ 3\ 2\ 6\ 8\ 7\ 4)^{-1} = (1\ 4\ 7\ 8\ 6\ 2\ 3)$

One-line notation of $\sigma^{-1}$: $\sigma^{-1}(1)=4, \sigma^{-1}(2)=3, \sigma^{-1}(3)=1, \sigma^{-1}(4)=7, \sigma^{-1}(5)=5, \sigma^{-1}(6)=2, \sigma^{-1}(7)=8, \sigma^{-1}(8)=6$
$$\sigma^{-1} = 4\ 3\ 1\ 7\ 5\ 2\ 8\ 6$$

**Square $\sigma^2$:** Apply $\sigma$ twice to each element:
- $1 \to 3 \to 2$; $2 \to 6 \to 8$; $3 \to 2 \to 6$; $4 \to 1 \to 3$; $5 \to 5$; $6 \to 8 \to 7$; $7 \to 4 \to 1$; $8 \to 7 \to 4$

$\sigma^2$: $2\ 8\ 6\ 3\ 5\ 7\ 1\ 4$

Cycles of $\sigma^2$: $(1\ 2\ 8\ 4\ 3\ 6\ 7)(5)$ — a 7-cycle (squaring a 7-cycle gives another 7-cycle since $\gcd(2,7)=1$).

---

### (b) $\sigma = 42765813$ on $[8]$

$\sigma(1)=4, \sigma(2)=2, \sigma(3)=7, \sigma(4)=6, \sigma(5)=5, \sigma(6)=8, \sigma(7)=1, \sigma(8)=3$

**Find cycles:**
- $1 \to 4 \to 6 \to 8 \to 3 \to 7 \to 1$ → $(1\ 4\ 6\ 8\ 3\ 7)$ (length 6)
- $2 \to 2$ → fixed point
- $5 \to 5$ → fixed point

**Cycle notation:** $(1\ 4\ 6\ 8\ 3\ 7)(2)(5)$
**Fixed points:** $\{2, 5\}$
**Number of cycles:** 3

**Inverse:** $(1\ 4\ 6\ 8\ 3\ 7)^{-1} = (1\ 7\ 3\ 8\ 6\ 4)$

$\sigma^{-1}(1)=7, \sigma^{-1}(2)=2, \sigma^{-1}(3)=8, \sigma^{-1}(4)=1, \sigma^{-1}(5)=5, \sigma^{-1}(6)=4, \sigma^{-1}(7)=3, \sigma^{-1}(8)=6$
$$\sigma^{-1} = 7\ 2\ 8\ 1\ 5\ 4\ 3\ 6$$

**Square $\sigma^2$:** A 6-cycle squared gives two 3-cycles: $(1\ 4\ 6\ 8\ 3\ 7)^2 = (1\ 6\ 3)(4\ 8\ 7)$.

$\sigma^2 = (1\ 6\ 3)(4\ 8\ 7)(2)(5)$

One-line: $\sigma^2(1)=6, \sigma^2(2)=2, \sigma^2(3)=1, \sigma^2(4)=8, \sigma^2(5)=5, \sigma^2(6)=3, \sigma^2(7)=4, \sigma^2(8)=7$
$$\sigma^2 = 6\ 2\ 1\ 8\ 5\ 3\ 4\ 7$$

---

### (c) $\sigma = 361452$ on $[6]$

$\sigma(1)=3, \sigma(2)=6, \sigma(3)=1, \sigma(4)=4, \sigma(5)=5, \sigma(6)=2$

**Find cycles:**
- $1 \to 3 \to 1$ → $(1\ 3)$
- $2 \to 6 \to 2$ → $(2\ 6)$
- $4 \to 4$ → fixed
- $5 \to 5$ → fixed

**Cycle notation:** $(1\ 3)(2\ 6)(4)(5)$
**Fixed points:** $\{4, 5\}$
**Number of cycles:** 4

**Inverse:** Transpositions are self-inverse: $(1\ 3)^{-1} = (1\ 3)$, $(2\ 6)^{-1} = (2\ 6)$.
$$\sigma^{-1} = \sigma = 361452$$

**Square:** $(1\ 3)^2 = \text{id}$, $(2\ 6)^2 = \text{id}$, so $\sigma^2 = \text{identity}$:
$$\sigma^2 = 1\ 2\ 3\ 4\ 5\ 6$$

---

### (d) $\sigma = 32156487$ on $[8]$

$\sigma(1)=3, \sigma(2)=2, \sigma(3)=1, \sigma(4)=5, \sigma(5)=6, \sigma(6)=4, \sigma(7)=8, \sigma(8)=7$

**Find cycles:**
- $1 \to 3 \to 1$: $(1\ 3)$
- $2 \to 2$: fixed
- $4 \to 5 \to 6 \to 4$: $(4\ 5\ 6)$
- $7 \to 8 \to 7$: $(7\ 8)$

**Cycle notation:** $(1\ 3)(2)(4\ 5\ 6)(7\ 8)$
**Fixed points:** $\{2\}$
**Number of cycles:** 4

**Inverse:**
- $(1\ 3)^{-1} = (1\ 3)$
- $(4\ 5\ 6)^{-1} = (4\ 6\ 5)$
- $(7\ 8)^{-1} = (7\ 8)$

$\sigma^{-1}(1)=3, \sigma^{-1}(2)=2, \sigma^{-1}(3)=1, \sigma^{-1}(4)=6, \sigma^{-1}(5)=4, \sigma^{-1}(6)=5, \sigma^{-1}(7)=8, \sigma^{-1}(8)=7$
$$\sigma^{-1} = 3\ 2\ 1\ 6\ 4\ 5\ 8\ 7$$

**Square:**
- $(1\ 3)^2 = \text{id}$
- $(4\ 5\ 6)^2 = (4\ 6\ 5)$
- $(7\ 8)^2 = \text{id}$

$\sigma^2 = (4\ 6\ 5)$. One-line: $\sigma^2 = 1\ 2\ 3\ 6\ 4\ 5\ 7\ 8$

---

## Problem 75 — Two-line notation from cycle notation; $\sigma^{-1}$ and $\sigma^2$

> **Convention:** Cycles are composed right-to-left (apply rightmost first).

### (a) $\sigma = (1,3,5)(2,4,6)$ on $[6]$

**Two-line notation:** $\sigma(1)=3, \sigma(3)=5, \sigma(5)=1$; $\sigma(2)=4, \sigma(4)=6, \sigma(6)=2$.

$$\sigma = \begin{pmatrix}1&2&3&4&5&6\\3&4&5&6&1&2\end{pmatrix}$$

**$\sigma^{-1}$:** Reverse each cycle: $(1\ 5\ 3)(2\ 6\ 4)$.
$$\sigma^{-1} = \begin{pmatrix}1&2&3&4&5&6\\5&6&1&2&3&4\end{pmatrix}$$

**$\sigma^2$:** Each 3-cycle squared gives another 3-cycle (since $\gcd(2,3)=1$): $(1,3,5)^2 = (1,5,3)$ and $(2,4,6)^2 = (2,6,4)$.
$$\sigma^2 = (1,5,3)(2,6,4) = \begin{pmatrix}1&2&3&4&5&6\\5&6&1&2&3&4\end{pmatrix}$$

*Note: $\sigma^{-1} = \sigma^2$ here — this holds because each 3-cycle satisfies $(c)^3 = \text{id}$, so $(c)^{-1} = (c)^2$.*

---

### (b) $\sigma = (2,3)(1,7)(5)(6,2)$ on $[7]$

> **Warning:** This is NOT disjoint cycle notation — cycles $(2,3)$ and $(6,2)$ share element 2. We must compose them right-to-left: first apply $(6,2)$, then $(1,7)$, then $(5)$ (identity), then $(2,3)$.

**Trace each element (apply rightmost cycle first):**

| Element | After $(6,2)$ | After $(1,7)$ | After $(2,3)$ | $\sigma(\cdot)$ |
|---|---|---|---|---|
| 1 | 1 | 7 | 7 | 7 |
| 2 | 6 | 6 | 6 | 6 |
| 3 | 3 | 3 | 2 | 2 |
| 4 | 4 | 4 | 4 | 4 |
| 5 | 5 | 5 | 5 | 5 |
| 6 | 2 | 2 | 3 | 3 |
| 7 | 7 | 1 | 1 | 1 |

$$\sigma = \begin{pmatrix}1&2&3&4&5&6&7\\7&6&2&4&5&3&1\end{pmatrix}$$

**Disjoint cycle decomposition:** $1\to7\to1$: $(1\ 7)$; $2\to6\to3\to2$: $(2\ 6\ 3)$; 4,5 fixed.

$$\sigma = (1\ 7)(2\ 6\ 3)(4)(5)$$

**$\sigma^{-1}$:** $(1\ 7)^{-1}=(1\ 7)$; $(2\ 6\ 3)^{-1}=(2\ 3\ 6)$.
$$\sigma^{-1} = \begin{pmatrix}1&2&3&4&5&6&7\\7&3&6&4&5&2&1\end{pmatrix}$$

**$\sigma^2$:** $(1\ 7)^2=\text{id}$; $(2\ 6\ 3)^2=(2\ 3\ 6)$ (3-cycle squared).
$$\sigma^2 = (2\ 3\ 6) = \begin{pmatrix}1&2&3&4&5&6&7\\1&3&6&4&5&2&7\end{pmatrix}$$

---

### (c) $\sigma = (7,5,3,1)(2,4,6)$ on $[7]$

**Two-line notation:** $\sigma(7)=5,\sigma(5)=3,\sigma(3)=1,\sigma(1)=7$; $\sigma(2)=4,\sigma(4)=6,\sigma(6)=2$.

$$\sigma = \begin{pmatrix}1&2&3&4&5&6&7\\7&4&1&6&3&2&5\end{pmatrix}$$

**$\sigma^{-1}$:** Reverse each cycle: $(1,3,5,7)^{-1}=(1,7,5,3)$ and $(2,4,6)^{-1}=(2,6,4)$.

$\sigma^{-1}(1)=3, \sigma^{-1}(3)=5, \sigma^{-1}(5)=7, \sigma^{-1}(7)=1$; $\sigma^{-1}(2)=6, \sigma^{-1}(6)=4, \sigma^{-1}(4)=2$.
$$\sigma^{-1} = \begin{pmatrix}1&2&3&4&5&6&7\\3&6&5&2&7&4&1\end{pmatrix}$$

**$\sigma^2$:** $(7,5,3,1)^2 = (7,3)(5,1)$ (4-cycle squared gives two 2-cycles); $(2,4,6)^2=(2,6,4)$.

$\sigma^2 = (7\ 3)(5\ 1)(2\ 6\ 4)$

One-line: $\sigma^2(1)=5, \sigma^2(2)=6, \sigma^2(3)=7, \sigma^2(4)=2, \sigma^2(5)=1, \sigma^2(6)=4, \sigma^2(7)=3$:
$$\sigma^2 = \begin{pmatrix}1&2&3&4&5&6&7\\5&6&7&2&1&4&3\end{pmatrix}$$

---

### (d) $\sigma = (2,7)(6,5,1)(4,3)$ on $[7]$

**Two-line notation:** $\sigma(2)=7,\sigma(7)=2$; $\sigma(6)=5,\sigma(5)=1,\sigma(1)=6$; $\sigma(4)=3,\sigma(3)=4$.

$$\sigma = \begin{pmatrix}1&2&3&4&5&6&7\\6&7&4&3&1&5&2\end{pmatrix}$$

**$\sigma^{-1}$:** $(2\ 7)^{-1}=(2\ 7)$; $(6\ 5\ 1)^{-1}=(1\ 5\ 6)$; $(4\ 3)^{-1}=(4\ 3)=(3\ 4)$.

$\sigma^{-1}(1)=5, \sigma^{-1}(5)=6, \sigma^{-1}(6)=1, \sigma^{-1}(2)=7, \sigma^{-1}(7)=2, \sigma^{-1}(3)=4, \sigma^{-1}(4)=3$.
$$\sigma^{-1} = \begin{pmatrix}1&2&3&4&5&6&7\\5&7&4&3&6&1&2\end{pmatrix}$$

**$\sigma^2$:** $(2\ 7)^2=\text{id}$; $(6\ 5\ 1)^2=(6\ 1\ 5)$; $(4\ 3)^2=\text{id}$.

$\sigma^2 = (6\ 1\ 5)$. One-line: $\sigma^2(1)=5, \sigma^2(5)=6, \sigma^2(6)=1$; all others fixed.
$$\sigma^2 = \begin{pmatrix}1&2&3&4&5&6&7\\5&2&3&4&6&1&7\end{pmatrix}$$

---

## Problem 76 — Permutations without fixed points (derangements) on $[4]$ and $[6]$

**Rule used:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|Derangement formula $D_n$]]

$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$$

**$D_4 = 9$:** The 9 derangements of $[4]$ (in one-line notation):

| Cycle type | Permutations |
|---|---|
| $(2\ 2)$ — two 2-cycles | $2143,\ 3412,\ 4321$ |
| $(4)$ — one 4-cycle | $2341,\ 2413,\ 3142,\ 3421,\ 4123,\ 4312$ |

All 9: $2143,\ 3412,\ 4321,\ 2341,\ 2413,\ 3142,\ 3421,\ 4123,\ 4312$

**$D_6 = 265$:**
$$D_6 = 6!\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120} + \frac{1}{720}\right) = 720 \cdot \frac{265}{720} = \boxed{265}$$

---

## Problem 77 — Permutations with exactly 2 cycles on $[4]$ and $[6]$

**Rule used:** [[2- DM-Advanced-Counting#12. Stirling Numbers of the First Kind|Unsigned Stirling numbers of the first kind $c(n,k)$]]

$c(n,k)$ counts permutations of $[n]$ with exactly $k$ cycles (including fixed points as 1-cycles).

**$c(4,2) = 11$:**

Possible cycle-type decompositions summing to 4 with exactly 2 cycles:

- **Type $(1,3)$:** 1 fixed point + one 3-cycle. Choose the fixed point: $C(4,1)=4$ ways. The 3-cycle on 3 elements: $(3-1)!=2$ ways (cyclic arrangements). Total: $4 \times 2 = 8$.
- **Type $(2,2)$:** Two 2-cycles. Choose which pair forms the first 2-cycle: $C(4,2)/2! = 3$ ways (divide by 2 since the two 2-cycles are unordered). Total: 3.

$$c(4,2) = 8 + 3 = 11$$

**$c(6,2) = 274$:** Using recurrence $c(n,k) = c(n-1,k-1) + (n-1)\cdot c(n-1,k)$:
- $c(5,1) = 4! = 24$, $c(5,2) = 50$
- $c(6,2) = c(5,1) + 5 \cdot c(5,2) = 24 + 250 = \boxed{274}$

---

## Problem 78 — Derangements of $[3]$ and $[4]$; prove $D_n = (n-1)(D_{n-1}+D_{n-2})$

**$D_3 = 2$:**
- $231$: $\sigma(1)=2,\sigma(2)=3,\sigma(3)=1$ (cycle $(1\ 2\ 3)$)
- $312$: $\sigma(1)=3,\sigma(2)=1,\sigma(3)=2$ (cycle $(1\ 3\ 2)$)

**$D_4 = 9$** (listed in Problem 76).

### Proof of $D_n = (n-1)(D_{n-1} + D_{n-2})$

**Setup:** In a derangement $\sigma$ of $[n]$, element $n$ must go somewhere — say $\sigma(n) = k$ where $k \neq n$. There are $n-1$ choices for $k$.

**For each fixed $k$, split into two sub-cases based on where $k$ goes:**

**Case 1: $\sigma(k) = n$** (elements $k$ and $n$ swap each other).

Then elements $\{1, \ldots, n\} \setminus \{k, n\}$ must form a derangement among themselves — none of the remaining $n-2$ elements can go to their own position. This gives $D_{n-2}$ possibilities.

**Case 2: $\sigma(k) \neq n$** (element $k$ does NOT go to $n$).

Define a new permutation $\tau$ of $[n-1]$ by: for $i \neq k$, $\tau(i) = \sigma(i)$; and $\tau(k) = \sigma(k)$. Think of "relabeling" $n$ as $k$. Then $\tau$ is a derangement of $[n-1]$ (since $\sigma(k) \neq n$ means in $\tau$, $k$ does not map to the position labeled $k$). This gives $D_{n-1}$ possibilities.

**Combining:** For each of the $n-1$ choices of $k$, there are $D_{n-2} + D_{n-1}$ derangements. Hence:

$$D_n = (n-1)(D_{n-2} + D_{n-1}) \qquad \blacksquare$$

---

## Problem 79 — 8 hats returned so no man gets his own hat

**Rule used:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|$D_8$]]

This is exactly counting derangements of 8 elements:

$$D_8 = 8!\left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!} - \frac{1}{5!} + \frac{1}{6!} - \frac{1}{7!} + \frac{1}{8!}\right)$$

$$= 40320\left(\frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120} + \frac{1}{720} - \frac{1}{5040} + \frac{1}{40320}\right)$$

Computing step by step (numerator over 40320):
$$= 20160 - 6720 + 1680 - 336 + 56 - 8 + 1 = \boxed{14{,}833}$$

---

## Problem 80 — Eating 3 mangos, 2 papayas, 2 kiwis (only type matters)

**Rule used:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient]]

The sequence of fruits consumed over 7 days: types are M(3), P(2), K(2):

$$\frac{7!}{3!\,2!\,2!} = \frac{5040}{6 \times 2 \times 2} = \frac{5040}{24} = \boxed{210}$$

---

## Problem 81 — 4 men, each marrying one of 6 women (distinct women)

**Rule used:** [[1- DM-Basic-Counting-Rules#5.2 Injective Functions|Injective functions / $P(n,k)$]]

Each man marries a distinct woman (no woman can marry two men). This is choosing an ordered assignment of 4 distinct women from 6:

$$P(6,4) = 6 \times 5 \times 4 \times 3 = \boxed{360}$$

---

## Problem 82 — 8 identical DVDs into 5 indistinguishable boxes, each $\geq 1$

**Rule used:** Integer partitions of 8 into exactly 5 positive parts

Since both DVDs (identical) and boxes (indistinguishable) are non-labeled, we need the number of ways to write 8 as a sum of exactly 5 positive integers (order doesn't matter):

| Partition | Multiset of counts |
|---|---|
| $4+1+1+1+1=8$ | $(4,1,1,1,1)$ |
| $3+2+1+1+1=8$ | $(3,2,1,1,1)$ |
| $2+2+2+1+1=8$ | $(2,2,2,1,1)$ |

$$\boxed{3 \text{ ways}}$$

---

## Problem 83 — 10 exam questions, scores sum to 100, each $\geq 5$

**Rule used:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]]

Let $x_i$ = score of question $i$ ($x_i \geq 5$, $\sum x_i = 100$). Substitute $y_i = x_i - 5 \geq 0$:

$$\sum_{i=1}^{10} y_i = 100 - 10 \times 5 = 50$$

Non-negative solutions with 10 variables and sum 50:

$$C(50 + 9,\, 9) = C(59,\, 9) = \boxed{C(59, 9)}$$

---

## Problem 84 — Permutations of $[2n]$ assigning even numbers to odd positions

**Rule used:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule for constrained bijections]]

**Setup:**
- Odd positions: $\{1, 3, 5, \ldots, 2n-1\}$ — exactly $n$ positions.
- Even positions: $\{2, 4, 6, \ldots, 2n\}$ — exactly $n$ positions.
- Even values: $\{2, 4, \ldots, 2n\}$ — exactly $n$ values.
- Odd values: $\{1, 3, \ldots, 2n-1\}$ — exactly $n$ values.

**Task:** Assign even values to odd positions, and (consequently) odd values to even positions.

- Assign $n$ even values to $n$ odd positions (bijection): $n!$ ways.
- Assign $n$ odd values to $n$ even positions (bijection): $n!$ ways.

$$\boxed{(n!)^2}$$

---

## Problem 85 — Minimum socks to guarantee a matching pair (Pigeonhole)

**Rule used:** Pigeonhole Principle

**Setup:** 3 colors of socks (red, blue, green). Think of color as the "pigeonhole" — there are 3 pigeonholes.

**Worst case scenario:** You draw one sock of each color (3 socks total) without getting any matching pair. The next sock (4th sock) must be one of the 3 colors, creating a pair with the sock of that color already drawn.

**Therefore you need at minimum:**

$$\boxed{4 \text{ socks}}$$

---

## Problem 86 — 5 points in unit square: two within $\frac{\sqrt{2}}{2}$

**Rule used:** Pigeonhole Principle (generalized: $\lceil N/k \rceil$ objects in $k$ boxes → at least one box has $\geq \lceil N/k \rceil$)

**Proof:**

Divide the unit square $[0,1] \times [0,1]$ into 4 smaller squares of side $\frac{1}{2}$:

$$\left[0,\tfrac{1}{2}\right]\times\left[0,\tfrac{1}{2}\right],\ \left[\tfrac{1}{2},1\right]\times\left[0,\tfrac{1}{2}\right],\ \left[0,\tfrac{1}{2}\right]\times\left[\tfrac{1}{2},1\right],\ \left[\tfrac{1}{2},1\right]\times\left[\tfrac{1}{2},1\right]$$

With 5 points placed and 4 sub-squares (pigeonholes), by the Pigeonhole Principle at least one sub-square contains $\geq 2$ points.

The maximum distance between any two points within a $\frac{1}{2} \times \frac{1}{2}$ square is the diagonal:
$$\sqrt{\left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2} = \sqrt{\frac{1}{4} + \frac{1}{4}} = \sqrt{\frac{1}{2}} = \frac{\sqrt{2}}{2}$$

Therefore, those 2 points are at most $\dfrac{\sqrt{2}}{2}$ apart. $\blacksquare$

---

## Problem 87 — 5 points in equilateral triangle of side 1: two within $\frac{1}{2}$

**Rule used:** Pigeonhole Principle

**Proof:**

Connect the midpoints of the equilateral triangle of side 1. This creates **4 smaller equilateral triangles**, each with side $\frac{1}{2}$.

With 5 points and 4 sub-triangles, by the Pigeonhole Principle at least one sub-triangle contains $\geq 2$ points.

The maximum distance between any two points within an equilateral triangle of side $\frac{1}{2}$ is at most $\frac{1}{2}$ (the side length is the longest distance). $\blacksquare$

---

## Problem 88 — Among $n+1$ integers $\leq 2n$, one divides another

**Rule used:** Pigeonhole Principle

**Proof:**

**Key fact:** Every positive integer can be written uniquely as $2^a \cdot m$ where $m$ is odd (factor out all powers of 2).

**Setup:** For each integer $x \leq 2n$, define its "odd part" as the $m$ in $x = 2^a \cdot m$. Since $x \leq 2n$, we have $m \leq 2n$ and $m$ is odd, so $m \in \{1, 3, 5, \ldots, 2n-1\}$ — exactly $n$ possible odd values.

**Apply Pigeonhole:** We have $n+1$ integers but only $n$ possible odd parts. By the Pigeonhole Principle, two integers share the same odd part: say $x = 2^a \cdot m$ and $y = 2^b \cdot m$ with (say) $a < b$. Then $x = 2^a m$ divides $y = 2^b m$ since $y/x = 2^{b-a}$ is an integer. $\blacksquare$

---

## Problem 89 — 7 integers from $\{1,\ldots,10\}$: two pairs summing to 11

**Rule used:** Pigeonhole Principle

**Setup:** Define 5 "complementary pairs" from $\{1,\ldots,10\}$:
$$\{1,10\},\quad \{2,9\},\quad \{3,8\},\quad \{4,7\},\quad \{5,6\}$$

Each number belongs to exactly one pair, and each pair sums to 11.

**With 7 integers selected from 5 pairs:**

By Pigeonhole, at least $\lceil 7/5 \rceil = 2$ pairs must have both members selected. Since we have 7 elements and 5 pairs, and $7 = 5 + 2$, at least 2 pairs are "fully selected" → at least 2 pairs summing to 11. ✓

**With 6 integers:** Possible to select only 1 pair summing to 11 (e.g., pick one from each of 5 pairs = 5 elements, then add one more from any pair). Example: $\{1,2,3,4,5,6\}$ contains only the pair $\{5,6\}$ summing to 11. So the conclusion (two pairs) is **not guaranteed** with only 6.

---

## Problem 90 — 7 numbers from $\{2,\ldots,13\}$: two sum to 15

**Rule used:** Pigeonhole Principle

**Setup:** Partition $\{2,3,\ldots,13\}$ (12 elements) into 6 pairs summing to 15:
$$\{2,13\},\quad \{3,12\},\quad \{4,11\},\quad \{5,10\},\quad \{6,9\},\quad \{7,8\}$$

Every number in $\{2,\ldots,13\}$ belongs to exactly one pair.

With 7 numbers and 6 pairs (pigeonholes), by the Pigeonhole Principle at least one pair has both members selected. Those two members sum to 15. $\blacksquare$

---

## Problem 91 — 12 chairs, 9 people: 3 consecutive chairs occupied

**Rule used:** Pigeonhole Principle

**Proof:**

Partition the 12 chairs into 4 groups of 3 consecutive chairs:
$$\{1,2,3\},\quad \{4,5,6\},\quad \{7,8,9\},\quad \{10,11,12\}$$

With 9 people distributed among 4 groups (pigeonholes), by the Pigeonhole Principle at least one group receives $\lceil 9/4 \rceil = 3$ people.

Since that group consists of exactly 3 consecutive chairs, those 3 chairs are all occupied by the 3 people in that group. $\blacksquare$

---

## Problem 92 — Sequence of $n^2+1$ distinct reals: monotone subsequence of length $n+1$

**Rule used:** Erdős–Szekeres Theorem, proved by Pigeonhole Principle

**Proof:**

Let $a_1, a_2, \ldots, a_{n^2+1}$ be the sequence of distinct real numbers.

For each $i$, define $d_i$ = the length of the longest strictly **increasing** subsequence starting at position $i$.

**Case 1:** Some $d_i \geq n+1$. Then we have an increasing subsequence of length $n+1$ and we're done.

**Case 2:** All $d_i \leq n$ (i.e., $d_i \in \{1, 2, \ldots, n\}$ for all $i$).

With $n^2+1$ positions and $n$ possible values for $d_i$, by the Pigeonhole Principle at least $n+1$ positions share the same value of $d_i$. Call them positions $i_1 < i_2 < \cdots < i_{n+1}$ with $d_{i_1} = d_{i_2} = \cdots = d_{i_{n+1}} = d$.

**Claim:** $a_{i_1} > a_{i_2} > \cdots > a_{i_{n+1}}$ (strictly decreasing).

**Proof of claim:** Suppose for contradiction that $a_{i_j} < a_{i_{j+1}}$ for some $j$. Then we can prepend $a_{i_j}$ to an increasing subsequence of length $d$ starting at $i_{j+1}$, obtaining an increasing subsequence of length $d+1$ starting at $i_j$ — contradicting $d_{i_j} = d$.

Therefore $a_{i_1}, a_{i_2}, \ldots, a_{i_{n+1}}$ is a strictly decreasing subsequence of length $n+1$. $\blacksquare$


---

---

# Section 2 — Advanced Counting Rules

---

## Adv. Problem 1 — Generating functions for sequences

**Rule used:** [[2- DM-Advanced-Counting#2. Standard Generating Function Correspondences|Standard OGF catalogue]]

> **Recall:** The OGF (ordinary generating function) for a sequence $(a_0, a_1, a_2, \ldots)$ is $G(x) = \sum_{n \geq 0} a_n x^n$. Finding the OGF is like encoding the whole sequence into one algebraic object.

---

### (a) Non-negative integers $(0, 1, 2, 3, \ldots)$

**Strategy:** Differentiate the geometric series.

We know $\dfrac{1}{1-x} = \sum_{n \geq 0} x^n$, so the sequence is $(1, 1, 1, \ldots)$.

Differentiate: $\dfrac{d}{dx}\dfrac{1}{1-x} = \dfrac{1}{(1-x)^2} = \sum_{n \geq 1} n x^{n-1}$.

Multiply by $x$: $\dfrac{x}{(1-x)^2} = \sum_{n \geq 1} n x^n = x + 2x^2 + 3x^3 + \cdots$

The sequence $(0, 1, 2, 3, \ldots)$ corresponds to:

$$\boxed{G(x) = \dfrac{x}{(1-x)^2}}$$

---

### (b) $k$-combinations with repetition from $[n]$ (for fixed $n$, varying $k$)

The number of $k$-combinations with repetition from $n$ elements is $C(n+k-1, k)$.

This equals the coefficient of $x^k$ in $\dfrac{1}{(1-x)^n}$ (generalized binomial series):

$$\frac{1}{(1-x)^n} = \sum_{k \geq 0} \binom{n+k-1}{k} x^k$$

$$\boxed{G(x) = \dfrac{1}{(1-x)^n}}$$

---

### (c) Perfect squares $(1, 4, 9, 16, \ldots)$

From (a): $\dfrac{x}{(1-x)^2} = \sum_{n \geq 1} n x^n$. Differentiate and multiply by $x$:

$$\frac{d}{dx}\frac{x}{(1-x)^2} = \frac{(1-x)^2 + 2x(1-x)}{(1-x)^4} = \frac{1+x}{(1-x)^3} = \sum_{n \geq 1} n^2 x^{n-1}$$

Multiply by $x$: $\dfrac{x(1+x)}{(1-x)^3} = \sum_{n \geq 1} n^2 x^n$

But this starts from $n=1$. The sequence $(1,4,9,\ldots)$ is indexed as $a_1=1, a_2=4$, etc. If we want $a_n = n^2$ for $n \geq 1$:

$$\boxed{G(x) = \dfrac{x(1+x)}{(1-x)^3}}$$

---

### (d) Fibonacci numbers $(0, 1, 1, 2, 3, 5, \ldots)$

**Derivation:** Fibonacci recurrence is $f_n = f_{n-1} + f_{n-2}$ for $n \geq 2$, with $f_0=0, f_1=1$.

Let $F(x) = \sum_{n \geq 0} f_n x^n$. Then:
$$F(x) - f_0 - f_1 x = \sum_{n \geq 2} f_n x^n = \sum_{n \geq 2}(f_{n-1}+f_{n-2})x^n = x(F(x)-f_0) + x^2 F(x)$$

$$F(x) - x = xF(x) + x^2 F(x)$$
$$F(x)(1 - x - x^2) = x$$

$$\boxed{F(x) = \dfrac{x}{1-x-x^2}}$$

---

### (e) Catalan numbers $(1, 1, 2, 5, 14, 42, \ldots)$

The Catalan numbers satisfy $C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k}$ (convolution recurrence). Their OGF $C(x)$ satisfies:

$$C(x) = 1 + x \cdot C(x)^2$$

Solving (quadratic in $C$): $C = \dfrac{1 \pm \sqrt{1-4x}}{2x}$. Choosing the sign so $C(0)=1$:

$$\boxed{C(x) = \dfrac{1-\sqrt{1-4x}}{2x}}$$

---

### (f) Filling a bag with fruit under constraints

We need the OGF for the number of ways to fill a bag with $n$ fruits where:
- Apples: even number → OGF $= 1 + x^2 + x^4 + \cdots = \dfrac{1}{1-x^2}$
- Bananas: multiple of 5 → OGF $= 1 + x^5 + x^{10} + \cdots = \dfrac{1}{1-x^5}$
- Oranges: at most 4 → OGF $= 1 + x + x^2 + x^3 + x^4 = \dfrac{1-x^5}{1-x}$
- Pears: at most 1 → OGF $= 1 + x$

The total OGF (by the convolution rule — independent choices):

$$G(x) = \frac{1}{1-x^2} \cdot \frac{1}{1-x^5} \cdot \frac{1-x^5}{1-x} \cdot (1+x)$$

Simplify: $\dfrac{1-x^5}{1-x^2} \cdot (1+x) = \dfrac{1-x^5}{(1-x)(1+x)} \cdot (1+x) = \dfrac{1-x^5}{1-x}$, then:

$$G(x) = \frac{1}{1-x^5} \cdot \frac{1-x^5}{1-x} \cdot \frac{1}{1-x} \cdot \text{(wait, let me redo)}$$

Actually:
$$G(x) = \frac{1}{1-x^2} \cdot \frac{1-x^5}{1-x} \cdot \frac{1}{1-x^5} \cdot (1+x) = \frac{1}{1-x^2} \cdot \frac{1}{1-x} \cdot (1+x) = \frac{1+x}{(1-x^2)(1-x)}$$

Since $1-x^2 = (1-x)(1+x)$:

$$G(x) = \frac{1+x}{(1-x)(1+x)(1-x)} = \frac{1}{(1-x)^2}$$

**So $a_n = n+1$** — the number of ways to fill a bag with $n$ fruits is $n+1$.

$$\boxed{G(x) = \dfrac{1}{(1-x)^2}}$$

---

## Adv. Problem 2 — Express OGFs in terms of $A(x)$

Let $A(x) = \sum_{n \geq 0} a_n x^n$.

> **Key operations:**
> - Multiplying $A(x)$ by $x$ shifts the sequence right: $xA(x) \leftrightarrow (0, a_0, a_1, a_2, \ldots)$
> - $\dfrac{A(x)-a_0}{x}$ shifts left: $\leftrightarrow (a_1, a_2, a_3, \ldots)$
> - $\dfrac{A(x)}{1-x}$ takes partial sums: $\leftrightarrow (a_0, a_0+a_1, a_0+a_1+a_2, \ldots)$
> - $A(bx) \leftrightarrow (a_0, a_1 b, a_2 b^2, \ldots)$

**(a) $(a_0,\ a_0+a_1,\ a_1+a_2,\ \ldots)$** — $n$-th term is $a_{n-1}+a_n$ for $n \geq 1$, and $a_0$ for $n=0$.

Check: $(1+x)A(x)$ has $n$-th term $a_n + a_{n-1}$. ✓

$$\boxed{(1+x)A(x)}$$

**(b) $(a_1, a_2, a_3, \ldots)$** — left-shift by 1.

$$\boxed{\dfrac{A(x)-a_0}{x}}$$

**Verify:** $\dfrac{A(x)-a_0}{x} = \dfrac{a_1 x + a_2 x^2 + \cdots}{x} = a_1 + a_2 x + a_3 x^2 + \cdots$ ✓

**(c) $(a_0+a_1,\ a_1+a_2,\ a_2+a_3,\ \ldots)$** — $n$-th term is $a_n + a_{n+1}$.

The sequence $(a_1, a_2, a_3, \ldots)$ has OGF $\dfrac{A(x)-a_0}{x}$. Adding $A(x)$ gives sequence $(a_0+a_1, a_1+a_2, \ldots)$:

$$\boxed{\dfrac{A(x)-a_0}{x} + A(x) = \dfrac{(1+x)A(x)-a_0}{x}}$$

**(d) $(a_0,\ 2a_1,\ 4a_2,\ 8a_3,\ \ldots) = (a_n \cdot 2^n)$**

Substitute $x \leftarrow 2x$:

$$\boxed{A(2x)}$$

**Verify:** $A(2x) = \sum a_n (2x)^n = \sum a_n 2^n x^n$ ✓

**(e) $(a_0,\ a_0+a_1,\ a_0+a_1+a_2,\ \ldots)$** — partial sums.

Multiplying by $\dfrac{1}{1-x}$ computes prefix sums:

$$\boxed{\dfrac{A(x)}{1-x}}$$

**(f) $(a_0,\ a_1 b,\ a_2 b^2,\ a_3 b^3,\ \ldots)$**

$$\boxed{A(bx)}$$

**(g) $(a_0,\ 0,\ a_2,\ 0,\ a_4,\ 0,\ \ldots)$** — keep even-indexed, zero the odd-indexed.

Use the identity: $A(x) + A(-x) = 2(a_0 + a_2 x^2 + a_4 x^4 + \cdots)$

$$\boxed{\dfrac{A(x)+A(-x)}{2}}$$

**(h) $(a_0,\ a_2,\ a_4,\ \ldots)$** — re-index: new sequence $b_n = a_{2n}$.

We want $\sum b_n x^n = \sum a_{2n} x^n$. Substituting $x \leftarrow \sqrt{x}$ in part (g):

$$\boxed{\dfrac{A(\sqrt{x})+A(-\sqrt{x})}{2}}$$

---

## Adv. Problem 3 — OGF for paying $n$ dollars using 3, 5, 7 dollar coins

**Rule used:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule — each denomination is independent]]

- OGF for 3-dollar coins (0 or more): $1 + x^3 + x^6 + \cdots = \dfrac{1}{1-x^3}$
- OGF for 5-dollar coins: $\dfrac{1}{1-x^5}$
- OGF for 7-dollar coins: $\dfrac{1}{1-x^7}$

Total (multiply for independent choices):

$$\boxed{G(x) = \dfrac{1}{(1-x^3)(1-x^5)(1-x^7)}}$$

---

## Adv. Problem 4 — OGF for distributing $n$ candies: 4 children (each odd), 1 adult (1 or 2)

**Each child gets an odd number of candies:** $1, 3, 5, \ldots$ → OGF per child $= x + x^3 + x^5 + \cdots = \dfrac{x}{1-x^2}$.

**Four children** (independent, multiply): $\left(\dfrac{x}{1-x^2}\right)^4 = \dfrac{x^4}{(1-x^2)^4}$.

**Adult gets 1 or 2:** OGF $= x + x^2 = x(1+x)$.

**Total:**

$$G(x) = \frac{x^4}{(1-x^2)^4} \cdot x(1+x) = \frac{x^5(1+x)}{(1-x^2)^4}$$

Simplify: $(1-x^2)^4 = [(1-x)(1+x)]^4$, so $\dfrac{1+x}{(1-x^2)^4} = \dfrac{1}{(1-x)^4(1+x)^3}$.

$$\boxed{G(x) = \dfrac{x^5}{(1-x)^4(1+x)^3}}$$

---

## Adv. Problem 5 — OGF for scoring $n$ points (1, 2, or 4 per turn)

**Unrestricted:** OGF $= \dfrac{1}{(1-x)(1-x^2)(1-x^4)}$

### (a) At least 2 turns scoring 4 points

**OGF for turns scoring 4 only (at least 2):** Normal OGF $= \dfrac{1}{1-x^4}$, but remove the "0 turns" and "1 turn" terms:

$$\frac{1}{1-x^4} - 1 - x^4 = \frac{1 - (1-x^4) - x^4(1-x^4)}{1-x^4} = \frac{x^8}{1-x^4}$$

**Turns scoring 1 or 2 (no restrictions):** $\dfrac{1}{(1-x)(1-x^2)}$

$$\boxed{G(x) = \dfrac{x^8}{(1-x^4)(1-x)(1-x^2)}}$$

### (b) Number of turns scoring 2 is a multiple of 3

**OGF for turns scoring 2 (multiples of 3 only):** $1 + x^6 + x^{12} + \cdots = \dfrac{1}{1-x^6}$

**Turns scoring 1 or 4 (unrestricted):**

$$\boxed{G(x) = \dfrac{1}{(1-x)(1-x^6)(1-x^4)}}$$

---

## Adv. Problem 6 — OGF for $x_1+x_2+x_3+x_4=k$ with constraints; find $a_7$

**Constraints:** $x_1 \geq 3$, $1 \leq x_2 \leq 5$, $0 \leq x_3 \leq 4$, $x_4 \geq 1$.

**OGF for each variable:**
- $x_1 \geq 3$: $x^3 + x^4 + \cdots = \dfrac{x^3}{1-x}$
- $1 \leq x_2 \leq 5$: $x + x^2 + x^3 + x^4 + x^5 = x\dfrac{1-x^5}{1-x}$
- $0 \leq x_3 \leq 4$: $1 + x + \cdots + x^4 = \dfrac{1-x^5}{1-x}$
- $x_4 \geq 1$: $x + x^2 + \cdots = \dfrac{x}{1-x}$

**Total OGF:**

$$G(x) = \frac{x^3}{1-x} \cdot x\frac{1-x^5}{1-x} \cdot \frac{1-x^5}{1-x} \cdot \frac{x}{1-x} = \frac{x^5(1-x^5)^2}{(1-x)^4}$$

**Finding $a_7$** (coefficient of $x^7$):

We need the coefficient of $x^2$ in $\dfrac{(1-x^5)^2}{(1-x)^4}$.

Since $(1-x^5)^2 = 1 - 2x^5 + x^{10}$, and we only need the $x^2$ coefficient, the $x^5$ and $x^{10}$ terms don't contribute:

$$a_7 = [x^2]\frac{1}{(1-x)^4} = \binom{2+3}{3} = \binom{5}{3} = \boxed{10}$$

*(Alternatively: substitute $y_1=x_1-3$, $y_4=x_4-1$, $z_2=x_2-1$: then $y_1+z_2+x_3+y_4=2$ with all $\geq 0$ and $z_2, x_3 \leq 4$; since max value is 2 < 4, upper bounds are inactive. Stars and Bars: $C(5,3)=10$.)*

---

## Adv. Problem 7 — Fibonacci identities via generating functions

**OGF:** $F(x) = \dfrac{x}{1-x-x^2} = \sum_{n \geq 0} f_n x^n$

### (a) $f_0 + f_1 + \cdots + f_n = f_{n+2} - 1$

**GF proof:** $\dfrac{F(x)}{1-x}$ has $n$-th coefficient $\sum_{k=0}^n f_k$.

**Direct proof (telescoping):** Use $f_{k+2} - f_{k+1} = f_k$:
$$\sum_{k=0}^n f_k = \sum_{k=0}^n (f_{k+2} - f_{k+1}) = f_{n+2} - f_1 = f_{n+2} - 1 \checkmark$$

*(The sum telescopes because $f_{k+2} - f_{k+1} = f_k$ means each $f_k$ is a difference of consecutive terms.)*

### (b) $f_0 + f_2 + \cdots + f_{2n} = f_{2n+1} - 1$

**Direct proof:** Use $f_{2k+1} - f_{2k-1} = f_{2k}$ (follows from Fibonacci recurrence applied twice):
$$\sum_{k=0}^n f_{2k} = f_0 + \sum_{k=1}^n (f_{2k+1}-f_{2k-1}) = 0 + (f_{2n+1}-f_1) = f_{2n+1}-1 \checkmark$$

### (c) $f_1 + f_3 + \cdots + f_{2n-1} = f_{2n}$

**From (a) and (b):** The total sum (all terms $f_0$ through $f_{2n}$) is $f_{2n+2}-1$. The even-indexed sum is $f_{2n+1}-1$. So:

$$\text{odd-indexed sum} = (f_{2n+2}-1) - (f_{2n+1}-1) = f_{2n+2} - f_{2n+1} = f_{2n} \checkmark$$

---

## Adv. Problem 8 — Closed formula for $k$-combinations with repetition via Maclaurin

**Rule used:** [[2- DM-Advanced-Counting#6. From Generating Functions to Closed Formulas|Generalized binomial theorem]]

The OGF for $k$-combinations with repetition from $n$ elements is $\dfrac{1}{(1-x)^n}$.

**Maclaurin expansion:** By repeated differentiation of $\dfrac{1}{1-x}$:

$$\frac{d^k}{dx^k}\frac{1}{1-x} = \frac{k!}{(1-x)^{k+1}}$$

or by the generalized binomial theorem with $\alpha = -n$:

$$\frac{1}{(1-x)^n} = \sum_{k=0}^{\infty} \binom{-n}{k}(-x)^k = \sum_{k=0}^{\infty} \binom{n+k-1}{k} x^k$$

The coefficient of $x^k$ is $\binom{n+k-1}{k}$, confirming:

$$\boxed{C(n+k-1,\,k)}$$

---

## Adv. Problem 9 — OGF for $S(n,2)$ and closed formula

**Recurrence:** $S(0,2) = S(1,2) = 0$; for $n \geq 2$: $S(n,2) = 1 + 2\cdot S(n-1,2)$.

**Solving via OGF:**

Let $F(x) = \sum_{n \geq 0} S(n,2) x^n$. Multiply the recurrence $S(n,2) = 1 + 2S(n-1,2)$ by $x^n$ and sum for $n \geq 2$:

$$\sum_{n \geq 2} S(n,2) x^n = \sum_{n \geq 2} x^n + 2x\sum_{n \geq 2} S(n-1,2) x^{n-1}$$

$$F(x) - 0 - 0 = \frac{x^2}{1-x} + 2x \cdot F(x)$$

$$F(x)(1 - 2x) = \frac{x^2}{1-x}$$

$$F(x) = \frac{x^2}{(1-x)(1-2x)}$$

**Partial fractions:** Numerator has degree 2, denominator has degree 2, so we first do long division:

$\dfrac{x^2}{1 - 3x + 2x^2}$: leading terms $\dfrac{x^2}{2x^2} = \dfrac{1}{2}$. So:

$$F(x) = \frac{1}{2} + \frac{F_1(x)}{(1-x)(1-2x)} \quad \text{where } F_1(x) = x^2 - \frac{1}{2}(1-3x+2x^2) = \frac{3x-1}{2} + \frac{x^2-x^2}{...}$$

Let me redo cleanly with $\dfrac{A}{1-x} + \dfrac{B}{1-2x}$ after noting the polynomial part is $\dfrac{1}{2}$:

Remainder: $x^2 - \dfrac{1}{2}(2x^2 - 3x + 1) = \dfrac{3x-1}{2}$.

$$F(x) = \frac{1}{2} + \frac{(3x-1)/2}{(1-x)(1-2x)}$$

For $\dfrac{3x-1}{2(1-x)(1-2x)} = \dfrac{A}{1-x} + \dfrac{B}{1-2x}$:

$\dfrac{3x-1}{2} = A(1-2x) + B(1-x)$

$x=1$: $\dfrac{2}{2}=1=A(-1)$, so $A=-1$.

$x=\frac{1}{2}$: $\dfrac{1/2}{2}=\dfrac{1}{4}=B(\frac{1}{2})$, so $B=\dfrac{1}{2}$.

$$F(x) = \frac{1}{2} - \frac{1}{1-x} + \frac{1/2}{1-2x}$$

**Extract coefficients** ($n \geq 1$):

$$S(n,2) = \frac{1}{2}[n=0] - 1 + \frac{2^n}{2} = 2^{n-1} - 1$$

*Check:* $S(2,2)=1$: $2^1-1=1$ ✓; $S(3,2)=3$: $2^2-1=3$ ✓; $S(4,2)=7$: $2^3-1=7$ ✓.

$$\boxed{S(n,2) = 2^{n-1}-1}$$

---

## Adv. Problem 10 — Solve recurrences using characteristic polynomial

**Rule:** [[2- DM-Advanced-Counting#7. Homogeneous Linear Recurrences|Characteristic polynomial method]]

> **Method:**
> 1. Write the characteristic polynomial (roots $r_i$).
> 2. General solution: $a_n = \sum c_i r_i^n$.
> 3. Use initial conditions to solve for $c_i$.
> 4. For non-homogeneous: the RHS introduces an extra root.

### (a) $a_0 = 2$, $a_n = 3a_{n-1}$

**Characteristic equation:** $r = 3$. General solution: $a_n = c \cdot 3^n$.

**Initial condition:** $a_0 = c \cdot 1 = 2$, so $c = 2$.

$$\boxed{a_n = 2 \cdot 3^n}$$

---

### (b) $a_0 = 2$, $a_n = 3a_{n-1} + 1$

**Non-homogeneous:** RHS is $1 = 1^n$. The characteristic root of the homogeneous part is $r=3$. The RHS introduces root $r=1$.

**General solution:** $a_n = c_1 \cdot 3^n + c_2 \cdot 1^n = c_1 \cdot 3^n + c_2$.

**Initial conditions:**
- $a_0 = c_1 + c_2 = 2$
- $a_1 = 3(2) + 1 = 7$, so $3c_1 + c_2 = 7$

Subtract: $2c_1 = 5$, so $c_1 = \dfrac{5}{2}$, $c_2 = -\dfrac{1}{2}$.

$$\boxed{a_n = \dfrac{5 \cdot 3^n - 1}{2}}$$

**Check:** $a_0 = (5-1)/2 = 2$ ✓; $a_1 = (15-1)/2 = 7$ ✓.

---

### (c) $a_0=1$, $a_1=2$, $a_n = 5a_{n-1} - 4a_{n-2}$

**Characteristic equation:** $r^2 - 5r + 4 = 0 = (r-1)(r-4)$. Roots: $r=1$, $r=4$.

**General solution:** $a_n = c_1 \cdot 1^n + c_2 \cdot 4^n = c_1 + c_2 \cdot 4^n$.

**Initial conditions:**
- $a_0 = c_1 + c_2 = 1$
- $a_1 = c_1 + 4c_2 = 2$

Subtract: $3c_2 = 1$, so $c_2 = \dfrac{1}{3}$, $c_1 = \dfrac{2}{3}$.

$$\boxed{a_n = \dfrac{2 + 4^n}{3}}$$

---

### (d) $u_0=2$, $u_1=-6$, $u_{n+2} + 8u_{n+1} - 9u_n = 8 \cdot 3^{n+1}$

**Homogeneous characteristic equation:** $r^2 + 8r - 9 = (r+9)(r-1) = 0$. Roots: $r=-9$, $r=1$.

**Non-homogeneous:** RHS is $8 \cdot 3^{n+1} = 24 \cdot 3^n$. This introduces root $r=3$.

**General solution:** $u_n = c_1(-9)^n + c_2(1)^n + c_3(3)^n$.

**Find $u_2$ from recurrence:** $u_2 = -8u_1 + 9u_0 + 8\cdot3^1 = 48 + 18 + 24 = 90$.

**System of equations:**
- $u_0 = c_1 + c_2 + c_3 = 2$
- $u_1 = -9c_1 + c_2 + 3c_3 = -6$
- $u_2 = 81c_1 + c_2 + 9c_3 = 90$

From (1)–(2): $10c_1 - 2c_3 = 8$, so $5c_1 - c_3 = 4$.

From (3)–(1): $80c_1 + 8c_3 = 88$, so $10c_1 + c_3 = 11$.

Adding: $15c_1 = 15$, so $c_1 = 1$. Then $c_3 = 5-4 = 1$. Then $c_2 = 2 - 1 - 1 = 0$.

$$\boxed{u_n = (-9)^n + 3^n}$$

---

### (e) $u_0=1$, $u_{n+1} - 2u_n = 4^n$

**Homogeneous:** $r-2=0$, root $r=2$.
**Non-homogeneous:** $4^n$ introduces root $r=4$.

**General solution:** $u_n = c_1 \cdot 2^n + c_2 \cdot 4^n$.

**Initial conditions:**
- $u_0 = c_1 + c_2 = 1$
- $u_1 = 2(1) + 1 = 3$, so $2c_1 + 4c_2 = 3$

From first: $c_1 = 1-c_2$. Substitute: $2(1-c_2)+4c_2 = 3 \Rightarrow 2+2c_2=3 \Rightarrow c_2=\frac{1}{2}$, $c_1=\frac{1}{2}$.

$$\boxed{u_n = \dfrac{2^n + 4^n}{2}}$$

---

### (f) Words of length $n$ in $\{a,b,c,d\}$ with odd number of b's

**Showing $q_{n+1} = 4^n + 2q_n$:**

Words of length $n+1$ with an odd number of b's can end with:
- A non-b character (a, c, or d — 3 choices): the first $n$ characters must already have an odd number of b's → $3q_n$ words.
- The letter b: the first $n$ characters must have an **even** number of b's → $4^n - q_n$ words.

$$q_{n+1} = 3q_n + (4^n - q_n) = 4^n + 2q_n \checkmark$$

**Solving:** Initial condition $q_0 = 0$ (empty word has 0 b's = even, not odd), so $q_1 = 1$ (only "b").

**Characteristic roots:** $r=2$ (homogeneous) and $r=4$ (from RHS $4^n$).

**General solution:** $q_n = c_1 \cdot 2^n + c_2 \cdot 4^n$.

- $q_0 = c_1 + c_2 = 0 \Rightarrow c_1 = -c_2$
- $q_1 = 2c_1 + 4c_2 = 1 \Rightarrow -2c_2 + 4c_2 = 1 \Rightarrow c_2 = \frac{1}{2}, c_1 = -\frac{1}{2}$

$$\boxed{q_n = \dfrac{4^n - 2^n}{2}}$$

---

## Adv. Problem 11 — Closed formulas from generating functions

> **Key formulas:**
> - $[x^n]\dfrac{1}{1-ax} = a^n$
> - $[x^n]\dfrac{1}{(1-x)^r} = \binom{n+r-1}{r-1}$
> - Multiplying by $x^k$ shifts the index.

### (a) $(3x-4)^3$

Expand using Binomial Theorem:

$$(3x-4)^3 = \sum_{k=0}^3 \binom{3}{k}(3x)^k(-4)^{3-k}$$

$$= (-4)^3 + 3(3x)(-4)^2 + 3(3x)^2(-4) + (3x)^3$$

$$= -64 + 3 \cdot 3 \cdot 16 \cdot x + 3 \cdot 9(-4)x^2 + 27x^3$$

$$= -64 + 144x - 108x^2 + 27x^3$$

**Sequence:** $(a_0, a_1, a_2, a_3) = (-64,\ 144,\ -108,\ 27)$; $a_n = 0$ for $n \geq 4$.

---

### (b) $\dfrac{x^3}{1-3x}$

$$\frac{x^3}{1-3x} = x^3 \sum_{n \geq 0} 3^n x^n = \sum_{n \geq 3} 3^{n-3} x^n$$

$$a_n = \begin{cases} 3^{n-3} & n \geq 3 \\ 0 & n < 3 \end{cases}$$

---

### (c) $\dfrac{x^3+x}{1-3x}$

Split: $\dfrac{x^3}{1-3x} + \dfrac{x}{1-3x}$.

- First term: $a_n = 3^{n-3}$ for $n \geq 3$, 0 otherwise (from (b)).
- Second term: $x \cdot \dfrac{1}{1-3x} = \sum_{n \geq 1} 3^{n-1}x^n$, so $a_n = 3^{n-1}$ for $n \geq 1$.

Combined:
$$a_n = \begin{cases} 0 & n=0 \\ 3^{n-1} & 1 \leq n \leq 2 \\ 3^{n-1} + 3^{n-3} = 3^{n-3}(9+1) = 10 \cdot 3^{n-3} & n \geq 3 \end{cases}$$

---

### (d) $\dfrac{x^2}{(1-x)^2}$

$$\frac{x^2}{(1-x)^2} = x^2 \sum_{n \geq 0}(n+1)x^n = \sum_{n \geq 2}(n-1)x^n$$

$$a_n = \begin{cases} n-1 & n \geq 2 \\ 0 & n < 2 \end{cases}$$

---

### (e) $\dfrac{x^2-x}{(1-x)^2}$

Simplify: $\dfrac{x(x-1)}{(1-x)^2} = \dfrac{-x(1-x)}{(1-x)^2} = \dfrac{-x}{1-x}$

$$\frac{-x}{1-x} = -x\sum_{n \geq 0}x^n = -\sum_{n \geq 1}x^n$$

$$a_n = \begin{cases} 0 & n=0 \\ -1 & n \geq 1 \end{cases}$$

---

### (f) $\dfrac{x^2}{(1-x)^3}$

$$[x^n]\frac{1}{(1-x)^3} = \binom{n+2}{2} = \frac{(n+2)(n+1)}{2}$$

Shifting by 2 (multiplying by $x^2$):

$$[x^n]\frac{x^2}{(1-x)^3} = [x^{n-2}]\frac{1}{(1-x)^3} = \binom{n}{2} = \frac{n(n-1)}{2}$$

$$a_n = \begin{cases} \dfrac{n(n-1)}{2} = \binom{n}{2} & n \geq 2 \\ 0 & n < 2 \end{cases}$$

---

## Adv. Problem 12 — 10 identical balloons to 4 children, each gets $\geq 2$

**Rule used:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule]] + coefficient extraction

**OGF for each child** (at least 2 balloons): $x^2 + x^3 + x^4 + \cdots = \dfrac{x^2}{1-x}$.

**Four children** (multiply):
$$G(x) = \left(\frac{x^2}{1-x}\right)^4 = \frac{x^8}{(1-x)^4}$$

**We need** the coefficient of $x^{10}$ in $G(x)$ = coefficient of $x^2$ in $\dfrac{1}{(1-x)^4}$:

$$[x^2]\frac{1}{(1-x)^4} = \binom{2+3}{3} = \binom{5}{3} = \boxed{10}$$

**Substitution check:** Let $y_i = x_i - 2 \geq 0$: $\sum y_i = 10 - 8 = 2$ in 4 variables → $C(5,3) = 10$ ✓.

---

## Adv. Problem 13 — 15 identical objects into 6 distinct boxes, $1 \leq$ each $\leq 3$

**OGF per box** (between 1 and 3 objects): $x + x^2 + x^3 = x\dfrac{1-x^3}{1-x}$

**Six boxes:**
$$G(x) = \left(x\frac{1-x^3}{1-x}\right)^6 = \frac{x^6(1-x^3)^6}{(1-x)^6}$$

**Find** coefficient of $x^{15}$ = coefficient of $x^9$ in $\dfrac{(1-x^3)^6}{(1-x)^6}$.

**Expand** $(1-x^3)^6 = \sum_{k=0}^6 \binom{6}{k}(-1)^k x^{3k}$.

For each term $(-1)^k\binom{6}{k}x^{3k}$, we need $[x^{9-3k}]\dfrac{1}{(1-x)^6} = \binom{9-3k+5}{5}$.

Only $k=0,1,2,3$ contribute (since $9-3k \geq 0$):

$$[x^9]\frac{(1-x^3)^6}{(1-x)^6} = \binom{14}{5} - \binom{6}{1}\binom{11}{5} + \binom{6}{2}\binom{8}{5} - \binom{6}{3}\binom{5}{5}$$

$$= 2002 - 6(462) + 15(56) - 20(1)$$
$$= 2002 - 2772 + 840 - 20 = \boxed{50}$$

---

## Adv. Problem 14 — Words from MISSISSIPPI with forbidden patterns

**Setup:** MISSISSIPPI has 11 letters: M(1), I(4), S(4), P(2).
**Total arrangements:** $\dfrac{11!}{4!\,4!\,2!} = \dfrac{39916800}{24 \times 24 \times 2} = \dfrac{39916800}{1152} = 34{,}650$.

### (a) Does NOT contain four S's consecutively

**Let $A$** = arrangements WITH "SSSS" as a consecutive block.

Treating SSSS as one block: remaining letters are M(1), I(4), P(2), SSSS(1) — a total of $1+4+2+1 = 8$ items with I repeated 4 times and P repeated 2 times:

$$|A| = \frac{8!}{4!\,2!} = \frac{40320}{24 \times 2} = 840$$

$$\text{Answer} = 34{,}650 - 840 = \boxed{33{,}810}$$

### (b) Neither four consecutive S's NOR two consecutive P's

**Let $A$** = contains "SSSS", **$B$** = contains "PP".

$|A| = 840$ (from above).

$|B|$: Treat PP as one block. Items: M(1), I(4), S(4), PP(1) — total $1+4+4+1 = 10$ items with I repeated 4 and S repeated 4:
$$|B| = \frac{10!}{4!\,4!} = \frac{3{,}628{,}800}{576} = 6{,}300$$

$|A \cap B|$: Both SSSS and PP are blocks. Items: M(1), I(4), SSSS(1), PP(1) — total $1+4+1+1=7$ items with I repeated 4:
$$|A \cap B| = \frac{7!}{4!} = \frac{5040}{24} = 210$$

**By PIE:**
$$|\text{neither}| = 34{,}650 - |A| - |B| + |A \cap B| = 34{,}650 - 840 - 6{,}300 + 210 = \boxed{27{,}720}$$

---

## Adv. Problem 15 — Positive integers $\leq 100$ NOT divisible by 5 or 7

**Rule used:** [[2- DM-Advanced-Counting#14. General PIE|PIE complement]]

Let $A_5$ = {integers $\leq 100$ divisible by 5}, $A_7$ = {divisible by 7}.

$$|A_5| = \lfloor 100/5 \rfloor = 20, \quad |A_7| = \lfloor 100/7 \rfloor = 14, \quad |A_{35}| = \lfloor 100/35 \rfloor = 2$$

By PIE: $|A_5 \cup A_7| = 20 + 14 - 2 = 32$.

Numbers divisible by **neither**: $100 - 32 = \boxed{68}$.

---

## Adv. Problem 16 — Positive integers $\leq 100$: odd OR perfect square

**Rule used:** PIE for two sets

Let $O$ = odd numbers $\leq 100$, $S$ = perfect squares $\leq 100$.

$$|O| = 50, \quad |S| = \lfloor\sqrt{100}\rfloor = 10, \quad |O \cap S| = |\{1,9,25,49,81\}| = 5$$

$$|O \cup S| = 50 + 10 - 5 = \boxed{55}$$

---

## Adv. Problem 17 — Positive integers $\leq 1000$: perfect square OR cube

**Rule used:** PIE for two sets

$$|S| = \lfloor\sqrt{1000}\rfloor = 31, \quad |C| = \lfloor 1000^{1/3}\rfloor = 10, \quad |S \cap C| = \lfloor 1000^{1/6}\rfloor = 3 \quad (1^6=1, 2^6=64, 3^6=729)$$

$$|S \cup C| = 31 + 10 - 3 = \boxed{38}$$

---

## Adv. Problem 18 — Union of 4 sets (each 100, pairs share 50, triples share 25, all four share 5)

**Rule used:** [[2- DM-Advanced-Counting#14. General PIE|General PIE for 4 sets]]

$$|A_1 \cup A_2 \cup A_3 \cup A_4| = \binom{4}{1}(100) - \binom{4}{2}(50) + \binom{4}{3}(25) - \binom{4}{4}(5)$$

$$= 4(100) - 6(50) + 4(25) - 1(5)$$

$$= 400 - 300 + 100 - 5 = \boxed{195}$$

---

## Adv. Problem 19 — Survey: students who like none of three vegetables

**Rule used:** PIE for three sets

Let $B$ = Brussels sprouts, $Br$ = broccoli, $C$ = cauliflower.

$$|B \cup Br \cup C| = |B| + |Br| + |C| - |B \cap Br| - |B \cap C| - |Br \cap C| + |B \cap Br \cap C|$$

$$= 64 + 94 + 58 - 26 - 28 - 22 + 14 = 216 - 76 + 14 = 154$$

$$\text{Neither} = 270 - 154 = \boxed{116}$$

---

## Adv. Problem 20 — Terms in PIE formula for 5 sets

**Rule used:** [[2- DM-Advanced-Counting#14. General PIE|General PIE formula structure]]

For $n$ sets, PIE has one term for each non-empty subset of sets:
$$\binom{5}{1} + \binom{5}{2} + \binom{5}{3} + \binom{5}{4} + \binom{5}{5} = 5 + 10 + 10 + 5 + 1 = \boxed{31}$$

*(This equals $2^5 - 1 = 31$, the number of non-empty subsets of 5 sets.)*

---

## Adv. Problem 21 — Permutations of 26 letters containing none of FISH, RAT, BIRD

**Rule used:** PIE with string-avoidance

Let $A$ = permutations containing "FISH" (4 letters as 1 block → $23!$ arrangements).
Let $B$ = permutations containing "RAT" (3 letters as 1 block → $24!$).
Let $C$ = permutations containing "BIRD" (4 letters as 1 block → $23!$).

**Check overlaps:**
- $|A \cap B|$: FISH and RAT share no letters → both fit as blocks: $22!$.
- $|A \cap C|$: FISH = {F,I,S,H} and BIRD = {B,I,R,D} share the letter **I**. A permutation of 26 letters uses each letter exactly once, so I can't appear in both blocks simultaneously → $|A \cap C| = 0$.
- $|B \cap C|$: RAT = {R,A,T} and BIRD = {B,I,R,D} share **R** → $|B \cap C| = 0$.
- $|A \cap B \cap C| = 0$ (since $|A \cap C| = 0$).

**By PIE:**

$$|A \cup B \cup C| = 23! + 24! + 23! - 22! - 0 - 0 + 0 = 2(23!) + 24! - 22!$$

Factor out $22!$: $= 22!(2 \cdot 23 + 24 \cdot 23 - 1) = 22!(46 + 552 - 1) = 597 \cdot 22!$

Wait — let me recheck: $24! = 24 \cdot 23!$. So $2 \cdot 23! + 24 \cdot 23! = 26 \cdot 23!$... no:

$2(23!) + 24! - 22! = 2(23!) + 24 \cdot 23! - 22! = 26 \cdot 23! - 22! = 22!(26 \cdot 23 - 1) = 22!(598-1) = 597 \cdot 22!$

**Permutations containing NONE:**

$$26! - 597 \cdot 22! = \boxed{26! - 597 \cdot 22!}$$

---

## Adv. Problem 22 — Non-negative solutions of $x+y+z=13$, $0 \leq x,y,z \leq 6$

**Rule used:** [[2- DM-Advanced-Counting#14. General PIE|Stars and Bars + PIE for upper bounds]]

**Unconstrained** (all $\geq 0$): $C(13+2,2) = C(15,2) = 105$.

**Let $A_x$** = solutions with $x \geq 7$: substitute $x'=x-7$, then $x'+y+z=6$ → $C(8,2)=28$.

By symmetry $|A_y| = |A_z| = 28$.

**$|A_x \cap A_y|$:** $x \geq 7, y \geq 7$ → sum $\geq 14 > 13$: impossible. So $|A_x \cap A_y| = 0$.

$$\text{Answer} = 105 - 3(28) + 0 = 105 - 84 = \boxed{21}$$

---

## Adv. Problem 23 — Solutions of $x+y+z+t=18$, $0 \leq x \leq 4$, $0 \leq y \leq 7$

**Rule used:** Stars and Bars + PIE

**Unconstrained** ($x,y,z,t \geq 0$): $C(21,3) = 1330$.

**$|A_x|$** ($x \geq 5$, substitute $x'=x-5$, sum=13): $C(16,3) = 560$.

**$|A_y|$** ($y \geq 8$, substitute $y'=y-8$, sum=10): $C(13,3) = 286$.

**$|A_x \cap A_y|$** ($x \geq 5, y \geq 8$, substitute both, sum=5): $C(8,3) = 56$.

$$1330 - 560 - 286 + 56 = \boxed{540}$$

---

## Adv. Problem 24 — Surjective functions from 7-element set to 5-element set

**Rule used:** [[2- DM-Advanced-Counting#15.2 Number of Onto (Surjective) Functions|Surjection formula via PIE]]

$$\text{Surjections} = \sum_{j=0}^{5}(-1)^j\binom{5}{j}(5-j)^7$$

| $j$ | $(-1)^j$ | $\binom{5}{j}$ | $(5-j)^7$ | Term |
|---|---|---|---|---|
| 0 | +1 | 1 | $5^7=78125$ | $+78125$ |
| 1 | $-1$ | 5 | $4^7=16384$ | $-81920$ |
| 2 | +1 | 10 | $3^7=2187$ | $+21870$ |
| 3 | $-1$ | 10 | $2^7=128$ | $-1280$ |
| 4 | +1 | 5 | $1^7=1$ | $+5$ |
| 5 | $-1$ | 1 | $0$ | $0$ |

$$78125 - 81920 + 21870 - 1280 + 5 = \boxed{16{,}800}$$

---

## Adv. Problem 25 — 6 different toys to 3 children, each gets $\geq 1$

**Rule used:** Surjections from $[6]$ to $[3]$

$$\sum_{j=0}^{3}(-1)^j\binom{3}{j}(3-j)^6 = 3^6 - 3(2^6) + 3(1^6) - 0$$

$$= 729 - 192 + 3 = \boxed{540}$$

---

## Adv. Problem 26 — 8 distinct balls into 3 distinct urns, each urn $\geq 1$

**Rule used:** Surjections from $[8]$ to $[3]$

$$3^8 - 3(2^8) + 3(1^8) = 6561 - 768 + 3 = \boxed{5796}$$

---

## Adv. Problem 27 — Derangements of $[4]$: count and complete list

**Rule used:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|$D_4 = 9$, derangement formula]]

$$D_4 = 4!\left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right) = 24\left(\frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 24\cdot\frac{12-4+1}{24} = 9$$

**All 9 derangements of $[4]$** (in one-line notation $\sigma(1)\sigma(2)\sigma(3)\sigma(4)$):

| Cycle type | Cycle notation | One-line |
|---|---|---|
| $(1\ 2)(3\ 4)$ | swap 1↔2, 3↔4 | $2143$ |
| $(1\ 3)(2\ 4)$ | swap 1↔3, 2↔4 | $3412$ |
| $(1\ 4)(2\ 3)$ | swap 1↔4, 2↔3 | $4321$ |
| $(1\ 2\ 3\ 4)$ | $1\to2\to3\to4\to1$ | $2341$ |
| $(1\ 2\ 4\ 3)$ | $1\to2\to4\to3\to1$ | $2413$ |
| $(1\ 3\ 2\ 4)$ | $1\to3\to2\to4\to1$ | $3142$ |
| $(1\ 3\ 4\ 2)$ | $1\to3\to4\to2\to1$ | $3421$ |
| $(1\ 4\ 2\ 3)$ | $1\to4\to2\to3\to1$ | $4312$ |
| $(1\ 4\ 3\ 2)$ | $1\to4\to3\to2\to1$ | $4123$ |

---

## Adv. Problem 28 — 8 students, same classroom two classes: no student same seat

**Rule used:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|$D_8$]]

The second seating arrangement must be a derangement of the first (no student occupies their same seat):

$$D_8 = 8!\left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!} - \frac{1}{5!} + \frac{1}{6!} - \frac{1}{7!} + \frac{1}{8!}\right) = \boxed{14{,}833}$$

---

## Adv. Problem 29 — Non-negative integers $\leq 100$ relatively prime to 100

**Rule used:** [[2- DM-Advanced-Counting#15.1 Euler's Phi Function|Euler's phi function]]

$100 = 2^2 \cdot 5^2$. Using the product formula for $\varphi$:

$$\varphi(100) = 100 \cdot \left(1 - \frac{1}{2}\right) \cdot \left(1 - \frac{1}{5}\right) = 100 \cdot \frac{1}{2} \cdot \frac{4}{5} = \boxed{40}$$

**Verification via PIE:** Integers $\leq 100$ divisible by 2: 50. By 5: 20. By 10: 10.
$|A_2 \cup A_5| = 50 + 20 - 10 = 60$. So coprime: $100 - 60 = 40$ ✓.

