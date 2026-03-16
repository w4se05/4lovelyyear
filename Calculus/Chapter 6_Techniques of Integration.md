## 1. Integration by Parts (Method)

Used for integrating **products** of functions (e.g., $x \ln x, x e^x$) or single functions like $\ln x, \tan^{-1}x$.

> [!Theorem] Formula
> Derived from the Product Rule for differentiation:
> $$\int u \, dv = uv - \int v \, du$$
> * **Strategy:** Choose $u$ to be the function that simplifies when differentiated (e.g., algebraic, logarithmic), and $dv$ to be the part that is easy to integrate .
> * **LIATE Rule:** Priority for choosing $u$: **L**ogarithmic, **I**nverse Trig, **A**lgebraic, **T**rigonometric, **E**xponential.

> [!Tip] Definite Integrals
> $$\int_{a}^{b} u(x)v'(x) \, dx = \left[ u(x)v(x) \right]_{a}^{b} - \int_{a}^{b} v(x)u'(x) \, dx$$


---

## 2. Trigonometric Integrals (Method)

Strategy for integrating combinations of powers of sine and cosine: $\int \sin^m x \cos^n x \, dx$.

| Condition | Strategy | Identity Used |
| :--- | :--- | :--- |
| **Odd power of cosine** | Save one factor of $\cos x$. Convert remaining $\cos^2 x$ to $\sin^2 x$. Let $u = \sin x$. | $\cos^2 x = 1 - \sin^2 x$ |
| **Odd power of sine** | Save one factor of $\sin x$. Convert remaining $\sin^2 x$ to $\cos^2 x$. Let $u = \cos x$. | $\sin^2 x = 1 - \cos^2 x$ |
| **Both powers even** | Use half-angle identities to reduce powers. | $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$ <br> $\cos^2 x = \frac{1}{2}(1 + \cos 2x)$ |

*Note:* Similar strategies exist for $\tan^m x \sec^n x$ using $\sec^2 x = 1 + \tan^2 x$.

---

## 3. Trigonometric Substitution (Method)

Used to integrate expressions containing radicals: $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$.

> [!Table] Substitution Table
> | Expression | Substitution | Domain Restriction | Identity Simplification |
> | :--- | :--- | :--- | :--- |
> | $\sqrt{a^2 - x^2}$ | $x = a \sin \theta$ | $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$ | $1 - \sin^2 \theta = \cos^2 \theta$ |
> | $\sqrt{a^2 + x^2}$ | $x = a \tan \theta$ | $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$ | $1 + \tan^2 \theta = \sec^2 \theta$ |
> | $\sqrt{x^2 - a^2}$ | $x = a \sec \theta$ | $0 \le \theta < \frac{\pi}{2}$ or $\pi \le \theta < \frac{3\pi}{2}$ | $\sec^2 \theta - 1 = \tan^2 \theta$ |
> .

---

## 4. Partial Fractions (Method)

Used for integrating **rational functions** $f(x) = \frac{P(x)}{Q(x)}$.
* **Prerequisite:** The degree of $P(x)$ must be less than the degree of $Q(x)$. If not, perform **long division** first.

**Decomposition Rules:**
1.  **Distinct Linear Factors:** If $Q(x) = (x-a_1)(x-a_2)...$, decompose as:
    $$\frac{A_1}{x-a_1} + \frac{A_2}{x-a_2} + \dots$$
2.  **Repeated Linear Factors:** If $Q(x)$ contains $(x-a)^r$, include:
    $$\frac{A_1}{x-a} + \frac{A_2}{(x-a)^2} + \dots + \frac{A_r}{(x-a)^r}$$
3.  **Irreducible Quadratic Factors:** If $Q(x)$ contains $(ax^2 + bx + c)$ where $b^2 - 4ac < 0$, include:
    $$\frac{Ax + B}{ax^2 + bx + c}$$

---

## 5. Approximate Integration (Conceptual)

Used when an antiderivative cannot be found in terms of elementary functions (e.g., $e^{x^2}$).

> [!Definition] Methods
> 1.  **Midpoint Rule ($M_n$):** Uses midpoints of subintervals $\bar{x}_i$.
> 2.  **Trapezoidal Rule ($T_n$):** Averages the function values at endpoints.
>     $$T_n = \frac{\Delta x}{2} [f(x_0) + 2f(x_1) + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n)]$$
> 3.  **Simpson's Rule ($S_n$):** Uses parabolas to approximate the curve ($n$ must be even).
>     $$S_n = \frac{\Delta x}{3} [f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \dots + 4f(x_{n-1}) + f(x_n)]$$
>     *Pattern:* $1, 4, 2, 4, 2, \dots, 4, 1$.

---

## 6. Improper Integrals (Conceptual)

Integrals with infinite intervals or discontinuous integrands.

> [!Definition] Type 1: Infinite Intervals
> * $\int_{a}^{\infty} f(x) \, dx = \lim_{t \to \infty} \int_{a}^{t} f(x) \, dx$
> * $\int_{-\infty}^{b} f(x) \, dx = \lim_{t \to -\infty} \int_{t}^{b} f(x) \, dx$
> * If the limit exists and is finite, the integral **converges**. Otherwise, it **diverges** .
> * **p-test for Integrals:** $\int_{1}^{\infty} \frac{1}{x^p} \, dx$ converges if $p > 1$ and diverges if $p \le 1$.

> [!Definition] Type 2: Discontinuous Integrands
> If $f$ is discontinuous at $b$ (vertical asymptote), then:
> $$\int_{a}^{b} f(x) \, dx = \lim_{t \to b^-} \int_{a}^{t} f(x) \, dx$$


> [!Theorem] Comparison Test
> If $f(x) \ge g(x) \ge 0$ for $x \ge a$:
> * If $\int_{a}^{\infty} f(x) \, dx$ converges, then $\int_{a}^{\infty} g(x) \, dx$ converges.
> * If $\int_{a}^{\infty} g(x) \, dx$ diverges, then $\int_{a}^{\infty} f(x) \, dx$ diverges.


---

## 📘 Examples & Applications (Exam Mode)

### Example 1: Integration by Parts
> [!Example] Problem
> Evaluate $\int x \cos x \, dx$.
> **Using:** Integration by Parts ($\int u dv = uv - \int v du$).
>
> **Step 1:** Choose $u$ and $dv$.
> Let $u = x$ (Algebraic) and $dv = \cos x \, dx$ (Trig).
> Then $du = dx$ and $v = \sin x$.
>
> **Step 2:** Apply formula.
> $$\int x \cos x \, dx = x \sin x - \int \sin x \, dx$$
>
> **Step 3:** Evaluate remaining integral.
> $$= x \sin x - (-\cos x) + C$$
> $$= x \sin x + \cos x + C$$
> .

### Example 2: Trigonometric Substitution
> [!Example] Problem
> Evaluate $\int \frac{\sqrt{9-x^2}}{x^2} \, dx$.
> **Using:** Trig Sub ($\sqrt{a^2-x^2} \to x = a\sin\theta$).
>
> **Step 1:** Substitution.
> Let $x = 3 \sin \theta$, so $dx = 3 \cos \theta \, d\theta$.
> $\sqrt{9 - x^2} = \sqrt{9 - 9\sin^2 \theta} = 3\cos \theta$.
>
> **Step 2:** Rewrite integral.
> $$\int \frac{3 \cos \theta}{(3 \sin \theta)^2} \cdot 3 \cos \theta \, d\theta = \int \frac{9 \cos^2 \theta}{9 \sin^2 \theta} \, d\theta = \int \cot^2 \theta \, d\theta$$
>
> **Step 3:** Integrate.
> Use identity $\cot^2 \theta = \csc^2 \theta - 1$.
> $$\int (\csc^2 \theta - 1) \, d\theta = -\cot \theta - \theta + C$$
>
> **Step 4:** Back-substitute.
> Since $\sin \theta = \frac{x}{3}$, draw a triangle: Opposite=$x$, Hypotenuse=$3$, Adjacent=$\sqrt{9-x^2}$.
> $\cot \theta = \frac{\text{Adj}}{\text{Opp}} = \frac{\sqrt{9-x^2}}{x}$ and $\theta = \sin^{-1}(\frac{x}{3})$.
> **Result:** $-\frac{\sqrt{9-x^2}}{x} - \sin^{-1}\left(\frac{x}{3}\right) + C$.

### Example 3: Partial Fractions
> [!Example] Problem
> Evaluate $\int \frac{x^2 + 2x - 1}{2x^3 + 3x^2 - 2x} \, dx$.
> **Using:** Partial Fraction Decomposition.
>
> **Step 1:** Factor denominator.
> $Q(x) = x(2x^2 + 3x - 2) = x(2x-1)(x+2)$.
>
> **Step 2:** Setup decomposition.
> $$\frac{x^2 + 2x - 1}{x(2x-1)(x+2)} = \frac{A}{x} + \frac{B}{2x-1} + \frac{C}{x+2}$$
>
> **Step 3:** Solve for constants ($A, B, C$).
> Multiply by denominator:
> $x^2 + 2x - 1 = A(2x-1)(x+2) + B(x)(x+2) + C(x)(2x-1)$.
> * Set $x=0$: $-1 = A(-1)(2) \implies A = \frac{1}{2}$.
> * Set $x=-2$: $4 - 4 - 1 = C(-2)(-5) \implies -1 = 10C \implies C = -\frac{1}{10}$.
> * Set $x=1/2$: $\frac{1}{4} + 1 - 1 = B(\frac{1}{2})(\frac{5}{2}) \implies \frac{1}{4} = \frac{5}{4}B \implies B = \frac{1}{5}$.
>
> **Step 4:** Integrate.
> $$\int \left( \frac{1/2}{x} + \frac{1/5}{2x-1} - \frac{1/10}{x+2} \right) dx$$
> $$= \frac{1}{2}\ln|x| + \frac{1}{10}\ln|2x-1| - \frac{1}{10}\ln|x+2| + C$$
> *Note:* The term $\int \frac{1}{2x-1}dx$ requires a mini $u$-sub ($u=2x-1$), resulting in $\frac{1}{2}\ln|u|$.
> .

### Example 4: Improper Integral
> [!Example] Problem
> Evaluate $\int_{1}^{\infty} \frac{1}{x} \, dx$.
> **Using:** Improper Integral Definition.
>
> **Step 1:** Definition.
> $$\lim_{t \to \infty} \int_{1}^{t} \frac{1}{x} \, dx$$
>
> **Step 2:** Integrate.
> $$= \lim_{t \to \infty} \left[ \ln|x| \right]_{1}^{t} = \lim_{t \to \infty} (\ln t - \ln 1)$$
>
> **Step 3:** Limit.
> Since $\ln t \to \infty$ as $t \to \infty$, the limit is $\infty$.
> **Result:** The integral **diverges**.

---

## 7. Summary Recap

| Integration Method | Form / Condition | Key Step |
| :--- | :--- | :--- |
| **Parts** | $\int x e^x, \int x \ln x$ | $u = $ easy diff, $dv = $ easy int. |
| **Trig Identity** | $\int \sin^m \cos^n$ | Save 1 odd factor, convert rest. |
| **Trig Sub** | $\sqrt{a^2 \pm x^2}$ | $x = a\sin\theta, a\tan\theta, a\sec\theta$. |
| **Partial Fractions** | Rational $\frac{P}{Q}$ | Decompose into $\frac{A}{x-r}$. |
| **Approximate** | No elem antideriv | Simpson's Rule (1-4-2-4-1). |
| **Improper** | $\infty$ bounds or asymptotes | Replace bound with $t$, take limit. |