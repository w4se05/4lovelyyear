# Sect.2 Advanced Counting Rules — Full Solutions

---

**1.** Find generating functions for the following sequences.

**Solution.**

**(a)** Consecutive non-negative integers $(1,2,3,\dots)$ (i.e., $a_n=n+1$ for $n\ge0$).

Step 1. Recall the standard OGF catalogue: $\displaystyle\sum_{n\ge0}x^n=\frac{1}{1-x}$ and $\displaystyle\sum_{n\ge0}nx^n=\frac{x}{(1-x)^2}$.

Step 2. Then $\displaystyle\sum_{n\ge0}(n+1)x^n=\sum_{n\ge0}nx^n+\sum_{n\ge0}x^n=\frac{x}{(1-x)^2}+\frac{1}{1-x}$.

Step 3. Combine over common denominator $(1-x)^2$:
$$\frac{x}{(1-x)^2}+\frac{1-x}{(1-x)^2}=\frac{1}{(1-x)^2}$$

$$\boxed{\dfrac{1}{(1-x)^2}}$$

---

**(b)** The number of $k$-combinations with repetition of $[n]$, for fixed $n$, and $k=0,1,2,\dots$

Step 1. The number of $k$-combinations with repetition from $n$ types is $C(n+k-1,k)$. This is the sequence $a_k=\binom{n+k-1}{k}$ for $k\ge0$.

Step 2. By the standard OGF catalogue, the generating function for the sequence $\binom{n+k-1}{k}$ (as a function of $k$) is:
$$\sum_{k\ge0}\binom{n+k-1}{k}x^k=\frac{1}{(1-x)^n}$$

Step 3. Combinatorial reasoning: choosing $k$ items from $n$ types with unlimited repetition corresponds to the coefficient of $x^k$ in $(1+x+x^2+\cdots)^n = \left(\frac{1}{1-x}\right)^n$.

$$\boxed{\dfrac{1}{(1-x)^n}}$$

---

**(c)** Perfect square numbers $(1,4,9,16,\dots)$, i.e., $a_n=(n+1)^2$ for $n\ge0$.

Step 1. Use $(n+1)^2=n^2+2n+1$. We need $\sum_{n\ge0}n^2x^n$, $\sum_{n\ge0}nx^n$, and $\sum_{n\ge0}x^n$.

Step 2. Known OGFs:
$$\sum_{n\ge0}x^n=\frac{1}{1-x},\qquad\sum_{n\ge0}nx^n=\frac{x}{(1-x)^2},\qquad\sum_{n\ge0}n^2x^n=\frac{x(1+x)}{(1-x)^3}$$

Step 3. Therefore:
$$A(x)=\frac{x(1+x)}{(1-x)^3}+\frac{2x}{(1-x)^2}+\frac{1}{1-x}$$
Put over common denominator $(1-x)^3$:
$$A(x)=\frac{x(1+x)+2x(1-x)+(1-x)^2}{(1-x)^3}
=\frac{x+x^2+2x-2x^2+1-2x+x^2}{(1-x)^3}
=\frac{1+x}{(1-x)^3}$$

$$\boxed{\dfrac{1+x}{(1-x)^3}}$$

---

**(d)** Fibonacci numbers $(0,1,1,2,3,5,\dots)$ with $f_0=0,f_1=1$, $f_n=f_{n-1}+f_{n-2}$ for $n\ge2$.

Step 1. Let $F(x)=\sum_{n\ge0}f_nx^n$. Multiply the recurrence by $x^n$ and sum for $n\ge2$:
$$\sum_{n\ge2}f_nx^n=\sum_{n\ge2}f_{n-1}x^n+\sum_{n\ge2}f_{n-2}x^n$$

Step 2. Express in terms of $F(x)$:
$$F(x)-f_0-f_1x=x(F(x)-f_0)+x^2F(x)$$
$$F(x)-0-x=xF(x)+x^2F(x)$$
$$F(x)-x=xF(x)+x^2F(x)$$

Step 3. Solve for $F(x)$:
$$F(x)(1-x-x^2)=x\quad\Longrightarrow\quad F(x)=\frac{x}{1-x-x^2}$$

$$\boxed{\dfrac{x}{1-x-x^2}}$$

---

**(e)** Catalan numbers $(1,1,2,5,14,42,\dots)$ with $C_0=1$, $C_n=\sum_{i=0}^{n-1}C_iC_{n-1-i}$ for $n\ge1$.

Step 1. Let $C(x)=\sum_{n\ge0}C_nx^n$. The convolution recurrence gives:
$$C(x)-1=x\,C(x)^2$$

Step 2. Solve the quadratic: $xC(x)^2-C(x)+1=0$. Using the quadratic formula:
$$C(x)=\frac{1\pm\sqrt{1-4x}}{2x}$$

Step 3. Since $C(0)=C_0=1$, take the minus sign (the plus sign gives $\lim_{x\to0}C(x)=\infty$):
$$C(x)=\frac{1-\sqrt{1-4x}}{2x}$$

$$\boxed{\dfrac{1-\sqrt{1-4x}}{2x}}$$

---

**(f)** The number of ways of filling a bag with $n$ fruits such that:
(i) apples even, (ii) bananas multiple of 5, (iii) at most 4 oranges, (iv) at most 1 pear.

Step 1. Build the per-fruit-type OGF:

- Apples (even): $1+x^2+x^4+\cdots=\dfrac{1}{1-x^2}$
- Bananas (multiple of 5): $1+x^5+x^{10}+\cdots=\dfrac{1}{1-x^5}$
- Oranges (at most 4): $1+x+x^2+x^3+x^4=\dfrac{1-x^5}{1-x}$
- Pears (at most 1): $1+x$

Step 2. Multiply (fruits are independent):
$$G(x)=\frac{1}{1-x^2}\cdot\frac{1}{1-x^5}\cdot\frac{1-x^5}{1-x}\cdot(1+x)$$

Step 3. Cancel $(1-x^5)$:
$$G(x)=\frac{1+x}{(1-x)(1-x^2)}=\frac{1+x}{(1-x)(1-x)(1+x)}=\frac{1}{(1-x)^2}$$

$$\boxed{\dfrac{1}{(1-x)^2}}$$

---

**2.** Let $A(x)=a_0+a_1x+\cdots$ be the generating function for $(a_0,a_1,a_2,\dots)$. Express in terms of $A$ the generating functions for the following sequences.

**Solution.**

**(a)** $(a_0,\,a_0+a_1,\,a_1+a_2,\,a_2+a_3,\dots)$

Step 1. Let $B(x)=\sum_{n\ge0}b_nx^n$. Here $b_0=a_0$, $b_n=a_{n-1}+a_n$ for $n\ge1$.

Step 2.
$$B(x)=a_0+\sum_{n\ge1}(a_{n-1}+a_n)x^n
=a_0+x\sum_{n\ge1}a_{n-1}x^{n-1}+\sum_{n\ge1}a_nx^n$$
$$=a_0+xA(x)+\big(A(x)-a_0\big)=a_0+xA(x)+A(x)-a_0=(1+x)A(x)$$

$$\boxed{(1+x)A(x)}$$

---

**(b)** $(a_1,a_2,a_3,\dots)$

Step 1. Shift indices: $\sum_{n\ge0}a_{n+1}x^n = \frac{1}{x}\sum_{n\ge0}a_{n+1}x^{n+1}=\frac{A(x)-a_0}{x}$.

$$\boxed{\dfrac{A(x)-a_0}{x}}$$

---

**(c)** $(a_0+a_1,\,a_1+a_2,\,a_2+a_3,\dots)$

Step 1. Let $b_n=a_n+a_{n+1}$ for $n\ge0$.

Step 2.
$$B(x)=\sum_{n\ge0}(a_n+a_{n+1})x^n
=\sum_{n\ge0}a_nx^n+\sum_{n\ge0}a_{n+1}x^n
=A(x)+\frac{A(x)-a_0}{x}$$

Step 3. Simplify:
$$B(x)=A(x)+\frac{A(x)-a_0}{x}$$

$$\boxed{A(x)+\dfrac{A(x)-a_0}{x}}$$

---

**(d)** $(a_0,\,2a_1,\,4a_2,\,8a_3,\dots)$

Step 1. General term: $b_n=2^na_n$.

Step 2.
$$B(x)=\sum_{n\ge0}2^na_nx^n=\sum_{n\ge0}a_n(2x)^n=A(2x)$$

$$\boxed{A(2x)}$$

---

**(e)** $(a_0,\,a_0+a_1,\,a_0+a_1+a_2,\dots)$

Step 1. General term: $b_n=\sum_{k=0}^{n}a_k$.

Step 2. This is the convolution of $(a_n)$ with $(1,1,1,\dots)$, whose OGF is $\frac{1}{1-x}$:
$$B(x)=A(x)\cdot\frac{1}{1-x}=\frac{A(x)}{1-x}$$

$$\boxed{\dfrac{A(x)}{1-x}}$$

---

**(f)** $(a_0,\,a_1b,\,a_2b^2,\,a_3b^3,\dots)$ where $b$ is constant.

Step 1. General term: $b_n=a_nb^n$.

Step 2.
$$B(x)=\sum_{n\ge0}a_nb^nx^n=\sum_{n\ge0}a_n(bx)^n=A(bx)$$

$$\boxed{A(bx)}$$

---

**(g)** $(a_0,\,0,\,a_2,\,0,\,a_4,\,0,\dots)$

Step 1. Keep only even-indexed terms, insert zeros at odd indices.

Step 2. Observe that $\frac{1}{2}(A(x)+A(-x))$ gives:
$$\frac{1}{2}\sum_{n\ge0}a_n\big(x^n+(-x)^n\big)=\sum_{n\text{ even}}a_nx^n$$

$$\boxed{\dfrac{A(x)+A(-x)}{2}}$$

---

**(h)** $(a_0,\,a_2,\,a_4,\dots)$

Step 1. Take only even-indexed terms without zeros: $b_n=a_{2n}$.

Step 2. Apply the extraction of part (g) and compress indices:
$$B(x)=\sum_{n\ge0}a_{2n}x^n=\frac{A(\sqrt{x})+A(-\sqrt{x})}{2}$$

$$\boxed{\dfrac{A(\sqrt{x})+A(-\sqrt{x})}{2}}$$

---

**3.** Find the generating function for the number of ways to pay $n$ dollars from coins of denominations 3, 5, 7 dollars.

**Solution.**

Step 1. Each coin denomination is an independent source with unlimited supply.

Step 2. Per-denomination OGF (unlimited of each):
- 3-dollar coin: $1+x^3+x^6+\cdots=\dfrac{1}{1-x^3}$
- 5-dollar coin: $1+x^5+x^{10}+\cdots=\dfrac{1}{1-x^5}$
- 7-dollar coin: $1+x^7+x^{14}+\cdots=\dfrac{1}{1-x^7}$

Step 3. By the Convolution Rule (independent choices), the product gives the combined OGF:
$$G(x)=\frac{1}{1-x^3}\cdot\frac{1}{1-x^5}\cdot\frac{1}{1-x^7}$$

The number of ways to pay $n$ dollars is the coefficient of $x^n$ in $G(x)$.

$$\boxed{G(x)=\dfrac{1}{(1-x^3)(1-x^5)(1-x^7)}}$$

---

**4.** Find the generating function for $b_n$, the number of ways $n$ identical candies can be distributed among 4 children and 1 adult so that each child receives an odd number of candies, and the adult receives 1 or 2 candies.

**Solution.**

Step 1. Build per-recipient OGF.

Step 2. Each child (odd number of candies): $x+x^3+x^5+\cdots=\dfrac{x}{1-x^2}$.

Step 3. The adult (1 or 2 candies): $x+x^2=x(1+x)$.

Step 4. All 5 recipients are independent; multiply their OGFs:
$$G(x)=\left(\frac{x}{1-x^2}\right)^4\cdot x(1+x)
=\frac{x^4}{(1-x^2)^4}\cdot x(1+x)$$

Step 5. Simplify:
$$G(x)=\frac{x^5(1+x)}{(1-x^2)^4}$$

$$\boxed{G(x)=\dfrac{x^5+x^6}{(1-x^2)^4}}$$

---

**5.** In a certain game it is possible to score 1, 2, or 4 points on each turn. Find the generating function for the number of ways to score $n$ points in a game in which

**(a)** there are at least two turns where 4 points are scored.

**Solution.**

Step 1. Interpret "ways to score $n$ points" as counting multisets of turn-values (order of turns does not matter — this is a distribution-of-point-values problem).

Step 2. Let $a$, $b$, $c$ be the number of turns scoring 1, 2, 4 points respectively. A way corresponds to a non-negative integer solution of $a+2b+4c=n$.

Step 3. Per-type OGF:
- 1-point turns (any $a\ge0$): $\dfrac{1}{1-x}$
- 2-point turns (any $b\ge0$): $\dfrac{1}{1-x^2}$
- 4-point turns: $c\ge 2$ $\Rightarrow$ $x^8+x^{12}+\cdots=\dfrac{x^8}{1-x^4}$

Step 4. Multiply:
$$G_a(x)=\frac{1}{1-x}\cdot\frac{1}{1-x^2}\cdot\frac{x^8}{1-x^4}
=\frac{x^8}{(1-x)(1-x^2)(1-x^4)}$$

$$\boxed{G_a(x)=\dfrac{x^8}{(1-x)(1-x^2)(1-x^4)}}$$

---

**(b)** there is a multiple of 3 turns where 2 points are scored.

**Solution.**

Step 1. The number of 2-point turns $b$ must satisfy $b=0,3,6,9,\dots$

Step 2. OGF for $b$ restricted to multiples of 3:
$$1+(x^2)^3+(x^2)^6+\cdots=\sum_{k\ge0}(x^6)^k=\frac{1}{1-x^6}$$

Step 3. The 1-point and 4-point turns are unrestricted:
$$G_b(x)=\frac{1}{1-x}\cdot\frac{1}{1-x^6}\cdot\frac{1}{1-x^4}
=\frac{1}{(1-x)(1-x^4)(1-x^6)}$$

$$\boxed{G_b(x)=\dfrac{1}{(1-x)(1-x^4)(1-x^6)}}$$

*Note:* If both constraints (a) and (b) must hold simultaneously, the combined OGF is $G(x)=\dfrac{x^8}{(1-x)(1-x^4)(1-x^6)}$, matching the answer-key entry.

---

**6.** What is the generating function for $\{a_k\}$, where $a_k$ is the number of solutions of $x_1+x_2+x_3+x_4=k$, when $x_1\ge3$, $1\le x_2\le5$, $0\le x_3\le4$, and $x_4\ge1$. Use this generating function to find $a_7$.

**Solution.**

Step 1. Build the OGF for each variable's contribution:

- $x_1\ge3$: $x^3+x^4+x^5+\cdots=\dfrac{x^3}{1-x}$
- $1\le x_2\le5$: $x+x^2+x^3+x^4+x^5=\dfrac{x(1-x^5)}{1-x}$
- $0\le x_3\le4$: $1+x+x^2+x^3+x^4=\dfrac{1-x^5}{1-x}$
- $x_4\ge1$: $x+x^2+x^3+\cdots=\dfrac{x}{1-x}$

Step 2. Multiply all four OGFs:
$$G(x)=\frac{x^3}{1-x}\cdot\frac{x(1-x^5)}{1-x}\cdot\frac{1-x^5}{1-x}\cdot\frac{x}{1-x}=\frac{x^5(1-x^5)^2}{(1-x)^4}$$

Step 3. Expand $(1-x^5)^2=1-2x^5+x^{10}$:
$$G(x)=\frac{x^5-2x^{10}+x^{15}}{(1-x)^4}$$

Step 4. Recall $\dfrac{1}{(1-x)^4}=\displaystyle\sum_{k\ge0}\binom{k+3}{3}x^k$. The coefficient of $x^n$ in $G(x)$ is:
$$a_n=\binom{n-5+3}{3}-2\binom{n-10+3}{3}+\binom{n-15+3}{3}$$
$$=\binom{n-2}{3}-2\binom{n-7}{3}+\binom{n-12}{3}$$
(where $\binom{m}{3}=0$ if $m<3$, i.e., the term contributes only if the upper index $\ge 3$).

Step 5. Compute $a_7$: Only the first term contributes ($7-2=5\ge3$; $7-7=0<3$, $7-12=-5<3$):
$$a_7=\binom{5}{3}=\frac{5\cdot4\cdot3}{6}=10$$

$$\boxed{G(x)=\dfrac{x^5(1-x^5)^2}{(1-x)^4},\qquad a_7=10}$$

---

**7.** Using the generating function for the Fibonacci numbers, prove the following identities.

**Solution.** Let $F(x)=\dfrac{x}{1-x-x^2}=\sum_{n\ge0}f_nx^n$ with $f_0=0,f_1=1$, $f_n=f_{n-1}+f_{n-2}$ for $n\ge2$.

---

**(a)** $f_0+f_1+\cdots+f_n=f_{n+2}-1$.

Step 1. The partial sum $S_n=\sum_{k=0}^{n}f_k$ has generating function $\dfrac{F(x)}{1-x}$ (convolution with $(1,1,1,\dots)$).

Step 2. Compute:
$$\frac{F(x)}{1-x}=\frac{x}{(1-x)(1-x-x^2)}$$

Step 3. Observe the algebraic identity:
$$\frac{1+x}{1-x-x^2}-\frac{1}{1-x}=\frac{(1+x)(1-x)-(1-x-x^2)}{(1-x)(1-x-x^2)}=\frac{1-x^2-1+x+x^2}{(1-x)(1-x-x^2)}=\frac{x}{(1-x)(1-x-x^2)}$$

So:
$$\frac{F(x)}{1-x}=\frac{1+x}{1-x-x^2}-\frac{1}{1-x}$$

Step 4. Expand both terms. Using $F(x)/x=1/(1-x-x^2)=\sum_{n\ge0}f_{n+1}x^n$:
$$\frac{1+x}{1-x-x^2}=\frac{1}{1-x-x^2}+\frac{x}{1-x-x^2}=\sum_{n\ge0}f_{n+1}x^n+\sum_{n\ge0}f_nx^n$$
And $\dfrac{1}{1-x}=\sum_{n\ge0}x^n$.

Step 5. Therefore:
$$\frac{F(x)}{1-x}=\sum_{n\ge0}(f_{n+1}+f_n-1)x^n=\sum_{n\ge0}(f_{n+2}-1)x^n$$

Step 6. But $\dfrac{F(x)}{1-x}=\sum_{n\ge0}(\sum_{k=0}^{n}f_k)x^n$. Equating coefficients:
$$\sum_{k=0}^{n}f_k = f_{n+2}-1$$

$$\boxed{f_0+f_1+\cdots+f_n=f_{n+2}-1}$$

---

**(b)** $f_0+f_2+\cdots+f_{2n}=f_{2n+1}-1$.

Step 1. From part (a), the OGF of the partial sums gives:
$$\sum_{k=0}^{2n}f_k = f_{2n+2}-1$$

Step 2. Split the sum into even and odd indices:
$$\sum_{k=0}^{2n}f_k = \left(\sum_{k=0}^{n}f_{2k}\right) + \left(\sum_{k=0}^{n-1}f_{2k+1}\right)$$

Step 3. From the Fibonacci recurrence $f_{2k+1}=f_{2k+2}-f_{2k}$:
$$\sum_{k=0}^{n-1}f_{2k+1} = \sum_{k=0}^{n-1}(f_{2k+2}-f_{2k}) = f_{2n}-f_0 = f_{2n}$$

Step 4. Therefore:
$$f_{2n+2}-1 = \left(\sum_{k=0}^{n}f_{2k}\right) + f_{2n}$$

Step 5. Using $f_{2n+2}=f_{2n+1}+f_{2n}$:
$$\sum_{k=0}^{n}f_{2k} = f_{2n+2}-1-f_{2n} = f_{2n+1}+f_{2n}-1-f_{2n} = f_{2n+1}-1$$

**(c)** $f_1+f_3+\cdots+f_{2n-1}=f_{2n}$.

Step 1. From step 3 of part (b):
$$\sum_{k=0}^{n-1}f_{2k+1} = f_{2n} - f_0 = f_{2n}$$

This is exactly the required identity with $f_1+f_3+\cdots+f_{2n-1}=f_{2n}$. (Note $f_{2k+1}$ for $k=0$ gives $f_1$, and for $k=n-1$ gives $f_{2n-1}$, matching the summation range.)

$$\boxed{\begin{aligned}
\text{(a) }&\sum_{k=0}^{n}f_k = f_{n+2}-1\\
\text{(b) }&\sum_{k=0}^{n}f_{2k} = f_{2n+1}-1\\
\text{(c) }&\sum_{k=0}^{n-1}f_{2k+1} = f_{2n}
\end{aligned}}$$

---

**8.** Find a closed formula for the number of $k$-combinations with repetition of $n$ elements by using the Maclaurin decomposition of its generating function.

**Solution.**

Step 1. The generating function for $k$-combinations with repetition from $n$ types is:
$$G(x)=\frac{1}{(1-x)^n}$$

Step 2. The Maclaurin series expansion of $(1-x)^{-n}$:
$$(1-x)^{-n}=\sum_{k=0}^{\infty}\frac{(-n)(-n-1)\cdots(-n-k+1)}{k!}(-x)^k$$

Step 3. Simplify the coefficient:
$$\frac{(-1)^k \cdot n(n+1)\cdots(n+k-1)}{k!} \cdot (-1)^k
= \frac{n(n+1)\cdots(n+k-1)}{k!}$$

Step 4. Recognize this as a binomial coefficient:
$$\frac{n(n+1)\cdots(n+k-1)}{k!} = \binom{n+k-1}{k}$$

Step 5. Therefore the number of $k$-combinations with repetition of $n$ elements is:
$$\binom{n+k-1}{k}=C(n+k-1,k)$$

$$\boxed{C(n+k-1,k)=\binom{n+k-1}{k}}$$

---

**9.** Find the generating function for the number of partitions of $[n]$ into 2 parts, $S(n,2)$. From it, find a closed formula.

**Solution.**

Step 1. The recurrence: $S(0,2)=S(1,2)=0$, and for $n\ge2$:
$$S(n,2)=1+2S(n-1,2)$$

Step 2. Let $G(x)=\sum_{n\ge0}S(n,2)x^n$. Multiply the recurrence by $x^n$ and sum for $n\ge2$:
$$\sum_{n\ge2}S(n,2)x^n = \sum_{n\ge2}1\cdot x^n + 2\sum_{n\ge2}S(n-1,2)x^n$$

Step 3. Express in terms of $G(x)$:
$$G(x)-S(0,2)-S(1,2)x = \frac{x^2}{1-x} + 2x\big(G(x)-S(0,2)\big)$$

Since $S(0,2)=S(1,2)=0$:
$$G(x) = \frac{x^2}{1-x} + 2x\,G(x)$$

Step 4. Solve for $G(x)$:
$$G(x)(1-2x)=\frac{x^2}{1-x}\quad\Longrightarrow\quad G(x)=\frac{x^2}{(1-x)(1-2x)}$$

Step 5. Partial fraction decomposition:
$$\frac{x^2}{(1-x)(1-2x)} = \frac{A}{1-x}+\frac{B}{1-2x}$$

Multiply by the denominator: $x^2 = A(1-2x)+B(1-x)$.

At $x=1$: $1 = A(1-2)+B(0) = -A \Rightarrow A = -1$.
At $x=1/2$: $1/4 = A(0)+B(1/2) = B/2 \Rightarrow B = 1/2$.

So:
$$G(x) = \frac{-1}{1-x} + \frac{1/2}{1-2x}$$

Step 6. Expand:
$$G(x) = -\sum_{n\ge0}x^n + \frac12\sum_{n\ge0}(2x)^n = \sum_{n\ge0}\left(\frac12\cdot2^n - 1\right)x^n = \sum_{n\ge0}\left(2^{n-1}-1\right)x^n$$

Step 7. For $n\ge2$, $S(n,2)=2^{n-1}-1$. For $n=0,1$, check: $S(0,2)=2^{-1}-1=-1/2$ (wrong — but our GF was derived from $n\ge2$, and the formula $2^{n-1}-1$ gives $S(0,2)=2^{-1}-1=-1/2$, which is not the intended domain; the recurrence starts at $n\ge2$ with base values $S(0,2)=S(1,2)=0$). So the closed form holds for $n\ge1$ (and $S(1,2)=2^{0}-1=0$, matching). For $n\ge1$, $S(n,2)=2^{n-1}-1$.

$$\boxed{G(x)=\dfrac{x^2}{(1-x)(1-2x)},\qquad S(n,2)=2^{n-1}-1\;(n\ge1)}$$

---

**10.** Use the generating function method to solve the following recursions.

**Solution.**

**(a)** $a_0=2$, $a_n=3a_{n-1}$ for $n\ge1$.

Step 1. Let $A(x)=\sum_{n\ge0}a_nx^n$. Multiply the recurrence by $x^n$ and sum for $n\ge1$:
$$\sum_{n\ge1}a_nx^n=3\sum_{n\ge1}a_{n-1}x^n$$

Step 2. Express in terms of $A(x)$:
$$A(x)-a_0=3x\,A(x)$$

Step 3. Solve for $A(x)$:
$$A(x)(1-3x)=a_0=2\quad\Longrightarrow\quad A(x)=\frac{2}{1-3x}$$

Step 4. Expand: $\dfrac{2}{1-3x}=2\sum_{n\ge0}(3x)^n=\sum_{n\ge0}(2\cdot3^n)x^n$.

Hence $a_n=2\cdot3^n$.

$$\boxed{A(x)=\dfrac{2}{1-3x},\qquad a_n=2\cdot3^n}$$

---

**(b)** $a_0=2$, $a_n=3a_{n-1}+1$ for $n\ge1$.

Step 1 (GF method). Let $A(x)=\sum a_nx^n$. Sum for $n\ge1$:
$$\sum_{n\ge1}a_nx^n=3\sum_{n\ge1}a_{n-1}x^n+\sum_{n\ge1}1\cdot x^n$$
$$A(x)-a_0=3x\,A(x)+\frac{x}{1-x}$$

Step 2. Solve:
$$A(x)(1-3x)=a_0+\frac{x}{1-x}=2+\frac{x}{1-x}=\frac{2(1-x)+x}{1-x}=\frac{2-x}{1-x}$$

$$A(x)=\frac{2-x}{(1-x)(1-3x)}$$

Step 3. Partial fractions:
$$\frac{2-x}{(1-x)(1-3x)}=\frac{A}{1-x}+\frac{B}{1-3x}$$

$2-x=A(1-3x)+B(1-x)$.

At $x=1$: $1=A(-2)\Rightarrow A=-\frac12$.
At $x=1/3$: $2-\frac13 = B(1-\frac13)\Rightarrow \frac53 = B\cdot\frac23\Rightarrow B=\frac52$.

$$A(x)=\frac{-1/2}{1-x}+\frac{5/2}{1-3x}$$

Step 4. Expand:
$$A(x)=-\frac12\sum_{n\ge0}x^n+\frac52\sum_{n\ge0}3^nx^n=\sum_{n\ge0}\left(\frac52\cdot3^n-\frac12\right)x^n$$

Step 5. Check $n=0$: $\frac52-\frac12=2=a_0$. ✓. So $a_n=\frac52\cdot3^n-\frac12$ for all $n\ge0$.

$$\boxed{A(x)=\dfrac{2-x}{(1-x)(1-3x)},\qquad a_n=\dfrac{5}{2}\cdot3^n-\dfrac{1}{2}}$$

---

**(c)** $a_0=1$, $a_1=2$, $a_n=5a_{n-1}-4a_{n-2}$ for $n\ge2$.

Step 1. Let $A(x)=\sum a_nx^n$. Sum the recurrence for $n\ge2$:
$$\sum_{n\ge2}a_nx^n=5\sum_{n\ge2}a_{n-1}x^n-4\sum_{n\ge2}a_{n-2}x^n$$

$$A(x)-a_0-a_1x=5x\big(A(x)-a_0\big)-4x^2A(x)$$

Step 2. Substitute initial values:
$$A(x)-1-2x=5x\big(A(x)-1\big)-4x^2A(x)$$
$$A(x)-1-2x=5x\,A(x)-5x-4x^2A(x)$$

Step 3. Solve:
$$A(x)(1-5x+4x^2)=1+2x-5x=1-3x$$
$$A(x)=\frac{1-3x}{1-5x+4x^2}$$

Factor denominator: $1-5x+4x^2=(1-x)(1-4x)$.

Step 4. Partial fractions:
$$\frac{1-3x}{(1-x)(1-4x)}=\frac{A}{1-x}+\frac{B}{1-4x}$$

$1-3x=A(1-4x)+B(1-x)$.

At $x=1$: $-2=A(-3)\Rightarrow A=\frac23$.
At $x=1/4$: $1-\frac34 = B(1-\frac14)\Rightarrow \frac14 = B\cdot\frac34\Rightarrow B=\frac13$.

$$A(x)=\frac{2/3}{1-x}+\frac{1/3}{1-4x}$$

Step 5. Expand:
$$A(x)=\frac23\sum_{n\ge0}x^n+\frac13\sum_{n\ge0}4^nx^n=\sum_{n\ge0}\left(\frac23+\frac13\cdot4^n\right)x^n$$

Hence $a_n=\frac23+\frac13\cdot4^n$.

Check $n=0$: $\frac23+\frac13=1$. ✓. Check $n=1$: $\frac23+\frac43=2$. ✓.

$$\boxed{A(x)=\dfrac{1-3x}{(1-x)(1-4x)},\qquad a_n=\dfrac{2}{3}+\dfrac{1}{3}\cdot4^n}$$

---

**(d)** $u_0=2$, $u_1=-6$, $u_{n+2}+8u_{n+1}-9u_n=8\cdot3^{n+1}$.

Step 1. This is a non-homogeneous recurrence. Rewrite as: $u_{n+2}+8u_{n+1}-9u_n=8\cdot3^{n+1}$.

Step 2. Use the Characteristic Polynomial Method (faster than OGF for exam).

**Homogeneous part:** $p(x)=x^2+8x-9=(x-1)(x+9)$. Roots: $r_1=1$, $r_2=-9$ (both distinct).

**RHS:** $8\cdot3^{n+1}=8\cdot3\cdot3^n=24\cdot3^n$. This is of form $b^n\cdot P(n)$ with $b=3$, $d=0$ (constant polynomial).

**Augmented characteristic polynomial:** $(x-1)(x+9)(x-3)^{0+1}=(x-1)(x+9)(x-3)$.

Step 3. Three distinct roots: $1,-9,3$. General solution:
$$u_n=c_1\cdot1^n+c_2(-9)^n+c_3\cdot3^n$$

Step 4. Use initial conditions $u_0=2$, $u_1=-6$, and compute $u_2$ from the recurrence.

Recurrence for $n=0$: $u_2+8u_1-9u_0=8\cdot3^1=24$.
$u_2+8(-6)-9(2)=24\Rightarrow u_2-48-18=24\Rightarrow u_2=90$.

System:
$$\begin{aligned}
u_0=2&: &c_1+c_2+c_3&=2\\
u_1=-6&: &c_1-9c_2+3c_3&=-6\\
u_2=90&: &c_1+81c_2+9c_3&=90
\end{aligned}$$

Step 5. Solve. Subtract eq(1) from eq(2) and (3):
Eq(2)-Eq(1): $-10c_2+2c_3=-8\Rightarrow -5c_2+c_3=-4$  ... (4)
Eq(3)-Eq(1): $80c_2+8c_3=88\Rightarrow 10c_2+c_3=11$  ... (5)

Subtract (4) from (5): $15c_2=15\Rightarrow c_2=1$.
From (5): $10(1)+c_3=11\Rightarrow c_3=1$.
From (1): $c_1+1+1=2\Rightarrow c_1=0$.

Step 6. Therefore:
$$u_n=0\cdot1^n+1\cdot(-9)^n+1\cdot3^n=(-9)^n+3^n$$

Check: $u_0=1+1=2$ ✓, $u_1=-9+3=-6$ ✓, $u_2=81+9=90$ ✓.

$$\boxed{u_n=(-9)^n+3^n}$$

---

**(e)** $u_0=1$, $u_{n+1}-2u_n=4^n$.

Step 1. Rewrite as $u_{n+1}=2u_n+4^n$. This is a first-order non-homogeneous recurrence.

Step 2. **Homogeneous part:** $p(x)=x-2$. Root: $r=2$.

**RHS:** $4^n = (4)^n\cdot 1$ with $b=4$, $d=0$.

**Augmented polynomial:** $(x-2)(x-4)$.

General solution: $u_n=c_1\cdot2^n+c_2\cdot4^n$.

Step 3. Find $c_1,c_2$ using $u_0=1$ and $u_1$ computed from recurrence.

$u_1=2u_0+4^0=2(1)+1=3$.

System:
$$\begin{aligned}
u_0=1&: &c_1+c_2&=1\\
u_1=3&: &2c_1+4c_2&=3
\end{aligned}$$

Step 4. From (1): $c_2=1-c_1$. Substitute into (2):
$$2c_1+4(1-c_1)=3\Rightarrow 2c_1+4-4c_1=3\Rightarrow -2c_1=-1\Rightarrow c_1=\frac12$$
Then $c_2=1-\frac12=\frac12$.

Step 5.
$$u_n=\frac12\cdot2^n+\frac12\cdot4^n=2^{n-1}+\frac12\cdot4^n$$

Check: $u_0=1/2+1/2=1$ ✓, $u_1=1+2=3$ ✓.

$$\boxed{u_n=2^{n-1}+\dfrac{1}{2}\cdot4^n}$$

---

**(f)** Let $q_n$ be the number of words of length $n$ in the alphabet $\{a,b,c,d\}$ which contain an odd number of $b$'s. Show that $q_{n+1}=4^n+2q_n$.

**Solution.**

Step 1. Total words of length $n+1$: $4^{n+1}$. These consist of words whose last letter determines a relationship with shorter words.

Consider building a word of length $n+1$:

- **Case 1:** The last letter is $a$, $c$, or $d$ (3 choices). Then the prefix of length $n$ must have an odd number of $b$'s to keep the total odd. Number: $3q_n$.

- **Case 2:** The last letter is $b$. Then the prefix must have an **even** number of $b$'s. Number of length-$n$ words with even number of $b$'s = $4^n-q_n$ (total minus odd). So this contributes $1\cdot(4^n-q_n)=4^n-q_n$.

Step 2. Sum the cases:
$$q_{n+1}=3q_n+(4^n-q_n)=4^n+2q_n$$

Thus $q_{n+1}=4^n+2q_n$ as required.

Step 3. (Optional closed form). The recurrence is $q_{n+1}-2q_n=4^n$. With $q_0=0$ (empty word has 0 $b$'s, which is even, not odd).

Using the augmented characteristic polynomial $(x-2)(x-4)$:
$q_n=c_1\cdot2^n+c_2\cdot4^n$.

$q_0=0$: $c_1+c_2=0\Rightarrow c_2=-c_1$.
$q_1=4^0+2q_0=1$: $2c_1+4c_2=2c_1-4c_1=-2c_1=1\Rightarrow c_1=-\frac12$, $c_2=\frac12$.

$q_n=-\frac12\cdot2^n+\frac12\cdot4^n=\frac12(4^n-2^n)$.

$$\boxed{q_{n+1}=4^n+2q_n,\qquad q_n=\dfrac{1}{2}(4^n-2^n)}$$

---

**11.** For each of these generating functions, provide a closed formula for the sequence it determines.

**Solution.**

**(a)** $(3x-4)^3$

Step 1. Expand:
$$(3x-4)^3 = (3x)^3 + 3(3x)^2(-4) + 3(3x)(-4)^2 + (-4)^3$$
$$= 27x^3 - 108x^2 + 144x - 64$$

Step 2. This is a polynomial; the coefficients are the sequence. In order $a_0,a_1,a_2,a_3$:
$$a_0=-64,\; a_1=144,\; a_2=-108,\; a_3=27,\; a_n=0\;(n\ge4)$$

$$\boxed{(-64,\,144,\,-108,\,27,\,0,\,0,\dots)}$$

---

**(b)** $\dfrac{x^3}{1-3x}$

Step 1. Factor: $x^3\cdot\dfrac{1}{1-3x}=x^3\sum_{k\ge0}(3x)^k=\sum_{k\ge0}3^kx^{k+3}$.

Step 2. Let $n=k+3$, so $k=n-3$. For $n\ge3$, $a_n=3^{n-3}$. For $n=0,1,2$, $a_n=0$.

$$\boxed{a_n=\begin{cases}0,&n=0,1,2\\[4pt]3^{\,n-3},&n\ge3\end{cases}}$$

---

**(c)** $\dfrac{x^3+x}{1-3x}$

Step 1. Split: $\dfrac{x^3}{1-3x}+\dfrac{x}{1-3x}$.

Step 2. $\dfrac{x}{1-3x}=x\sum_{k\ge0}3^kx^k=\sum_{k\ge0}3^kx^{k+1}$. For $n\ge1$, term from this part: $3^{n-1}$.

Step 3. From part (b), first part gives $3^{n-3}$ for $n\ge3$.

Step 4. Combine:
- $n=0$: $a_0=0$
- $n=1$: $a_1=3^{0}=1$
- $n=2$: $a_2=3^{1}=3$
- $n\ge3$: $a_n=3^{\,n-3}+3^{\,n-1}=3^{\,n-3}(1+9)=10\cdot3^{\,n-3}$

$$\boxed{a_0=0,\;a_1=1,\;a_2=3,\;a_n=10\cdot3^{\,n-3}\;(n\ge3)}$$

---

**(d)** $\dfrac{x^2}{(1-x)^2}$

Step 1. Recall $\dfrac{1}{(1-x)^2}=\sum_{n\ge0}(n+1)x^n$.

Step 2. Multiply by $x^2$:
$$\frac{x^2}{(1-x)^2}=x^2\sum_{n\ge0}(n+1)x^n=\sum_{n\ge0}(n+1)x^{n+2}$$

Step 3. Let $k=n+2$, $n=k-2$. For $k\ge2$: $a_k = (k-2)+1 = k-1$. For $k=0,1$: $a_k=0$.

$$\boxed{a_0=0,\;a_1=0,\;a_n=n-1\;(n\ge2)}$$

---

**(e)** $\dfrac{x^2-x}{(1-x)^2}$

Step 1. Split: $\dfrac{x^2}{(1-x)^2}-\dfrac{x}{(1-x)^2}$.

Step 2. $\dfrac{x}{(1-x)^2}=x\sum_{n\ge0}(n+1)x^n=\sum_{n\ge0}(n+1)x^{n+1}$. For $n\ge1$: term $=n$ (since $(n-1)+1=n$).

Step 3. From (d), $\dfrac{x^2}{(1-x)^2}$ gives $a_n=n-1$ for $n\ge2$.

Step 4. Combine:
- $n=0$: $a_0=0-0=0$
- $n=1$: $a_1=0-1=-1$
- $n\ge2$: $a_n=(n-1)-n=-1$

$$\boxed{a_0=0,\;a_1=-1,\;a_n=-1\;(n\ge2)}$$

---

**(f)** $\dfrac{x^2}{(1-x)^3}$

Step 1. Recall $\dfrac{1}{(1-x)^3}=\sum_{n\ge0}\binom{n+2}{2}x^n$.

Step 2. Multiply by $x^2$:
$$\frac{x^2}{(1-x)^3}=x^2\sum_{n\ge0}\binom{n+2}{2}x^n=\sum_{n\ge0}\binom{n+2}{2}x^{n+2}$$

Step 3. For $k=n+2$, $n=k-2$. For $k\ge2$:
$$a_k=\binom{k}{2}=\frac{k(k-1)}{2}$$
For $k=0,1$: $a_k=0$.

$$\boxed{a_0=0,\;a_1=0,\;a_n=\binom{n}{2}=\dfrac{n(n-1)}{2}\;(n\ge2)}$$

---

**12.** Use generating functions to find the number of different ways 10 identical balloons can be given to four children if each child receives at least two balloons.

**Solution.**

Step 1. Per-child OGF (at least 2 balloons): $x^2+x^3+x^4+\cdots=\dfrac{x^2}{1-x}$.

Step 2. Product for 4 children:
$$G(x)=\left(\frac{x^2}{1-x}\right)^4=\frac{x^8}{(1-x)^4}$$

Step 3. Expand $\dfrac{1}{(1-x)^4}=\sum_{k\ge0}\binom{k+3}{3}x^k$.

Step 4. The number of ways to distribute $n$ balloons is the coefficient of $x^n$ in $G(x)$, which equals the coefficient of $x^{n-8}$ in $\dfrac{1}{(1-x)^4}$:
$$a_n=\binom{(n-8)+3}{3}=\binom{n-5}{3}$$

Step 5. For $n=10$:
$$a_{10}=\binom{10-5}{3}=\binom{5}{3}=10$$

$$\boxed{10}$$

---

**13.** Use generating functions to find the number of different ways 15 identical objects can be put into 6 distinct boxes such that each box contains at least one but no more than three objects.

**Solution.**

Step 1. Per-box OGF (between 1 and 3 objects): $x+x^2+x^3=x(1+x+x^2)=\dfrac{x(1-x^3)}{1-x}$.

Step 2. Product for 6 boxes:
$$G(x)=\left(\frac{x(1-x^3)}{1-x}\right)^6=\frac{x^6(1-x^3)^6}{(1-x)^6}$$

Step 3. The number of ways for $n$ objects is the coefficient of $x^n$ in $G(x)$. For $n=15$, we need the coefficient of $x^9$ in $\dfrac{(1-x^3)^6}{(1-x)^6}$.

Step 4. Expand $(1-x^3)^6=1-6x^3+15x^6-20x^9+15x^{12}-6x^{15}+x^{18}$.

And $\dfrac{1}{(1-x)^6}=\sum_{k\ge0}\binom{k+5}{5}x^k$.

Step 5. The coefficient of $x^9$ in the product:
$$a_{15}=1\cdot\binom{9+5}{5}-6\cdot\binom{6+5}{5}+15\cdot\binom{3+5}{5}-20\cdot\binom{0+5}{5}$$

$$=\binom{14}{5}-6\binom{11}{5}+15\binom{8}{5}-20\binom{5}{5}$$

Step 6. Compute each term:
- $\binom{14}{5}=2002$
- $\binom{11}{5}=462$
- $\binom{8}{5}=56$
- $\binom{5}{5}=1$

$$a_{15}=2002-6\cdot462+15\cdot56-20\cdot1$$
$$=2002-2772+840-20=50$$

$$\boxed{50}$$

---

**14.** How many words are formed from all letters of the word MISSISSIPPI that

**(a)** does not contain four letters S consecutively.

**Solution.**

Step 1. Total arrangements of MISSISSIPPI letters: M(1), I(4), S(4), P(2). Total 11 letters.
$$\text{Total}=\frac{11!}{1!\,4!\,4!\,2!}=\frac{11!}{4!\,4!\,2!}=\frac{39916800}{24\cdot24\cdot2}=34650$$

Step 2. Count arrangements **with** four consecutive S's. Glue the four S's into one block "SSSS". Now we arrange: M(1), I(4), SSSS(1), P(2). Total 8 objects.
$$\text{With SSSS}=\frac{8!}{1!\,4!\,1!\,2!}=\frac{8!}{4!\,2!}=\frac{40320}{24\cdot2}=840$$

Step 3. By the Complement Rule:
$$\text{Without SSSS}=34650-840=33810$$

$$\boxed{33810}$$

---

**(b)** does not contain four consecutive letters S nor two consecutive letters P.

**Solution.**

Step 1. Define properties:
- $A$: contains four consecutive S's (block "SSSS").
- $B$: contains two consecutive P's (block "PP").

We want words with **neither** property: $|U|-|A\cup B|$, where $|U|=34650$.

Step 2. Compute $|A|=840$ (from part (a)).

Step 3. Compute $|B|$: glue "PP" as one block. Objects: M(1), I(4), S(4), PP(1). Total 10.
$$|B|=\frac{10!}{1!\,4!\,4!\,1!}=\frac{10!}{4!\,4!}=\frac{3628800}{576}=6300$$

Step 4. Compute $|A\cap B|$: both "SSSS" and "PP" as blocks. Objects: M(1), I(4), SSSS(1), PP(1). Total 7.
$$|A\cap B|=\frac{7!}{1!\,4!\,1!\,1!}=\frac{7!}{4!}=\frac{5040}{24}=210$$

Step 5. By PIE:
$$|A\cup B|=|A|+|B|-|A\cap B|=840+6300-210=6930$$

Step 6.
$$\text{Without either}=34650-6930=27720$$

Check: $|=34650-6300-840+210=27720$. ✓

$$\boxed{27720}$$

---

**15.** Use PIE to find the number of positive integers not exceeding 100 that are NOT divisible by 5 or by 7.

**Solution.**

Step 1. Define properties:
- $A$: integer in $\{1,\dots,100\}$ divisible by 5.
- $B$: integer in $\{1,\dots,100\}$ divisible by 7.

We want integers with **neither** property.

Step 2. Universe $U=\{1,2,\dots,100\}$, $|U|=100$.

Step 3.
$$|A|=\left\lfloor\frac{100}{5}\right\rfloor=20$$
$$|B|=\left\lfloor\frac{100}{7}\right\rfloor=14$$
$$|A\cap B|=\left\lfloor\frac{100}{35}\right\rfloor=2\quad(\text{lcm}(5,7)=35)$$

Step 4. By PIE:
$$|A\cup B|=|A|+|B|-|A\cap B|=20+14-2=32$$

Step 5.
$$\text{Answer}=100-|A\cup B|=100-32=68$$

$$\boxed{68}$$

---

**16.** Use PIE to find the number of positive integers not exceeding 100 that are either odd or the square of an integer.

**Solution.**

Step 1. Define:
- $A$: odd integers in $\{1,\dots,100\}$.
- $B$: perfect squares in $\{1,\dots,100\}$.

We want $|A\cup B|$.

Step 2.
$$|A|=\left\lceil\frac{100}{2}\right\rceil=50\quad(\text{odd numbers from }1,3,\dots,99)$$

Step 3. Perfect squares up to 100: $1^2=1,2^2=4,\dots,10^2=100$. So $|B|=10$.

Step 4. $A\cap B$: odd perfect squares up to 100. These are $1^2=1,3^2=9,5^2=25,7^2=49,9^2=81$. So $|A\cap B|=5$.

Step 5. By PIE:
$$|A\cup B|=|A|+|B|-|A\cap B|=50+10-5=55$$

$$\boxed{55}$$

---

**17.** Find the number of positive integers not exceeding 1000 that are either the square or cube of an integer.

**Solution.**

Step 1. Define:
- $A$: perfect squares in $\{1,\dots,1000\}$.
- $B$: perfect cubes in $\{1,\dots,1000\}$.

We want $|A\cup B|$.

Step 2.
$$|A|=\lfloor\sqrt{1000}\rfloor=\lfloor31.62\rfloor=31$$

Step 3.
$$|B|=\lfloor\sqrt[3]{1000}\rfloor=10\quad(\text{since }10^3=1000)$$

Step 4. $A\cap B$: numbers that are both perfect squares and perfect cubes = perfect sixth powers.
$$|A\cap B|=\lfloor\sqrt[6]{1000}\rfloor=\lfloor3.16\rfloor=3\quad(1^6=1,2^6=64,3^6=729)$$

Step 5. By PIE:
$$|A\cup B|=31+10-3=38$$

$$\boxed{38}$$

---

**18.** How many elements are in the union of four sets if each of the sets has 100 elements, each pair of the sets share 50 elements, each three of the sets share 25 elements, and there are 5 elements in all four sets?

**Solution.**

Step 1. Apply the PIE formula for 4 sets $A_1,A_2,A_3,A_4$:
$$|A_1\cup A_2\cup A_3\cup A_4|=\sum|A_i|-\sum_{i<j}|A_i\cap A_j|+\sum_{i<j<k}|A_i\cap A_j\cap A_k|-|A_1\cap A_2\cap A_3\cap A_4|$$

Step 2. Substitute given values:
- $\sum|A_i|=4\cdot100=400$
- $\sum_{i<j}|A_i\cap A_j|=\binom{4}{2}\cdot50=6\cdot50=300$
- $\sum_{i<j<k}|A_i\cap A_j\cap A_k|=\binom{4}{3}\cdot25=4\cdot25=100$
- $|A_1\cap A_2\cap A_3\cap A_4|=5$

Step 3.
$$|A_1\cup A_2\cup A_3\cup A_4|=400-300+100-5=195$$

$$\boxed{195}$$

---

**19.** In a survey of 270 college students, it is found that 64 students like Brussels sprouts, 94 like broccoli, 58 like cauliflower, 26 like both Brussels sprouts and broccoli, 28 like both Brussels sprouts and cauliflower, 22 like both cauliflower and broccoli, and 14 like all three vegetables. How many of the 270 students do not like any of these vegetables?

**Solution.**

Step 1. Define sets:
- $B$: like Brussels sprouts, $|B|=64$.
- $R$: like broccoli, $|R|=94$.
- $C$: like cauliflower, $|C|=58$.

Step 2. Given intersections:
$$\begin{aligned}
|B\cap R|&=26\\
|B\cap C|&=28\\
|R\cap C|&=22\\
|B\cap R\cap C|&=14
\end{aligned}$$

Step 3. By PIE for three sets:
$$|B\cup R\cup C|=|B|+|R|+|C|-|B\cap R|-|B\cap C|-|R\cap C|+|B\cap R\cap C|$$
$$=64+94+58-26-28-22+14$$
$$=216-76+14=154$$

Step 4. Students liking **none**:
$$270-|B\cup R\cup C|=270-154=116$$

$$\boxed{116}$$

---

**20.** How many terms are there in the formula for the number of elements in the union of 5 sets given by PIE?

**Solution.**

Step 1. The PIE formula for 5 sets alternates sums of intersections of $k$ sets for $k=1,2,\dots,5$.

Step 2. The number of terms at level $k$ (intersections of exactly $k$ sets) is $\binom{5}{k}$. The total number of terms is the sum:
$$\binom{5}{1}+\binom{5}{2}+\binom{5}{3}+\binom{5}{4}+\binom{5}{5}$$

Step 3. Compute:
$$\binom{5}{1}=5,\;\binom{5}{2}=10,\;\binom{5}{3}=10,\;\binom{5}{4}=5,\;\binom{5}{5}=1$$

Step 4. Total:
$$5+10+10+5+1=31$$

Alternatively, $2^5-1=31$ (all non-empty subsets of a 5-element set).

$$\boxed{31}$$

---

**21.** How many permutations of the 26 letters of the English alphabet do not contain any of the strings "fish", "rat", and "bird"?

**Solution.**

Step 1. Define properties (a permutation has the property if it contains the string as a contiguous block):
- $A$: contains "fish" as a block.
- $B$: contains "rat" as a block.
- $C$: contains "bird" as a block.

Total permutations: $|U|=26!$.

Step 2. Compute $|A|$: treat "fish" as one block. Then we have 23 objects (22 remaining letters + 1 block): $23!$.

Step 3. Compute $|B|$: treat "rat" as one block. 24 objects: $24!$.

Step 4. Compute $|C|$: treat "bird" as one block. 23 objects: $23!$.

Step 5. Compute $|A\cap B|$: treat both "fish" and "rat" as blocks. Check for overlapping letters: "fish" uses f,i,s,h; "rat" uses r,a,t. No overlap, so they can coexist. 21 objects: $21!$.

Step 6. Compute $|A\cap C|$: "fish" and "bird". "fish" uses f,i,s,h; "bird" uses b,i,r,d. They share the letter 'i'! The blocks overlap — they cannot appear simultaneously as disjoint blocks. $|A\cap C|=0$.

Step 7. Compute $|B\cap C|$: "rat" and "bird". "rat" uses r,a,t; "bird" uses b,i,r,d. They share 'r'. Cannot coexist: $|B\cap C|=0$.

Step 8. Compute $|A\cap B\cap C|$: all three blocks. Since $A\cap C$ already impossible, $|A\cap B\cap C|=0$.

Step 9. By PIE:
$$|A\cup B\cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|$$
$$= 23! + 24! + 23! - 21! - 0 - 0 + 0$$
$$= 2\cdot23! + 24! - 21!$$

Step 10. Answer (no such strings):
$$\text{Answer}=26! - (2\cdot23! + 24! - 21!) = 26!-24!-2\cdot23!+21!$$

$$\boxed{26!-24!-2\cdot23!+21!}$$

---

**22.** How many non-negative integer solutions does $x+y+z=13$ have, where $0\le x,y,z\le6$?

**Solution.**

Step 1. **Unrestricted** solutions ($x,y,z\ge0$, $\sum=13$): $\binom{13+3-1}{13}=\binom{15}{2}=105$.

Step 2. Define properties $P_1$: $x\ge7$, $P_2$: $y\ge7$, $P_3$: $z\ge7$. We want solutions with **none** of these.

Step 3. $|P_1|$: set $x'=x-7\ge0$, solve $x'+y+z=6$. Number: $\binom{6+3-1}{6}=\binom{8}{2}=28$. By symmetry, same for $P_2,P_3$.

Step 4. $|P_i\cap P_j|$ (two variables $\ge7$): $x\ge7$ and $y\ge7$ gives sum $\ge14>13$, impossible. All pairwise intersections are $0$.

Step 5. $|P_1\cap P_2\cap P_3|$: also $0$.

Step 6. By PIE:
$$\text{solutions with none} = 105 - 3\cdot28 + 0 - 0 = 105-84=21$$

$$\boxed{21}$$

---

**23.** How many non-negative integer solutions does $x+y+z+t=18$ have, where $0\le x\le4$, $0\le y\le7$?

**Solution.**

Step 1. **Unrestricted** solutions ($x,y,z,t\ge0$, $\sum=18$): $\binom{18+4-1}{18}=\binom{21}{3}=1330$.

Step 2. Only $x$ and $y$ have upper bounds. Define:
- $P_1$: $x\ge5$
- $P_2$: $y\ge8$

We want solutions with **neither** property.

Step 3. $|P_1|$: set $x'=x-5\ge0$, solve $x'+y+z+t=13$. Number: $\binom{13+4-1}{13}=\binom{16}{3}=560$.

Step 4. $|P_2|$: set $y'=y-8\ge0$, solve $x+y'+z+t=10$. Number: $\binom{10+4-1}{10}=\binom{13}{3}=286$.

Step 5. $|P_1\cap P_2|$: set $x'=x-5\ge0$, $y'=y-8\ge0$, solve $x'+y'+z+t=5$. Number: $\binom{5+4-1}{5}=\binom{8}{3}=56$.

Step 6. By PIE:
$$\text{solutions with neither} = 1330 - 560 - 286 + 56 = 540$$

$$\boxed{540}$$

---

**24.** How many surjective (onto) functions are there from a set with 7 elements to a set with 5 elements?

**Solution.**

Step 1. A surjection from a 7-set to a 5-set means every element of the codomain is hit at least once. Use the PIE formula for surjections:
$$\text{Surj}(m,n)=\sum_{j=0}^{n}(-1)^j\binom{n}{j}(n-j)^m$$
with $m=7$, $n=5$.

Step 2. Compute:
$$\begin{aligned}
j=0&: &+\binom{5}{0}5^7 &= 1\cdot78125 &= 78125\\
j=1&: &-\binom{5}{1}4^7 &= -5\cdot16384 &= -81920\\
j=2&: &+\binom{5}{2}3^7 &= +10\cdot2187 &= 21870\\
j=3&: &-\binom{5}{3}2^7 &= -10\cdot128 &= -1280\\
j=4&: &+\binom{5}{4}1^7 &= +5\cdot1 &= 5\\
j=5&: &-\binom{5}{5}0^7 &= -1\cdot0 &= 0
\end{aligned}$$

Step 3. Sum:
$$78125-81920+21870-1280+5-0=16800$$

Alternatively, use the formula $5!\cdot S(7,5)$, where $S(7,5)=140$:
$$5!\cdot S(7,5)=120\cdot140=16800$$

$$\boxed{16800}$$

---

**25.** How many ways are there to distribute six different toys to three different children such that each child gets at least one toy?

**Solution.**

Step 1. This is a surjection from a 6-set (toys) to a 3-set (children). Each toy goes to one child; each child must receive at least one toy.

Step 2. PIE formula with $m=6$, $n=3$:
$$\text{Surj}(6,3)=\sum_{j=0}^{3}(-1)^j\binom{3}{j}(3-j)^6$$

$$\begin{aligned}
j=0&: &+\binom{3}{0}3^6 &= 1\cdot729 &= 729\\
j=1&: &-\binom{3}{1}2^6 &= -3\cdot64 &= -192\\
j=2&: &+\binom{3}{2}1^6 &= +3\cdot1 &= 3\\
j=3&: &-\binom{3}{3}0^6 &= -1\cdot0 &= 0
\end{aligned}$$

Step 3.
$$\text{Surj}(6,3)=729-192+3=540$$

Alternatively: $3!\cdot S(6,3)=6\cdot90=540$. ✓

$$\boxed{540}$$

---

**26.** In how many ways can eight distinct balls be distributed into three distinct urns if each urn must contain at least one ball?

**Solution.**

Step 1. Surjection from an 8-set to a 3-set. Use PIE with $m=8$, $n=3$:

$$\text{Surj}(8,3)=\sum_{j=0}^{3}(-1)^j\binom{3}{j}(3-j)^8$$

$$\begin{aligned}
j=0&: &+\binom{3}{0}3^8 &= 1\cdot6561 &= 6561\\
j=1&: &-\binom{3}{1}2^8 &= -3\cdot256 &= -768\\
j=2&: &+\binom{3}{2}1^8 &= +3\cdot1 &= 3\\
j=3&: &-\binom{3}{3}0^8 &= -0 &= 0
\end{aligned}$$

Step 2.
$$\text{Surj}(8,3)=6561-768+3=5796$$

Alternatively: $3!\cdot S(8,3)=6\cdot966=5796$. ✓

$$\boxed{5796}$$

---

**27.** How many derangements of $[4]$ are there? List all derangements of $[4]$.

**Solution.**

Step 1. A derangement is a permutation with no fixed points. The number is $D_4$.

Step 2. Formula: $D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$.
$$D_4=4!\left(\frac{1}{0!}-\frac{1}{1!}+\frac{1}{2!}-\frac{1}{3!}+\frac{1}{4!}\right)=24\left(1-1+\frac12-\frac16+\frac1{24}\right)$$
$$=24\left(\frac{12-4+1}{24}\right)=24\cdot\frac{9}{24}=9$$

Or via recurrence: $D_1=0$, $D_2=1$, $D_3=2(1+0)=2$, $D_4=3(2+1)=9$.

Step 3. List all derangements of $[4]$ (in cycle notation):

**Two 2-cycles** (3 derangements):
$$(1\;2)(3\;4),\quad(1\;3)(2\;4),\quad(1\;4)(2\;3)$$

**One 4-cycle** (6 derangements):
$$(1\;2\;3\;4),\;(1\;2\;4\;3),\;(1\;3\;2\;4),\;(1\;3\;4\;2),\;(1\;4\;2\;3),\;(1\;4\;3\;2)$$

Total: $3+6=9$.

$$\boxed{D_4=9}$$

---

**28.** A group of 8 students is assigned seats for each of two classes in the same classroom. How many ways can these seats be assigned if no student is assigned the same seat for both classes?

**Solution.**

Step 1. For the first class, assign the 8 students to the 8 seats arbitrarily: $8!$ ways.

Step 2. For the second class, the assignment must be a derangement of the students' seats relative to the first class. That is, no student sits in the same seat they had for the first class. The number of such assignments is $D_8$.

Step 3. Compute $D_8$. Use the recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$ with $D_1=0$, $D_2=1$:
$$\begin{aligned}
D_3 &= 2(1+0) = 2\\
D_4 &= 3(2+1) = 9\\
D_5 &= 4(9+2) = 44\\
D_6 &= 5(44+9) = 265\\
D_7 &= 6(265+44) = 1854\\
D_8 &= 7(1854+265) = 7\cdot 2119 = 14833
\end{aligned}$$

Step 4. By the Product Rule:
$$\text{Total}=8!\cdot D_8=40320\cdot14833=598066560$$

$$\boxed{8!\cdot D_8=598066560}$$

---

**29.** How many non-negative integers not exceeding 100 are there which are relatively prime with 100?

**Solution.**

Step 1. This is Euler's totient function $\varphi(100)$, which counts positive integers $a\le 100$ with $\gcd(a,100)=1$.

Step 2. Factor $100$:
$$100=2^2\cdot5^2$$

Step 3. Apply the formula $\varphi(n)=n\prod_{p\mid n}\left(1-\dfrac{1}{p}\right)$:
$$\varphi(100)=100\left(1-\frac12\right)\left(1-\frac15\right)=100\cdot\frac12\cdot\frac45=100\cdot\frac{4}{10}=40$$

Step 4. The integers $0$ through $100$ relatively prime to $100$: since $\gcd(0,100)=100\neq1$, $0$ is not included. The positive integers not exceeding $100$ that are relatively prime to $100$ are precisely the $\varphi(100)=40$ numbers coprime to $100$ (all numbers from $1$ to $100$ not divisible by $2$ or $5$).

$$\boxed{\varphi(100)=40}$$
