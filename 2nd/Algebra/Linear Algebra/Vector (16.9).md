# 🧮 Vector  

## [[Definition: Vector]] in $\mathbb{R}^n$  

A **vector** is an ordered list of numbers (called *components*) that represents a **magnitude** and **direction** in space.  
For $\vec{u} \in \mathbb{R}^n$:  
$$
\vec{u} = (u_1, u_2, \dots, u_n)
$$

Two vectors are **equal** if their corresponding components are equal.  
$$
\vec{u} = \vec{v} \iff u_i = v_i, \forall i
$$

---

## [[Basic Operations]] ⚙️  

Given $\vec{u}, \vec{v} \in \mathbb{R}^n$, and $\alpha \in \mathbb{R}$  

1️⃣ **Addition**  
$$
\vec{u} + \vec{v} = (u_1 + v_1, u_2 + v_2, \dots, u_n + v_n)
$$  

2️⃣ **Scalar Multiplication**  
$$
\alpha \vec{u} = (\alpha u_1, \alpha u_2, \dots, \alpha u_n)
$$  

3️⃣ **Zero Vector**  
$$
\vec{0} = (0, 0, \dots, 0)
$$  

---

## [[Properties of Vector Operations]] 📏  

- **Commutative:** $\vec{u} + \vec{v} = \vec{v} + \vec{u}$  
- **Associative:** $\vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w}$  
- **Distributive:** $\alpha(\vec{u} + \vec{v}) = \alpha\vec{u} + \alpha\vec{v}$  
- **Identity:** $\vec{u} + \vec{0} = \vec{u}$  
- **Inverse:** $\vec{u} + (-\vec{u}) = \vec{0}$  

---

## [[Coordinates and Unit Vectors]] 📍  

In $\mathbb{R}^2$:  
$$
\vec{u} = x e_1 + y e_2, \quad e_1 = (1,0), e_2 = (0,1)
$$  
In $\mathbb{R}^3$:  
$$
\vec{u} = x e_1 + y e_2 + z e_3, \quad e_3 = (0,0,1)
$$

$\{e_1, e_2, e_3\}$ forms the **standard basis**.

---

## [[Vector from Two Points]] 📐  

Given $A(x_a, y_a)$ and $B(x_b, y_b)$, the vector from A to B is:  
$$
\vec{AB} = (x_b - x_a, y_b - y_a)
$$  

> 💡 Direction → from A to B  
> Magnitude → distance between A and B

---

## [[Magnitude (Norm)]] 🧭  

The **length** or **magnitude** of a vector $\vec{u} = (x_1, x_2, \dots, x_n)$ is:
$$
|\vec{u}| = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}
$$  

If $|\vec{u}| = 1$, then $\vec{u}$ is a **unit vector**.

---

## [[Dot Product (Scalar Product)]] ⚔️  

Given $\vec{u}=(u_1,u_2,\dots,u_n)$ and $\vec{v}=(v_1,v_2,\dots,v_n)$:
$$
\vec{u}\cdot\vec{v} = u_1v_1 + u_2v_2 + \dots + u_nv_n
$$

### Geometric Interpretation:
$$
\vec{u}\cdot\vec{v} = |\vec{u}|\,|\vec{v}|\cos\theta
$$
where $\theta$ is the angle between $\vec{u}$ and $\vec{v}$.

### Orthogonality:
$$
\vec{u}\cdot\vec{v}=0 \iff \vec{u} \perp \vec{v}
$$

---

### 🧩 Example 1 — Orthogonality and Angle

Given:
$$
\vec{u}=(2,1,-1), \quad \vec{v}=(1,-3,2)
$$

Compute the dot product and the angle between them.

**Solution:**
$$
\vec{u}\cdot\vec{v} = 2(1) + 1(-3) + (-1)(2) = -3
$$
$$
|\vec{u}| = \sqrt{2^2 + 1^2 + (-1)^2} = \sqrt{6}, \quad |\vec{v}| = \sqrt{1^2 + (-3)^2 + 2^2} = \sqrt{14}
$$
$$
\cos\theta = \frac{-3}{\sqrt{6}\sqrt{14}} \Rightarrow \boxed{\theta \approx 112.9^\circ}
$$

✅ Since $\vec{u}\cdot\vec{v}<0$, the angle is **obtuse**.

---

## [[Cross Product]] (for $\mathbb{R}^3$) 🔁  

Given $\vec{u}=(u_1,u_2,u_3)$ and $\vec{v}=(v_1,v_2,v_3)$:
$$
\vec{u}\times\vec{v}=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
u_1 & u_2 & u_3\\
v_1 & v_2 & v_3
\end{vmatrix}
=(u_2v_3-u_3v_2)\hat{i}-(u_1v_3-u_3v_1)\hat{j}+(u_1v_2-u_2v_1)\hat{k}
$$

The result is a **vector perpendicular** to both $\vec{u}$ and $\vec{v}$.

---

### 🧩 Example 2 — Area of Parallelogram  

Let $\vec{u}=(1,2,3)$ and $\vec{v}=(2,0,1)$.  

Compute the **area of the parallelogram** spanned by them.

$$
\vec{u}\times\vec{v} =
\begin{vmatrix}
\hat{i}&\hat{j}&\hat{k}\\
1&2&3\\
2&0&1
\end{vmatrix}
= (2\cdot1-3\cdot0)\hat{i} - (1\cdot1-3\cdot2)\hat{j} + (1\cdot0-2\cdot2)\hat{k}
= (2, 5, -4)
$$
$$
|\vec{u}\times\vec{v}| = \sqrt{2^2 + 5^2 + (-4)^2} = \sqrt{45} = 3\sqrt{5}
$$
✅ **Area:** $\boxed{3\sqrt{5}}$

---

## [[Projection of a Vector]] 🎯  

Projection of $\vec{u}$ onto $\vec{v}$:
$$
\text{proj}_{\vec{v}}(\vec{u}) = \frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\vec{v}
$$

---

### 🧩 Example 3 — Projection and Decomposition

Let $\vec{u} = (3,4)$ and $\vec{v}=(1,2)$.

Compute $\text{proj}_{\vec{v}}(\vec{u})$ and the component of $\vec{u}$ orthogonal to $\vec{v}$.

$$
\vec{u}\cdot\vec{v}=3(1)+4(2)=11, \quad |\vec{v}|^2=1^2+2^2=5
$$
$$
\text{proj}_{\vec{v}}(\vec{u})=\frac{11}{5}(1,2)=\left(\frac{11}{5},\frac{22}{5}\right)
$$
$$
\text{Orthogonal Component: } \vec{u}_\perp = \vec{u} - \text{proj}_{\vec{v}}(\vec{u}) = (3,4) - \left(\frac{11}{5},\frac{22}{5}\right) = \left(\frac{4}{5},-\frac{2}{5}\right)
$$

✅ Check: $\vec{v}\cdot\vec{u}_\perp = 1\cdot\frac{4}{5} + 2\cdot(-\frac{2}{5}) = 0$  
→ Confirmed orthogonal.

---

## [[Linear Dependence & Independence]] 🧠  

Vectors $\vec{v}_1,\dots,\vec{v}_k$ are **linearly independent** if
$$
\alpha_1\vec{v}_1 + \dots + \alpha_k\vec{v}_k = \vec{0} \Rightarrow \alpha_1=\dots=\alpha_k=0
$$

Otherwise, they are **dependent**.

---

### 🧩 Example 4 — Linear Independence Check  

Let $\vec{v}_1=(1,2,3)$, $\vec{v}_2=(2,4,6)$, $\vec{v}_3=(1,0,1)$.  
Check if $\{\vec{v}_1,\vec{v}_2,\vec{v}_3\}$ is linearly independent.

Form the equation:
$$
\alpha_1\vec{v}_1+\alpha_2\vec{v}_2+\alpha_3\vec{v}_3=\vec{0}
$$
$$
\Rightarrow
\begin{bmatrix}
1&2&1\\
2&4&0\\
3&6&1
\end{bmatrix}
\begin{bmatrix}\alpha_1\\\alpha_2\\\alpha_3\end{bmatrix} = \vec{0}
$$

Row-reduce:
$$
R_2-2R_1, \; R_3-3R_1 \Rightarrow
\begin{bmatrix}
1&2&1\\
0&0&-2\\
0&0&-2
\end{bmatrix}
\Rightarrow
\alpha_3 \text{ is free } \Rightarrow \text{Dependent set.}
$$

✅ **Conclusion:** $\boxed{\vec{v}_2 = 2\vec{v}_1}$ → linearly dependent.

---

## [[Geometric Insight]] 🌌  

Vectors represent **directions** and **magnitudes**.  
- **Span** of a set of vectors = all possible linear combinations.  
- If two vectors in $\mathbb{R}^3$ are not multiples, they span a **plane**.  
- If three vectors in $\mathbb{R}^3$ are linearly independent, they span all of $\mathbb{R}^3$.

---

| Concept             | Symbolic Form                                                                         | Interpretation                                       |
| ------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Magnitude           | $\| \vec{u} \| = \sqrt{u_1^2 + \dots + u_n^2}$                                        | Length of the vector                                 |
| Dot Product         | $\vec{u} \cdot \vec{v} = \| \vec{u} \| \| \vec{v} \| \cos\theta$                      | Measures angle similarity                            |
| Cross Product       | $$\vec{u} \times \vec{v}$$                                                            | Vector perpendicular to both $\vec{u}$ and $\vec{v}$ |
| Projection          | $\text{proj}_{\vec{v}}(\vec{u}) = \frac{\vec{u}\cdot\vec{v}}{\| \vec{v} \|^2}\vec{v}$ | Component of $\vec{u}$ along $\vec{v}$               |
| Linear Independence | $\alpha_1 v_1 + \dots + \alpha_k v_k = 0$                                             | No vector can be written as a combination of others  |

---

✨ **Exam Tip:**  
In vector questions, always:  
1. Start by stating the **dimension and space** ($\mathbb{R}^2, \mathbb{R}^3$, etc.)  
2. Write all intermediate steps (especially in dot/cross product)  
3. Conclude with **geometric meaning** (angle, plane, orthogonality)  
→ It demonstrates conceptual mastery, not just computation.
