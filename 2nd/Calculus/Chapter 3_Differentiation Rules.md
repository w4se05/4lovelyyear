## 1. Basic Differentiation Rules (Conceptual)

### Power and Exponential Rules
> [!Theorem] Power Rule
> If $n$ is any real number, then:
> $$\frac{d}{dx}(x^n) = nx^{n-1}$$
> * **Note:** This applies to negative and fractional powers (roots) as well .

> [!Definition] Derivative of the Natural Exponential
> The function $f(x) = e^x$ is unique because it is its own derivative:
> $$\frac{d}{dx}(e^x) = e^x$$

### Linearity Properties
If $f$ and $g$ are differentiable and $c$ is a constant:
1.  **Constant Multiple:** $\frac{d}{dx}[cf(x)] = c \frac{d}{dx}f(x)$.
2.  **Sum/Difference:** $\frac{d}{dx}[f(x) \pm g(x)] = \frac{d}{dx}f(x) \pm \frac{d}{dx}g(x)$.

---

## 2. Combination Rules (Conceptual)

### Product and Quotient Rules
> [!Theorem] Product Rule
> If $f$ and $g$ are differentiable, then:
> $$\frac{d}{dx}[f(x)g(x)] = f(x)g'(x) + g(x)f'(x)$$
> *Mnemonic:* "First d-Second plus Second d-First".

> [!Theorem] Quotient Rule
> If $f$ and $g$ are differentiable and $g(x) \neq 0$:
> $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x)f'(x) - f(x)g'(x)}{[g(x)]^2}$$
> *Mnemonic:* "Low d-High minus High d-Low, over Low squared".

### Trigonometric Derivatives
> [!Note] Standard Trig Derivatives
> * $\frac{d}{dx}(\sin x) = \cos x$ 
> * $\frac{d}{dx}(\cos x) = -\sin x$
> * $\frac{d}{dx}(\tan x) = \sec^2 x$ 
> * $\frac{d}{dx}(\csc x) = -\csc x \cot x$
> * $\frac{d}{dx}(\sec x) = \sec x \tan x$
> * $\frac{d}{dx}(\cot x) = -\csc^2 x$

---

## 3. The Chain Rule (Conceptual)

> [!Theorem] The Chain Rule
> Used for **composite functions** $F(x) = f(g(x))$.
> If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then:
> $$F'(x) = f'(g(x)) \cdot g'(x)$$
> **Leibniz Notation:** If $y = f(u)$ and $u = g(x)$:
> $$\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}$$
> .

> [!Tip] Combined Power Chain Rule
> For $y = [g(x)]^n$:
> $$\frac{d}{dx}([g(x)]^n) = n[g(x)]^{n-1} \cdot g'(x)$$

---

## 4. Advanced Differentiation Methods

### Implicit Differentiation
Used when $y$ cannot be easily isolated (e.g., $x^2 + y^2 = 25$).
**Method:**
1.  Differentiate both sides with respect to $x$.
2.  Treat $y$ as a function of $x$ (apply Chain Rule: $\frac{d}{dx}(y^2) = 2y \cdot y'$).
3.  Solve the resulting equation for $y'$ .

### Derivatives of Logarithmic Functions
> [!Theorem] Log Rules
> * $\frac{d}{dx}(\ln x) = \frac{1}{x}$
> * **Chain Rule version:** $\frac{d}{dx}(\ln u) = \frac{1}{u} \frac{du}{dx}$.
> * **General Base:** $\frac{d}{dx}(\log_b x) = \frac{1}{x \ln b}$.

> [!Tip] Logarithmic Differentiation
> Useful for messy products/quotients or variable exponents like $y = x^x$.
> 1.  Take $\ln$ of both sides: $\ln y = \ln(\dots)$.
> 2.  Simplify using log laws (turn products to sums, powers to coefficients).
> 3.  Differentiate implicitly with respect to $x$.
> 4.  Solve for $y'$.

### Hyperbolic Functions
Defined using $e^x$:
* $\sinh x = \frac{e^x - e^{-x}}{2}$
* $\cosh x = \frac{e^x + e^{-x}}{2}$
* **Derivatives:**
    * $\frac{d}{dx}(\sinh x) = \cosh x$
    * $\frac{d}{dx}(\cosh x) = \sinh x$ (Note: No negative sign!) .

---

## 5. Applications of Derivatives

### Rates of Change
* **Physics:** If $s(t)$ is position:
    * Velocity $v(t) = s'(t)$.
    * Acceleration $a(t) = v'(t) = s''(t)$.
* **Biology/Economics:** $f'(x)$ represents the instantaneous rate of change of the quantity $f(x)$ with respect to $x$ .

### Exponential Growth and Decay
For populations or radioactive substances where growth rate is proportional to size:
$$\frac{dy}{dt} = ky \implies y(t) = y_0 e^{kt}$$
* $k > 0$: Growth.
* $k < 0$: Decay .

### Related Rates
Calculating how one rate affects another (e.g., radius vs. volume of a balloon).
**Strategy:**
1.  Draw a diagram and define variables.
2.  Write the equation relating the variables (Geometry/Trig).
3.  **Differentiate both sides** with respect to time $t$ (Implicitly).
4.  Substitute known values *after* differentiation to solve for the unknown rate .

### Linear Approximation
Approximating a curve with its tangent line near $x = a$.
> [!Definition] Linearization
> $$L(x) = f(a) + f'(a)(x-a)$$
> This is used to estimate $f(x)$ when $x$ is close to $a$.

---

## 📘 Examples & Applications (Exam Mode)

### Example 1: Chain Rule
> [!Example] Problem
> Differentiate $F(x) = \sqrt{x^2 + 1}$.
> **Using:** Chain Rule (Power Rule version).
>
> **Step 1:** Rewrite as power.
> $F(x) = (x^2 + 1)^{1/2}$. Let $u = x^2+1$ and $y = u^{1/2}$.
>
> **Step 2:** Apply formula.
> $$F'(x) = \frac{1}{2}(x^2 + 1)^{-1/2} \cdot \frac{d}{dx}(x^2 + 1)$$
>
> **Step 3:** Differentiate inside.
> $$F'(x) = \frac{1}{2\sqrt{x^2 + 1}} \cdot (2x)$$
>
> **Result:**
> $$F'(x) = \frac{x}{\sqrt{x^2 + 1}}$$
> .

### Example 2: Implicit Differentiation
> [!Example] Problem
> Find $y'$ for $x^2 + y^2 = 25$.
> **Using:** Implicit Differentiation.
>
> **Step 1:** Differentiate w.r.t $x$.
> $$\frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = \frac{d}{dx}(25)$$
> $$2x + 2y \frac{dy}{dx} = 0$$
>
> **Step 2:** Solve for $\frac{dy}{dx}$.
> $$2y \frac{dy}{dx} = -2x$$
> $$\frac{dy}{dx} = -\frac{x}{y}$$


### Example 3: Related Rates (Ladder Problem)
> [!Example] Problem
> 
> A 10ft ladder rests against a wall. The bottom slides away at 1 ft/s. How fast is the top sliding down when the bottom is 6 ft from the wall?
> **Using:** Pythagorean Theorem + Chain Rule.
>
> **Step 1:** Setup.
> $x^2 + y^2 = 10^2 = 100$.
> Given: $\frac{dx}{dt} = 1$. Find $\frac{dy}{dt}$ when $x = 6$.
>
> **Step 2:** Differentiate w.r.t $t$.
> $$2x \frac{dx}{dt} + 2y \frac{dy}{dt} = 0 \implies x \frac{dx}{dt} + y \frac{dy}{dt} = 0$$
>
> **Step 3:** Find $y$ when $x=6$.
> $6^2 + y^2 = 100 \implies 36 + y^2 = 100 \implies y = \sqrt{64} = 8$.
>
> **Step 4:** Solve.
> $$(6)(1) + (8) \frac{dy}{dt} = 0$$
> $$8 \frac{dy}{dt} = -6 \implies \frac{dy}{dt} = -0.75 \text{ ft/s}$$


### Example 4: Linear Approximation
> [!Example] Problem
> Estimate $\sqrt{4.02}$.
> **Using:** Linearization $L(x)$ at $a=4$ for $f(x)=\sqrt{x}$.
>
> **Step 1:** Find $f(a)$ and $f'(a)$.
> $f(4) = 2$.
> $f'(x) = \frac{1}{2\sqrt{x}} \implies f'(4) = \frac{1}{4} = 0.25$.
>
> **Step 2:** Form Equation.
> $$L(x) = 2 + 0.25(x - 4)$$
>
> **Step 3:** Estimate.
> $\sqrt{4.02} \approx L(4.02) = 2 + 0.25(4.02 - 4) = 2 + 0.25(0.02)$.
> $$= 2 + 0.005 = 2.005$$


---

## 6. Summary Recap

| Rule | Formula | Condition |
| :--- | :--- | :--- |
| **Product** | $f'g + fg'$ | Use for $x^2 \sin x$ |
| **Quotient** | $\frac{g f' - f g'}{g^2}$ | Use for $\frac{x}{x+1}$ |
| **Chain** | $f'(g(x))g'(x)$ | Use for $\sin(x^2)$ |
| **Implicit** | Diff terms, add $y'$ to $y$-terms | Use for $x^2+y^2=1$ |
| **Log Diff** | $\ln y = \dots \implies \frac{y'}{y} = \dots$ | Use for $x^x$ or huge products |
| **Linear Approx**| $L(x) = f(a) + f'(a)(x-a)$ | Estimation near $a$ |