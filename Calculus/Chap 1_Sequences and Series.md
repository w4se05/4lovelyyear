## 1. Sequences (Conceptual)

### Definitions and Limits

> [!Definition] Sequence
> A **sequence** is a list of numbers written in a definite order:
> $$a_{1}, a_{2}, a_{3}, ..., a_{n}, ...$$
> denoted as $\{a_{n}\}$.
> * $a_n$: The $n$-th term.
> * **Infinite sequence:** $\{a_{n}\}_{n=1}^{\infty}$, where every term has a successor.
> * **General Term:** A formula representing $a_n$ in terms of $n$ (e.g., $a_n = \frac{n}{n+1}$).

> [!Definition] Limit of a Sequence
> A sequence $\{a_{n}\}$ has the **limit** $L$ if for every $\epsilon > 0$, there exists an integer $N$ such that for all $n > N$:
> $$|a_{n} - L| < \epsilon$$
> We write $\lim_{n\rightarrow\infty}a_{n}=L$ or $a_{n}\rightarrow L$ .

> [!Note] Convergence vs. Divergence
> * **Convergent:** If $\lim_{n\rightarrow\infty}a_{n}=L$ (limit exists and is unique).
> * **Divergent to Infinity:** If $\lim_{n\rightarrow\infty}a_{n}=\pm\infty$.
> * **Divergent:** If the limit does not exist (e.g., oscillates like $(-1)^n$).

### Special Sequences

> [!Example] Geometric Sequence
> A sequence of the form $a, ar, ar^2, ...$ where $a \neq 0$ is the first term and $r \neq 0$ is the **common ratio**.
> * **General term:** $a_n = ar^{n-1}$.
> * **Limit Property:** If $|r| < 1$, then $\lim_{n\rightarrow\infty}r^n = 0$.

> [!Example] Arithmetic Sequence
> A sequence of the form $a, a+d, a+2d, ...$ where $d$ is the **common difference**.
> * **General term:** $a_n = a + (n-1)d$.

### Theorems for Sequences

> [!Theorem] Limit Laws
> If $\lim a_n = A$ and $\lim b_n = B$, then:
> 1.  $\lim(a_n \pm b_n) = A \pm B$.
> 2.  $\lim(c a_n) = cA$ (where $c \in \mathbb{R}$).
> 3.  $\lim(a_n b_n) = AB$.
> 4.  $\lim(\frac{a_n}{b_n}) = \frac{A}{B}$ (if $B \neq 0$).

> [!Theorem] Squeeze Theorem
> Let $\{a_n\}, \{b_n\}, \{c_n\}$ be sequences such that $a_n \le b_n \le c_n$ for all $n \ge N$.
> If $\lim_{n\rightarrow\infty}a_{n} = L$ and $\lim_{n\rightarrow\infty}c_{n} = L$, then:
> $$\lim_{n\rightarrow\infty}b_{n} = L$$
> .

> [!Theorem] Convergence via Subsequences
> * If the subsequences of even indices ($a_{2k}$) and odd indices ($a_{2k-1}$) both converge to the **same limit** $L$, the whole sequence converges to $L$ .
> * If they converge to **different** limits, the sequence diverges.

> [!Theorem] Weierstrass Monotone Convergence Theorem
> * **Bounded:** A sequence is bounded if $|a_n| \le M$ for some $M > 0$.
> * **Monotone:** A sequence is monotone if it is entirely increasing ($a_{n+1} \ge a_n$) or decreasing ($a_{n+1} \le a_n$) .
> * **Theorem:** Every **bounded monotone** sequence is convergent.
> * **Application (Number $e$):** The sequence $a_n = (1 + \frac{1}{n})^n$ is increasing and bounded, converging to $e$.

---

## 2. Infinite Series (Conceptual)

### Definitions

> [!Definition] Infinite Series
> An expression of the sum of a sequence $\{a_n\}$:
> $$\sum_{n=1}^{\infty}a_{n} = a_{1} + a_{2} + a_{3} + \cdot\cdot\cdot$$
> .

> [!Definition] Partial Sums & Convergence
> The **$n$-th partial sum** is $s_{n} = \sum_{k=1}^{n}a_{k}$.
> * If the sequence of partial sums $\{s_n\}$ has a finite limit $s$, the series **converges** to $s$: $\sum_{n=1}^{\infty}a_{n} = s$.
> * If the limit does not exist, the series **diverges**.

### Fundamental Series Types

> [!Tip] Geometric Series
> Form: $\sum_{n=0}^{\infty}ar^{n} = a + ar + ar^2 + ...$ ($a \neq 0$).
> * **Converges** if $|r| < 1$. Sum = $\frac{a}{1-r}$.
> * **Diverges** if $|r| \ge 1$.

> [!Tip] p-Series
> Form: $\sum_{n=1}^{\infty}\frac{1}{n^{p}}$.
> * **Converges** if $p > 1$.
> * **Diverges** if $p \le 1$.
> * **Harmonic Series ($p=1$):** $\sum \frac{1}{n}$ diverges.

> [!Theorem] Test for Divergence ($n$-th Term Test)
> If $\sum a_n$ converges, then $\lim_{n\rightarrow\infty}a_{n} = 0$.
> **Contrapositive (The Test):** If $\lim_{n\rightarrow\infty}a_{n} \neq 0$ (or does not exist), then $\sum a_n$ **diverges**.
> *Warning:* If limit is 0, the test is inconclusive (e.g., Harmonic series limit is 0 but diverges).

---

## 3. Convergence Tests (Teach Mode)

### Comparison Tests
1.  **Direct Comparison Test:** Suppose $0 \le a_n \le b_n$.
    * If $\sum b_n$ (larger) converges $\implies \sum a_n$ converges.
    * If $\sum a_n$ (smaller) diverges $\implies \sum b_n$ diverges .
2.  **Limit Comparison Test (LCT):** If $a_n, b_n > 0$ and $\lim_{n\rightarrow\infty}\frac{a_n}{b_n} = c$ where $0 < c < \infty$:
    * Both series converge OR both series diverge .

### Absolute Convergence Tests
> [!Definition] Absolute vs. Conditional
> * **Absolute Convergence:** $\sum |a_n|$ converges. This implies $\sum a_n$ converges.
> * **Conditional Convergence:** $\sum a_n$ converges, but $\sum |a_n|$ diverges.

1.  **Ratio Test:** Let $L = \lim_{n\rightarrow\infty}|\frac{a_{n+1}}{a_{n}}|$.
    * $L < 1$: Converges absolutely.
    * $L > 1$ or $\infty$: Diverges.
    * $L = 1$: Inconclusive .
2.  **Root Test:** Let $L = \lim_{n\rightarrow\infty}\sqrt[n]{|a_{n}|}$.
    * $L < 1$: Converges absolutely.
    * $L > 1$ or $\infty$: Diverges.
    * $L = 1$: Inconclusive .

### Alternating Series
**Leibniz Criterion:** For $\sum (-1)^{n-1}b_n$ where $b_n \ge 0$:
The series converges if:
1.  $b_{n+1} \le b_n$ (Decreasing), AND
2.  $\lim_{n\rightarrow\infty}b_n = 0$ .

---

## 4. Power Series (Conceptual)

> [!Definition] Power Series
> A series centered at $a$:
> $$\sum_{n=0}^{\infty}c_{n}(x-a)^{n}$$
### Radius and Interval of Convergence
There exists a **Radius of Convergence ($R$)** such that the series:
1.  Converges for $|x-a| < R$.
2.  Diverges for $|x-a| > R$ .

**Interval of Convergence ($I$):**
The set of all $x$ for which the series converges.
$$I = (a-R, a+R) \cup \{\text{endpoints if convergent}\}$$
.
*Note:* Endpoints ($x = a \pm R$) must be checked individually.

---

## 📘 Examples & Applications (Exam Mode)

### Example 1: Finding the General Term of a Sequence
> [!Example] Problem
> Find the formula for the sequence: $\frac{3}{5}, -\frac{4}{25}, \frac{5}{125}, -\frac{6}{625}, ...$.
> **Analysis:**
> * **Numerator:** $3, 4, 5, 6...$ increases by 1. If $n=1$, numerator is $n+2$.
> * **Denominator:** $5, 25, 125, 625...$ are powers of 5. If $n=1$, denominator is $5^n$.
> * **Signs:** $+ - + -$ indicates an alternating term like $(-1)^{n-1}$ (starts positive).
>
> **Solution:**
> $$a_{n} = (-1)^{n-1}\frac{n+2}{5^{n}}$$
> .

### Example 2: Squeeze Theorem Application
> [!Example] Problem
> Determine the limit of $a_{n} = \frac{(-1)^{n}}{2\sqrt{n}}$.
> **Using:** Squeeze Theorem.
>
> **Step 1:** Establish bounds.
> Since $-1 \le (-1)^n \le 1$, we have:
> $$-\frac{1}{2\sqrt{n}} \le a_{n} \le \frac{1}{2\sqrt{n}}$$
> .
>
> **Step 2:** Take limits of bounds.
> $$\lim_{n\rightarrow\infty} -\frac{1}{2\sqrt{n}} = 0 \quad \text{and} \quad \lim_{n\rightarrow\infty} \frac{1}{2\sqrt{n}} = 0$$
> .
>
> **Conclusion:** By Squeeze Theorem, $\lim_{n\rightarrow\infty} a_n = 0$.

### Example 3: Telescoping Series
> [!Example] Problem
> Calculate the sum $\sum_{n=1}^{\infty}\frac{1}{n(n+1)}$.
> **Using:** Partial Fractions & Definition of Partial Sums.
>
> **Step 1:** Decompose term.
> $$\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$$
> .
>
> **Step 2:** Write partial sum $s_n$.
> $$s_{n} = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + ... + \left(\frac{1}{n} - \frac{1}{n+1}\right)$$
> The intermediate terms cancel out.
> $$s_{n} = 1 - \frac{1}{n+1}$$
> .
>
> **Step 3:** Take the limit.
> $$\lim_{n\rightarrow\infty} s_n = 1 - 0 = 1$$
> **Result:** The series converges to 1.

### Example 4: Ratio Test for Convergence
> [!Example] Problem
> Test the series $\sum \frac{n!}{2^n}$ for convergence.
> **Using:** Ratio Test.
>
> **Step 1:** Set up limit $L$.
> $$L = \lim_{n\rightarrow\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\rightarrow\infty} \frac{(n+1)!}{2^{n+1}} \cdot \frac{2^n}{n!}$$
>
> **Step 2:** Simplify.
> $$L = \lim_{n\rightarrow\infty} \frac{(n+1)n!}{2 \cdot 2^n} \cdot \frac{2^n}{n!} = \lim_{n\rightarrow\infty} \frac{n+1}{2}$$
>
> **Step 3:** Evaluate.
> $$L = \infty$$
> .
>
> **Conclusion:** Since $L > 1$, the series **diverges**.

### Example 5: Power Series Interval
> [!Example] Problem
> Find the interval of convergence for $\sum_{n=1}^{\infty}(-1)^{n-1}\frac{(x-1)^{n}}{n}$ (Center $a=1$).
> **Using:** Ratio Test & Endpoint Check.
>
> **Step 1:** Ratio Test.
> $$\lim_{n\rightarrow\infty} \left| \frac{(x-1)^{n+1}}{n+1} \cdot \frac{n}{(x-1)^n} \right| = |x-1| \lim_{n\rightarrow\infty} \frac{n}{n+1} = |x-1|$$
> Converges if $|x-1| < 1$, so Radius $R=1$. Range: $(0, 2)$ .
>
> **Step 2:** Check Endpoints ($x=0, x=2$).
> * **At $x=0$:** Series becomes $\sum \frac{-1}{n}$ (Harmonic). **Diverges**.
> * **At $x=2$:** Series becomes $\sum \frac{(-1)^{n-1}}{n}$ (Alternating Harmonic). **Converges**.
>
> **Conclusion:** Interval of Convergence is $I = (0, 2]$.

---

## 5. Summary Recap

| Type                | Form                 | Convergence Condition                        |     |                                              |
| :------------------ | :------------------- | :------------------------------------------- | --- | -------------------------------------------- |
| **Geometric**       | $\sum ar^n$          | Converges if $                               | r   | < 1$. Sum = $\frac{a}{1-r}$.                 |
| **p-Series**        | $\sum \frac{1}{n^p}$ | Converges if $p > 1$. Diverges if $p \le 1$. |     |                                              |
| **Divergence Test** | $\lim a_n$           | If $\lim a_n \neq 0$, Series Diverges.       |     |                                              |
| **Ratio Test**      | $L = \lim            | \frac{a_{n+1}}{a_n}                          | $   | $L < 1$ (Conv), $L > 1$ (Div), $L=1$ (Fail). |
| **Root Test**       | $L = \lim \sqrt[n]{  | a_n                                          | }$  | $L < 1$ (Conv), $L > 1$ (Div), $L=1$ (Fail). |
| **Alternating**     | $\sum (-1)^n b_n$    | Converges if decreasing and $\lim b_n = 0$.  |     |                                              |

**Key Theorem Strategy:**
1.  Check **Divergence Test** first (Is limit 0?).
2.  If it looks geometric or p-series, use those rules.
3.  If it has factorials ($n!$) or exponentials, use **Ratio Test**.
4.  If it has powers of $n$ ($(\dots)^n$), use **Root Test**.
5.  If it is a rational function, use **Comparison Tests**.