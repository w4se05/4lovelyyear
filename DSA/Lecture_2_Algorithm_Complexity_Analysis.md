---
tags: [61CSE108, complexity-analysis]
topic: "Lecture 2: Algorithm Complexity Analysis"
course: "61CSE108: Algorithms and Data Structures"
---
	
# Algorithm Complexity Analysis

> [!Note] 💡 Notation Conventions
> Throughout this note:
> - $n$ denotes the **problem size** (length of the input string / number of elements).
> - $f, g$ denote functions $\mathbb{Z}^+ \to \mathbb{R}^+$ (positive-valued functions of a positive integer variable).
> - All asymptotic statements hold for sufficiently large input; constants $c, c_1, c_2 > 0$ and threshold $x_0 > 0$ are existential unless stated otherwise.
> - $\log$ without a base means $\log_2$ unless context specifies otherwise.

---

## 1. Computational Models

### 1.1 Turing Machine

> [!Definition] 📖 Turing Machine
> A **Turing machine** is an abstract (non-physical) computational model consisting of:
> **1.** A tape of **infinite** length divided into squares.
> **2.** Finitely many squares contain a single symbol from a finite alphabet (language).
> **3.** A **read-write head** that can read and write symbols on the tape.
> **4.** At any moment the machine occupies exactly one of a **finite number of internal states**.
> **5.** A set of instructions that, given the current state and the symbol under the head, determine what to do next:
> - Change internal state
> - Write a new symbol on the current square
> - Move the head **forward** (right)
> - Move the head **backward** (left)
> - **HALT** (stop execution)

> [!Note] 💡 Key Point
> A Turing machine is **abstract** — it is a set of procedures, not a physical device. Informally:
> - **Run time** = number of operations (head moves / state transitions)
> - **Memory usage** = tape length used
> - **Problem size** = length of the input string on the tape

---

### 1.2 RAM Model

> [!Definition] 📖 Random-Access Machine (RAM) Model
> The **RAM model** is the standard idealised model for algorithm analysis:
> **1.** Every **simple operation** (arithmetic, comparison, conditional branch, etc.) takes the same **constant amount of time** — i.e., $O(1)$.
> **2.** Data is stored in an **infinite array of registers** $0, 1, 2, \ldots$, each capable of holding $c \log x$ bits, where $x$ is the problem size and $c$ is a constant independent of $x$.

> [!Note] 💡 Why the RAM Model?
> The RAM model lets us study algorithms independently of any specific hardware, operating system, compiler, or programmer. We count **basic operations** rather than wall-clock seconds.

---

## 2. Algorithms and Algorithm Analysis

> [!Definition] 📖 Algorithm
> An **algorithm** is a sequence of unambiguous instructions for solving a problem — that is, for obtaining a required output for any *legitimate* input in a **finite** amount of time.
>
> $$\text{instance} \;\longrightarrow\; \boxed{\text{Algorithm}} \;\longrightarrow\; \text{output}$$

> [!Definition] 📖 Analysis of Algorithms
> **Analysis of algorithms** is the quantitative study of the performance of algorithms in terms of their **run time**, **memory usage**, or other properties as a function of the input size $n$.

---

## 3. Asymptotic Notations

> [!Note] 💡 Motivation
> We are interested in how algorithm performance **changes** as the problem input size $n$ increases. Asymptotic notations measure the **growth rate** of the run-time function, independent of constant factors or hardware.

### Quick Reference: Limit Characterisation

Let $L = \displaystyle\lim_{x \to \infty} \dfrac{f(x)}{g(x)}$.

| $L$ | $f = o(g)$ | $f = \Omega(g)$ | $f = \Theta(g)$ | $f = O(g)$ | $f = \omega(g)$ |
|-----|:---:|:---:|:---:|:---:|:---:|
| $0$ | ✓ | | | ✓ | |
| $(0, \infty)$ | | ✓ | ✓ | ✓ | |
| $\infty$ | | ✓ | | | ✓ |

Informal interpretation: $f < g$ (asymptotically), $f \geq g$, $f = g$, $f \leq g$, $f > g$.

---

### 3.1 Big-Oh $O$

> [!Definition] 📖 Big-Oh $O(g(x))$
> $f(x) = O(g(x))$ (**$f$ is asymptotically bounded ABOVE by $g$, up to a constant factor**) iff
> $$\exists\, c > 0,\; \exists\, x_0 > 0 : \forall x \geq x_0,\quad |f(x)| \leq c\, g(x).$$
> To **prove** $f(x) \in O(g(x))$: exhibit a specific pair $(c, x_0)$.

> [!Property] ⚙️ Common Function Orders (from slowest to fastest growth)
>
> | Notation | Name |
> |---|---|
> | $O(1)$ | Constant |
> | $O(\log \log n)$ | Double logarithmic |
> | $O(\log n)$ | Logarithmic |
> | $O(\log^c n),\; c > 1$ | Polylogarithmic |
> | $O(n^\alpha),\; 0 < \alpha < 1$ | Fractional power |
> | $O(n)$ | Linear |
> | $O(n \log n)$ | Quasilinear |
> | $O(n^2)$ | Quadratic |
> | $O(n^c),\; c > 1$ | Polynomial |
> | $O(c^n),\; c > 1$ | Exponential |
> | $O(n!)$ | Factorial |

---

### 3.2 Big-Omega $\Omega$

> [!Definition] 📖 Big-Omega $\Omega(g(x))$
> $f(x) = \Omega(g(x))$ (**$f$ is asymptotically bounded BELOW by $g$**) iff
> $$\exists\, c > 0,\; \exists\, x_0 > 0 : \forall x \geq x_0,\quad f(x) \geq c\, g(x).$$
> To **prove** $f(x) \in \Omega(g(x))$: exhibit a specific pair $(c, x_0)$.

> [!Property] ⚙️ Equivalence
> $$f(x) = \Omega(g(x)) \;\Longleftrightarrow\; g(x) = O(f(x)).$$

---

### 3.3 Big-Theta $\Theta$

> [!Definition] 📖 Big-Theta $\Theta(g(x))$
> $f(x) = \Theta(g(x))$ (**$f$ is asymptotically bounded both ABOVE and BELOW by $g$**) iff
> $$\exists\, c_1, c_2 > 0,\; \exists\, x_0 > 0 : \forall x \geq x_0,\quad c_1\, g(x) \leq f(x) \leq c_2\, g(x).$$
> To **prove**: exhibit a specific triple $(c_1, c_2, x_0)$.

> [!Property] ⚙️ Equivalence
> $$f(x) = \Theta(g(x)) \;\Longleftrightarrow\; f(x) = O(g(x)) \text{ and } f(x) = \Omega(g(x)).$$

---

### 3.4 Little-Oh $o$

> [!Definition] 📖 Little-Oh $o(g(x))$
> $f(x) = o(g(x))$ (**$f$ is asymptotically dominated by $g$, for ANY constant factor**) iff
> $$\forall\, c > 0,\; \exists\, x_0 > 0 : \forall x \geq x_0,\quad f(x) \leq c\, g(x).$$
> To **prove**: for every $c > 0$, find an $x_0$ that works.

> [!Property] ⚙️ Limit Characterisation
> $$f(x) = o(g(x)) \;\Longleftrightarrow\; \lim_{x \to \infty} \frac{f(x)}{g(x)} = 0.$$

---

### 3.5 Little-Omega $\omega$

> [!Definition] 📖 Little-Omega $\omega(g(x))$
> $f(x) = \omega(g(x))$ (**$f$ asymptotically dominates $g$**) iff
> $$\forall\, c > 0,\; \exists\, x_0 > 0 : \forall x \geq x_0,\quad f(x) \geq c\, g(x).$$

> [!Property] ⚙️ Limit Characterisation
> $$f(x) = \omega(g(x)) \;\Longleftrightarrow\; \lim_{x \to \infty} \frac{f(x)}{g(x)} = \infty.$$

---

## 4. Analysing Iterative Algorithms

> [!Definition] 📖 Summation Method
> For an iterative algorithm, let $a_i$ be the number of operations (comparisons and assignments) at iteration $i$. The total cost over $n$ iterations is:
> $$\sum_{i=\ell}^{n} a_i = a_\ell + a_{\ell+1} + \cdots + a_n.$$
> If the upper limit is infinite: $\displaystyle\sum_{i=\ell}^{\infty} a_i = \lim_{n \to \infty} \sum_{i=\ell}^{n} a_i$.

---

## 📘 Examples & Applications

### Example 1 — Big-Oh: Proving Membership

> [!Example] 📘 Show $x^2 + 2x + 5 = O(x^2)$
> **Using:** Big-Oh definition, finding a witness pair $(c, x_0)$.
>
> **Step 1.** We need constants $c > 0$ and $x_0 > 0$ such that $x^2 + 2x + 5 \leq c \cdot x^2$ for all $x \geq x_0$.
>
> **Step 2.** Choose $x_0 = 1$ and $c = 10$.
>
> **Step 3.** Verify: for $x \geq 1$,
> $$x^2 + 2x + 5 \leq x^2 + 2x^2 + 5x^2 = 8x^2 \leq 10x^2.$$
>
> Since we exhibit the pair $(c, x_0) = (10, 1)$, $\square$

---

### Example 2 — Big-Oh: Disproving Membership

> [!Example] 📘 Show $x^2 + 2x + 5 \notin O(x)$
> **Using:** Big-Oh definition, proof by contradiction.
>
> **Step 1.** Assume for contradiction $\exists\, c > 0,\; x_0 > 0$ such that $x^2 + 2x + 5 \leq cx$ for all $x \geq x_0$.
>
> **Step 2.** Rearranging: $x^2 + (2-c)x + 5 \leq 0$, which can be written as
> $$\left(x - \left(1 - \tfrac{c}{2}\right)\right)^2 + \left(5 - \left(1 - \tfrac{c}{2}\right)^2\right) \leq 0.$$
>
> **Step 3.** As $x \to \infty$, the left side $\to +\infty$, so the inequality cannot hold for all large $x$. Contradiction. $\square$

---

### Example 3 — Big-Omega: Proofs

> [!Example] 📘 Show $x^2 + 2x + 5 = \Omega(x)$ and $x^2 + 2x + 5 = \Omega(x^2)$
> **Using:** Big-Omega definition.
>
> **Part (a): $\Omega(x)$.** Choose $(c, x_0) = (1, 1)$. Then for $x \geq 1$:
> $$x^2 + 2x + 5 \geq x. \quad \checkmark$$
>
> **Part (b): $\Omega(x^2)$.** Choose $(c, x_0) = (1, 1)$. Then for $x \geq 1$:
> $$x^2 + 2x + 5 \geq x^2. \quad \checkmark$$

> [!Example] 📘 Show $x^2 + 2x + 5 \notin \Omega(x^3)$
> **Using:** Big-Omega definition, proof by contradiction.
>
> **Step 1.** Assume $\exists\, c > 0,\; x_0 > 0$ such that $x^2 + 2x + 5 \geq cx^3$ for all $x \geq x_0$.
>
> **Step 2.** Rearranging: $-x^2(cx - 1) + x + 5 \geq 0$.
>
> **Step 3.** As $x \to \infty$, the term $-x^2(cx-1)$ dominates and $\to -\infty$. Contradiction. $\square$

---

### Example 4 — Big-Theta: Proofs

> [!Example] 📘 Show $x^2 + 2x + 5 = \Theta(x^2)$
> **Using:** Big-Theta definition (must show both $O$ and $\Omega$).
>
> **Step 1.** Choose $(c_1, c_2, x_0) = (1, 10, 1)$.
>
> **Step 2.** For all $x \geq 1$:
> $$1 \cdot x^2 \;\leq\; x^2 + 2x + 5 \;\leq\; 10x^2. \quad \checkmark$$

> [!Example] 📘 Show $x^2 + 2x + 5 \neq \Theta(x)$
> **Using:** Contradiction on the upper bound.
>
> The upper bound $x^2 + 2x + 5 \leq c_2 x$ fails for large $x$ by the same argument as Example 2. Therefore $x^2 + 2x + 5 \notin O(x)$, so $\Theta(x)$ is impossible. $\square$

---

### Example 5 — Little-Oh and Little-Omega

> [!Example] 📘 Show $x^2 + 2x + 5 = o(x^3)$
> **Using:** Limit characterisation of little-oh.
>
> $$\lim_{x \to \infty} \frac{x^2 + 2x + 5}{x^3} = \lim_{x \to \infty} \left(\frac{1}{x} + \frac{2}{x^2} + \frac{5}{x^3}\right) = 0. \quad \checkmark$$

> [!Example] 📘 Show $x^2 + 2x + 5 \notin o(x)$
> **Using:** Limit characterisation of little-oh.
>
> $$\lim_{x \to \infty} \frac{x^2 + 2x + 5}{x} = \lim_{x \to \infty} \left(x + 2 + \frac{5}{x}\right) = \infty \neq 0. \quad \checkmark$$

> [!Example] 📘 Show $x^2 + 2x + 5 = \omega(x)$
> **Using:** Limit characterisation of little-omega.
>
> $$\lim_{x \to \infty} \frac{x^2 + 2x + 5}{x} = \lim_{x \to \infty} \left(x + 2 + \frac{5}{x}\right) = \infty. \quad \checkmark$$

---

### Example 6 — Counting Operations in Nested Loops (AlgA vs AlgB)

> [!Example] 📘 Do AlgA and AlgB have the same asymptotic run time?
> **Using:** Summation method, Big-Theta.
>
> ```c
> // AlgA: inner loop runs j < i
> int AlgA(int n) {
>     int sum = 0;
>     for(int i=0; i<n; i++)
>         for(int j=0; j<i; j++)
>             sum++;
>     return sum;
> }
>
> // AlgB: inner loop runs j < n
> int AlgB(int n) {
>     int sum = 0;
>     for(int i=0; i<n; i++)
>         for(int j=0; j<n; j++)
>             sum++;
>     return sum;
> }
> ```
>
> **AlgA:** Count the total number of `sum++` executions:
> $$A(n) = \sum_{i=0}^{n-1} \sum_{j=0}^{i-1} 1 = \sum_{i=0}^{n-1} i = \frac{n(n-1)}{2} = \Theta(n^2).$$
>
> **AlgB:**
> $$B(n) = \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} 1 = \sum_{i=0}^{n-1} n = n^2 = \Theta(n^2).$$
>
> **Answer: YES** — both run in $\Theta(n^2)$.

---

### Example 7 — Logarithmic Outer Loop (AlgC vs AlgD)

> [!Example] 📘 Do AlgC and AlgD have the same asymptotic run time?
> **Using:** Summation method with geometric series, substitution $i = 2^k$.
>
> ```c
> // AlgC: outer loop i *= 2, inner loop j < i
> int AlgC(int n) {
>     int sum = 0;
>     for(int i=1; i<=n; i*=2)
>         for(int j=0; j<i; j++)
>             sum++;
>     return sum;
> }
>
> // AlgD: outer loop i *= 2, inner loop j < n
> int AlgD(int n) {
>     int sum = 0;
>     for(int i=1; i<=n; i*=2)
>         for(int j=0; j<n; j++)
>             sum++;
>     return sum;
> }
> ```
>
> Since $i$ doubles each iteration, set $i = 2^k$, so $k$ ranges from $0$ to $\lfloor \log_2 n \rfloor - 1$.
>
> **AlgC:**
> $$C(n) = \sum_{k=0}^{\lfloor \log_2 n \rfloor - 1} \sum_{j=0}^{2^k - 1} 1 = \sum_{k=0}^{\lfloor \log_2 n \rfloor - 1} 2^k = 2^{\lfloor \log_2 n \rfloor} - 1 = \Theta(n).$$
>
> **AlgD:**
> $$D(n) = \sum_{k=0}^{\lfloor \log_2 n \rfloor - 1} \sum_{j=0}^{n-1} 1 = \sum_{k=0}^{\lfloor \log_2 n \rfloor - 1} n = n \lfloor \log_2 n \rfloor = \Theta(n \ln n).$$
>
> **Answer: NO** — $C(n) = \Theta(n)$ but $D(n) = \Theta(n \log n)$.

---

### Example 8 — Run Time of Fast Power Algorithm

> [!Example] 📘 What is the run time of the `power` function?
> **Using:** Binary representation of exponent, $\lfloor \log_2 n \rfloor$ iterations.
>
> ```c
> double power(double a, long n) {
>     double result = 1;
>     double x = a;
>     long y = n;
>     while (y) {
>         if (y % 2 == 1) result *= x;
>         x *= x;
>         y /= 2;
>     }
>     return result;
> }
> ```
>
> Each iteration halves $y$, so the loop runs $\lfloor \log_2 n \rfloor$ times. Each iteration does $O(1)$ work.
>
> **Run time: $O(\log n)$.**

---

### Exercise Set 1 — Proofs to Practise

> [!Example] 📘 Prove the following (exam-level exercises)
> **Using:** Big-Oh/Omega/Theta definitions and limit characterisations.
>
> **1.** $n^3 + 1000n^2 = O(n^4)$. [Hint: for $n \geq 1$, bound each term by $n^4$.]
>
> **2.** $\log n = O(n)$. [Hint: $\log n \leq n$ for all $n \geq 1$.]
>
> **3.** $\log n = O(\sqrt{n})$. [Hint: use $\lim_{n\to\infty} \frac{\log n}{\sqrt{n}} = 0$.]
>
> **4.** $n! \notin O(n^c)$ for any constant $c > 0$. [Hint: use Stirling's approximation or direct growth comparison.]
>
> **5.** $n^a = O(b^n)$ for any $a > 0$ and $b > 1$. [Hint: L'Hôpital or limit comparison.]
>
> **6.** $\log n! = O(n \log n)$ and $\log n! \geq \frac{n}{2} \log \frac{n}{2}$, therefore $\log n! = \Theta(n \log n)$.
>
> **7.** $1000x^3 - x^2 + 79 = \Theta(x^3)$.

---

### Exercise Set 2 — Algebraic Properties

> [!Example] 📘 Prove the following algebraic properties
> **Using:** Definitions of $O$, products, and polynomial dominance.
>
> **8.** If $f(x) = O(h(x))$ and $g(x) = O(h(x))$, and $a, b > 0$, then $af(x) + bg(x) = O(h(x))$.
>
> **9.** If $f_1(x) = O(g_1(x))$ and $f_2(x) = O(g_2(x))$, then $f_1(x) f_2(x) = O(g_1(x) g_2(x))$.
>
> **10.** $x^n + a_{n-1}x^{n-1} + \cdots + a_0 = O(x^n)$.
>
> **11.** $x^n + a_{n-1}x^{n-1} + \cdots + a_0 = \Theta(x^n)$.
>
> **12.** $\log n = O(n^c)$ for $0 < c < 1$.

---

### Exercise Set 3 — Counting Operations in Code

> [!Example] 📘 Count comparisons and assignments (problem size $n$)
> **Using:** Direct counting, summation method.
>
> ```c
> sum = 0;
> for (i = 0; i < n; i++) {
>     cin >> x;
>     sum = sum + x;
> }
> ```
>
> Assignments: `sum=0` (1) + `i=0` (1) + `i++` ($n$ times) + `cin>>x` ($n$) + `sum=sum+x` ($n$) = $3n + 2$ assignments.
> Comparisons: `i < n` checked $n + 1$ times.
> Total: $\Theta(n)$.

> [!Example] 📘 Count assignments in the matrix multiplication fragment (size $n$)
> **Using:** Triple summation.
>
> ```c
> for (i = 0; i < n; i++)
>     for (j = 0; j < n; j++) {
>         C[i][j] = 0;
>         for (k = 0; k < n; k++)
>             C[i][j] = C[i][j] + A[i][k] * B[k][j];
>     }
> ```
>
> The outer two loops give $n^2$ pairs $(i,j)$. For each pair: 1 assignment for `C[i][j]=0`, and $n$ assignments in the inner loop. Total assignments: $n^2(1 + n) = n^3 + n^2 = \Theta(n^3)$.

> [!Example] 📘 Order of growth of the halving outer loop
> **Using:** Geometric series (same structure as AlgC).
>
> ```c
> int sum = 0;
> for (int n = N; n > 0; n /= 2)
>     for (int i = 0; i < n; i++)
>         sum++;
> ```
>
> Let $N = 2^k$. The outer loop runs with $n = N, N/2, N/4, \ldots, 1$. Total count:
> $$\sum_{j=0}^{k} \frac{N}{2^j} = N \sum_{j=0}^{k} \frac{1}{2^j} < 2N.$$
> **Order of growth: $\Theta(N)$.**

---

## 🗂️ Summary

- A **Turing machine** is an abstract computational model; a **RAM model** assumes each simple operation costs $O(1)$ and provides the foundation for counting operations.
- An **algorithm** produces the required output for any legitimate input in finite time. **Analysis** measures its run-time / memory as a function of input size $n$.
- **Five asymptotic notations** express growth-rate relationships:
  - $O(g)$: upper bound (exists one constant $c$)
  - $\Omega(g)$: lower bound (exists one constant $c$)
  - $\Theta(g)$: tight bound (exists two constants $c_1, c_2$)
  - $o(g)$: strict upper bound (holds for ALL constants $c$)
  - $\omega(g)$: strict lower bound (holds for ALL constants $c$)
- **Limit rule**: let $L = \lim_{x\to\infty} f(x)/g(x)$. Then $L=0 \Rightarrow f=o(g)=O(g)$; $L\in(0,\infty) \Rightarrow f=\Theta(g)=O(g)=\Omega(g)$; $L=\infty \Rightarrow f=\omega(g)=\Omega(g)$.
- To prove $f = O(g)$ or $f = \Omega(g)$: exhibit a concrete witness pair $(c, x_0)$. To prove $f = o(g)$ or $f = \omega(g)$: show the limit equals $0$ or $\infty$.
- To count operations in **iterative code**: use the summation $\sum_{i} a_i$ where $a_i$ is the cost at iteration $i$.
- Standard growth hierarchy (slow to fast): $O(1) \subset O(\log n) \subset O(\sqrt{n}) \subset O(n) \subset O(n\log n) \subset O(n^2) \subset O(n^c) \subset O(c^n) \subset O(n!)$.
- Any **degree-$d$ polynomial** $p(n) = \Theta(n^d)$.
- $\log n = O(n^c)$ for any $c > 0$; polynomial functions grow faster than any logarithm.
- $n^a = O(b^n)$ for any $a > 0$, $b > 1$; exponentials dominate polynomials.
