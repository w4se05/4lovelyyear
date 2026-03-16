# Answer Key & Explanations

### Part 1: Logic
1.  **True**. Definition of equivalence ($p \leftrightarrow q$). 
2.  **False**. The negation is "Some birds cannot fly".
3.  **True**. In classical logic, either $p$ is true (making $q \Rightarrow p$ true) or $p$ is false (making $p \Rightarrow q$ true).
4.  **False**. Validity implies if premises are true, conclusion is true. Premises could be false. 
5.  **False**. De Morgan's Law says $\neg(p \wedge q) \equiv \neg p \vee \neg q$. 
6.  **True**. Modus Ponens is valid.
7.  **False**. Contrapositive switches AND negates: "If $x^2 \le 100$, then $x \le 10$".
8.  **True**. Negation of "For all" is "There exists one that does not".
9.  **False**. $p \Rightarrow q$ is FALSE when $p$ is True and $q$ is False. (Question said "only when").
10. **True**. Example: "Pigs fly (F) $\Rightarrow$ 1+1=2 (T)". Valid argument structure, unsound premises.

### Part 2: Sets & Relations
11. **False**. Power set has $2^n$ elements. 
12. **False**. It is Reflexive, Transitive, but NOT Symmetric ($1 \le 2$ but $2 \not\le 1$). It is a Partial Order. 
13. **False**. Counterexample: $R = \{(1,1)\}$ on set $\{1,2\}$. Sym/Trans hold, but $(2,2)$ missing. 
14. **False**. On $\mathbb{Z}$, $a|b$ and $b|a \implies a = \pm b$. Not antisymmetric. On $\mathbb{N}$, it is true. 
15. **True**. Equivalence classes partition the set. 
16. **True**. $a \neq a$ is false (Irreflexive). $a \neq b \implies b \neq a$ (Symmetric).
17. **True**. Definition of transitive closure. 
18. **False**. Antisymmetry says if $(a,b)$ and $(b,a)$ exist, then $a=b$. It allows $(a,b)$ if $(b,a)$ is absent.
19. **True**. Definition of invertible functions. 
20. **False**. Hasse diagrams omit loops and implied transitive edges. 

### Part 3: Number Theory
21. **True**. $\gcd(a,n) = \gcd(b+kn, n) = \gcd(b,n)$.
22. **False**. $\phi(p) = p - 1$.
23. **False**. Only true if $n$ is prime. In $\mathbb{Z}_6$, $2 \cdot 3 = 6 \equiv 0$, but $2 \not\equiv 0$ and $3 \not\equiv 0$.
24. **False**. $\gcd(e, \phi(n)) = 1$, not $\gcd(e, n) = 1$. 
25. **False**. It has 4 solutions ($1, -1$ and two others from CRT).
26. **True**. Definition of Euler's totient. 
27. **True**. Property of Mersenne primes. 
28. **True**. Inverse exists iff $\gcd(a,n)=1$. 
29. **True**. Caesar is shift $x+b$. Affine is $ax+b$. If $a=1$, they match. 
30. **False**. Dangerous message is $\gcd(m,n) = p$ or $q$. If $\gcd=1$, it's safe. 
31. **True**. $10 \equiv -1$. $(-1)^{even} = 1$.
32. **True**. Linear Diophantine equation solvability condition.

### Part 4: Matrices
33. **False**. $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}^2 = 0$. $A \neq 0, B=A \neq 0$. 
34. **False**. Only if $AB = BA$. Matrix multiplication is not commutative. 
35. **True**. Transpose and Inverse commute. 
36. **True**. Eigenvalues are on diagonal.
37. **True**. And columns too.
38. **False**. $\det(cA) = c^n \det(A)$ for $n \times n$. 
39. **True**. $(A^{-1})^T = (A^T)^{-1} = A^{-1}$.
40. **True**. Trace property. 
41. **False**. $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, $A^2 = I$. 
42. **True**. Determinant will be 0. 
43. **True**. $3 \times 3$ matrix: $\det(2A) = 2^3 \det(A) = 8 \cdot 2 = 16$. 
44. **False**. Swapping rows negates sign. Multiplying row scales determinant. Adding rows preserves it. 
45. **True**. Rank definition. 

### Part 5: Linear Systems
46. **True**. The trivial solution $x=0$ always works. 
47. **False**. Only if it is consistent. It could be inconsistent (parallel planes).
48. **True**. Rank $m$ means pivots in every row $\implies$ no row like $[0\dots0 | b]$.
49. **True**. Row equivalent matrices represent equivalent systems.
50. **False**. Only for square systems with non-zero determinant. 
51. **True**. Row implies $0 = b$ ($b \neq 0$). 
52. **False**. Could be inconsistent. If consistent + free variable $\implies$ infinite.
53. **False**. $A(x_1+x_2) = Ax_1 + Ax_2 = b + b = 2b \neq b$. (True for Homogeneous).
54. **True**. Rank-Nullity Theorem concept. 

### Part 6: Vector Spaces
55. **False**. Subspace must contain the zero vector. Empty set has nothing.
56. **False**. Sum of $t^2$ and $-t^2+t$ is $t$ (degree 1). Not closed under addition. 
57. **True**. Adding vectors doesn't reduce the span.
58. **True**. $1 \cdot 0 + 0 \cdot v = 0$ is a non-trivial combination.
59. **True**. Transformation matrix is upper triangular with 1s on diagonal (invertible).
60. **True**. Intersection is closed under operations.
61. **False**. Union is rarely a subspace (unless one contains the other).
62. **False**. They must be linearly independent (or span).
63. **True**. Definition of rank. 
64. **True**. Row ops change columns but preserve linear relations among columns (null space).
65. **False**. Infinitely many bases exist.
66. **False**. Does not contain zero vector ($0+0+0 \neq 1$). 
67. **True**. Pythagorean theorem for inner product spaces. 
68. **False**. Dimension is $2 \times 3 = 6$.
69. **True**. If proper subspace, dimension would be lower.

### Part 7: Linear Maps
70. **True**. For finite-dimensional spaces.
71. **False**. $T(0) = 1 \neq 0$. Fails additivity.
72. **True**. Kernel is trivial iff Injective. 
73. **True**. Composition preserves linearity.
74. **True**. From $R^3$ to $R^2$, Rank $\le 2 < 3$. Nullity must be $\ge 1$.
75. **True**. From $R^2$ to $R^3$, Rank $\le 2 < 3$. Cannot cover $R^3$.
76. **False**. Kernel is subspace of Domain ($V$). Image is subspace of Codomain ($W$). 
77. **True**. Transpose is linear. 
78. **True**. $T(0) = T(0+0) = T(0)+T(0) \implies T(0)=0$. 
79. **True**. Definition of column space.
80. **False**. Isomorphism $\implies$ Invertible $\implies$ Det $\neq 0$.

### Part 8: Advanced / Mixed
81. **True**. $B = P^{-1}AP \implies \det(B) = \det(P^{-1})\det(A)\det(P) = \det(A)$. 
82. **True**. $\det(A^2) = \det(A)^2 = \det(A)$. $x^2=x \implies x=0,1$.
83. **False**. Sum of invertible matrices (e.g., $I$ and $-I$) can be zero (not invertible). 
84. **False**. Positivity fails. $(1,0) \cdot (1,0) = 1 > 0$, but $(0,1) \cdot (0,1) = -1 < 0$. Inner products must be positive definite.
85. **True**. Definition of independence extension.
86. **True**. 0, 1, or Infinite. Never exactly 2 (for Real/Complex fields). 
87. **False**. Rank $\le \min(3,5) = 3$.
88. **False**. $\det(I+I) = 2^n \neq 1+1$.
89. **True**. $A=A^T, B=B^T \implies (A+B)^T = A^T+B^T = A+B$. Closed. 
90. **True**. Evaluation functional is linear.
91. **False**. Dependent $(2,2) = 2(1,1)$.
92. **True**. Sum Dimension formula.
93. **False**. $Ax=b$ solvable iff $b$ is **in the column space**, or $b$ is orthogonal to the **Left Null Space** (Null($A^T$)). Not rows of $A$.
94. **True**. Singular matrix.
95. **False**. Neither is a scalar multiple of the other.
96. **True**. $T(c(x,y)) = T(cx, cy) = (c^2 x^2, cy) \neq c(x^2, y)$. 
97. **True**. $Ax = \lambda x \implies A^2x = A(\lambda x) = \lambda Ax = \lambda^2 x$.
98. **True**. Row rank = Column rank. 
99. **True**. If product is invertible, factors must be invertible (for square matrices). 
100. **True**. You practiced 100 questions.