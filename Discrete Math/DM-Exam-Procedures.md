---
tags: [discrete-math, exam-prep, counting, recurrence, generating-functions]
course: Discrete Mathematics — VGU CS
topics: [basic counting, linear recurrences, generating functions]
status: ready
---

# 📐 DM Exam Procedures — Counting, Recurrences, GFs

---

## Part 1 — Basic Counting Rules

### 🔢 Rule Map

| Situation | Tool |
|---|---|
| Sequential independent choices | **Product Rule** |
| Mutually exclusive alternatives | **Sum Rule** |
| Ordered selection, no repeat | **Permutation** $P(n,k) = \frac{n!}{(n-k)!}$ |
| Unordered selection, no repeat | **Combination** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| Indistinct objects in a line | **Multinomial** $\frac{n!}{k_1! k_2! \cdots k_r!}$ |
| Indistinct objects to bins | **Stars & Bars** |
| Ordered selection, with repeat | $n^k$ |
| Unordered selection, with repeat | Stars & Bars $\binom{n+k-1}{k}$ |

---

### 🧩 Product Rule

**When:** you make $k$ sequential choices independently.

**Procedure:**
1. Identify each independent decision slot.
2. Count options for each slot.
3. Multiply all counts together.

> [!example]+ License plates: 3 uppercase letters then 3 digits
> - Slot 1–3 (letters): 26 choices each → $26^3$
> - Slot 4–6 (digits): 10 choices each → $10^3$
> - Total: $26^3 \times 10^3 = 17{,}576{,}000$

> [!example]+ Passwords 4–8 chars, upper+lower case
> - 52 choices per character (26 lower + 26 upper)
> - Each length is independent: $52^4 + 52^5 + 52^6 + 52^7 + 52^8$

---

### ➕ Sum Rule

**When:** alternatives are mutually exclusive (can't happen together).

**Procedure:**
1. Split into disjoint cases.
2. Count each case separately.
3. Add.

> [!example]+ Chairs labeled letter + number ≤ 100
> - Letters: 26, numbers: 100
> - Each chair = one letter AND one number → Product Rule inside
> - Total: $26 \times 100 = 2600$

> [!tip]+ Complement Trick
> If "at least one" or "more than $k$" is hard, compute:
> $$\text{Answer} = \text{Total} - \text{(what you don't want)}$$
> **Example:** 5-char ASCII strings with at least one `@`:
> Total = $128^5$, none with `@` = $127^5$
> Answer = $128^5 - 127^5$

---

### 🔀 Permutations

**When:** ordered selection, no repetition.

$$P(n, k) = \frac{n!}{(n-k)!}$$

**Procedure:**
1. Confirm order matters and no repeats.
2. Plug in $n$ (pool size) and $k$ (slots to fill).

> [!example]+ 10-person club: president + 2-person advisory board
> - President: choose 1 from 10 → 10 ways
> - Board (order doesn't matter among board): choose 2 from remaining 9 → $\binom{9}{2}$
> - Total: $10 \times \binom{9}{2} = 10 \times 36 = 360$

> [!example]+ Draw 1st, 2nd, 3rd card from 52-card deck
> Order matters, no repeat: $P(52, 3) = 52 \times 51 \times 50 = 132{,}600$

**Treating a block as one unit:**

> [!example]+ Permutations of `ABC12DE` containing `BC1` as substring
> - Glue `BC1` into one unit → now 5 units: `[BC1], A, 2, D, E`
> - Arrange 5 units: $5! = 120$

---

### 🎯 Combinations

**When:** unordered selection, no repetition.

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

> [!example]+ Draw 2 cards from 52 (order doesn't matter)
> $\binom{52}{2} = \frac{52 \times 51}{2} = 1326$

> [!example]+ Class of 9F + 20M, pick 11 for soccer with exactly 3 female
> - Choose 3 from 9 female: $\binom{9}{3}$
> - Choose 8 from 20 male: $\binom{20}{8}$
> - Total: $\binom{9}{3} \times \binom{20}{8} = 84 \times 125970 = 10{,}581{,}480$

> [!example]+ At least one female (complement)
> Total ways = $\binom{29}{11}$
> All male = $\binom{20}{11}$
> Answer = $\binom{29}{11} - \binom{20}{11}$

---

### 🧮 Multinomial — Indistinct Objects in a Line

**When:** arrange $n$ objects where object type $i$ appears $k_i$ times.

$$\frac{n!}{k_1!\, k_2!\, \cdots\, k_r!}$$

> [!example]+ Strings from `CASABLANCA` (10 letters: C×2, A×4, S×1, B×1, L×1, N×1)
> $$\frac{10!}{2!\cdot 4!\cdot 1!\cdot 1!\cdot 1!\cdot 1!} = \frac{3628800}{2 \times 24} = 75600$$

> [!example]+ Paint 10 distinct chairs: 3 green, 3 blue, 4 red
> Chairs are distinct → this is assignment, not arrangement:
> $$\frac{10!}{3!\,3!\,4!} = 4200$$

> [!example]+ Multinomial coefficient in expansion of $(2x - 3y - 2z)^{10}$, term $x^3 y^2 z^5$
> 1. Check: $3 + 2 + 5 = 10$ ✓
> 2. Coefficient = $\binom{10}{3,2,5} \times (2)^3 \times (-3)^2 \times (-2)^5$
> $$= \frac{10!}{3!\,2!\,5!} \times 8 \times 9 \times (-32) = 2520 \times (-2304) = -5{,}806{,}080$$

---

### ⭐ Stars & Bars

**Case 1 — Non-negative integers** ($x_i \geq 0$):
$$x_1 + x_2 + \cdots + x_n = k \quad\Longrightarrow\quad \binom{n+k-1}{k}$$

**Case 2 — Positive integers** ($x_i \geq 1$): substitute $y_i = x_i - 1$:
$$y_1 + \cdots + y_n = k - n \quad\Longrightarrow\quad \binom{k-1}{n-1}$$

**Case 3 — Lower bound** $x_i \geq c_i$: substitute $y_i = x_i - c_i$.

**Case 4 — Upper bound** $x_i \leq u_i$: use complement + PIE (subtract cases that exceed bound).

> [!example]+ $x_1+x_2+x_3+x_4+x_5 = 21$, each $x_i \geq 2$
> Let $y_i = x_i - 2$, so $\sum y_i = 21 - 10 = 11$, $y_i \geq 0$
> $$\binom{5+11-1}{11} = \binom{15}{11} = 1365$$

> [!example]+ $x_1+x_2+x_3+x_4+x_5 = 21$, $0 \leq x_1 \leq 10$
> Total (no upper bound): $\binom{25}{21}$
> Subtract bad (x₁ ≥ 11): let $y_1 = x_1 - 11$, solve $\sum = 10$ → $\binom{14}{10}$
> Answer: $\binom{25}{21} - \binom{14}{10}$

> [!example]+ Inequality $x_1+x_2+x_3 \leq 11$, $x_i \geq 0$
> Add slack variable $x_4 \geq 0$: $x_1+x_2+x_3+x_4 = 11$
> $$\binom{4+11-1}{11} = \binom{14}{11} = 364$$

---

### 🔁 Distinct vs Identical Distribution Table

| Objects | Boxes | Condition | Formula |
|---|---|---|---|
| Distinct | Distinct | None | $n^k$ |
| Distinct | Distinct | Each box ≥ 1 | PIE / Stirling |
| Identical | Distinct | None | $\binom{n+k-1}{k}$ |
| Identical | Distinct | Each ≥ 1 | $\binom{k-1}{n-1}$ |
| Distinct | Identical | None | $\sum_{j=1}^{n} S(k,j)$ |
| Distinct | Identical | Each ≥ 1 | $S(k,n)$ |

---

## Part 2 — Linear Recurrence Relations

### 🔁 Homogeneous Linear Recurrences

**Form:** $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k}$

**Procedure:**

**Step 1 — Write the characteristic equation:**
$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \cdots - c_k = 0$$

**Step 2 — Find roots.**

**Step 3 — Write general solution by case:**

> [!note]- Case A: All roots distinct ($r_1, r_2, \ldots, r_k$ all different)
> $$a_n = A_1 r_1^n + A_2 r_2^n + \cdots + A_k r_k^n$$

> [!note]- Case B: Root $r$ has multiplicity $m$
> That root contributes:
> $$(A_1 + A_2 n + A_3 n^2 + \cdots + A_m n^{m-1})\, r^n$$

**Step 4 — Apply initial conditions** to solve for constants $A_i$.

> [!example]+ $a_0=1,\ a_1=2,\ a_n = 5a_{n-1} - 4a_{n-2}$
> Characteristic eq: $r^2 - 5r + 4 = 0 \Rightarrow (r-1)(r-4) = 0$
> Roots: $r_1 = 1,\, r_2 = 4$ (distinct)
> General solution: $a_n = A \cdot 1^n + B \cdot 4^n = A + B \cdot 4^n$
> Initial conditions:
> - $n=0$: $A + B = 1$
> - $n=1$: $A + 4B = 2$
> Subtract: $3B = 1 \Rightarrow B = \frac{1}{3},\ A = \frac{2}{3}$
> $$\boxed{a_n = \frac{2}{3} + \frac{1}{3} \cdot 4^n}$$

---

### 🔁 Non-Homogeneous Linear Recurrences

**Form:** $a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + f(n)$

**Procedure:**

**Step 1 — Solve the homogeneous part** (set $f(n) = 0$, find $a_n^{(h)}$ as above).

**Step 2 — Find a particular solution** $a_n^{(p)}$ matching the form of $f(n)$:

| $f(n)$ form | Try particular solution |
|---|---|
| Constant $C$ | $a_n^{(p)} = P$ |
| $\beta^n$ (not a characteristic root) | $a_n^{(p)} = P \cdot \beta^n$ |
| $\beta^n$ (is a root of multiplicity $m$) | $a_n^{(p)} = P \cdot n^m \cdot \beta^n$ |
| Polynomial degree $d$ | $a_n^{(p)} = P_d n^d + \cdots + P_0$ |
| $n \cdot \beta^n$ | $a_n^{(p)} = (Pn + Q)\beta^n$ |

**Step 3 — Substitute** $a_n^{(p)}$ into recurrence to solve for coefficients $P, Q, \ldots$

**Step 4 — General solution:** $a_n = a_n^{(h)} + a_n^{(p)}$

**Step 5 — Apply initial conditions** to find constants in $a_n^{(h)}$.

> [!example]+ $a_0=2,\ a_n = 3a_{n-1} + 1$ (constant non-homogeneous)
> Homogeneous: $a_n^{(h)} = A \cdot 3^n$
> Try $a_n^{(p)} = P$ (constant):
> $P = 3P + 1 \Rightarrow -2P = 1 \Rightarrow P = -\frac{1}{2}$
> General: $a_n = A \cdot 3^n - \frac{1}{2}$
> IC: $a_0 = A - \frac{1}{2} = 2 \Rightarrow A = \frac{5}{2}$
> $$\boxed{a_n = \frac{5}{2} \cdot 3^n - \frac{1}{2}}$$

> [!example]+ $u_0=1,\ u_{n+1} - 2u_n = 4^n$ (exponential RHS, not a root)
> Rewrite: $u_{n+1} = 2u_n + 4^n$
> Homogeneous: $u_n^{(h)} = A \cdot 2^n$
> Try $u_n^{(p)} = P \cdot 4^n$: substitute into recurrence (shift index carefully)
> $P \cdot 4^{n+1} = 2P \cdot 4^n + 4^n$
> $4P = 2P + 1 \Rightarrow P = \frac{1}{2}$
> General: $u_n = A \cdot 2^n + \frac{1}{2} \cdot 4^n$
> IC: $u_0 = A + \frac{1}{2} = 1 \Rightarrow A = \frac{1}{2}$
> $$\boxed{u_n = \frac{1}{2} \cdot 2^n + \frac{1}{2} \cdot 4^n}$$

> [!example]+ $u_0=2,\ u_1=-6,\ u_{n+2} + 8u_{n+1} - 9u_n = 8 \cdot 3^{n+1}$ (RHS is root)
> Characteristic eq: $r^2 + 8r - 9 = 0 \Rightarrow (r+9)(r-1) = 0$
> Roots: $r = 1, -9$
> Homogeneous: $u_n^{(h)} = A \cdot 1^n + B \cdot (-9)^n$
> RHS = $24 \cdot 3^n$; is $3$ a characteristic root? No (roots are 1 and -9).
> Try $u_n^{(p)} = P \cdot 3^n$:
> $P \cdot 3^{n+2} + 8P \cdot 3^{n+1} - 9P \cdot 3^n = 24 \cdot 3^n$
> Divide by $3^n$: $9P + 24P - 9P = 24 \Rightarrow 24P = 24 \Rightarrow P = 1$
> General: $u_n = A + B(-9)^n + 3^n$
> IC: $u_0 = A + B + 1 = 2 \Rightarrow A + B = 1$
> $u_1 = A - 9B + 3 = -6 \Rightarrow A - 9B = -9$
> Subtract: $10B = 10 \Rightarrow B = 1,\ A = 0$
> $$\boxed{u_n = (-9)^n + 3^n}$$

---

### ⚡ Solving via Generating Functions (GF Method)

Use when: the problem says "use the GF method" or characteristic roots are messy.

**Procedure:**

**Step 1 — Multiply both sides by $x^n$** and sum from $n = n_0$ to $\infty$.

**Step 2 — Express sums in terms of** $A(x) = \sum_{n \geq 0} a_n x^n$ using shift identities:
$$\sum_{n \geq 1} a_{n-1} x^n = x \cdot A(x)$$
$$\sum_{n \geq 1} a_n x^n = A(x) - a_0$$

**Step 3 — Solve for $A(x)$** algebraically.

**Step 4 — Partial fraction decompose** $A(x)$.

**Step 5 — Expand using** $\dfrac{1}{1 - rx} = \sum_{n \geq 0} r^n x^n$ **to read off $a_n$.**

> [!example]+ $a_0 = 2,\ a_n = 3a_{n-1}$ via GF
> Multiply by $x^n$, sum $n \geq 1$:
> $\sum_{n \geq 1} a_n x^n = 3x \sum_{n \geq 1} a_{n-1} x^{n-1} \cdot x$
> $A(x) - 2 = 3x \cdot A(x)$
> $A(x)(1 - 3x) = 2 \Rightarrow A(x) = \dfrac{2}{1-3x}$
> Expand: $a_n = 2 \cdot 3^n$ ✓

> [!example]+ $a_0=1,\ a_1=2,\ a_n = 5a_{n-1} - 4a_{n-2}$ via GF
> Sum $n \geq 2$:
> $A(x) - 1 - 2x = 5x(A(x) - 1) - 4x^2 A(x)$
> $A(x)(1 - 5x + 4x^2) = 1 - 3x$
> Factor: $(1-x)(1-4x)$
> Partial fractions: $A(x) = \dfrac{1-3x}{(1-x)(1-4x)} = \dfrac{A}{1-x} + \dfrac{B}{1-4x}$
> $1 - 3x = A(1-4x) + B(1-x)$
> $x=1$: $-2 = -3A \Rightarrow A = \frac{2}{3}$
> $x=\frac{1}{4}$: $\frac{1}{4} = \frac{3}{4}B \Rightarrow B = \frac{1}{3}$
> $a_n = \frac{2}{3} \cdot 1^n + \frac{1}{3} \cdot 4^n$ ✓

---

## Part 3 — Generating Functions

### 📚 Core Reference Table

$$\frac{1}{1-x} = \sum_{n \geq 0} x^n \qquad \frac{1}{1-rx} = \sum_{n \geq 0} r^n x^n$$

$$\frac{1}{(1-x)^k} = \sum_{n \geq 0} \binom{n+k-1}{k-1} x^n$$

$$(1+x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k$$

$$\frac{x}{(1-x)^2} = \sum_{n \geq 1} n \cdot x^n \qquad \frac{1}{(1-x)^2} = \sum_{n \geq 0}(n+1)x^n$$

---

### 🛠️ Building a GF from Constraints

**Key idea:** each independent variable/urn contributes one factor. Multiply all factors together.

**Step 1 — Identify variables** and their constraints.

**Step 2 — Write the factor for each variable:**

| Constraint on $x_i$ | Factor |
|---|---|
| $x_i \geq 0$ (no restriction) | $\dfrac{1}{1-x}$ |
| $x_i \geq c$ | $\dfrac{x^c}{1-x}$ |
| $x_i$ even | $\dfrac{1}{1-x^2}$ |
| $x_i$ odd | $\dfrac{x}{1-x^2}$ |
| $x_i$ multiple of $m$ | $\dfrac{1}{1-x^m}$ |
| $0 \leq x_i \leq u$ | $1 + x + x^2 + \cdots + x^u = \dfrac{1-x^{u+1}}{1-x}$ |
| $x_i = c$ (fixed) | $x^c$ |
| $x_i \in \{a, b\}$ | $x^a + x^b$ |

**Step 3 — Multiply all factors.**

**Step 4 — The coefficient of $x^n$** in the product = answer.

> [!example]+ Pay $n$ dollars using coins of 3, 5, 7 dollars
> Each coin type used any number of times:
> $$G(x) = \frac{1}{1-x^3} \cdot \frac{1}{1-x^5} \cdot \frac{1}{1-x^7}$$

> [!example]+ Distribute $n$ candies: 4 children (each odd amount) + 1 adult (1 or 2)
> - Each child (odd): $\dfrac{x}{1-x^2}$ (four children: raise to 4th power)
> - Adult (1 or 2): $x + x^2 = x(1+x)$
> $$G(x) = \left(\frac{x}{1-x^2}\right)^4 \cdot x(1+x) = \frac{x^5}{(1-x^2)^3(1-x)}$$

> [!example]+ Ways to fill bag: apples even, bananas mult of 5, ≤4 oranges, ≤1 pear
> $$G(x) = \frac{1}{1-x^2} \cdot \frac{1}{1-x^5} \cdot (1+x+x^2+x^3+x^4) \cdot (1+x)$$

> [!example]+ Find $a_7$ for $x_1 \geq 3,\ 1 \leq x_2 \leq 5,\ 0 \leq x_3 \leq 4,\ x_4 \geq 1$
> $$G(x) = \frac{x^3}{1-x} \cdot \frac{x(1-x^5)}{1-x} \cdot \frac{1-x^5}{1-x} \cdot \frac{x}{1-x}$$
> $$= \frac{x^5 (1-x^5)^2}{(1-x)^4}$$
> To find $a_7$: coefficient of $x^7$ = coefficient of $x^2$ in $\dfrac{(1-x^5)^2}{(1-x)^4}$
> Since $x^5$ terms don't contribute at $n=2$: coefficient of $x^2$ in $\dfrac{1}{(1-x)^4} = \binom{2+3}{3} = \binom{5}{3} = 10$

---

### 🔍 Extracting Coefficients from a GF

**Goal:** given $G(x)$, find $[x^n] G(x)$ (the coefficient of $x^n$).

**Method 1 — Direct expansion** (for simple $G$):
Use the reference table above directly.

**Method 2 — Partial fractions** (for rational $G$):

1. Factor the denominator completely.
2. Decompose: $\dfrac{P(x)}{(1-r_1 x)(1-r_2 x)\cdots} = \dfrac{A}{1-r_1 x} + \dfrac{B}{1-r_2 x} + \cdots$
3. Solve for $A, B, \ldots$ by substituting roots or matching coefficients.
4. Read off: $[x^n] = A r_1^n + B r_2^n + \cdots$

> [!warning]+ Repeated root in denominator
> If $(1-rx)^m$ appears, that factor contributes:
> $$(A_0 + A_1 n + \cdots + A_{m-1} \binom{n+m-2}{m-1}) r^n$$
> For $(1-rx)^2$: $[x^n] \dfrac{1}{(1-rx)^2} = (n+1)r^n$

> [!example]+ Find closed form for $G(x) = \dfrac{x^2}{(1-x)^2}$
> $= x^2 \cdot \dfrac{1}{(1-x)^2} = x^2 \sum_{n \geq 0}(n+1)x^n = \sum_{n \geq 2}(n-1)x^n$
> So $a_n = n - 1$ for $n \geq 2$, and $a_0 = a_1 = 0$.

> [!example]+ $G(x) = \dfrac{x^3}{1-3x}$
> $= x^3 \sum_{n \geq 0} 3^n x^n = \sum_{n \geq 3} 3^{n-3} x^n$
> So $a_n = 3^{n-3}$ for $n \geq 3$, else $0$.

---

### 🎈 GF for Combinatorial Counting (Distribution Problems)

**Procedure:**
1. Build $G(x)$ by multiplying one factor per bin/variable.
2. Find coefficient of $x^n$ (or $x^k$ for a specific $k$).

> [!example]+ 10 identical balloons, 4 children, each gets ≥ 2
> Each child: $x^2 + x^3 + \cdots = \dfrac{x^2}{1-x}$
> $$G(x) = \left(\frac{x^2}{1-x}\right)^4 = \frac{x^8}{(1-x)^4}$$
> Need $[x^{10}]$: = $[x^2] \dfrac{1}{(1-x)^4} = \binom{2+3}{3} = \binom{5}{3} = 10$

> [!example]+ 15 identical objects, 6 boxes, each box 1–3 objects
> Each box: $x + x^2 + x^3 = x \cdot \dfrac{1-x^3}{1-x}$
> $$G(x) = \left(\frac{x(1-x^3)}{1-x}\right)^6 = \frac{x^6(1-x^3)^6}{(1-x)^6}$$
> Need $[x^{15}]$: = $[x^9] \dfrac{(1-x^3)^6}{(1-x)^6}$
> Expand $(1-x^3)^6 = \sum_{j=0}^{6}(-1)^j \binom{6}{j} x^{3j}$
> $[x^9]$: terms with $3j \leq 9$, i.e., $j = 0, 1, 2, 3$
> $$= \sum_{j=0}^{3}(-1)^j\binom{6}{j}\binom{9-3j+5}{5}$$
> $= \binom{14}{5} - 6\binom{11}{5} + 15\binom{8}{5} - 20\binom{5}{5}$
> $= 2002 - 2772 + 840 - 20 = 50$

---

### 📋 GF Manipulation Reference

| Operation on sequence | Effect on $A(x)$ |
|---|---|
| Shift right (prepend $a_0$) | $x \cdot A(x) + a_0$ ... use carefully |
| Shift left (drop $a_0$) | $\dfrac{A(x) - a_0}{x}$ |
| Scale by $b^n$: $(a_n b^n)$ | $A(bx)$ |
| Partial sums: $\left(\sum_{k=0}^n a_k\right)$ | $\dfrac{A(x)}{1-x}$ |
| Even-indexed terms only | $\dfrac{A(x)+A(-x)}{2}$ |

> [!example]+ GF for $(a_0,\ a_0+a_1,\ a_1+a_2,\ a_2+a_3, \ldots)$
> This is $b_n = a_{n-1} + a_n$ for $n \geq 1$, $b_0 = a_0$
> $B(x) = A(x) + xA(x) - xa_0 + a_0 \cdot x^0$... careful:
> Actually $B(x) = a_0 + \sum_{n \geq 1}(a_{n-1}+a_n)x^n = a_0 + xA(x) + (A(x)-a_0) = (1+x)A(x)$

---

> [!tip]+ Exam checklist
> - [ ] Read constraint type first (≥, ≤, exact, mult of $k$)
> - [ ] Check if RHS is a characteristic root before guessing particular solution
> - [ ] When using GF: shift your index after extracting coefficient ($[x^n] \Rightarrow [x^{n-k}]$ after canceling $x^k$)
> - [ ] Partial fraction: set $x = 1/r_i$ to isolate each coefficient instantly
> - [ ] Stars & bars: always substitute to make $y_i \geq 0$ before applying formula
