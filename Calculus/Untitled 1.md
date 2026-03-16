# Applications of Integration

## 1. Areas Between Curves

### 1.1 Vertical Slicing (Functions of $x$)

When calculating the area between two curves $y=f(x)$ and $y=g(x)$, we consider the region bounded by vertical lines $x=a$ and $x=b$.

> [!Definition] Area Formula (Vertical)
> The area $A$ of the region bounded by $y=f(x)$, $y=g(x)$, $x=a$, and $x=b$ where $f(x) \ge g(x)$ on $[a, b]$ is:
> $$A = \int_{a}^{b} [f(x) - g(x)] \, dx$$
> 


### 1.2 Horizontal Slicing (Functions of $y$)

Some regions are geometrically simpler when treated as functions of $y$. This occurs when curves are defined as $x=f(y)$ (Right curve) and $x=g(y)$ (Left curve).

> [!Definition] Area Formula (Horizontal)
> If a region is bounded by the curves $x=f(y)$ (Right, $x_R$) and $x=g(y)$ (Left, $x_L$), and horizontal lines $y=c$ and $y=d$, where $f(y) \ge g(y)$ on $[c, d]$, then:
> $$A = \int_{c}^{d} [f(y) - g(y)] \, dy$$
> 

**Key Strategy:** Always subtract the "Smaller" function from the "Larger" function to ensure the area is positive.
* **Vertical ($dx$):** Top Curve $-$ Bottom Curve.
* **Horizontal ($dy$):** Right Curve $-$ Left Curve. 

### 1.3 Parametric Curves

If the boundary of a region is defined by parametric equations $x=f(t)$ and $y=g(t)$ for $\alpha \le t \le \beta$:

> [!Theorem] Parametric Area Formula
> The area under the curve can be expressed using the parameter $t$:
> $$A = \int_{a}^{b} y \, dx = \int_{\alpha}^{\beta} g(t) f'(t) \, dt$$
> **Note:** Ensure strict attention to the limits of integration corresponding to the traversal of the curve from $x=a$ to $x=b$.
> 

---

## 2. Volumes of Solids

### 2.1 General Slicing Method

This method is used when the shape of the cross-section $A(x)$ is known.

> [!Theorem] Volume by Slicing
> Let $S$ be a solid lying between $x=a$ and $x=b$. If the cross-sectional area of $S$ in a plane perpendicular to the $x$-axis at position $x$ is $A(x)$, and $A$ is continuous, then the volume $V$ is:
> $$V = \int_{a}^{b} A(x) \, dx$$
> 


### 2.2 Solids of Revolution: Disk and Washer Methods

These methods apply when a region is rotated about an axis (e.g., the $x$-axis or $y$-axis).

> [!Method] The Disk Method
> Used when the region is fully solid (no gap between the region and the axis of rotation).
> $$A = \pi (\text{radius})^2$$
> $$V = \int_{a}^{b} \pi [f(x)]^2 \, dx$$
> 

> [!Method] The Washer Method
> Used when there is a "hole" or gap between the region and the axis of rotation.
> $$A = \pi (\text{outer radius})^2 - \pi (\text{inner radius})^2$$
> $$V = \int_{a}^{b} \pi \left( [R_{outer}(x)]^2 - [r_{inner}(x)]^2 \right) \, dx$$
> 

### 2.3 The Method of Cylindrical Shells

This method is an alternative to slicing, often useful when solving $x$ in terms of $y$ is difficult. Instead of slicing the solid perpendicular to the rotation axis, we use concentric cylindrical shells parallel to the axis.

> [!Theorem] Volume by Cylindrical Shells
> For a solid obtained by rotating the region under $y=f(x)$ from $a$ to $b$ about the **y-axis**:
> $$V = \int_{a}^{b} 2\pi x f(x) \, dx$$
> where $0 \le a \le b$.
> 

**Geometric Interpretation of the Integrand:**
* **Circumference:** $2\pi x$ (where $x$ is the radius of the shell).
* **Height:** $f(x)$ (height of the shell).
* **Thickness:** $dx$.
* **Total Volume Integral:** $\int (\text{circumference}) \cdot (\text{height}) \cdot (\text{thickness})$. 

---

## 3. Lengths of Curves (Arc Length)

We compute the length $L$ of a curve by integrating the differential arc length $ds$.

### 3.1 Parametric Equations

> [!Formula] Arc Length (Parametric)
> If a smooth curve is defined by $x=f(t), y=g(t)$ for $a \le t \le b$, and traversed exactly once:
> $$L = \int_{a}^{b} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$
> 


### 3.2 Cartesian Functions

If the curve is defined as a function of $x$ or $y$, we treat the independent variable as the parameter.

> [!Formula] Arc Length (Function of x)
> For $y=f(x)$ where $a \le x \le b$:
> $$L = \int_{a}^{b} \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$$
> 

> [!Formula] Arc Length (Function of y)
> For $x=g(y)$ where $c \le y \le d$:
> $$L = \int_{c}^{d} \sqrt{\left(\frac{dx}{dy}\right)^2 + 1} \, dy$$
> 

---

## 4. The Average Value of a Function

> [!Definition] Average Value Formula
> The average value of a function $f(x)$ on the interval $[a, b]$ is defined as:
> $$f_{avg} = \frac{1}{b-a} \int_{a}^{b} f(x) \, dx$$
> 

> [!Theorem] Mean Value Theorem for Integrals
> If $f$ is continuous on $[a, b]$, there exists at least one point $c \in [a, b]$ such that:
> $$f(c) = f_{avg} = \frac{1}{b-a} \int_{a}^{b} f(x) \, dx$$
> Or equivalently: $\int_{a}^{b} f(x) \, dx = f(c)(b-a)$.
> 

---

## 📘 Examples & Applications

### Example 1: Area Between Curves (Standard)
**Using:** Vertical Slicing formula 
**Problem:** Find the area of the region bounded above by $y=e^x$, below by $y=x$, and on the sides by $x=0$ and $x=1$. 

**Solution:**
1.  Identify upper function $f(x) = e^x$ and lower function $g(x) = x$.
2.  Set up the integral with limits $a=0, b=1$.
    $$A = \int_{0}^{1} (e^x - x) \, dx$$
3.  Evaluate the integral:
    $$A = \left[ e^x - \frac{x^2}{2} \right]_{0}^{1}$$
    $$A = \left( e^1 - \frac{1^2}{2} \right) - \left( e^0 - \frac{0^2}{2} \right)$$
    $$A = e - \frac{1}{2} - 1 = e - \frac{3}{2}$$
    **Result:** $e - 1.5$ 

### Example 2: Area Between Curves (Horizontal Slicing)
**Using:** Integration with respect to $y$ 
**Problem:** Find the area enclosed by the line $y=x-1$ and the parabola $y^2 = 2x+6$. 

**Solution:**
1.  Rewrite equations in terms of $y$:
    * Line: $x_R = y+1$ (Right boundary). 
    * Parabola: $x_L = \frac{1}{2}y^2 - 3$ (Left boundary). 
2.  Find intersection points by setting $x_R = x_L$:
    $$y+1 = \frac{1}{2}y^2 - 3 \implies \frac{1}{2}y^2 - y - 4 = 0 \implies y^2 - 2y - 8 = 0$$
    $$(y-4)(y+2) = 0 \implies y = 4, y = -2$$
    Limits are $c=-2$ and $d=4$. 
3.  Set up the integral:
    $$A = \int_{-2}^{4} \left[ (y+1) - \left( \frac{1}{2}y^2 - 3 \right) \right] \, dy$$
4.  Evaluate:
    $$A = \int_{-2}^{4} \left( -\frac{1}{2}y^2 + y + 4 \right) \, dy = 18$$
    **Result:** 18 

### Example 3: Volume of Revolution (Washer Method)
**Using:** Washer Formula 
**Problem:** Find the volume of the solid obtained by rotating the region enclosed by $y=x$ and $y=x^2$ about the x-axis. 

**Solution:**
1.  Identify the radii:
    * Outer radius $R(x) = x$ (the line is further from the axis on $[0,1]$).
    * Inner radius $r(x) = x^2$ (the parabola is closer).
2.  Formula: $A(x) = \pi(x^2 - (x^2)^2) = \pi(x^2 - x^4)$. 
3.  Limits: Intersection at $x=0$ and $x=1$.
4.  Integrate:
    $$V = \int_{0}^{1} \pi (x^2 - x^4) \, dx$$
    $$V = \pi \left[ \frac{x^3}{3} - \frac{x^5}{5} \right]_{0}^{1}$$
    $$V = \pi \left( \frac{1}{3} - \frac{1}{5} \right) = \pi \left( \frac{2}{15} \right)$$
    **Result:** $\frac{2\pi}{15}$ 

### Example 4: Volume of Revolution (Cylindrical Shells)
**Using:** Shell Method Formula 
**Problem:** Find the volume obtained by rotating the region bounded by $y=2x^2 - x^3$ and $y=0$ about the **y-axis**. 

**Solution:**
1.  Identify components for shells:
    * Radius of shell: $x$. 
    * Height of shell: $f(x) = 2x^2 - x^3$. 
2.  Find limits: $2x^2 - x^3 = x^2(2-x) = 0 \implies x=0, x=2$. 
3.  Set up integral:
    $$V = \int_{0}^{2} 2\pi x (2x^2 - x^3) \, dx$$
    $$V = 2\pi \int_{0}^{2} (2x^3 - x^4) \, dx$$
4.  Evaluate:
    $$V = 2\pi \left[ \frac{x^4}{2} - \frac{x^5}{5} \right]_{0}^{2}$$
    Calculation yields $\frac{16\pi}{5}$.
    **Result:** $\frac{16\pi}{5}$ 

### Example 5: Arc Length (Parametric)
**Using:** Parametric Arc Length Formula 
**Problem:** Find the length of the curve $x=t^2, y=t^3$ between $(1,1)$ and $(4,8)$. 

**Solution:**
1.  Determine $t$-limits: $(1,1) \to t=1$; $(4,8) \to t=2$.
2.  Compute derivatives:
    $$\frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2$$
3.  Set up integrand:
    $$\sqrt{(2t)^2 + (3t^2)^2} = \sqrt{4t^2 + 9t^4} = \sqrt{t^2(4+9t^2)} = t\sqrt{4+9t^2}$$
4.  Integrate:
    $$L = \int_{1}^{2} t\sqrt{4+9t^2} \, dt$$
    Using substitution $u=4+9t^2$, result is $\frac{1}{27}(80\sqrt{10} - 13\sqrt{13})$.
    **Result:** $\frac{1}{27}(80\sqrt{10} - 13\sqrt{13})$ 

---

## 5. Summary

| Concept | Formula / Method | Note |
| :--- | :--- | :--- |
| **Area (Vertical)** | $\int_{a}^{b} [f(x) - g(x)] \, dx$ | Top minus Bottom  |
| **Area (Horizontal)** | $\int_{c}^{d} [f(y) - g(y)] \, dy$ | Right minus Left  |
| **Volume (Disk)** | $\int_{a}^{b} \pi [R(x)]^2 \, dx$ | No hole in solid  |
| **Volume (Washer)** | $\int_{a}^{b} \pi ([R_{out}]^2 - [r_{in}]^2) \, dx$ | Solid has a hole  |
| **Volume (Shells)** | $\int_{a}^{b} 2\pi x f(x) \, dx$ | Parallel to rotation axis (y-axis rotation)  |
| **Arc Length** | $\int \sqrt{1 + (f')^2} \, dx$ | For $y=f(x)$  |
| **Average Value** | $\frac{1}{b-a} \int_{a}^{b} f(x) \, dx$ |  |