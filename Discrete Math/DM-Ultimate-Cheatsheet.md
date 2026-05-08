# 📐 Discrete Mathematics — Ultimate Cheatsheet
> **Philosophy:** Read top to bottom. Every problem in your exercise set is solved by one of the patterns below. When stuck, find the matching row in the decision tables — the formula follows automatically.
---

## 🗺️ Master Navigation

```
Got a problem → Which TYPE of problem is it?
│
├── Counting arrangements/selections ──────────────→ §1 Basic Counting
├── Distributing objects into boxes ───────────────→ §2 Distributions
├── Integer equation x₁+x₂+…+xₙ = k ─────────────→ §3 Stars & Bars
├── Strings / bit strings / multisets ─────────────→ §4 Strings & Multisets
├── Binomial / multinomial coefficients ───────────→ §5 Binomial Theorem
├── Prove "at least two share property X" ─────────→ §6 Pigeonhole
├── No fixed points / hat problems ────────────────→ §7 Derangements
├── Partitions of a set [n] into k parts ──────────→ §8 Stirling & Bell
├── Permutation cycles / inverses ──────────────────→ §9 Permutation Algebra
├── Sequence defined by recurrence ────────────────→ §10 Recurrences
└── Count sequences under constraints ─────────────→ §11 Generating Functions
```

---

## §1 — Basic Counting

> [!tip] 🔑 Two questions to ask first
> 1. Does **order matter**?
> 2. Is **repetition allowed**?

### 1.1 The Four Regimes

| Order matters? | Repetition? | Formula | Name | Example |
|---|---|---|---|---|
| ✅ Yes | ✅ Yes | $n^k$ | Functions $[k]\to[n]$ | Passwords, strings |
| ✅ Yes | ❌ No | $\dfrac{n!}{(n-k)!} = P(n,k)$ | Permutations | Ranked selection |
| ❌ No | ❌ No | $\dbinom{n}{k} = \dfrac{n!}{k!(n-k)!}$ | Combinations | Committee |
| ❌ No | ✅ Yes | $\dbinom{n+k-1}{k}$ | Stars & Bars | Identical objects |

### 1.2 Product Rule & Sum Rule

> [!note] 📌 Product Rule
> If task A can be done in $a$ ways **AND then** task B in $b$ ways → total = $a \times b$

> [!note] 📌 Sum Rule
> If event A can happen in $a$ ways **OR** event B in $b$ ways (mutually exclusive) → total = $a + b$

> [!warning] Inclusion-Exclusion (two sets)
> $$|A \cup B| = |A| + |B| - |A \cap B|$$
> For three sets: $|A\cup B\cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|$

### 1.3 Subsets

$$\text{Subsets of } [n] = 2^n \quad \text{(each element: in or out)}$$

| "How many subsets with…" | Formula |
|---|---|
| Exactly $k$ elements | $\binom{n}{k}$ |
| At most 2 elements | $1 + n + \binom{n}{2}$ |
| More than 2 elements | $2^n - 1 - n - \binom{n}{2}$ |

### 1.4 Functions

| Type                                        | Formula                                                                    | Condition         |
| ------------------------------------------- | -------------------------------------------------------------------------- | ----------------- |
| All functions $[m]\to[n]$                   | $n^m$                                                                      | any               |
| Injections (one-to-one) $[m]\to[n]$         | $P(n,m) = \frac{n!}{(n-m)!}$                                               | need $m \leq n$   |
| Bijections $[n]\to[n]$                      | $n!$                                                                       | $m = n$ only      |
| Surjections (onto)<br>$[m] \rightarrow [n]$ | $\sum_{i=0}^{n} (-1)^i \binom{n}{i} (n-i)^m$<br>_or_<br>$n! \cdot S(m, n)$ | need<br>$m \ge n$ |
> [!example] Exercises 13–19
> - Functions $[3]\to[2]$: $2^3 = 8$
> - Injections $[2]\to[3]$: $P(3,2) = 6$
> - Bijections $[3]\to[3]$: $3! = 6$
> - Injections $[m]\to[n]$ (general): $P(n,m) = n!/(n-m)!$

---

## §2 — Distributions (The Big Table)

> [!tip] 🔑 Ask two questions
> 1. Are the **objects** distinct or identical?
> 2. Are the **boxes** distinct or identical?

### 2.1 The Master Distribution Table

| Objects   | Boxes     | Restriction                 | Formula                                    | Notes                                               |
| --------- | --------- | --------------------------- | ------------------------------------------ | --------------------------------------------------- |
| Distinct  | Distinct  | None                        | $n^k$                                      | $k$ objects, $n$ boxes                              |
| Distinct  | Distinct  | $\leq 1$ per box            | $P(n,k) = \frac{n!}{(n-k)!}$               | injections                                          |
| Distinct  | Distinct  | $\geq 1$ per box            | $n!\cdot S(k,n)$                           | surjections                                         |
| Identical | Distinct  | None                        | $\binom{n+k-1}{k}$                         | stars & bars                                        |
| Identical | Distinct  | $\geq 1$ per box            | $\binom{k-1}{n-1}$                         | substitute $y_i = x_i - 1$                          |
| Identical | Distinct  | $\geq a$ per box            | $\binom{k - na + n - 1}{n-1}$              | substitute $y_i = x_i - a$                          |
| Distinct  | Identical | None                        | $\sum_{j=1}^{n} S(k,j)$                    | sum of Stirlings                                    |
| Distinct  | Identical | $\geq 1$ per box            | $S(k,n)$                                   | Stirling 2nd kind                                   |
| Identical | Identical | None                        | $p(k,n)$                                   | integer partitions                                  |
| Identical | Identical | $\geq 1$ per box            | $p(k-n, n)$                                | shift by $n$                                        |
| Distinct  | Distinct  | Exact amounts $k_i$ per box | $$\frac{k!}{k_1! \cdot k_2! \cdots k_n!}$$ | Permutations with repetition (where $\sum k_i = k$) |
> [!warning] ⚠️ Most common mistake
> **Identical → Identical** uses *integer partitions*, not stars & bars. Stars & bars only applies when boxes are **distinct**.

### 2.2 Worked Distribution Examples

> [!example] Q66–Q69: Gifts into boxes
> - **15 distinct → 10 distinct, no restriction**: $10^{15}$
> - **15 distinct → 10 distinct, ≥1 each**: $10!\cdot S(15,10)$
> - **15 distinct → 10 distinct, ≤1 each**: $P(10,15) = 0$ (impossible, $k > n$)
> - **10 distinct → 15 distinct, ≤1 each**: $P(15,10) = \frac{15!}{5!}$

> [!example] Q62–Q65: Gifts into identical boxes
> - **4 distinct → 3 identical, no restriction**: $S(4,1)+S(4,2)+S(4,3) = 1+7+6 = 14$
> - **4 distinct → 3 identical, ≥1 each**: $S(4,3) = 6$
> - **4 identical → 3 identical, no restriction**: $p(4,3)$ = partitions of 4 into ≤3 parts: $\{4\},\{3,1\},\{2,2\},\{2,1,1\} = 4$
> - **4 identical → 3 identical, ≥1 each**: partitions of 4 into exactly 3 positive parts: $\{2,1,1\} = 1$

> [!example] Q82: 8 identical DVDs into 5 indistinguishable boxes, ≥1 each
> Partitions of 8 into exactly 5 positive parts:
> $\{4,1,1,1,1\}, \{3,2,1,1,1\}, \{2,2,2,1,1\}, \{2,2,2,2,0\}$... wait, need ≥1 so no zeros.
> Valid: $\{4,1,1,1,1\},\{3,2,1,1,1\},\{2,2,2,1,1\}$ → **5 partitions**

> [!example] Q81: 4 men, 6 women — each man marries one woman
> Injections $[4]\to[6]$: $P(6,4) = 6\cdot5\cdot4\cdot3 = 360$

---

## §3 — Stars & Bars (Integer Equations)

> [!tip] 🔑 Core formula
> Non-negative integer solutions to $x_1 + x_2 + \cdots + x_n = k$:
> $$\binom{n+k-1}{k} = \binom{n+k-1}{n-1}$$

### 3.1 Handling Constraints — The Substitution Method

| Constraint | Substitution | New equation | Formula |
|---|---|---|---|
| $x_i \geq 0$ | — | unchanged | $\binom{n+k-1}{k}$ |
| $x_i \geq 1$ (all) | $y_i = x_i - 1$ | sum becomes $k-n$ | $\binom{n+(k-n)-1}{k-n} = \binom{k-1}{n-1}$ |
| $x_i \geq a$ (all) | $y_i = x_i - a$ | sum becomes $k-na$ | $\binom{n+(k-na)-1}{k-na}$ |
| $x_1 \leq b$ | Inclusion-exclusion or GF | — | Total $-$ (solutions with $x_1 \geq b+1$) |
| Inequality $\sum x_i \leq k$ | Add slack $s \geq 0$ | $\sum x_i + s = k$ | $\binom{n+k}{k}$ (now $n+1$ variables) |

> [!example] Q54: $x_1+x_2+x_3+x_4+x_5 = 21$, $x_i \geq 0$
> **(a) $x_i \geq 1$:** sub $y_i = x_i - 1$, new sum = $21-5=16$ → $\binom{16+4}{4} = \binom{20}{4}$
> **(b) $x_i \geq 2$:** sub $y_i = x_i - 2$, new sum = $21-10=11$ → $\binom{11+4}{4} = \binom{15}{4}$
> **(c) $0 \leq x_1 \leq 10$:** Total (no restriction) $-$ (solutions with $x_1 \geq 11$)
> $= \binom{25}{4} - \binom{14}{4}$

> [!example] Q55: $x_1+x_2+x_3 \leq 11$, $x_i \geq 0$
> Add slack $s \geq 0$: $x_1+x_2+x_3+s = 11$, now 4 variables →
> $$\binom{11+4-1}{11} = \binom{14}{3} = 364$$

> [!example] Q83: 10 questions, sum = 100, each $\geq 5$
> Sub $y_i = x_i - 5$: new sum = $100 - 50 = 50$, still 10 variables →
> $$\binom{50+10-1}{10-1} = \binom{59}{9}$$

> [!example] Q70–Q71
> - Q70: **100 identical → 3 distinct**: $\binom{100+3-1}{3-1} = \binom{102}{2}$
> - Q71: **100 identical → 10 distinct, $\geq 5$ each**: sub $y_i = x_i-5$, sum = 50 → $\binom{59}{9}$

---

## §4 — Strings, Bit Strings & Multisets

### 4.1 Bit Strings

> [!note] Bit string of length $n$ with exactly $k$ zeros: $\binom{n}{k}$

| Question | Formula |
|---|---|
| Exactly $k$ zeros | $\binom{n}{k}$ |
| At most $k$ zeros | $\sum_{i=0}^{k} \binom{n}{i}$ |
| At least $k$ zeros | $2^n - \sum_{i=0}^{k-1}\binom{n}{i}$ |
| No restrictions | $2^n$ |

> [!example] Q6: Bit strings of length 5
> **(a) exactly 2 zeros:** $\binom{5}{2} = 10$
> **(b) at most 2 zeros:** $\binom{5}{0}+\binom{5}{1}+\binom{5}{2} = 1+5+10 = 16$
> **(c) at least 2 zeros:** $2^5 - \binom{5}{0} - \binom{5}{1} = 32-1-5 = 26$

> [!example] Q35: Bit strings length 7 starting with `0` OR ending with `10`
> Use inclusion-exclusion:
> - $|A|$ = start with 0: $2^6 = 64$
> - $|B|$ = end with 10: $2^5 = 32$
> - $|A \cap B|$ = start with 0 AND end with 10: $2^4 = 16$
> $$|A \cup B| = 64 + 32 - 16 = \boxed{80}$$

### 4.2 General Strings

> [!example] Q5: ASCII strings of length 5 with at least one `@`
> **Complement:** Total $-$ (no `@`) $= 128^5 - 127^5$

### 4.3 Strings with Repeated Letters (Multinomial)

$$\text{Arrangements of } n \text{ objects with } r_1 \text{ of type 1, } r_2 \text{ of type 2, ...}: \quad \frac{n!}{r_1!\, r_2!\, \cdots\, r_m!}$$

> [!example] Arranging CASABLANCA (10 letters: C×3, A×4, S×1, B×1, L×1, N×1)
> $$\frac{10!}{3!\cdot 4!\cdot 1!\cdot 1!\cdot 1!\cdot 1!} = \frac{3628800}{6\cdot 24} = 25200$$

> [!example] Arranging SUCCESS (7 letters: S×3, C×2, U×1, E×1)
> $$\frac{7!}{3!\cdot 2!\cdot 1!\cdot 1!} = \frac{5040}{12} = 420$$

> [!example] Q80: 3 mangos, 2 papayas, 2 kiwis — order of eating
> $$\frac{7!}{3!\cdot 2!\cdot 2!} = \frac{5040}{24} = 210$$

### 4.4 Painting / Labelling (Multinomial)

> [!example] Q40: 10 distinct chairs, paint 3 green, 3 blue, 4 red
> $$\frac{10!}{3!\cdot 3!\cdot 4!} = \binom{10}{3}\binom{7}{3}\binom{4}{4} = 4200$$

---

## §5 — Binomial & Multinomial Theorem

### 5.1 Binomial Theorem

$$\boxed{(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k\, y^{n-k}}$$

**To find coefficient of $x^a y^b$ in $(cx + dy)^n$:** need $a+b=n$, then
$$\binom{n}{a}\cdot c^a \cdot d^b$$

> [!warning] Don't forget the scalars and signs!
> $(2x - 3y)^{200}$: coefficient of $x^{101}y^{99}$ is $\binom{200}{101}\cdot 2^{101}\cdot(-3)^{99}$
> Since 99 is **odd**, $(-3)^{99}$ is **negative** → final coefficient is **negative**.

### 5.2 Multinomial Theorem

$$(x_1 + x_2 + \cdots + x_m)^n = \sum_{k_1+k_2+\cdots+k_m=n} \frac{n!}{k_1!\,k_2!\cdots k_m!}\, x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m}$$

**To find coefficient of $x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m}$ in $(c_1x_1+c_2x_2+\cdots)^n$:**
1. Verify $\sum k_i = n$ (else coefficient is 0)
2. Answer: $\dfrac{n!}{k_1!\cdots k_m!}\cdot c_1^{k_1}\cdots c_m^{k_m}$

> [!example] Q39: Coefficient of $x^{101}y^{99}z^{105}$ in $(2x-3y-z)^{305}$
> Check: $101+99+105 = 305$ ✅
> $$\frac{305!}{101!\cdot 99!\cdot 105!}\cdot 2^{101}\cdot(-3)^{99}\cdot(-1)^{105}$$

> [!example] Q45: Coefficient of $x^3y^2z^5$ in $(2x-3y-2z)^{10}$
> Check: $3+2+5=10$ ✅
> $$\frac{10!}{3!\cdot 2!\cdot 5!}\cdot 2^3\cdot(-3)^2\cdot(-2)^5 = 2520 \cdot 8 \cdot 9 \cdot (-32) = -5806080$$

### 5.3 Key Binomial Identities

| Identity | How to prove it |
|---|---|
| $\binom{n}{k} = \binom{n}{n-k}$ | Bijection: map $S\mapsto [n]\setminus S$ |
| $\binom{2n}{2} = 2\binom{n}{2} + n^2$ | Count pairs from two groups of size $n$ |
| $\sum_{k=0}^{n} k\binom{n}{k} = n\cdot 2^{n-1}$ | Differentiate $(1+x)^n$ at $x=1$ |
| Pascal: $\binom{n}{k} = \binom{n-1}{k}+\binom{n-1}{k-1}$ | Element $n$: either in or out |
| Vandermonde: $\binom{m+n}{r} = \sum_{i=0}^{r}\binom{m}{i}\binom{n}{r-i}$ | Count $r$-subsets of $m+n$ elements |
| $\binom{n}{k}\binom{k}{j} = \binom{n}{j}\binom{n-j}{k-j}$ | Both sides $= \frac{n!}{j!(k-j)!(n-k)!}$ |
| $\binom{n}{k} = \binom{n-2}{k-2}+\binom{n-2}{k-1}+\binom{n-2}{k}$ | **TRUE** — apply Pascal twice |

> [!example] Q38: Coefficient of $x^k$ in $\left(x + \frac{1}{x}\right)^{100}$
> General term: $\binom{100}{j}\cdot x^j \cdot x^{-(100-j)} = \binom{100}{j}\cdot x^{2j-100}$
> Set $2j-100=k$ → $j = \frac{k+100}{2}$. Need $j$ to be integer $\Rightarrow k$ must be **even** with $-100 \leq k \leq 100$.
> $$\text{Coefficient of }x^k = \binom{100}{\frac{k+100}{2}}\quad (k \text{ even})$$

### 5.4 Pascal's Triangle — Next Rows

Row 10: `1 10 45 120 210 252 210 120 45 10 1`
Row 11: `1 11 55 165 330 462 462 330 165 55 11 1`
Row 12: `1 12 66 220 495 792 924 792 495 220 66 12 1`

---

## §6 — Pigeonhole Principle

> [!tip] 🔑 Core statements
> **Basic:** $n+1$ items into $n$ boxes → at least one box has $\geq 2$ items.
> **Generalized:** $kn+1$ items into $n$ boxes → at least one box has $\geq k+1$ items.

### 6.1 Proof Template

```
1. Define the "pigeons" (the objects being counted)
2. Define the "holes" (the categories/boxes)
3. Show |pigeons| > |holes|  (or > k×|holes|)
4. Conclude by PHP that some hole has ≥ 2 (or ≥ k+1) pigeons
```

### 6.2 Standard Tricks

| Problem type | Holes to define |
|---|---|
| Sum = $c$ from a set | Pair up elements that sum to $c$ |
| Divisibility | Residue classes mod $m$ |
| Geometric (side 1 square) | Divide into $n$ sub-regions |
| Sequence has monotone subsequence | Use $(a_i, b_i)$ where $a_i$ = length of longest increasing ending at $i$ |

> [!example] Q85: 60 socks (10 red pairs, 10 blue, 10 green), minimum to guarantee a matching pair?
> Worst case: draw 1 red + 1 blue + 1 green = 3 socks, still no pair. The 4th sock must match one. **Answer: 4**

> [!example] Q86: 5 points in unit square → two points $\leq \frac{\sqrt{2}}{2}$ apart
> Divide square into 4 sub-squares of side $\frac{1}{2}$. By PHP, two of 5 points share a sub-square. Max distance in a $\frac{1}{2}\times\frac{1}{2}$ square = diagonal = $\frac{\sqrt{2}}{2}$.

> [!example] Q87: 5 points in equilateral triangle side 1 → two points $\leq \frac{1}{2}$ apart
> Divide triangle into 4 smaller equilateral triangles of side $\frac{1}{2}$. By PHP, two of 5 points share one. Max distance = $\frac{1}{2}$.

> [!example] Q88: $n+1$ positive integers $\leq 2n$ → one divides another
> Write each integer as $2^a \cdot m$ where $m$ is odd. The odd parts $m \in \{1,3,5,...,2n-1\}$: only $n$ choices. With $n+1$ integers, two share the same odd part $m$: $2^a m \mid 2^b m$ (assume $a < b$).

> [!example] Q89: 7 integers from $\{1,...,10\}$ → at least 2 pairs summing to 11
> Pairs summing to 11: $\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$ — 5 pairs. With 7 integers, by PHP at least $\lceil 7/5 \rceil - 1 = 2$ pairs must be complete. (With 6 integers: possibly only 1 pair.)

> [!example] Q90: 7 numbers from $\{2,...,13\}$ → two sum to 15
> Pairs: $\{2,13\},\{3,12\},\{4,11\},\{5,10\},\{6,9\},\{7,8\}$ — 6 pairs. 7 numbers into 6 pairs → one pair complete.

> [!example] Q91: 12 chairs, 9 people → 3 consecutive chairs occupied
> Suppose not: between any two occupied, there's a gap. Group chairs into 4 triples: $\{1,2,3\},\{4,5,6\},\{7,8,9\},\{10,11,12\}$. By PHP, some triple has $\geq \lceil 9/4\rceil = 3$ people → 3 consecutive.

> [!example] Q92: Sequence of $n^2+1$ distinct reals → monotone subsequence of length $n+1$ (Erdős–Szekeres)
> For each element $a_i$, let $(f_i, g_i)$ = (length of longest increasing subseq ending at $i$, length of longest decreasing subseq ending at $i$). If neither $f_i \geq n+1$ nor $g_i \geq n+1$: then $f_i, g_i \in \{1,...,n\}$ → only $n^2$ pairs, but $n^2+1$ elements → two elements share same pair → contradicts distinct reals and strict monotonicity. Contradiction.

---

## §7 — Derangements

> [!note] Derangement = permutation with **no fixed points**

$$\boxed{D_n = n!\sum_{k=0}^{n}\frac{(-1)^k}{k!} \approx \frac{n!}{e}}$$

**Recurrence:**
$$D_n = (n-1)(D_{n-1} + D_{n-2}), \quad D_1 = 0,\; D_2 = 1$$

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $D_n$ | 0 | 1 | 2 | 9 | 44 | 265 | 1854 | 14833 |

> [!example] Q79: 8 men, hats returned — no man gets his own
> $D_8 = 14833$

**Proof of recurrence $D_n = (n-1)(D_{n-1}+D_{n-2})$:**
Consider where element 1 goes: say it goes to position $k \neq 1$. Two cases:
- If $k$ goes to 1: remaining $n-2$ elements must be deranged → $D_{n-2}$ ways.
- If $k$ doesn't go to 1: relabel $k$'s slot as "1" → derangement of $n-1$ elements → $D_{n-1}$ ways.
There are $n-1$ choices for $k$, so $D_n = (n-1)(D_{n-1}+D_{n-2})$.

---

## §8 — Stirling Numbers & Set Partitions

### 8.1 Definitions

> [!note] **Stirling number of the 2nd kind $S(n,k)$**
> = number of ways to partition $[n]$ into exactly $k$ **non-empty** subsets

**Recurrence:**
$$\boxed{S(n,k) = k\cdot S(n-1,k) + S(n-1,k-1)}$$

> [!tip] Intuition: Element $n$ either joins an existing subset ($k$ choices → $k\cdot S(n-1,k)$) or forms its own new subset ($S(n-1,k-1)$).

### 8.2 Special Values

| Formula | Value |
|---|---|
| $S(n,1)$ | $1$ |
| $S(n,n)$ | $1$ |
| $S(n,n-1)$ | $\binom{n}{2}$ |
| $S(n,2)$ | $2^{n-1}-1$ |

### 8.3 Bell Numbers

$$B_n = \sum_{k=0}^{n} S(n,k) \quad \text{(total partitions of } [n]\text{)}$$

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $B_n$ | 1 | 2 | 5 | 15 | 52 |

### 8.4 Partitions of $[4]$

| $k$ | $S(4,k)$ | Partitions |
|---|---|---|
| 1 | 1 | $\{1,2,3,4\}$ |
| 2 | 7 | $\{1\}\{2,3,4\},\{2\}\{1,3,4\},\{3\}\{1,2,4\},\{4\}\{1,2,3\},\{1,2\}\{3,4\},\{1,3\}\{2,4\},\{1,4\}\{2,3\}$ |
| 3 | 6 | $\{1,2\}\{3\}\{4\}, \{1,3\}\{2\}\{4\}, \{1,4\}\{2\}\{3\}, \{2,3\}\{1\}\{4\}, \{2,4\}\{1\}\{3\}, \{3,4\}\{1\}\{2\}$ |
| 4 | 1 | $\{1\}\{2\}\{3\}\{4\}$ |

$B_4 = 1+7+6+1 = 15$

### 8.5 Bijection: Partitions of $[n]$ into 2 parts ↔ Non-empty subsets of $[n-1]$

Map: partition $\{A, B\}$ of $[n]$ where $n \in A$ → $A \setminus \{n\}$ (non-empty subset of $[n-1]$).
Inverse: $S \subseteq [n-1]$, $S \neq \emptyset$ → partition $\{S\cup\{n\}, [n-1]\setminus S\}$.

### 8.6 Checking if Something is a Partition

A collection of sets is a partition of $X$ iff:
1. All sets are **non-empty**
2. Sets are **pairwise disjoint** (no element in two sets)
3. Their **union = $X$**

> [!example] Q61: Which are partitions of $\{1,2,3,4,5,6\}$?
> (a) $\{1,2\},\{2,3,4\},\{4,5,6\}$ — 2 appears twice, 3 missing → **NO**
> (b) $\{1\},\{2,3,6\},\{4\}$ — 5 missing → **NO**
> (c) $\{2,4,6\},\{1,3,5\}$ — disjoint, union = all → **YES**
> (d) $\{1,4,5\},\{2,6\}$ — 3 missing → **NO**

---

## §9 — Permutation Algebra

### 9.1 Notations

**One-line notation:** $\sigma = a_1 a_2 \cdots a_n$ means $\sigma(i) = a_i$

**Two-line notation:**
$$\sigma = \begin{pmatrix} 1 & 2 & 3 & \cdots & n \\ \sigma(1) & \sigma(2) & \sigma(3) & \cdots & \sigma(n) \end{pmatrix}$$

**Cycle notation:** $(a\;b\;c)$ means $a\to b\to c\to a$. Fixed points are omitted.

### 9.2 Converting One-line to Cycle

```
Example: σ = 36215847  (σ(1)=3, σ(2)=6, σ(3)=2, σ(4)=1, σ(5)=5, σ(6)=8, σ(7)=4, σ(8)=7)

Start at 1: 1→3→2→6→8→7→4→1  (one cycle!)
            5→5 (fixed point)
Result: (1 3 2 6 8 7 4)(5)  →  simplified: (1 3 2 6 8 7 4)
```

### 9.3 Operations

| Operation | How to compute |
|---|---|
| $\sigma^{-1}$ | Reverse each cycle: $(a\;b\;c\;d)^{-1} = (d\;c\;b\;a)$ |
| $\sigma^2$ | Apply $\sigma$ twice. For $k$-cycle: $(a_1\cdots a_k)^2$ → two cycles if $k$ even, one cycle if $k$ odd |
| $\sigma \circ \tau$ | Apply $\tau$ first, then $\sigma$: $(\sigma\circ\tau)(x) = \sigma(\tau(x))$ |

> [!example] $\sigma = (1\;3\;5)(2\;4\;6)$
> $\sigma^{-1} = (5\;3\;1)(6\;4\;2) = (1\;5\;3)(2\;6\;4)$
> $\sigma^2 = (1\;5\;3)(2\;6\;4)$... apply $(1\;3\;5)$ twice: $1\to3\to5$, $3\to5\to1$, $5\to1\to3$ → $(1\;5\;3)$. Same for the other. So $\sigma^2 = (1\;5\;3)(2\;6\;4)$.

> [!example] Compositions with $(6\;2)$ in $\sigma = (2\;3)(1\;7)(5)(6\;2)$
> Note $(6\;2) = (2\;6)$. Composition: apply right to left. This is shorthand for $\sigma = (2\;3)\circ(1\;7)\circ(5)\circ(2\;6)$. Trace each element: $1\to 7, 2\to 6\to 6\to 6..$ trace carefully step by step.

### 9.4 Counting Permutations

> [!example] Q72: Permutations of $[4]$ mapping $1\to 3$
> Fix $\sigma(1)=3$, remaining 3 elements arrange freely: $3! = 6$

> [!example] Q84: Permutations of $[2n]$ with even numbers at odd positions
> Odd positions: $1,3,5,...,2n-1$ ($n$ positions). Place $n$ even numbers: $n!$ ways. Place $n$ odd numbers in $n$ even positions: $n!$ ways.
> $$\text{Answer: }(n!)^2$$

> [!example] Q32: $n$ men and $n$ women in a row, alternating
> Either M-W-M-W-… or W-M-W-M-…: 2 patterns. Each pattern: $n!$ for men $\times$ $n!$ for women.
> $$\text{Answer: }2\cdot(n!)^2$$

> [!example] Q27: Pair up $2n$ club members for singles
> Step 1 — choose pairs: $\frac{(2n)!}{2^n \cdot n!}$ (divide by $2^n$ because each pair unordered, divide by $n!$ because pairs themselves unordered)
> Step 2 — also specify server: multiply by $2^n$ → $\frac{(2n)!}{n!}$

---

## §10 — Linear Recurrences

### 10.1 Characteristic Root Method

**Step 1:** Write characteristic equation by substituting $a_n = r^n$:

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots \implies r^n = c_1 r^{n-1} + c_2 r^{n-2} + \cdots$$

Divide by $r^{n-k}$ to get the **characteristic polynomial**.

**Step 2:** Find roots $r_1, r_2, \ldots$

**Step 3:** Write general solution:

| Root type | Contribution to $a_n$ |
|---|---|
| Distinct real $r$ | $A \cdot r^n$ |
| Repeated root $r$ (multiplicity $m$) | $(A_0 + A_1 n + \cdots + A_{m-1}n^{m-1})\cdot r^n$ |

**Step 4:** For non-homogeneous, add particular solution:

| RHS type | Try as particular solution |
|---|---|
| Constant $c$ | $A$ (if $1$ not a root), or $An$ (if $1$ is a root) |
| $\alpha^n$ | $A\cdot\alpha^n$ (if $\alpha$ not a root), or $An\cdot\alpha^n$ (if $\alpha$ is a root) |
| Degree-$d$ polynomial | Degree-$d$ polynomial (or $d+m$ if 1 is a root of multiplicity $m$) |

**Step 5:** Use initial conditions to solve for constants.

### 10.2 Worked Examples

> [!example] Q10a: $a_0 = 2$, $a_n = 3a_{n-1}$
> Characteristic: $r=3$. General: $a_n = A\cdot 3^n$.
> IC: $a_0 = A = 2$ → $\boxed{a_n = 2\cdot 3^n}$

> [!example] Q10b: $a_0 = 2$, $a_n = 3a_{n-1} + 1$
> Homogeneous: $A\cdot 3^n$. Particular: try $B$ (constant). $B = 3B+1 \Rightarrow B = -\frac{1}{2}$.
> General: $a_n = A\cdot 3^n - \frac{1}{2}$. IC: $A - \frac{1}{2} = 2 \Rightarrow A = \frac{5}{2}$.
> $$\boxed{a_n = \frac{5}{2}\cdot 3^n - \frac{1}{2}}$$

> [!example] Q10c: $a_0=1,\; a_1=2,\; a_n = 5a_{n-1}-4a_{n-2}$
> Characteristic: $r^2 - 5r + 4 = 0 \Rightarrow (r-1)(r-4)=0 \Rightarrow r=1,4$.
> General: $a_n = A\cdot 1^n + B\cdot 4^n = A + B\cdot 4^n$.
> IC: $A+B=1$, $A+4B=2$ → $3B=1 \Rightarrow B=\frac{1}{3}, A=\frac{2}{3}$.
> $$\boxed{a_n = \frac{2}{3} + \frac{1}{3}\cdot 4^n}$$

> [!example] Q10d: $u_0=2,\; u_1=-6$, $u_{n+2}+8u_{n+1}-9u_n = 8\cdot 3^{n+1}$
> Characteristic: $r^2+8r-9=0 \Rightarrow (r+9)(r-1)=0 \Rightarrow r=1,-9$.
> Particular: RHS $= 24\cdot 3^n$, try $P\cdot 3^n$ (3 is not a root).
> $9P\cdot 3^n + 24P\cdot 3^n - 9P\cdot 3^n = 24\cdot 3^n \Rightarrow 24P = 24 \Rightarrow P=1$.
> General: $u_n = A + B(-9)^n + 3^n$.
> IC: $u_0: A+B+1=2 \Rightarrow A+B=1$. $u_1: A-9B+3=-6 \Rightarrow A-9B=-9$. Subtract: $10B=10 \Rightarrow B=1, A=0$.
> $$\boxed{u_n = (-9)^n + 3^n}$$

> [!example] Q10e: $u_0=1$, $u_{n+1}-2u_n = 4^n$
> Homogeneous: $r=2$ → $A\cdot 2^n$. Particular: try $B\cdot 4^n$ (4 ≠ 2).
> $B\cdot 4^{n+1} - 2B\cdot 4^n = 4^n \Rightarrow 4B-2B=1 \Rightarrow B=\frac{1}{2}$.
> General: $u_n = A\cdot 2^n + \frac{1}{2}\cdot 4^n$.
> IC: $A + \frac{1}{2} = 1 \Rightarrow A = \frac{1}{2}$.
> $$\boxed{u_n = \frac{1}{2}\cdot 2^n + \frac{1}{2}\cdot 4^n = 2^{n-1} + 4^{n-1}\cdot 2 = 2^{n-1}(1+2^{n-1})}$$

> [!example] Q10f: Words of length $n$ over $\{a,b,c,d\}$ with odd number of b's
> Show $q_{n+1} = 4^n + 2q_n$: A word of length $n+1$ with odd b's either ends in non-b (4 choices... wait: 3 choices × $q_n$ words) or ends in b (1 choice × words of length $n$ with EVEN b's = $4^n - q_n$). So $q_{n+1} = 3q_n + (4^n - q_n) = 2q_n + 4^n$ ✓.
> Solve: $q_n = A\cdot 2^n + B\cdot 4^n$ (particular for $4^n$: since 4 is not a root of $r=2$, try $B\cdot 4^n$: $B\cdot 4^{n+1} = 2B\cdot 4^n + 4^n \Rightarrow 4B-2B=1 \Rightarrow B=\frac{1}{2}$).
> $q_0 = 0$ (empty word, 0 b's = even, not odd): $A + \frac{1}{2} = 0 \Rightarrow A = -\frac{1}{2}$.
> $$\boxed{q_n = \frac{4^n - 2^n}{2}}$$

---

## §11 — Generating Functions

### 11.1 The Essential GF Dictionary

$$\boxed{\text{Each "bin" or "type" contributes one factor. Multiply all factors.}}$$

# Generating Functions: Master Reference

| Description / Sequence                                                             | Generating Function (OGF)          | Series Expansion / General Formula              |
| :--------------------------------------------------------------------------------- | :--------------------------------- | :---------------------------------------------- |
| **Combinatorial Conditions**                                                       |                                    | *(Building blocks for a single variable $x_i$)* |
| $x_i \geq 0$ (no restriction)                                                      | $\frac{1}{1 - x}$                  | $1 + x + x^2 + x^3 + \dots$                     |
| $x_i \geq a$                                                                       | $\frac{x^a}{1 - x}$                | $x^a + x^{a+1} + x^{a+2} + \dots$               |
| $x_i = a$ (exactly $a$)                                                            | $x^a$                              | $x^a$                                           |
| $0 \leq x_i \leq b$                                                                | $\frac{1 - x^{b+1}}{1 - x}$        | $1 + x + x^2 + \dots + x^b$                     |
| $a \leq x_i \leq b$                                                                | $\frac{x^a(1 - x^{b-a+1})}{1 - x}$ | $x^a + x^{a+1} + \dots + x^b$                   |
| $x_i$ even                                                                         | $\frac{1}{1 - x^2}$                | $1 + x^2 + x^4 + \dots$                         |
| $x_i$ odd                                                                          | $\frac{x}{1 - x^2}$                | $x + x^3 + x^5 + \dots$                         |
| $x_i$ multiple of $m$                                                              | $\frac{1}{1 - x^m}$                | $1 + x^m + x^{2m} + \dots$                      |
| $x_i \in \{1, 2\}$                                                                 | $x + x^2$                          | $x + x^2$                                       |
| $x_i \geq a$, at least 2 turns                                                     | $\frac{x^{2a}}{(1 - x^a)^2} \dots$ | $(x^a + x^{a+1} + \dots)^2$                     |
| **Standard Sequences**                                                             |                                    | *(Closed-form OGFs for common sequences)*       |
| Constant 1s: $(1, 1, 1, \dots)$                                                    | $\frac{1}{1 - x}$                  | $\sum_{k=0}^{\infty} x^k$                       |
| Geometric: $(1, r, r^2, \dots)$                                                    | $\frac{1}{1 - rx}$                 | $\sum_{k=0}^{\infty} r^k x^k$                   |
| Alternating: $(1, 0, 1, 0, \dots)$                                                 | $\frac{1}{1 - x^2}$                | $\sum_{k=0}^{\infty} x^{2k}$                    |
| Binomial Theorem: <br> $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}, 0, \dots$ | $(1 + x)^n$                        | $\sum_{k=0}^{n} \binom{n}{k} x^k$               |
| Multichoose / Combinations with repetition: $\binom{n+k-1}{k}$                     | $\frac{1}{(1 - x)^n}$              | $\sum_{k=0}^{\infty} \binom{n+k-1}{k} x^k$      |
| Counting: $(1, 2, 3, 4, \dots)$                                                    | $\frac{1}{(1 - x)^2}$              | $\sum_{k=0}^{\infty} (k+1) x^k$                 |
| Whole Numbers: $(0, 1, 2, 3, \dots)$                                               | $\frac{x}{(1 - x)^2}$              | $\sum_{k=0}^{\infty} k x^k$                     |
| Squares: $(1, 4, 9, 16, \dots)$                                                    | $\frac{1 + x}{(1 - x)^3}$          | $\sum_{k=0}^{\infty} (k+1)^2 x^k$               |

### 11.2 Key Standard GFs to Memorize

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n \qquad \frac{1}{(1-x)^r} = \sum_{n=0}^{\infty}\binom{n+r-1}{r-1}x^n$$

$$\frac{x}{1-x-x^2} = \sum_{n=0}^{\infty} f_n x^n \quad \text{(Fibonacci)}$$

### 11.3 GF Manipulation Rules

| Transform                                             | Result                                 |
| ----------------------------------------------------- | -------------------------------------- |
| $(a_1, a_2, a_3, \ldots)$ — drop first term           | $\dfrac{A(x) - a_0}{x}$                |
| $(a_0, 2a_1, 4a_2, \ldots)$ — scale by powers of 2    | $A(2x)$                                |
| $(a_0, a_0+a_1, a_0+a_1+a_2, \ldots)$ — prefix sums   | $\dfrac{A(x)}{1-x}$                    |
| $(a_0, a_1 b, a_2 b^2, \ldots)$ — scale by $b^n$      | $A(bx)$                                |
| $(a_0, 0, a_2, 0, a_4, \ldots)$ — even terms in place | $\dfrac{A(x)+A(-x)}{2}$                |
| $(a_0, a_2, a_4, \ldots)$ — extract even-indexed      | $\dfrac{A(\sqrt{x})+A(-\sqrt{x})}{2}$  |
| Right shift by $k$<br>Left shift by k                 | $x^k \cdot A(x)$<br>$\frac{A(x)}{x^k}$ |
| Convolution $c_n = \sum a_i b_{n-i}$                  | $A(x) \cdot B(x)$                      |

> [!warning] For $(a_0, a_0+a_1, a_1+a_2, \ldots)$ — use the definition directly, these mixed-shift formulas are easy to confuse. Write out the first few terms and match.

### 11.4 Extracting Coefficients (Partial Fractions)

**Procedure:**
1. Factor denominator completely into $(1-r_i x)$ terms
2. Decompose: $A(x) = \dfrac{C_1}{1-r_1 x} + \dfrac{C_2}{1-r_2 x} + \cdots$
3. Each $\dfrac{C}{1-rx} = \sum C\cdot r^n x^n$ → coefficient of $x^n$ is $C\cdot r^n$

| GF | $a_n$ |
|---|---|
| $\frac{x^3}{1-3x}$ | $3^{n-3}$ for $n \geq 3$, else $0$ |
| $\frac{x^3+x}{1-3x}$ | For $n\geq 3$: $3^{n-3}+3^{n-1}$. For $n=1$: 1. |
| $\frac{x^2}{(1-x)^2}$ | $n-1$ for $n \geq 1$, else 0 (since $\frac{1}{(1-x)^2}=\sum(n+1)x^n$) |
| $\frac{x^2-x}{(1-x)^2}$ | $n-2$ for $n\geq 2$, else check by expanding |
| $\frac{x^2}{(1-x)^3}$ | $\binom{n-2+2}{2} = \binom{n}{2}$ for $n\geq 2$ |
| $(3x-4)^3$ | Expand: coefficient of $x^k$ is $\binom{3}{k}3^k(-4)^{3-k}$ for $k=0,1,2,3$ |

### 11.5 GF for Constrained Distributions — Worked Examples

> [!example] Q12: 10 identical balloons to 4 children, each gets $\geq 2$
> $A(x) = \left(\frac{x^2}{1-x}\right)^4 = \frac{x^8}{(1-x)^4}$
> Need $[x^{10}]$: $[x^2]$ in $\frac{1}{(1-x)^4} = \sum\binom{n+3}{3}x^n$
> $= \binom{2+3}{3} = \binom{5}{3} = 10$

> [!example] Q13: 15 identical objects to 6 boxes, $1 \leq x_i \leq 3$
> $A(x) = \left(\frac{x(1-x^3)}{1-x}\right)^6 = \frac{x^6(1-x^3)^6}{(1-x)^6}$
> Need $[x^{15}]$: → $[x^9]$ in $\frac{(1-x^3)^6}{(1-x)^6}$
> $(1-x^3)^6 = \sum_{j=0}^{6}\binom{6}{j}(-1)^j x^{3j}$
> $\frac{1}{(1-x)^6} = \sum\binom{n+5}{5}x^n$
> $[x^9] = \sum_{j: 3j\leq 9}\binom{6}{j}(-1)^j\binom{9-3j+5}{5}$
> $= \binom{6}{0}\binom{14}{5} - \binom{6}{1}\binom{11}{5} + \binom{6}{2}\binom{8}{5} - \binom{6}{3}\binom{5}{5}$
> $= 2002 - 6\cdot462 + 15\cdot56 - 20\cdot1 = 2002 - 2772 + 840 - 20 = 50$

> [!example] Q6: $x_1+x_2+x_3+x_4=k$, with $x_1\geq3,\;1\leq x_2\leq5,\;0\leq x_3\leq4,\;x_4\geq1$. Find $a_7$.
> $A(x) = \frac{x^3}{1-x}\cdot\frac{x(1-x^5)}{1-x}\cdot\frac{1-x^5}{1-x}\cdot\frac{x}{1-x} = \frac{x^5(1-x^5)^2}{(1-x)^4}$
> Need $[x^7]$: → $[x^2]$ in $\frac{(1-x^5)^2}{(1-x)^4} = (1-2x^5+x^{10})\sum\binom{n+3}{3}x^n$
> $[x^2] = \binom{5}{3} = 10$. (Terms $-2x^5$ and $+x^{10}$ contribute nothing at $x^2$.)
> $a_7 = 10$

### 11.6 Fibonacci GF Identities

GF: $F(x) = \dfrac{x}{1-x-x^2}$. Note $F(x) = \dfrac{F(x)}{1} + x\cdot\dfrac{F(x)}{x}$ tricks.

| Identity | Proof idea |
|---|---|
| $\sum_{k=0}^{n}f_k = f_{n+2}-1$ | $F(x)/(1-x) = \sum(\text{prefix sums})$; compare with $(F(x)+x)/(1-x)$ |
| $\sum_{k=0}^{n}f_{2k} = f_{2n+1}-1$ | Use $F(x^2)$ or odd/even split |
| $\sum_{k=1}^{n}f_{2k-1} = f_{2n}$ | Complement of even sum identity |

### 11.7 Closed Formula for $k$-combinations with Repetition

$k$-combinations with repetition from $[n]$: GF is $\dfrac{1}{(1-x)^n}$.

$$[x^k]\frac{1}{(1-x)^n} = \binom{k+n-1}{k} = \binom{k+n-1}{n-1}$$

### 11.8 Solving $S(n,2)$ via GF

Recurrence: $S(n,2) = 1 + 2S(n-1,2)$, $S(0,2)=S(1,2)=0$.

GF: $G(x) = \dfrac{x^2}{(1-x)(1-2x)}$. Partial fractions: $\dfrac{-1}{1-x} + \dfrac{1}{1-2x}$.

$$\boxed{S(n,2) = 2^{n-1}-1}$$

### 11.9 Solving Recurrences with Generating Functions

> [!tip] GF method — full pipeline
> 1. Multiply both sides by $x^n$, sum over all valid $n$
> 2. Express every sum in terms of $F(x) = \sum a_n x^n$
> 3. Solve for $F(x)$ algebraically
> 4. Partial-fraction decompose $F(x)$
> 5. Read off $a_n$ from standard OGF table

> [!example] GF method
> $a_0 = 2$, $a_n = 3a_{n-1}$ for $n \geq 1$
> Multiply by $x^n$, sum $n \geq 1$: $\sum_{n\geq1} a_n x^n = 3x \sum_{n\geq1} a_{n-1} x^{n-1}$
> $F(x) - 2 = 3x \cdot F(x)$
> $F(x) = \dfrac{2}{1-3x} \implies a_n = 2 \cdot 3^n$


---

## §12 — Quick-Fire Reference

> [!warning] Common patterns
> - **"At least one"** → complement: total $-$ none
> - **"At most $k$"** → sum cases $0\ldots k$, or complement
> - **"Exactly $k$"** → $C(n,k) \cdot (\text{rest})$
> - **Distributing identical objects** → stars & bars
> - **Distributing distinct objects, identical boxes** → Stirling numbers
> - **No two consecutive / alternating** → direct case split or complement
> - **Recurrence given** → characteristic equation first; check if RHS matches a root
> - **GF asked** → build from constraints using $\frac{1}{1-x^k}$ blocks, multiply together
### 12.1 Must-Know Numbers

| Symbol | Value |
|---|---|
| $D_3$ | 2 |
| $D_4$ | 9 |
| $D_5$ | 44 |
| $D_8$ | 14833 |
| $S(4,2)$ | 7 |
| $S(4,3)$ | 6 |
| $B_4$ | 15 |
| $B_5$ | 52 |

### 12.2 Pattern → Formula at a Glance

| Magic phrase in problem | Formula |
|---|---|
| "arrange $n$ objects, $r_i$ identical" | $n!/(r_1!\cdots r_m!)$ |
| "in how many ways can you choose $k$ from $n$" | $\binom{n}{k}$ |
| "how many passwords of length $k$ from $n$ chars" | $n^k$ |
| "distribute $k$ distinct into $n$ distinct, no restriction" | $n^k$ |
| "distribute $k$ identical into $n$ distinct, no restriction" | $\binom{n+k-1}{k}$ |
| "distribute $k$ identical into $n$ distinct, $\geq 1$ each" | $\binom{k-1}{n-1}$ |
| "distribute $k$ identical into $n$ distinct, $\geq a$ each" | $\binom{k-na+n-1}{n-1}$ |
| "distribute $k$ distinct into $n$ identical, $\geq 1$ each" | $S(k,n)$ |
| "no man receives his own hat" | $D_n$ |
| "partitions of $[n]$ into $k$ nonempty parts" | $S(n,k)$ |
| "prove two share same [property]" | Pigeonhole |
| "coefficient of $x^a y^b$ in $(cx+dy)^n$" | $\binom{n}{a}c^a d^b$ |
| "solve recurrence $a_n = c_1 a_{n-1} + c_2 a_{n-2}$" | Characteristic roots |
| "integer solutions to $\sum x_i = k$, $x_i \geq 0$" | $\binom{n+k-1}{k}$ |
| "integer solutions to $\sum x_i \leq k$, $x_i \geq 0$" | $\binom{n+k}{k}$ |

### 12.3 The Substitution Kit (Stars & Bars Constraints)

```
Constraint     →   Substitution         →   Effect on sum
──────────────────────────────────────────────────────────
xᵢ ≥ a         →   yᵢ = xᵢ - a        →   subtract n·a from k
xᵢ ≤ b         →   inclusion-exclusion →   subtract cases xᵢ ≥ b+1
xᵢ = 0 or ≥c  →   split into cases    →   case analysis
∑xᵢ ≤ k        →   add slack s ≥ 0    →   becomes ∑xᵢ + s = k
```

### 12.4 Traps Checklist

- [ ] Order matters vs doesn't matter → $P$ vs $C$
- [ ] After substitution $y_i = x_i - a$: did you update the total? ($k \to k - na$)
- [ ] $k > n$ with "at most 1 each" → answer is **0**, not an error
- [ ] Signs in binomial expansion: $(-3y)^{99}$ is **negative**
- [ ] In multinomial: verify $\sum k_i = n$ before computing
- [ ] "Identical boxes" → Stirling or integer partitions, **not** stars & bars
- [ ] Cycle notation composition: **right to left**
- [ ] $S(n,2) = 2^{n-1}-1$ not $2^{n-1}$
- [ ] Pigeonhole: explicitly state what are the pigeons and what are the holes
- [ ] GF method: when RHS $= \alpha^n$ and $\alpha$ is already a root, multiply particular guess by $n$
