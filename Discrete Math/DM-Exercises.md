## Section 1: Basic Counting Rules

### 1.1 Subsets

1. How many subsets of a set with $n$ elements have exactly **two** elements?
2. How many subsets of a set with **100** elements have **at most two** elements?
3. How many subsets of a set with **100** elements have **more than two** elements?
4. How many subsets of a set with $n$ elements are there?

---

### 1.2 Euler's Phi Function

7. Prove that Euler's phi function $\phi(p^k) = p^k - p^{k-1}$ where $p$ is prime and $k$ is a positive integer.

---

### 1.3 Product & Sum Rule

5. How many strings of **five ASCII characters** contain the character `@` at least once? *(There are 128 different ASCII characters.)*
8. Chairs are labeled with an uppercase English letter followed by a positive integer not exceeding 100. What is the largest number of chairs that can be labeled differently?
9. How many different license plates can be made if each plate contains **three uppercase English letters** followed by **three digits**?
10. A computer password is between **4 and 8 characters** long and composed of lower and/or upper case letters. How many passwords are possible?

---

### 1.4 Permutations & Arrangements

11. In how many ways may a **ten-person club** select a president and a two-person executive advisory board? *(The president is not on the advisory board.)*
12. What is the number of five-digit numbers? What is the number of five-digit numbers that have **no two consecutive digits equal**? What is the number that have **at least one pair** of consecutive digits equal?
20. In how many ways can you draw a **first, second, and third card** from a deck of 52 cards?
21. In how many ways can you draw **two cards** from a deck of 52 cards? *(Order does not matter.)*
27. A tennis club has $2n$ members. In how many ways may we **pair up all members** for singles matches? If we also specify who **serves first** for each pairing, in how many ways may we specify our pairs?
31. How many permutations of the characters `ABC12DE` contain the string `BC1`?
32. A group contains $n$ men and $n$ women. How many ways are there to arrange them in a row if the **men and women alternate**?
33. How many permutations of $[2n]$ assign **even numbers to odd positions**?

---

### 1.5 Bit Strings

6. How many bit strings of length **5** contain:
   - (a) exactly two occurrences of 0s?
   - (b) at most two occurrences of 0s?
   - (c) at least two occurrences of 0s?
26. How many bit strings of length $n$ have exactly $k$ occurrences of 0s?
35. Count the number of bit strings of length **7** that either start with a `0` or end with the two bits `10`.

---

### 1.6 Functions

13. List all **functions** from $[3]$ to $[2]$.
14. List all **one-to-one functions** from $[2]$ to $[3]$.
15. List all **bijections** from $[3]$ to $[3]$.
16. How many **functions** from $[m]$ to $[n]$ are there?
17. List all **one-to-one functions** from $[2]$ to $[4]$.
18. How many **one-to-one functions** from $[3]$ to $[5]$ are there?
19. How many **one-to-one functions** from $[m]$ to $[n]$ are there?

---

### 1.7 Combinations & Selections

22. Given $n$ different objects in a box, take $k$ objects out:
    - (a) How many ways if **order matters**?
    - (b) How many ways if **order does not matter**?
28. How many 3-digit numbers have digits that are **pairwise different** and **decrease from left to right**?
33. A class has **25 students**. How many choices are there to:
    - Pick 3 students for a **Calculus** competition?
    - Pick 3 students where one goes to Calculus, one to Algebra, one to Discrete Math?
34. A class has **9 female** and **20 male** students. How many ways to pick 11 students for a soccer team if:
    - (a) the team must have exactly **3 female** students?
    - (b) the team must have **at least one female** student?

---

### 1.8 Binomial Theorem & Identities

29. Give a bijection proving $\dbinom{n}{k} = \dbinom{n}{n-k}$.
30. Give **two proofs** for each of the following identities:
    - (a) $\dbinom{2n}{2} = 2\dbinom{n}{2} + n^2$
    - (b) $\dbinom{n}{1} + 2\dbinom{n}{2} + 3\dbinom{n}{3} + \cdots + n\dbinom{n}{n} = n \cdot 2^{n-1}$
    - (c) $n\dbinom{n-1}{2} = \dbinom{n}{2}(n-2)$
    - (d) Pascal's triangle: $C_n^k = C_{n-1}^k + C_{n-1}^{k-1}$
    - (e) $C_n^k \cdot C_k^j = C_n^j \cdot C_{n-j}^{k-j}$
    - (f) $C_n^k \cdot C_{n-k}^j = C_n^j \cdot C_{n-j}^k$
    - (g) Vandermonde's identity: $C_{m+n}^r = \displaystyle\sum_{i=0}^{r} C_m^i \cdot C_n^{r-i}$
36. The row of Pascal's triangle for $\binom{10}{k}$, $0 \leq k \leq 10$, is:
    `1 10 45 120 210 252 210 120 45 10 1`
    Use Pascal's formula to produce the **next two rows**.
37. Find the coefficient of $x^{101}y^{99}$ in the expansion of $(2x - 3y)^{200}$.
38. Give the formula for the coefficient of $x^k$ in the expansion of $\left(x + \dfrac{1}{x}\right)^{100}$, where $k$ is an integer.
39. Find the coefficient of $x^{101}y^{99}z^{105}$ in the expansion of $(2x - 3y - z)^{305}$.
40. You have **10 distinct chairs** to paint. How many ways to paint 3 green, 3 blue, and 4 red?
41. In a Cartesian coordinate system, how many **paths** are there from the origin to $(m, n)$ using exactly $m+n$ unit horizontal and vertical segments?
42. **True or False** (give reason): $\dbinom{n}{k} = \dbinom{n-2}{k-2} + \dbinom{n-2}{k-1} + \dbinom{n-2}{k}$
43. How many different strings can be made from the letters in **CASABLANCA** using all letters?
44. How many different strings can be made from the letters in **SUCCESS** using all letters?
45. Find the coefficient of $x^3 y^2 z^5$ in the expansion of $(2x - 3y - 2z)^{10}$.

---

### 1.9 Distributions — Distinct Objects

23. In how many ways can we pass out $k$ **distinct** fruits to $n$ children with **no restriction**?
24. In how many ways can we pass out $k$ **distinct** fruits to $n$ children if each child may get **at most one**? What if $k > n$?
66. How many ways are there to place **15 distinct** gifts into **10 distinct** boxes?
67. How many ways to place **15 distinct** gifts into **10 distinct** boxes such that each box contains **at least 1** gift?
68. How many ways to place **15 distinct** gifts into **10 distinct** boxes such that each box contains **at most 1** gift?
69. How many ways to place **10 distinct** gifts into **15 distinct** boxes such that each box contains **at most 1** gift?
81. There are **4 men** and **6 women**. Each man marries one of the women. In how many ways can this be done?

---

### 1.10 Distributions — Identical Objects & Stars and Bars

25. In how many ways can we pass out $k$ **identical** fruits to $n$ children if each child may get **at most one**? What if $k > n$?
46. How many ways are there to line up **3 identical red** apples and **2 identical golden** apples?
47. How many ways are there to line up **3 identical red**, **2 identical golden**, and **4 identical green** apples?
48. How many ways are there to distribute $k$ **indistinguishable** apples to $n$ children?
49. How many ways are there to place $k$ **indistinguishable** books onto the $n$ shelves of a bookcase?
50. How many **non-negative** solutions of $x_1 + x_2 + \cdots + x_n = k$ are there?
51. How many **positive integer** solutions of $x_1 + x_2 + \cdots + x_n = k$ are there? *(each $x_i > 0,\ x_i \in \mathbb{Z}$)*
52. In how many ways may we pass out $k$ **indistinguishable** apples to $n$ children if each child must get **at least one**?
53. In how many ways may $n$ **red** checkers and $n+1$ **black** checkers be arranged in a **circle**?
54. How many solutions to $x_1 + x_2 + x_3 + x_4 + x_5 = 21$ with $x_i$ non-negative integers such that:
    - (a) $x_i \geq 1$ for all $i$
    - (b) $x_i \geq 2$ for all $i$
    - (c) $0 \leq x_1 \leq 10$
55. How many solutions to the **inequality** $x_1 + x_2 + x_3 \leq 11$, where $x_1, x_2, x_3$ are non-negative integers?
70. How many ways are there to place **100 identical** gifts into **3 distinct** boxes?
71. How many ways are there to place **100 identical** gifts into **10 distinct** boxes such that each box contains **at least 5** gifts?
80. A student has **3 mangos, 2 papayas, and 2 kiwi fruits**, eaten one per day (only type matters). How many different orders?
82. How many ways to pack **8 identical DVDs** into **5 indistinguishable** boxes so that each box contains **at least one** DVD?
83. There are **10 questions** on a DM exam. How many ways to assign scores if the sum is **100** and each question is worth **at least 5 points**?

---

### 1.11 Stirling Numbers & Set Partitions

56. Which of the following subsets form a **partition** of the set of all real numbers?
    - (a) Positive integers, negative integers
    - (b) Non-positive integers, non-negative integers
    - (c) Rational numbers, irrational numbers
    - (d) Closed intervals $[n, n+1]$ where $n$ is an integer
    - (e) Intervals $(n, n+1]$ where $n$ is an integer
57. List all **partitions of $[4]$** into $k = 1, 2, 3, 4$ parts. What is $S(4,k)$? What is the **4th Bell number**?
58. What are $S(n,1)$, $S(n,n-1)$, $S(n,n)$ in the general case?
59. Construct a **recursive formula** for $S(n,k)$. What is the value of $S(n,2)$?
60. Construct a **bijection** from the set of all partitions of $[n]$ into 2 parts to the family of non-empty subsets of $[n-1]$.
61. Which of these collections are **partitions** of $\{1,2,3,4,5,6\}$?
    - (a) $\{1,2\},\ \{2,3,4\},\ \{4,5,6\}$
    - (b) $\{1\},\ \{2,3,6\},\ \{4\}$
    - (c) $\{2,4,6\},\ \{1,3,5\}$
    - (d) $\{1,4,5\},\ \{2,6\}$
62. How many ways to place **4 distinct** gifts into **3 identical** boxes?
63. How many ways to place **4 distinct** gifts into **3 identical** boxes such that each box has **at least 1** gift?
64. How many ways to place **4 identical** gifts into **3 identical** boxes?
65. How many ways to place **4 identical** gifts into **3 identical** boxes such that each box has **at least 1** gift?

---

### 1.12 Permutations — Notation & Operations

72. Write down all possible **permutations of $[4]$** that map $1 \to 3$.
73. Write down all permutations of $[5]$ in **two-line notation** that have **5 as a fixed point** and map $3 \to 2$.
74. Write the following permutations in **cycle notation** and **two-line notation**; find their fixed points; count the number of cycles; compute $\sigma^{-1}$ and $\sigma^2$:
    - (a) $\sigma = 36215847$
    - (b) $\sigma = 42765813$
    - (c) $\sigma = 361452$
    - (d) $\sigma = 32156487$
75. Write the following (given in cycle notation) in **two-line notation**; compute $\sigma^{-1}$ and $\sigma^2$:
    - (a) $\sigma = (1,3,5)(2,4,6)$
    - (b) $\sigma = (2,3)(1,7)(5)(6,2)$
    - (c) $\sigma = (7,5,3,1)(2,4,6)$
    - (d) $\sigma = (2,7)(6,5,1)(4,3)$
76. List all **permutations without fixed points** on $[4]$ and $[6]$.
77. List all **permutations with exactly 2 cycles** of $[4]$ and of $[6]$.

---

### 1.13 Derangements

78. List all **derangements** of $[3]$ and $[4]$. Prove that $D_n = (n-1)(D_{n-1} + D_{n-2})$.
79. **8 men** give their hats to a hat-check person. In how many ways can hats be returned so that **no man receives his own hat**?

---

### 1.14 Pigeonhole Principle

85. A drawer has 60 socks: 10 red pairs, 10 blue pairs, 10 green pairs, all mixed in the dark. What is the **minimum number** of socks to remove to guarantee at least one matching pair?
86. Prove that if **5 points** are placed on or in a **square of side 1**, at least two points are no farther apart than $\dfrac{\sqrt{2}}{2}$.
87. Prove that if **5 points** are placed on or in an **equilateral triangle of side 1**, at least two points are no farther apart than $\dfrac{1}{2}$.
88. Show that among any $n+1$ positive integers not exceeding $2n$, there must be an integer that **divides** one of the others.
89. Show that if **7 integers** are selected from the first 10 positive integers, there must be **at least two pairs** with sum 11. Is the conclusion true if only 6 are selected?
90. Show that if you pick **7 numbers** from the consecutive integers 2 to 13, you can always find two whose sum is **exactly 15**.
91. There are **12 chairs** in a row and **9 people** sitting. Prove there are **3 consecutive chairs** occupied.
92. Prove that every sequence of $n^2 + 1$ distinct real numbers contains a subsequence of length $n+1$ that is either **strictly increasing** or **strictly decreasing**.

---

---

## Section 2: Advanced Counting Rules

### 2.1 Generating Functions — Finding GFs

1. Find generating functions for the following sequences:
   - (a) Consecutive non-negative integers $(0,1, 2, 3, \ldots, n, \ldots)$
   - (b) The number of $k$-combinations with repetition of $[n]$, for a fixed $n$, and $k = 0, 1, 2, \ldots$
   - (c) Perfect square numbers $(1, 4, 9, 16, \ldots)$
   - (d) Fibonacci numbers $(0, 1, 1, 2, 3, 5, \ldots)$
   - (e) Catalan numbers $(1, 1, 2, 5, 14, 42, \ldots)$
   - (f) Number of ways to fill a bag with $n$ fruits such that:
     - i. The number of apples is **even**
     - ii. The number of bananas is a **multiple of 5**
     - iii. There are **at most 4** oranges
     - iv. There is **at most 1** pear

2. Let $A(x) = a_0 + a_1 x + a_2 x^2 + \cdots$ be the GF for $(a_0, a_1, a_2, \ldots)$. Express in terms of $A(x)$ the generating functions for:
   - (a) $(a_0,\ a_0 + a_1,\ a_1 + a_2,\ a_2 + a_3, \ldots)$
   - (b) $(a_1, a_2, a_3, \ldots)$
   - (c) $(a_0 + a_1,\ a_1 + a_2,\ a_2 + a_3, \ldots)$
   - (d) $(a_0,\ 2a_1,\ 4a_2,\ 8a_3, \ldots)$
   - (e) $(a_0,\ a_0 + a_1,\ a_0 + a_1 + a_2, \ldots)$
   - (f) $(a_0,\ a_1 b,\ a_2 b^2,\ a_3 b^3, \ldots)$, where $b$ is a constant
   - (g) $(a_0,\ 0,\ a_2,\ 0,\ a_4,\ 0, \ldots)$
   - (h) $(a_0, a_2, a_4, \ldots)$

3. Find the generating function for the number of ways to pay $n$ dollars ($n = 0, 1, \ldots$) using coins of denominations **3, 5, 7 dollars**.

4. Find the generating function for $b_n$, the number of ways that $n$ identical candies can be distributed among **4 children and 1 adult** such that each child receives an **odd** number and the adult receives **1 or 2** candies.

5. In a game, you can score **1, 2, or 4 points** per turn. Find the GF for the number of ways to score $n$ points if:
   - (a) There are **at least two turns** where 4 points are scored
   - (b) The number of turns scoring 2 points is a **multiple of 3**

1. What is the generating function for $\{a_k\}$ where $a_k$ is the number of solutions to $x_1 + x_2 + x_3 + x_4 = k$, with $x_1 \geq 3$, $1 \leq x_2 \leq 5$, $0 \leq x_3 \leq 4$, $x_4 \geq 1$. Use the GF to find $a_7$.b
2. Using the generating function for the Fibonacci numbers, prove:
   - (a) $f_0 + f_1 + \cdots + f_n = f_{n+2} - 1$
   - (b) $f_0 + f_2 + \cdots + f_{2n} = f_{2n+1} - 1$
   - (c) $f_1 + f_3 + \cdots + f_{2n-1} = f_{2n}$

8. Find a **closed formula** for the number of $k$-combinations with repetition of $n$ elements by using the Maclaurin decomposition of its generating function.

9. The number of partitions of $[n]$ into 2 parts satisfies: $S(0,2) = S(1,2) = 0$ and for $n \geq 2$, $S(n,2) = 1 + 2S(n-1,2)$. Find the GF and a **closed formula** for $S(n,2)$.

---

### 2.2 Linear Recurrence Relations

10. Use the **generating function method** to solve the following recurrences:
    - (a) $a_0 = 2,\quad a_n = 3a_{n-1}$
    - (b) $a_0 = 2,\quad a_n = 3a_{n-1} + 1$
    - (c) $a_0 = 1,\ a_1 = 2,\quad a_n = 5a_{n-1} - 4a_{n-2}$
    - (d) $u_0 = 2,\ u_1 = -6,\quad u_{n+2} + 8u_{n+1} - 9u_n = 8 \cdot 3^{n+1}$
    - (e) $u_0 = 1,\quad u_{n+1} - 2u_n = 4^n$
    - (f) Let $q_n$ be the number of words of length $n$ over $\{a,b,c,d\}$ that contain an **odd number of b's**. Show that $q_{n+1} = 4^n + 2q_n$ and solve the recurrence.

11. For each generating function, provide a **closed formula** for the sequence it determines:
    - (a) $(3x - 4)^3$
    - (b) $\dfrac{x^3}{1 - 3x}$
    - (c) $\dfrac{x^3 + x}{1 - 3x}$
    - (d) $\dfrac{x^2}{(1-x)^2}$
    - (e) $\dfrac{x^2 - x}{(1-x)^2}$
    - (f) $\dfrac{x^2}{(1-x)^3}$

---

### 2.3 GF Applications — Combinatorial Problems

12. Use generating functions to find the number of ways to give **10 identical balloons** to **4 children** if each child receives **at least 2** balloons.

13. Use generating functions to find the number of ways to put **15 identical objects** into **6 distinct boxes** such that each box contains **at least 1 but no more than 3** objects.

---

### 2.4 Inclusion-Exclusion Principle (PIE)

14. How many words are formed from all letters of **MISSISSIPPI** that:
    - (a) Do **not** contain four consecutive letters S
    - (b) Do **not** contain four consecutive S's **nor** two consecutive P's

15. Use PIE to find the number of positive integers not exceeding **100** that are **not** divisible by 5 or by 7.

16. Use PIE to find the number of positive integers not exceeding **100** that are either **odd** or a **perfect square**.

17. Find the number of positive integers not exceeding **1000** that are either a **perfect square** or a **perfect cube**.

18. How many elements are in the union of **four sets** if: each set has 100 elements, each pair shares 50, each triple shares 25, and all four share 5 elements?

19. In a survey of **270 college students**: 64 like Brussels sprout, 94 like broccoli, 58 like cauliflower, 26 like both Brussels sprout & broccoli, 28 like both Brussels sprout & cauliflower, 22 like both cauliflower & broccoli, and 14 like all three. How many like **none** of these vegetables?

20. How many terms are in the PIE formula for $|A_1 \cup A_2 \cup A_3 \cup A_4 \cup A_5|$?

21. How many permutations of the **26 letters** of the English alphabet do **not** contain any of the strings `fish`, `rat`, or `bird`?

22. How many non-negative integer solutions does $x + y + z = 13$ have, where $0 \leq x, y, z \leq 6$?

23. How many non-negative integer solutions does $x + y + z + t = 18$ have, where $0 \leq x \leq 4$ and $0 \leq y \leq 7$?

24. How many **surjective (onto) functions** are there from a set with **7 elements** to a set with **5 elements**?

25. How many ways to distribute **6 different toys** to **3 different children** such that each child gets **at least one** toy?

26. In how many ways can **8 distinct balls** be distributed into **3 distinct urns** if each urn must contain **at least one** ball?

27. How many **derangements** of $[4]$ are there? List them all.

28. A group of **8 students** is assigned seats for **two classes** in the same classroom. How many ways can seats be assigned if **no student gets the same seat** for both classes?

29. How many non-negative integers not exceeding **100** are **relatively prime** with 100?
