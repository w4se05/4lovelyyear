---
tags:
  - discrete-mathematics
  - generating-functions
  - recurrence-relations
  - permutations
  - stirling-numbers
  - inclusion-exclusion
  - derangements
topic: "Advanced Counting: Generating Functions, Recurrences, Permutation Structure & PIE"
course: DISCRETE MATHEMATICS
---

> [!Note] 💡 Notation Conventions
> - $[n] = \{1, 2, \ldots, n\}$ — the set of the first $n$ positive integers.
> - $n!$ — $n$ factorial, with $0! = 1$.
> - $C(n,k) = \binom{n}{k}$ — number of $k$-combinations of $n$ (without repetition).
> - $P(n,k) = \dfrac{n!}{(n-k)!}$ — number of $k$-permutations of $n$.
> - $S(m,n)$ — Stirling number of the **second** kind: number of ways to partition $[m]$ into $n$ non-empty unordered blocks.
> - $c(n,k)$ — **unsigned** Stirling number of the **first** kind: number of permutations of $[n]$ with exactly $k$ cycles.
> - $s(n,k) = (-1)^{n-k}\,c(n,k)$ — **signed** Stirling number of the first kind.
> - $\sigma$ — a **permutation** (bijection $[n] \to [n]$); $\sigma(i)$ is the image of $i$.
> - $\sigma \circ \tau$ (or $\sigma\tau$) — composition: $(\sigma \circ \tau)(x) = \sigma(\tau(x))$; apply $\tau$ first.
> - $\sigma^{-1}$ — the inverse permutation; $\text{id}$ — the identity permutation ($\text{id}(i)=i$).
> - $(a_0, a_1, \ldots)$ — a sequence of real numbers.
> - $G(x)$ or $F(x)$ — the ordinary generating function (OGF) for a sequence.
> - $f \leftrightarrow G(x)$ — correspondence between a sequence and its OGF.
> - $t_n$ — the $n$-th term of a sequence defined by a recurrence relation.
> - $p(x)$ — characteristic polynomial of a recurrence relation.
> - $D_n$ — number of derangements of $[n]$.
> - $\varphi(n)$ — Euler's phi (totient) function.

---

# Advanced Counting Techniques

---

# Part A — Generating Functions

---

## 1. Introduction to Generating Functions

> [!Definition] 📖 Ordinary Generating Function (OGF)
> The **ordinary generating function** for the sequence $(a_0, a_1, a_2, \ldots)$ of real numbers is the formal power series:
> $$G(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n + \cdots = \sum_{n=0}^{\infty} a_n x^n$$
> Here $x$ is treated as a **formal placeholder** — questions of convergence are ignored. Each sequence has a **unique** OGF.

> [!Note] 💡 Purpose
> Generating functions transform problems about sequences into problems about functions (algebraic manipulation), enabling:
> **1.** Efficient representation of counting sequences.
> **2.** Solving counting problems even when no closed formula is known in advance.
> **3.** Proving combinatorial identities.

---

## 2. Standard Generating Function Correspondences

> [!Property] ⚙️ Catalogue of Standard OGFs
> **1.** $(0, 0, 0, \ldots) \leftrightarrow 0$
>
> **2.** $(3, 2, 1, 0, 0, \ldots) \leftrightarrow 3 + 2x + x^2$
>
> **3.** $(1, 1, 1, \ldots) \leftrightarrow \dfrac{1}{1-x}$ (geometric series)
>
> **4.** $(1, -1, 1, -1, \ldots) \leftrightarrow \dfrac{1}{1+x}$
>
> **5.** $(1, r, r^2, r^3, \ldots) \leftrightarrow \dfrac{1}{1-rx}\quad\forall x \in \mathbb{R}$
>
> **6.** $(1, 0, 1, 0, \ldots) \leftrightarrow \dfrac{1}{1-x^2}$
>
> **7.** $(C(n,0),\, C(n,1),\, \ldots,\, C(n,n),\, 0, 0, \ldots) \leftrightarrow (1+x)^n$ (combinations without repetition) (Binomial Theorem)

---

## 3. Operations on Generating Functions

> [!Theorem] 📌 Scaling Rule
> If $(a_0, a_1, \ldots) \leftrightarrow F(x)$ and $c$ is a constant, then:
> $$(ca_0, ca_1, ca_2, \ldots) \leftrightarrow c \cdot F(x)$$

> [!Theorem] 📌 Addition Rule
> If $(a_0, a_1, \ldots) \leftrightarrow F(x)$ and $(b_0, b_1, \ldots) \leftrightarrow G(x)$, then:
> $$(a_0+b_0,\; a_1+b_1,\; \ldots,\; a_n+b_n,\; \ldots) \leftrightarrow F(x) + G(x)$$

> [!Theorem] 📌 Right Shifting Rule
> If $(a_0, a_1, a_2, \ldots) \leftrightarrow F(x)$, then for any integer $k \geq 1$:
> $$(\underbrace{0, 0, \ldots, 0}_{k}, a_0, a_1, a_2, \ldots) \leftrightarrow x^k F(x)$$
>
> **Example:** $(0, 0, 1, 1, 1, \ldots) \leftrightarrow \dfrac{x^2}{1-x}$

> [!Theorem] 📌 Differentiation Rule
> If $(a_0, a_1, a_2, \ldots) \leftrightarrow F(x)$, then:
> $$(a_1, 2a_2, 3a_3, \ldots, na_n, \ldots) \leftrightarrow F'(x)$$
>
> **Derived correspondences:**
>
> $(1, 2, 3, 4, \ldots) \leftrightarrow \left(\dfrac{1}{1-x}\right)' = \dfrac{1}{(1-x)^2}$
>
> $(0, 1, 2, 3, \ldots) \leftrightarrow \dfrac{x}{(1-x)^2}$ (apply right shift)
>
> $(1, 4, 9, 16, \ldots) \leftrightarrow \left(\dfrac{x}{(1-x)^2}\right)' = \dfrac{1+x}{(1-x)^3}$ (perfect squares)

> [!Theorem] 📌 Convolution Rule
> If $(a_0, a_1, \ldots) \leftrightarrow A(x)$ and $(b_0, b_1, \ldots) \leftrightarrow B(x)$, define:
> $$c_n = \sum_{i=0}^{n} a_i b_{n-i} = a_0 b_n + a_1 b_{n-1} + \cdots + a_n b_0$$
> Then $(c_0, c_1, c_2, \ldots) \leftrightarrow A(x) \cdot B(x)$.
>
> **Combinatorial interpretation:** If $A(x)$ is the OGF for selecting items from set $A$ and $B(x)$ for set $B$ (disjoint), then $A(x) \cdot B(x)$ is the OGF for selecting from $A \cup B$.

---

## 4. Combinatorial Applications of the Convolution Rule

### 4.1 Combinations Without Repetition

> [!Property] ⚙️ Binomial Coefficients via Convolution
> For each element $a_i$ in $\{a_1, \ldots, a_n\}$, the OGF for choosing $a_i$ at most once is $A_i(x) = 1 + x$.
> By the convolution rule applied $n$ times:
> $$\text{OGF for } k\text{-subsets of } \{a_1,\ldots,a_n\} = (1+x)^n$$
> The coefficient of $x^k$ in $(1+x)^n$ is $C(n,k)$. ✓

### 4.2 Combinations With Repetition

> [!Property] ⚙️ Combinations with Repetition
> For each element $a_i$, the OGF for choosing $a_i$ any number of times is $\dfrac{1}{1-x}$.
> By the convolution rule applied to all $n$ elements:
> $$\text{OGF for } k\text{-combinations with repetition from } n \text{ elements} = \frac{1}{(1-x)^n}$$
> The coefficient of $x^k$ gives $C(n+k-1, k)$.

### 4.3 Partitions of $n$

> [!Theorem] 📌 Generating Function for Partitions
> Let $p(n)$ denote the number of **integer partitions** of $n$ (ways to write $n$ as an unordered sum of positive integers). Then:
> $$P(x) = \sum_{n=0}^{\infty} p(n) x^n = \prod_{i=1}^{\infty} \frac{1}{1-x^i}$$

> [!Proof] 🔷 Proof Idea
> For each positive integer $i$, the OGF for the number of times $i$ appears as a part is:
> $$1 + x^i + x^{2i} + \cdots = \frac{1}{1-x^i}$$
> By the convolution rule (parts drawn from disjoint sets $\{1\}, \{2\}, \ldots$):
> $$P(x) = \prod_{i=1}^{\infty} \frac{1}{1-x^i} \qquad \blacksquare$$

> [!Property] ⚙️ Corollary — Bounded Partitions
> The OGF for the number of partitions of $n$ with **largest part at most $k$** is:
> $$\prod_{i=1}^{k} \frac{1}{1-x^i}$$

---

## 5. From Recurrences to Generating Functions

> [!Note] 💡 Method
> Given a recurrence, multiply both sides by $x^n$, sum over all valid $n$, apply the shift/addition rules to express everything in terms of $F(x)$, then solve algebraically.

> [!Example] 📘 Fibonacci OGF
> **Using:** Right Shifting Rule, Addition Rule
>
> **Recurrence:** $f_0 = 0$, $f_1 = 1$, $f_n = f_{n-1} + f_{n-2}$ for $n \geq 2$.
>
> **Step 1 — Write $F(x)$ using the recurrence:**
> $$F(x) \leftrightarrow (0, 1, f_0+f_1, f_1+f_2, \ldots, f_{n-2}+f_{n-1}, \ldots)$$
>
> **Step 2 — Decompose via addition rule:**
> $$\leftrightarrow (0, 1, 0, \ldots) + (0, 0, f_0, f_1, \ldots, f_{n-2}, \ldots) + (0, f_0, f_1, \ldots, f_{n-1}, \ldots)$$
>
> **Step 3 — Apply right shifting rule:**
> $$\leftrightarrow x + x^2 F(x) + x F(x)$$
>
> **Step 4 — Solve for $F(x)$:**
> $$F(x) = x + xF(x) + x^2 F(x)$$
> $$F(x)(1 - x - x^2) = x$$
> $$\boxed{F(x) = \frac{x}{1 - x - x^2}}$$

---

## 6. From Generating Functions to Closed Formulas

> [!Note] 💡 The core question
> Given a generating function $F(x) = \sum_{n=0}^{\infty} a_n x^n$, how do we recover the sequence term $a_n$ as a closed formula?
>
> There are two methods. They always give the same answer — they are just different tools.
>
> | | Method A | Method B |
> |---|---|---|
> | **Name** | Derivative formula | Maclaurin identity |
> | **Formula** | $a_n = \dfrac{F^{(n)}(0)}{n!}$ | Factor → partial fractions → read off $c^n$ |
> | **Best for** | Simple $F(x)$; understanding *why* | Rational $F(x)$; general closed formula |
> | **Avoid when** | Denominator is complicated | $F(x)$ involves $e^x$, $\sin x$, etc. |

---

> [!Note] 💡 Method A — the derivative formula $a_n = F^{(n)}(0)/n!$
>
> **Why it works — one idea at a time.**
>
> Start from the definition:
> $$F(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots$$
>
> **Setting $x = 0$** kills every term that has an $x$ in it, leaving only $a_0$:
> $$F(0) = a_0$$
>
> **Differentiating once** shifts all the coefficients down by one power:
> $$F'(x) = a_1 + 2a_2 x + 3a_3 x^2 + \cdots$$
> Now setting $x = 0$ isolates $a_1$: $\quad F'(0) = a_1$
>
> **Differentiating twice** and setting $x = 0$:
> $$F''(x) = 2a_2 + 6a_3 x + \cdots \implies F''(0) = 2a_2$$
>
> Notice: we got $2a_2$, not $a_2$. The factor $2$ appeared because the power rule
> on $x^2$ gives $2x$, and then $2 \cdot 1 = 2$ at $x=0$.
>
> **The general pattern.** Differentiating $x^n$ exactly $n$ times produces $n!$:
> $$x^n \;\to\; nx^{n-1} \;\to\; n(n-1)x^{n-2} \;\to\; \cdots \;\to\; n!$$
> So after $n$ differentiations, every term below degree $n$ has already vanished,
> every term above degree $n$ still has an $x$ (so it vanishes at $x = 0$), and the
> degree-$n$ term contributes exactly $n! \cdot a_n$:
> $$F^{(n)}(0) = n! \cdot a_n$$
> Dividing both sides by $n!$ (to undo the power-rule overcounting):
> $$\boxed{a_n = \frac{F^{(n)}(0)}{n!}}$$

---

> [!Note] 💡 Method B — the Maclaurin identity
>
> The single identity that powers this whole method:
> $$\frac{1}{1-cx} = \sum_{n=0}^{\infty} c^n x^n = 1 + cx + c^2x^2 + c^3x^3 + \cdots$$
> The coefficient of $x^n$ on the right is exactly $c^n$ — no derivatives needed.
>
> **Why we need fractions of the form $\dfrac{1}{1-cx}$:**
> The identity only works when the denominator is *linear* in $x$ with this exact shape.
> If $F(x)$ has a quadratic or higher denominator, we must break it into a sum of
> linear pieces first — that is what partial fractions does.
>
> **The four steps:**
> **1.** Factor the denominator of $F(x)$ into factors of the form $(1 - \alpha_i x)$.
> **2.** Write $F(x) = \dfrac{A_1}{1-\alpha_1 x} + \dfrac{A_2}{1-\alpha_2 x} + \cdots$ (partial fractions).
> **3.** Apply the identity to each fraction: $\dfrac{A_i}{1-\alpha_i x} = A_i \displaystyle\sum_{n=0}^\infty \alpha_i^n x^n$.
> **4.** Collect all $x^n$ terms: $a_n = A_1\alpha_1^n + A_2\alpha_2^n + \cdots$

---

> [!Example] 📘 Example — Simple case: $F(x) = \dfrac{1}{1-3x}$
> **Using both methods on the same function, to compare.**
>
> **Method A:**
>
> Find the pattern for the $n$-th derivative of $\dfrac{1}{1-3x}$ using the chain rule:
> $$F'(x) = \frac{3}{(1-3x)^2}, \quad F''(x) = \frac{3^2 \cdot 2!}{(1-3x)^3}, \quad \ldots \quad F^{(n)}(x) = \frac{3^n \cdot n!}{(1-3x)^{n+1}}$$
> Set $x = 0$:
> $$F^{(n)}(0) = 3^n \cdot n!$$
> Apply the formula:
> $$a_n = \frac{F^{(n)}(0)}{n!} = \frac{3^n \cdot n!}{n!} = \boxed{3^n}$$
>
> **Method B:**
>
> $F(x) = \dfrac{1}{1-3x}$ is already in the form $\dfrac{1}{1-cx}$ with $c = 3$.
> Apply the Maclaurin identity directly:
> $$F(x) = \sum_{n=0}^{\infty} 3^n x^n \implies \boxed{a_n = 3^n}$$
>
> Same answer. Method B needed one line; Method A needed a derivative pattern.
>
> **Verdict:** When $F(x)$ is already in the form $\dfrac{1}{1-cx}$, use Method B — it is immediate.
> Method A is useful here only to *understand why* the formula is valid.

---

> [!Example] 📘 Example — Fibonacci: $F(x) = \dfrac{x}{1-x-x^2}$
> **Using:** Method B (Method A is impractical here — the derivative pattern has no clean form)
>
> **Step 1 — Factor the denominator**
>
> We want $1 - x - x^2 = (1 - \alpha_1 x)(1-\alpha_2 x)$. Expanding the right side:
> $$(1-\alpha_1 x)(1-\alpha_2 x) = 1 - (\alpha_1+\alpha_2)x + \alpha_1\alpha_2\,x^2$$
> Matching with $1 - x - x^2$ gives the system:
> $$\alpha_1 + \alpha_2 = 1, \qquad \alpha_1 \alpha_2 = -1$$
> So $\alpha_1, \alpha_2$ are roots of $t^2 - t - 1 = 0$. By the quadratic formula:
> $$\alpha_1 = \frac{1+\sqrt{5}}{2}, \qquad \alpha_2 = \frac{1-\sqrt{5}}{2}$$
> Keep in mind: $\alpha_1 - \alpha_2 = \sqrt{5}$ — this appears in the next step.
>
> **Step 2 — Partial fraction decomposition**
>
> Write:
> $$\frac{x}{(1-\alpha_1 x)(1-\alpha_2 x)} = \frac{A}{1-\alpha_1 x} + \frac{B}{1-\alpha_2 x}$$
> Multiply both sides by $(1-\alpha_1 x)(1-\alpha_2 x)$:
> $$x = A(1-\alpha_2 x) + B(1-\alpha_1 x)$$
> **Solve for $A$:** set $x = 1/\alpha_1$ to zero out $B$:
> $$\frac{1}{\alpha_1} = A \cdot \frac{\alpha_1 - \alpha_2}{\alpha_1} \implies A = \frac{1}{\alpha_1 - \alpha_2} = \frac{1}{\sqrt{5}}$$
> **Solve for $B$:** set $x = 1/\alpha_2$ to zero out $A$:
> $$\frac{1}{\alpha_2} = B \cdot \frac{\alpha_2 - \alpha_1}{\alpha_2} \implies B = \frac{1}{\alpha_2 - \alpha_1} = -\frac{1}{\sqrt{5}}$$
> Result:
> $$F(x) = \frac{1}{\sqrt{5}} \cdot \frac{1}{1-\alpha_1 x} - \frac{1}{\sqrt{5}} \cdot \frac{1}{1-\alpha_2 x}$$
> Both fractions are now in the form $\dfrac{1}{1-cx}$.
>
> **Step 3 — Apply the Maclaurin identity to each fraction**
>
> $$\frac{1}{\sqrt{5}} \cdot \frac{1}{1-\alpha_1 x} = \frac{1}{\sqrt{5}}\sum_{n=0}^{\infty} \alpha_1^n\, x^n$$
> $$\frac{1}{\sqrt{5}} \cdot \frac{1}{1-\alpha_2 x} = \frac{1}{\sqrt{5}}\sum_{n=0}^{\infty} \alpha_2^n\, x^n$$
> Combining into one series:
> $$F(x) = \sum_{n=0}^{\infty} \frac{\alpha_1^n - \alpha_2^n}{\sqrt{5}}\, x^n$$
>
> **Step 4 — Read off the coefficient of $x^n$**
>
> $$\boxed{f_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]}$$
>
> **Verification:**
>
> | $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|---|
> | $f_n$ | 0 | 1 | 1 | 2 | 3 | 5 |
>
> **Why does an irrational formula give integers?**
> $\alpha_1$ and $\alpha_2$ are conjugate surds: $\alpha_1^n - \alpha_2^n$ is always an integer
> multiple of $\sqrt{5}$, so the $\sqrt{5}$ in the denominator cancels exactly for every $n$.

---

> [!Note] 💡 What about $e^x$, $\sin x$, $\ln(1+x)$?
> These are transcendental functions — their denominators cannot be factored, so
> Method B does not apply. Their series were derived *once* using Method A and are
> now standard results to memorise:
>
> $$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}, \qquad \sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \qquad \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$
> $$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n}$$
>
> In discrete mathematics, generating functions are almost always rational
> (polynomial over polynomial), so Method B covers nearly every problem you will see.

---
# Part B — Linear Recurrence Relations

---

## 7. Homogeneous Linear Recurrences

> [!Definition] 📖 Homogeneous Linear Recurrence
> A **homogeneous linear recurrence** of order $k$ has the form:
> $$a_0 t_n + a_1 t_{n-1} + \cdots + a_k t_{n-k} = 0$$
> where $a_0, a_1, \ldots, a_k$ are constants ($a_0 \neq 0$), and initial conditions $t_0, t_1, \ldots, t_{k-1}$ are given.

> [!Definition] 📖 Characteristic Polynomial
> The **characteristic polynomial** of the recurrence above is:
> $$p(x) = a_0 x^k + a_1 x^{k-1} + \cdots + a_k$$
> The roots of $p(x) = 0$ determine the form of all solutions.

> [!Theorem] 📌 Solution — Distinct Roots
> If $p(x)$ has exactly $k$ **distinct** roots $r_1, r_2, \ldots, r_k$, then the **general solution** is:
> $$t_n = \sum_{i=1}^{k} c_i r_i^n = c_1 r_1^n + c_2 r_2^n + \cdots + c_k r_k^n$$
> The constants $c_1, \ldots, c_k$ are determined by the $k$ initial conditions.

> [!Theorem] 📌 Solution — Repeated Roots
> If $p(x)$ has roots $r_1, r_2, \ldots, r_l$ with multiplicities $m_1, m_2, \ldots, m_l$ respectively (so $\sum m_i = k$), then the **general solution** is:
> $$t_n = \sum_{i=1}^{l} \sum_{j=0}^{m_i - 1} c_{i,j}\, n^j r_i^n$$
> That is, a root $r_i$ of multiplicity $m_i$ contributes the terms $c_{i,0} r_i^n + c_{i,1} n r_i^n + \cdots + c_{i,m_i-1} n^{m_i-1} r_i^n$.

> [!Note] 💡 Algorithm for Homogeneous Recurrences
> **1.** Write the characteristic polynomial $p(x)$.
> **2.** Factor $p(x)$; find all roots with multiplicities.
> **3.** Write the general solution using the template above.
> **4.** Substitute the $k$ initial conditions to solve for all constants $c_{i,j}$.

---

## 8. Non-Homogeneous Linear Recurrences

> [!Definition] 📖 Non-Homogeneous Linear Recurrence
> A **non-homogeneous** recurrence has the form:
> $$a_0 t_n + a_1 t_{n-1} + \cdots + a_k t_{n-k} = b^n p(n)$$
> where $b$ is a constant and $p(n)$ is a polynomial in $n$ of degree $d$.

> [!Theorem] 📌 Solution — Non-Homogeneous Case
> Form the **augmented characteristic polynomial**:
> $$(a_0 x^k + a_1 x^{k-1} + \cdots + a_k)(x - b)^{d+1}$$
> Then solve this expanded polynomial using the standard method (distinct/repeated roots) from Section 7.

> [!Note] 💡 Intuition
> The factor $(x-b)^{d+1}$ accounts for the particular solution forced by the right-hand side $b^n p(n)$. If $b$ is already a root of the homogeneous part with multiplicity $m$, then the total multiplicity of $b$ in the augmented polynomial becomes $m + d + 1$.

---

## 📘 Examples & Applications — Recurrences

> [!Example] 📘 Example 1: Homogeneous — Distinct Roots
> **Using:** Characteristic Polynomial, Distinct Roots Theorem
>
> **Problem:** Solve $t_n = 5t_{n-1} - 6t_{n-2}$ with $t_0 = 0$, $t_1 = 7$.
>
> **Step 1 — Rewrite in standard form and write characteristic polynomial:**
> $$t_n - 5t_{n-1} + 6t_{n-2} = 0 \implies p(x) = x^2 - 5x + 6 = (x-2)(x-3)$$
> Roots: $r_1 = 3$, $r_2 = 2$ (both distinct).
>
> **Step 2 — General solution:**
> $$t_n = c_1 \cdot 3^n + c_2 \cdot 2^n$$
>
> **Step 3 — Apply initial conditions:**
> $$n=0:\quad c_1 + c_2 = 0$$
> $$n=1:\quad 3c_1 + 2c_2 = 7$$
>
> **Step 4 — Solve:**
> From $c_2 = -c_1$: $3c_1 - 2c_1 = 7 \implies c_1 = 7$, $c_2 = -7$.
>
> $$\boxed{t_n = 7 \cdot 3^n - 7 \cdot 2^n}$$

> [!Example] 📘 Example 2: Homogeneous — Repeated Roots
> **Using:** Characteristic Polynomial, Repeated Roots Theorem
>
> **Problem:** Solve $t_n - 5t_{n-1} + 8t_{n-2} - 4t_{n-3} = 0$ with $t_0 = 0$, $t_1 = 1$, $t_2 = 2$.
>
> **Step 1 — Characteristic polynomial and factoring:**
> $$p(x) = x^3 - 5x^2 + 8x - 4 = (x-1)(x-2)^2$$
> Roots: $r_1 = 1$ (multiplicity 1), $r_2 = 2$ (multiplicity 2).
>
> **Step 2 — General solution:**
> $$t_n = c_1 \cdot 1^n + c_2 \cdot 2^n + c_3 \cdot n \cdot 2^n$$
>
> **Step 3 — Apply initial conditions:**
> $$n=0:\quad c_1 + c_2 = 0$$
> $$n=1:\quad c_1 + 2c_2 + 2c_3 = 1$$
> $$n=2:\quad c_1 + 4c_2 + 8c_3 = 2$$
>
> **Step 4 — Solve the system:**
> From row 1: $c_2 = -c_1$.
> Substitute into row 2: $c_1 - 2c_1 + 2c_3 = 1 \implies -c_1 + 2c_3 = 1$.
> Substitute into row 3: $c_1 - 4c_1 + 8c_3 = 2 \implies -3c_1 + 8c_3 = 2$.
> From these: $c_1 = -2$, $c_2 = 2$, $c_3 = -\tfrac{1}{2}$.
>
> $$\boxed{t_n = 2^{n+1} - n \cdot 2^{n-1} - 2}$$

> [!Example] 📘 Example 3: Non-Homogeneous Recurrence
> **Using:** Non-Homogeneous Characteristic Polynomial, Distinct Roots
>
> **Problem:** Solve $t_n - 2t_{n-1} = 3^n$ with initial value $t_0$ given.
>
> **Step 1 — Identify components:**
> Right-hand side $= 3^n \cdot 1$, so $b = 3$, $p(n) = 1$ (degree $d = 0$).
>
> **Step 2 — Augmented characteristic polynomial:**
> Homogeneous part gives $(x - 2)$; non-homogeneous contributes $(x-3)^{0+1} = (x-3)$.
> $$\text{Augmented: } (x-2)(x-3)$$
> Roots: $x = 2$, $x = 3$ (distinct).
>
> **Step 3 — General solution:**
> $$t_n = c_1 \cdot 2^n + c_2 \cdot 3^n$$
>
> **Step 4 — Find $t_1$ from recurrence and set up system:**
> $t_1 = 2t_0 + 3^1 = 2t_0 + 3$.
> $$n=0:\quad c_1 + c_2 = t_0$$
> $$n=1:\quad 2c_1 + 3c_2 = 2t_0 + 3$$
>
> **Step 5 — Solve:**
> Subtract first equation $\times 2$ from second: $c_2 = 3$.
> Then $c_1 = t_0 - 3$.
>
> $$\boxed{t_n = (t_0 - 3)\cdot 2^n + 3^{n+1}}$$
> Dominant term is $3^{n+1}$, so $t_n \in \Theta(3^n)$.

> [!Example] 📘 Example 4: Non-Homogeneous with $b=1$
> **Using:** Non-Homogeneous Characteristic Polynomial
>
> **Problem:** Solve $t_n - 2t_{n-1} = 1$ with $t_0 = 0$.
>
> **Step 1:** Right-hand side $= 1^n \cdot 1$, so $b=1$, $d=0$.
>
> **Step 2 — Augmented polynomial:**
> $(x-2)(x-1)$. Roots: $x=1$, $x=2$.
>
> **Step 3 — General solution:**
> $$t_n = c_1 \cdot 1^n + c_2 \cdot 2^n = c_1 + c_2 \cdot 2^n$$
>
> **Step 4 — Initial conditions:**
> $t_1 = 2t_0 + 1 = 1$.
> $$n=0:\quad c_1 + c_2 = 0$$
> $$n=1:\quad c_1 + 2c_2 = 1$$
> Solving: $c_1 = -1$, $c_2 = 1$.
>
> $$\boxed{t_n = 2^n - 1} \qquad t_n \in \Theta(2^n)$$

---

## 🗂️ Summary — Generating Functions & Recurrences

- **OGF:** $G(x) = \sum a_n x^n$; $x$ is a formal placeholder; each sequence has a unique OGF.
- **Scaling:** $c \cdot F(x) \leftrightarrow (ca_n)$. **Addition:** $F(x)+G(x) \leftrightarrow (a_n+b_n)$.
- **Right shift:** $x^k F(x)$ prepends $k$ zeros. **Differentiation:** $F'(x) \leftrightarrow (na_n)$ shifted left by 1.
- **Convolution:** $A(x)B(x) \leftrightarrow c_n = \sum_{i=0}^n a_i b_{n-i}$; models independent selection from disjoint sets.
- **Partitions:** $P(x) = \prod_{i=1}^\infty \frac{1}{1-x^i}$; bounded version truncates product at $k$.
- **Fibonacci OGF:** $F(x) = \dfrac{x}{1-x-x^2}$; closed formula uses partial fractions and golden ratio.
- **Homogeneous recurrence:** Write $p(x)$, factor, form $t_n = \sum c_{i,j} n^j r_i^n$, solve for constants.
- **Distinct roots $r_i$:** $t_n = \sum c_i r_i^n$. **Root of multiplicity $m$:** contributes $\sum_{j=0}^{m-1} c_j n^j r^n$.
- **Non-homogeneous ($b^n p(n)$):** Multiply characteristic polynomial by $(x-b)^{d+1}$, then solve normally.
- **Asymptotic behaviour:** The dominant root (largest $|r_i|$) determines the $\Theta$-class of $t_n$.

---

# Part C — Permutation Structure

---

## 9. Finite Functions — Summary

> [!Theorem] 📌 Counts of Functions $[m] \to [n]$
>
> | Type | Count |
> |---|---|
> | All functions | $n^m$ |
> | Injective (one-to-one) | $P(n,m) = \dfrac{n!}{(n-m)!}$ (zero if $m > n$) |
> | Surjective (onto) | $n! \cdot S(m,n)$ |
> | Bijections ($m=n$) | $n!$ |

> [!Proof] 🔷 Surjective Functions $[m] \to [n]$
> Let $f:[m]\to[n]$ be surjective. Define the **preimage partition**: $B_i = \{x \in [m] : f(x) = i\}$ for $i = 1, \ldots, n$.
>
> These sets satisfy: (i) $B_i \neq \emptyset$ (surjective), (ii) $B_i \cap B_j = \emptyset$ for $i \neq j$, (iii) $\bigcup B_i = [m]$.
>
> So $(B_1, \ldots, B_n)$ is an **ordered** partition of $[m]$ into $n$ non-empty blocks. There is a bijection:
> $$\{\text{surjections } f:[m]\to[n]\} \;\longleftrightarrow\; \{\text{ordered partitions of } [m] \text{ into } n \text{ blocks}\}$$
>
> Counting: $S(m,n)$ unordered partitions $\times$ $n!$ label assignments $= n! \cdot S(m,n)$. $\blacksquare$

---

## 10. Permutations on $[n]$

> [!Definition] 📖 Permutation
> A **permutation** on $[n]$ is a bijection $\sigma: [n] \to [n]$. The set of all permutations on $[n]$ is denoted $\mathfrak{S}_n$, and $|\mathfrak{S}_n| = n!$.

### 10.1 One-Line Notation

> [!Definition] 📖 One-Line Notation
> Write the **images** of $1, 2, \ldots, n$ in order:
> $$\sigma = \sigma(1)\; \sigma(2)\; \cdots\; \sigma(n)$$

### 10.2 Cycle Notation

> [!Definition] 📖 Cycle
> A **cycle** $(i_1\; i_2\; \cdots\; i_k)$ is the permutation:
> $$i_1 \mapsto i_2 \mapsto \cdots \mapsto i_k \mapsto i_1, \quad \text{all others fixed.}$$
> **Length $k$:** number of elements in the cycle.
> **Fixed point:** a cycle of length 1, written $(i)$; satisfies $\sigma(i) = i$.
> **Transposition:** a cycle of length 2.

> [!Theorem] 📌 Cycle Decomposition
> Every permutation $\sigma \in \mathfrak{S}_n$ decomposes **uniquely** into a product of disjoint cycles (up to order of cycles and cyclic rotation within each cycle).

> [!Note] 💡 Cycle Notation Conventions
> **1.** Order of disjoint cycles does not matter: $(1\;2\;5)(3\;4) = (3\;4)(1\;2\;5)$.
> **2.** Within a cycle, only circular order matters: $(1\;2\;5) = (2\;5\;1) = (5\;1\;2)$.
> **3.** Fixed points are sometimes omitted for brevity.

> [!Example] 📘 All Permutations of $[3]$ in Both Notations
>
> | One-line | Cycle Notation | Description |
> |---|---|---|
> | $1\;2\;3$ | $(1)(2)(3)$ | Identity — 3 fixed points |
> | $1\;3\;2$ | $(1)(2\;3)$ | Transposition of 2 and 3 |
> | $2\;1\;3$ | $(1\;2)(3)$ | Transposition of 1 and 2 |
> | $2\;3\;1$ | $(1\;2\;3)$ | 3-cycle |
> | $3\;1\;2$ | $(1\;3\;2)$ | 3-cycle (reverse direction) |
> | $3\;2\;1$ | $(1\;3)(2)$ | Transposition of 1 and 3 |

### 10.3 Composition ($\sigma^2$ and $\sigma \circ \tau$)

> [!Definition] 📖 Composition
> $(\sigma \circ \tau)(x) = \sigma(\tau(x))$ — apply $\tau$ first, then $\sigma$.
> $\sigma^2 = \sigma \circ \sigma$.

> [!Property] ⚙️ Squaring a Cycle
> For a $k$-cycle $(i_1\; i_2\; \cdots\; i_k)$:
> - If $k$ is **odd**: $\sigma^2$ is a single $k$-cycle.
> - If $k$ is **even**: $\sigma^2$ splits into **two** cycles of length $k/2$.

### 10.4 Inverse of a Permutation

> [!Definition] 📖 Inverse Permutation
> The **inverse** $\sigma^{-1}$ satisfies $\sigma \circ \sigma^{-1} = \text{id}$.
> **Rule:** Reverse each cycle:
> $$(i_1\; i_2\; \cdots\; i_k)^{-1} = (i_1\; i_k\; i_{k-1}\; \cdots\; i_2)$$
> Transpositions (length-2 cycles) are **self-inverse**.

---

## 11. Fixed Points and Derangements

> [!Definition] 📖 Fixed Point & Derangement
> - A **fixed point** of $\sigma$ is $i$ with $\sigma(i) = i$ (appears as $(i)$ in cycle notation).
> - A **derangement** is a permutation with **no fixed points**.
> - $D_n$ denotes the number of derangements of $[n]$.

> [!Theorem] 📌 Derangement Formula
> $$D_n = n!\sum_{k=0}^{n} \frac{(-1)^k}{k!} = n!\left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}\right)$$
> This is derived via the Principle of Inclusion-Exclusion (see Part D).

> [!Example] 📘 Small Values of $D_n$
> $D_1 = 0$, $D_2 = 1$, $D_3 = 2$, $D_4 = 9$.

---

## 12. Stirling Numbers of the First Kind

> [!Definition] 📖 Stirling Numbers of the First Kind
> $c(n,k)$ = number of permutations of $[n]$ with **exactly $k$ cycles** (unsigned Stirling number of the first kind).
> $$s(n,k) = (-1)^{n-k}\,c(n,k) \quad \text{(signed version)}$$

> [!Note] 💡 Comparison: First vs. Second Kind
>
> | | $S(n,k)$ — 2nd kind | $c(n,k)$ — 1st kind |
> |---|---|---|
> | **Counts** | Partitions of $[n]$ into $k$ blocks | Permutations of $[n]$ with $k$ cycles |
> | **Objects** | Set partitions | Bijections $[n]\to[n]$ |
> | **Recurrence** | $S(n-1,k-1) + k \cdot S(n-1,k)$ | $c(n-1,k-1) + (n-1) \cdot c(n-1,k)$ |

> [!Theorem] 📌 Recurrence for $c(n,k)$
> $$c(n,k) = c(n-1,\,k-1) + (n-1)\cdot c(n-1,\,k)$$
> with boundary conditions: $c(n,n) = 1$, $c(n,1) = (n-1)!$, $c(n,k) = 0$ for $k > n$.

> [!Proof] 🔷 Proof
> Consider where element $n$ appears in a permutation of $[n]$ with $k$ cycles:
>
> **Case 1:** $n$ forms a **fixed point** $(n)$ alone. The remaining $n-1$ elements must form $k-1$ cycles: $c(n-1, k-1)$ ways.
>
> **Case 2:** $n$ is **inserted into an existing cycle**. First form a permutation of $[n-1]$ with $k$ cycles: $c(n-1,k)$ ways. Then insert $n$ immediately after any of the $n-1$ existing elements (turning $\cdots \to i \to \cdots$ into $\cdots \to i \to n \to \cdots$): $n-1$ choices.
>
> By the sum rule: $c(n,k) = c(n-1,k-1) + (n-1)\cdot c(n-1,k)$. $\blacksquare$

> [!Theorem] 📌 Special Values of $c(n,k)$
> **1.** $c(n,1) = (n-1)!$ — permutations consisting of a single $n$-cycle (circular permutations).
>
> **2.** $c(n,n-1) = C(n,2)$ — exactly one transposition, rest are fixed points.
>
> **3.** $\displaystyle\sum_{k=1}^{n} c(n,k) = n!$ — every permutation has some cycle structure.

> [!Proof] 🔷 Proof of $c(n,1) = (n-1)!$
> A single $n$-cycle is a circular arrangement of $n$ elements. The number of distinct circular arrangements of $n$ elements is $(n-1)!$ (fix one element, arrange the rest). $\blacksquare$

> [!Proof] 🔷 Proof of $c(n,n-1) = C(n,2)$
> Having $n-1$ cycles with $n$ elements total forces exactly one cycle of length 2 and $n-2$ fixed points ($2 + (n-2)\cdot 1 = n$). Choose the 2 elements forming the transposition: $C(n,2)$ ways. $\blacksquare$

> [!Example] 📘 Table of $c(n,k)$ for Small $n$
>
> | $n \backslash k$ | 1 | 2 | 3 | 4 | Total |
> |---|---|---|---|---|---|
> | 1 | 1 | — | — | — | 1 |
> | 2 | 1 | 1 | — | — | 2 |
> | 3 | 2 | 3 | 1 | — | 6 |
> | 4 | 6 | 11 | 6 | 1 | 24 |

---

## 📘 Examples & Applications — Permutation Structure

> [!Example] 📘 Example 5: Full Cycle Analysis of $\sigma = 3\;6\;2\;1\;5\;8\;4\;7$
> **Using:** Cycle decomposition, inverse, composition ($\sigma^2$)
>
> **Step 1 — Cycle decomposition (trace orbits):**
> - Start at 1: $1\to3\to2\to6\to8\to7\to4\to1$. Cycle: $(1\;3\;2\;6\;8\;7\;4)$.
> - Start at 5: $5\to5$. Fixed point: $(5)$.
>
> $$\sigma = (1\;3\;2\;6\;8\;7\;4)(5)$$
>
> **Step 2 — Compute $\sigma^{-1}$ (reverse each cycle):**
> $$\sigma^{-1} = (1\;4\;7\;8\;6\;2\;3)(5)$$
> One-line: $\sigma^{-1} = 4\;3\;1\;7\;5\;2\;8\;6$.
>
> **Step 3 — Compute $\sigma^2$ (apply $\sigma$ twice):**
>
> | $x$ | $\sigma(x)$ | $\sigma^2(x)$ |
> |---|---|---|
> | 1 | 3 | 2 |
> | 2 | 6 | 8 |
> | 3 | 2 | 6 |
> | 4 | 1 | 3 |
> | 5 | 5 | 5 |
> | 6 | 8 | 7 |
> | 7 | 4 | 1 |
> | 8 | 7 | 4 |
>
> $\sigma^2 = 2\;8\;6\;3\;5\;7\;1\;4$ (one-line) $= (1\;2\;8\;4\;3\;6\;7)(5)$ (cycle).
> *Note:* The 7-cycle (odd length) squared gives a 7-cycle; the fixed point stays fixed.

> [!Example] 📘 Example 6: $\sigma = 3\;6\;1\;4\;5\;2$ on $[6]$
> **Using:** Cycle decomposition, transposition inverse, squaring even cycles
>
> **Cycle decomposition:**
> $1\to3\to1$: $(1\;3)$. $\quad 2\to6\to2$: $(2\;6)$. $\quad 4\to4$: $(4)$. $\quad 5\to5$: $(5)$.
>
> $$\sigma = (1\;3)(2\;6)(4)(5)$$
>
> **Inverse:** Each transposition is self-inverse, so $\sigma^{-1} = \sigma$.
>
> **Square:** $(1\;3)^2 = (1)(3)$ and $(2\;6)^2 = (2)(6)$, so:
> $$\sigma^2 = \text{id}$$

> [!Example] 📘 Example 7: Count Permutations of $[5]$ with Exactly 2 Cycles
> **Using:** Cycle structure enumeration, $c(n,k)$ recurrence
>
> Partitions of 5 into exactly 2 positive parts: $(1,4)$ and $(2,3)$.
>
> **Cycle type $(1,4)$:** Choose 1 fixed point: $C(5,1)=5$; remaining 4 form a 4-cycle: $(4-1)!=6$.
> Count: $5 \times 6 = 30$.
>
> **Cycle type $(2,3)$:** Choose 2 elements for the 2-cycle: $C(5,2)=10$; arrange them: 1 way (only one 2-cycle on 2 elements); remaining 3 form a 3-cycle: $(3-1)!=2$.
> Count: $10 \times 1 \times 2 = 20$.
>
> $$c(5,2) = 30 + 20 = 50$$
>
> **Verification via recurrence:**
> $c(5,2) = c(4,1) + 4\cdot c(4,2) = 6 + 4\times11 = 6 + 44 = 50$. ✓

> [!Example] 📘 Example 8: All Derangements of $[4]$
> **Using:** Fixed-point exclusion, cycle type enumeration
>
> Cycle types with no 1-cycles summing to 4: $(4)$ and $(2,2)$.
>
> **Type $(4)$ — one 4-cycle:** $(4-1)! = 6$ permutations.
> $(1\;2\;3\;4)$, $(1\;2\;4\;3)$, $(1\;3\;2\;4)$, $(1\;3\;4\;2)$, $(1\;4\;2\;3)$, $(1\;4\;3\;2)$.
>
> **Type $(2,2)$ — two 2-cycles:** Choose 2 elements for first 2-cycle: $C(4,2)/2 = 3$ (divide by 2 since the two 2-cycles are unordered).
> $(1\;2)(3\;4)$, $(1\;3)(2\;4)$, $(1\;4)(2\;3)$.
>
> $$D_4 = 6 + 3 = 9$$
>
> **Formula check:** $D_4 = 4!\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 24 \cdot \frac{9}{24} = 9$. ✓

---

## 🗂️ Summary — Permutation Structure

- **Permutation:** bijection $\sigma:[n]\to[n]$; $|\mathfrak{S}_n| = n!$.
- **One-line:** write $\sigma(1)\sigma(2)\cdots\sigma(n)$. **Cycle:** $(i_1\cdots i_k)$ means $i_1\to\cdots\to i_k\to i_1$.
- **Unique decomposition** into disjoint cycles; order of cycles and rotation within cycles are irrelevant.
- **Inverse:** reverse each cycle; transpositions are self-inverse.
- **Squaring:** odd-length $k$-cycle $\to$ $k$-cycle; even-length $k$-cycle $\to$ two $(k/2)$-cycles.
- **Fixed point:** $\sigma(i)=i$ — appears as $(i)$. **Derangement:** no fixed points; $D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!}$.
- **$c(n,k)$:** permutations of $[n]$ with exactly $k$ cycles; recurrence $c(n,k)=c(n-1,k-1)+(n-1)c(n-1,k)$.
- **Special values:** $c(n,1)=(n-1)!$; $c(n,n-1)=C(n,2)$; $c(n,n)=1$; $\sum_k c(n,k)=n!$.
- **Surjections:** $|\{\text{surjections }[m]\to[n]\}| = n!\cdot S(m,n)$.

---

# Part D — Principle of Inclusion-Exclusion (PIE)

---

## 13. Two-Set and Three-Set PIE

> [!Theorem] 📌 PIE for Two Sets
> For any two finite sets $A$ and $B$:
> $$|A \cup B| = |A| + |B| - |A \cap B|$$

> [!Theorem] 📌 PIE for Three Sets
> For any three finite sets $A$, $B$, $C$:
> $$|A \cup B \cup C| = |A| + |B| + |C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|$$

---

## 14. General PIE

> [!Theorem] 📌 General Principle of Inclusion-Exclusion
> For finite sets $A_1, A_2, \ldots, A_n$:
> $$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{i}|A_i| - \sum_{i<j}|A_i\cap A_j| + \sum_{i<j<k}|A_i\cap A_j\cap A_k| - \cdots + (-1)^{n-1}|A_1\cap\cdots\cap A_n|$$
> Equivalently, using subsets $S \subseteq [n]$, $S \neq \emptyset$:
> $$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{\emptyset \neq S \subseteq [n]} (-1)^{|S|-1} \left|\bigcap_{i\in S} A_i\right|$$

> [!Note] 💡 Complement Counting
> Often we want $|U \setminus (A_1 \cup \cdots \cup A_n)|$ (elements satisfying none of the properties):
> $$\left|U \setminus \bigcup_{i=1}^n A_i\right| = |U| - \left|\bigcup_{i=1}^n A_i\right|$$

---

## 15. Applications of PIE

### 15.1 Euler's Phi Function

> [!Definition] 📖 Euler's Phi Function
> $\varphi(n)$ = number of positive integers $\leq n$ that are **relatively prime** to $n$.

> [!Theorem] 📌 Formula for $\varphi(n)$
> Let $n = p_1^{k_1} p_2^{k_2} \cdots p_r^{k_r}$ be the prime factorisation of $n$. Then:
> $$\varphi(n) = n \prod_{i=1}^{r} \left(1 - \frac{1}{p_i}\right) = n - \sum_i \frac{n}{p_i} + \sum_{i<j}\frac{n}{p_i p_j} - \cdots + (-1)^r \frac{n}{p_1 p_2 \cdots p_r}$$

> [!Proof] 🔷 Proof Sketch
> Let $A_i = \{m \leq n : p_i \mid m\}$, so $|A_i| = \lfloor n/p_i \rfloor = n/p_i$ (exact for prime powers).
> By PIE: $|A_1 \cup \cdots \cup A_r| = \sum \frac{n}{p_i} - \sum \frac{n}{p_ip_j} + \cdots$
> So $\varphi(n) = n - |A_1\cup\cdots\cup A_r| = n\prod(1 - 1/p_i)$. $\blacksquare$

### 15.2 Number of Onto (Surjective) Functions

> [!Theorem] 📌 Surjective Functions via PIE
> The number of surjective functions from a set with $m$ elements to a set with $n$ elements ($m \geq n$) is:
> $$\sum_{j=0}^{n} (-1)^j \binom{n}{j}(n-j)^m = n^m - \binom{n}{1}(n-1)^m + \binom{n}{2}(n-2)^m - \cdots + (-1)^{n-1}\binom{n}{n-1} 1^m$$

> [!Proof] 🔷 Proof Hint
> Let $A_i$ = set of functions with no element mapping to $i$. Then $|A_i| = (n-1)^m$, $|A_i\cap A_j| = (n-2)^m$, etc.
> Surjections $= |U| - |A_1\cup\cdots\cup A_n|$, apply PIE. $\blacksquare$

### 15.3 Derangements

> [!Theorem] 📌 Number of Derangements
> The number of derangements of $[n]$ is:
> $$D_n = n!\left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}\right) = \sum_{k=0}^{n} (-1)^k \frac{n!}{k!}$$

> [!Proof] 🔷 Proof Hint
> Let $A_i$ = set of permutations where $\sigma(i) = i$ (element $i$ is fixed).
> $|A_i| = (n-1)!$; $|A_i\cap A_j|=(n-2)!$; generally $|\bigcap_{i\in S}A_i| = (n-|S|)!$.
> By PIE: $|A_1\cup\cdots\cup A_n| = \sum_{k=1}^n(-1)^{k-1}\binom{n}{k}(n-k)!$
> $D_n = n! - |A_1\cup\cdots\cup A_n| = \sum_{k=0}^n(-1)^k\frac{n!}{k!}$. $\blacksquare$

---

## 📘 Examples & Applications — PIE

> [!Example] 📘 Example 9: Binary Strings Starting with 1 or Ending with 01
> **Using:** PIE for two sets
>
> Let $A$ = binary strings of length $n$ starting with $1$; $B$ = ending with $01$.
> $|A| = 2^{n-1}$, $|B| = 2^{n-2}$, $|A\cap B| = 2^{n-3}$ (for $n \geq 3$).
>
> $$|A\cup B| = 2^{n-1} + 2^{n-2} - 2^{n-3} = 5\cdot 2^{n-3}$$

> [!Example] 📘 Example 10: Integers Relatively Prime to 70 in $[1, 150]$
> **Using:** PIE for three sets, Euler's phi setup
>
> $70 = 2 \cdot 5 \cdot 7$.
> Let $U = \{1,\ldots,150\}$; $A = \{n \in U : 2\mid n\}$; $B = \{n : 5\mid n\}$; $C = \{n : 7\mid n\}$.
>
> $$|A| = 75,\quad |B| = 30,\quad |C| = 21$$
> $$|A\cap B| = \lfloor 150/10\rfloor = 15,\quad |A\cap C| = \lfloor 150/14\rfloor = 10,\quad |B\cap C| = \lfloor 150/35\rfloor = 4$$
> $$|A\cap B\cap C| = \lfloor 150/70\rfloor = 2$$
>
> By PIE:
> $$|A\cup B\cup C| = 75+30+21-15-10-4+2 = 99$$
> $$|U\setminus(A\cup B\cup C)| = 150 - 99 = \boxed{51}$$

> [!Example] 📘 Example 11: $\varphi(n)$ Computations
> **Using:** Euler's phi formula
>
> $\varphi(8) = 8\left(1-\frac{1}{2}\right) = 4$.
>
> $\varphi(15) = 15\left(1-\frac{1}{3}\right)\left(1-\frac{1}{5}\right) = 15 \cdot \frac{2}{3} \cdot \frac{4}{5} = 8$.

> [!Example] 📘 Example 12: Surjections from $[7]$ to $[5]$
> **Using:** Surjection formula via PIE
>
> $$\text{Surjections} = \sum_{j=0}^{5}(-1)^j\binom{5}{j}(5-j)^7$$
> $$= 5^7 - \binom{5}{1}4^7 + \binom{5}{2}3^7 - \binom{5}{3}2^7 + \binom{5}{4}1^7 - \binom{5}{5}0^7$$
> $$= 78125 - 5\cdot16384 + 10\cdot2187 - 10\cdot128 + 5\cdot1 - 0$$
> $$= 78125 - 81920 + 21870 - 1280 + 5 = 16800$$

> [!Example] 📘 Example 13: Non-Negative Integer Solutions with Bounds
> **Using:** Stars-and-bars, PIE for upper bound constraints
>
> **Problem:** Count non-negative integer solutions to $x + y + z = 13$ with $0 \leq x, y, z \leq 6$.
>
> **Unconstrained count** (stars and bars): $\binom{13+2}{2} = \binom{15}{2} = 105$.
>
> Let $A_x$ = solutions with $x \geq 7$ (substitute $x' = x-7$: solve $x'+y+z=6$): $\binom{8}{2}=28$. By symmetry $|A_y|=|A_z|=28$.
>
> $A_x\cap A_y$: $x\geq7,y\geq7 \implies$ sum $\geq 14 > 13$: $|A_x\cap A_y|=0$. Similarly all pairwise and triple intersections are 0.
>
> $$\text{Answer} = 105 - 3\cdot28 + 0 = 105 - 84 = \boxed{21}$$

---

## 🗂️ Summary — Principle of Inclusion-Exclusion

- **2-set PIE:** $|A\cup B| = |A|+|B|-|A\cap B|$.
- **3-set PIE:** $|A\cup B\cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|$.
- **General PIE:** alternating sum over all non-empty subsets of the index set; sign is $(-1)^{|S|-1}$.
- **Complement counting:** $|U\setminus\bigcup A_i| = |U| - |\bigcup A_i|$ — used when "none of the properties" is desired.
- **Euler's phi:** $\varphi(n) = n\prod_{p\mid n, p \text{ prime}}(1 - 1/p)$.
- **Surjection count:** $\sum_{j=0}^{n}(-1)^j\binom{n}{j}(n-j)^m$.
- **Derangements:** $D_n = \sum_{k=0}^{n}(-1)^k\frac{n!}{k!} = n!\sum_{k=0}^n\frac{(-1)^k}{k!}$.
- **Strategy tip:** To count elements satisfying none of $n$ properties $P_1,\ldots,P_n$: define $A_i$ = elements satisfying $P_i$, compute $|A_1\cup\cdots\cup A_n|$ via PIE, subtract from $|U|$.
