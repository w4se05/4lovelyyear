	### **Part 1: Logic & Proofs**
1.  The statement $(p \Rightarrow q) \wedge (q \Rightarrow p)$ is logically equivalent to $p \Leftrightarrow q$.
2.  The negation of "Every bird can fly" is "No bird can fly".
3.  The formula $(p \Rightarrow q) \vee (q \Rightarrow p)$ is a tautology (always true).
4.  If an argument is valid, then its conclusion must be true.
5.  The statement $\neg(p \wedge q)$ is logically equivalent to $\neg p \wedge \neg q$.
6.  "Correlation implies causation" is a logical fallacy, but $(p \wedge (p \Rightarrow q)) \Rightarrow q$ is a valid logical inference rule (Modus Ponens).
7.  The contrapositive of "If $x > 10$, then $x^2 > 100$" is "If $x^2 \le 100$, then $x \le 10$".
8.  To prove a statement of the form $\forall x, P(x)$ is false, it is sufficient to find a single counterexample.
9.  The statement $p \Rightarrow q$ is false only when $p$ is false and $q$ is true.
10. A valid argument can have false premises and a true conclusion.

### **Part 2: Sets & Relations**
11. If $A$ has $n$ elements, the power set $\mathcal{P}(A)$ has $2^n - 1$ elements.
12. The relation $R = \{(x,y) \in \mathbb{R}^2 : x \le y\}$ is an equivalence relation.
13. If a relation is symmetric and transitive, it must be reflexive.
14. The "divides" relation ($a|b$) on the set of integers $\mathbb{Z}$ is a partial ordering.
15. If $R$ is an equivalence relation on set $A$, the intersection of any two distinct equivalence classes is empty.
16. The relation $R = \{(a,b) : a \neq b\}$ is irreflexive and symmetric.
17. The transitive closure of a relation $R$ is the smallest transitive relation containing $R$.
18. If $R$ is antisymmetric, it cannot contain any pair $(a,b)$ where $a \neq b$.
19. A function $f: A \to B$ is invertible if and only if it is bijective (one-to-one and onto).
20. In a Hasse diagram for a partial order, loops (reflexive pairs) are explicitly drawn.

### **Part 3: Number Theory & Cryptography**
21. If $a \equiv b \pmod n$, then $\gcd(a, n) = \gcd(b, n)$.
22. The Euler totient function $\phi(p)$ for a prime $p$ is $p$.
23. If $ab \equiv 0 \pmod n$, then either $a \equiv 0 \pmod n$ or $b \equiv 0 \pmod n$.
24. In RSA, the public exponent $e$ and the modulus $n$ must be relatively prime ($\gcd(e, n) = 1$).
25. If $n = pq$ where $p$ and $q$ are distinct primes, then $x^2 \equiv 1 \pmod n$ has exactly 2 solutions in $\mathbb{Z}_n$.
26. The number of integers less than $n$ that are relatively prime to $n$ is given by $\phi(n)$.
27. If $2^n - 1$ is prime, then $n$ must be prime (Mersenne primes).
28. The Extended Euclidean Algorithm can be used to find the multiplicative inverse of $a$ modulo $n$ only if $\gcd(a, n) = 1$.
29. Caesar cipher is a specific case of an affine cipher $y = ax + b \pmod{26}$ where $a=1$.
30. A "dangerous message" in RSA is one where $\gcd(m, n) = 1$.
31. $10 \equiv -1 \pmod{11}$, therefore $10^{2026} \equiv 1 \pmod{11}$.
32. The Diophantine equation $ax + by = c$ has integer solutions if and only if $\gcd(a, b)$ divides $c$.

### **Part 4: Matrices & Determinants**
33. If $AB = 0$ and $A$ is not the zero matrix, then $B$ must be the zero matrix.
34. $(A + B)^2 = A^2 + 2AB + B^2$ for any two $n \times n$ matrices.
35. If $A$ is invertible, then $(A^T)^{-1} = (A^{-1})^T$.
36. The determinant of a triangular matrix is the product of its diagonal entries.
37. If $\det(A) = 0$, then the rows of $A$ are linearly dependent.
38. For any scalar $c$ and $n \times n$ matrix $A$, $\det(cA) = c \det(A)$.
39. If $A$ is symmetric, then $A^{-1}$ (if it exists) is also symmetric.
40. $Tr(AB) = Tr(BA)$ for any square matrices $A$ and $B$ of the same size.
41. If $A^2 = I$, then $A$ must be $I$ or $-I$.
42. A square matrix with a row of zeros cannot be invertible.
43. If $A$ is $3 \times 3$ and $\det(A) = 2$, then $\det(2A) = 16$.
44. Elementary row operations do not change the determinant of a matrix.
45. The rank of a matrix is equal to the number of non-zero rows in its reduced row echelon form.

### **Part 5: Linear Systems**
46. A homogeneous system $Ax = 0$ always has at least one solution.
47. If a system $Ax = b$ has more variables than equations, it must have infinitely many solutions.
48. If $A$ is an $m \times n$ matrix and rank($A$) = $m$, then $Ax = b$ is consistent for every $b \in \mathbb{R}^m$.
49. If two linear systems have the same solution set, their augmented matrices must be row equivalent.
50. Cramer's Rule can be used to solve any system of $n$ linear equations with $n$ variables.
51. If the augmented matrix $[A|b]$ has a pivot in the last column, the system is inconsistent.
52. A system with a free variable always has infinitely many solutions.
53. If $x_1$ and $x_2$ are solutions to the non-homogeneous system $Ax = b$, then $x_1 + x_2$ is also a solution to $Ax = b$.
54. The dimension of the null space of $A$ is the number of free variables in the equation $Ax=0$.

### **Part 6: Vector Spaces**
55. The empty set $\emptyset$ is a subspace of every vector space.
56. The set of all polynomials of degree **exactly** 2 is a subspace of $P_2$.
57. If a set of vectors spans a space $V$, then any superset of those vectors also spans $V$.
58. A set of vectors containing the zero vector is always linearly dependent.
59. If $\{v_1, v_2, v_3\}$ is a linearly independent set, then $\{v_1, v_1+v_2, v_1+v_2+v_3\}$ is also linearly independent.
60. The intersection of any two subspaces of $V$ is a subspace of $V$.
61. The union of any two subspaces of $V$ is a subspace of $V$.
62. If $\dim(V) = n$, then any set of $n$ vectors in $V$ is a basis for $V$.
63. The dimension of the subspace spanned by the columns of $A$ (Column Space) is equal to the rank of $A$.
64. Row operations change the column space of a matrix but preserve the null space.
65. The vector space $\mathbb{R}^3$ has exactly one basis.
66. The set of solutions to $x + y + z = 1$ is a subspace of $\mathbb{R}^3$.
67. If $u$ is orthogonal to $v$, then $\|u+v\|^2 = \|u\|^2 + \|v\|^2$.
68. The dimension of $M_{2 \times 3}$ (the space of $2 \times 3$ matrices) is 5.
69. If $W$ is a subspace of $V$ and $\dim(W) = \dim(V)$, then $W = V$ (for finite-dimensional $V$).

### **Part 7: Linear Maps**
70. Every linear map $T: \mathbb{R}^n \to \mathbb{R}^m$ can be represented by a matrix.
71. The map $T(x) = x + 1$ is a linear transformation.
72. If a linear map $T: V \to W$ is injective (one-to-one), then $\ker(T) = \{0\}$.
73. The composition of two linear transformations is a linear transformation.
74. If $T: \mathbb{R}^3 \to \mathbb{R}^2$ is a linear map, it cannot be injective.
75. If $T: \mathbb{R}^2 \to \mathbb{R}^3$ is a linear map, it cannot be surjective (onto).
76. The kernel of a linear transformation $T: V \to W$ is a subspace of $W$.
77. The map $T(A) = A^T$ from $M_{n \times n}$ to $M_{n \times n}$ is linear.
78. If $T$ is linear, then $T(0_V) = 0_W$.
79. The range (image) of a matrix transformation $x \mapsto Ax$ is the column space of $A$.
80. If $T: \mathbb{R}^n \to \mathbb{R}^n$ is an isomorphism, then its standard matrix has determinant 0.

### **Part 8: Advanced / Mixed Concepts**
81. If $A$ is similar to $B$, then $\det(A) = \det(B)$.
82. If $A^2 = A$ (idempotent), then $\det(A)$ must be 0 or 1.
83. The set of invertible $n \times n$ matrices forms a subspace of $M_{n \times n}$.
84. $x \cdot y = x_1 y_1 - x_2 y_2$ defines a valid inner product on $\mathbb{R}^2$.
85. If $S$ is a linearly independent set and $v \notin \text{span}(S)$, then $S \cup \{v\}$ is linearly independent.
86. A system of linear equations with real coefficients cannot have exactly 2 solutions.
87. If $A$ is a $3 \times 5$ matrix, the largest possible rank of $A$ is 5.
88. $\det(A+B) = \det(A) + \det(B)$ if $A$ is diagonal.
89. The set of symmetric matrices is a subspace of $M_{n \times n}$.
90. If $T: P_2 \to \mathbb{R}$ is defined by $T(p) = p(1)$, then $T$ is linear.
91. The vector $(1, 1)$ and $(2, 2)$ form a basis for $\mathbb{R}^2$.
92. For vector spaces, $\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$.
93. $Ax = b$ has a solution if and only if $b$ is orthogonal to the rows of $A$.
94. If the columns of $A$ are linearly dependent, then $\det(A) = 0$ (for square $A$).
95. In the vector space of functions, $\sin(x)$ and $\cos(x)$ are linearly dependent.
96. The transformation $T(x, y) = (x^2, y)$ is non-linear.
97. If $\lambda$ is an eigenvalue of $A$, then $\lambda^2$ is an eigenvalue of $A^2$. (Bonus concept).
	1. The rank of $A$ is equal to the rank of $A^T$.
98. If $AB$ is invertible, then both $A$ and $B$ must be invertible (for square matrices).
99. You are going to ace this exam.
