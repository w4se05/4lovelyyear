## 1. Maximum and Minimum Values (Conceptual)

### Definitions and Theorems

> [!Definition] Absolute vs. Local Extrema
> Let $c$ be a number in the domain $D$ of a function $f$.
> * **Absolute Maximum:** $f(c) \ge f(x)$ for all $x$ in $D$.
> * **Absolute Minimum:** $f(c) \le f(x)$ for all $x$ in $D$.
> * **Local Maximum:** $f(c) \ge f(x)$ when $x$ is *near* $c$.
> * **Local Minimum:** $f(c) \le f(x)$ when $x$ is *near* $c$.

> [!Theorem] The Extreme Value Theorem (EVT)
> If $f$ is **continuous** on a **closed interval** $[a, b]$, then $f$ attains an absolute maximum value $f(c)$ and an absolute minimum value $f(d)$ at some numbers $c$ and $d$ in $[a, b]$.

> [!Theorem] Fermat's Theorem
> If $f$ has a local maximum or minimum at $c$, and if $f'(c)$ exists, then **$f'(c) = 0$**.
> * *Warning:* The converse is false. $f'(c) = 0$ does not guarantee a max/min (e.g., $y=x^3$ at $0$).

> [!Definition] Critical Number
> A **critical number** of a function $f$ is a number $c$ in the domain of $f$ such that either:
> 1.  $f'(c) = 0$, or
> 2.  $f'(c)$ does not exist.

### The Closed Interval Method
To find the **absolute** max and min values of a continuous function $f$ on a closed interval $[a, b]$:
1.  Find the values of $f$ at the **critical numbers** in $(a, b)$.
2.  Find the values of $f$ at the **endpoints** ($a$ and $b$).
3.  The largest value is the absolute max; the smallest is the absolute min.

---

## 2. The Mean Value Theorem (Conceptual)

> [!Theorem] Rolle's Theorem (EVT - Extreme Value Theorem)
> Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
> If **$f(a) = f(b)$**, then there exists a number $c$ in $(a, b)$ such that **$f'(c) = 0$**.

> [!Theorem] The Mean Value Theorem (MVT)
> Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
> Then there exists a number $c$ in $(a, b)$ such that:
> $$f'(c) = \frac{f(b) - f(a)}{b - a}$$
> * **Geometric Interpretation:** There is a tangent line at $c$ parallel to the secant line connecting $(a, f(a))$ and $(b, f(b))$ .

---

## 3. Derivatives and Graphs (Teach Mode)

### Increasing/Decreasing Test
* If $f'(x) > 0$ on an interval, then $f$ is **increasing** on that interval.
* If $f'(x) < 0$ on an interval, then $f$ is **decreasing** on that interval.

### Concavity Test
* If $f''(x) > 0$ for all $x$ in $I$, the graph of $f$ is **concave upward** on $I$ (shaped like a cup $\cup$).
* If $f''(x) < 0$ for all $x$ in $I$, the graph of $f$ is **concave downward** on $I$ (shaped like a frown $\cap$).

> [!Definition] Inflection Point
> A point $P$ on a curve $y = f(x)$ is called an **inflection point** if $f$ is continuous there and the curve changes from concave upward to concave downward or vice versa.

### Tests for Local Extrema

> [!Method] The First Derivative Test
> Suppose $c$ is a critical number of a continuous function $f$.
> * If $f'$ changes from **positive to negative** at $c$, then $f$ has a **local maximum** at $c$.
> * If $f'$ changes from **negative to positive** at $c$, then $f$ has a **local minimum** at $c$.
> * If $f'$ does not change sign, $f$ has no local extremum at $c$.

> [!Method] The Second Derivative Test
> Suppose $f''$ is continuous near $c$.
> * If $f'(c) = 0$ and **$f''(c) > 0$**, then $f$ has a **local minimum** at $c$ (concave up).
> * If $f'(c) = 0$ and **$f''(c) < 0$**, then $f$ has a **local maximum** at $c$ (concave down).

---

## 4. L'Hospital's Rule (Indeterminate Forms)

> [!Theorem] L'Hospital's Rule
> Suppose $f$ and $g$ are differentiable and $g'(x) \neq 0$. If $\lim_{x \to a} \frac{f(x)}{g(x)}$ produces an indeterminate form of type **$\frac{0}{0}$** or **$\frac{\infty}{\infty}$**, then:
> $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
> provided the limit on the right exists (or is $\pm \infty$).

**Other Indeterminate Forms:**
* **Products ($0 \cdot \infty$):** Write $fg$ as $\frac{f}{1/g}$ or $\frac{g}{1/f}$ to get $\frac{0}{0}$ or $\frac{\infty}{\infty}$.
* **Differences ($\infty - \infty$):** Combine fractions using a common denominator or simplify.
* **Powers ($0^0, \infty^0, 1^\infty$):** Use natural logarithms: Let $y = [f(x)]^{g(x)}$, then $\ln y = g(x) \ln f(x)$. Find $\lim \ln y$, then exponentiate.

---

## 5. Optimization & Antiderivatives (Conceptual)

### Optimization Problems
**Steps to Solve:**
1.  **Understand:** Draw a diagram, introduce notation .
2.  **Express:** Write a formula for the quantity $Q$ to be maximized/minimized.
3.  **Constraint:** Use given conditions to express $Q$ as a function of **one variable**.
4.  **Domain:** Identify the domain of this function.
5.  **Solve:** Find absolute extrema (usually finding critical numbers $f'=0$).

### Newton's Method
A numerical method to approximate roots of $f(x) = 0$.
**Formula:**
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
Start with an initial guess $x_1$ and iterate.

### Antiderivatives
> [!Definition] Antiderivative
> A function $F$ is an antiderivative of $f$ on an interval $I$ if $F'(x) = f(x)$ for all $x$ in $I$.
> **General Form:** $F(x) + C$, where $C$ is an arbitrary constant .

**Rectilinear Motion Application:**
* Given acceleration $a(t)$, integrate to get velocity $v(t) = \int a(t) dt$.
* Integrate velocity to get position $s(t) = \int v(t) dt$.

---

## 📘 Examples & Applications (Exam Mode)

### Example 1: Finding Absolute Extrema
> [!Example] Problem
> Find the absolute max and min of $f(x) = x^3 - 3x^2 + 1$ on $[-\frac{1}{2}, 4]$.
> **Using:** Closed Interval Method.
>
> **Step 1:** Find critical numbers.
> $$f'(x) = 3x^2 - 6x = 3x(x - 2)$$
> $f'(x) = 0$ implies $x = 0$ and $x = 2$. Both are in the interval.
>
> **Step 2:** Evaluate $f$ at critical numbers.
> $f(0) = 1$.
> $f(2) = 2^3 - 3(2)^2 + 1 = 8 - 12 + 1 = -3$.
>
> **Step 3:** Evaluate $f$ at endpoints.
> $f(-\frac{1}{2}) = (-\frac{1}{2})^3 - 3(-\frac{1}{2})^2 + 1 = -\frac{1}{8} - \frac{3}{4} + 1 = \frac{1}{8}$.
> $f(4) = 4^3 - 3(4)^2 + 1 = 64 - 48 + 1 = 17$.
>
> **Conclusion:**
> * **Absolute Max:** $f(4) = 17$.
> * **Absolute Min:** $f(2) = -3$.

### Example 2: Curve Sketching
> [!Example] Problem
> Sketch the graph of $f(x)$ given $f'(x) > 0$ for $|x| < 2$, $f'(x) < 0$ for $|x| > 2$, $f''(-2) = 0$, $f''(2) = 0$, $f''(x) < 0$ for $x > 2$.
> **Analysis:**
> * **Increasing:** On $(-2, 2)$.
> * **Decreasing:** On $(-\infty, -2)$ and $(2, \infty)$.
> * **Extrema:** Local min at $x=-2$, local max at $x=2$ (First Derivative Test).
> * **Concavity:** Since $f''(x) < 0$ for $x > 2$, it is concave down on $(2, \infty)$ .

### Example 3: L'Hospital's Rule
> [!Example] Problem
> Evaluate $\lim_{x \to \infty} \frac{\ln x}{x - 1}$.
> **Using:** L'Hospital's Rule ($\frac{\infty}{\infty}$ form).
>
> **Step 1:** Check form.
> $\ln \infty = \infty$, $\infty - 1 = \infty$. Form is $\frac{\infty}{\infty}$.
>
> **Step 2:** Apply Rule.
> $$\lim_{x \to \infty} \frac{\frac{d}{dx}(\ln x)}{\frac{d}{dx}(x - 1)} = \lim_{x \to \infty} \frac{1/x}{1} = \lim_{x \to \infty} \frac{1}{x}$$
>
> **Step 3:** Evaluate.
> $$= 0$$

### Example 4: Optimization (Cylindrical Can)

> [!Example] Problem
> Minimize the cost of metal to make a cylindrical can that holds $1$ L ($1000 \text{ cm}^3$).
> **Using:** Optimization Algorithm.
>
> **Step 1:** Formulate equations.
> Volume $V = \pi r^2 h = 1000 \implies h = \frac{1000}{\pi r^2}$.
> Surface Area (Cost) $A = 2\pi r^2 + 2\pi r h$ (Top/Bottom + Side).
>
> **Step 2:** Substitute constraint ($h$) into Objective ($A$).
> $$A(r) = 2\pi r^2 + 2\pi r \left( \frac{1000}{\pi r^2} \right) = 2\pi r^2 + \frac{2000}{r}$$
> Domain: $r > 0$.
>
> **Step 3:** Differentiate.
> $$A'(r) = 4\pi r - \frac{2000}{r^2}$$
> Set $A'(r) = 0$:
> $$4\pi r = \frac{2000}{r^2} \implies r^3 = \frac{500}{\pi} \implies r = \sqrt[3]{\frac{500}{\pi}}$$
>
> **Step 4:** Verify Minimum.
> $A''(r) = 4\pi + \frac{4000}{r^3} > 0$ for $r > 0$.
> By 2nd Derivative Test, this $r$ gives a minimum.

---

## 6. Summary Recap

| Concept | Condition/Formula | Implication |
| :--- | :--- | :--- |
| **Critical Number** | $f'(c)=0$ or DNE | Potential local extremum. |
| **EVT** | Continuous on $[a, b]$ | Guaranteed Abs Max & Min. |
| **MVT** | Continuous $[a, b]$, Diff $(a, b)$ | Inst. Rate = Avg Rate ($f'(c) = \frac{\Delta y}{\Delta x}$). |
| **Increasing** | $f'(x) > 0$ | Graph goes up. |
| **Concave Up** | $f''(x) > 0$ | Graph shaped like $\cup$ (tangents below). |
| **Inflection Pt** | Concavity changes | $f''(x)$ changes sign. |
| **L'Hospital** | $0/0$ or $\infty/\infty$ | Limit equals $\lim (f'/g')$. |
| **Newton's** | $x_{n+1} = x_n - f/f'$ | Finds roots iteratively. |
| **Antiderivative** | $F'(x) = f(x)$ | $F(x) + C$ (reverse differentiation). |