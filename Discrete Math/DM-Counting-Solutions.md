---
tags: [discrete-mathematics, solutions, basic-counting, advanced-counting]
topic: "Complete Solutions — Basic & Advanced Counting"
course: "DISCRETE MATHEMATICS"
links:
  - "[[1- DM-Basic-Counting-Rules]]"
  - "[[2- DM-Advanced-Counting]]"
---

> [!Note] 📁 How to Use This File
> This file contains **complete solutions** to all exercises in Sections 1 (Basic Counting) and 2 (Advanced Counting) from the exercise sheet. Every solution cites the **exact rule, theorem, or formula** from the two knowledge notes. Place all three files in the **same Obsidian vault folder** so the `[[wikilinks]]` resolve correctly.
>
> **Knowledge files referenced:**
> - `[[1- DM-Basic-Counting-Rules]]` — Sum/Product/Division/Bijection rules, permutations, combinations, binomial theorem, stars-and-bars, Stirling numbers, partitions.
> - `[[2- DM-Advanced-Counting]]` — Generating functions, recurrence relations, permutation structure, PIE, derangements.

---

# Section 1 — Basic Counting Rules

---

## Problem 1 — 2-element subsets of $[n]$

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$k$-combinations formula]] $C(n,k) = \dfrac{n!}{k!(n-k)!}$.

We want to choose 2 elements (unordered, no repetition) from a set of $n$ elements.

$$\boxed{C(n,2) = \frac{n!}{2!(n-2)!} = \frac{n(n-1)}{2}}$$

---

## Problem 2 — Subsets of $[100]$ with at most 2 elements

> **Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Sum Rule]] (disjoint cases: 0-element, 1-element, 2-element subsets).

Count subsets of each size and add (the cases are mutually disjoint):

- Size 0 (empty set): $C(100,0) = 1$
- Size 1: $C(100,1) = 100$
- Size 2: $C(100,2) = \dfrac{100 \cdot 99}{2} = 4950$

$$\boxed{1 + 100 + 4950 = 5051}$$

---

## Problem 3 — Subsets of $[100]$ with MORE than 2 elements

> **Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement method]]: total subsets minus subsets with at most 2 elements.

Total subsets of a 100-element set: $2^{100}$ (from [[1- DM-Basic-Counting-Rules#1.2 Subsets of $[n]$ — The Power Set|Power Set Theorem]]).

$$\boxed{2^{100} - 5051}$$

---

## Problem 4 — Total subsets of $[n]$

> **Rule:** [[1- DM-Basic-Counting-Rules#1.2 Subsets of $[n]$ — The Power Set|Power Set Theorem]]: bijection between subsets and binary strings of length $n$.

$$\boxed{2^n}$$

---

## Problem 5 — 5-character ASCII strings containing '@' at least once

> **Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement method]] + [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]].

Total 5-character ASCII strings (128 choices per position): $128^5$.

Strings with **no** '@': each position has $127$ choices, giving $127^5$.

$$\boxed{128^5 - 127^5}$$

---

## Problem 6 — Bit strings of length 5

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Binary strings with $k$ ones = $C(n,k)$]], [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Sum Rule / Complement]].

A bit string has 5 positions; "occurrences of 0" = choosing which positions are 0.

**(a) Exactly two 0s:** Choose 2 positions out of 5 for the zeros:
$$\boxed{C(5,2) = 10}$$

**(b) At most two 0s** (0, 1, or 2 zeros):
$$C(5,0) + C(5,1) + C(5,2) = 1 + 5 + 10 = \boxed{16}$$

**(c) At least two 0s** (complement of "fewer than 2 zeros"):
$$2^5 - C(5,0) - C(5,1) = 32 - 1 - 5 = \boxed{26}$$

---

## Problem 7 — Euler's phi: $\varphi(p^k) = p^k - p^{k-1}$

> **Rule:** [[2- DM-Advanced-Counting#15.1 Euler's Phi Function|Euler's Phi via PIE]].

Among $\{1, 2, \ldots, p^k\}$, the only integers **not** coprime to $p^k$ are the multiples of $p$:
$$\{p, 2p, 3p, \ldots, p^{k-1} \cdot p\}$$
There are exactly $p^{k-1}$ such multiples. Therefore:
$$\varphi(p^k) = p^k - p^{k-1} \qquad \blacksquare$$

---

## Problem 8 — Auditorium chair labels

> **Rule:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]].

Each label = one uppercase English letter (26 choices) followed by a positive integer from 1 to 100 (100 choices). These two tasks are independent:
$$26 \times 100 = \boxed{2600}$$

---

## Problem 9 — License plates: 3 letters then 3 digits

> **Rule:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]].

- 3 uppercase letters: $26^3 = 17576$ ways
- 3 digits (0–9): $10^3 = 1000$ ways

$$26^3 \times 10^3 = \boxed{17{,}576{,}000}$$

---

## Problem 10 — Passwords of 4–8 lower/upper case letters

> **Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Sum Rule]] (disjoint by length) + [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] (52 choices per character: 26 lower + 26 upper).

$$\sum_{k=4}^{8} 52^k = 52^4 + 52^5 + 52^6 + 52^7 + 52^8$$
$$= 7{,}311{,}616 + 380{,}204{,}032 + 19{,}770{,}609{,}664 + 1{,}028{,}071{,}702{,}528 + 53{,}459{,}728{,}531{,}456$$
$$= \boxed{54{,}507{,}385{,}159{,}296}$$

---

## Problem 11 — Club selects president and 2-person advisory board

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Product Rule + Combinations]]. The president is **not** on the advisory board.

- Choose president: 10 ways
- Choose advisory board from remaining 9 people: $C(9,2) = 36$ ways

$$10 \times 36 = \boxed{360}$$

---

## Problem 12 — Five-digit numbers

> **Rule:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] + [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement method]].

**Total five-digit numbers:** The first digit has 9 choices (1–9), each remaining digit has 10 choices:
$$9 \times 10^4 = \boxed{90{,}000}$$

**No two consecutive digits equal:** The first digit has 9 choices; each subsequent digit must differ from the previous (9 choices each):
$$9 \times 9^4 = 9^5 = \boxed{59{,}049}$$

**At least one pair of consecutive digits equal:** complement of above:
$$90{,}000 - 59{,}049 = \boxed{30{,}951}$$

---

## Problem 13 — All functions from $[3]$ to $[2]$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|All functions $[m] \to [n]$: $n^m$]]. Here $m=3$, $n=2$, total $= 2^3 = 8$.

Each element of $[3]=\{1,2,3\}$ maps to either 1 or 2. Listing all 8:

| $f(1)$ | $f(2)$ | $f(3)$ |
|--------|--------|--------|
| 1 | 1 | 1 |
| 1 | 1 | 2 |
| 1 | 2 | 1 |
| 1 | 2 | 2 |
| 2 | 1 | 1 |
| 2 | 1 | 2 |
| 2 | 2 | 1 |
| 2 | 2 | 2 |

---

## Problem 14 — All one-to-one functions from $[2]$ to $[3]$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Injective functions: $P(n,m)$]]. Here $P(3,2)=3\times2=6$.

Listing all 6 injections $\{1,2\} \to \{1,2,3\}$:

$(f(1), f(2)) \in \{(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)\}$

---

## Problem 15 — All bijections from $[3]$ to $[3]$

> **Rule:** [[1- DM-Basic-Counting-Rules#1.3 Arrangements in a Line (Permutations)|Permutations of $[n]$: $n! = 3! = 6$]].

All permutations of $\{1,2,3\}$ in one-line notation:
$$123,\; 132,\; 213,\; 231,\; 312,\; 321$$

---

## Problem 16 — Number of functions from $[m]$ to $[n]$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Product Rule: each of $m$ elements has $n$ independent image choices]].

$$\boxed{n^m}$$

---

## Problem 17 — One-to-one functions from $[2]$ to $[4]$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Injective functions: $P(4,2) = 4 \times 3 = 12$]].

Listing all 12 injections $\{1,2\} \to \{1,2,3,4\}$:
$(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)$

---

## Problem 18 — One-to-one functions from $[3]$ to $[5]$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|$P(5,3) = 5 \times 4 \times 3$]].

$$P(5,3) = \frac{5!}{2!} = 60 \qquad \boxed{60}$$

---

## Problem 19 — One-to-one functions from $[m]$ to $[n]$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|$k$-permutations formula]].

$$\boxed{P(n,m) = \frac{n!}{(n-m)!}}$$
(equals 0 when $m > n$).

---

## Problem 20 — Drawing 1st, 2nd, 3rd card from 52

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$k$-permutations: ordered selection without repetition]].

$$P(52,3) = 52 \times 51 \times 50 = \boxed{132{,}600}$$

---

## Problem 21 — Drawing 2 cards (order does not matter)

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$k$-combinations: unordered selection]].

$$C(52,2) = \frac{52 \times 51}{2} = \boxed{1326}$$

---

## Problem 22 — Taking $k$ objects from $n$ distinct objects in a box

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Permutations vs. Combinations]].

**(a) Order matters:** $P(n,k) = \dfrac{n!}{(n-k)!}$

**(b) Order does not matter:** $C(n,k) = \dfrac{n!}{k!(n-k)!}$

---

## Problem 23 — Pass out $k$ distinct fruits to $n$ children, no restriction

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|All functions $[k] \to [n]$: $n^k$]]. Each fruit independently goes to any of $n$ children.

$$\boxed{n^k}$$

---

## Problem 24 — Pass out $k$ distinct fruits, each child at most one

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Injective functions / $k$-permutations]].

- If $k \leq n$: $P(n,k) = \dfrac{n!}{(n-k)!}$
- If $k > n$: **0** (impossible — more fruit than children, each child at most 1).

---

## Problem 25 — Pass out $k$ identical fruits, each child at most one

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$C(n,k)$]] — identical objects, so only *which* children receive matters.

- If $k \leq n$: $C(n,k)$ (choose $k$ children out of $n$).
- If $k > n$: **0** (impossible).

---

## Problem 26 — Bit strings of length $n$ with exactly $k$ zeros

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Binary strings with $k$ specified values = $C(n,k)$]].

Choose $k$ of the $n$ positions to be 0; the rest are 1:
$$\boxed{C(n,k) = \binom{n}{k}}$$

---

## Problem 27 — Tennis club: pairing $2n$ members

> **Rule:** [[1- DM-Basic-Counting-Rules#2.3 The Division Rule|Division Rule]] + [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]].

**Pairing only (who plays whom):**

Choose pairs in sequence: $\dfrac{(2n)!}{2^n \cdot n!}$.

*Derivation:* Order all $2n$ players: $(2n)!$ ways. Then pair up consecutive: divide by $2^n$ (each pair's internal order doesn't matter) and $n!$ (order of pairs doesn't matter).

$$\boxed{\frac{(2n)!}{2^n \cdot n!}}$$

**Pairing + who serves first:** Each of the $n$ pairs now has 2 internal orderings:
$$\frac{(2n)!}{2^n \cdot n!} \times 2^n = \frac{(2n)!}{n!}$$

---

## Problem 28 — 3-digit numbers with pairwise different, strictly decreasing digits

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$C(n,k)$ — choosing a set determines the number uniquely]].

We need 3 distinct digits from $\{0,1,\ldots,9\}$ arranged in decreasing order $d_1 > d_2 > d_3$. Once we choose the 3 digits, there is **exactly one** decreasing arrangement. However, the leading digit must be non-zero, which is guaranteed since $d_1 > d_2 > d_3 \geq 0$ implies $d_1 \geq 2 > 0$.

$$\boxed{C(10,3) = 120}$$

---

## Problem 29 — Bijection proving $C(n,k) = C(n, n-k)$

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Symmetry of combinations — $C(n,k) = C(n,n-k)$]].

**Bijection:** For any $k$-subset $A \subseteq [n]$, map $A \mapsto [n] \setminus A$. This sends $k$-subsets to $(n-k)$-subsets, is its own inverse (hence a bijection), so $C(n,k) = C(n,n-k)$. $\blacksquare$

---

## Problem 30 — Combinatorial identities (two proofs each)

> **Rule:** [[1- DM-Basic-Counting-Rules#3.1 Pascal's Theorem|Pascal's Identity]], [[1- DM-Basic-Counting-Rules#2.4 The Bijection Rule|Double counting / Bijection Rule]], [[1- DM-Basic-Counting-Rules#3.2 Binomial Theorem|Binomial Theorem]].

### (a) $\dbinom{2n}{2} = 2\dbinom{n}{2} + n^2$

**Algebraic proof:**
$$\binom{2n}{2} = \frac{2n(2n-1)}{2} = n(2n-1) = 2n^2 - n$$
$$2\binom{n}{2} + n^2 = 2\cdot\frac{n(n-1)}{2} + n^2 = n^2 - n + n^2 = 2n^2 - n \qquad \checkmark$$

**Combinatorial proof (double counting):**
Count 2-element subsets of $[2n]$, split into two halves $A=\{1,\ldots,n\}$ and $B=\{n+1,\ldots,2n\}$.
- Both from $A$: $\binom{n}{2}$; both from $B$: $\binom{n}{2}$; one from each: $n \times n = n^2$.
- Total: $2\binom{n}{2} + n^2$. $\blacksquare$

---

### (b) $\dbinom{n}{1} + 2\dbinom{n}{2} + 3\dbinom{n}{3} + \cdots + n\dbinom{n}{n} = n \cdot 2^{n-1}$

**Algebraic proof (Binomial Theorem differentiation):**
$(1+x)^n = \sum_{k=0}^n \binom{n}{k}x^k$. Differentiate both sides with respect to $x$:
$$n(1+x)^{n-1} = \sum_{k=1}^n k\binom{n}{k}x^{k-1}$$
Set $x=1$: $n \cdot 2^{n-1} = \sum_{k=1}^n k\binom{n}{k}$. $\checkmark$

**Combinatorial proof (double counting):**
Count pairs (committee, chair) where we choose a non-empty subset of $[n]$ and designate one member as chair.
- By chair: choose chair ($n$ ways), then any subset of the remaining $n-1$ ($2^{n-1}$ ways): total $n \cdot 2^{n-1}$.
- By committee size: committees of size $k$ contribute $k\binom{n}{k}$ (choose committee, then chair among $k$). Sum over all $k$: $\sum_{k=1}^n k\binom{n}{k}$. $\blacksquare$

---

### (c) $n\dbinom{n-1}{2} = \dbinom{n}{2}(n-2)$

**Algebraic proof:**
$$n\cdot\frac{(n-1)(n-2)}{2} = \frac{n(n-1)}{2}(n-2) \qquad \checkmark$$

**Combinatorial proof:** Count ordered triples $(a; b, c)$ where $a \in [n]$, $\{b,c\} \subseteq [n]\setminus\{a\}$.
- Choose $a$ first ($n$ ways), then choose $\{b,c\}$ from remaining ($\binom{n-1}{2}$ ways): $n\binom{n-1}{2}$.
- Choose $\{b,c\}$ first ($\binom{n}{2}$ ways), then choose $a$ from the remaining $n-2$ elements: $\binom{n}{2}(n-2)$. $\blacksquare$

---

### (d) Pascal's Triangle: $C_n^k = C_{n-1}^k + C_{n-1}^{k-1}$

**Algebraic proof:**
$$C_{n-1}^{k-1} + C_{n-1}^{k} = \frac{(n-1)!}{(k-1)!(n-k)!} + \frac{(n-1)!}{k!(n-1-k)!} = \frac{(n-1)!}{k!(n-k)!}[k + (n-k)] = \frac{n!}{k!(n-k)!} = C_n^k$$

**Combinatorial proof (from [[1- DM-Basic-Counting-Rules#3.1 Pascal's Theorem|Pascal's Identity]]):**
$C_n^k$ counts $k$-subsets of $[n]$. Fix element $n$: either the subset contains $n$ (choose remaining $k-1$ from $[n-1]$: $C_{n-1}^{k-1}$ ways) or it does not (choose all $k$ from $[n-1]$: $C_{n-1}^{k}$ ways). $\blacksquare$

---

### (e) $C_n^k \cdot C_k^j = C_n^j \cdot C_{n-j}^{k-j}$

**Algebraic proof:**
$$\frac{n!}{k!(n-k)!} \cdot \frac{k!}{j!(k-j)!} = \frac{n!}{j!(n-k)!(k-j)!} = \frac{n!}{j!(n-j)!} \cdot \frac{(n-j)!}{(k-j)!(n-k)!} = C_n^j \cdot C_{n-j}^{k-j}$$

**Combinatorial proof:** Count pairs (committee of $k$, sub-committee of $j$) from $[n]$.
- Choose committee of $k$ first, then sub-committee of $j$: $C_n^k \cdot C_k^j$.
- Choose sub-committee of $j$ first, then fill remaining $k-j$ from the other $n-j$: $C_n^j \cdot C_{n-j}^{k-j}$. $\blacksquare$

---

### (f) $C_n^k \cdot C_{n-k}^j = C_n^j \cdot C_{n-j}^k$

**Algebraic proof:**
$$\frac{n!}{k!(n-k)!} \cdot \frac{(n-k)!}{j!(n-k-j)!} = \frac{n!}{k!\,j!\,(n-k-j)!} = \frac{n!}{j!(n-j)!} \cdot \frac{(n-j)!}{k!(n-j-k)!} = C_n^j \cdot C_{n-j}^k$$

**Combinatorial proof:** Count ways to choose disjoint subsets $A$ (size $k$) and $B$ (size $j$) from $[n]$.
- Choose $A$ first, then $B$ from $[n]\setminus A$: $C_n^k \cdot C_{n-k}^j$.
- Choose $B$ first, then $A$ from $[n]\setminus B$: $C_n^j \cdot C_{n-j}^k$. $\blacksquare$

---

### (g) Vandermonde's Identity: $C_{m+n}^r = \sum_{i=0}^{r} C_m^i \cdot C_n^{r-i}$

**Algebraic proof (Binomial Theorem):**
$(1+x)^{m+n} = (1+x)^m(1+x)^n$. The coefficient of $x^r$ on the left is $C_{m+n}^r$. On the right, the coefficient of $x^r$ in the product is $\sum_{i=0}^r C_m^i \cdot C_n^{r-i}$ (convolution). $\checkmark$

**Combinatorial proof:** Choose $r$ people from a group of $m$ men and $n$ women. If $i$ men are chosen, then $r-i$ women are chosen: $C_m^i \cdot C_n^{r-i}$ ways. Summing over $i=0,\ldots,r$ gives $C_{m+n}^r$. $\blacksquare$

---

## Problem 31 — Permutations of ABC12DE containing string BC1

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Treat the constrained block as a single object]] + [[1- DM-Basic-Counting-Rules#1.3 Arrangements in a Line (Permutations)|$n!$ for distinct objects]].

Treat "BC1" as a single super-character. The alphabet becomes $\{A, \text{[BC1]}, 2, D, E\}$ — 5 distinct objects:
$$5! = \boxed{120}$$

---

## Problem 32 — Alternating men and women in a row ($n$ men, $n$ women)

> **Rule:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]] + [[1- DM-Basic-Counting-Rules#1.3 Arrangements in a Line (Permutations)|$n!$ permutations]].

Two alternating patterns: MWMW… or WMWM…. In each pattern, arrange the $n$ men in $n!$ ways and the $n$ women in $n!$ ways:
$$2 \times n! \times n! = \boxed{2(n!)^2}$$

---

## Problem 33 — Class of 25, choosing students for competitions

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|Combinations vs. Permutations]].

**3 students for Calculus (no roles distinguished):**
$$C(25,3) = \frac{25 \times 24 \times 23}{6} = \boxed{2300}$$

**3 students for distinct competitions (roles matter):**
$$P(25,3) = 25 \times 24 \times 23 = \boxed{13{,}800}$$

---

## Problem 34 — Soccer team of 11 from 9 female + 20 male

> **Rule:** [[1- DM-Basic-Counting-Rules#2.2 The Product Rule|Product Rule]], [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Complement method]].

**(a) Exactly 3 female:**
$$C(9,3) \times C(20,8) = 84 \times 125{,}970 = \boxed{10{,}581{,}480}$$

**(b) At least 1 female** (complement: all-male is impossible since only 20 males but need 11):
Total teams of 11 from 29 people: $C(29,11)$.
All-male teams: $C(20,11)$.
$$C(29,11) - C(20,11) = 20{,}030{,}010 - 167{,}960 = \boxed{19{,}862{,}050}$$

---

## Problem 35 — Bit strings of length 7: starts with 0 OR ends with 10

> **Rule:** [[2- DM-Advanced-Counting#13. Two-Set and Three-Set PIE|PIE for two sets]].

Let $A$ = strings starting with 0, $B$ = strings ending with 10.

$|A| = 2^6 = 64$ (first bit fixed, 6 free bits).
$|B| = 2^5 = 32$ (last 2 bits fixed, 5 free bits).
$|A \cap B| = 2^4 = 16$ (first bit and last 2 bits fixed, 4 free).

$$|A \cup B| = 64 + 32 - 16 = \boxed{80}$$

---

## Problem 36 — Pascal's triangle: two rows after the row of $\binom{10}{k}$

> **Rule:** [[1- DM-Basic-Counting-Rules#3.1 Pascal's Theorem|Pascal's Identity]]: $C(n,k) = C(n-1,k-1) + C(n-1,k)$.

**Row 10 (given):** $1\ 10\ 45\ 120\ 210\ 252\ 210\ 120\ 45\ 10\ 1$

**Row 11** (each entry = sum of two entries above):
$$1\ 11\ 55\ 165\ 330\ 462\ 462\ 330\ 165\ 55\ 11\ 1$$

**Row 12:**
$$1\ 12\ 66\ 220\ 495\ 792\ 924\ 792\ 495\ 220\ 66\ 12\ 1$$

---

## Problem 37 — Coefficient of $x^{101}y^{99}$ in $(2x - 3y)^{200}$

> **Rule:** [[1- DM-Basic-Counting-Rules#3.2 Binomial Theorem|Binomial Theorem]]: $(a+b)^n = \sum_{k=0}^n \binom{n}{k}a^k b^{n-k}$.

Write $(2x-3y)^{200} = \sum_{k=0}^{200} \binom{200}{k}(2x)^k(-3y)^{200-k}$.

For $x^{101}y^{99}$: need $k=101$, $200-k=99$.

$$\text{Coefficient} = \binom{200}{101}(2)^{101}(-3)^{99} = \boxed{-\binom{200}{101} \cdot 2^{101} \cdot 3^{99}}$$

---

## Problem 38 — Coefficient of $x^k$ in $\left(x + \frac{1}{x}\right)^{100}$

> **Rule:** [[1- DM-Basic-Counting-Rules#3.2 Binomial Theorem|Binomial Theorem]] (see also [[1- DM-Basic-Counting-Rules#📘 Examples & Applications|Example 5 in knowledge file]]).

$$\left(x + \frac{1}{x}\right)^{100} = \sum_{j=0}^{100}\binom{100}{j}x^j \cdot x^{-(100-j)} = \sum_{j=0}^{100}\binom{100}{j}x^{2j-100}$$

Set $2j - 100 = k \implies j = \dfrac{k+100}{2}$.

$$\text{Coefficient of } x^k = \begin{cases} \dbinom{100}{\frac{k+100}{2}} & \text{if } k \in \{-100,-98,\ldots,98,100\} \text{ (i.e., $k$ even and $|k|\leq 100$)} \\ 0 & \text{otherwise} \end{cases}$$

---

## Problem 39 — Coefficient of $x^{101}y^{99}z^{105}$ in $(2x-3y-z)^{305}$

> **Rule:** [[1- DM-Basic-Counting-Rules#3.3 Multinomial Theorem|Multinomial Theorem]]: coefficient of $x_1^{r_1}\cdots x_m^{r_m}$ in $(c_1x_1+\cdots+c_mx_m)^n$ is $\dfrac{n!}{r_1!\cdots r_m!}\prod c_i^{r_i}$.

Here $r_1=101$, $r_2=99$, $r_3=105$, $r_1+r_2+r_3=305$ ✓, and $c_1=2$, $c_2=-3$, $c_3=-1$.

$$\text{Coefficient} = \frac{305!}{101!\,99!\,105!} \cdot 2^{101} \cdot (-3)^{99} \cdot (-1)^{105}$$
$$= \boxed{\frac{305!}{101!\,99!\,105!} \cdot 2^{101} \cdot (-3)^{99} \cdot (-1)^{105}}$$

Since $(-3)^{99}$ is negative and $(-1)^{105}$ is negative, the product $(-3)^{99}(-1)^{105}$ is positive, giving a final positive coefficient of $\dfrac{305!}{101!\,99!\,105!}\cdot 2^{101}\cdot 3^{99}$.

---

## Problem 40 — Painting 10 distinct chairs: 3 green, 3 blue, 4 red

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Multinomial coefficient]] (see [[1- DM-Basic-Counting-Rules#📘 Examples & Applications|Example 9 in knowledge file]]).

$$\frac{10!}{3!\,3!\,4!} = \frac{3{,}628{,}800}{6 \cdot 6 \cdot 24} = \boxed{4200}$$

---

## Problem 41 — Lattice paths from $(0,0)$ to $(m,n)$

> **Rule:** [[1- DM-Basic-Counting-Rules#3. Permutations and Combinations — Formulas|$C(m+n, m)$]] — every path uses exactly $m$ right-steps (R) and $n$ up-steps (U) in some order.

A path consists of $m+n$ steps total; choosing which $m$ of them are horizontal (R) determines the path:
$$\boxed{C(m+n, m) = \binom{m+n}{m}}$$

---

## Problem 42 — True or False: $\binom{n}{k} = \binom{n-2}{k-2} + \binom{n-2}{k-1} + \binom{n-2}{k}$

> **Rule:** [[1- DM-Basic-Counting-Rules#3.1 Pascal's Theorem|Pascal's Identity applied twice]].

**True.** Using Pascal twice:
$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$
Apply Pascal to each:
$$\binom{n-1}{k-1} = \binom{n-2}{k-2} + \binom{n-2}{k-1}, \quad \binom{n-1}{k} = \binom{n-2}{k-1} + \binom{n-2}{k}$$
Adding: $\binom{n}{k} = \binom{n-2}{k-2} + 2\binom{n-2}{k-1} + \binom{n-2}{k}$.

This equals $\binom{n-2}{k-2} + \binom{n-2}{k-1} + \binom{n-2}{k}$ only if $\binom{n-2}{k-1} = 0$, which is not generally true.

**Therefore the statement is FALSE** in general. (Counterexample: $n=4$, $k=2$: LHS $= 6$; RHS $= 1+2+1 = 4 \neq 6$.)

---

## Problem 43 — Distinct strings from CASABLANCA

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Permutations with repetition]]: $\dfrac{n!}{n_1!\,n_2!\cdots}$.

CASABLANCA has 10 letters: C(2), A(4), S(1), B(1), L(1), N(1).

$$\frac{10!}{2!\,4!\,1!\,1!\,1!\,1!} = \frac{3{,}628{,}800}{2 \times 24} = \boxed{75{,}600}$$

---

## Problem 44 — Distinct strings from SUCCESS

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Permutations with repetition]].

SUCCESS has 7 letters: S(3), U(1), C(2), E(1).

$$\frac{7!}{3!\,1!\,2!\,1!} = \frac{5040}{6 \times 2} = \boxed{420}$$

---

## Problem 45 — Coefficient of $x^3y^2z^5$ in $(2x - 3y - 2z)^{10}$

> **Rule:** [[1- DM-Basic-Counting-Rules#3.3 Multinomial Theorem|Multinomial Theorem]].

$r_1=3$, $r_2=2$, $r_3=5$, sum $=10$ ✓. Coefficients: $c_1=2$, $c_2=-3$, $c_3=-2$.

$$\frac{10!}{3!\,2!\,5!} \cdot 2^3 \cdot (-3)^2 \cdot (-2)^5 = 2520 \cdot 8 \cdot 9 \cdot (-32) = 2520 \times (-2304) = \boxed{-5{,}806{,}080}$$

---

## Problem 46 — Lining up 3 identical red + 2 identical golden apples

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Permutations with repetition]].

$$\frac{5!}{3!\,2!} = \frac{120}{12} = \boxed{10}$$

---

## Problem 47 — Lining up 3 red + 2 golden + 4 green apples (all identical within color)

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Permutations with repetition]].

$$\frac{9!}{3!\,2!\,4!} = \frac{362{,}880}{6 \times 2 \times 24} = \boxed{1260}$$

---

## Problem 48 — Distribute $k$ indistinguishable apples to $n$ children

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars / $k$-combinations with repetition]].

Equivalent to non-negative integer solutions of $x_1+\cdots+x_n = k$:
$$\boxed{C(n+k-1,\,k)}$$

---

## Problem 49 — Place $k$ indistinguishable books onto $n$ shelves

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars]]. Identical to distributing $k$ identical objects into $n$ distinct bins.

$$\boxed{C(n+k-1,\,k)}$$

---

## Problem 50 — Non-negative solutions of $x_1 + \cdots + x_n = k$

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars Theorem]].

$$\boxed{C(n+k-1,\,k) = C(n+k-1,\,n-1)}$$

---

## Problem 51 — Positive integer solutions of $x_1 + \cdots + x_n = k$

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]]: substitute $y_i = x_i - 1 \geq 0$.

$\sum y_i = k - n$. Solutions exist only when $k \geq n$:
$$\boxed{C(k-1,\,n-1)}$$

---

## Problem 52 — Pass out $k$ indistinguishable apples to $n$ children, each gets $\geq 1$

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with $x_i \geq 1$ substitution]] (same as Problem 51 but reframed as distribution).

Substitute $y_i = x_i - 1 \geq 0$; then $\sum y_i = k-n$. Need $k \geq n$:
$$\boxed{C(k-1,\,n-1)}$$

---

## Problem 53 — Circular arrangement of $n$ red and $n+1$ black checkers

> **Rule:** [[1- DM-Basic-Counting-Rules#1.4 Arrangements at a Round Table|Circular permutations with identical objects]].

Total checkers: $2n+1$. Fix one black checker to remove rotational equivalence. Arrange the remaining $2n$ checkers (n red, n black) in the $2n$ remaining positions:

$$\frac{(2n)!}{n!\,n!} = \boxed{C(2n,n)}$$

---

## Problem 54 — Solutions of $x_1+x_2+x_3+x_4+x_5=21$ with constraints

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars]] + [[2- DM-Advanced-Counting#15. Applications of PIE|PIE for upper bound constraints]].

**(a) $x_i \geq 1$:** substitute $y_i = x_i - 1 \geq 0$, $\sum y_i = 16$:
$$C(16+4,4) = C(20,4) = \boxed{4845}$$

**(b) $x_i \geq 2$:** substitute $y_i = x_i - 2 \geq 0$, $\sum y_i = 11$:
$$C(11+4,4) = C(15,4) = \boxed{1365}$$

**(c) $0 \leq x_1 \leq 10$:** Unconstrained non-negative: $C(21+4,4) = C(25,4) = 12650$. Subtract cases where $x_1 \geq 11$ (set $x_1' = x_1-11$, $\sum = 10$: $C(14,4) = 1001$). By PIE (only $x_1$ has upper bound; other variables unconstrained):
$$12650 - 1001 = \boxed{11649}$$

---

## Problem 55 — Non-negative solutions of $x_1+x_2+x_3 \leq 11$

> **Rule:** [[1- DM-Basic-Counting-Rules#📘 Examples & Applications|Stars and Bars inequality trick (Example 8 in knowledge file)]]: introduce slack variable $x_4 \geq 0$ so $x_1+x_2+x_3+x_4 = 11$.

$$C(11+3,3) = C(14,3) = \boxed{364}$$

---

## Problem 56 — Partitions of $\mathbb{R}$

> **Rule:** A **partition** requires sets to be mutually disjoint, cover everything, and be non-empty.

**(a)** Positive integers + negative integers: **Not a partition** — omits $0$ and all non-integers.

**(b)** Non-positive integers + non-negative integers: **Not a partition** — $0$ appears in both sets (not disjoint), and non-integers are omitted.

**(c)** Rationals + irrationals: **Yes, a partition** — every real is either rational or irrational (not both), and together they cover $\mathbb{R}$.

**(d)** Closed intervals $[n, n+1]$ for $n \in \mathbb{Z}$: **Not a partition** — adjacent intervals share endpoints (e.g., $[0,1]$ and $[1,2]$ both contain $1$).

**(e)** Intervals $(n, n+1]$ for $n \in \mathbb{Z}$: **Yes, a partition** — these are pairwise disjoint (left endpoint excluded) and their union is all of $\mathbb{R}$.

---

## Problem 57 — All partitions of $[4]$, Stirling numbers, Bell number

> **Rule:** [[1- DM-Basic-Counting-Rules#6.1 Definitions: Partitions and Stirling Numbers|Stirling numbers $S(n,k)$ and Bell numbers]].

**$k=1$:** $\{\{1,2,3,4\}\}$. $S(4,1)=1$.

**$k=2$:** All 2-block partitions of $[4]$: $S(4,2) = 2^{4-1}-1 = 7$.
$\{1\}|\{2,3,4\}$, $\{2\}|\{1,3,4\}$, $\{3\}|\{1,2,4\}$, $\{4\}|\{1,2,3\}$, $\{1,2\}|\{3,4\}$, $\{1,3\}|\{2,4\}$, $\{1,4\}|\{2,3\}$.

**$k=3$:** $S(4,3) = C(4,2) = 6$.
$\{1,2\}|\{3\}|\{4\}$, $\{1,3\}|\{2\}|\{4\}$, $\{1,4\}|\{2\}|\{3\}$, $\{2,3\}|\{1\}|\{4\}$, $\{2,4\}|\{1\}|\{3\}$, $\{3,4\}|\{1\}|\{2\}$.

**$k=4$:** $\{1\}|\{2\}|\{3\}|\{4\}$. $S(4,4)=1$.

**4th Bell number:** $B(4) = S(4,1)+S(4,2)+S(4,3)+S(4,4) = 1+7+6+1 = \boxed{15}$.

---

## Problem 58 — $S(n,1)$, $S(n,n-1)$, $S(n,n)$

> **Rule:** [[1- DM-Basic-Counting-Rules#6.2 Recurrence and Special Values|Special values of Stirling numbers]].

$$S(n,1) = 1 \quad \text{(only one partition into 1 block: all elements together)}$$
$$S(n,n-1) = C(n,2) = \frac{n(n-1)}{2} \quad \text{(exactly one pair merged, rest singletons)}$$
$$S(n,n) = 1 \quad \text{(only partition into $n$ blocks: all singletons)}$$

---

## Problem 59 — Recurrence for $S(n,k)$ and $S(n,2)$

> **Rule:** [[1- DM-Basic-Counting-Rules#6.2 Recurrence and Special Values|Stirling number recurrence]].

**Recurrence:**
$$S(n,k) = S(n-1,k-1) + k \cdot S(n-1,k)$$

*Derivation:* Consider element $n$. Either $\{n\}$ forms its own block ($S(n-1,k-1)$ ways for the rest), or $n$ is added to one of the $k$ existing blocks of a partition of $[n-1]$ into $k$ blocks ($k \cdot S(n-1,k)$ ways).

**$S(n,2)$:** Using the recurrence with $S(n,2) = S(n-1,1) + 2S(n-1,2) = 1 + 2S(n-1,2)$, with $S(2,2)=1$:
$$S(n,2) = 2^{n-1} - 1$$

---

## Problem 60 — Bijection: partitions of $[n]$ into 2 parts $\leftrightarrow$ non-empty subsets of $[n-1]$

> **Rule:** [[1- DM-Basic-Counting-Rules#2.4 The Bijection Rule|Bijection Rule]].

**Bijection:** Given a 2-partition $\{A, B\}$ of $[n]$ with $n \in A$ (WLOG), map it to the set $A \setminus \{n\} \subseteq [n-1]$. Since $A \neq \emptyset$ and $A \setminus \{n\}$ can be any subset of $[n-1]$ (including $\emptyset$ when $A = \{n\}$, but then $B=[n-1]$ is non-empty). Actually we map $\{A,B\}$ to whichever part **does not** contain $n$: that part is a non-empty subset of $[n-1]$ (non-empty since otherwise all elements but $n$ are in $A$, making $B = \emptyset$). This map is a bijection from 2-partitions of $[n]$ to non-empty subsets of $[n-1]$, confirming $S(n,2) = 2^{n-1}-1$.

---

## Problem 61 — Which collections are partitions of $\{1,2,3,4,5,6\}$?

**(a)** $\{1,2\}, \{2,3,4\}, \{4,5,6\}$: **Not a partition** — element 2 appears twice; element 4 appears twice; element 6 not covered correctly; 1 is missing from second partition. (Overlap: $2 \in$ both first and second sets; $4 \in$ both second and third.)

**(b)** $\{1\}, \{2,3,6\}, \{4\}$: **Not a partition** — element 5 is missing.

**(c)** $\{2,4,6\}, \{1,3,5\}$: **Yes, a partition** — disjoint, union = $\{1,2,3,4,5,6\}$, both non-empty.

**(d)** $\{1,4,5\}, \{2,6\}$: **Not a partition** — element 3 is missing.

---

## Problem 62 — Place 4 distinct gifts into 3 identical boxes

> **Rule:** [[1- DM-Basic-Counting-Rules#6.1 Definitions: Partitions and Stirling Numbers|Stirling numbers (identical boxes, distinct gifts)]]: $\sum_{k=1}^{3} S(4,k)$.

$$S(4,1)+S(4,2)+S(4,3) = 1+7+6 = \boxed{14}$$

---

## Problem 63 — 4 distinct gifts into 3 identical boxes, each box $\geq 1$

> **Rule:** [[1- DM-Basic-Counting-Rules#6.1 Definitions: Partitions and Stirling Numbers|Stirling number $S(4,3)$]].

$$S(4,3) = \boxed{6}$$

---

## Problem 64 — Place 4 identical gifts into 3 identical boxes

> **Rule:** Integer partitions of 4 into at most 3 parts (order doesn't matter, objects identical).

Partitions of 4 with at most 3 parts: $(4)$, $(3,1)$, $(2,2)$, $(2,1,1)$, $(1,1,1,1)$ — but at most 3 boxes:
$(4,0,0)$, $(3,1,0)$, $(2,2,0)$, $(2,1,1)$.

$$\boxed{4}$$

---

## Problem 65 — 4 identical gifts into 3 identical boxes, each box $\geq 1$

Partitions of 4 into exactly 3 positive parts: $(2,1,1)$.

$$\boxed{1}$$

---

## Problem 66 — Place 15 distinct gifts into 10 distinct boxes

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|All functions: $10^{15}$]] (each gift independently goes to any of 10 boxes).

$$\boxed{10^{15}}$$

---

## Problem 67 — 15 distinct gifts into 10 distinct boxes, each box $\geq 1$

> **Rule:** [[2- DM-Advanced-Counting#15.2 Number of Onto (Surjective) Functions|Surjection count via PIE]].

Number of surjections from 15-element set to 10-element set:
$$\sum_{j=0}^{10}(-1)^j\binom{10}{j}(10-j)^{15}$$

---

## Problem 68 — 15 distinct gifts into 10 distinct boxes, each box $\leq 1$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Injective functions]]. Since $15 > 10$, impossible.

$$\boxed{0}$$

---

## Problem 69 — 10 distinct gifts into 15 distinct boxes, each box $\leq 1$

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|$k$-permutations / injective functions]]: $P(15,10)$.

$$P(15,10) = \frac{15!}{5!} = \boxed{10{,}897{,}286{,}400}$$

---

## Problem 70 — Place 100 identical gifts into 3 distinct boxes

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars]]: non-negative integer solutions of $x_1+x_2+x_3=100$.

$$C(100+2,\,2) = C(102,2) = \frac{102 \times 101}{2} = \boxed{5151}$$

---

## Problem 71 — 100 identical gifts into 10 distinct boxes, each $\geq 5$

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]].

Substitute $y_i = x_i - 5 \geq 0$: $\sum y_i = 100 - 50 = 50$. Then:
$$C(50+9,\,9) = C(59,9) = \boxed{C(59,9)}$$

---

## Problem 72 — All permutations of $[4]$ mapping $1 \to 3$

> **Rule:** [[1- DM-Basic-Counting-Rules#1.3 Arrangements in a Line (Permutations)|Fix one value, permute the rest]]: $\sigma(1)=3$ is fixed; the remaining 3 elements $\{2,3,4\} \setminus \{3\} \cup \{1\} = \{1,2,4\}$ map to $\{1,2,4\}$ freely in $3!=6$ ways.

The $3! = 6$ permutations (one-line notation):

$3124,\ 3142,\ 3214,\ 3241,\ 3412,\ 3421$

---

## Problem 73 — Permutations of $[5]$ with $\sigma(5)=5$ and $\sigma(3)=2$

Both $\sigma(5)=5$ and $\sigma(3)=2$ are fixed. The remaining elements $\{1,2,4\}$ must map to $\{1,3,4\}$ (since 2 and 5 are already used as images). That gives $3!=6$ choices... but $\sigma(3)=2$ is already set, so images 2 and 5 are used; remaining domain: $\{1,2,4\}$, remaining codomain values: $\{1,3,4\}$. So $3! = 6$ permutations.

In two-line notation (showing all 6):

$$\begin{pmatrix}1&2&3&4&5\\a&b&2&c&5\end{pmatrix}$$

where $(a,b,c)$ is a permutation of $(1,3,4)$: $(1,3,4),(1,4,3),(3,1,4),(3,4,1),(4,1,3),(4,3,1)$.

---

## Problem 74 — Cycle notation, inverse, square of given permutations

> **Rule:** [[2- DM-Advanced-Counting#10.2 Cycle Notation|Cycle decomposition]], [[2- DM-Advanced-Counting#10.4 Inverse of a Permutation|Inverse by reversing cycles]], [[2- DM-Advanced-Counting#10.3 Composition ($\sigma^2$ and $\sigma \circ \tau$)|Squaring]].

### (a) $\sigma = 36215847$ (i.e., $\sigma(1)=3,\sigma(2)=6,\ldots$)

Trace orbits: $1\to3\to2\to6\to8\to7\to4\to1$ (7-cycle), $5\to5$ (fixed).

**Cycle notation:** $(1\;3\;2\;6\;8\;7\;4)(5)$. **Fixed points:** $\{5\}$. **Number of cycles:** 2.

**$\sigma^{-1}$:** Reverse the 7-cycle: $(1\;4\;7\;8\;6\;2\;3)(5)$.
One-line: $\sigma^{-1} = 4\ 3\ 1\ 7\ 5\ 2\ 8\ 6$.

**$\sigma^2$:** The 7-cycle (odd length) squared is a 7-cycle. Apply $\sigma$ twice to each element:
$1\to3\to2$, $2\to6\to8$, $3\to2\to6$, $4\to1\to3$, $6\to8\to7$, $7\to4\to1$, $8\to7\to4$, $5\to5$.
$\sigma^2 = 2\ 8\ 6\ 3\ 5\ 7\ 1\ 4$, cycle: $(1\;2\;8\;4\;3\;6\;7)(5)$.

---

### (b) $\sigma = 42765813$

Trace: $1\to4\to6\to8\to3\to7\to1$ — wait, let me re-read: $\sigma(1)=4,\sigma(2)=2,\sigma(3)=7,\sigma(4)=6,\sigma(5)=5,\sigma(6)=8,\sigma(7)=1,\sigma(8)=3$.

$1\to4\to6\to8\to3\to7\to1$: $(1\;4\;6\;8\;3\;7)$ (6-cycle). $2\to2$, $5\to5$: fixed points.

**Cycle notation:** $(1\;4\;6\;8\;3\;7)(2)(5)$. **Fixed points:** $\{2,5\}$. **Cycles:** 3.

**$\sigma^{-1}$:** Reverse 6-cycle: $(1\;7\;3\;8\;6\;4)(2)(5)$.
One-line: $\sigma^{-1} = 7\ 2\ 8\ 1\ 5\ 3\ 6\ 4$... Wait: $\sigma^{-1}(1)=7$ (since $\sigma(7)=1$), $\sigma^{-1}(4)=1$, $\sigma^{-1}(6)=4$, $\sigma^{-1}(8)=6$, $\sigma^{-1}(3)=8$, $\sigma^{-1}(7)=3$. So one-line: $7\ 2\ 8\ 1\ 5\ 4\ 3\ 6$.

**$\sigma^2$:** 6-cycle (even) splits into two 3-cycles. $(1\;4\;6\;8\;3\;7)^2 = (1\;6\;3)(4\;8\;7)$.
$\sigma^2 = (1\;6\;3)(4\;8\;7)(2)(5)$. One-line: $6\ 2\ 1\ 8\ 5\ 3\ 4\ 7$.

---

### (c) $\sigma = 361452$ on $[6]$

$\sigma(1)=3,\sigma(2)=6,\sigma(3)=1,\sigma(4)=4,\sigma(5)=5,\sigma(6)=2$.

Trace: $1\to3\to1$: $(1\;3)$. $2\to6\to2$: $(2\;6)$. $4\to4$, $5\to5$: fixed.

**Cycle notation:** $(1\;3)(2\;6)(4)(5)$. **Fixed points:** $\{4,5\}$. **Cycles:** 4.

**$\sigma^{-1}$:** Transpositions are self-inverse: $\sigma^{-1} = \sigma = (1\;3)(2\;6)$. One-line: $361452$.

**$\sigma^2$:** $(1\;3)^2 = \text{id}$, $(2\;6)^2 = \text{id}$, so $\sigma^2 = \text{id} = 123456$.

---

### (d) $\sigma = 32156487$ on $[8]$

$\sigma(1)=3,\sigma(2)=2,\sigma(3)=1,\sigma(4)=5,\sigma(5)=6,\sigma(6)=4,\sigma(7)=8,\sigma(8)=7$.

Trace: $1\to3\to1$: $(1\;3)$. $2\to2$: fixed. $4\to5\to6\to4$: $(4\;5\;6)$. $7\to8\to7$: $(7\;8)$.

**Cycle notation:** $(1\;3)(2)(4\;5\;6)(7\;8)$. **Fixed points:** $\{2\}$. **Cycles:** 4.

**$\sigma^{-1}$:** $(1\;3)^{-1}=(1\;3)$; $(4\;5\;6)^{-1}=(4\;6\;5)$; $(7\;8)^{-1}=(7\;8)$.
One-line: $\sigma^{-1}(1)=3,\sigma^{-1}(2)=2,\sigma^{-1}(3)=1,\sigma^{-1}(4)=6,\sigma^{-1}(5)=4,\sigma^{-1}(6)=5,\sigma^{-1}(7)=8,\sigma^{-1}(8)=7$: $32165487$.

**$\sigma^2$:** $(1\;3)^2=\text{id}$; $(4\;5\;6)^2=(4\;6\;5)$ (odd cycle); $(7\;8)^2=\text{id}$.
$\sigma^2 = (4\;6\;5)$. One-line: $1\ 2\ 3\ 6\ 4\ 5\ 7\ 8$.

---

## Problem 75 — Two-line notation from cycle notation; $\sigma^{-1}$ and $\sigma^2$

> **Rule:** [[2- DM-Advanced-Counting#10.1 One-Line Notation|Cycle to two-line conversion]], [[2- DM-Advanced-Counting#10.3 Composition ($\sigma^2$ and $\sigma \circ \tau$)|Squaring]], [[2- DM-Advanced-Counting#10.4 Inverse of a Permutation|Inverse]].

### (a) $\sigma = (1,3,5)(2,4,6)$ on $[6]$

Two-line: $\sigma(1)=3,\sigma(2)=4,\sigma(3)=5,\sigma(4)=6,\sigma(5)=1,\sigma(6)=2$.
$$\sigma = \begin{pmatrix}1&2&3&4&5&6\\3&4&5&6&1&2\end{pmatrix}$$

**$\sigma^{-1}$:** $(1,5,3)(2,6,4)$. Two-line: $5\ 6\ 1\ 2\ 3\ 4$.

**$\sigma^2$:** Both are 3-cycles (odd): $(1,3,5)^2=(1,5,3)$; $(2,4,6)^2=(2,6,4)$. Two-line: $5\ 6\ 1\ 2\ 3\ 4$.

---

### (b) $\sigma = (2,3)(1,7)(5)(6,2)$ on $[7]$

**Note:** This is a composition, not disjoint cycles. $(6,2)$ and $(2,3)$ share element 2, so we compose right to left: first apply $(6,2)$, then $(5)$, then $(1,7)$, then $(2,3)$.

Apply right to left (i.e., $(6,2)$ first, then $(1,7)$, then $(2,3)$, noting $(5)$ is identity):

- $1\xrightarrow{(6,2)}\!1\xrightarrow{(1,7)}\!7\xrightarrow{(2,3)}\!7$: so $\sigma(1)=7$.
- $2\xrightarrow{(6,2)}\!6\xrightarrow{(1,7)}\!6\xrightarrow{(2,3)}\!6$: $\sigma(2)=6$.
- $3\xrightarrow{(6,2)}\!3\xrightarrow{(1,7)}\!3\xrightarrow{(2,3)}\!2$: $\sigma(3)=2$.
- $4\xrightarrow{}\!4\to4\to4$: $\sigma(4)=4$.
- $5\to5$: $\sigma(5)=5$.
- $6\xrightarrow{(6,2)}\!2\xrightarrow{(1,7)}\!2\xrightarrow{(2,3)}\!3$: $\sigma(6)=3$.
- $7\xrightarrow{(6,2)}\!7\xrightarrow{(1,7)}\!1\xrightarrow{(2,3)}\!1$: $\sigma(7)=1$.

$$\sigma = \begin{pmatrix}1&2&3&4&5&6&7\\7&6&2&4&5&3&1\end{pmatrix}$$

Cycle decomposition: $1\to7\to1$: $(1\;7)$; $2\to6\to3\to2$: $(2\;6\;3)$; $4,5$ fixed.
$\sigma = (1\;7)(2\;6\;3)(4)(5)$.

**$\sigma^{-1}$:** $(1\;7)(2\;3\;6)$. Two-line: $7\ 3\ 6\ 4\ 5\ 2\ 1$.

**$\sigma^2$:** $(1\;7)^2=\text{id}$; $(2\;6\;3)^2=(2\;3\;6)$. Two-line: $1\ 3\ 6\ 4\ 5\ 2\ 7$.

---

### (c) $\sigma = (7,5,3,1)(2,4,6)$ on $[7]$

$\sigma(7)=5,\sigma(5)=3,\sigma(3)=1,\sigma(1)=7,\sigma(2)=4,\sigma(4)=6,\sigma(6)=2$.
$$\sigma = \begin{pmatrix}1&2&3&4&5&6&7\\7&4&1&6&3&2&5\end{pmatrix}$$

**$\sigma^{-1}$:** $(1,3,5,7)(2,6,4)$. Two-line: $3\ 6\ 5\ 2\ 7\ 4\ 1$.

**$\sigma^2$:** $(7,5,3,1)^2=(7,3)(5,1)$ (4-cycle splits); $(2,4,6)^2=(2,6,4)$ (3-cycle, odd). Two-line: $3\ 6\ 7\ 2\ 1\ 4\ 5$.

---

### (d) $\sigma = (2,7)(6,5,1)(4,3)$ on $[7]$

$\sigma(2)=7,\sigma(7)=2,\sigma(6)=5,\sigma(5)=1,\sigma(1)=6,\sigma(4)=3,\sigma(3)=4$.
$$\sigma = \begin{pmatrix}1&2&3&4&5&6&7\\6&7&4&3&1&5&2\end{pmatrix}$$

**$\sigma^{-1}$:** $(2,7)(1,5,6)(3,4)$. Two-line: $5\ 7\ 4\ 3\ 6\ 1\ 2$.

**$\sigma^2$:** $(2,7)^2=\text{id}$; $(6,5,1)^2=(6,1,5)$ (3-cycle); $(4,3)^2=\text{id}$. Two-line: $5\ 2\ 3\ 4\ 6\ 1\ 7$.

---

## Problem 76 — Permutations without fixed points (derangements) on $[4]$ and $[6]$

> **Rule:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|Derangements formula: $D_n = n!\sum_{k=0}^n(-1)^k/k!$]].

$D_4 = 9$. The 9 derangements of $[4]$ (from [[2- DM-Advanced-Counting#📘 Examples & Applications — Permutation Structure|Example 8 in knowledge file]]):

Cycle type $(4)$: $(1\;2\;3\;4),(1\;2\;4\;3),(1\;3\;2\;4),(1\;3\;4\;2),(1\;4\;2\;3),(1\;4\;3\;2)$ — 6 permutations.
Cycle type $(2,2)$: $(1\;2)(3\;4),(1\;3)(2\;4),(1\;4)(2\;3)$ — 3 permutations.

$D_6 = 6!\left(1-1+\frac{1}{2}-\frac{1}{6}+\frac{1}{24}-\frac{1}{120}+\frac{1}{720}\right) = 720 \cdot \frac{265}{720} = \boxed{265}$

---

## Problem 77 — Permutations with exactly 2 cycles on $[4]$ and $[6]$

> **Rule:** [[2- DM-Advanced-Counting#12. Stirling Numbers of the First Kind|$c(n,k)$ = unsigned Stirling number of the first kind]].

$c(4,2) = 11$ (from the table in the knowledge file).

Listing all 11 permutations of $[4]$ with exactly 2 cycles (cycle types $(1,3)$ and $(2,2)$ — no, wait: two cycles summing to 4 means types $(1,3)$ and $(2,2)$):
- Type $(1,3)$: 1 fixed point + 3-cycle: choose fixed point ($C(4,1)=4$), form 3-cycle from rest ($(3-1)!=2$): $4\times2=8$.
- Type $(2,2)$: two 2-cycles: $C(4,2)/2=3$ ways.
Total: $8+3=11$. ✓

$c(6,2)$: Using recurrence $c(6,2) = c(5,1) + 5\cdot c(5,2)$, with $c(5,1)=4!=24$ and $c(5,2)=50$:
$c(6,2) = 24 + 5\times50 = 274$.

---

## Problem 78 — Derangements of $[3]$ and $[4]$; prove $D_n = (n-1)(D_{n-1}+D_{n-2})$

> **Rule:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|Derangement formula and recurrence]].

**$D_3 = 2$:** The 2 derangements of $[3]$: $231$ and $312$ (i.e., $(1\;2\;3)$ and $(1\;3\;2)$).

**$D_4 = 9$:** Listed in Problem 76 above.

**Proof of $D_n = (n-1)(D_{n-1}+D_{n-2})$:**

Consider a derangement $\sigma$ of $[n]$. Suppose $\sigma(n) = k$ for some $k \neq n$ ($n-1$ choices for $k$). Now look at element $k$:

**Case 1:** $\sigma(k) = n$ (i.e., $k$ and $n$ swap). The remaining $n-2$ elements must form a derangement of $[n]\setminus\{k,n\}$: $D_{n-2}$ ways.

**Case 2:** $\sigma(k) \neq n$. Define $\tau$ on $[n-1]$ by $\tau(i) = \sigma(i)$ for $i \neq k$ and $\tau(k) = \sigma(k)$ (replacing the role of $n$ with $k$). Then $\tau$ is a derangement of $[n-1]$: $D_{n-1}$ ways.

By the sum rule and the $n-1$ choices for $k$:
$$D_n = (n-1)(D_{n-2} + D_{n-1}) \qquad \blacksquare$$

---

## Problem 79 — 8 men, hats returned so no man gets his own hat

> **Rule:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|Derangements: $D_8$]].

$$D_8 = 8!\left(1-1+\frac{1}{2!}-\frac{1}{3!}+\frac{1}{4!}-\frac{1}{5!}+\frac{1}{6!}-\frac{1}{7!}+\frac{1}{8!}\right) = \boxed{14{,}833}$$

---

## Problem 80 — Student eats 3 mangos, 2 papayas, 2 kiwis, one per day; distinct sequences

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Permutations with Repetition|Permutations with repetition]].

Total fruits $= 7$; types: mango(3), papaya(2), kiwi(2).
$$\frac{7!}{3!\,2!\,2!} = \frac{5040}{6\cdot2\cdot2} = \boxed{210}$$

---

## Problem 81 — 4 men each marrying one of 6 women (distinct women, no sharing)

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Injective functions / $k$-permutations]]: $P(6,4)$.

Each man chooses a distinct woman:
$$P(6,4) = 6\times5\times4\times3 = \boxed{360}$$

---

## Problem 82 — 8 identical DVDs into 5 indistinguishable boxes, each $\geq 1$

> **Rule:** Integer partitions of 8 into exactly 5 positive parts.

Partitions of 8 with exactly 5 parts (positive):
$(4,1,1,1,1)$, $(3,2,1,1,1)$, $(2,2,2,1,1)$.

$$\boxed{3}$$

---

## Problem 83 — 10 exam questions, scores sum to 100, each $\geq 5$

> **Rule:** [[1- DM-Basic-Counting-Rules#5.3 k-combinations with Repetition (Stars and Bars)|Stars and Bars with substitution]].

Let $x_i \geq 5$ be the score of question $i$. Substitute $y_i = x_i - 5 \geq 0$: $\sum y_i = 100 - 50 = 50$.
$$C(50+9,\,9) = C(59,9) = \boxed{C(59,9)}$$

---

## Problem 84 — Permutations of $[2n]$ assigning even numbers to odd positions

> **Rule:** [[1- DM-Basic-Counting-Rules#4. Finite Functions|Product Rule for constrained bijections]].

Odd positions: $\{1,3,5,\ldots,2n-1\}$ — there are $n$ of them. Each must receive an even number from $\{2,4,\ldots,2n\}$ ($n$ even numbers). This is a bijection from $n$ odd positions to $n$ even values: $n!$ ways. The remaining $n$ even positions receive the $n$ odd values: $n!$ ways.

$$\boxed{(n!)^2}$$

---

## Problem 85 — Minimum socks to guarantee a matching pair (Pigeonhole)

> **Rule:** [[1- DM-Basic-Counting-Rules#2.1 The Sum Rule|Pigeonhole Principle]]: 3 colors = 3 pigeonholes.

In the worst case you draw one sock of each color (3 socks) without a pair. The 4th sock must match one of the 3 colors.

$$\boxed{4}$$

---

## Problem 86 — 5 points in a unit square: two points within $\frac{\sqrt{2}}{2}$

> **Rule:** Pigeonhole Principle. Divide the unit square into 4 sub-squares of side $\frac{1}{2}$.

Divide the $1\times1$ square into 4 sub-squares each of side $\frac{1}{2}$. By the Pigeonhole Principle, with 5 points and 4 sub-squares, at least one sub-square contains $\geq 2$ points. The maximum distance within a $\frac{1}{2}\times\frac{1}{2}$ square is the diagonal $= \sqrt{(\frac{1}{2})^2+(\frac{1}{2})^2} = \frac{\sqrt{2}}{2}$. $\blacksquare$

---

## Problem 87 — 5 points in equilateral triangle of side 1: two within $\frac{1}{2}$

> **Rule:** Pigeonhole Principle. Divide into 4 smaller equilateral triangles.

Connect midpoints of the equilateral triangle of side 1, creating 4 smaller equilateral triangles each of side $\frac{1}{2}$. With 5 points and 4 triangles, by Pigeonhole at least one triangle contains $\geq 2$ points. The maximum distance inside an equilateral triangle of side $\frac{1}{2}$ is $\frac{1}{2}$. $\blacksquare$

---

## Problem 88 — Among $n+1$ integers $\leq 2n$, one divides another

> **Rule:** Pigeonhole Principle. Every positive integer writes uniquely as $2^k \cdot m$ with $m$ odd.

For each integer $a \leq 2n$, write $a = 2^k \cdot m$ where $m$ is odd. The odd part $m$ satisfies $1 \leq m \leq 2n-1$ (odd), so $m \in \{1,3,5,\ldots,2n-1\}$ — exactly $n$ possible odd values. With $n+1$ integers, by Pigeonhole two share the same odd part: $a = 2^j \cdot m$ and $b = 2^k \cdot m$ with $j < k$ (say). Then $a \mid b$. $\blacksquare$

---

## Problem 89 — 7 integers from $\{1,\ldots,10\}$: two pairs summing to 11

> **Rule:** Pigeonhole Principle. Pairs summing to 11: $\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$.

There are 5 such pairs. With 7 integers selected and 5 pair-groups, by Pigeonhole at least $\lceil 7/5 \rceil = 2$ selected integers share a pair-group. Actually more precisely: with 7 selections from 5 groups, at least 2 groups must contribute both members ($7-5=2$ extra items), giving at least 2 pairs summing to 11. ✓

**With 6 integers:** It is possible to pick one from each of the 5 groups plus one extra — but that extra forces one group to have both members, giving at least 1 pair. The conclusion is NOT guaranteed to give two pairs. For example $\{1,2,3,4,5,6\}$ has only the pair $(5,6)$ summing to 11.

---

## Problem 90 — 7 numbers from $\{2,\ldots,13\}$: two sum to 15

> **Rule:** Pigeonhole Principle. Pairs summing to 15: $\{2,13\},\{3,12\},\{4,11\},\{5,10\},\{6,9\},\{7,8\}$.

There are 6 such pairs, covering all 12 numbers $\{2,\ldots,13\}$. With 7 numbers chosen from 6 pairs, by Pigeonhole at least one pair contributes both members. Those two numbers sum to 15. $\blacksquare$

---

## Problem 91 — 12 chairs, 9 people: 3 consecutive chairs occupied

> **Rule:** Pigeonhole Principle. Divide the 12 chairs into groups of 3 consecutive chairs.

Partition the 12 chairs into 4 groups: $\{1,2,3\},\{4,5,6\},\{7,8,9\},\{10,11,12\}$. With 9 people and 4 groups, by Pigeonhole at least one group contains $\lceil 9/4 \rceil = 3$ people. Since the group consists of 3 consecutive chairs, those 3 people occupy 3 consecutive chairs. $\blacksquare$

---

## Problem 92 — Sequence of $n^2+1$ distinct reals contains monotone subsequence of length $n+1$

> **Rule:** Erdős–Szekeres Theorem, proven via Pigeonhole.

**Proof:** For each element $a_i$ in the sequence, let $d_i$ be the length of the longest increasing subsequence starting at $a_i$. If any $d_i \geq n+1$, we are done. Otherwise all $d_i \in \{1,\ldots,n\}$. With $n^2+1$ elements and $n$ possible values of $d_i$, by Pigeonhole some value $d$ is taken by at least $n+1$ elements: $a_{i_1}, a_{i_2}, \ldots, a_{i_{n+1}}$ with $i_1 < i_2 < \cdots < i_{n+1}$ and all $d_{i_j} = d$. But if $a_{i_j} < a_{i_{j+1}}$, then $d_{i_j} \geq d_{i_{j+1}} + 1 > d_{i_{j+1}}$, contradiction. So $a_{i_1} > a_{i_2} > \cdots > a_{i_{n+1}}$: a strictly decreasing subsequence of length $n+1$. $\blacksquare$

---

---

# Section 2 — Advanced Counting Rules

---

## Adv. Problem 1 — Generating functions for sequences

> **Rule:** [[2- DM-Advanced-Counting#2. Standard Generating Function Correspondences|Standard OGF catalogue]], [[2- DM-Advanced-Counting#3. Operations on Generating Functions|Operations on OGFs]], [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule]].

**(a) $(0,1,2,3,\ldots,n,\ldots)$** — consecutive non-negative integers:

$(0,1,2,3,\ldots) \leftrightarrow \dfrac{x}{(1-x)^2}$ (from differentiation rule: shift of $(1,2,3,\ldots)$).

**(b) Number of $k$-combinations with repetition of $[n]$ (fixed $n$, varying $k$):**

$$C(n+k-1,k) \leftrightarrow \frac{1}{(1-x)^n}$$

**(c) Perfect squares $(1,4,9,16,\ldots)$:**

From the differentiation rule in knowledge file: $\left(\dfrac{x}{(1-x)^2}\right)' = \dfrac{1+x}{(1-x)^3}$ gives $(1,4,9,16,\ldots)$.

$$G(x) = \frac{1+x}{(1-x)^3}$$

**(d) Fibonacci numbers $(0,1,1,2,3,5,\ldots)$:**

$$G(x) = \frac{x}{1-x-x^2}$$

(derived in [[2- DM-Advanced-Counting#5. From Recurrences to Generating Functions|Fibonacci OGF example]]).

**(e) Catalan numbers $(1,1,2,5,14,42,\ldots)$:**

$$G(x) = \frac{1-\sqrt{1-4x}}{2x}$$

**(f) Filling a bag with fruit under constraints** (convolution of individual OGFs):

- Apples (even count): $1 + x^2 + x^4 + \cdots = \dfrac{1}{1-x^2}$
- Bananas (multiple of 5): $1 + x^5 + x^{10} + \cdots = \dfrac{1}{1-x^5}$
- Oranges (at most 4): $1 + x + x^2 + x^3 + x^4 = \dfrac{1-x^5}{1-x}$
- Pears (at most 1): $1 + x$

$$G(x) = \frac{1}{1-x^2} \cdot \frac{1}{1-x^5} \cdot \frac{1-x^5}{1-x} \cdot (1+x) = \frac{1+x}{(1-x^2)(1-x)} = \frac{1}{(1-x)^2}$$

So the OGF simplifies to $\dfrac{1}{(1-x)^2}$, meaning $a_n = n+1$.

---

## Adv. Problem 2 — Express OGFs in terms of $A(x)$

> **Rule:** [[2- DM-Advanced-Counting#3. Operations on Generating Functions|Shift, addition, differentiation, scaling operations on OGFs]].

Let $A(x) = \sum_{n \geq 0} a_n x^n$.

**(a) $(a_0, a_0+a_1, a_1+a_2, \ldots)$:**

The $n$-th term is $a_{n-1}+a_n$ for $n\geq 1$ (and $a_0$ for $n=0$). This equals $\dfrac{A(x)}{1-x}$... actually: $\dfrac{A(x)}{1-x} = A(x)\cdot\sum x^n$, whose $n$-th coefficient is $\sum_{k=0}^n a_k$. That's not quite right.

Coefficient $n$: $a_{n-1}+a_n$ for $n\geq1$, and $a_0$ for $n=0$. This is $A(x) + xA(x) = (1+x)A(x)$? No: $(1+x)A(x)$ has $n$-th coefficient $a_n + a_{n-1}$. ✓

$$\boxed{(1+x)A(x)}$$

**(b) $(a_1, a_2, a_3, \ldots)$** (left shift by 1):

$$\frac{A(x) - a_0}{x}$$

**(c) $(a_0+a_1, a_1+a_2, a_2+a_3, \ldots)$** ($n$-th term = $a_n + a_{n+1}$):

This is $A(x)\cdot(1+x)$... no. $n$-th coefficient of $\dfrac{A(x)-a_0}{x} + A(x) = \dfrac{A(x)(1+x)-a_0}{x}$? Let's verify: $\dfrac{A(x)-a_0}{x}$ has $n$-th coeff $a_{n+1}$. Adding $A(x)$: $n$-th coeff becomes $a_n + a_{n+1}$. ✓

$$\frac{A(x) - a_0}{x} + A(x) = \frac{(1+x)A(x) - a_0}{x}$$

**(d) $(a_0, 2a_1, 4a_2, 8a_3, \ldots)$ = $(a_n \cdot 2^n)$:**

$$A(2x)$$

**(e) $(a_0, a_0+a_1, a_0+a_1+a_2, \ldots)$** (partial sums):

$$\frac{A(x)}{1-x}$$

**(f) $(a_0, a_1 b, a_2 b^2, \ldots)$:**

$$A(bx)$$

**(g) $(a_0, 0, a_2, 0, a_4, \ldots)$** (keep even-indexed, zero odd-indexed):

$$\frac{A(x) + A(-x)}{2}$$

**(h) $(a_0, a_2, a_4, \ldots)$** (extract even-indexed terms into a new sequence):

Sequence with $n$-th term $= a_{2n}$: this is the OGF $\sum_{n\geq0} a_{2n}x^n = \dfrac{A(\sqrt{x})+A(-\sqrt{x})}{2}$ (formal). In standard notation:

$$\frac{A(\sqrt{x})+A(-\sqrt{x})}{2}$$

---

## Adv. Problem 3 — OGF for number of ways to pay $n$ dollars using 3, 5, 7 dollar coins

> **Rule:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule — independent selection]].

$$G(x) = \frac{1}{1-x^3} \cdot \frac{1}{1-x^5} \cdot \frac{1}{1-x^7}$$

---

## Adv. Problem 4 — OGF for distributing $n$ identical candies: 4 children (each odd) + 1 adult (1 or 2)

> **Rule:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule]].

Each child gets an odd number: OGF $= x + x^3 + x^5 + \cdots = \dfrac{x}{1-x^2}$. Four children: $\left(\dfrac{x}{1-x^2}\right)^4$.

Adult gets 1 or 2: OGF $= x + x^2$.

$$G(x) = \frac{x^4}{(1-x^2)^4} \cdot (x + x^2) = \frac{x^5(1+x)}{(1-x^2)^4} = \frac{x^5}{(1-x^2)^3(1-x)}$$

---

## Adv. Problem 5 — OGF for scoring $n$ points (1, 2, or 4 per turn)

> **Rule:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule for constrained counts]].

**(a) At least two turns with 4 points:**

Let $b_k = $ ways to achieve $k$ points on turns scoring 4. Unconstrained: $\dfrac{1}{1-x^4}$. At least 2 turns with 4: remove terms with 0 and 1 occurrences of 4:
$$\frac{1}{1-x^4} - 1 - x^4 = \frac{x^8}{1-x^4}$$

Turns scoring 1 or 2 (unconstrained): $\dfrac{1}{(1-x)(1-x^2)}$.

$$G(x) = \frac{x^8}{(1-x^4)(1-x)(1-x^2)}$$

**(b) Multiple of 3 turns with 2 points:** terms with 0, 3, 6, $\ldots$ twos:
$$1 + x^6 + x^{12} + \cdots = \frac{1}{1-x^6}$$

$$G(x) = \frac{1}{(1-x)(1-x^6)(1-x^4)}$$

---

## Adv. Problem 6 — OGF for $x_1+x_2+x_3+x_4=k$, $x_1\geq3$, $1\leq x_2\leq5$, $0\leq x_3\leq4$, $x_4\geq1$

> **Rule:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule with constrained sums]].

$$G(x) = \frac{x^3}{1-x} \cdot (x+x^2+x^3+x^4+x^5) \cdot (1+x+x^2+x^3+x^4) \cdot \frac{x}{1-x}$$
$$= \frac{x^4}{(1-x)^2} \cdot x\frac{1-x^5}{1-x} \cdot \frac{1-x^5}{1-x}$$
$$= \frac{x^5(1-x^5)^2}{(1-x)^4}$$

**Find $a_7$** (coefficient of $x^7$): Need $k=7$ in $x_1+x_2+x_3+x_4=7$. Set $y_1=x_1-3\geq0$, $y_4=x_4-1\geq0$: $y_1+x_2+x_3+y_4=3$, with $1\leq x_2\leq5$, $0\leq x_3\leq4$.

Setting $z_2=x_2-1\geq0$: $y_1+z_2+x_3+y_4=2$, $z_2\leq4$, $x_3\leq4$. Unconstrained non-negative solutions: $C(5,3)=10$. All solutions have each variable $\leq2\leq4$, so no constraint violation. $a_7 = \boxed{10}$.

---

## Adv. Problem 7 — Fibonacci identities via generating functions

> **Rule:** [[2- DM-Advanced-Counting#5. From Recurrences to Generating Functions|Fibonacci OGF $F(x) = \frac{x}{1-x-x^2}$]].

**(a) $f_0+f_1+\cdots+f_n = f_{n+2}-1$:**

$\dfrac{F(x)}{1-x}$ has $n$-th coefficient $\sum_{k=0}^n f_k$. Now $\dfrac{F(x)}{1-x} = \dfrac{x}{(1-x)(1-x-x^2)}$. One shows by partial fractions or direct Fibonacci argument: $\sum_{k=0}^n f_k = f_{n+2}-1$ (since $f_{n+2}=f_{n+1}+f_n$ and the telescoping sum gives $f_{n+2}-f_2 = f_{n+2}-1$).

**(b) $f_0+f_2+\cdots+f_{2n} = f_{2n+1}-1$:**

Using $f_{k+2} = f_{k+1}+f_k$ and telescoping: $f_{2n+1}-f_1 = f_{2n+1}-1$.

**(c) $f_1+f_3+\cdots+f_{2n-1} = f_{2n}$:**

$\sum_{k=0}^n f_k = f_{n+2}-1$. Sum of all $= (\text{even-indexed sum}) + (\text{odd-indexed sum})$:
$(f_{2n+1}-1) + f_{2n} = f_{2n+2}-1$, and using $f_0=0$: even-indexed sum $= f_{2n+1}-1$; odd-indexed $= (f_{2n+2}-1)-(f_{2n+1}-1) = f_{2n+2}-f_{2n+1} = f_{2n}$. ✓

---

## Adv. Problem 8 — Closed formula for $k$-combinations with repetition via Maclaurin decomposition

> **Rule:** [[2- DM-Advanced-Counting#6. From Generating Functions to Closed Formulas|Partial fractions / Maclaurin expansion of $\frac{1}{(1-x)^n}$]].

The OGF is $\dfrac{1}{(1-x)^n}$. By the generalized binomial theorem / repeated differentiation:

$$\frac{1}{(1-x)^n} = \sum_{k=0}^{\infty} \binom{n+k-1}{k} x^k$$

So the number of $k$-combinations with repetition from $n$ elements is:
$$\boxed{C(n+k-1,k)}$$

---

## Adv. Problem 9 — OGF for $S(n,2)$ and closed formula

> **Rule:** [[2- DM-Advanced-Counting#5. From Recurrences to Generating Functions|Recurrence to OGF method]].

Recurrence: $S(0,2)=S(1,2)=0$, $S(n,2) = 1 + 2S(n-1,2)$ for $n\geq2$.

Let $F(x) = \sum_{n\geq0} S(n,2)x^n$.

Multiply recurrence by $x^n$ and sum for $n\geq2$:
$$F(x) - 0 - 0 = \frac{x^2}{1-x} + 2xF(x)$$
$$F(x)(1-2x) = \frac{x^2}{1-x}$$
$$F(x) = \frac{x^2}{(1-x)(1-2x)}$$

Partial fractions: $\dfrac{x^2}{(1-x)(1-2x)} = \dfrac{A}{1-x} + \dfrac{B}{1-2x}$.

$x^2 = A(1-2x)+B(1-x)$. At $x=1$: $1=-A$, so $A=-1$. At $x=1/2$: $1/4=B/2$, so $B=1/2$... Let me recheck: $x^2 = A(1-2x)+B(1-x)$, expanding: $A+B + (-2A-B)x = 0+0\cdot x + x^2$... this only works if the numerator is degree $\geq$ denominator. Let me do polynomial division first:

$\dfrac{x^2}{(1-x)(1-2x)} = \dfrac{x^2}{1-3x+2x^2}$. Long division: $x^2 \div (1-3x+2x^2)$: quotient $\frac{1}{2}$ times ... better to use the form:

$$\frac{x^2}{(1-x)(1-2x)} = -1 + \frac{1}{1-x} + \frac{-1}{1-2x} + \cdots$$

Actually: $\dfrac{x^2}{(1-x)(1-2x)} = \dfrac{A}{1-x}+\dfrac{B}{1-2x}+\text{polynomial}$.

Since the numerator degree (2) equals denominator degree (2), we first divide: $\dfrac{x^2}{2x^2-3x+1}$. Polynomial part: $\frac{1}{2}$. Remainder: $x^2 - \frac{1}{2}(2x^2-3x+1) = \frac{3}{2}x-\frac{1}{2}$.

So $F(x) = \frac{1}{2} + \dfrac{\frac{3}{2}x-\frac{1}{2}}{(1-x)(1-2x)}$. Now do partial fractions on $\dfrac{\frac{3}{2}x-\frac{1}{2}}{(1-x)(1-2x)}$:

$= \dfrac{A}{1-x}+\dfrac{B}{1-2x}$.

$\tfrac{3}{2}x-\tfrac{1}{2} = A(1-2x)+B(1-x)$.
$x=1$: $1 = -A \Rightarrow A=-1$.
$x=\frac{1}{2}$: $\frac{3}{4}-\frac{1}{2}=\frac{1}{4}=\frac{B}{2} \Rightarrow B=\frac{1}{2}$.

$$F(x) = \frac{1}{2} - \frac{1}{1-x} + \frac{1/2}{1-2x} = \frac{1}{2} - \sum_{n\geq0}x^n + \frac{1}{2}\sum_{n\geq0}2^n x^n$$

Coefficient of $x^n$ for $n\geq1$: $S(n,2) = -1 + \frac{2^n}{2} = 2^{n-1}-1$. ✓

$$\boxed{S(n,2) = 2^{n-1}-1}$$

---

## Adv. Problem 10 — Solve recurrences using generating function / characteristic polynomial methods

> **Rule:** [[2- DM-Advanced-Counting#7. Homogeneous Linear Recurrences|Homogeneous recurrences]], [[2- DM-Advanced-Counting#8. Non-Homogeneous Linear Recurrences|Non-homogeneous recurrences]].

### (a) $a_0=2$, $a_n = 3a_{n-1}$

Characteristic polynomial: $x - 3 = 0$, root $r=3$. General solution: $a_n = c \cdot 3^n$. $a_0=2 \Rightarrow c=2$.
$$\boxed{a_n = 2 \cdot 3^n}$$

### (b) $a_0=2$, $a_n = 3a_{n-1}+1$

Non-homogeneous: RHS $= 1^n \cdot 1$, so $b=1$, $d=0$. Augmented polynomial: $(x-3)(x-1)$. Roots $3,1$.
$a_n = c_1\cdot3^n + c_2\cdot1^n$. From $a_0=2$: $c_1+c_2=2$. From $a_1=3\cdot2+1=7$: $3c_1+c_2=7$. Solving: $c_1=\frac{5}{2}$, $c_2=-\frac{1}{2}$.
$$\boxed{a_n = \frac{5\cdot3^n - 1}{2}}$$

### (c) $a_0=1$, $a_1=2$, $a_n=5a_{n-1}-4a_{n-2}$

Characteristic polynomial: $x^2-5x+4=(x-1)(x-4)$. Roots $1,4$.
$a_n=c_1\cdot1^n+c_2\cdot4^n$. $a_0=1$: $c_1+c_2=1$. $a_1=2$: $c_1+4c_2=2$. Solving: $c_2=\frac{1}{3}$, $c_1=\frac{2}{3}$.
$$\boxed{a_n = \frac{2}{3} + \frac{4^n}{3} = \frac{2+4^n}{3}}$$

### (d) $u_0=2$, $u_1=-6$, $u_{n+2}+8u_{n+1}-9u_n = 8\cdot3^{n+1}$

Rewrite as $u_n+8u_{n-1}-9u_{n-2}=8\cdot3^{n-1}$ for $n\geq2$. Homogeneous part: $x^2+8x-9=(x+9)(x-1)$. Non-homogeneous RHS: $b=3$, $d=0$. Augmented: $(x+9)(x-1)(x-3)$. Roots: $-9, 1, 3$.
$u_n=c_1(-9)^n+c_2\cdot1^n+c_3\cdot3^n$.
$u_0=2$: $c_1+c_2+c_3=2$.
$u_1=-6$: $-9c_1+c_2+3c_3=-6$.
$u_2=$ from recurrence: $u_2=-8u_1+9u_0+8\cdot3 = 48+18+24=90$. Wait, recurrence is $u_{n+2}=-8u_{n+1}+9u_n+8\cdot3^{n+1}$: $u_2=-8(-6)+9(2)+8\cdot3=48+18+24=90$.
$81c_1+c_2+9c_3=90$.

From first two: $-10c_1+2c_3=-8\Rightarrow c_3=5c_1-4$.
From first and third: $80c_1+8c_3=88\Rightarrow 10c_1+c_3=11$. Substituting: $10c_1+5c_1-4=11\Rightarrow c_1=1$.
$c_3=1$, $c_2=0$.
$$\boxed{u_n = (-9)^n + 3^n}$$

### (e) $u_0=1$, $u_{n+1}-2u_n=4^n$

Non-homogeneous: $b=4$, $d=0$. Homogeneous part: $x-2$. Augmented: $(x-2)(x-4)$.
$u_n=c_1\cdot2^n+c_2\cdot4^n$.
$u_0=1$: $c_1+c_2=1$.
$u_1=2\cdot1+1=3$: $2c_1+4c_2=3$. Solving: $c_2=\frac{1}{2}$, $c_1=\frac{1}{2}$.
$$\boxed{u_n = \frac{2^n+4^n}{2}}$$

### (f) Words of length $n$ in $\{a,b,c,d\}$ with odd number of b's: $q_{n+1}=4^n+2q_n$; solve

Show $q_{n+1}=4^n+2q_n$: Words of length $n+1$ with an odd number of b's. Either add a non-b character ($3$ choices) to a word of length $n$ with odd b's ($3q_n$ ways), or add a b to a word with even b's. Words of length $n$ with even b's $= 4^n - q_n$. So $q_{n+1} = 3q_n + (4^n-q_n) = 4^n + 2q_n$. ✓ (Note: the problem states $4^n$ not $3q_n+(4^n-q_n)$, consistent.)

Initial value $q_0=0$ (empty word has 0 b's, which is even, not odd) or $q_1=1$ (only "b").

Using $q_0=0$: This is non-homogeneous $q_{n+1}-2q_n=4^n$, same form as (e) but shifted. Augmented polynomial: $(x-2)(x-4)$. $q_n=c_1\cdot2^n+c_2\cdot4^n$. $q_0=0$: $c_1+c_2=0$. $q_1=1$: $2c_1+4c_2=1$. Solving: $c_2=\frac{1}{2}$, $c_1=-\frac{1}{2}$.

$$\boxed{q_n = \frac{4^n - 2^n}{2} = \frac{4^n-2^n}{2}}$$

---

## Adv. Problem 11 — Closed formulas from generating functions

> **Rule:** [[2- DM-Advanced-Counting#6. From Generating Functions to Closed Formulas|Expand / partial fractions / coefficient extraction]].

### (a) $(3x-4)^3$

Expand: $(3x-4)^3 = \sum_{k=0}^3\binom{3}{k}(3x)^k(-4)^{3-k}$.
$= -64 + 144x - 108x^2 + 27x^3$.
Sequence: $(-64, 144, -108, 27, 0, 0, \ldots)$.

### (b) $\dfrac{x^3}{1-3x}$

$= x^3 \cdot \dfrac{1}{1-3x} = x^3\sum_{n\geq0}3^n x^n$. Coefficient of $x^n$: $a_n = 3^{n-3}$ for $n\geq3$, else $0$.
$$a_n = \begin{cases}3^{n-3} & n\geq3 \\ 0 & n<3\end{cases}$$

### (c) $\dfrac{x^3+x}{1-3x}$

$= \dfrac{x^3}{1-3x}+\dfrac{x}{1-3x}$. From (b): first part gives $3^{n-3}$ for $n\geq3$. Second: $x\cdot\frac{1}{1-3x}$ gives $3^{n-1}$ for $n\geq1$, 0 for $n=0$. So:
$$a_n = \begin{cases}0 & n=0 \\ 3^{n-1} & 1\leq n\leq2 \\ 3^{n-1}+3^{n-3} & n\geq3\end{cases} = \begin{cases}0&n=0\\ 3^{n-1}(1+3^{-2}) = \frac{10\cdot3^{n-1}}{9} & n\geq3\end{cases}$$

For $n\geq3$: $a_n = 3^{n-1}+3^{n-3} = 3^{n-3}(9+1) = 10\cdot3^{n-3}$.

### (d) $\dfrac{x^2}{(1-x)^2}$

$= x^2\cdot\dfrac{1}{(1-x)^2} = x^2\sum_{n\geq0}(n+1)x^n$. Coefficient of $x^n$: $a_n = n-1$ for $n\geq2$ (i.e., $n-1$ shifted), else 0. Precisely: $(n-1)$ for $n \geq 1$ via shift: $a_n = n-1$ for $n\geq1$.

Actually: coefficient of $x^n$ is the coefficient of $x^{n-2}$ in $\frac{1}{(1-x)^2}$, which is $n-2+1=n-1$ for $n\geq2$.
$$a_n = \begin{cases}0&n<2\\ n-1&n\geq2\end{cases}$$

### (e) $\dfrac{x^2-x}{(1-x)^2} = \dfrac{x(x-1)}{(1-x)^2} = \dfrac{-x(1-x)}{(1-x)^2} = \dfrac{-x}{1-x}$

$= -x\sum_{n\geq0}x^n = -\sum_{n\geq1}x^n$. So $a_0=0$, $a_n=-1$ for $n\geq1$.

### (f) $\dfrac{x^2}{(1-x)^3}$

$= x^2 \cdot \dfrac{1}{(1-x)^3}$. Coefficient of $x^n$ in $\dfrac{1}{(1-x)^3}$ is $\binom{n+2}{2}$. Shift by 2:
$$a_n = \binom{n}{2} = \frac{n(n-1)}{2} \quad \text{for } n\geq2, \quad \text{else } 0.$$

---

## Adv. Problem 12 — 10 identical balloons to 4 children, each gets $\geq 2$

> **Rule:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule]] + coefficient extraction.

OGF for each child (at least 2): $x^2+x^3+\cdots = \dfrac{x^2}{1-x}$. Four children:

$$G(x) = \frac{x^8}{(1-x)^4}$$

We need coefficient of $x^{10}$, i.e., coefficient of $x^2$ in $\dfrac{1}{(1-x)^4}$:

$$[x^2]\frac{1}{(1-x)^4} = \binom{2+3}{3} = \binom{5}{3} = \boxed{10}$$

---

## Adv. Problem 13 — 15 identical objects into 6 distinct boxes, $1\leq$ each $\leq3$

> **Rule:** [[2- DM-Advanced-Counting#4. Combinatorial Applications of the Convolution Rule|Convolution rule]] + coefficient extraction.

OGF for each box: $x+x^2+x^3 = x\dfrac{1-x^3}{1-x}$. Six boxes:

$$G(x) = \frac{x^6(1-x^3)^6}{(1-x)^6}$$

We need coefficient of $x^{15}$, i.e., coefficient of $x^9$ in $\dfrac{(1-x^3)^6}{(1-x)^6}$.

$(1-x^3)^6 = \sum_{k=0}^6\binom{6}{k}(-1)^k x^{3k}$.

Coefficient of $x^9$ in $\dfrac{(1-x^3)^6}{(1-x)^6}$:
$$\sum_{k=0}^{3}(-1)^k\binom{6}{k}\binom{9-3k+5}{5}$$
$$= \binom{6}{0}\binom{14}{5} - \binom{6}{1}\binom{11}{5} + \binom{6}{2}\binom{8}{5} - \binom{6}{3}\binom{5}{5}$$
$$= 2002 - 6\cdot462 + 15\cdot56 - 20\cdot1 = 2002 - 2772 + 840 - 20 = \boxed{50}$$

---

## Adv. Problem 14 — Words from MISSISSIPPI letters with forbidden patterns

> **Rule:** [[2- DM-Advanced-Counting#15. Applications of PIE|PIE (complement counting)]]. MISSISSIPPI: M(1),I(4),S(4),P(2). Total = 11 letters. Total arrangements: $\dfrac{11!}{4!\,4!\,2!} = 34650$.

**(a) Does not contain four S's consecutively:**

Treat SSSS as one block. Remaining: M(1),I(4),P(2),SSSS(1) — 8 items total. Arrangements: $\dfrac{8!}{4!\,2!} = \dfrac{40320}{48} = 840$.

$$34650 - 840 = \boxed{33810}$$

**(b) Neither four consecutive S's nor two consecutive P's:**

By PIE: $|\text{neither}| = |\text{total}| - |A| - |B| + |A\cap B|$.

$|A|$ (four consecutive S's) $= 840$ (from above).

$|B|$ (two consecutive P's): treat PP as block. Items: M(1),I(4),S(4),PP(1) — 10 items. $\dfrac{10!}{4!\,4!} = \dfrac{3628800}{576} = 6300$.

$|A\cap B|$: treat SSSS and PP each as blocks. Items: M(1),I(4),SSSS(1),PP(1) — 7 items. $\dfrac{7!}{4!} = \dfrac{5040}{24} = 210$.

$$34650 - 840 - 6300 + 210 = \boxed{27720}$$

---

## Adv. Problem 15 — Positive integers $\leq 100$ not divisible by 5 or 7

> **Rule:** [[2- DM-Advanced-Counting#15. Applications of PIE|PIE complement counting]].

$|A_5|=\lfloor100/5\rfloor=20$, $|A_7|=\lfloor100/7\rfloor=14$, $|A_{35}|=\lfloor100/35\rfloor=2$.

$$|A_5\cup A_7| = 20+14-2=32$$
$$100-32=\boxed{68}$$

---

## Adv. Problem 16 — Positive integers $\leq 100$ that are odd or perfect squares

> **Rule:** [[2- DM-Advanced-Counting#13. Two-Set and Three-Set PIE|PIE for two sets]].

Odd numbers $\leq100$: 50. Perfect squares $\leq100$: 10 ($1^2,\ldots,10^2$). Odd perfect squares $\leq100$: $1,9,25,49,81$ — 5.

$$50+10-5=\boxed{55}$$

---

## Adv. Problem 17 — Positive integers $\leq 1000$ that are perfect squares or cubes

> **Rule:** [[2- DM-Advanced-Counting#13. Two-Set and Three-Set PIE|PIE for two sets]].

Squares $\leq1000$: $\lfloor\sqrt{1000}\rfloor=31$. Cubes $\leq1000$: $\lfloor1000^{1/3}\rfloor=10$. Sixth powers (both): $\lfloor1000^{1/6}\rfloor=3$ ($1,64,729$).

$$31+10-3=\boxed{38}$$

---

## Adv. Problem 18 — Union of 4 sets

> **Rule:** [[2- DM-Advanced-Counting#14. General PIE|General PIE]].

$$|A_1\cup A_2\cup A_3\cup A_4| = 4(100) - \binom{4}{2}(50) + \binom{4}{3}(25) - \binom{4}{4}(5)$$
$$= 400 - 6(50) + 4(25) - 5 = 400 - 300 + 100 - 5 = \boxed{195}$$

---

## Adv. Problem 19 — Survey: students who like none of three vegetables

> **Rule:** [[2- DM-Advanced-Counting#13. Two-Set and Three-Set PIE|PIE for three sets]].

$|B|=64$, $|Br|=94$, $|C|=58$, $|B\cap Br|=26$, $|B\cap C|=28$, $|Br\cap C|=22$, $|B\cap Br\cap C|=14$.

$$|B\cup Br\cup C| = 64+94+58-26-28-22+14 = 154$$
$$270 - 154 = \boxed{116}$$

---

## Adv. Problem 20 — Number of terms in PIE formula for 5 sets

> **Rule:** [[2- DM-Advanced-Counting#14. General PIE|General PIE]]: $2^n - 1$ terms for $n$ sets.

For 5 sets: $\binom{5}{1}+\binom{5}{2}+\binom{5}{3}+\binom{5}{4}+\binom{5}{5} = 5+10+10+5+1 = \boxed{31}$ terms.

---

## Adv. Problem 21 — Permutations of 26 letters containing none of FISH, RAT, BIRD

> **Rule:** [[2- DM-Advanced-Counting#14. General PIE|PIE with string-avoidance]].

Let $A$ = permutations containing FISH (4 letters → treat as 1 block: $23!$ arrangements).
$B$ = containing RAT (3 letters → $24!$).
$C$ = containing BIRD (4 letters → $23!$).

$|A\cap B|$: FISH and RAT share no letters; treat both as blocks: $22!$.
$|A\cap C|$: FISH and BIRD share letters I — they overlap! Any permutation containing both FISH and BIRD must contain I in two places, impossible in a permutation. $|A\cap C|=0$.
$|B\cap C|$: RAT and BIRD share no letters: treat as blocks: $22!$.
$|A\cap B\cap C|=0$ (since $A\cap C=\emptyset$).

$$|A\cup B\cup C| = 23!+24!+23!-22!-0-22!+0 = 2(23!)+24!-2(22!)$$
$$= 22!(2\cdot23+24\cdot23-2) = 22!(46+552-2) = 596\cdot22!$$

$$26! - 596\cdot22!$$

---

## Adv. Problem 22 — Non-negative solutions of $x+y+z=13$, $0\leq x,y,z\leq6$

> **Rule:** [[2- DM-Advanced-Counting#📘 Examples & Applications — PIE|Stars-and-bars + PIE (Example 13 in knowledge file)]].

Unconstrained: $\binom{15}{2}=105$.
Let $A_x$: $x\geq7$, sub $x'=x-7$: $x'+y+z=6$, $\binom{8}{2}=28$. By symmetry $|A_y|=|A_z|=28$.
$A_x\cap A_y$: sum $\geq14>13$: 0.

$$105 - 3\cdot28 = \boxed{21}$$

---

## Adv. Problem 23 — Non-negative solutions of $x+y+z+t=18$, $0\leq x\leq4$, $0\leq y\leq7$

> **Rule:** [[2- DM-Advanced-Counting#14. General PIE|PIE for upper bound constraints]].

Unconstrained: $\binom{21}{3}=1330$.
$|A_x|$ ($x\geq5$, sub $x'=x-5$: sum=13): $\binom{16}{3}=560$.
$|A_y|$ ($y\geq8$, sub: sum=10): $\binom{13}{3}=286$.
$|A_x\cap A_y|$ ($x\geq5,y\geq8$: sum=5): $\binom{8}{3}=56$.

$$1330 - 560 - 286 + 56 = \boxed{540}$$

---

## Adv. Problem 24 — Surjective functions from 7-element set to 5-element set

> **Rule:** [[2- DM-Advanced-Counting#15.2 Number of Onto (Surjective) Functions|Surjection formula via PIE]].

$$\sum_{j=0}^{5}(-1)^j\binom{5}{j}(5-j)^7 = 5^7-5\cdot4^7+10\cdot3^7-10\cdot2^7+5\cdot1^7$$
$$= 78125-81920+21870-1280+5 = \boxed{16800}$$

---

## Adv. Problem 25 — 6 different toys to 3 children, each gets $\geq1$

> **Rule:** [[2- DM-Advanced-Counting#15.2 Number of Onto (Surjective) Functions|Surjections from 6-set to 3-set]].

$$\sum_{j=0}^{3}(-1)^j\binom{3}{j}(3-j)^6 = 3^6-3\cdot2^6+3\cdot1^6 = 729-192+3 = \boxed{540}$$

---

## Adv. Problem 26 — 8 distinct balls into 3 distinct urns, each urn $\geq1$

> **Rule:** [[2- DM-Advanced-Counting#15.2 Number of Onto (Surjective) Functions|Surjections]].

$$3^8-3\cdot2^8+3\cdot1^8 = 6561-768+3 = \boxed{5796}$$

---

## Adv. Problem 27 — Derangements of $[4]$: count and list

> **Rule:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|$D_4=9$, derangement formula]].

$D_4 = 9$. All 9 derangements listed in Problem 76 (Basic section) above:

Cycle type $(4)$: $2341, 2413, 3142, 3412, 4123, 4312$ — one-line notations of the 6 four-cycles.
Cycle type $(2,2)$: $2143, 3412$... Let me list correctly:

$(1\;2)(3\;4)$: $2143$. $(1\;3)(2\;4)$: $3412$. $(1\;4)(2\;3)$: $4321$.
$(1\;2\;3\;4)$: $2341$. $(1\;2\;4\;3)$: $2413$. $(1\;3\;2\;4)$: $3142$.
$(1\;3\;4\;2)$: $3412$... wait:

Let me be careful. $(1\;3\;4\;2)$: $1\to3,3\to4,4\to2,2\to1$. One-line: $3\ 1\ 4\ 2$. $(1\;4\;2\;3)$: $1\to4,4\to2,2\to3,3\to1$: $4\ 3\ 1\ 2$. $(1\;4\;3\;2)$: $1\to4,4\to3,3\to2,2\to1$: $4\ 1\ 2\ 3$.

So the 9 derangements of $[4]$ in one-line notation:
$$2143,\ 3412,\ 4321,\ 2341,\ 2413,\ 3142,\ 3412,\ 4312,\ 4123$$

(Corrected list): $2143, 3412, 4321, 2341, 2413, 3142, 3412, 4312, 4123$ — some duplicates indicate error; let me recount carefully. The 9 derangements are:

$2143$ ($(12)(34)$), $3412$ ($(13)(24)$... wait $(1\;3)(2\;4)$: $\sigma(1)=3,\sigma(3)=1,\sigma(2)=4,\sigma(4)=2$: $3412$ ✓), $4321$ ($(14)(23)$: $\sigma(1)=4,\sigma(4)=1,\sigma(2)=3,\sigma(3)=2$: $4321$ ✓).

Four-cycles: $(1234)$: $2341$; $(1243)$: $2413$; $(1324)$: $3421$; $(1342)$: $3\ 1\ 4\ 2 = 3142$; $(1423)$: $4\ 3\ 1\ 2 = 4312$; $(1432)$: $4\ 1\ 2\ 3$... wait $(1\;4\;3\;2)$: $1\to4,4\to3,3\to2,2\to1$, so one-line: $4123$.

All 9: $\boxed{2143,\ 3412,\ 4321,\ 2341,\ 2413,\ 3421,\ 3142,\ 4312,\ 4123}$

---

## Adv. Problem 28 — 8 students, same classroom two classes: no student same seat both

> **Rule:** [[2- DM-Advanced-Counting#11. Fixed Points and Derangements|Derangements: $D_8$]].

The second seating is a derangement of the first:
$$D_8 = \boxed{14833}$$

---

## Adv. Problem 29 — Non-negative integers $\leq 100$ relatively prime to 100

> **Rule:** [[2- DM-Advanced-Counting#15.1 Euler's Phi Function|Euler's phi function]].

$100 = 2^2 \cdot 5^2$.

$$\varphi(100) = 100\left(1-\frac{1}{2}\right)\left(1-\frac{1}{5}\right) = 100 \cdot \frac{1}{2} \cdot \frac{4}{5} = \boxed{40}$$
