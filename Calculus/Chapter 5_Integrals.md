## 1. Areas and Distances (Conceptual)

### The Area Problem
To find the area $A$ of the region $S$ that lies under the curve $y=f(x)$ from $a$ to $b$, we approximate it using rectangles .

> [!Definition] Riemann Sum Approximation
> We divide the interval $[a, b]$ into $n$ subintervals of equal width $\Delta x = \frac{b-a}{n}$.
> The area is approximated by the sum of the areas of $n$ rectangles:
> $$A \approx \sum_{i=1}^{n} f(x_i^*)\Delta x$$
> where $x_i^*$ is any sample point in the $i$-th subinterval $[x_{i-1}, x_i]$.
> * **Right Endpoints:** $x_i^* = x_i = a + i\Delta x$.
> * **Left Endpoints:** $x_i^* = x_{i-1} = a + (i-1)\Delta x$.
> * **Midpoints:** $x_i^* = \bar{x}_i = \frac{x_{i-1} + x_i}{2}$.



### The Exact Area
The exact area is defined as the limit of the sums of the approximating rectangles as the number of rectangles ($n$) approaches infinity:
$$A = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\Delta x$$
.

---

## 2. The Definite Integral (Conceptual)

> [!Definition] Definite Integral
> If $f$ is a function defined for $a \le x \le b$, the **definite integral of $f$ from $a$ to $b$** is:
> $$\int_{a}^{b} f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\Delta x$$
> provided that this limit exists. If it does, $f$ is called **integrable** on $[a, b]$ .
> * **Geometric Meaning:** $\int_{a}^{b} f(x) \, dx$ represents the **net signed area** between the graph of $f$ and the x-axis. (Area above is positive, area below is negative).

### Properties of the Definite Integral
1.  $\int_{a}^{b} c \, dx = c(b-a)$ (Area of a rectangle).
2.  $\int_{a}^{b} [f(x) \pm g(x)] \, dx = \int_{a}^{b} f(x) \, dx \pm \int_{a}^{b} g(x) \, dx$.
3.  $\int_{a}^{b} c f(x) \, dx = c \int_{a}^{b} f(x) \, dx$.
4.  $\int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx = \int_{a}^{b} f(x) \, dx$ (Additivity).
5.  If $f(x) \ge 0$, then $\int_{a}^{b} f(x) \, dx \ge 0$.
6.  If $f(x) \ge g(x)$, then $\int_{a}^{b} f(x) \, dx \ge \int_{a}^{b} g(x) \, dx$ .

---

## 3. The Fundamental Theorem of Calculus (FTC)

This theorem connects differential calculus (derivatives) with integral calculus (areas).

> [!Theorem] FTC Part 1 (Differentiation)
> If $f$ is continuous on $[a, b]$, then the function $g$ defined by:
> $$g(x) = \int_{a}^{x} f(t) \, dt \quad \text{for } a \le x \le b$$
> is continuous on $[a, b]$, differentiable on $(a, b)$, and **$g'(x) = f(x)$**.
> * **Implication:** Differentiation and integration are inverse processes.

> [!Theorem] FTC Part 2 (Evaluation)
> If $f$ is continuous on $[a, b]$, then:
> $$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$
> where $F$ is **any antiderivative** of $f$ (i.e., $F'(x) = f(x)$) .

>[!Theorem] Extended Theorem (**Leibniz Integral Rule**.)
>$$\frac{d}{dx} \int_{\color{blue}{g(x)}}^{\color{red}{h(x)}} f(u) \, du = \color{red}f({h(x)}) \cdot \color{red}{h'(x)} \color{blue}- f({g(x)}) \cdot \color{blue}{g'(x)}$$

$\lim_{ t \to \infty} \left( \frac{1}{t-2} \right)^{\frac{5}{2}} \frac{2}{5}-\left( \frac{1}{3-2} \right)^{\frac{5}{2}} \frac{2}{5}$
---

## 4. Indefinite Integrals & Net Change (Teach Mode)

> [!Definition] Indefinite Integral
> The notation $\int f(x) \, dx$ represents the **general antiderivative** of $f(x)$:
> $$\int f(x) \, dx = F(x) + C$$
> where $F'(x) = f(x)$ and $C$ is an arbitrary constant.

> [!Table] Table of Indefinite Integrals
> * $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$ ($n \neq -1$)
> * $\int \frac{1}{x} \, dx = \ln|x| + C$
> * $\int e^x \, dx = e^x + C$
> * $\int \sin x \, dx = -\cos x + C$
> * $\int \sec^2 x \, dx = \tan x + C$
> * $\int \frac{1}{1+x^2} \, dx = \tan^{-1} x + C$.

> [!Theorem] Net Change Theorem
> The integral of a rate of change is the net change:
> $$\int_{a}^{b} F'(x) \, dx = F(b) - F(a)$$
> * **Application:** If $v(t)$ is velocity, $\int_{t_1}^{t_2} v(t) \, dt = s(t_2) - s(t_1)$ is the **displacement** (change in position). The **total distance traveled** is $\int_{t_1}^{t_2} |v(t)| \, dt$.

---

## 5. The Substitution Rule (Integration Technique)

Used to reverse the **Chain Rule**.

> [!Method] The Substitution Rule
> If $u = g(x)$ is a differentiable function, then:
> $$\int f(g(x))g'(x) \, dx = \int f(u) \, du$$
> **Steps:**
> 1.  Choose a substitution $u = g(x)$ (usually the "inside" part of a composite function).
> 2.  Find $du = g'(x) \, dx$.
> 3.  Express the entire integral in terms of $u$ and $du$.
> 4.  Evaluate the integral with respect to $u$.
> 5.  Replace $u$ with $g(x)$ (for indefinite integrals) .

**For Definite Integrals:**
Two methods:
1.  Evaluate the indefinite integral first, substitute back to $x$, then use original limits $[a, b]$.
2.  **Change Limits (Preferred):** Calculate new limits for $u$. Lower limit $u_1 = g(a)$, upper limit $u_2 = g(b)$.
    $$\int_{a}^{b} f(g(x))g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du$$
    .

> [!Note] Integrals of Symmetric Functions
> Let $f$ be continuous on $[-a, a]$.
> * If $f$ is **even** ($f(-x) = f(x)$), then $\int_{-a}^{a} f(x) \, dx = 2\int_{0}^{a} f(x) \, dx$.
> * If $f$ is **odd** ($f(-x) = -f(x)$), then $\int_{-a}^{a} f(x) \, dx = 0$ .

---

## 📘 Examples & Applications (Exam Mode)

### Example 1: Using FTC Part 1
> [!Example] Problem
> Find the derivative of $g(x) = \int_{0}^{x} \sqrt{1+t^2} \, dt$.
> **Using:** Fundamental Theorem of Calculus Part 1.
>
> **Analysis:**
> The theorem states $\frac{d}{dx} \int_{a}^{x} f(t) \, dt = f(x)$.
> Here $f(t) = \sqrt{1+t^2}$.
>
> **Solution:**
> $$g'(x) = \sqrt{1+x^2}$$
>.

### Example 2: Using FTC Part 2 (Evaluation)
> [!Example] Problem
> Evaluate $\int_{1}^{3} e^x \, dx$.
> **Using:** Fundamental Theorem of Calculus Part 2.
>
> **Step 1:** Find antiderivative $F(x)$.
> An antiderivative of $e^x$ is $e^x$.
>
> **Step 2:** Apply limits.
> $$\int_{1}^{3} e^x \, dx = \left[ e^x \right]_{1}^{3} = e^3 - e^1$$
>.

### Example 3: Substitution Rule (Indefinite)
> [!Example] Problem
> Find $\int x^3 \cos(x^4 + 2) \, dx$.
> **Using:** Substitution Rule ($u$-sub).
>
> **Step 1:** Choose $u$.
> Let $u = x^4 + 2$.
>
> **Step 2:** Find $du$.
> $du = 4x^3 \, dx$.
> Thus, $x^3 \, dx = \frac{1}{4} du$.
>
> **Step 3:** Substitute.
> $$\int \cos(u) \cdot \frac{1}{4} \, du = \frac{1}{4} \int \cos u \, du$$
>
> **Step 4:** Integrate.
> $$\frac{1}{4} \sin u + C$$
>
> **Step 5:** Back-substitute.
> $$\frac{1}{4} \sin(x^4 + 2) + C$$
>.

### Example 4: Substitution with Definite Integrals
> [!Example] Problem
> Evaluate $\int_{0}^{4} \sqrt{2x+1} \, dx$.
> **Using:** Substitution with Limits Change.
>
> **Step 1:** Substitution.
> Let $u = 2x + 1$, so $du = 2 \, dx \implies dx = \frac{1}{2} du$.
>
> **Step 2:** Change Limits.
> * If $x = 0$, $u = 2(0) + 1 = 1$.
> * If $x = 4$, $u = 2(4) + 1 = 9$.
>
> **Step 3:** Evaluate new integral.
> $$\int_{1}^{9} \sqrt{u} \cdot \frac{1}{2} \, du = \frac{1}{2} \int_{1}^{9} u^{1/2} \, du$$
> $$= \frac{1}{2} \left[ \frac{u^{3/2}}{3/2} \right]_{1}^{9} = \frac{1}{2} \cdot \frac{2}{3} [u^{3/2}]_{1}^{9} = \frac{1}{3} [(\sqrt{9})^3 - (\sqrt{1})^3]$$
> $$= \frac{1}{3} [27 - 1] = \frac{26}{3}$$
>.

---

## 6. Summary Recap

| Concept | Formula / Rule | Key Note |
| :--- | :--- | :--- |
| **Definite Integral** | $\int_{a}^{b} f(x) dx = \lim \sum f(x_i^*) \Delta x$ | Net signed area. |
| **FTC Part 1** | $\frac{d}{dx} \int_{a}^{x} f(t) dt = f(x)$ | Derivative of integral is the function. |
| **FTC Part 2** | $\int_{a}^{b} f(x) dx = F(b) - F(a)$ | Use antiderivative to find area. |
| **Substitution** | $\int f(g(x))g'(x) dx = \int f(u) du$ | "Reverse Chain Rule". Don't forget $du$. |
| **Even Function** | $\int_{-a}^{a} f(x) dx = 2 \int_{0}^{a} f(x) dx$ | Symmetric about y-axis (e.g., $x^2, \cos x$). |
| **Odd Function** | $\int_{-a}^{a} f(x) dx = 0$ | Symmetric about origin (e.g., $x^3, \sin x$). |

| **Function**                   | **Integral**                               |
| ------------------------------ | ------------------------------------------ |
| **Sine**                       | $\int \sin(x) \, dx = -\cos(x) + C$        |
| **Cosine**                     | $\int \cos(x) \, dx = \sin(x) + C$         |
| **Secant Squared**             | $\int \sec^2(x) \, dx = \tan(x) + C$       |
| **Cosecant Squared**           | $\int \csc^2(x) \, dx = -\cot(x) + C$      |
| **Secant $\cdot$ Tangent**     | $\int \sec(x)\tan(x) \, dx = \sec(x) + C$  |
| **Cosecant $\cdot$ Cotangent** | $\int \csc(x)\cot(x) \, dx = -\csc(x) + C$ |
| **Tangent**                    | $\int \tan(x) , dx = -\ln$                 |
| **Cotangent**                  | $\int \cot(x) , dx = \ln$                  |

| **Form**            | **Integral**                                         |
| ------------------- | ---------------------------------------------------- |
| **Arcsine Form**    | $\int \frac{1}{\sqrt{1-x^2}} \, dx = \arcsin(x) + C$ |
| **Arctangent Form** | $\int \frac{1}{1+x^2} \, dx = \arctan(x) + C$        |
| **Arcsecant Form**  | $\int \frac{1}{                                      |