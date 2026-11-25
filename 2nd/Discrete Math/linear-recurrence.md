---
tags: [discrete-math, recurrence, exam-prep]
topic: Linear Recurrence Relations
course: Discrete Mathematics
status: ready
---

# 📐 Linear Recurrence Relations

> [!tip] Big picture
> Every linear recurrence solution has the same skeleton:
> $$a_n = a_n^{(h)} + a_n^{(p)}$$
> For **homogeneous** recurrences, $a_n^{(p)} = 0$ — you only need the left half.

---

## 1 — Homogeneous Recurrences

> [!info] 🔖 Form
> $$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k}$$
> Nothing on the right except previous terms.

### Step-by-step

> [!example] ✏️ Template problem
> $a_0 = 1,\ a_1 = 2,\quad a_n = 5a_{n-1} - 4a_{n-2}$

**Step 1 — Write the characteristic equation**

Replace $a_n \to r^n$, divide by the lowest power of $r$:

$$r^n = 5r^{n-1} - 4r^{n-2} \;\Longrightarrow\; r^2 - 5r + 4 = 0$$

**Step 2 — Find the roots**

Factor or use the quadratic formula:

$$(r-1)(r-4) = 0 \quad\Longrightarrow\quad r_1 = 1,\; r_2 = 4$$

**Step 3 — Write the general solution**

| Root situation | General solution |
|---|---|
| Two distinct roots $r_1, r_2$ | $a_n = A \cdot r_1^n + B \cdot r_2^n$ |
| One repeated root $r$ (double) | $a_n = A \cdot r^n + B \cdot n \cdot r^n$ |
| One repeated root $r$ (triple) | $a_n = A \cdot r^n + B \cdot n \cdot r^n + C \cdot n^2 \cdot r^n$ |

For the template: $a_n = A \cdot 1^n + B \cdot 4^n = A + B \cdot 4^n$

**Step 4 — Apply initial conditions**

$$n=0:\quad A + B = 1$$
$$n=1:\quad A + 4B = 2$$
$$\Longrightarrow\; 3B = 1 \;\Longrightarrow\; B = \tfrac{1}{3},\; A = \tfrac{2}{3}$$

$$\boxed{a_n = \dfrac{2}{3} + \dfrac{4^n}{3}}$$

---

### Worked exercises (Sec. 2, Problem 10)

> [!example] ✏️ 10(a) — $a_0 = 2,\quad a_n = 3a_{n-1}$
>
> Char. eq: $r - 3 = 0 \Rightarrow r = 3$
>
> General: $a_n = A \cdot 3^n$
>
> IC $a_0 = 2$: $A = 2$
>
> $$\boxed{a_n = 2 \cdot 3^n}$$

> [!example] ✏️ 10(c) — $a_0 = 1,\ a_1 = 2,\quad a_n = 5a_{n-1} - 4a_{n-2}$
>
> Char. eq: $r^2 - 5r + 4 = 0 \Rightarrow r = 1,\, r = 4$
>
> General: $a_n = A + B \cdot 4^n$
>
> ICs: $A + B = 1$, $A + 4B = 2$ $\Rightarrow$ $B = \tfrac{1}{3}$, $A = \tfrac{2}{3}$
>
> $$\boxed{a_n = \dfrac{2}{3} + \dfrac{4^n}{3}}$$

---

## 2 — Non-Homogeneous Recurrences

> [!info] 🔖 Form
> $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + f(n)$$
> There is an extra term $f(n) \neq 0$ on the right.

### Step-by-step

> [!example] ✏️ Template problem
> $u_0 = 2,\ u_1 = -6,\quad u_{n+2} + 8u_{n+1} - 9u_n = 8 \cdot 3^{n+1}$

**Step 1 — Solve the homogeneous part**

Strip $f(n)$, solve $u_{n+2} + 8u_{n+1} - 9u_n = 0$:

$$r^2 + 8r - 9 = 0 \;\Longrightarrow\; (r+9)(r-1) = 0 \;\Longrightarrow\; r_1 = 1,\; r_2 = -9$$

$$u_n^{(h)} = A + B(-9)^n$$

**Step 2 — Guess the particular solution**

> [!warning] ⚠️ Conflict rule
> If your guess has the same form as any term already in $u_n^{(h)}$, multiply the guess by $n$. If it conflicts again, multiply by $n^2$.

| $f(n)$ shape | Guess for $u_n^{(p)}$ | Conflict → multiply by |
|---|---|---|
| Constant $c$ | $C$ | $n$ (if $r=1$ is a root) |
| $b^n$ | $C \cdot b^n$ | $n \cdot b^n$ (if $b$ is a root) |
| Degree-$d$ polynomial | $C_d n^d + \cdots + C_0$ | multiply whole guess by $n$ |
| $b^n \cdot \text{poly}(n)$ | $(C_d n^d + \cdots + C_0) \cdot b^n$ | multiply by $n$ |

For the template: $f(n) = 8 \cdot 3^{n+1} = 24 \cdot 3^n$. Since $3 \neq 1$ and $3 \neq -9$, guess $u_n^{(p)} = C \cdot 3^n$.

**Step 3 — Substitute and solve for constants**

$$C \cdot 3^{n+2} + 8C \cdot 3^{n+1} - 9C \cdot 3^n = 24 \cdot 3^n$$

Divide by $3^n$:

$$9C + 24C - 9C = 24 \;\Longrightarrow\; 24C = 24 \;\Longrightarrow\; C = 1$$

$$u_n^{(p)} = 3^n$$

**Step 4 — Combine and apply ICs**

$$u_n = u_n^{(h)} + u_n^{(p)} = A + B(-9)^n + 3^n$$

$$n=0:\quad A + B + 1 = 2 \;\Longrightarrow\; A + B = 1$$
$$n=1:\quad A - 9B + 3 = -6 \;\Longrightarrow\; A - 9B = -9$$

Subtract: $10B = 10 \Rightarrow B = 1,\; A = 0$

$$\boxed{u_n = (-9)^n + 3^n}$$

---

### Worked exercises (Sec. 2, Problem 10)

> [!example] ✏️ 10(b) — $a_0 = 2,\quad a_n = 3a_{n-1} + 1$
>
> **Homo:** $r = 3 \Rightarrow a_n^{(h)} = A \cdot 3^n$
>
> **Particular:** $f(n) = 1$ (constant). Since $r=1$ is NOT a root, guess $C$.
>
> Sub: $C = 3C + 1 \Rightarrow -2C = 1 \Rightarrow C = -\tfrac{1}{2}$
>
> **Total:** $a_n = A \cdot 3^n - \tfrac{1}{2}$
>
> IC $a_0 = 2$: $A - \tfrac{1}{2} = 2 \Rightarrow A = \tfrac{5}{2}$
>
> $$\boxed{a_n = \dfrac{5}{2} \cdot 3^n - \dfrac{1}{2}}$$

> [!example] ✏️ 10(d) — $u_0 = 2,\ u_1 = -6,\quad u_{n+2} + 8u_{n+1} - 9u_n = 8 \cdot 3^{n+1}$
>
> (Full worked solution in the step-by-step above.)
>
> $$\boxed{u_n = (-9)^n + 3^n}$$

> [!example] ✏️ 10(e) — $u_0 = 1,\quad u_{n+1} - 2u_n = 4^n$
>
> **Homo:** $r = 2 \Rightarrow u_n^{(h)} = A \cdot 2^n$
>
> **Particular:** $f(n) = 4^n$, and $4 \neq 2$, so guess $C \cdot 4^n$.
>
> Sub: $C \cdot 4^{n+1} - 2C \cdot 4^n = 4^n \Rightarrow 4C - 2C = 1 \Rightarrow C = \tfrac{1}{2}$
>
> **Total:** $u_n = A \cdot 2^n + \tfrac{4^n}{2}$
>
> IC $u_0 = 1$: $A + \tfrac{1}{2} = 1 \Rightarrow A = \tfrac{1}{2}$
>
> $$\boxed{u_n = \dfrac{2^n}{2} + \dfrac{4^n}{2} = 2^{n-1} + \dfrac{4^n}{2}}$$

> [!example] ✏️ 10(f) — $q_{n+1} = 4^n + 2q_n$, words of length $n$ over $\{a,b,c,d\}$ with odd number of b's
>
> **Homo:** $r = 2 \Rightarrow q_n^{(h)} = A \cdot 2^n$
>
> **Particular:** $f(n) = 4^n$, guess $C \cdot 4^n$.
>
> Sub: $C \cdot 4^{n+1} - 2C \cdot 4^n = 4^n \Rightarrow 2C = 1 \Rightarrow C = \tfrac{1}{2}$
>
> **Total:** $q_n = A \cdot 2^n + \tfrac{4^n}{2}$
>
> IC $q_0 = 0$ (empty word has 0 b's, which is even — so 0 valid words):
> $A + \tfrac{1}{2} = 0 \Rightarrow A = -\tfrac{1}{2}$
>
> $$\boxed{q_n = \dfrac{4^n - 2^n}{2}}$$

---

## 3 — Quick Reference

> [!summary] 🗂️ Decision flowchart
>
> 1. Is there an $f(n)$?
>    - **No** → homogeneous, skip to char. eq
>    - **Yes** → non-homogeneous, do homo part first
> 2. Solve char. eq → roots
> 3. Repeated root of multiplicity $m$? → multiply that term by $n, n^2, \ldots, n^{m-1}$
> 4. Pick particular guess from the table
> 5. Does guess clash with homo solution? → multiply guess by $n$
> 6. Substitute guess → find constants
> 7. Combine → apply ICs → done

> [!warning] ⚠️ Common mistakes
> - Applying initial conditions to just $a_n^{(h)}$ before adding $a_n^{(p)}$ — always combine first
> - Forgetting the conflict rule when $f(n) = c$ and $r=1$ is a root
> - Sign errors when rearranging the characteristic equation (move everything to one side)
