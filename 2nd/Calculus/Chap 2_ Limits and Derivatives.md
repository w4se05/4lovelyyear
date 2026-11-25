## 1. The Limit Concept (Conceptual)

### Tangents and Velocities
> [!Note] Motivation
> Calculus arises from two classic problems:
> 1.  **The Tangent Problem:** Finding the slope of a tangent line to a curve at a specific point. We approximate this using **secant lines** passing through the point $P$ and a nearby point $Q$ .
> 2.  **The Velocity Problem:** Finding instantaneous velocity. We approximate this using **average velocity** over shorter and shorter time intervals .

### Definition of a Limit
> [!Definition] Intuitive Definition
> We write:
> $$\lim_{x \to a} f(x) = L$$
> if the values of $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $a$ (on either side of $a$), but not equal to $a$.
> * **Important:** The value of $f(a)$ does *not* affect the limit. The function might be undefined at $a$.

### One-Sided Limits
> [!Definition] Left and Right Limits
> * **Left-hand limit:** $\lim_{x \to a^-} f(x) = L$ (approaching $a$ from values $x < a$).
> * **Right-hand limit:** $\lim_{x \to a^+} f(x) = L$ (approaching $a$ from values $x > a$).
> 
> **Theorem:** The general limit $\lim_{x \to a} f(x) = L$ exists **if and only if**:
> $$\lim_{x \to a^-} f(x) = L \quad \text{and} \quad \lim_{x \to a^+} f(x) = L$$

### Infinite Limits
> [!Definition] Vertical Asymptote
> If $\lim_{x \to a} f(x) = \pm \infty$, the line $x = a$ is called a **vertical asymptote** of the curve $y = f(x)$.
> * This means $f(x)$ grows arbitrarily large (positive or negative) as $x$ approaches $a$.

---

## 2. Calculating Limits (Teach Mode)

### Limit Laws
If $\lim_{x \to a} f(x) = A$ and $\lim_{x \to a} g(x) = B$, then:
1.  **Sum/Difference:** $\lim [f(x) \pm g(x)] = A \pm B$.
2.  **Constant Multiple:** $\lim [c f(x)] = cA$.
3.  **Product:** $\lim [f(x)g(x)] = A \cdot B$.
4.  **Quotient:** $\lim \left[\frac{f(x)}{g(x)}\right] = \frac{A}{B}$ (provided $B \neq 0$).
5.  **Power/Root:** $\lim [f(x)]^n = A^n$ and $\lim \sqrt[n]{f(x)} = \sqrt[n]{A}$ .

> [!Tip] Direct Substitution Property
> If $f$ is a polynomial or a rational function and $a$ is in the domain of $f$, then:
> $$\lim_{x \to a} f(x) = f(a)$$

### Special Techniques
1.  **Algebraic Simplification:** If direct substitution results in an indeterminate form (like $\frac{0}{0}$), factor and cancel common terms or rationalize the numerator/denominator .
2.  **Squeeze Theorem:**
> [!Theorem] Squeeze Theorem
> If $f(x) \le g(x) \le h(x)$ when $x$ is near $a$ (except possibly at $a$) and:
> $$\lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L$$
> Then $\lim_{x \to a} g(x) = L$.
---
## 3. Continuity (Conceptual)

> [!Definition] Continuity at a Point
> A function $f$ is **continuous at a number $a$** if:
> $$\lim_{x \to a} f(x) = f(a)$$
> This implies three conditions:
> 1.  $f(a)$ is defined.
> 2.  $\lim_{x \to a} f(x)$ exists.
> 3.  The limit equals the function value.

### Types of Discontinuity
If $f$ is not continuous at $a$, it has a **discontinuity**:
1.  **Removable:** The limit exists, but $f(a)$ is different or undefined (hole in graph).
2.  **Jump:** Left and right limits exist but are different (step in graph).
3.  **Infinite:** The limit is $\pm \infty$ (vertical asymptote) .

### Theorems on Continuity
* **Polynomials & Rational Functions** are continuous on their domains.
* **Root, Trig, Inverse Trig, Exponential, Log** functions are continuous on their domains.
* **Composite Functions:** If $g$ is continuous at $a$ and $f$ is continuous at $g(a)$, then $(f \circ g)(x) = f(g(x))$ is continuous at $a$.

> [!Theorem] Intermediate Value Theorem (IVT)
> Suppose $f$ is continuous on the closed interval $[a, b]$ and let $N$ be any number between $f(a)$ and $f(b)$ (where $f(a) \neq f(b)$).
> Then there exists a number $c$ in $(a, b)$ such that $f(c) = N$.
> * **Application:** Used to show that a root exists for an equation $f(x)=0$ within an interval.

---

## 4. Limits at Infinity (Asymptotes)

> [!Definition] Horizontal Asymptote
> If $\lim_{x \to \infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$, then the line $y = L$ is a **horizontal asymptote** of the curve.

> [!Tip] Calculation Strategy for Rational Functions
> To evaluate $\lim_{x \to \infty} \frac{P(x)}{Q(x)}$, divide both numerator and denominator by the **highest power of $x$** that appears in the denominator.
> * Recall: $\lim_{x \to \infty} \frac{1}{x^r} = 0$ for $r > 0$.

---

## 5. Precise Definition (Advanced)

> [!Definition] $\epsilon-\delta$ Definition
> $\lim_{x \to a} f(x) = L$ if for every number $\epsilon > 0$, there exists a number $\delta > 0$ such that:
> $$\text{if } 0 < |x - a| < \delta \text{ then } |f(x) - L| < \epsilon$$
> 
> * **Meaning:** We can force $f(x)$ to be within distance $\epsilon$ of $L$ by keeping $x$ within distance $\delta$ of $a$.

---

## 6. Derivatives (Intro)

> [!Definition] The Derivative
> The **derivative** of a function $f$ at a number $a$, denoted by $f'(a)$, is:
> $$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$
> (provided the limit exists) 
> * **Geometric Interpretation:** $f'(a)$ is the **slope** of the tangent line to the curve $y=f(x)$ at $(a, f(a))$.

---

## 📘 Examples & Applications (Exam Mode)

### Example 1: Evaluating Indeterminate Forms
> [!Example] Problem
> Evaluate $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$.
> **Using:** Factorization (Simplifying $0/0$ form).
> 
> **Step 1:** Check direct substitution.
> Sub $x=1$: $\frac{1^2-1}{1-1} = \frac{0}{0}$ (Indeterminate).
> 
> **Step 2:** Factor numerator.
> $$x^2 - 1 = (x-1)(x+1)$$
> 
> **Step 3:** Cancel terms.
> $$\lim_{x \to 1} \frac{(x-1)(x+1)}{x-1} = \lim_{x \to 1} (x+1)$$
> 
> **Step 4:** Substitute.
> $$1 + 1 = 2$$
> .

### Example 2: Squeeze Theorem
> [!Example] Problem
> Show that $\lim_{x \to 0} x^2 \sin(\frac{1}{x}) = 0$.
> **Using:** Squeeze Theorem.
> 
> **Step 1:** Bound the sine function.
> $$-1 \le \sin\left(\frac{1}{x}\right) \le 1$$
> 
> **Step 2:** Multiply by $x^2$ (since $x^2 \ge 0$, inequality direction stays).
> $$-x^2 \le x^2 \sin\left(\frac{1}{x}\right) \le x^2$$
> 
> **Step 3:** Take limits of the bounds.
> $$\lim_{x \to 0} (-x^2) = 0 \quad \text{and} \quad \lim_{x \to 0} (x^2) = 0$$
> 
> **Conclusion:** By Squeeze Theorem, $\lim_{x \to 0} x^2 \sin(\frac{1}{x}) = 0$.

### Example 3: Finding Horizontal Asymptotes
> [!Example] Problem
> Find $\lim_{x \to \infty} \frac{3x^2 - x - 2}{5x^2 + 4x + 1}$.
> **Using:** Limits at Infinity (Divide by highest power).
> 
> **Step 1:** Identify highest power in denominator ($x^2$).
> Divide all terms by $x^2$:
> $$\frac{\frac{3x^2}{x^2} - \frac{x}{x^2} - \frac{2}{x^2}}{\frac{5x^2}{x^2} + \frac{4x}{x^2} + \frac{1}{x^2}} = \frac{3 - \frac{1}{x} - \frac{2}{x^2}}{5 + \frac{4}{x} + \frac{1}{x^2}}$$
> 
> **Step 2:** Take the limit as $x \to \infty$.
> Terms $\frac{1}{x}, \frac{2}{x^2}, \dots$ go to 0.
> $$\frac{3 - 0 - 0}{5 + 0 + 0} = \frac{3}{5}$$
> 
> **Result:** Horizontal asymptote at $y = \frac{3}{5}$.

### Example 4: Definition of Derivative
> [!Example] Problem
> Find the derivative of $f(x) = x^2 - 8x + 9$ at the number $a$.
> **Using:** Definition of Derivative.
> 
> **Step 1:** Setup the formula.
> $$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$
> 
> **Step 2:** Expand terms.
> $$f(a+h) = (a+h)^2 - 8(a+h) + 9 = a^2 + 2ah + h^2 - 8a - 8h + 9$$
> $$f(a) = a^2 - 8a + 9$$
> 
> **Step 3:** Subtract and simplify numerator.
> $$f(a+h) - f(a) = 2ah + h^2 - 8h = h(2a + h - 8)$$
> 
> **Step 4:** Evaluate limit.
> $$f'(a) = \lim_{h \to 0} \frac{h(2a + h - 8)}{h} = \lim_{h \to 0} (2a + h - 8) = 2a - 8$$
> .

---

## 7. Summary Recap

| Concept | Notation/Condition | Key Implication |
| :--- | :--- | :--- |
| **Limit Existence** | $\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$ | Limit exists only if one-sided limits match. |
| **Continuity** | $\lim_{x \to a} f(x) = f(a)$ | No holes, jumps, or asymptotes at $a$. |
| **IVT** | $f$ cont. on $[a,b]$, $N$ between $f(a), f(b)$ | $f(c) = N$ for some $c \in (a,b)$ (Existence of roots). |
| **Vertical Asymptote** | $\lim_{x \to a} f(x) = \pm \infty$ | Function explodes near $a$. Check denominator roots. |
| **Horiz. Asymptote** | $\lim_{x \to \infty} f(x) = L$ | End behavior. Compare degrees of numerator/denom. |
| **Derivative** | $f'(a) = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h}$ | Slope of tangent at $x=a$. |