# Discrete Mathematics — Counting Cheatsheet
## Basic Counting Rules

| Rule | Formula | When to use |
|------|---------|-------------|
| **Sum** | $\|A \cup B\| = \|A\| + \|B\|$ (disjoint) | Mutually exclusive cases |
| **Product** | $m_1 \cdot m_2 \cdots m_k$ | Sequential independent choices |
| **Complement** | $\|P\| = \|\text{total}\| - \|\overline{P}\|$ | "at least one", "more than k" |
| **Division** | $n$ objects in blocks of $r$ → $n/r$ blocks | Overcounting by fixed factor |
| **Bijection** | $\|A\| = \|B\|$ if bijection $A \leftrightarrow B$ | Double counting, identities |

---

## Permutations & Combinations

$$P(n,k) = \frac{n!}{(n-k)!} \qquad C(n,k) = \frac{n!}{k!\,(n-k)!}$$

$$C(n,k) = C(n,\, n-k) \qquad \text{(symmetry)}$$

$$C(n,k) = C(n-1,k) + C(n-1,k-1) \qquad \text{(Pascal)}$$

- All subsets of $[n]$: $2^n$
- Circular arrangements of $n$: $(n-1)!$

---

## Binomial & Multinomial Theorem

$$\text{Binomial: } (x+y)^n = \sum_{k=0}^{n} C(n,k)\, x^k y^{n-k}$$

$$ x_1^{r_1} x_2^{r_2} \cdots x_m^{r_m} \text{ in } (x_1 + \cdots + x_m)^n = \frac{n!}{r_1!\, r_2! \cdots r_m!}\prod x_i^{r_i}$$

where $r_1 + r_2 + \cdots + r_m = n$.

> [!example] Coefficient extraction
> Coeff of $x^{101}y^{99}$ in $(2x - 3y)^{200}$:
> $$\frac{200!}{101!\, 99!} \cdot 2^{101} \cdot (-3)^{99} = C(200,101) \cdot 2^{101} \cdot (-3)^{99}$$

> [!example] Finding coeff of $x^k$ in $(x + \frac{1}{x})^{100}$
> General term: $C(100, j)\, x^j \cdot x^{-(100-j)} = C(100,j)\, x^{2j-100}$
> Set $2j - 100 = k$ → $j = \frac{k+100}{2}$ (integer only when $k$ is even)
> $$\text{Coeff} = \begin{cases} C\!\left(100,\, \frac{k+100}{2}\right) & k \in \{-100,-98,\ldots,100\} \\ 0 & \text{otherwise} \end{cases}$$

---

## Permutations with Repetition (Multiset)

$$\text{Arrange } n \text{ objects with } n_1 \text{ of type 1, } n_2 \text{ of type 2, ...} = \frac{n!}{n_1!\, n_2! \cdots n_k!}$$

> [!example]
> MISSISSIPPI (M×1, I×4, S×4, P×2): $\dfrac{11!}{1!\,4!\,4!\,2!}$

---

## Stars and Bars

$$x_1 + x_2 + \cdots + x_n = k, \quad x_i \geq 0 \implies C(n+k-1,\, k)$$
> [!Note] 💡 Equivalent Formulations
> The following all count the same thing $$= C(n+k-1,k)=C(n+k-1,n-1)$$
> **1.** Non-negative integer solutions to $x_1 + x_2 + \cdots + x_n = k$.
> **2.** $k$-combinations with repetition from $n$ elements.
> **3.** Ways to distribute $k$ identical objects to $n$ people.
> **4.** Ways to place $k$ identical books onto $n$ shelves.

| Constraint | Substitution | Result |
|-----------|-------------|--------|
| $x_i \geq 0$ | — | $C(n+k-1, k)$ |
| $x_i \geq 1$ | $y_i = x_i - 1$ | $C(k-1, n-1)$ |
| $x_i \geq c_i$ | $y_i = x_i - c_i$ | $C(n + k - \sum c_i - 1,\; n-1)$ |

> [!tip] Inequality trick
> $x_1 + \cdots + x_n \leq k$ — add slack variable $x_{n+1} \geq 0$:
> $$x_1 + \cdots + x_n + x_{n+1} = k \implies C(k+n,\, k)$$

---

## Functions $[m] \to [n]$

| Type | Count |
|------|-------|
| All functions | $n^m$ |
| Injective (1-1) | $P(n,m) = \dfrac{n!}{(n-m)!}$ |
| Surjective (onto) | $n!\cdot S(m,n)$ |
| Bijective | $n!$ (requires $m = n$) |

---

## Stirling Numbers of the 2nd Kind $S(n,k)$

$S(n,k)$ = partitions of $[n]$ into $k$ non-empty unordered blocks

$$S(n,k) = S(n-1,k-1) + k \cdot S(n-1,k)$$

| Special value | Formula |
|--------------|---------|
| $S(n,1)$ | $1$ |
| $S(n,n)$ | $1$ |
| $S(n,n-1)$ | $C(n,2)$ |
| $S(n,2)$ | $2^{n-1} - 1$ |

$$\text{Bell number: } B(n) = \sum_{k=1}^{n} S(n,k)$$

$$\text{Surjections } [m] \to [n] = n! \cdot S(m,n)$$

---

## Derangements

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} = n!\left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}\right)$$

$$D_n = (n-1)\bigl(D_{n-1} + D_{n-2}\bigr)$$

| $n$ | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|
| $D_n$ | 0 | 1 | 2 | 9 | 44 |

---

## Linear Recurrence Equations

A **linear recurrence of order $k$** has the form:

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k} + f(n)$$

- **Homogeneous:** $f(n) = 0$
- **Non-homogeneous:** $f(n) \neq 0$

---

## Solving Homogeneous Linear Recurrences

**Step 1 — Write the characteristic equation:**

$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \cdots - c_k = 0$$

**Step 2 — Find roots, then write general solution:**

| Root type | Contribution to $a_n$ |
|-----------|----------------------|
| Distinct real root $r$ | $A \cdot r^n$ |
| Repeated root $r$ of multiplicity $m$ | $(A_0 + A_1 n + \cdots + A_{m-1} n^{m-1})\, r^n$ |
| Conjugate complex roots $r e^{\pm i\theta}$ | $r^n(A\cos n\theta + B\sin n\theta)$ |

**Step 3 — Use initial conditions** to solve for constants $A, B, \ldots$

> [!example] Order-2 homogeneous — distinct roots
> $a_n = 5a_{n-1} - 4a_{n-2}$, $a_0 = 1$, $a_1 = 2$
> Characteristic equation: $r^2 - 5r + 4 = 0 \implies (r-1)(r-4) = 0 \implies r = 1, 4$
> General: $a_n = A \cdot 1^n + B \cdot 4^n$
> From ICs: $A + B = 1$, $A + 4B = 2$ → $B = \tfrac{1}{3}$, $A = \tfrac{2}{3}$
> $$\boxed{a_n = \tfrac{2}{3} + \tfrac{1}{3} \cdot 4^n}$$

> [!example] Repeated root
> $a_n = 6a_{n-1} - 9a_{n-2}$, $a_0 = 1$, $a_1 = 6$
> Characteristic: $r^2 - 6r + 9 = (r-3)^2 = 0 \implies r = 3$ (mult. 2)
> General: $a_n = (A + Bn)\cdot 3^n$
> From ICs: $A = 1$, $3A + 3B = 6 \implies B = 1$
> $$\boxed{a_n = (1+n)\cdot 3^n}$$

---

## Solving Non-Homogeneous Linear Recurrences

$$a_n^{(\text{general})} = a_n^{(\text{homogeneous})} + a_n^{(\text{particular})}$$

**Find $a_n^{(p)}$ by guessing based on $f(n)$:**

| $f(n)$ form | Guess for $a_n^{(p)}$ |
|------------|----------------------|
| Constant $d$ | $C$ (if $r=1$ not a root), else $Cn$ |
| $d \cdot s^n$ | $C \cdot s^n$ (if $s$ not a root), else $C \cdot n \cdot s^n$ |
| Degree-$t$ polynomial in $n$ | Degree-$t$ polynomial $C_0 + C_1 n + \cdots + C_t n^t$ |
| $s^n \cdot \text{poly}(n)$ | $s^n \cdot \text{poly}(n)$ (multiply by $n^m$ if $s$ is a root of mult. $m$) |

> [!example] Non-homogeneous — exponential RHS
> $a_n = 3a_{n-1} + 1$, $a_0 = 2$
> Homogeneous: $a_n^{(h)} = A \cdot 3^n$
> Particular (try $a_n^{(p)} = C$): $C = 3C + 1 \implies C = -\tfrac{1}{2}$
> General: $a_n = A \cdot 3^n - \tfrac{1}{2}$
> From IC: $A - \tfrac{1}{2} = 2 \implies A = \tfrac{5}{2}$
> $$\boxed{a_n = \tfrac{5}{2} \cdot 3^n - \tfrac{1}{2}}$$

> [!example] Non-homogeneous — $f(n) = b \cdot s^n$ where $s$ IS a root
> $u_{n+2} + 8u_{n+1} - 9u_n = 8 \cdot 3^{n+1}$, $u_0 = 2$, $u_1 = -6$
> Characteristic: $r^2 + 8r - 9 = (r+9)(r-1) = 0 \implies r = 1, -9$
> Homogeneous: $A \cdot 1^n + B \cdot (-9)^n$
> For particular: RHS $= 24 \cdot 3^n$, and $s=3$ is **not** a root, so try $C \cdot 3^n$:
> $C \cdot 3^{n+2} + 8C \cdot 3^{n+1} - 9C \cdot 3^n = 24 \cdot 3^n$
> $C(9 + 24 - 9) = 24 \implies C = 1$
> General: $u_n = A + B(-9)^n + 3^n$
> From ICs: $A + B + 1 = 2$ and $A - 9B + 3 = -6$ → $A = 1, B = 0$
> $$\boxed{u_n = 1 + 3^n}$$

---

## Solving Recurrences with Generating Functions

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

## Generating Functions (OGF)

$$G(x) = \sum_{n=0}^{\infty} a_n x^n$$

### Standard Correspondences

| Sequence                          | OGF                                     |
| --------------------------------- | --------------------------------------- |
| $(1,1,1,\ldots)$                  | $\dfrac{1}{1-x}$                        |
| $(1,r,r^2,\ldots)$                | $\dfrac{1}{1-rx}$<br>(geometric series) |
| $(1,0,1,0,\ldots)$                | $\dfrac{1}{1-x^2}$                      |
| $(C(n,0),\ldots,C(n,n),0,\ldots)$ | $(1+x)^n$                               |
| $C(n+k-1,k)$ for $k=0,1,\ldots$   | $\dfrac{1}{(1-x)^n}$                    |
| $(1,2,3,4,\ldots)$                | $\dfrac{1}{(1-x)^2}$                    |
| $(0,1,2,3,\ldots)$                | $\dfrac{x}{(1-x)^2}$                    |
| $(1,4,9,16,\ldots)$               | $\dfrac{1+x}{(1-x)^3}$                  |

### Operations

| Transform                             | OGF                                    |
| ------------------------------------- | -------------------------------------- |
| Right shift by $k$<br>Left shift by k | $x^k \cdot F(x)$<br>$\frac{F(x)}{x^k}$ |
| Scale by $b^n$                        | $F(bx)$                                |
| $(a_0, a_0{+}a_1, a_1{+}a_2, \ldots)$ | $\dfrac{F(x)}{1-x}$                    |
| $(a_1, a_2, a_3, \ldots)$             | $\dfrac{F(x) - a_0}{x}$                |
| Even-indexed terms only               | $\dfrac{F(x)+F(-x)}{2}$                |
| Convolution $c_n = \sum a_i b_{n-i}$  | $A(x) \cdot B(x)$                      |

---

## Solving Recurrences with GF

> [!tip] Method
> Multiply recurrence by $x^n$, sum over valid $n$, express in $F(x)$, solve algebraically, then partial-fraction decompose.

$$a_n = r \cdot a_{n-1} \implies F(x) = \frac{a_0}{1-rx} \implies a_n = a_0 \cdot r^n$$

$$\text{Fibonacci: } F(x) = \frac{x}{1-x-x^2}$$

**Characteristic roots:**

| Root type | General solution |
|-----------|----------------|
| Distinct roots $r_1, r_2$ | $a_n = A\,r_1^n + B\,r_2^n$ |
| Repeated root $r$ | $a_n = (A + Bn)\,r^n$ |

**Partial fractions:**
$$\frac{1}{(1-r_1 x)(1-r_2 x)} = \frac{A}{1-r_1 x} + \frac{B}{1-r_2 x} \implies a_n = A\,r_1^n + B\,r_2^n$$

---

## Closed Form: $k$-Combinations with Repetition

$$\text{Coeff of } x^k \text{ in } \frac{1}{(1-x)^n} = C(n+k-1,\, k)$$

This follows from the Maclaurin expansion of $\dfrac{1}{(1-x)^n}$.

---

## Distribution Summary

| Objects | Boxes | Constraint | Count |
|---------|-------|-----------|-------|
| distinct | distinct | none | $n^m$ |
| distinct | distinct | injective | $P(n,m)$ |
| distinct | distinct | surjective | $n! \cdot S(m,n)$ |
| distinct | identical | none | $\sum_{k=1}^{n} S(m,k)$ |
| distinct | identical | surjective | $S(m,n)$ |
| identical | distinct | none | $C(n+m-1, m)$ |
| identical | distinct | $\geq 1$ each | $C(m-1, n-1)$ |
| identical | identical | none | partitions of $m$ |
| identical | identical | $\geq 1$ each | partitions into $\leq n$ parts |

---

## Exam Tactics

> [!warning] Leave answers in exact form
> $C(n,k)$, $n!$, $\dfrac{n!}{r_1!\cdots r_k!}$, finite sums — full marks, no arithmetic needed.
