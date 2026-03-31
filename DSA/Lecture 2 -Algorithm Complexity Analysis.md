# Lecture 2: Algorithm Complexity Analysis

## 1. Conceptual Section

### 1.1. Foundations of Algorithms
> [!Definition] 📖 **Algorithm**
>  An algorithm is a sequence of unambiguous instructions for solving a problem, meaning it obtains a required output for any legitimate input in a finite amount of time.

 The analysis of algorithms is the quantitative study of their performance, primarily in terms of run time and memory usage. 
*  **Run time:** Measured by the number of operations.
*  **Memory usage:** Measured by the abstract "tape length" required.
*  **Problem size ($x$):** The length of the input string required to represent the data.

### 1.2. Abstract Computation Models
 To analyze algorithms objectively, we utilize theoretical models of computation.

> [!Note] 📝 **Turing Machine**
>  An abstract machine defined by a set of procedures, not physical hardware. It consists of:
>
>  **1.** A tape of infinite length.
>  **2.** Finitely many squares of the tape have a single symbol from a finite language.
>  **3.** A read-write head that can read the squares and write in them.
>  **4.** Finite internal states, with instructions dictated by the current state and the symbol encountered.  It can change state, change symbol, move forward, move backward, or halt .

> [!Note] 📝 **Random-Access Machine (RAM) Model**
>  * Simple operations (arithmetic, comparisons, conditionals) take a uniform, constant amount of time.
>  * Data is stored in an infinite array of registers $(0, 1, 2, ...)$.
> * Each register holds $c \log x$ bits (where $x$ is the problem size and $c$ is a constant independent of $x$).

---

### 1.3. Asymptotic Notations
 Asymptotic notations measure the growth rate of a function representing an algorithm's run time as the input size increases. Let $f(x)$ be the function describing our algorithm's complexity, and $g(x)$ be a benchmark function. We analyze their relationship using limits:
 $L = \lim_{x\rightarrow\infty}\frac{f(x)}{g(x)}$.

| $L$ Value | Resulting Notation |  Meaning  |
| :--- | :--- | :--- |
| $0$ | $o(g(x)), O(g(x))$ | $f < g$ or $f \le g$ |
| $(0, \infty)$ | $\Omega(g(x)), \Theta(g(x)), O(g(x))$ | $f \ge g$, $f = g$, $f \le g$ |
| $\infty$ | $\Omega(g(x)), \omega(g(x))$ | $f \ge g$, $f > g$ |

> [!Definition] 📖 **Big-Oh ($O$) - Asymptotic Upper Bound**
>  $f$ is asymptotically bounded **ABOVE** by $g$ up to a constant factor $C$.
> $$f(x) \in O(g(x)) \iff \exists c > 0 \text{ and } \exists x_0 > 0 : \forall x \ge x_0, |f(x)|  \le c g(x)$$ 

> [!Definition] 📖 **Big-Omega ($\Omega$) - Asymptotic Lower Bound**
>  $f$ is asymptotically bounded **BELOW** by $g$.
>  $$f(x) \in \Omega(g(x)) \iff \exists c > 0 \text{ and } \exists x_0 > 0 : \forall x \ge x_0, f(x) \ge c g(x)$$ 
>  *Property:* $f(x) = \Omega(g(x)) \Leftrightarrow g(x) = O(f(x))$.

> [!Definition] 📖 **Big-Theta ($\Theta$) - Asymptotic Tight Bound**
>  $f$ is asymptotically bounded by $g$ both **ABOVE** (with constant factor $c_2$) and **BELOW** (with constant factor $c_1$).
>  $$f(x) \in \Theta(g(x)) \iff \exists c_1, c_2 > 0 \text{ and } \exists x_0 > 0 : \forall x \ge x_0, c_1 g(x) \le f(x) \le c_2 g(x)$$ 
>  *Property:* $f(x) = \Theta(g(x)) \Leftrightarrow g(x) = O(f(x)) \text{ and } f(x) = O(g(x))$.

> [!Definition] 📖 **Little-Oh ($o$) - Strict Upper Bound**
>  $f$ is asymptotically dominated by $g$ (for **ANY** constant factor $c$).
>  $$f(x) \in o(g(x)) \iff \forall c > 0 \text{ and } \exists x_0 > 0 : \forall x \ge x_0, f(x) \le c g(x)$$ 
>  *Limit test:* $\lim_{x\rightarrow\infty}\frac{f(x)}{g(x)} = 0$.

> [!Definition] 📖 **Little-Omega ($\omega$) - Strict Lower Bound**
>  $f$ asymptotically dominates $g$.
>  $$f(x) \in \omega(g(x)) \iff \forall c > 0 \text{ and } \exists x_0 > 0 : \forall x \ge x_0, f(x) \ge c g(x)$$ 
>  *Limit test:* $\lim_{x\rightarrow\infty}\frac{f(x)}{g(x)} = \infty$.

### 1.4. Common Function Orders
 Algorithms are typically classified into the following growth rates:

**1.** $O(1)$: Constant
**2.** $O(\log \log n)$: double logarithmic
**3.** $O(\log n)$: logarithmic
**4.** $O(\log^c n), c > 1$: polylogarithmic
**5.** $O(n^\alpha), 0 < \alpha < 1$: fractional power
**6.** $O(n)$: Linear
**7.** $O(n \log n)$: Quasilinear
**8.** $O(n^2)$: Quadratic
**9.** $O(n^c), 1 < c$: Polynomial
**10.** $O(c^n), c > 1$: Exponential
**11.** $O(n!)$: factorial

---

## 2. 📘 Examples & Applications (Exam Mode)

 ### Part 1: Proof Practice

> [!Example] 📘 Proving Polynomial Bounds
> **Using:** Limit Theorem
> **Problem:** Prove that $n^3 + 1000n^2 = O(n^4)$.
> **Solution:**
> We evaluate the limit $L = \lim_{n \to \infty} \frac{f(n)}{g(n)}$.
>
> **1.** Set up the limit: $\lim_{n \to \infty} \frac{n^3 + 1000n^2}{n^4}$
> **2.** Simplify the fraction: $\lim_{n \to \infty} \left( \frac{1}{n} + \frac{1000}{n^2} \right)$
> **3.** Evaluate: As $n \to \infty$, both terms approach 0. Thus, $L = 0$.
> **4.** **Conclusion:** Because $L = 0$, $f(n)$ is strictly bounded above by $g(n)$. This satisfies $o(n^4)$, which inherently implies $O(n^4)$.

> [!Example] 📘 Proving Logarithmic vs Linear Bounds
> **Using:** Limit Theorem & L'Hôpital's Rule
> **Problem:** Prove that $\log n = O(n)$.
> **Solution:**
>
> **1.** Set up the limit: $L = \lim_{n \to \infty} \frac{\log n}{n}$
> **2.** Apply L'Hôpital's rule (taking the derivative of the numerator and denominator): $\lim_{n \to \infty} \frac{1/n}{1}$
> **3.** Evaluate: $\lim_{n \to \infty} \frac{1}{n} = 0$.
> **4.** **Conclusion:** Since $L = 0$, $\log n$ grows asymptotically slower than $n$, proving $\log n = O(n)$.

> [!Example] 📘 Proving Logarithmic vs Fractional Power Bounds
> **Using:** Limit Theorem & L'Hôpital's Rule
> **Problem:** Prove that $\log n = O(\sqrt{n})$.
> **Solution:**
>
> **1.** Set up the limit: $L = \lim_{n \to \infty} \frac{\log n}{n^{0.5}}$
> **2.** Apply L'Hôpital's rule: $\lim_{n \to \infty} \frac{1/n}{0.5n^{-0.5}} = \lim_{n \to \infty} \frac{1}{0.5 n^{0.5}}$
> **3.** Simplify: $\lim_{n \to \infty} \frac{2}{\sqrt{n}}$
> **4.** Evaluate: As $n \to \infty$, the fraction approaches $0$.
> **5.** **Conclusion:** Since $L = 0$, $\log n = O(\sqrt{n})$.

> [!Example] 📘 Proving Factorial Bounds are Not Polynomial
> **Using:** Limit Theorem & Limit Ratio Test
> **Problem:** Prove that $n! \notin O(n^c)$ for any positive constant $c$.
> **Solution:**
> We must show that $\lim_{n \to \infty} \frac{n!}{n^c} = \infty$.
>
> **1.** Let $a_n = \frac{n!}{n^c}$. We examine the ratio of consecutive terms: $\lim_{n \to \infty} \frac{a_{n+1}}{a_n}$.
> **2.** Expand the ratio: $\lim_{n \to \infty} \frac{(n+1)! / (n+1)^c}{n! / n^c} = \lim_{n \to \infty} \frac{n!(n+1) \cdot n^c}{n! \cdot (n+1)^c}$.
> **3.** Simplify: $\lim_{n \to \infty} (n+1) \left(\frac{n}{n+1}\right)^c = \lim_{n \to \infty} (n+1) \left(1 - \frac{1}{n+1}\right)^c$.
> **4.** Evaluate: As $n \to \infty$, $\left(1 - \frac{1}{n+1}\right)^c \to 1^c = 1$, but $(n+1) \to \infty$. Thus, the ratio diverges to $\infty$.
> **5.** **Conclusion:** Because the function grows to infinity relative to $n^c$, $n!$ is strictly greater than any polynomial. It is not bounded above by $O(n^c)$.

> [!Example] 📘 Proving Polynomial vs Exponential Bounds
> **Using:** Limit Theorem & L'Hôpital's Rule
> **Problem:** Prove that $n^a = O(b^n)$ for any positive constants $a$ and $b > 1$.
> **Solution:**
>
> **1.** Set up the limit: $L = \lim_{n \to \infty} \frac{n^a}{b^n}$.
> **2.** Apply L'Hôpital's rule repeatedly ($\lceil a \rceil$ times).
> **3.** The $k$-th derivative of $n^a$ is $a(a-1)\dots(a-k+1)n^{a-k}$. The $k$-th derivative of $b^n$ is $b^n (\ln b)^k$.
> **4.** Eventually, the exponent in the numerator becomes $\le 0$, making the numerator a constant or approaching $0$, while the denominator $b^n (\ln b)^k \to \infty$ (since $b>1, \ln b > 0$).
> **5.** Evaluate: The overall limit is $0$.
> **6.** **Conclusion:** Since $L = 0$, $n^a = O(b^n)$.

> [!Example] 📘 Proving Tight Bounds for Factorial Logarithms
> **Using:** Big-Theta Formal Bounding ($O$ and $\Omega$)
> **Problem:** Prove that $\log n! = \Theta(n \log n)$.
> **Solution:**
> We must prove both upper ($O$) and lower ($\Omega$) bounds.
>
> **1. Prove $O(n \log n)$ (Upper Bound):**
>    We know $n! = n \times (n-1) \times \dots \times 1 \le n \times n \times \dots \times n = n^n$.
>    Taking the log of both sides: $\log(n!) \le \log(n^n) = n \log n$.
>    Thus, $\log n! = O(n \log n)$ (using $c_2 = 1, x_0 = 1$).
> **2. Prove $\Omega(n \log n)$ (Lower Bound):**
>    Consider only the largest half of the terms in the factorial:
>    $n! = n \times (n-1) \times \dots \times 1 \ge n \times (n-1) \times \dots \times \frac{n}{2} \times 1 \times \dots \times 1$.
>    There are $\frac{n}{2}$ terms that are strictly greater than or equal to $\frac{n}{2}$.
>    Thus, $n! \ge (\frac{n}{2})^{\frac{n}{2}}$.
>    Taking the log of both sides: $\log(n!) \ge \log((\frac{n}{2})^{\frac{n}{2}}) = \frac{n}{2} \log(\frac{n}{2}) = \frac{n}{2}(\log n - \log 2)$.
>    For large $n$, $\frac{n}{2}(\log n - 1) \ge c_1(n \log n)$.
>    Thus, $\log n! = \Omega(n \log n)$.
> **3. Conclusion:** Since $\log n!$ is both $O(n \log n)$ and $\Omega(n \log n)$, it is exactly $\Theta(n \log n)$.

> [!Example] 📘 Proving Big-Theta Tight Bounds
> **Using:** Limit Theorem
> **Problem:** Prove that $1000x^3 - x^2 + 79 = \Theta(x^3)$.
> **Solution:**
>
> **1.** Set up the limit: $L = \lim_{x \to \infty} \frac{1000x^3 - x^2 + 79}{x^3}$
> **2.** Simplify: $\lim_{x \to \infty} \left( 1000 - \frac{1}{x} + \frac{79}{x^3} \right)$
> **3.** Evaluate: The fractional terms go to 0, leaving $L = 1000$.
> **4.** **Conclusion:** Because $0 < 1000 < \infty$, the functions grow at the same asymptotic rate, confirming tight bounds $\Theta(x^3)$.

---

### Part 2: Property Proofs

> [!Example] 📘 Addition Property of Big-Oh
> **Using:** Big-Oh Definition Bounds
> **Problem:** Prove $af(x) + bg(x) = O(h(x))$ given $f(x)=O(h(x))$ and $g(x)=O(h(x))$, where $a, b > 0$.
> **Solution:**
>
> **1.** From definitions: $\exists c_1, x_1$ such that $f(x) \le c_1 h(x)$ for all $x \ge x_1$.
> **2.** And $\exists c_2, x_2$ such that $g(x) \le c_2 h(x)$ for all $x \ge x_2$.
> **3.** Let $x_0 = \max(x_1, x_2)$. For all $x \ge x_0$, multiply the inequalities by constants $a$ and $b$: $af(x) \le ac_1 h(x)$ and $bg(x) \le bc_2 h(x)$.
> **4.** Add them together: $af(x) + bg(x) \le ac_1 h(x) + bc_2 h(x) = (ac_1 + bc_2)h(x)$.
> **5.** **Conclusion:** Let constant $C = ac_1 + bc_2$. Because $C > 0$, we have bounded the expression, proving $af(x) + bg(x) = O(h(x))$.

> [!Example] 📘 Multiplication Property of Big-Oh
> **Using:** Big-Oh Definition Bounds
> **Problem:** Prove $f_1(x)f_2(x) = O(g_1(x)g_2(x))$ given $f_1(x)=O(g_1(x))$ and $f_2(x)=O(g_2(x))$.
> **Solution:**
>
> **1.** From definitions: $\exists c_1, x_1$ such that $f_1(x) \le c_1 g_1(x)$ for all $x \ge x_1$.
> **2.** And $\exists c_2, x_2$ such that $f_2(x) \le c_2 g_2(x)$ for all $x \ge x_2$.
> **3.** Let $x_0 = \max(x_1, x_2)$. For all $x \ge x_0$, multiply the inequalities: $f_1(x)f_2(x) \le (c_1 g_1(x))(c_2 g_2(x))$.
> **4.** Rearrange: $f_1(x)f_2(x) \le (c_1 c_2) (g_1(x)g_2(x))$.
> **5.** **Conclusion:** Let $C = c_1 c_2$. We have found a constant $C$ that satisfies the Big-Oh definition.

---

### Part 3: Code Analysis

> [!Example] 📘 Code Analysis 1: Logarithmic Operations
> **Using:** Halving Loop Trajectory
> **Problem:** Determine the asymptotic complexity of:
> `while(y) { if(y%2==1) result*=x; x*=x; y/=2; }`
> **Solution:**
>
> **1.** **Analyze the control variable:** The loop variable `y` is halved during every iteration (`y /= 2`).
> **2.** **Determine Iterations:** A variable initialized to $y$ and halved continuously will reach $0$ (via integer division) in exactly $\lfloor \log_2 y \rfloor + 1$ iterations.
> **3.** **Analyze loop body:** The operations inside the loop (modulo check, assignment, multiplication, division) all execute in constant $O(1)$ time.
> **4.** **Conclusion:** Total operations equal Iterations $\times$ Body Complexity $= (\log_2 y) \times O(1) = \Theta(\log y)$.

> [!Example] 📘 Code Analysis 2: Matrix Operations
> **Using:** Nested Loop Summations
> **Problem:** Determine the asymptotic complexity of:
> `for(i=0; i<n; i++) for(j=0; j<n; j++) { C[i][j]=0; for(k=0; k<n; k++) C[i][j]=C[i][j]+A[i][k]*B[k][j]; }`
> **Solution:**
>
> **1.** **Set up summations:** The code represents standard matrix multiplication.
> **2.** The outer loop ($i$) runs $n$ times. The middle loop ($j$) runs $n$ times. The initialization `C[i][j]=0` executes $n \times n = n^2$ times.
> **3.** The inner loop ($k$) runs $n$ times *inside* the outer two loops.
> **4.** **Summation Model:** $\sum_{i=0}^{n-1} \sum_{j=0}^{n-1} \sum_{k=0}^{n-1} 1 = n \times n \times n = n^3$.
> **5.** **Conclusion:** The total number of dominant operations is $n^3 + n^2$. Taking the highest order term, the complexity is $\Theta(n^3)$.

> [!Example] 📘 Code Analysis 3: Geometric Outer Loop
> **Using:** Geometric Series Summation
> **Problem:** Determine the asymptotic complexity of:
> `for(int n=N; n>0; n/=2) for(int i=0; i<n; i++) sum++;`
> **Solution:**
>
> **1.** **Analyze Outer Loop:** The variable $n$ takes the sequence of values $N, \frac{N}{2}, \frac{N}{4}, \frac{N}{8}, \dots, 1$.
> **2.** **Analyze Inner Loop:** For each value of $n$, the inner loop executes exactly $n$ times, adding $n$ to the total operation count.
> **3.** **Set up Summation:** Total operations $= N + \frac{N}{2} + \frac{N}{4} + \dots + 1$.
> **4.** **Evaluate Series:** This is a geometric series sum: $N \left(1 + \frac{1}{2} + \frac{1}{4} + \dots \right)$. The infinite sum of $(1/2)^k$ converges to $2$.
> **5.** Therefore, the sum evaluates strictly to $\le 2N$.
> **6.** **Conclusion:** Because the total operations are bounded linearly by a constant factor of $2$, the time complexity is $\Theta(N)$.

---

## 3. Summary Section
* **Performance Tracking:** Algorithms are fundamentally evaluated via abstract memory (tape) and operation counts in theoretical computation models .
* **Limits Determine Bounds:** Use $L = \lim_{x\rightarrow\infty}\frac{f(x)}{g(x)}$ to classify tight, upper, or lower asymptotic relations definitively .
* **Formal Proof Structures:** Bounds must be mathematically justified by identifying specific constants $(c, x_0)$ that satisfy the structural inequalities as $x \to \infty$.
* **Summation Tools for Iteration:** Iterative loops are reliably converted into mathematical summations ($\sum$) to reveal their exact polynomial, logarithmic, or quasilinear complexities .