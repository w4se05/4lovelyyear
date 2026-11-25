# 📘 Calculus & Series Comprehensive Summary

## 1. Infinite Sequences and Series
**Source:** *Chap 1_Sequences and Series.md*

### Definitions
* **Sequence:** A list of numbers $\{a_n\}$ in a definite order. A sequence **converges** if $\lim_{n\to\infty} a_n = L$ exists and is unique.
* **Series:** The sum of a sequence $\sum_{n=1}^{\infty} a_n$. A series **converges** if the sequence of its partial sums $s_n = \sum_{i=1}^n a_i$ has a finite limit.

### Fundamental Series Types
| Type          | Form                 | Convergence Condition                       | Sum Formula         |
| :------------ | :------------------- | :------------------------------------------ | :------------------ |
| **Geometric** | $\sum ar^{n}$        | Converges if $r< 1$                         | $S = \frac{a}{1-r}$ |
| **p-Series**  | $\sum \frac{1}{n^p}$ | Converges if $p > 1$; Diverges if $p \le 1$ | N/A                 |
| **Harmonic**  | $\sum \frac{1}{n}$   | **Diverges** ($p=1$)                        | N/A                 |

### Convergence Tests
1.  **Test for Divergence:** If $\lim_{n\to\infty} a_n \neq 0$ (or DNE), the series **diverges**. (Note: Limit $= 0$ is inconclusive).
2.  **Ratio Test:** Let $L = \lim_{n\to\infty} |\frac{a_{n+1}}{a_n}|$.
    * If $L < 1$: Absolute Convergence.
    * If $L > 1$: Divergence.
    * If $L = 1$: Inconclusive.
3.  **Root Test:** Let $L = \lim_{n\to\infty} \sqrt[n]{|a_n|}$. Same conditions as Ratio Test.
4.  **Alternating Series Test (Leibniz):** $\sum (-1)^{n-1}b_n$ converges if $b_{n+1} \le b_n$ (decreasing) and $\lim b_n = 0$.

---

## 2. L'Hospital's Rule
**Source:** *Chapter 4_ Applications of Differentiation.md*

### The Rule
Suppose $f$ and $g$ are differentiable and $g'(x) \neq 0$. If $\lim_{x \to a} \frac{f(x)}{g(x)}$ results in an indeterminate form of **$\frac{0}{0}$** or **$\frac{\infty}{\infty}$**, then:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
*Provided the limit on the right exists.*

### Handling Other Indeterminate Forms
* **Products ($0 \cdot \infty$):** Rewrite $f \cdot g$ as $\frac{f}{1/g}$ to force a $\frac{0}{0}$ or $\frac{\infty}{\infty}$ form.
* **Differences ($\infty - \infty$):** Combine fractions using a common denominator or rationalization.
* **Powers ($0^0, \infty^0, 1^\infty$):** Use natural logs. Let $y = [f(x)]^{g(x)}$, then $\ln y = g(x) \ln f(x)$. Find the limit of $\ln y$, then exponentiate the result.

---

## 3. Newton’s Method
**Source:** *Chapter 4_ Applications of Differentiation.md*

### Purpose
A numerical method used to approximate the roots (zeros) of a function $f(x) = 0$.

### Iterative Formula
Given an initial guess $x_1$:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
Repeat the process to find $x_2, x_3, \dots$ until the value stabilizes to the desired accuracy.

---

## 4. Related Rates
**Source:** *Chapter 3_Differentiation Rules.md*

### Concept
Calculating how the rate of change of one quantity affects the rate of change of another connected quantity (e.g., how fast the water level rises as volume increases).

### Strategy
1.  **Draw a diagram** and define variables.
2.  **Write the equation** relating the variables (often Geometry or Trig definitions).
3.  **Differentiate implicitly** with respect to time $t$. (Remember: $\frac{d}{dt}(y^2) = 2y \frac{dy}{dt}$).
4.  **Substitute** known values *after* differentiation to solve for the unknown rate.

---

## 5. Mean Value Theorem (MVT)
**Source:** *Chapter 4_ Applications of Differentiation.md*

### Rolle's Theorem (Prerequisite)
If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then there is a number $c$ where $f'(c) = 0$.

### The Mean Value Theorem
If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, there exists a number $c$ in $(a, b)$ such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$
* **Interpretation:** There is a point $c$ where the instantaneous slope (tangent) equals the average slope (secant line) over the interval.

---

## 6. Fundamental Theorem of Calculus (FTC)
**Source:** *Chapter 5_Integrals.md*

### Part 1: Differentiation of Integrals
If $f$ is continuous on $[a, b]$, the function $g(x) = \int_{a}^{x} f(t) \, dt$ is continuous and differentiable, and:
$$g'(x) = f(x)$$
* **Meaning:** Differentiation allows you to recover the original function from its integral.

### Part 2: Evaluation of Integrals
If $f$ is continuous on $[a, b]$ and $F$ is any antiderivative of $f$ (where $F' = f$), then:
$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$
* **Meaning:** The net area under the curve is the difference in the antiderivative values at the endpoints.

### Net Change Theorem
$\int_{a}^{b} F'(x) \, dx = F(b) - F(a)$. The integral of a rate of change is the net change in the quantity (e.g., integrating velocity gives displacement).

---

## 7. Approximate Integration
**Source:** *Chapter 6_Techniques of Integration.md*

When an elementary antiderivative cannot be found, we approximate the definite integral $\int_a^b f(x) dx$.

### Midpoint Rule ($M_n$)
Uses the midpoint $\bar{x}_i$ of each subinterval to calculate rectangle heights.
* Formula: $M_n = \Delta x [f(\bar{x}_1) + f(\bar{x}_2) + \dots + f(\bar{x}_n)]$.

### Trapezoidal Rule ($T_n$)
Approximates the area using trapezoids connecting the function values at endpoints.
$$T_n = \frac{\Delta x}{2} [f(x_0) + 2f(x_1) + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n)]$$
* **Pattern:** Coefficients are $1, 2, 2, \dots, 2, 1$.

---

## 8. Improper Integrals (Type 1)
**Source:** *Chapter 6_Techniques of Integration.md*
### Definition (Infinite Intervals)
Integrals where the interval of integration is infinite.
1.  **Upper bound infinity:** $\int_{a}^{\infty} f(x) \, dx = \lim_{t \to \infty} \int_{a}^{t} f(x) \, dx$.
2.  **Lower bound infinity:** $\int_{-\infty}^{b} f(x) \, dx = \lim_{t \to -\infty} \int_{t}^{b} f(x) \, dx$.
### Convergence
* If the limit exists and is finite, the integral **converges**.
* If the limit does not exist or is infinite, the integral **diverges**.

### p-Test for Integrals
For $\int_{1}^{\infty} \frac{1}{x^p} \, dx$:
* **Converges** if $p > 1$.
* **Diverges** if $p \le 1$.

---

## 9. Applications of Integration (Area & Volume)
*(Note: General area concepts are in Chapter 5; Volume formulas are created as they were not present in the provided files).*

### Area Between Curves **(Created)**
If $f(x) \ge g(x)$ on $[a, b]$, the area $A$ bounded by the curves is:
$$A = \int_{a}^{b} [f(x) - g(x)] \, dx$$
* **Strategy:** Determine which function is "top" ($f$) and which is "bottom" ($g$), then integrate the difference.

### Volumes of Revolution **(Created)**
1.  **Disk Method:**
    Used when rotating a region under a curve $y=f(x)$ about the **x-axis** (no gap between region and axis).
    $$V = \int_{a}^{b} \pi [f(x)]^2 \, dx$$
    * Think: Sum of circular disks with radius $R = f(x)$.

2.  **Washer Method:**
    Used when rotating the region between two curves $f(x)$ and $g(x)$ about the axis (there is a gap/hole).
    $$V = \int_{a}^{b} \pi ([R_{outer}(x)]^2 - [r_{inner}(x)]^2) \, dx$$
    * Think: Disk with a hole removed.