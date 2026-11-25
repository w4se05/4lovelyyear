# Sect.1 Basic Counting Rules — Full Solutions — Full Solutions

---

**1.** How many subsets of a set with $n$ elements have exactly two elements?

**Solution.**
Step 1. A subset of size $2$ from an $n$-element set is a $2$-combination. By the definition of combinations, the number is $C(n,2)$.
Step 2. Explicitly, $C(n,2)=\frac{n(n-1)}{2}$.

$$\boxed{C(n,2)=\dfrac{n(n-1)}{2}}$$

---

**2.** How many subsets of a set with 100 elements have at most two elements?

**Solution.**
Step 1. "At most two elements" means $0$, $1$, or $2$ elements. By the Sum Rule (disjoint cases):
$$C(100,0)+C(100,1)+C(100,2)$$
Step 2. Compute each:
$$C(100,0)=1,\quad C(100,1)=100,\quad C(100,2)=\frac{100\cdot 99}{2}=4950$$
Step 3. Sum:
$$1+100+4950=5051$$

$$\boxed{5051}$$

---

**3.** How many subsets of a set with 100 elements have more than two elements?

**Solution.**
Step 1. By the Complement Rule: (all subsets) $-$ (subsets with at most two elements).
Step 2. All subsets of a 100-element set: $2^{100}$.
Step 3. Subtract the result of Problem 2:
$$2^{100}-5051$$

$$\boxed{2^{100}-5051}$$

---

**4.** How many subsets of a set with $n$ elements are there?

**Solution.**
Each of the $n$ elements may independently be in the subset or not (2 choices per element). By the Product Rule:
$$2^n$$

$$\boxed{2^n}$$

---

**5.** How many strings of five ASCII characters contain the character @ at least once?

**Solution.**
Step 1. Total 5-character strings over 128 ASCII symbols: $128^5$ (Product Rule; 5 slots, 128 choices each).
Step 2. Strings with **no** @: $127^5$ (127 choices per slot, excluding @).
Step 3. By the Complement Rule:
$$128^5-127^5$$
Step 4. Compute: $128^5=34359738368$, $127^5=33038369407$, difference $=1321368961$.

$$\boxed{128^5-127^5=1321368961}$$

---

**6.** How many bit strings of length $5$ contain
a. exactly two occurrences of 0s;
b. at most two occurrences of 0s;
c. at least two occurrences of 0s.

**Solution.**
**(a)** Choose which 2 of the 5 positions are 0 (the remaining 3 are 1). By combinations:
$$C(5,2)=\frac{5\cdot 4}{2}=10$$

**(b)** "At most two 0s" = 0, 1, or 2 zeros. By the Sum Rule:
$$C(5,0)+C(5,1)+C(5,2)=1+5+10=16$$

**(c)** "At least two 0s" = complement of "at most one 0":
$$2^5-[C(5,0)+C(5,1)]=32-(1+5)=26$$
Alternatively, by sum: $C(5,2)+C(5,3)+C(5,4)+C(5,5)=10+10+5+1=26$.

$$\boxed{\text{(a) }10\quad\text{(b) }16\quad\text{(c) }26}$$

---

**7.** Prove that Euler's phi function $\varphi(p^k)=p^k-p^{k-1}$ where $p$ is prime and $k$ is a positive integer.

**Solution.**
Step 1. $\varphi(p^k)$ counts integers $a$ with $1\le a\le p^k$ such that $\gcd(a,p^k)=1$.
Step 2. Since $p$ is prime, $\gcd(a,p^k)\neq1$ iff $p\mid a$, i.e., $a$ is a multiple of $p$.
Step 3. Multiples of $p$ up to $p^k$: $p,2p,3p,\dots,p^k$. There are $p^{k-1}$ such numbers (one for each coefficient $1$ through $p^{k-1}$).
Step 4. By the Complement Rule:
$$\varphi(p^k)=p^k-p^{k-1}$$

$$\boxed{\varphi(p^k)=p^k-p^{k-1}}$$

---

**8.** The chairs of an auditorium are to be labeled with an uppercase English letter followed by a positive integer not exceeding 100. What is the largest number of chairs?

**Solution.**
Step 1. Two independent choices: letter (26 choices) and integer (100 choices).
Step 2. By the Product Rule: $26\times 100=2600$.

$$\boxed{2600}$$

---

**9.** How many different license plates with three uppercase English letters followed by three digits?

**Solution.**
Three letter slots (26 choices each) then three digit slots (10 choices each). By the Product Rule:
$$26^3\cdot10^3=17576\times 1000=17576000$$

$$\boxed{26^3\cdot10^3=17576000}$$

---

**10.** A password is between 4 and 8 characters long, composed of lower and/or upper case letters. How many passwords are possible?

**Solution.**
Step 1. Each character has $26+26=52$ choices (lower or upper case).
Step 2. Passwords of lengths $4,5,6,7,8$ are disjoint cases. By the Sum Rule:
$$52^4+52^5+52^6+52^7+52^8$$

$$\boxed{\sum_{i=4}^{8}52^i}$$

---

**11.** In how many ways may a ten person club select a president and a two person executive advisory board from among its members (assume the president is not on the advisory board)?

**Solution.**
Step 1. Choose president: $10$ choices.
Step 2. From the remaining 9 members, choose an unordered 2-person board: $C(9,2)$ choices.
Step 3. By the Product Rule:
$$10\times C(9,2)=10\times 36=360$$

$$\boxed{360}$$

---

**12.** What is the number of five digit numbers? What is the number of five digit numbers that have no two consecutive digits equal? What is the number that have at least one pair of consecutive digits equal?

**Solution.**
**(a) All five-digit numbers:** First digit $1$-$9$ (9 choices), remaining four digits $0$-$9$ (10 choices each). Product Rule:
$$9\cdot10^4=90000$$

**(b) No two consecutive equal:** First digit $1$-$9$ (9 choices). Each subsequent digit cannot equal the previous digit, so 9 choices per remaining slot:
$$9\cdot9^4=9^5=59049$$

**(c) At least one pair of consecutive equal:** Complement of (b):
$$9\cdot10^4-9^5=90000-59049=30951$$

$$\boxed{\text{(a) }90000\quad\text{(b) }59049\quad\text{(c) }30951}$$

---

**13.** List all functions from $[3]$ to $[2]$.

**Solution.**
A function $f:[3]\to[2]$ is determined by the triple $(f(1),f(2),f(3))$ with each $f(i)\in\{1,2\}$. Total: $2^3=8$. Listed as triples:
$$(1,1,1),\;(1,1,2),\;(1,2,1),\;(2,1,1),\;(1,2,2),\;(2,1,2),\;(2,2,1),\;(2,2,2)$$

$$\boxed{\begin{array}{l}(1,1,1),\;(1,1,2),\;(1,2,1),\;(2,1,1),\\(1,2,2),\;(2,1,2),\;(2,2,1),\;(2,2,2)\end{array}}$$

---

**14.** List all one-to-one functions from $[2]$ to $[3]$.

**Solution.**
An injection $f:[2]\to[3]$: $f(1)\neq f(2)$, each in $\{1,2,3\}$. Total: $P(3,2)=3\cdot2=6$. Listed as ordered pairs $(f(1),f(2))$:
$$(1,2),\;(1,3),\;(2,1),\;(2,3),\;(3,1),\;(3,2)$$

$$\boxed{(1,2),\,(1,3),\,(2,1),\,(2,3),\,(3,1),\,(3,2)}$$

---

**15.** List all bijections from $[3]$ to $[3]$.

**Solution.**
Bijections from $[3]$ to $[3]$ are the $3!=6$ permutations of $\{1,2,3\}$. In one-line notation $(\sigma(1),\sigma(2),\sigma(3))$:
$$(1,2,3),\;(1,3,2),\;(2,1,3),\;(2,3,1),\;(3,1,2),\;(3,2,1)$$

$$\boxed{\begin{array}{l}(1,2,3),\;(1,3,2),\;(2,1,3),\\(2,3,1),\;(3,1,2),\;(3,2,1)\end{array}}$$

---

**16.** How many functions from $[m]$ to $[n]$ are there?

**Solution.**
Each of the $m$ domain elements independently maps to one of $n$ values. By the Product Rule:
$$\boxed{n^m}$$

---

**17.** List all one-to-one functions from $[2]$ to $[4]$.

**Solution.**
$P(4,2)=4\cdot3=12$ injections. Listed as ordered pairs $(f(1),f(2))$:
$$(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)$$

$$\boxed{\begin{array}{l}(1,2),\;(1,3),\;(1,4),\;(2,1),\;(2,3),\;(2,4),\\(3,1),\;(3,2),\;(3,4),\;(4,1),\;(4,2),\;(4,3)\end{array}}$$

---

**18.** How many one-to-one functions from $[3]$ to $[5]$ are there?

**Solution.**
Choose ordered images for the 3 domain elements from the 5 codomain elements. By the Product Rule: $P(5,3)=5\cdot4\cdot3=60$.

$$\boxed{P(5,3)=60}$$

---

**19.** How many one-to-one functions from $[m]$ to $[n]$ are there?

**Solution.**
If $m>n$, no injection exists: $0$. If $m\le n$, $P(n,m)=\frac{n!}{(n-m)!}$ (select $m$ from $n$ in order).

$$\boxed{P(n,m)=\dfrac{n!}{(n-m)!}\;(\text{or }0\text{ if }m>n)}$$

---

**20.** In how many ways can you draw a first card, second, and third card from a deck of 52 cards?

**Solution.**
Drawing sequentially without replacement: 52 choices for first, 51 for second, 50 for third. By the Product Rule:
$$52\cdot51\cdot50=132600$$

$$\boxed{52\cdot51\cdot50=132600}$$

---

**21.** In how many ways can you draw two cards from a deck of 52 cards (order does not matter)?

**Solution.**
An unordered 2-card hand from 52: $C(52,2)=\frac{52\cdot51}{2}=1326$.

$$\boxed{C(52,2)=1326}$$

---

**22.** Given $n$ different objects put in a secret box. Take $k$ objects out.
a. How many ways if the order of taking matters?
b. How many ways if the order does not matter?

**Solution.**
**(a)** Order matters = $k$-permutations of $n$: $P(n,k)=\frac{n!}{(n-k)!}$.
**(b)** Order does not matter = $k$-combinations of $n$: $C(n,k)=\frac{n!}{k!(n-k)!}$.

$$\boxed{\text{(a) }P(n,k)=\dfrac{n!}{(n-k)!}\qquad\text{(b) }C(n,k)}$$

---

**23.** In how many ways can we pass out $k$ distinct pieces of fruit to $n$ children with no restriction?

**Solution.**
Each piece of fruit independently goes to one of $n$ children. By the Product Rule: $n^k$.

$$\boxed{n^k}$$

---

**24.** In how many ways can we pass out $k$ distinct pieces of fruit to $n$ children if each child may get at most one? What if $k>n$?

**Solution.**
Step 1. If $k\le n$: assign $k$ distinct fruit to $k$ distinct children. This is a $k$-permutation: $P(n,k)=\frac{n!}{(n-k)!}$.
Step 2. If $k>n$: impossible, answer $0$.

$$\boxed{P(n,k)=\dfrac{n!}{(n-k)!}\;(k\le n);\quad 0\;(k>n)}$$

---

**25.** In how many ways can we pass out $k$ **identical** pieces of fruit to $n$ children if each child may get at most one? What if $k>n$?

**Solution.**
Since fruit are identical, choosing which $k$ children receive one fruit determines the distribution: $C(n,k)$. If $k>n$, answer $0$.

$$\boxed{C(n,k)\;(k\le n);\quad 0\;(k>n)}$$

---

**26.** How many bit strings of length $n$ have exactly $k$ occurrences of 0s?

**Solution.**
Choose which $k$ of the $n$ positions are 0 (the remaining $n-k$ are 1): $C(n,k)$.

$$\boxed{C(n,k)}$$

---

**27.** A tennis club has $2n$ members. We want to pair up the members by twos for single matches. In how many ways may we pair up all the members? If in addition for each pairing we say who serves first, now in how many ways?

**Solution.**
**(a) Pairing only (unordered matches, unordered within each match):**
Step 1. Line up all $2n$ members: $(2n)!$ ways.
Step 2. Each pairing is overcounted: within each of the $n$ pairs the two members can be swapped ($2$ ways per pair): divide by $2^n$. The $n$ pairs themselves can be reordered: divide by $n!$. By the Division Rule:
$$\frac{(2n)!}{2^n\,n!}$$

**(b) With serving order (who serves first in each match):**
For each of the $n$ pairs, there are 2 choices for who serves first. Multiply by $2^n$:
$$\frac{(2n)!}{2^n\,n!}\times 2^n=\frac{(2n)!}{n!}$$

$$\boxed{\text{(a) }\dfrac{(2n)!}{2^n\,n!}\qquad\text{(b) }\dfrac{(2n)!}{n!}}$$

---

**28.** How many numbers of 3 digits whose digits are pairwise different and decrease from left to right?

**Solution.**
Step 1. Choose any 3 distinct digits from $\{0,1,\dots,9\}$. There is exactly one way to arrange them in decreasing order.
Step 2. Number of choices: $C(10,3)=\frac{10\cdot9\cdot8}{6}=120$.
Step 3. Even if 0 is among the chosen digits, it becomes the units digit (smallest), keeping a valid 3-digit number.

$$\boxed{C(10,3)=120}$$

---

**29.** Give a bijection that proves that $\binom{n}{k}=\binom{n}{n-k}$.

**Solution.**
**(Bijection)**
Define $f:\{A\subseteq[n]:|A|=k\}\to\{B\subseteq[n]:|B|=n-k\}$ by $f(A)=[n]\setminus A$ (the complement).

- **Domain:** all $k$-subsets of $[n]$.
- **Codomain:** all $(n-k)$-subsets of $[n]$.
- **Well-defined:** $|[n]\setminus A|=n-|A|=n-k$, so $f(A)$ is indeed an $(n-k)$-subset.
- **Injectivity:** If $f(A_1)=f(A_2)$, then $[n]\setminus A_1=[n]\setminus A_2$, so $A_1=A_2$.
- **Surjectivity:** For any $(n-k)$-subset $B$, let $A=[n]\setminus B$. Then $|A|=k$ and $f(A)=B$.

Thus $f$ is a bijection. Since a bijection exists between the two collections, they have the same size. Hence $C(n,k)=C(n,n-k)$.

$$\boxed{\text{Bijection }f(A)=[n]\setminus A}$$


---

**30.** Give two proofs (algebraic and combinatorial) for each identity.

**30a.** $\displaystyle\binom{2n}{2}=2\binom{n}{2}+n^2$

**Solution.**
**(Algebraic)**
$$C(2n,2)=\frac{2n(2n-1)}{2}=n(2n-1)=2n^2-n$$
$$2C(n,2)+n^2=2\cdot\frac{n(n-1)}{2}+n^2=n(n-1)+n^2=n^2-n+n^2=2n^2-n$$
Both equal $2n^2-n$.

**(Combinatorial proof)**
Choose a 2-element subset from a set of $2n$ elements partitioned into two groups of $n$ each (say "left" and "right"). Three disjoint cases:
- Both from left group: $C(n,2)$ ways.
- Both from right group: $C(n,2)$ ways.
- One from each group: $n\cdot n=n^2$ ways.
By the Sum Rule: $C(n,2)+C(n,2)+n^2=2C(n,2)+n^2$.

$$\boxed{\text{Both proofs verified}}$$

---

**30b.** $\displaystyle\sum_{k=1}^{n}k\binom{n}{k}=n2^{\,n-1}$

**Solution.**
**(Algebraic)**
Use $k\binom{n}{k}=n\binom{n-1}{k-1}$:
$$\sum_{k=1}^{n}k\binom{n}{k}=n\sum_{k=1}^{n}\binom{n-1}{k-1}=n\sum_{j=0}^{n-1}\binom{n-1}{j}=n\cdot2^{\,n-1}$$

**(Combinatorial proof)**
Count the number of ways to choose a committee (any size $k\ge 1$) from $n$ people and designate a chair:
- Left side: sum over possible committee sizes $k$: choose $k$ members ($\binom{n}{k}$), then choose chair from those $k$ ($k$ choices).
- Right side: first choose the chair ($n$ choices), then any subset of the remaining $n-1$ people may join ($2^{n-1}$ choices).
Both count the same set, so they are equal.

$$\boxed{n2^{n-1}}$$

---

**30c.** $\displaystyle n\binom{n-1}{2}=\binom{n}{2}(n-2)$

**Solution.**
**(Algebraic)**
LHS: $n\cdot\frac{(n-1)(n-2)}{2}=\frac{n(n-1)(n-2)}{2}$.
RHS: $\frac{n(n-1)}{2}\cdot(n-2)=\frac{n(n-1)(n-2)}{2}$. Equal.

**(Combinatorial proof)**
Count ways to pick a 2-person committee from $n$ people plus a witness from the remaining $n-2$.
- Left side: choose the chair of a 3-person committee ($n$ choices), then choose 2 other members from remaining $n-1$: $n\binom{n-1}{2}$.
- Right side: choose the 2-person committee ($\binom{n}{2}$ ways), then choose a witness from the $n-2$ others: $(n-2)\binom{n}{2}$.
Both count the same (a 3-person set with one distinguished member).

$$\boxed{\dfrac{n(n-1)(n-2)}{2}}$$

---

**30d.** Pascal's identity: $\displaystyle\binom{n}{k}=\binom{n-1}{k}+\binom{n-1}{k-1}$

**Solution.**
**(Algebraic)**
$$\binom{n-1}{k}+\binom{n-1}{k-1}=\frac{(n-1)!}{k!(n-1-k)!}+\frac{(n-1)!}{(k-1)!(n-k)!}$$
$$=\frac{(n-1)!}{(k-1)!(n-1-k)!}\left[\frac{1}{k}+\frac{1}{n-k}\right]=\frac{(n-1)!}{(k-1)!(n-1-k)!}\cdot\frac{n}{k(n-k)}=\frac{n!}{k!(n-k)!}=\binom{n}{k}$$

**(Combinatorial proof)**
Count $k$-subsets of $[n]$. Fix element $n$. Every $k$-subset either:
- Does **not** contain $n$: choose $k$ from $[n-1]$: $\binom{n-1}{k}$ ways.
- **Contains** $n$: choose $k-1$ from $[n-1]$: $\binom{n-1}{k-1}$ ways.
By the Sum Rule, $\binom{n}{k}=\binom{n-1}{k}+\binom{n-1}{k-1}$.

$$\boxed{\text{Pascal's identity verified}}$$

---

**30e.** $\displaystyle\binom{n}{k}\binom{k}{j}=\binom{n}{j}\binom{n-j}{k-j}$

**Solution.**
**(Algebraic)**
LHS: $\frac{n!}{k!(n-k)!}\cdot\frac{k!}{j!(k-j)!}=\frac{n!}{j!(k-j)!(n-k)!}$.
RHS: $\frac{n!}{j!(n-j)!}\cdot\frac{(n-j)!}{(k-j)!(n-k)!}=\frac{n!}{j!(k-j)!(n-k)!}$. Equal.

**(Combinatorial proof)**
Count ways to pick a $k$-subset $A$ of $[n]$ and then a $j$-subset $B$ of $A$.
- Left side: choose $A$ ($\binom{n}{k}$), then choose $B\subseteq A$ ($\binom{k}{j}$).
- Right side: choose $B$ ($\binom{n}{j}$) first, then choose $A\setminus B$ (size $k-j$) from the remaining $n-j$ elements: $\binom{n-j}{k-j}$.
Both produce an ordered pair $(A,B)$ with $|B|=j$, $|A|=k$, $B\subseteq A\subseteq[n]$. Equal.

$$\boxed{\text{Identity verified}}$$

---

**30f.** $\displaystyle\binom{n}{k}\binom{n-k}{j}=\binom{n}{j}\binom{n-j}{k}$

**Solution.**
**(Algebraic)**
LHS: $\frac{n!}{k!(n-k)!}\cdot\frac{(n-k)!}{j!(n-k-j)!}=\frac{n!}{k!j!(n-k-j)!}$.
RHS: $\frac{n!}{j!(n-j)!}\cdot\frac{(n-j)!}{k!(n-k-j)!}=\frac{n!}{k!j!(n-k-j)!}$. Equal.

**(Combinatorial proof)**
Count ways to partition $[n]$ into three labeled blocks of sizes $j$, $k$, $n-j-k$.
- Left: choose block of size $k$ ($\binom{n}{k}$), then choose block of size $j$ from the remaining ($\binom{n-k}{j}$).
- Right: choose block of size $j$ first ($\binom{n}{j}$), then choose block of size $k$ from the remaining ($\binom{n-j}{k}$).
Both count the same.

$$\boxed{\text{Identity verified}}$$

---

**30g.** Vandermonde's identity: $\displaystyle\binom{m+n}{r}=\sum_{i=0}^{r}\binom{m}{i}\binom{n}{r-i}$

**Solution.**
**(Algebraic)**
Coefficient of $x^r$ in $(1+x)^{m+n}=(1+x)^m(1+x)^n$:
$$(1+x)^{m+n}=\sum_{r=0}^{m+n}\binom{m+n}{r}x^r$$
$$(1+x)^m(1+x)^n=\left(\sum_{i=0}^{m}\binom{m}{i}x^i\right)\left(\sum_{j=0}^{n}\binom{n}{j}x^j\right)$$
The coefficient of $x^r$ in the product is $\sum_{i=0}^{r}\binom{m}{i}\binom{n}{r-i}$. Equating coefficients gives the identity.

**(Combinatorial proof)**
Count $r$-subsets from $m+n$ elements where $m$ are "type A" (say women) and $n$ are "type B" (men).
- Left: choose any $r$ from all $m+n$: $\binom{m+n}{r}$.
- Right: sum over the number $i$ of type-A elements chosen. Choose $i$ from $m$ of type A ($\binom{m}{i}$) and $r-i$ from $n$ of type B ($\binom{n}{r-i}$).
By the Sum Rule, these are equal.

$$\boxed{\text{Vandermonde's identity verified}}$$

---

**31.** How many permutations of the characters ABC12DE contain the string BC1?

**Solution.**
Treat "BC1" as a single block. The objects to permute are: $\{\text{A},\;\text{BC1},\;2,\;\text{D},\;\text{E}\}$ — 5 distinct objects. Permutations of 5 distinct objects: $5!=120$.

$$\boxed{5!=120}$$

---

**32.** A group contains $n$ men and $n$ women. How many ways are there to arrange these people in a row if the men and women alternate?

**Solution.**
Two disjoint cases based on which gender sits first.
Case 1 (MWMW...MW): arrange $n$ men in $n$ positions: $n!$; arrange $n$ women in the other $n$ positions: $n!$. Product: $(n!)^2$.
Case 2 (WMWM...WM): same product $(n!)^2$.
By the Sum Rule: total $=2(n!)^2$.

$$\boxed{2(n!)^2}$$

---

**33.** A class has 25 students. How many choices are there to pick 3 students to participate in a Calculus competition? How many choices to pick 3 students, one for Calculus, one for Algebra, one for Discrete Math?

**Solution.**
**(a) One competition (unordered 3-person team):**
Choose 3 from 25 without order: $C(25,3)=\frac{25\cdot24\cdot23}{6}=2300$.

**(b) Three distinct competitions (ordered):**
Choose 3 students and assign them to 3 distinct roles: $P(25,3)=25\cdot24\cdot23=13800$. Equivalently, $3!\cdot C(25,3)=6\cdot2300=13800$.

$$\boxed{\text{(a) }C(25,3)=2300\qquad\text{(b) }P(25,3)=13800}$$

---

**34.** A class has 9 female and 20 male students. How many ways to pick 11 students for a soccer team if
a. the team must have exactly 3 female students?
b. the team must have at least one female student?

**Solution.**
**(a)** Choose 3 females from 9: $C(9,3)$. Choose 8 males from 20: $C(20,8)$. By the Product Rule:
$$C(9,3)\cdot C(20,8)=84\cdot125970=10581480$$

**(b) At least one female.** Complement: all-male team $C(20,11)$. Total 11-student teams: $C(29,11)$.
$$C(29,11)-C(20,11)=10015005-167960=9847045$$

$$\boxed{\text{(a) }C(9,3)\cdot C(20,8)=10581480\qquad\text{(b) }C(29,11)-C(20,11)=9847045}$$

---

**35.** Count the number of bit strings of length 7 that either start with a 0 or end with the two bits 10.

**Solution.**
Let $A=\{\text{strings starting with }0\}$, $B=\{\text{strings ending with }10\}$.
$|A|=2^6=64$ (first bit fixed to 0, remaining 6 bits free).
$|B|=2^5=32$ (last two fixed to 10, remaining 5 bits free).
$|A\cap B|$: start with 0 AND end with 10. Bits 2-5 are free: $2^4=16$.
By Inclusion-Exclusion: $|A\cup B|=64+32-16=80$.

$$\boxed{80}$$

---

**36.** The row of Pascal's triangle with $n=10$ is: $1\;10\;45\;120\;210\;252\;210\;120\;45\;10\;1$. Use Pascal's formula to produce the two rows immediately following.

**Solution.**
**Row 11 ($n=11$):** each entry $C(11,k)=C(10,k)+C(10,k-1)$ (with $C(10,-1)=C(10,11)=0$).
$$1,\;1+10=11,\;10+45=55,\;45+120=165,\;120+210=330,\;210+252=462,$$
$$252+210=462,\;210+120=330,\;120+45=165,\;45+10=55,\;10+1=11,\;1$$

Row 11: $1\;11\;55\;165\;330\;462\;462\;330\;165\;55\;11\;1$.

**Row 12 ($n=12$):** similarly from Row 11.
$$1,\;1+11=12,\;11+55=66,\;55+165=220,\;165+330=495,\;330+462=792,\;462+462=924,$$
$$462+330=792,\;330+165=495,\;165+55=220,\;55+11=66,\;11+1=12,\;1$$

Row 12: $1\;12\;66\;220\;495\;792\;924\;792\;495\;220\;66\;12\;1$.

$$\boxed{\begin{aligned}\text{Row 11: }&1\;11\;55\;165\;330\;462\;462\;330\;165\;55\;11\;1\\\text{Row 12: }&1\;12\;66\;220\;495\;792\;924\;792\;495\;220\;66\;12\;1\end{aligned}}$$

---

**37.** Find the coefficient of $x^{101}y^{99}$ in the expansion of $(2x-3y)^{200}$.

**Solution.**
General term: $\binom{200}{k}(2x)^k(-3y)^{200-k}=\binom{200}{k}2^k(-3)^{200-k}x^ky^{200-k}$.
We need $k=101$ (so $200-k=99$). Coefficient is:
$$\binom{200}{101}\,2^{101}\,(-3)^{99}$$

$$\boxed{\binom{200}{101}\,2^{101}\,(-3)^{99}}$$

---

**38.** Give the formula for the coefficient of $x^k$ in the expansion of $\left(x+\frac{1}{x}\right)^{100}$, where $k$ is an integer.

**Solution.**
General term: $\binom{100}{j}x^j\left(\frac{1}{x}\right)^{100-j}=\binom{100}{j}x^{2j-100}$.
Set $2j-100=k\;\Rightarrow\;j=\frac{k+100}{2}$.
Requires $0\le j\le 100$ and $j$ integer $\Rightarrow$ $k$ must be even and $-100\le k\le 100$.
$$\text{Coefficient}=\begin{cases}\displaystyle\binom{100}{\frac{k+100}{2}},&\text{if }k\text{ is even and }|k|\le 100\\[10pt]0,&\text{otherwise}\end{cases}$$

$$\boxed{\displaystyle\binom{100}{\frac{k+100}{2}}\;\text{(if }k\text{ even, }|k|\le 100\text{)},\;0\;\text{otherwise}}$$

---

**39.** Find the coefficient of $x^{101}y^{99}z^{105}$ in the expansion of $(2x-3y-z)^{305}$.

**Solution.**
Verify exponents sum to $305$: $101+99+105=305$. Multinomial coefficient: $\frac{305!}{101!\,99!\,105!}$.
Coefficient contributions: $(2x)^{101}(-3y)^{99}(-z)^{105}=2^{101}(-3)^{99}(-1)^{105}$.
Multiply:
$$\frac{305!}{101!\,99!\,105!}\cdot2^{101}\cdot(-3)^{99}\cdot(-1)^{105}$$

$$\boxed{\dfrac{305!}{101!\,99!\,105!}\cdot2^{101}\cdot(-3)^{99}\cdot(-1)^{105}}$$

---

**40.** If you have ten distinct chairs to paint, in how many ways could you paint three of them green, three blue, and four red?

**Solution.**
Distribute 10 distinct chairs into 3 labeled color categories with sizes 3, 3, 4. By the multinomial coefficient:
$$\frac{10!}{3!\,3!\,4!}=\frac{3628800}{6\cdot6\cdot24}=\frac{3628800}{864}=4200$$

$$\boxed{\dfrac{10!}{3!\,3!\,4!}=4200}$$

---

**41.** (Lattice problem) In a Cartesian coordinate system, how many paths are there from the origin to $(m,n)$ if the paths use exactly $m+n$ horizontal and vertical line segments each of length one?

**Solution.**
A path from $(0,0)$ to $(m,n)$ consists of $m$ right steps (East) and $n$ up steps (North), total $m+n$ steps. The path is determined by choosing which $m$ of the $m+n$ steps are East steps:
$$C(m+n,m)=C(m+n,n)$$

$$\boxed{C(m+n,m)}$$

---

**42.** True or False, give the reason: $\displaystyle\binom{n}{k}=\binom{n-2}{k-2}+\binom{n-2}{k-1}+\binom{n-2}{k}$.

**Solution.**
The correct two-step expansion of Pascal's identity gives:
$$\binom{n}{k}=\binom{n-1}{k}+\binom{n-1}{k-1}=\left[\binom{n-2}{k}+\binom{n-2}{k-1}\right]+\left[\binom{n-2}{k-1}+\binom{n-2}{k-2}\right]$$
$$=\binom{n-2}{k}+2\binom{n-2}{k-1}+\binom{n-2}{k-2}$$
The stated identity has coefficient $1$ on $\binom{n-2}{k-1}$ instead of the correct $2$.
Counterexample: $n=4,k=2$. LHS: $\binom{4}{2}=6$. RHS: $\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4$. $6\neq4$.

$$\boxed{\text{False. Counterexample: }n=4,k=2,\;\text{LHS}=6,\;\text{RHS}=4}$$

---

**43.** How many different strings can be made from the letters in CASABLANCA, using all letters?

**Solution.**
Count letters: C(2), A(4), S(1), B(1), L(1), N(1). Total 10 letters.
Multiset permutation: $\dfrac{10!}{2!\,4!}=\frac{3628800}{2\cdot24}=\frac{3628800}{48}=75600$.

$$\boxed{\dfrac{10!}{2!\,4!}=75600}$$

---

**44.** How many different strings can be made from the letters in SUCCESS, using all letters?

**Solution.**
Count letters: S(3), U(1), C(2), E(1). Total 7.
Multiset permutation: $\dfrac{7!}{3!\,2!}=\frac{5040}{12}=420$.

$$\boxed{\dfrac{7!}{3!\,2!}=420}$$

---

**45.** Find the coefficient of the monomial $x^3y^2z^5$ in the expansion of $(2x-3y-2z)^{10}$.

**Solution.**
Verify $3+2+5=10$. Multinomial coefficient: $\frac{10!}{3!\,2!\,5!}$.
Coefficient from terms: $(2x)^3(-3y)^2(-2z)^5=2^3\cdot(-3)^2\cdot(-2)^5=8\cdot9\cdot(-32)=-2304$.
Note $2^8\cdot3^2=256\cdot9=2304$, so total coefficient:
$$-\frac{10!}{3!\,2!\,5!}\cdot2^8\cdot3^2$$
Compute: $\frac{3628800}{6\cdot2\cdot120}=\frac{3628800}{1440}=2520$. $2520\cdot(-2304)=-5806080$.

$$\boxed{-\dfrac{10!}{3!\,2!\,5!}\cdot2^8\cdot3^2=-5806080}$$

---

**46.** How many ways are there for three identical red apples and two identical golden apples to be lined up in a line?

**Solution.**
Total 5 apples, identical within colors. Multiset permutation: $\frac{5!}{3!\,2!}=C(5,2)=10$.

$$\boxed{\dfrac{5!}{3!\,2!}=C(5,2)=10}$$

---

**47.** How many ways are there for three identical red apples, two identical golden apples, and four identical green apples to be lined up in a line?

**Solution.**
Total 9 apples with multiplicities 3, 2, 4. Multiset permutation: $\dfrac{9!}{3!\,2!\,4!}=\frac{362880}{6\cdot2\cdot24}=\frac{362880}{288}=1260$.

$$\boxed{\dfrac{9!}{3!\,2!\,4!}=1260}$$

---

**48.** How many ways are there to distribute $k$ indistinguishable apples to $n$ children?

**Solution.**
Stars and bars model: $k$ identical stars, $n-1$ bars to separate $n$ children. Choose positions for bars:
$$C(k+n-1,k)=C(k+n-1,n-1)$$

$$\boxed{C(k+n-1,k)=C(n+k-1,n-1)}$$

---

**49.** How many ways are there to place $k$ indistinguishable books onto the $n$ shelves of a bookcase?

**Solution.**
Same stars and bars model: $k$ identical books (stars), $n$ shelves (bars separate shelves).
$$C(k+n-1,k)=C(n+k-1,n-1)$$

$$\boxed{C(k+n-1,k)=C(n+k-1,n-1)}$$


---

**50.** How many non-negative solutions of $x_1+x_2+\cdots+x_n=k$ are there?

**Solution.**
Stars and bars: $k$ stars, $n-1$ bars.
$$C(k+n-1,k)=C(n+k-1,n-1)$$

$$\boxed{C(n+k-1,k)}$$

---

**51.** How many solutions to $x_1+x_2+\cdots+x_n=k$ with each $x_i>0$ and $x_i\in\mathbb{Z}$?

**Solution.**
Set $x_i'=x_i-1\ge0$. Then $\sum x_i'=k-n$.
Non-negative solutions: $C((k-n)+n-1,\,k-n)=C(k-1,\,n-1)=C(k-1,k-n)$.

$$\boxed{C(k-1,n-1)=C(k-1,k-n)}$$

---

**52.** In how many ways may we pass out $k$ indistinguishable apples to $n$ children if each child must get at least one?

**Solution.**
Give each child 1 apple first (uses $n$ apples). Distribute remaining $k-n$ identical apples with no restriction.
Stars and bars: $C((k-n)+n-1,\,k-n)=C(k-1,\,n-1)=C(k-1,k-n)$.

$$\boxed{C(k-1,n-1)=C(k-1,k-n)}$$

---

**53.** In how many ways may $n$ red checkers and $n+1$ black checkers be arranged in a circle?

**Solution.**
Total checkers: $2n+1$. Linear arrangements (identical within color): $\frac{(2n+1)!}{n!(n+1)!}$.
In a circle, each arrangement is overcounted by a factor of $2n+1$ rotations. By the Division Rule:
$$\frac{(2n+1)!}{n!(n+1)!}\div(2n+1)=\frac{(2n)!}{n!(n+1)!}$$

$$\boxed{\dfrac{(2n)!}{n!(n+1)!}}$$

---

**54.** How many solutions are there to $x_1+x_2+x_3+x_4+x_5=21$, where $x_i$ are non-negative integers such that
a. $x_i\ge1$ for $i=1,\dots,5$;
b. $x_i\ge2$ for $i=1,\dots,5$;
c. $0\le x_1\le 10$ (no restriction on $x_2,\dots,x_5$).

**Solution.**
**(a) $x_i\ge1$ for all $i$:**
Set $x_i'=x_i-1\ge0$. Then $\sum x_i'=21-5=16$ over 5 variables.
Stars and bars: $C(16+5-1,16)=C(20,16)=C(20,4)=4845$.

**(b) $x_i\ge2$ for all $i$:**
Set $x_i'=x_i-2\ge0$. Then $\sum x_i'=21-10=11$ over 5 variables.
Stars and bars: $C(11+5-1,11)=C(15,11)=C(15,4)=1365$.

**(c) $0\le x_1\le 10$:**
Total unrestricted solutions: $C(21+5-1,21)=C(25,21)=C(25,4)=12650$.
Subtract solutions with $x_1\ge 11$: set $x_1'=x_1-11\ge0$, then $x_1'+x_2+\cdots+x_5=10$. Number: $C(10+5-1,10)=C(14,10)=C(14,4)=1001$.
By the Complement Rule: $C(25,4)-C(14,4)=12650-1001=11649$.

$$\boxed{\text{(a) }C(20,4)=4845\quad\text{(b) }C(15,4)=1365\quad\text{(c) }C(25,4)-C(14,4)=11649}$$

---

**55.** How many solutions to $x_1+x_2+x_3\le 11$, where $x_1,x_2,x_3$ are non-negative integers?

**Solution.**
Introduce slack variable $x_4\ge0$ such that $x_1+x_2+x_3+x_4=11$.
Non-negative solutions with 4 variables, sum 11: $C(11+4-1,11)=C(14,11)=C(14,3)=364$.

$$\boxed{C(14,3)=364}$$

---

**56.** Which of the following subsets form a partition of the set of all real numbers?

**Solution.**
Recall: a partition of $\mathbb{R}$ requires every real number to appear in **exactly one** subset.

**(a)** Positive integers, negative integers.
No — misses $0$ and all non-integer real numbers. **Not a partition.**

**(b)** Non-positive integers, non-negative integers.
No — $0$ belongs to **both** subsets (intersection non-empty). **Not a partition.**

**(c)** Rational numbers, irrational numbers.
Yes — every real number is either rational or irrational, never both. **Is a partition.**

**(d)** Closed intervals $[n,n+1]$ for integer $n$.
No — intervals overlap at endpoints: e.g., $[0,1]$ and $[1,2]$ both contain $1$. **Not a partition.**

**(e)** Intervals $(n,n+1]$ for integer $n$.
Yes — these are disjoint (each integer $n$ is the endpoint of exactly one interval) and they cover all reals. **Is a partition.**

$$\boxed{\text{(c) Yes, (e) Yes; (a),(b),(d) No}}$$

---

**57.** List all partitions of $[4]$ into $k=1,2,3,4$ parts. What are $S(4,k)$? What is $B(4)$?

**Solution.**
**$k=1$** ($S(4,1)=1$): $\{\{1,2,3,4\}\}$

**$k=2$** ($S(4,2)=7$):
$$\begin{aligned}
&\{1\},\{2,3,4\};\quad\{2\},\{1,3,4\};\quad\{3\},\{1,2,4\};\quad\{4\},\{1,2,3\};\\
&\{1,2\},\{3,4\};\quad\{1,3\},\{2,4\};\quad\{1,4\},\{2,3\}
\end{aligned}$$

**$k=3$** ($S(4,3)=C(4,2)=6$): one pair + two singletons.
$$\begin{aligned}
&\{1,2\},\{3\},\{4\};\quad\{1,3\},\{2\},\{4\};\quad\{1,4\},\{2\},\{3\};\\
&\{2,3\},\{1\},\{4\};\quad\{2,4\},\{1\},\{3\};\quad\{3,4\},\{1\},\{2\}
\end{aligned}$$

**$k=4$** ($S(4,4)=1$): $\{\{1\},\{2\},\{3\},\{4\}\}$

Stirling numbers: $S(4,1)=1$, $S(4,2)=7$, $S(4,3)=6$, $S(4,4)=1$.
Bell number $B(4)=1+7+6+1=15$.

$$\boxed{\begin{aligned}&S(4,1)=1,\;S(4,2)=7,\;S(4,3)=6,\;S(4,4)=1\\&B(4)=15\end{aligned}}$$

---

**58.** What are $S(n,1)$, $S(n,n-1)$, $S(n,n)$ in the general case?

**Solution.**
- $S(n,1)=1$: only one block = the whole set $[n]$.
- $S(n,n)=1$: all singletons.
- $S(n,n-1)=C(n,2)$: exactly one block of size 2 (choose the pair); all others singletons.

$$\boxed{S(n,1)=1,\quad S(n,n)=1,\quad S(n,n-1)=C(n,2)}$$

---

**59.** Construct a recursive formula for $S(n,k)$. What is $S(n,2)$?

**Solution.**
**(Recurrence)** Consider element $n$. It either forms a new singleton block ($S(n-1,k-1)$ ways) OR joins one of the $k$ existing blocks of a partition of $[n-1]$ ($k\cdot S(n-1,k)$ ways). By the Sum Rule:
$$S(n,k)=S(n-1,k-1)+k\cdot S(n-1,k)$$

**(Value $S(n,2)$):** Unfold the recurrence with $S(1,2)=0$:
$$S(n,2)=S(n-1,1)+2S(n-1,2)=1+2S(n-1,2)$$
$$=1+2(1+2S(n-2,2))=1+2+4+\cdots+2^{n-2}=2^{n-1}-1$$

$$\boxed{S(n,k)=S(n-1,k-1)+k\,S(n-1,k);\qquad S(n,2)=2^{n-1}-1}$$

---

**60.** Construct a bijection from the set of all partitions of $[n]$ into 2 parts to the family of non-empty subsets of $[n-1]$.

**Solution.**
**(Bijection)**
Define $f:\{\text{partitions of }[n]\text{ into 2 blocks}\}\to\{\text{non-empty subsets of }[n-1]\}$.
For a partition $\{A,B\}$ of $[n]$ into 2 non-empty blocks, let the block containing $n$ be $A$. Set $f(\{A,B\})=B$.

- **Well-defined:** $B\subseteq[n]\setminus\{n\}=[n-1]$. Since $B$ is non-empty, $f(\{A,B\})$ is a non-empty subset of $[n-1]$.
- **Injectivity:** If $f(\{A_1,B_1\})=f(\{A_2,B_2\})=B$, then $B_1=B_2=B$ and $A_1=[n]\setminus B=A_2$. Partitions are identical.
- **Surjectivity:** For any non-empty $B\subseteq[n-1]$, let $A=[n]\setminus B$. Then $n\in A$, $A\neq\emptyset$, and $\{A,B\}$ is a partition of $[n]$ into 2 blocks with $f(\{A,B\})=B$.

Both sets have size $2^{n-1}-1$, confirming the bijection.

$$\boxed{f(\{A,B\})=B\text{ where }n\in A}$$

---

**61.** Which of these collections of subsets are partitions of $\{1,2,3,4,5,6\}$?

**Solution.**
**(a)** $\{1,2\},\{2,3,4\},\{4,5,6\}$ — No (elements 2 and 4 appear in more than one subset).

**(b)** $\{1\},\{2,3,6\},\{4\}$ — No (element 5 is missing).

**(c)** $\{2,4,6\},\{1,3,5\}$ — Yes (disjoint, union is the whole set).

**(d)** $\{1,4,5\},\{2,6\}$ — No (element 3 is missing).

$$\boxed{\text{(a) No, (b) No, (c) Yes, (d) No}}$$

---

**62.** How many ways to place 4 distinct gifts into 3 identical boxes?

**Solution.**
Boxes are identical (unlabeled). Count set partitions into at most 3 blocks (empty boxes ignored):
$$S(4,1)+S(4,2)+S(4,3)=1+7+6=14$$

$$\boxed{S(4,1)+S(4,2)+S(4,3)=1+7+6=14}$$

---

**63.** How many ways if each box must contain at least one gift? (4 distinct gifts, 3 identical boxes)

**Solution.**
Partition into exactly 3 non-empty blocks: $S(4,3)=C(4,2)=6$.

$$\boxed{S(4,3)=C(4,2)=6}$$

---

**64.** How many ways to place 4 identical gifts into 3 identical boxes?

**Solution.**
Gifts identical, boxes identical $\Rightarrow$ integer partitions of 4 into at most 3 parts:
- $4$ (all in one box)
- $3+1$
- $2+2$
- $2+1+1$
Total: $4$ ways.

$$\boxed{4}$$

---

**65.** How many ways if each box must contain at least 1 gift? (4 identical gifts, 3 identical boxes)

**Solution.**
Integer partitions of 4 into exactly 3 positive parts: only $4=2+1+1$. So $1$ way.

$$\boxed{1}$$

---

**66.** How many ways to place 15 distinct gifts into 10 distinct boxes?

**Solution.**
Each gift independently goes to one of 10 boxes. By the Product Rule: $10^{15}$.

$$\boxed{10^{15}}$$

---

**67.** How many ways if each box contains at least 1 gift? (15 distinct, 10 distinct boxes)

**Solution.**
Surjective (onto) functions from a 15-set to a 10-set:
$$10!\cdot S(15,10)=\sum_{j=0}^{10}(-1)^j\binom{10}{j}(10-j)^{15}$$

$$\boxed{10!\cdot S(15,10)=\sum_{j=0}^{10}(-1)^j\binom{10}{j}(10-j)^{15}}$$

---

**68.** How many ways if each box contains at most 1 gift? (15 distinct gifts, 10 distinct boxes)

**Solution.**
With 15 gifts and only 10 boxes, by the Pigeonhole Principle it is impossible. Answer: $0$.

$$\boxed{0}$$

---

**69.** How many ways to place 10 distinct gifts into 15 distinct boxes such that each box contains at most 1 gift?

**Solution.**
Choose which 10 boxes receive a gift: $C(15,10)$. Assign 10 distinct gifts to those 10 boxes: $10!$. By the Product Rule:
$$C(15,10)\cdot10!=P(15,10)=\frac{15!}{5!}=10897286400$$

$$\boxed{P(15,10)=\dfrac{15!}{5!}=10897286400}$$

---

**70.** How many ways to place 100 identical gifts into 3 distinct boxes?

**Solution.**
Stars and bars: $k=100$, $n=3$. $C(100+3-1,100)=C(102,100)=C(102,2)=\frac{102\cdot101}{2}=5151$.

$$\boxed{C(102,2)=5151}$$

---

**71.** How many ways to place 100 identical gifts into 10 distinct boxes such that each box contains at least 5 gifts?

**Solution.**
Give each box 5 gifts first: uses $50$ gifts. Remaining $50$ identical gifts into $10$ distinct boxes, no restriction.
Stars and bars: $C(50+10-1,50)=C(59,50)=C(59,9)$.

$$\boxed{C(59,50)=C(59,9)}$$

---

**72.** Write down all possible permutations of $[4]$ that map 1 to 3.

**Solution.**
$\sigma(1)=3$ fixed. Remaining domain $\{2,3,4\}$ maps bijectively to $\{1,2,4\}$. $3!=6$ permutations. In one-line notation $(\sigma(1),\sigma(2),\sigma(3),\sigma(4))$:
$$(3,1,2,4),\;(3,1,4,2),\;(3,2,1,4),\;(3,2,4,1),\;(3,4,1,2),\;(3,4,2,1)$$

$$\boxed{(3,1,2,4),\;(3,1,4,2),\;(3,2,1,4),\;(3,2,4,1),\;(3,4,1,2),\;(3,4,2,1)}$$

---

**73.** Write down all possible permutations in two-line notation of $[5]$ that have 5 as a fixed point and that map 3 to 2.

**Solution.**
$\sigma(5)=5$, $\sigma(3)=2$. Remaining: domain $\{1,2,4\}$, codomain $\{1,3,4\}$. $3!=6$ permutations.

$$\boxed{\begin{aligned}
&\begin{pmatrix}1&2&3&4&5\\1&3&2&4&5\end{pmatrix},\;
\begin{pmatrix}1&2&3&4&5\\1&4&2&3&5\end{pmatrix},\;
\begin{pmatrix}1&2&3&4&5\\3&1&2&4&5\end{pmatrix},\\
&\begin{pmatrix}1&2&3&4&5\\3&4&2&1&5\end{pmatrix},\;
\begin{pmatrix}1&2&3&4&5\\4&1&2&3&5\end{pmatrix},\;
\begin{pmatrix}1&2&3&4&5\\4&3&2&1&5\end{pmatrix}
\end{aligned}}$$

---

**74.** For each permutation given in one-line notation, write in cycle notation and two-line notation; find fixed points, number of cycles, $\sigma^{-1}$, $\sigma^2$.

**74a.** $\sigma=36215847$

**Solution.**
$\sigma(1)=3,\sigma(2)=6,\sigma(3)=2,\sigma(4)=1,\sigma(5)=5,\sigma(6)=8,\sigma(7)=4,\sigma(8)=7$.

**Cycle decomposition:** $1\to3\to2\to6\to8\to7\to4\to1$ gives $(1\;3\;2\;6\;8\;7\;4)$. $5\to5$ gives $(5)$.
$$\sigma=(1\;3\;2\;6\;8\;7\;4)(5)$$

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6&7&8\\3&6&2&1&5&8&4&7\end{pmatrix}$

**Fixed points:** $\{5\}$. **Number of cycles:** $2$.

**$\sigma^{-1}$:** Reverse the 7-cycle: $(1\;4\;7\;8\;6\;2\;3)(5)$.
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7&8\\4&3&1&7&5&2&8&6\end{pmatrix}$

**$\sigma^2$:** 7-cycle (odd length) stays a 7-cycle; compute step-by-2:
$\sigma^2(1)=2,\sigma^2(2)=8,\sigma^2(8)=4,\sigma^2(4)=3,\sigma^2(3)=6,\sigma^2(6)=7,\sigma^2(7)=1$.
$$\sigma^2=(1\;2\;8\;4\;3\;6\;7)(5)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7&8\\2&8&6&3&5&7&1&4\end{pmatrix}$

$$\boxed{\begin{aligned}&\sigma=(1\;3\;2\;6\;8\;7\;4)(5),\;\text{fixed: }\{5\},\;\text{cycles: }2\\
&\sigma^{-1}=(1\;4\;7\;8\;6\;2\;3)(5)\\
&\sigma^2=(1\;2\;8\;4\;3\;6\;7)(5)\end{aligned}}$$

---

**74b.** $\sigma=42765813$

**Solution.**
$\sigma(1)=4,\sigma(2)=2,\sigma(3)=7,\sigma(4)=6,\sigma(5)=5,\sigma(6)=8,\sigma(7)=1,\sigma(8)=3$.

**Cycle decomposition:** $1\to4\to6\to8\to3\to7\to1$ gives $(1\;4\;6\;8\;3\;7)$. $2\to2$, $5\to5$.
$$\sigma=(1\;4\;6\;8\;3\;7)(2)(5)$$

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6&7&8\\4&2&7&6&5&8&1&3\end{pmatrix}$

**Fixed points:** $\{2,5\}$. **Number of cycles:** $3$.

**$\sigma^{-1}$:** Reverse the 6-cycle: $(1\;7\;3\;8\;6\;4)(2)(5)$.
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7&8\\7&2&8&1&5&4&3&6\end{pmatrix}$

**$\sigma^2$:** 6-cycle is even length $\to$ splits into two 3-cycles:
$\sigma^2(1)=6,\sigma^2(6)=3,\sigma^2(3)=1$ $\Rightarrow$ $(1\;6\;3)$.
$\sigma^2(4)=8,\sigma^2(8)=7,\sigma^2(7)=4$ $\Rightarrow$ $(4\;8\;7)$.
$$\sigma^2=(1\;6\;3)(4\;8\;7)(2)(5)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7&8\\6&2&1&8&5&3&4&7\end{pmatrix}$

$$\boxed{\begin{aligned}&\sigma=(1\;4\;6\;8\;3\;7)(2)(5),\;\text{fixed: }\{2,5\},\;\text{cycles: }3\\
&\sigma^{-1}=(1\;7\;3\;8\;6\;4)(2)(5)\\
&\sigma^2=(1\;6\;3)(4\;8\;7)(2)(5)\end{aligned}}$$

---

**74c.** $\sigma=361452$

**Solution.**
$n=6$. $\sigma(1)=3,\sigma(2)=6,\sigma(3)=1,\sigma(4)=4,\sigma(5)=5,\sigma(6)=2$.

**Cycle decomposition:** $1\to3\to1$: $(1\;3)$. $2\to6\to2$: $(2\;6)$. $4\to4$, $5\to5$.
$$\sigma=(1\;3)(2\;6)(4)(5)$$

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6\\3&6&1&4&5&2\end{pmatrix}$

**Fixed points:** $\{4,5\}$. **Number of cycles:** $4$.

**$\sigma^{-1}$:** All transpositions are self-inverse: $\sigma^{-1}=\sigma=(1\;3)(2\;6)(4)(5)$.

**$\sigma^2$:** Transpositions squared = identity, fixed points unchanged:
$$\sigma^2=\text{id}=(1)(2)(3)(4)(5)(6)$$

$$\boxed{\begin{aligned}&\sigma=(1\;3)(2\;6)(4)(5),\;\text{fixed: }\{4,5\},\;\text{cycles: }4\\
&\sigma^{-1}=\sigma=(1\;3)(2\;6)(4)(5)\\
&\sigma^2=\text{id}\end{aligned}}$$

---

**74d.** $\sigma=32156487$

**Solution.**
$\sigma(1)=3,\sigma(2)=2,\sigma(3)=1,\sigma(4)=5,\sigma(5)=6,\sigma(6)=4,\sigma(7)=8,\sigma(8)=7$.

**Cycle decomposition:** $1\to3\to1$: $(1\;3)$. $2\to2$: $(2)$. $4\to5\to6\to4$: $(4\;5\;6)$. $7\to8\to7$: $(7\;8)$.
$$\sigma=(1\;3)(2)(4\;5\;6)(7\;8)$$

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6&7&8\\3&2&1&5&6&4&8&7\end{pmatrix}$

**Fixed points:** $\{2\}$. **Number of cycles:** $4$.

**$\sigma^{-1}$:** $(1\;3)^{-1}=(1\;3)$, $(4\;5\;6)^{-1}=(4\;6\;5)$, $(7\;8)^{-1}=(7\;8)$, $(2)^{-1}=(2)$.
$$\sigma^{-1}=(1\;3)(2)(4\;6\;5)(7\;8)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7&8\\3&2&1&6&4&5&8&7\end{pmatrix}$

**$\sigma^2$:** $(1\;3)^2=\text{id}$, $(4\;5\;6)^2=(4\;6\;5)$, $(7\;8)^2=\text{id}$.
$$\sigma^2=(4\;6\;5)(2)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7&8\\1&2&3&6&4&5&7&8\end{pmatrix}$

$$\boxed{\begin{aligned}&\sigma=(1\;3)(2)(4\;5\;6)(7\;8),\;\text{fixed: }\{2\},\;\text{cycles: }4\\
&\sigma^{-1}=(1\;3)(2)(4\;6\;5)(7\;8)\\
&\sigma^2=(4\;6\;5)(2)\end{aligned}}$$


---

**75.** For each permutation given in cycle notation, write two-line notation, compute $\sigma^{-1}$ and $\sigma^2$.

**75a.** $\sigma=(1,3,5)(2,4,6)$

**Solution.**
Disjoint cycles, $n=6$. Direct reading:
$\sigma(1)=3,\sigma(3)=5,\sigma(5)=1,\sigma(2)=4,\sigma(4)=6,\sigma(6)=2$.

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6\\3&4&5&6&1&2\end{pmatrix}$

**$\sigma^{-1}$:** Reverse each cycle: $(1\;5\;3)(2\;6\;4)$.
Two-line: $\begin{pmatrix}1&2&3&4&5&6\\5&6&1&2&3&4\end{pmatrix}$

**$\sigma^2$:** Both 3-cycles (odd length) stay 3-cycles, step by 2: $\sigma^2=(1\;5\;3)(2\;6\;4)=\sigma^{-1}$.

$$\boxed{\begin{aligned}&\text{Two-line: }\begin{pmatrix}1&2&3&4&5&6\\3&4&5&6&1&2\end{pmatrix}\\
&\sigma^{-1}=(1\;5\;3)(2\;6\;4)\\
&\sigma^2=(1\;5\;3)(2\;6\;4)=\sigma^{-1}\end{aligned}}$$

---

**75b.** $\sigma=(2,3)(1,7)(5)(6,2)$

**Solution.**
Cycles are NOT disjoint (2 appears in two cycles). Compose right-to-left (function composition convention). Domain $[7]$.

Trace each element through $(6,2)\to(5)\to(1,7)\to(2,3)$:
- $1$: $(6,2)\to1,(5)\to1,(1,7)\to7,(2,3)\to7$. $\sigma(1)=7$.
- $2$: $(6,2)\to6,(5)\to6,(1,7)\to6,(2,3)\to6$. $\sigma(2)=6$.
- $3$: $(6,2)\to3,(5)\to3,(1,7)\to3,(2,3)\to2$. $\sigma(3)=2$.
- $4$: $(6,2)\to4,(5)\to4,(1,7)\to4,(2,3)\to4$. $\sigma(4)=4$.
- $5$: $(6,2)\to5,(5)\to5,(1,7)\to5,(2,3)\to5$. $\sigma(5)=5$.
- $6$: $(6,2)\to2,(5)\to2,(1,7)\to2,(2,3)\to3$. $\sigma(6)=3$.
- $7$: $(6,2)\to7,(5)\to7,(1,7)\to1,(2,3)\to1$. $\sigma(7)=1$.

Disjoint cycle decomposition: $1\to7\to1$: $(1\;7)$. $2\to6\to3\to2$: $(2\;6\;3)$. $4\to4$, $5\to5$.
$$\sigma=(1\;7)(2\;6\;3)(4)(5)$$

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6&7\\7&6&2&4&5&3&1\end{pmatrix}$

**$\sigma^{-1}$:** Reverse cycles: $(1\;7)(2\;3\;6)(4)(5)$.
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7\\7&3&6&4&5&2&1\end{pmatrix}$

**$\sigma^2$:** $(1\;7)^2=\text{id}$, $(2\;6\;3)^2=(2\;3\;6)$ (3-cycle squared = inverse).
$$\sigma^2=(2\;3\;6)(4)(5)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7\\1&3&6&4&5&2&7\end{pmatrix}$

$$\boxed{\begin{aligned}&\text{Two-line: }\begin{pmatrix}1&2&3&4&5&6&7\\7&6&2&4&5&3&1\end{pmatrix}\\
&\sigma^{-1}=(1\;7)(2\;3\;6)(4)(5)\\
&\sigma^2=(2\;3\;6)(4)(5)\end{aligned}}$$

---

**75c.** $\sigma=(7,5,3,1)(2,4,6)$

**Solution.**
Disjoint cycles, $n=7$. Direct reading:
$\sigma(1)=7,\sigma(2)=4,\sigma(3)=1,\sigma(4)=6,\sigma(5)=3,\sigma(6)=2,\sigma(7)=5$.

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6&7\\7&4&1&6&3&2&5\end{pmatrix}$

**$\sigma^{-1}$:** Reverse each cycle: $(1\;3\;5\;7)(2\;6\;4)$.
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7\\3&6&5&2&7&4&1\end{pmatrix}$

**$\sigma^2$:** 4-cycle $(7\;5\;3\;1)$ (even length) splits into two 2-cycles:
$\sigma^2(7)=\sigma(5)=3,\sigma^2(3)=\sigma(1)=7$ $\Rightarrow$ $(3\;7)$.
$\sigma^2(1)=\sigma(7)=5,\sigma^2(5)=\sigma(3)=1$ $\Rightarrow$ $(1\;5)$.
3-cycle $(2\;4\;6)$ squared: $(2\;6\;4)$.
$$\sigma^2=(1\;5)(3\;7)(2\;6\;4)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7\\5&6&7&2&1&4&3\end{pmatrix}$

$$\boxed{\begin{aligned}&\text{Two-line: }\begin{pmatrix}1&2&3&4&5&6&7\\7&4&1&6&3&2&5\end{pmatrix}\\
&\sigma^{-1}=(1\;3\;5\;7)(2\;6\;4)\\
&\sigma^2=(1\;5)(3\;7)(2\;6\;4)\end{aligned}}$$

---

**75d.** $\sigma=(2,7)(6,5,1)(4,3)$

**Solution.**
Disjoint cycles, $n=7$. Direct reading:
$\sigma(1)=6,\sigma(2)=7,\sigma(3)=4,\sigma(4)=3,\sigma(5)=1,\sigma(6)=5,\sigma(7)=2$.

**Two-line:** $\begin{pmatrix}1&2&3&4&5&6&7\\6&7&4&3&1&5&2\end{pmatrix}$

**$\sigma^{-1}$:** Reverse each cycle: $(2\;7)^{-1}=(2\;7)$, $(6\;5\;1)^{-1}=(1\;5\;6)$, $(4\;3)^{-1}=(4\;3)$.
$$\sigma^{-1}=(1\;5\;6)(2\;7)(3\;4)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7\\5&7&4&3&6&1&2\end{pmatrix}$

**$\sigma^2$:** $(2\;7)^2=\text{id}$, $(6\;5\;1)^2=(6\;1\;5)=(1\;5\;6)$, $(4\;3)^2=\text{id}$.
$$\sigma^2=(1\;5\;6)$$
Two-line: $\begin{pmatrix}1&2&3&4&5&6&7\\5&2&3&4&6&1&7\end{pmatrix}$

$$\boxed{\begin{aligned}&\text{Two-line: }\begin{pmatrix}1&2&3&4&5&6&7\\6&7&4&3&1&5&2\end{pmatrix}\\
&\sigma^{-1}=(1\;5\;6)(2\;7)(3\;4)\\
&\sigma^2=(1\;5\;6)\end{aligned}}$$

---

**76.** List all permutations without fixed points on $[4]$ and $[6]$.

**Solution.**
Permutations without fixed points = derangements.

**For $[4]$:** $D_4=9$. Cycle types:
- Two 2-cycles (3): $(1\;2)(3\;4)$, $(1\;3)(2\;4)$, $(1\;4)(2\;3)$.
- One 4-cycle (6): $(1\;2\;3\;4)$, $(1\;2\;4\;3)$, $(1\;3\;2\;4)$, $(1\;3\;4\;2)$, $(1\;4\;2\;3)$, $(1\;4\;3\;2)$.

Total: $9$.

**For $[6]$:** $D_6=265$. Cycle type breakdown:
- Three 2-cycles: $\frac{6!}{2^3\cdot3!}=15$ derangements.
- Two 3-cycles: $\frac{6!}{3^2\cdot2!}\cdot 2^2 = 40$ derangements (choose which 6 elements go into two 3-cycles, times $(2!)^2$ for cycle structure within each block).
- One 6-cycle: $(6-1)!=120$ derangements.
- One 4-cycle + one 2-cycle: $\binom{6}{2}\cdot(3!)\cdot\frac{2!}{2}=90$ derangements.
Total: $15+40+120+90=265$.

$$\boxed{D_4=9,\quad D_6=265}$$

---

**77.** List all permutations with 2 cycles of $[4]$ and of $[6]$.

**Solution.**
Number of permutations of $[n]$ with exactly $k$ cycles = unsigned Stirling number of first kind $c(n,k)$.

**For $[4]$:** $c(4,2)=11$. Cycle types:
- One 3-cycle + one 1-cycle (fixed point): $2\cdot C(4,3)=8$ (choose the fixed element: 4 ways; 3-cycle on remaining 3 elements: $2!=(3-1)!=2$ ways).
  $(1)(2\;3\;4)$, $(1)(2\;4\;3)$, $(2)(1\;3\;4)$, $(2)(1\;4\;3)$, $(3)(1\;2\;4)$, $(3)(1\;4\;2)$, $(4)(1\;2\;3)$, $(4)(1\;3\;2)$.
- Two 2-cycles: $\frac{C(4,2)}{2}\cdot\frac{C(2,2)}{1}=3$ (choose the first 2-cycle: $\binom{4}{2}=6$ ways, divide by 2 because the two 2-cycles are unordered).
  $(1\;2)(3\;4)$, $(1\;3)(2\;4)$, $(1\;4)(2\;3)$.

Total: $8+3=11$.

**For $[6]$:** $c(6,2)=274$. (Too many to exhaustively list; given by recurrence $c(6,2)=c(5,1)+5\cdot c(5,2)=24+5\cdot50=274$.)

Cycle type breakdown:
- One 5-cycle + one fixed point: $(5-1)!\cdot\binom{6}{1}=24\cdot6=144$.
- One 4-cycle + one 2-cycle: $\binom{6}{4}\cdot(4-1)!\cdot\frac{2!}{2}=15\cdot6\cdot1=90$.
- Two 3-cycles: $\frac{\binom{6}{3}}{2}\cdot(3-1)!\cdot(3-1)!=10\cdot2\cdot2=40$.
Total: $144+90+40=274$.

$$\boxed{c(4,2)=11,\quad c(6,2)=274}$$

---

**78.** List all derangements of $[3]$ and $[4]$. Prove that $D_n=(n-1)(D_{n-1}+D_{n-2})$.

**Solution.**

**Derangements of $[3]$ ($D_3=2$):**
The only derangements on $[3]$ are the two 3-cycles:
$$(1\;2\;3),\quad(1\;3\;2)$$

**Derangements of $[4]$ ($D_4=9$):**
Cycle types: two 2-cycles (3) + one 4-cycle (6).
Two 2-cycles: $(1\;2)(3\;4)$, $(1\;3)(2\;4)$, $(1\;4)(2\;3)$.
One 4-cycle: $(1\;2\;3\;4)$, $(1\;2\;4\;3)$, $(1\;3\;2\;4)$, $(1\;3\;4\;2)$, $(1\;4\;2\;3)$, $(1\;4\;3\;2)$.

**Proof of recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$:**
Step 1. Consider a derangement $\sigma$ of $[n]$. Element $1$ must map to some $k\neq 1$, where $k\in\{2,3,\dots,n\}$. There are $n-1$ choices for $\sigma(1)=k$.

Step 2. Two disjoint cases:
- **Case 1:** $\sigma(k)=1$ (1 and $k$ swap). The remaining $n-2$ elements $\{2,\dots,n\}\setminus\{k\}$ must form a derangement among themselves. Number of ways: $D_{n-2}$.
- **Case 2:** $\sigma(k)\neq 1$. We "identify" element $1$ with position $k$: among the $n-1$ elements $\{2,\dots,n\}$, we require that $k$ does not go to $1$ (forbidden position for $k$ is treated as position 1) and each other element $i$ does not go to its own position. This is exactly a derangement of $n-1$ elements. Number of ways: $D_{n-1}$.

Step 3. Cases are disjoint, so by the Sum Rule:
$$D_n=(n-1)(D_{n-2}+D_{n-1})=(n-1)(D_{n-1}+D_{n-2})$$

Base cases: $D_1=0$, $D_2=1$. Check: $D_3=2(1+0)=2$, $D_4=3(2+1)=9$, $D_5=4(9+2)=44$, etc.

$$\boxed{\begin{aligned}D_3=2&:\;(1\;2\;3),\;(1\;3\;2)\\
D_4=9&:\;(1\;2)(3\;4),(1\;3)(2\;4),(1\;4)(2\;3),\\
&\quad\;(1\;2\;3\;4),(1\;2\;4\;3),(1\;3\;2\;4),(1\;3\;4\;2),(1\;4\;2\;3),(1\;4\;3\;2)\\
D_n&=(n-1)(D_{n-1}+D_{n-2})\end{aligned}}$$

---

**79.** Suppose 8 men give their hats to a hat-check person. How many ways can the hats be given back so that no man receives his own hat?

**Solution.**
This is the derangement number $D_8$. Using the recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$ with $D_2=1$, $D_3=2$:
$$D_4=3(2+1)=9$$
$$D_5=4(9+2)=44$$
$$D_6=5(44+9)=265$$
$$D_7=6(265+44)=1854$$
$$D_8=7(1854+265)=14833$$

$$\boxed{D_8=14833}$$

---

**80.** A student has three mangos, two papayas, and two kiwi fruits. If the student eats one piece each day, and only the type matters, in how many different ways can these fruits be consumed?

**Solution.**
Total 7 fruits with multiplicities 3 (mangos), 2 (papayas), 2 (kiwis). The sequence of consumption is a multiset permutation:
$$\frac{7!}{3!\,2!\,2!}=\frac{5040}{6\cdot2\cdot2}=\frac{5040}{24}=210$$

$$\boxed{\dfrac{7!}{3!\,2!\,2!}=210}$$

---

**81.** There are 4 men and 6 women. Each man marries one of the women. In how many ways can this be done?

**Solution.**
Men are distinct, women are distinct. First man chooses one of 6 women, second chooses one of the remaining 5, etc. (Each marriage is distinct; a woman cannot marry more than one man.)
$$P(6,4)=6\cdot5\cdot4\cdot3=360$$

Equivalently, $\frac{6!}{2!}=360$.

$$\boxed{P(6,4)=\dfrac{6!}{2!}=360}$$

---

**82.** How many ways are there to pack eight identical DVDs into five indistinguishable boxes so that each box contains at least one DVD?

**Solution.**
Both items and boxes are identical, each box $\ge 1$. This is the number of integer partitions of 8 into exactly 5 positive parts.
$$8 = 4+1+1+1+1$$
$$8 = 3+2+1+1+1$$
$$8 = 2+2+2+1+1$$
Total: $3$ ways.

$$\boxed{3}$$

---

**83.** There are 10 questions on a discrete mathematics final exam. How many ways are there to assign scores if the sum is 100 and each question is worth at least 5 points?

**Solution.**
Let $x_i$ be the score on question $i$. Then $x_i\ge 5$ and $\sum_{i=1}^{10} x_i = 100$.
Set $y_i=x_i-5\ge 0$. Then $\sum y_i = 100-50 = 50$.
Stars and bars with 10 variables, sum 50: $C(50+10-1,\,50)=C(59,50)=C(59,9)$.

$$\boxed{C(59,50)=C(59,9)}$$

---

**84.** How many permutations of $[2n]$ assign even numbers to odd numbers?

**Solution.**
For each odd $i\in\{1,3,\dots,2n-1\}$, $\sigma(i)$ must be even. There are $n$ odd numbers and $n$ even numbers.
The restriction means: the $n$ odd domain elements map injectively to the $n$ even codomain elements: $n!$ ways. The $n$ even domain elements then map to the remaining $n$ odd values: $n!$ ways. By the Product Rule: $(n!)^2$.

$$\boxed{(n!)^2}$$

---

**85.** In a bureau drawer there are 60 socks: 10 pairs are red, 10 pairs are blue, 10 pairs are green. The socks are all mixed up and the room is totally dark. What is the smallest number of socks you must remove to be sure that you have at least one matching pair?

**Solution.**
**Pigeons:** socks removed. **Holes:** the 30 different pairs (10 red + 10 blue + 10 green).
Worst case: pick one sock from each different pair — that is 30 socks, all from different pairs, with no matching pair.
The 31st sock must match one of the 30 already taken. By the Pigeonhole Principle (Generalized), with 31 pigeons and 30 holes, $\lceil 31/30\rceil = 2$: at least one hole gets 2 socks, forming a matching pair.

$$\boxed{31}$$

---

**86.** Prove that if 5 points are placed anywhere on or in a square of side length 1, at least two points will be no farther apart than $\frac{\sqrt{2}}{2}$.

**Solution.**
**(Pigeonhole Principle)**
Step 1. Divide the unit square into 4 congruent smaller squares, each of side length $\frac{1}{2}$ (by drawing the two midlines).
Step 2. **Pigeons:** the 5 points. **Holes:** the 4 small squares.
Step 3. By the Pigeonhole Principle, at least $\lceil 5/4\rceil = 2$ points lie in the same small square.
Step 4. In a square of side $\frac{1}{2}$, the maximum distance between any two points is the diagonal: $\sqrt{(\frac{1}{2})^2+(\frac{1}{2})^2}=\sqrt{\frac{1}{2}}=\frac{\sqrt{2}}{2}$.
Step 5. Therefore, those two points are at distance at most $\frac{\sqrt{2}}{2}$.

$$\boxed{\text{Proven by dividing the square into 4 smaller squares}}$$

---

**87.** Prove that if 5 points are placed anywhere on or in an equilateral triangle of side length 1, at least two points will be no farther apart than $\frac{1}{2}$.

**Solution.**
**(Pigeonhole Principle)**
Step 1. Divide the equilateral triangle into 4 congruent smaller equilateral triangles of side length $\frac{1}{2}$ by connecting the midpoints of the three sides.
Step 2. **Pigeons:** the 5 points. **Holes:** the 4 small triangles.
Step 3. By the Pigeonhole Principle, at least $\lceil 5/4\rceil = 2$ points lie in the same small equilateral triangle.
Step 4. In an equilateral triangle of side $\frac{1}{2}$, the maximum distance between any two points is the side length $\frac{1}{2}$ (any two points are within the closure of the triangle, whose diameter equals the side length).
Step 5. Therefore, those two points are at distance at most $\frac{1}{2}$.

$$\boxed{\text{Proven by dividing into 4 smaller equilateral triangles}}$$

---

**88.** Show that among any $n+1$ positive integers not exceeding $2n$ there must be an integer that divides one of the other integers.

**Solution.**
**(Pigeonhole Principle)**
Step 1. Write each integer in the form $a = 2^k \cdot m$ where $m$ is odd (extract the largest power of 2 factor). Here $m$ is the "odd part" of $a$.
Step 2. Since $a \le 2n$, we have $m \le 2n$. The odd part $m$ must be an odd integer from $\{1,3,5,\dots,2n-1\}$, i.e., one of the $n$ odd positive integers not exceeding $2n$.
Step 3. **Pigeons:** the $n+1$ chosen integers. **Holes:** the $n$ possible odd parts.
Step 4. By the Pigeonhole Principle, at least two integers $a_1$ and $a_2$ share the same odd part $m$. Write $a_1 = 2^{k_1}m$, $a_2 = 2^{k_2}m$ with $k_1 \neq k_2$.
Step 5. Without loss, assume $k_1 < k_2$. Then $a_1 \mid a_2$ because $a_2 = 2^{k_2-k_1} \cdot a_1$.
Thus, one divides the other.

$$\boxed{\text{Proven by writing each integer as }2^k\cdot(\text{odd})}$$

---

**89.** Show that if seven integers are selected from the first 10 positive integers, there must be at least two pairs of these integers with the sum 11. Is the conclusion true if six integers are selected rather than seven?

**Solution.**
**(Pigeonhole Principle)**
Step 1. Partition $\{1,2,\dots,10\}$ into 5 pairs that sum to 11:
$$\{1,10\},\;\{2,9\},\;\{3,8\},\;\{4,7\},\;\{5,6\}$$
Step 2. **Pigeons:** the 7 selected integers. **Holes:** the 5 pairs.
Step 3. By the Pigeonhole Principle, $\lceil 7/5\rceil = 2$: some hole must contain at least 2 of the selected integers. But each hole can contain at most 2 integers (since there are only 2 in each pair). With 7 pigeons in 5 holes, the only way to avoid any hole getting 2 is to have at most 5 pigeons (one per hole). With 7, we need $7 = 5 + 2$ extra pigeons beyond one per hole. Actually: the number of "extra" pigeons beyond one per hole is $7-5=2$. These 2 extra must go into holes, forcing at least $\lceil (7-5)/5 \rceil$ holes to be full? No — more precisely: if each hole has at most 1 selected integer, we can select at most 5 integers. Since we selected 7, at least 2 holes must contain **both** members. Thus we get at least 2 pairs summing to 11.

Step 4. **For 6 integers:** We can select one from each of the 5 holes (5 integers) and one more from any hole, making exactly 1 full hole and 1 partial hole. This gives exactly 1 pair summing to 11, not necessarily 2. Counterexample: $\{1,2,3,4,5,10\}$. Pairs summing to 11: $\{1,10\}$ only. So the conclusion is **false** for 6 integers.

$$\boxed{\text{True for 7; false for 6 (counterexample: }\{1,2,3,4,5,10\})}$$

---

**90.** Show that if you pick seven numbers from the set of consecutive integers from 2 to 13, then you can always find two of them whose sum is exactly 15.  

**Solution.**
**(Pigeonhole Principle)**
Step 1. The set is $\{2,3,4,\dots,13\}$ (12 numbers). Partition into 6 pairs summing to 15:
$$\{2,13\},\;\{3,12\},\;\{4,11\},\;\{5,10\},\;\{6,9\},\;\{7,8\}$$
Step 2. **Pigeons:** the 7 selected integers. **Holes:** the 6 pairs.
Step 3. By the Pigeonhole Principle, $\lceil 7/6\rceil = 2$: at least two selected integers must fall into the same hole. Since each hole is a pair of numbers summing to 15, those two selected integers sum to 15.

$$\boxed{\text{Proven via 6 holes (pairs summing to 15) and 7 pigeons}}$$

---

**91.** There are 12 chairs in a row, and 9 people sitting. Prove that there are 3 consecutive chairs occupied.

**Solution.**
**(Pigeonhole Principle)**
Step 1. Divide the 12 chairs into 4 disjoint groups of 3 consecutive chairs:
$$\{1,2,3\},\;\{4,5,6\},\;\{7,8,9\},\;\{10,11,12\}$$
Step 2. **Pigeons:** the 9 occupied chairs (people). **Holes:** the 4 groups.
Step 3. By the Pigeonhole Principle, $\lceil 9/4\rceil = 3$: at least one group contains 3 occupied chairs. That group consists of 3 consecutive chairs, all occupied.

$$\boxed{\text{Proven by dividing 12 chairs into 4 groups of 3}}$$

---

**92.** Prove that every sequence of $n^2+1$ distinct real numbers contains a subsequence of length $n+1$ that is either strictly increasing or strictly decreasing.

**Solution.**
**(Pigeonhole Principle — Erdős–Szekeres Theorem)**

Step 1. For each term $a_i$ in the sequence, define the ordered pair $(\ell_i, d_i)$ where:
- $\ell_i$ = length of the longest increasing subsequence ending at $a_i$.
- $d_i$ = length of the longest decreasing subsequence ending at $a_i$.

Step 2. **Claim:** All $n^2+1$ ordered pairs are distinct.
If $i<j$ and $a_i<a_j$, then $\ell_j \ge \ell_i+1$, so $(\ell_i,d_i)\neq(\ell_j,d_j)$ (the first coordinates differ). If $a_i>a_j$, then $d_j \ge d_i+1$, so the second coordinates differ. Since all $a_i$ are distinct, $a_i\neq a_j$, so the pairs are always distinct.

Step 3. **Pigeons:** the $n^2+1$ distinct ordered pairs $(\ell_i,d_i)$. **Holes:** the Cartesian product $\{1,2,\dots,M_\ell\}\times\{1,2,\dots,M_d\}$ where $M_\ell, M_d$ are maximum possible values.

Step 4. If no increasing subsequence of length $n+1$ exists, then $\ell_i\le n$ for all $i$. Similarly, if no decreasing subsequence of length $n+1$ exists, then $d_i\le n$ for all $i$.
In that case, all $(\ell_i,d_i)$ belong to the set $\{1,\dots,n\}\times\{1,\dots,n\}$, which has size $n^2$.

Step 5. But we have $n^2+1$ distinct pairs drawn from a set of size $n^2$. By the Pigeonhole Principle, this is impossible. Contradiction.
Therefore, either some $\ell_i\ge n+1$ (an increasing subsequence of length $n+1$ exists) or some $d_i\ge n+1$ (a decreasing subsequence of length $n+1$ exists).

$$\boxed{\text{Proven via Erdős–Szekeres Theorem}}$$




---

## 2. Advanced Counting Rules

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


---

## 3. Graphs

# Sect.3 Graphs — Full Solutions

---

**1.** Investigate the existence of an Eulerian/Hamiltonian cycle on $C_n$, $W_n$, $K_n$, $K_{m,n}$, $Q_n$.

**Solution.**

**Recall (Euler's Theorem).** Let $G$ be a connected graph.
- $G$ has an **Eulerian circuit** iff every vertex has even degree.
- $G$ has an **Eulerian path** (non-circuit) iff exactly two vertices have odd degree (the path starts at one odd-degree vertex and ends at the other).
- If more than two vertices have odd degree, $G$ has **neither**.

**Recall (Hamiltonian sufficient conditions — Dirac, Ore).**
- **Dirac's Theorem:** If $G$ is a simple graph on $n\ge3$ vertices and $\deg(v)\ge n/2$ for every vertex $v$, then $G$ has a Hamiltonian circuit.
- **Ore's Theorem:** If $G$ is a simple graph on $n\ge3$ vertices and for every pair of non-adjacent vertices $u,v$, $\deg(u)+\deg(v)\ge n$, then $G$ has a Hamiltonian circuit.
- These are sufficient but not necessary. For special graphs we can often construct cycles directly or derive necessary conditions.

We now examine each graph family.

---

**$C_n$ (Cycle on $n$ vertices, $n\ge3$).**

Step 1. $v=n$, $e=n$. Every vertex has degree $2$ (even).

Step 2. **Eulerian:** All degrees even $\Rightarrow$ Eulerian circuit **always exists** (the cycle itself). Eulerian path also always exists (every circuit is a path).

Step 3. **Hamiltonian:** $C_n$ **is** a Hamiltonian cycle, so a Hamiltonian circuit (and path) **always exists**.

$$\boxed{\begin{aligned}C_n &: \text{Euler circuit: } \textbf{always} &&\text{Euler path (non-circuit): } \textbf{never}\\
&\text{Hamilton circuit: } \textbf{always} &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**$W_n$ (Wheel on $n+1$ vertices, $n\ge3$).**

Step 1. $v=n+1$, $e=2n$. Structure: one hub vertex $h$ connected to all $n$ rim vertices $r_1,\dots,r_n$, and the rim forms an $n$-cycle $r_1— r_2—\cdots— r_n— r_1$.

Step 2. Degrees: $\deg(h)=n$, $\deg(r_i)=3$ for all $i$ (connected to two rim neighbors and the hub).

Step 3. **Eulerian:** Every rim vertex has odd degree $3$. So there are $n$ odd-degree rim vertices. Additionally, if $n$ is odd, $h$ also has odd degree, giving $n+1$ odd vertices. In all cases for $n\ge3$, the number of odd-degree vertices is at least $n\ge3>2$. Hence **no Eulerian circuit or path exists** for $W_n$ when $n\ge3$.
(For $n=2$, $W_2\cong K_3$, which has $3$ vertices all degree $2$; $K_3$ has an Eulerian circuit because all degrees are even. But $W_n$ is standard for $n\ge3$.)

Step 4. **Hamiltonian:** The wheel always has a Hamiltonian circuit: start at $h$, go around all rim vertices $r_1\to r_2\to\cdots\to r_n$, and return to $h$. Thus a Hamiltonian circuit and path **always exist** for $W_n$ ($n\ge3$).

$$\boxed{\begin{aligned}W_n &: \text{Euler circuit: } \textbf{never }(n\ge3) &&\text{Euler path (non-circuit): } \textbf{never }(n\ge3)\\
&\text{Hamilton circuit: } \textbf{always} &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**$K_n$ (Complete graph on $n$ vertices).**

Step 1. $v=n$, $e=C(n,2)$. Every vertex has degree $n-1$.

Step 2. **Eulerian:**
- Eulerian circuit: all degrees $n-1$ must be even $\Rightarrow$ $n$ is **odd** ($n=1,3,5,\dots$). For $n=1$, the trivial graph has an Eulerian circuit (a walk of length $0$).
- Eulerian path (non-circuit): exactly $2$ odd-degree vertices needed. Since all vertices have the same degree, this requires $n=2$ ($K_2$ has two vertices both degree $1$, exactly $2$ odd $\Rightarrow$ path exists, not circuit).
- For $n\ge4$ and $n$ even: $n$ odd-degree vertices, $n\ge4$, so **neither** exists.

Summary:
- $K_n$ has Euler circuit iff $n$ is odd.
- $K_n$ has Euler path (non-circuit) iff $n=2$.
- Otherwise ($n\ge4$ even), neither exists.

Step 3. **Hamiltonian:** For $n\ge3$, $K_n$ obviously contains a Hamiltonian circuit (any permutation of vertices forms one). For $n=1,2$: $K_1$ has a trivial Hamiltonian circuit; $K_2$ has a Hamiltonian path but only a circuit if we allow returning along the same edge (not in a simple graph, so $K_2$ has no Hamiltonian circuit in the strict cycle sense, but $K_2$ does have a Hamiltonian path). For $n\ge3$, both circuit and path always exist.

$$\boxed{\begin{aligned}K_n &: \text{Euler circuit: } n \text{ is odd} &&\text{Euler path (non-circuit): } n=2\\
&\text{Hamilton circuit: } \textbf{always }(n\ge3) &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**$K_{m,n}$ (Complete bipartite graph).**

Step 1. $v=m+n$, $e=mn$. Vertices in part $A$ (size $m$) each have degree $n$; vertices in part $B$ (size $n$) each have degree $m$.

Step 2. **Eulerian:**
- Every vertex in $A$ has degree $n$; every vertex in $B$ has degree $m$.
- Eulerian circuit: all degrees even $\Rightarrow$ $m$ even **and** $n$ even.
- Eulerian path (non-circuit): exactly $2$ odd-degree vertices.
  - If $n$ is even and $m$ is odd: the $n$ vertices in part $B$ each have odd degree $m$. So there are $n$ odd-degree vertices. For exactly $2$, we need $n=2$. Thus $K_{m,2}$ with $m$ odd has an Eulerian path.
  - If $m$ is even and $n$ is odd: similarly, $m$ odd-degree vertices in $A$ $\Rightarrow$ need $m=2$. Thus $K_{2,n}$ with $n$ odd has an Eulerian path.
  - If both $m,n$ are odd: $m+n$ odd-degree vertices (all vertices are odd). $m+n$ is even. For exactly $2$, $m+n=2$, i.e. $m=n=1$ ($K_{1,1}\cong K_2$), which is already covered.
- Otherwise, more than $2$ odd-degree vertices $\Rightarrow$ **neither**.

Summary for Eulerian:
- Circuit: $m$ even **and** $n$ even.
- Path (non-circuit): $\{m=2,\;n\text{ odd}\}$ or $\{n=2,\;m\text{ odd}\}$.
- Neither: otherwise.

Step 3. **Hamiltonian:**
- $K_{m,n}$ is bipartite. A Hamiltonian circuit must alternate between the two partite sets, so necessarily $|A|=|B|$, i.e. $m=n$.
  - If $m=n\ge2$, a Hamiltonian circuit exists: label vertices $a_1,\dots,a_n$ and $b_1,\dots,b_n$, trace $a_1— b_1— a_2— b_2—\cdots— a_n— b_n— a_1$.
  - If $m=n=1$, $K_{1,1}\cong K_2$: a Hamiltonian path exists but no circuit (simple graph requires at least $3$ vertices for a cycle).
- Hamiltonian path: must alternate, so the part sizes can differ by at most $1$. Thus $|m-n|\le 1$ is necessary and sufficient.
  - If $|m-n|\le 1$, a Hamiltonian path exists.
  - If $|m-n|\ge 2$, no Hamiltonian path (you would run out of vertices in one part before alternating completes).

$$\boxed{\begin{aligned}K_{m,n} &: \text{Euler circuit: } m,n \text{ both even} &&\text{Euler path (non-circuit): } \{m=2,n\text{ odd}\}\cup\{n=2,m\text{ odd}\}\\
&\text{Hamilton circuit: } m=n\ge2 &&\text{Hamilton path: } |m-n|\le 1\end{aligned}}$$

---

**$Q_n$ ($n$-dimensional hypercube).**

Step 1. $v=2^n$, $e=n\cdot2^{n-1}$. Every vertex has degree $n$.

Step 2. **Eulerian:**
- All $2^n$ vertices share the same degree $n$.
- Eulerian circuit: all degrees even $\Rightarrow$ $n$ **even** ($n=2,4,6,\dots$).
- Eulerian path (non-circuit): exactly $2$ odd-degree vertices. This requires $2^n=2$, i.e. $n=1$ ($Q_1\cong K_2$). For $n\ge3$ odd, $2^n\ge8>2$ odd-degree vertices, so **neither**.
- For $n=0$, $Q_0$ is a single vertex (trivial, has Eulerian circuit of length $0$).

Step 3. **Hamiltonian:**
- For $n\ge2$, $Q_n$ always has a Hamiltonian circuit (well-known; construable via Gray codes). For $n=1$, $Q_1=K_2$ has a Hamiltonian path but no circuit ($v=2$). For $n=0$, trivial.

$$\boxed{\begin{aligned}Q_n &: \text{Euler circuit: } n \text{ even} &&\text{Euler path (non-circuit): } n=1\\
&\text{Hamilton circuit: } \textbf{always }(n\ge2) &&\text{Hamilton path: } \textbf{always}\end{aligned}}$$

---

**2.** Propose an algorithm for finding an Eulerian circuit of a given graph. What is the complexity of that algorithm?

**Solution.**

We present **Hierholzer's Algorithm**, which is more efficient.

**Theorem (Euler).** A connected graph has an Eulerian circuit iff every vertex has even degree. Hierholzer's algorithm assumes this condition holds.

**Algorithm (Hierholzer, 1873):**

Step 1. Choose any starting vertex $v_0$. Initialize a stack $S$ and a list $C$ (the circuit).

Step 2. Push $v_0$ onto $S$. While $S$ is non-empty:
- Let $u$ be the top vertex of $S$.
- If $\deg(u)>0$ (i.e., $u$ still has unused incident edges):
  - Choose any incident edge $e=\{u,w\}$.
  - Remove $e$ from the graph.
  - Push $w$ onto $S$.
- Else ($\deg(u)=0$):
  - Pop $u$ from $S$ and append $u$ to $C$.

Step 3. When the stack is empty, $C$ contains the vertices in the order of an Eulerian circuit (in reverse). Reverse $C$ to obtain the circuit starting at $v_0$.

**Complexity:** $O(|V|+|E|)$. Each edge is traversed and removed exactly once; each vertex is pushed and popped at most once.

**Fleury's Algorithm (alternative, $O(|E|^2)$ naive):**
At each step, traverse an edge that is **not a bridge** in the remaining graph (unless no other choice exists). This avoids disconnecting the graph prematurely. Fleury's algorithm can be implemented in $O(|E|^2)$ with naive bridge-detection, or $O(|E|\log|V|)$ with more sophisticated data structures.

**Complexity comparison:** Hierholzer's algorithm runs in linear time $O(|V|+|E|)$ and is the preferred method.

$$\boxed{\text{Hierholzer's Algorithm: } O(|V|+|E|);\quad \text{Fleury's Algorithm: } O(|E|^2)}$$

---

**3.** Show that a bipartite graph with an odd number of vertices does not have a Hamiltonian cycle.

**Solution.**

Step 1. Let $G=(V,E)$ be a bipartite graph with bipartition $(V_1,V_2)$, so $V=V_1\cup V_2$, $V_1\cap V_2=\emptyset$, and every edge joins a vertex of $V_1$ to a vertex of $V_2$.

Step 2. Suppose for contradiction that $G$ has a Hamiltonian cycle $C$. A Hamiltonian cycle visits every vertex exactly once and returns to the start.

Step 3. Along the cycle $C$, vertices must **alternate** between $V_1$ and $V_2$, because every edge of $G$ (hence every edge of $C$) joins a vertex from $V_1$ to a vertex from $V_2$.

Step 4. Alternation forces the cycle to have equal numbers of vertices from each part: $|V_1|=|V_2|$.

Step 5. Therefore $|V|=|V_1|+|V_2|=2|V_1|$ is **even**. This contradicts the hypothesis that $|V|$ is odd.

Step 6. Hence no Hamiltonian cycle can exist.

$$\boxed{\text{A bipartite graph with an odd number of vertices has no Hamiltonian cycle.}}$$

---

**4.** A diagnostic message can be sent out over a computer network to perform tests over all links and in all devices. What sort of paths should be used to test
a. all links?
b. all devices?

**Solution.**

**(a) Testing all links (edges):**
Testing every link exactly once corresponds to traversing every edge of the network graph exactly once — this is an **Eulerian path** (or Eulerian circuit if the walk returns to the start). The test message should follow an Eulerian trail that traverses each communication link exactly once.

**(b) Testing all devices (vertices):**
Testing every device exactly once corresponds to visiting every vertex of the network graph exactly once — this is a **Hamiltonian path** (or Hamiltonian circuit if returning to start). The test message should follow a Hamiltonian path that visits each device exactly once.

$$\boxed{\begin{aligned}\text{(a) All links: } &\textbf{Eulerian path (or circuit)}\\
\text{(b) All devices: } &\textbf{Hamiltonian path (or circuit)}\end{aligned}}$$

---

**5.** Investigate the existence of a Hamiltonian cycle/path on graphs in Exercises 30–36 (Chapter 10.5, Rosen's textbook).

**Solution.**

*General methodology for investigating Hamiltonian existence:*

Step 1. Compute $n=|V|$, the degree of each vertex, and check sufficient conditions:

- **Dirac's Theorem:** If every vertex has $\deg(v)\ge n/2$, a Hamiltonian circuit exists.
- **Ore's Theorem:** If for every pair of non-adjacent $u,v$, $\deg(u)+\deg(v)\ge n$, a Hamiltonian circuit exists.
- If either condition holds, the answer is **yes**.

Step 2. If neither sufficient condition holds, attempt **direct construction**:
- Try to trace a cycle visiting all vertices exactly once. For small graphs, this is feasible by inspection.
- For bipartite graphs: check partite set sizes. If $|V_1|\neq|V_2|$, no Hamiltonian circuit exists; a Hamiltonian path requires $||V_1|-|V_2||\le 1$.

Step 3. To prove **non-existence** when construction fails:
- Look for a **cut-vertex** whose removal disconnects the graph into $k\ge2$ components — a Hamiltonian cycle would need to enter and leave each component, which is impossible if a vertex is visited only once.
- Look for a **degree obstruction**: if any vertex has degree $1$, it cannot be on a Hamiltonian circuit (though it could be an endpoint of a Hamiltonian path).

Step 4. For the specific graphs in Rosen Exercises 30–36 (Chapter 10.5), apply the above methodology to each. The typical graphs include variations of grids, bipartite graphs, and graphs with degree patterns that require case-by-case analysis. For bipartite graphs with unequal parts, no Hamiltonian circuit exists; check $|m-n|\le 1$ for Hamiltonian path.

$$\boxed{\text{Methodology: Dirac/Ore sufficient conditions } \to \text{ direct construction } \to \text{ structural obstruction}}$$

---

**6.** Investigate the existence of an Eulerian cycle/path on graphs in Exercises 13–14, 18–22 (Chapter 10.5, Rosen's textbook).

**Solution.**

*General methodology for investigating Eulerian existence:*

Step 1. Compute the degree of every vertex in the graph.

Step 2. Apply **Euler's Theorem**:
- If **every** vertex has even degree, an **Eulerian circuit** exists (start anywhere).
- If **exactly two** vertices have odd degree, an **Eulerian path** (non-circuit) exists and must start at one odd-degree vertex and end at the other.
- If more than two vertices have odd degree, **neither** exists.

Step 3. Additionally, the graph must be **connected** (or all edges must belong to a single connected component — isolated vertices with no edges are irrelevant). If the graph is disconnected and edges exist in multiple components, no Eulerian trail covering all edges exists.

Step 4. For directed graphs: Eulerian circuit exists iff $\deg^+(v)=\deg^-(v)$ for every vertex $v$; Eulerian path exists iff exactly one vertex has $\deg^+-\deg^-=1$ (start) and exactly one has $\deg^--\deg^+=1$ (end), with all others balanced.

Step 5. Apply this check to each of the graphs in Rosen Exercises 13–14, 18–22: compute degree sequences, count odd-degree vertices, and conclude.

$$\boxed{\text{Methodology: count odd-degree vertices; } 0 \Rightarrow \text{circuit, } 2 \Rightarrow \text{path, } >2 \Rightarrow \text{neither}}$$

---

**7.** Construct a Gray code of $n$ contacts.

**Solution.**

A Gray code of $n$ bits is a cyclic ordering of all $2^n$ binary strings of length $n$ such that consecutive strings differ in exactly one bit. Equivalently, it is a Hamiltonian circuit on $Q_n$.

**Construction by induction on $n$:**

Step 1. **Base case $n=1$:** The Gray code of $1$ bit is $[0,\;1]$. Consecutive strings differ in exactly one bit, and we may cyclically close by noting $1$ and $0$ differ in one bit.

Step 2. **Induction hypothesis:** Assume we have a Gray code $G_{n-1}=[g_1,g_2,\dots,g_{2^{n-1}}]$ for $n-1$ bits, where each $g_i$ is an $(n-1)$-bit string, consecutive strings differ in one bit, and $g_1$ and $g_{2^{n-1}}$ differ in one bit.

Step 3. **Induction step:** Construct $G_n$ from $G_{n-1}$ as follows:
- **Forward pass:** Prepend a $0$ to each string in $G_{n-1}$. This gives the first half: $[0g_1,\;0g_2,\;\dots,\;0g_{2^{n-1}}]$.
- **Reverse pass:** Prepend a $1$ to each string in the **reverse** of $G_{n-1}$ (i.e., $[g_{2^{n-1}},\dots,g_2,g_1]$). This gives the second half: $[1g_{2^{n-1}},\;\dots,\;1g_2,\;1g_1]$.

The concatenated sequence has length $2\cdot2^{n-1}=2^n$, covering all $n$-bit strings.

Step 4. **Verification of the one-bit-difference property:**
- Within each half, consecutive strings differ in one bit (by induction hypothesis, since the same prefix bit is attached).
- At the **junction** between the two halves: $0g_{2^{n-1}}$ and $1g_{2^{n-1}}$ differ only in the first (new) bit.
- At the **cyclic junction** (wrap-around from $1g_1$ back to $0g_1$): these differ only in the first bit.
- At the **middle junction** within the second half (where the reversal happens), consecutiveness is preserved because $G_{n-1}$ was reversed, maintaining the one-bit-difference property in reverse order.

Step 5. By induction, a Gray code exists for all $n\ge1$.

**Example ($n=3$):**
$G_1=[0,1]$.
$G_2=[00,01,11,10]$ (prepend $0$ to $[0,1]$, then prepend $1$ to $[1,0]$).
$G_3=[000,001,011,010,110,111,101,100]$.

$$\boxed{\text{Gray code constructed by induction: } G_n = [0G_{n-1}]\;||\;[1\,\text{rev}(G_{n-1})]}$$

---

**8.** How many faces are there in a tree of $n$ vertices?

**Solution.**

Step 1. A tree $T$ with $n$ vertices is a connected acyclic graph, hence planar (it can be drawn in the plane without edge crossings).

Step 2. For a tree: $|V|=n$, $|E|=n-1$. The tree is connected, so $c=1$.

Step 3. By **Euler's formula** for connected planar graphs: $v-e+f=2$.

Step 4. Substitute: $n-(n-1)+f=2 \;\Longrightarrow\; 1+f=2 \;\Longrightarrow\; f=1$.

Step 5. The single face is the **outer (unbounded) face**. A tree has no cycles, so it cannot enclose any bounded region.

$$\boxed{f=1 \text{ (the outer face)}}$$

---

**9.** Can six houses be connected to two utilities without connections crossing?

**Solution.**

Step 1. Model six houses and two utilities as a complete bipartite graph $K_{6,2}$, where houses are one partite set ($m=6$) and utilities are the other ($n=2$).

Step 2. Compute parameters: $v=m+n=6+2=8$, $e=mn=6\times2=12$.

Step 3. $K_{6,2}$ is bipartite, thus **triangle-free** (no cycle of length $3$ is possible in a bipartite graph). Apply the triangle-free planar edge bound:

$$e\le 2v-4$$

Step 4. Compute $2v-4=2\cdot8-4=16-4=12$. Since $e=12\le12$, the bound is **not violated**.

Step 5. The bound is necessary but not sufficient. However, $K_{n,2}$ is known to be planar for **all** $n$. We can draw it: place the $2$ utility vertices on a horizontal line, place the $6$ houses in an arc above (or on both sides), and connect each house to each utility without crossings (all edges are straight-line segments if houses are positioned appropriately).

Step 6. Thus six houses **can** be connected to two utilities without crossings.

$$\boxed{\text{Yes; } K_{6,2} \text{ is planar (e.g. via a planar embedding of } K_{n,2} \text{ for any } n)}$$

---

**10.** Are $Q_4$, $Q_5$, $Q_6$ planar?

**Solution.**

Recall for $Q_n$ (the $n$-dimensional hypercube): $v=2^n$, $e=n\cdot2^{n-1}$.

**$Q_4$:**

Step 1. $v=2^4=16$, $e=4\cdot2^3=32$.

Step 2. Apply the general planar edge bound: $e\le3v-6$.

$$3v-6=3\cdot16-6=48-6=42.$$

Since $e=32\le42$, the bound is **not violated** — the bound test is inconclusive.

Step 3. By **Kuratowski's Theorem**, a graph is non-planar iff it contains a subdivision of $K_5$ or $K_{3,3}$. It is a known result that $Q_4$ contains a subdivision of $K_{3,3}$ (for example, vertices $\{0000,0011,0101,0110\}$ can be shown to form one part with paths through the hypercube to vertices in another appropriately chosen set). Therefore $Q_4$ is **non-planar**.

Step 4. Alternatively, $Q_4$ has genus $1$ (requires a torus for embedding without crossings), which directly implies non-planarity.

Thus $Q_4$ is **not planar**.

**$Q_5$:**

Step 1. $Q_5$ contains $Q_4$ as a subgraph (by fixing any one coordinate). Since $Q_4$ is non-planar, any supergraph is also non-planar.

Step 2. Alternatively, $v=2^5=32$, $e=5\cdot2^4=80$. Bound: $3v-6=96-6=90\ge80$ — inconclusive, but the subgraph argument suffices.

Thus $Q_5$ is **not planar**.

**$Q_6$:**

Step 1. $v=2^6=64$, $e=6\cdot2^5=6\cdot32=192$.

Step 2. Apply the edge bound: $3v-6=3\cdot64-6=192-6=186$.

Step 3. $e=192>186$. The bound is **violated**. By the necessary condition for planarity, $Q_6$ is **non-planar**.

$$\boxed{\begin{aligned}Q_4 &: \textbf{Not planar} \text{ (contains } K_{3,3} \text{ subdivision)}\\
Q_5 &: \textbf{Not planar} \text{ (contains } Q_4 \text{ as subgraph)}\\
Q_6 &: \textbf{Not planar} \text{ (} e=192 > 3v-6=186 \text{)}\end{aligned}}$$

---

**11.** Prove that if $G$ is a connected and planar graph, then $G$ has a vertex of degree not exceeding five.

**Solution.**

Step 1. Let $G$ be a connected planar simple graph with $v\ge3$ vertices and $e$ edges. By the general planar edge bound:

$$e\le 3v-6.$$

Step 2. By the **Handshaking Lemma**:

$$\sum_{i=1}^{v}\deg(v_i)=2e.$$

Step 3. Suppose, for contradiction, that every vertex has degree at least $6$, i.e., $\deg(v_i)\ge6$ for all $i=1,\dots,v$.

Step 4. Then:

$$2e=\sum_{i=1}^{v}\deg(v_i)\ge\sum_{i=1}^{v}6=6v\;\Longrightarrow\;e\ge3v.$$

Step 5. Combine with the planar bound:

$$3v\le e\le 3v-6\;\Longrightarrow\;3v\le3v-6\;\Longrightarrow\;0\le-6,$$

which is a contradiction.

Step 6. Therefore, the assumption that all vertices have degree $\ge6$ is false. Hence $G$ must have at least one vertex of degree $\le5$.

(For $v=1,2$, the statement is trivially true as the maximum possible degree is $v-1\le1$.)

$$\boxed{\text{Every connected planar graph has a vertex of degree } \le 5.}$$

---

**12.** Suppose that a connected planar graph has 20 vertices, each of degree 3. Into how many regions does a representation of this planar graph split the plane?

**Solution.**

Step 1. Given: $v=20$ vertices, each of degree $3$. The graph is connected and planar.

Step 2. By the **Handshaking Lemma**:

$$\sum_{v\in V}\deg(v)=2e\;\Longrightarrow\;20\cdot3=60=2e\;\Longrightarrow\;e=30.$$

Step 3. By **Euler's formula** for a connected planar graph:

$$v-e+f=2.$$

Step 4. Substitute:

$$20-30+f=2\;\Longrightarrow\;-10+f=2\;\Longrightarrow\;f=12.$$

Step 5. Thus the representation splits the plane into $12$ regions (faces).

$$\boxed{f=12 \text{ regions}}$$

---

**13.** Is the Petersen graph planar?

**Solution.**

Step 1. The Petersen graph has $v=10$ vertices and $e=15$ edges.

Step 2. Apply the edge bound: $3v-6=3\cdot10-6=24$. Since $e=15\le24$, the bound is **not violated** — the test is inconclusive.

Step 3. Use **Kuratowski's Theorem**: a graph is non-planar iff it contains a subdivision of $K_5$ or $K_{3,3}$.

Step 4. The Petersen graph is well-known to contain a subdivision of $K_{3,3}$. One explicit construction:

Label the outer $5$-cycle vertices as $a_1,a_2,a_3,a_4,a_5$ (in cyclic order) and the inner $5$-star (pentagram) vertices as $b_1,b_2,b_3,b_4,b_5$, where $b_i$ is connected to $a_i$, $b_{i+2}$ (mod $5$), and $b_{i+1}$ (mod $5$) in the pentagram arrangement.

Then identify two sets of three vertices, e.g. $\{a_1,a_3,b_2\}$ and $\{a_2,a_4,b_5\}$. One can find six internally vertex-disjoint paths connecting each vertex of the first set to each vertex of the second set, forming a $K_{3,3}$ subdivision.

Step 5. Since the Petersen graph contains a $K_{3,3}$ subdivision, by Kuratowski's Theorem it is **non-planar**.

$$\boxed{\text{The Petersen graph is } \textbf{not planar} \text{ (contains a } K_{3,3} \text{ subdivision)}.}$$

---

**14.** Are $K_{3,4}$, $K_6$ planar?

**Solution.**

**$K_{3,4}$:**

Step 1. $K_{3,4}$ has $v=3+4=7$ vertices, $e=3\cdot4=12$ edges.

Step 2. $K_{3,4}$ is bipartite, hence **triangle-free** (containing no $3$-cycle). Apply the triangle-free planar edge bound:

$$e\le 2v-4.$$

Step 3. Compute: $2v-4=2\cdot7-4=14-4=10$. Since $e=12>10$, the bound is **violated**.

Step 4. Therefore $K_{3,4}$ is **non-planar** (by violation of a necessary condition for planarity of triangle-free graphs).

**$K_6$:**

Step 1. $K_6$ has $v=6$ vertices, $e=C(6,2)=15$ edges.

Step 2. Apply the general planar edge bound: $e\le 3v-6$.

Step 3. Compute: $3v-6=3\cdot6-6=18-6=12$. Since $e=15>12$, the bound is **violated**.

Step 4. Therefore $K_6$ is **non-planar**.

$$\boxed{\begin{aligned}K_{3,4} &: \textbf{Not planar} \text{ (} e=12 > 2v-4=10 \text{)}\\
K_6 &: \textbf{Not planar} \text{ (} e=15 > 3v-6=12 \text{)}\end{aligned}}$$

---

**15.** Show that any connected triangle-free planar graph (i.e., it has no simple cycle of length three) has at least one vertex of degree not exceeding three.

**Solution.**

Step 1. Let $G$ be a connected, triangle-free, planar simple graph with $v\ge3$ vertices and $e$ edges. Since $G$ is triangle-free, every face in any planar embedding is bounded by at least $4$ edges. Consequently, the tighter planar edge bound applies:

$$e\le 2v-4.$$

Step 2. By the **Handshaking Lemma**:

$$\sum_{i=1}^{v}\deg(v_i)=2e.$$

Step 3. Suppose, for contradiction, that every vertex has degree at least $4$, i.e., $\deg(v_i)\ge4$ for all $i=1,\dots,v$.

Step 4. Then:

$$2e=\sum_{i=1}^{v}\deg(v_i)\ge\sum_{i=1}^{v}4=4v\;\Longrightarrow\;e\ge 2v.$$

Step 5. Combine with the triangle-free planar bound:

$$2v\le e\le 2v-4\;\Longrightarrow\;2v\le2v-4\;\Longrightarrow\;0\le-4,$$

which is a contradiction.

Step 6. Therefore, the assumption that all vertices have degree $\ge4$ is false. Hence $G$ must have at least one vertex of degree $\le3$.

(For $v=1,2$, the statement holds trivially as maximum degree is at most $1$.)

$$\boxed{\text{Every connected triangle-free planar graph has a vertex of degree } \le 3.}$$

---

**16.** Prove by induction on the number of vertices that any connected triangle-free planar graph is $4$-colorable.

**Solution.**

Step 1. **Theorem statement:** Every connected, triangle-free, planar graph $G$ is $4$-colorable (i.e., its vertices can be colored with at most $4$ colors such that adjacent vertices receive different colors).

Step 2. **Base case:** For $v=1$, a single vertex requires only $1$ color. For $v=2$, two adjacent vertices require at most $2$ colors. All small cases ($v\le4$) are trivially $4$-colorable.

Step 3. **Induction hypothesis:** Assume that every connected, triangle-free, planar graph with fewer than $n$ vertices is $4$-colorable.

Step 4. **Induction step:** Let $G$ be a connected, triangle-free, planar graph with $n$ vertices ($n\ge3$). By **Problem 15**, $G$ contains a vertex $v_0$ with $\deg(v_0)\le 3$.

Step 5. Delete $v_0$ (and all incident edges) to obtain $G' = G - v_0$. The graph $G'$:
- Is planar (subgraph of a planar graph).
- Is triangle-free (removing vertices cannot create new $3$-cycles; in fact, a triangle in $G'$ would also be a triangle in $G$, contradicting that $G$ is triangle-free).
- May be disconnected. However, we can apply the induction hypothesis to each connected component of $G'$ separately (each has $< n$ vertices) and combine the colorings. If $G'$ is connected, the induction hypothesis applies directly.

Step 6. By the induction hypothesis, $G'$ is $4$-colorable. Fix a $4$-coloring of $G'$ using colors $\{1,2,3,4\}$.

Step 7. Consider $v_0$ in $G$. Its neighbors in $G$ are at most $3$ vertices (since $\deg(v_0)\le3$). These neighbors are all in $G'$, so they have been colored. At most $3$ colors appear among the neighbors of $v_0$.

Step 8. Since only $4$ colors are available and at most $3$ are used by $v_0$'s neighbors, there is at least one color $c\in\{1,2,3,4\}$ **not** used by any neighbor of $v_0$. Assign color $c$ to $v_0$.

Step 9. This extends the $4$-coloring of $G'$ to a valid $4$-coloring of $G$, completing the induction.

**Remark.** The stronger statement — that every connected triangle-free planar graph is **$3$-colorable** — is **Grötzsch's Theorem** (a deep result). The problem asks only for $4$-colorability, which follows easily from the existence of a vertex of degree $\le3$ (Problem 15) and induction.

$$\boxed{\text{Proved by induction: delete a vertex of degree } \le 3, \text{ 4-color the remainder, and color the deleted vertex.}}$$


---

## 4. Trees

# Sect.4 Trees — Full Solutions

---

**1.** Given the rooted tree (root $d$; children of $d$: $a,c,o,i$; children of $c$: $b,k,g$; children of $b$: $h,l$; children of $i$: $f$; children of $f$: $e,m,n$; children of $h$: $p,q$):

**Solution.**
Step 1. Draw the tree structure explicitly:
- Level 0: $d$
- Level 1: $a,c,o,i$ (children of $d$)
- Level 2: $b,k,g$ (children of $c$); $f$ (child of $i$)
- Level 3: $h,l$ (children of $b$); $e,m,n$ (children of $f$)
- Level 4: $p,q$ (children of $h$)

**(a)** The designated top vertex with no parent is $d$.

**(b)** Internal vertices have at least one child: $d,c,b,h,i,f$. (6 vertices)

**(c)** Leaves have no children: $a,o,k,g,l,e,m,n,p,q$. (10 vertices)

**(d)** Level 3 vertices (distance 3 from root): $h,l,e,m,n$.

**(e)** Height of subtree rooted at $c$: longest path $c\to b\to h\to p$ has 3 edges, so height = 3.

**(f)** Descendants of $b$: $h,l$ (children) and $p,q$ (children of $h$). So $\{h,l,p,q\}$.

**(g)** Balanced? Leaves appear at levels 1 ($a,o$), 2 ($k,g$), 3 ($l,e,m,n$), and 4 ($p,q$). Leaf levels differ by more than 1, so **not balanced**.

**(h)** Ancestors of $q$: $h\to b\to c\to d$. So $\{h,b,c,d\}$.

$$\boxed{\begin{aligned}
\text{(a) }&d\\
\text{(b) }&d,c,b,h,i,f\\
\text{(c) }&a,o,k,g,l,e,m,n,p,q\\
\text{(d) }&\{h,l,e,m,n\}\\
\text{(e) }&3\\
\text{(f) }&\{h,l,p,q\}\\
\text{(g) }&\text{Not balanced}\\
\text{(h) }&\{h,b,c,d\}
\end{aligned}}$$

---

**2.** How many non-isomorphic unrooted trees are there with 3 vertices?

**Solution.**
Step 1. Any tree with 3 vertices has $3-1=2$ edges. All such trees are paths $P_3$. There is exactly 1 non-isomorphic tree.

$$\boxed{1 \text{ (the path } P_3\text{)}}$$

---

**3.** How many non-isomorphic unrooted trees are there with 4 vertices?

**Solution.**
Step 1. Trees with 4 vertices have $4-1=3$ edges. Up to isomorphism, only two degree-sequence patterns exist:
- $P_4$ (path, degree sequence $(2,2,1,1)$)
- $K_{1,3}$ (star, degree sequence $(3,1,1,1)$)

Step 2. Any other tree on 4 vertices is isomorphic to one of these two.

$$\boxed{2\text{ (the path }P_4\text{ and the star }K_{1,3}\text{)}}$$

---

**4.** How many leaves does a full 3-ary tree with 100 vertices have?

**Solution.**
Step 1. For a full $m$-ary tree: $n=mi+1$, where $n$ = total vertices, $i$ = internal vertices.
Step 2. $100=3i+1 \Rightarrow 3i=99 \Rightarrow i=33$.
Step 3. Leaves $=n-i=100-33=67$. Equivalently: leaves $=(m-1)i+1=2\cdot33+1=67$.

$$\boxed{67}$$

---

**5.** Either draw a full $m$-ary tree with 84 leaves and height 3, or show that no such tree exists.

**Solution.**
Step 1. For a full $m$-ary tree: leaves $l=84=(m-1)i+1$, so $(m-1)i=83$.
Step 2. Since $83$ is prime, $m-1\in\{1,83\}$, so $m\in\{2,84\}$.
Step 3. Height bound: $l\le m^3$ must hold.
- $m=2$: $2^3=8<84$ (fails).
- $m=84$: satisfies the bound, but $i=1$ gives only 1 internal vertex, so height is at most 1, not 3.
Step 4. No $m$ satisfies all constraints simultaneously.

$$\boxed{\text{No such tree exists.}}$$

---

**6.** Does there exist a full 4-ary tree with 80 leaves?

**Solution.**
Step 1. Leaves $l=80=(4-1)i+1=3i+1$, so $3i=79$.
Step 2. $i=79/3$ is not an integer. Hence no such tree exists.

$$\boxed{\text{No }(3i=79\text{ has no integer solution}).}$$

---

**7.** Does there exist a full $m$-ary tree with height 4 and 100 leaves?

**Solution.**
Step 1. Leaves $l=100=(m-1)i+1$, so $(m-1)i=99$. Divisors of $99$: $1,3,9,11,33,99$. So $m\in\{2,4,10,12,34,100\}$.
Step 2. Height bound: $100\le m^4$.
- $m=2$: $16<100$ (fails). All $m\ge4$ satisfy $m^4\ge256\ge100$.
Step 3. Try $m=4$: $i=99/3=33$ internal vertices. Max internal for height 4 balanced tree: $(4^4-1)/3=85$. Min internal for height 4: 4. Since $4\le33\le85$, **construction is possible**.
Step 4. For $m=4$: build a chain of 4 internal vertices to reach height 4, distribute the remaining 29 internal vertices in levels 1--3. All internal vertices have exactly 4 children. Total leaves $=4\times33-33+1=100$. Such a tree exists.

$$\boxed{\text{Yes, for } m=4 \text{ (33 internal vertices, 100 leaves, height 4).}}$$

---

**8.** Suppose 1000 people enter a chess tournament (single-elimination). How many games must be played?

**Solution.**
Step 1. Each game eliminates exactly one player. To reduce 1000 players to 1 champion, 999 players must be eliminated.
Step 2. Hence exactly 999 games are needed.

$$\boxed{999}$$

---

**9.** How many edges are there in a forest of $k$ trees and $n$ vertices?

**Solution.**
Step 1. Let tree $i$ have $n_i$ vertices; then it has $n_i-1$ edges. And $\sum_{i=1}^{k}n_i=n$.
Step 2. Total edges $=\sum_{i=1}^{k}(n_i-1)=\left(\sum n_i\right)-k=n-k$.

$$\boxed{n-k}$$

---

**10.** Using alphabetical order, construct a binary search tree for the words in the sentence "The quick brown fox jumps over the lazy dog."

**Solution.**
Step 1. Words (in sentence order): the, quick, brown, fox, jumps, over, the, lazy, dog. Ignore duplicate "the".

Step 2. Insert in order using alphabetical comparison:
1. Insert "the" $\to$ root.
2. "quick" $>$ "the" $\to$ right child of "the".
3. "brown" $<$ "the" $\to$ left child of "the".
4. "fox" $<$ "the" $\to$ left; $>$ "brown" $\to$ right child of "brown".
5. "jumps" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $>$ "fox" $\to$ right child of "fox".
6. "over" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $>$ "fox" $\to$ right; $>$ "jumps" $\to$ right child of "jumps".
7. "the" (skip duplicate).
8. "lazy" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $>$ "fox" $\to$ right; $<$ "jumps" $\to$ left child of "jumps".
9. "dog" $<$ "the" $\to$ left; $>$ "brown" $\to$ right; $<$ "fox" $\to$ left child of "fox".

```
        the
       /   \
   brown   quick
   /   \
 dog   fox
       /  \
    lazy  jumps
             \
            over
```

$$\boxed{\text{BST as shown above.}}$$

---

**11.** How many weighings of a balance scale are needed to find a lighter counterfeit coin among four coins? Describe an algorithm.

**Solution.**
Step 1. $l=4$ possible outcomes (which coin is light). Balance scale: $m=3$ outcomes per weighing. Decision tree bound: $h\ge\lceil\log_3 4\rceil=\lceil1.26\rceil=2$.
Step 2. Algorithm:
- **Weighing 1:** Coin 1 vs Coin 2.
  - If 1 lighter $\to$ coin 1 is counterfeit.
  - If 2 lighter $\to$ coin 2 is counterfeit.
  - If balanced $\to$ counterfeit is among $\{3,4\}$.
    - **Weighing 2:** Coin 3 vs Coin 4. The lighter one is counterfeit.
Step 3. Worst case: 2 weighings.

$$\boxed{2\text{ weighings}}$$

---

**12.** How many weighings are needed to find a counterfeit coin among four coins if it may be either heavier or lighter?

**Solution.**
Step 1. $l=4\times2=8$ outcomes (which coin + heavier/lighter). $h\ge\lceil\log_3 8\rceil=\lceil1.89\rceil=2$. Information-theoretically possible ($3^2=9\ge8$).
Step 2. Algorithm:
- **Weighing 1:** Coin 1 vs Coin 2.
  - **Case A (balanced):** 1 and 2 are genuine. Counterfeit is 3 or 4.
    - **Weighing 2:** Coin 3 vs Coin 1 (genuine). If balanced $\to$ Coin 4 is counterfeit. If unbalanced $\to$ Coin 3 is counterfeit.
  - **Case B (Coin 1 heavier):** Possibilities: 1 heavy or 2 light. Coins 3,4 are genuine.
    - **Weighing 2:** Coin 1 vs Coin 3 (genuine). If 1 = 3 $\to$ Coin 2 is counterfeit (light). If 1 heavier $\to$ Coin 1 is counterfeit (heavy).
  - **Case C (Coin 2 heavier):** Symmetric. Weigh 2 vs 3.
Step 3. In all cases, 2 weighings identify the counterfeit.

$$\boxed{2\text{ weighings}}$$

---

**13.** Using a decision tree to classify the given IDs.

**Solution.**
Step 1. The data:

| ID | time | gender | area  | risk |
|----|------|--------|-------|------|
| 1  | 1-2  | male   | urban | low  |
| 2  | 2-7  | male   | rural | high |
| 3  | >7   | female | rural | low  |
| 4  | 1-2  | female | rural | high |
| 5  | >7   | male   | rural | high |
| 6  | 1-2  | male   | rural | high |
| 7  | 2-7  | female | urban | low  |
| 8  | 2-7  | male   | urban | low  |

Step 2. Decision tree (using time first, then gender, then area):

```
                time
           /     |     \
        1-2    2-7     >7
        /        |        \
     gender    gender     gender
     /   \     /   \      /   \
   male  fem male  fem  male  fem
   / \    |   / \   |    |     |
area  high area low low  high  low
/ \       / \
u  r     u   r
|  |     |   |
low high low high
```

**Formal rules:**
- Root: time
  - **1-2:** check gender
    - **male:** check area $\to$ *urban*: low; *rural*: high
    - **female:** $\to$ high
  - **2-7:** check gender
    - **male:** check area $\to$ *urban*: low; *rural*: high
    - **female:** $\to$ low
  - **>7:** check gender
    - **male:** $\to$ high
    - **female:** $\to$ low

Step 3. The tree correctly classifies all 8 training examples.

$$\boxed{\text{Decision tree as described above.}}$$

---

**14.** Decision tree for classifying questions based on attributes L, M, and difficulty D.

**Solution.**
Step 1. The training data:

| L | M | D | Q |
|---|---|---|---|
| 0 | 0 | - | 1 |
| 0 | 0 | + | 2 |
| 0 | 1 | - | 3 |
| 0 | 1 | + | 4 |
| 1 | 0 | - | 5 |
| 1 | 0 | + | 6 |
| 1 | 1 | - | 7 |
| 1 | 1 | + | 8 |

Step 2. Every combination $(L,M)$ appears once with $D=-$ and once with $D=+$. The data is perfectly balanced; no attribute or combination of attributes perfectly separates the classes.

Step 3. The decision tree must check both attributes to reach a leaf:

```
      L
    /   \
   0     1
   |     |
   M     M
  / \   / \
 -/+ -/+ -/+ -/+
```

Each leaf outputs the majority class (here tie: either prediction is arbitrary). The tree has 2 internal nodes: L then M.

Step 4. To classify question 6 ($L=1,M=0,D=+$), the tree checks L (decision 1), then M (decision 2), then reaches a leaf. So **2** decisions are made.

$$\boxed{\text{2 decisions (check both L and M).}}$$

---

**15.** Find the least number of comparisons needed to sort four elements and devise an algorithm.

**Solution.**
Step 1. $l=4!=24$ possible orderings, binary comparisons ($m=2$). Decision tree height: $h\ge\lceil\log_2 24\rceil=\lceil4.585\rceil=5$. At least 5 comparisons are needed.

Step 2. Algorithm achieving exactly 5 comparisons (merge-insertion):
- Let elements be $a,b,c,d$.
1. Compare $a$ and $b$. WLOG $a<b$.
2. Compare $c$ and $d$. WLOG $c<d$. [2 comparisons]
3. Compare $b$ and $d$. WLOG $b<d$. Now $a<b<d$ and $c<d$. [3 comparisons]
4. Compare $c$ and $b$:
   - If $c>b$: $a<b<c<d$ (done, **4 comparisons** total).
   - If $c<b$: go to step 5.
5. Compare $c$ and $a$:
   - If $c<a$: $c<a<b<d$.
   - If $c>a$: $a<c<b<d$. [5 comparisons]

Worst case: 5 comparisons, matching the lower bound.

$$\boxed{5\text{ comparisons; algorithm as described above.}}$$

---

**16.** How many comparisons does the tournament sort use to find the second largest, third largest, ..., $(n-1)$st largest element?

**Solution.**
Step 1. Finding the **maximum** via tournament: $n-1$ comparisons (pairwise matches forming a binary tree of height $\lceil\log_2 n\rceil$).

Step 2. The elements that lost directly to the maximum are at most $\lceil\log_2 n\rceil$ opponents. The **second largest** must be among them; finding it takes $\lceil\log_2 n\rceil-1$ additional comparisons.

Step 3. To find the **$k$-th largest** (for $k\ge3$): after determining the $(k-1)$-st largest, replace it with $-\infty$ in the tournament tree and replay the matches along its path to the root. Each replay takes at most $\lceil\log_2 n\rceil$ comparisons.

Step 4. Therefore:
- Second largest: $\lceil\log_2 n\rceil-1$ additional comparisons (total $n-2+\lceil\log_2 n\rceil$).
- Each subsequent ($3$rd through $n$th): at most $\lceil\log_2 n\rceil$ additional comparisons each.

$$\boxed{\begin{aligned}
\text{2nd largest: }&\lceil\log_2 n\rceil-1\text{ additional}\\
\text{3rd through }n\text{th: }&\text{at most }\lceil\log_2 n\rceil\text{ additional each}
\end{aligned}}$$

---

**17.** Draw the tree whose Prüfer sequence is $(1,1,1,1,6,5)$.

**Solution.**
Step 1. $n=6+2=8$ vertices $\{1,\dots,8\}$. $P=(1,1,1,1,6,5)$. Initial $L=[8]\setminus P=\{2,3,4,7,8\}$.

| Step | smallest in $L$ | connect to (first of $P$) | update |
|------|-----------------|---------------------------|--------|
| 1 | 2 | 1 | remove 2; $P=(1,1,1,6,5)$; 1 still in $P$ |
| 2 | 3 | 1 | remove 3; $P=(1,1,6,5)$ |
| 3 | 4 | 1 | remove 4; $P=(1,6,5)$ |
| 4 | 7 | 1 | remove 7; $P=(6,5)$; 1 not in $P$ $\to$ add 1 to $L$; $L=\{8,1\}$ |
| 5 | 1 | 6 | remove 1; $P=(5)$; 6 not in $P$ $\to$ add 6 to $L$; $L=\{8,6\}$ |
| 6 | 6 | 5 | remove 6; $P=()$ empty; add 5 to $L$; $L=\{8,5\}$ |

Step 2. Connect final two in $L$: $(8,5)$.

Step 3. Edges: $\{2,1\},\{3,1\},\{4,1\},\{7,1\},\{1,6\},\{6,5\},\{8,5\}$.

Tree: vertex 1 is connected to 2,3,4,7,6; 6 to 5; 5 to 8.

```
     2   3   4   7
      \  |   |  /
         1
         |
         6
         |
         5
         |
         8
```

$$\boxed{\text{Edges: }\{2,1\},\{3,1\},\{4,1\},\{7,1\},\{1,6\},\{6,5\},\{8,5\}}$$

---

**18.** Draw the tree whose Prüfer sequence is $(10,9,8,7,6,5,4,3)$.

**Solution.**
Step 1. $n=8+2=10$ vertices. $P=(10,9,8,7,6,5,4,3)$. Initial $L=\{1,2\}$.

| Step | smallest in $L$ | connect to | update |
|------|-----------------|------------|--------|
| 1 | 1 | 10 | remove 1; $P=(9,8,7,6,5,4,3)$; 10 not in $P$ $\to$ add 10; $L=\{2,10\}$ |
| 2 | 2 | 9 | remove 2; $P=(8,7,6,5,4,3)$; add 9; $L=\{10,9\}$ |
| 3 | 9 | 8 | remove 9; $P=(7,6,5,4,3)$; add 8; $L=\{10,8\}$ |
| 4 | 8 | 7 | remove 8; $P=(6,5,4,3)$; add 7; $L=\{10,7\}$ |
| 5 | 7 | 6 | remove 7; $P=(5,4,3)$; add 6; $L=\{10,6\}$ |
| 6 | 6 | 5 | remove 6; $P=(4,3)$; add 5; $L=\{10,5\}$ |
| 7 | 5 | 4 | remove 5; $P=(3)$; add 4; $L=\{10,4\}$ |
| 8 | 4 | 3 | remove 4; $P=()$; add 3; $L=\{10,3\}$ |

Step 2. Connect $\{10,3\}$.

Step 3. Edges: $\{1,10\},\{2,9\},\{9,8\},\{8,7\},\{7,6\},\{6,5\},\{5,4\},\{4,3\},\{10,3\}$.
This is a path: $1-10-3-4-5-6-7-8-9-2$.

$$\boxed{\text{Path: }1-10-3-4-5-6-7-8-9-2}$$

---

**19.** Draw the tree whose Prüfer sequence is $(1,2,3,4,5,6,7,8)$.

**Solution.**
Step 1. $n=8+2=10$. $P=(1,2,3,4,5,6,7,8)$. Initial $L=\{9,10\}$.

| Step | smallest in $L$ | connect to | update |
|------|-----------------|------------|--------|
| 1 | 9 | 1 | remove 9; $P=(2,3,4,5,6,7,8)$; 1 not in $P$ $\to$ add 1; $L=\{10,1\}$ |
| 2 | 1 | 2 | remove 1; $P=(3,4,5,6,7,8)$; add 2; $L=\{10,2\}$ |
| 3 | 2 | 3 | remove 2; $P=(4,5,6,7,8)$; add 3; $L=\{10,3\}$ |
| 4 | 3 | 4 | remove 3; $P=(5,6,7,8)$; add 4; $L=\{10,4\}$ |
| 5 | 4 | 5 | remove 4; $P=(6,7,8)$; add 5; $L=\{10,5\}$ |
| 6 | 5 | 6 | remove 5; $P=(7,8)$; add 6; $L=\{10,6\}$ |
| 7 | 6 | 7 | remove 6; $P=(8)$; add 7; $L=\{10,7\}$ |
| 8 | 7 | 8 | remove 7; $P=()$; add 8; $L=\{10,8\}$ |

Step 2. Connect $\{10,8\}$.

Step 3. Edges: $\{9,1\},\{1,2\},\{2,3\},\{3,4\},\{4,5\},\{5,6\},\{6,7\},\{7,8\},\{10,8\}$.
This is the path: $9-1-2-3-4-5-6-7-8-10$.

$$\boxed{\text{Path: }9-1-2-3-4-5-6-7-8-10}$$

---

**20.** Determine the Prüfer codes for the two given labeled trees.

**Tree 1** (root 1 with children 9,5; 5 has children 2,3,8; 2 has child 6; 8 has child 4; 9 has child 7; 7 has child 10):

**Solution.**
Step 1. Vertices $\{1,\dots,10\}$. Edges: $\{1,9\},\{1,5\},\{5,2\},\{5,3\},\{5,8\},\{2,6\},\{8,4\},\{9,7\},\{7,10\}$.
Degrees: $d_1=2,d_2=2,d_3=1,d_4=1,d_5=4,d_6=1,d_7=2,d_8=2,d_9=2,d_{10}=1$.

Step 2. Leaves initially: $\{3,4,6,10\}$. Encode (10 vertices, 8 steps):

| Step | smallest leaf | neighbor (recorded) | remove leaf | update |
|------|---------------|---------------------|-------------|--------|
| 1 | 3 | **5** | remove 3 | $d_5$ becomes 3 |
| 2 | 4 | **8** | remove 4 | $d_8$ becomes 1 (now leaf) |
| 3 | 6 | **2** | remove 6 | $d_2$ becomes 1 (now leaf) |
| 4 | 2 | **5** | remove 2 | $d_5$ becomes 2 |
| 5 | 8 | **5** | remove 8 | $d_5$ becomes 1 (now leaf) |
| 6 | 5 | **1** | remove 5 | $d_1$ becomes 1 (now leaf) |
| 7 | 1 | **9** | remove 1 | $d_9$ becomes 1 (now leaf) |
| 8 | 9 | **7** | remove 9 | remaining: $\{7,10\}$ |

Prüfer code: $(5,8,2,5,5,1,9,7)$.

**Tree 2** (root 2 with children 3,8; 3 has children 4,7,9; 4 has child 1; 8 has children 6,10; 6 has child 5):

**Solution.**
Step 1. Edges: $\{2,3\},\{2,8\},\{3,4\},\{3,7\},\{3,9\},\{4,1\},\{8,6\},\{8,10\},\{6,5\}$.
Degrees: $d_1=1,d_2=2,d_3=4,d_4=2,d_5=1,d_6=2,d_7=1,d_8=3,d_9=1,d_{10}=1$.

Step 2. Leaves initially: $\{1,5,7,9,10\}$.

| Step | smallest leaf | neighbor | remove leaf | update |
|------|---------------|----------|-------------|--------|
| 1 | 1 | **4** | remove 1 | $d_4$ becomes 1 (leaf) |
| 2 | 4 | **3** | remove 4 | $d_3$ becomes 3 |
| 3 | 5 | **6** | remove 5 | $d_6$ becomes 1 (leaf) |
| 4 | 6 | **8** | remove 6 | $d_8$ becomes 2 |
| 5 | 7 | **3** | remove 7 | $d_3$ becomes 2 |
| 6 | 9 | **3** | remove 9 | $d_3$ becomes 1 (leaf) |
| 7 | 3 | **2** | remove 3 | $d_2$ becomes 1 (leaf) |
| 8 | 2 | **8** | remove 2 | remaining: $\{8,10\}$ |

Prüfer code: $(4,3,6,8,3,3,2,8)$.

$$\boxed{\text{Tree 1: }(5,8,2,5,5,1,9,7)\qquad\text{Tree 2: }(4,3,6,8,3,3,2,8)}$$

---

**21.** Determine which trees have Prüfer codes with distinct values in all positions. How many labeled trees with $n$ vertices have this property?

**Solution.**
Step 1. A Prüfer code of length $n-2$ has all entries distinct. Since vertex $i$ appears $d_i-1$ times, all-distinct entries means each appears at most once. So $d_i-1\le1$, i.e., $d_i\le2$ for all vertices.

Step 2. A tree with maximum degree at most 2 is a **path** $P_n$.

Step 3. How many labeled paths on $n$ vertices? Choose which 2 labels are the endpoints: $\binom{n}{2}$ ways. The remaining $n-2$ labels form the internal path in $(n-2)!$ orders. Total: $\binom{n}{2}(n-2)!=\frac{n!}{2!(n-2)!}\cdot(n-2)!=\frac{n!}{2}$.

Step 4. Verifying via Prüfer: choose which 2 labels do NOT appear in the code (the leaves/endpoints): $\binom{n}{2}$ ways. Arrange the remaining $n-2$ labels in the code: $(n-2)!$ ways. Same result.

$$\boxed{\text{Labeled paths }P_n;\quad\text{Number }=\binom{n}{2}(n-2)!=\frac{n!}{2}}$$

---

**22.** How many labeled trees with 6 vertices have given degree sequences?

**Solution.** Formula: $\displaystyle\frac{(n-2)!}{\prod_{i=1}^{n}(d_i-1)!}$, provided $\sum d_i=2(n-1)$.

For $n=6$, $(n-2)!=4!=24$, and $\sum d_i=10$.

**(a)** $(5,1,1,1,1,1)$:
Sum $=5+5=10$. ✓
Denominator $=(5-1)!(1-1)!^5=4!\cdot1=24$.
Count $=24/24=1$.

$$\boxed{1}$$

**(b)** $(4,2,1,1,1,1)$:
Sum $=4+2+4=10$. ✓
For a specific label assignment: denominator $=(4-1)!(2-1)!(1-1)!^4=3!\cdot1!\cdot1=6$.
Count per assignment $=24/6=4$.
Number of label-to-degree assignments: choose label for degree 4 ($6$ ways), then degree 2 ($5$ ways): $6\times5=30$.
Total $=30\times4=120$.

$$\boxed{120}$$

**(c)** $(3,2,2,1,1,1)$:
Sum $=3+2+2+3=10$. ✓
Per assignment: denominator $=(3-1)!(2-1)!^2(1-1)!^3=2!\cdot1\cdot1\cdot1=2$.
Count per assignment $=24/2=12$.
Assignments: choose label for degree 3 ($6$ ways), choose which 2 labels get degree 2 from remaining 5: $\binom{5}{2}=10$. Total $=6\times10=60$.
Total $=60\times12=720$.

$$\boxed{720}$$

**(d)** $(2,2,2,2,1,1)$:
Sum $=4\times2+2=10$. ✓
Per assignment: denominator $=(2-1)!^4(1-1)!^2=1^4\cdot1^2=1$.
Count per assignment $=24$.
Assignments: choose which 2 vertices are leaves (degree 1): $\binom{6}{2}=15$.
Total $=15\times24=360$.

$$\boxed{360}$$

---

**23.** How many labeled trees with $n$ vertices are there such that the degree of the node labeled $n$ is equal to $k$?

**Solution.**
Step 1. In the Prüfer code of length $n-2$, vertex $n$ appears exactly $d_n-1=k-1$ times.
Step 2. Choose which $k-1$ positions in the sequence contain $n$: $\binom{n-2}{k-1}$ ways.
Step 3. The remaining $(n-2)-(k-1)=n-k-1$ positions are filled with any labels from $\{1,2,\dots,n-1\}$: $(n-1)^{\,n-k-1}$ ways.
Step 4. By the Product Rule:
$$\binom{n-2}{k-1}(n-1)^{\,n-k-1}$$
This is valid for $1\le k\le n-1$. For $k=0$ or $k\ge n$, the count is 0.

$$\boxed{\binom{n-2}{k-1}(n-1)^{\,n-k-1}}$$

---

**24.** How many labeled rooted trees on $n$ vertices are there? Propose a generation method.

**Solution.**
Step 1. Labeled trees: $n^{n-2}$ (Cayley). For each, choose a root: $n$ choices. Total: $n\cdot n^{n-2}=n^{n-1}$.

Step 2. **Uniform generation method:**
1. Generate a random Prüfer sequence: $n-2$ independent uniform random integers from $[n]$.
2. Decode to obtain a labeled tree $T$ (uniform by Cayley + Prüfer bijection).
3. Choose a root uniformly from $\{1,\dots,n\}$ (independent of $T$).
4. Output the rooted tree $(T,\text{root})$.

Each rooted labeled tree has probability $1/(n^{n-1})$.

$$\boxed{n^{\,n-1}\text{ rooted labeled trees; Prüfer + uniform root choice.}}$$

---

**25.** How many labeled rooted forests on $n$ vertices with exactly $k$ components are there?

**Solution.**
Step 1. Add a "super-root" vertex $0$ and connect it to one vertex in each component. This creates a rooted tree on $n+1$ vertices (labels $0,1,\dots,n$) with root $0$, where $0$ has exactly $k$ children (the roots of the $k$ forest components).

Step 2. Using Problem 23 with $n$ replaced by $n+1$, vertex $0$ as the special vertex with degree $k$: the count is $\binom{(n+1)-2}{k-1}((n+1)-1)^{(n+1)-k-1}=\binom{n-1}{k-1}n^{\,n-k}$.

Step 3. Verify: for $k=1$ (single rooted tree), $\binom{n-1}{0}n^{\,n-1}=n^{\,n-1}$, matching Problem 24.

$$\boxed{\binom{n-1}{k-1}n^{\,n-k}}$$

---

**26.** Find a spanning tree for each of these graphs: $K_5$, $C_5$, $K_{1,6}$, $K_{2,3}$, $Q_3$.

**Solution.**
Step 1. **$K_5$** (complete graph on 5 vertices): any tree on 5 vertices with 4 edges. Take the path $1-2-3-4-5$.

Step 2. **$C_5$** (5-cycle): remove any single edge, e.g., $\{1,5\}$, leaving the path $1-2-3-4-5$.

Step 3. **$K_{1,6}$** (star with 6 leaves): it is already a tree. It is its own unique spanning tree.

Step 4. **$K_{2,3}$** (parts $A=\{a_1,a_2\}$, $B=\{b_1,b_2,b_3\}$): need 4 edges. Take a star at $a_1$ connecting to all three $b_i$, plus edge $\{b_1,a_2\}$ (or $\{a_1,a_2\}$). Edges: $\{a_1,b_1\},\{a_1,b_2\},\{a_1,b_3\},\{b_1,a_2\}$.

Step 5. **$Q_3$** (3-cube, 8 vertices, 12 edges). Run BFS from $000$:
- $000-001$, $000-010$, $000-100$
- $001-011$, $001-101$
- $010-110$
- $011-111$

Spanning tree edges (7 edges): $\{000,001\},\{000,010\},\{000,100\},\{001,011\},\{001,101\},\{010,110\},\{011,111\}$.

$$\boxed{\begin{aligned}
K_5&:\text{ path }1-2-3-4-5\\
C_5&:\text{ path of 5 vertices (remove any edge)}\\
K_{1,6}&:\text{ itself (it is a tree)}\\
K_{2,3}&:\text{ star at }a_1\text{ plus }\{b_1,a_2\}\\
 Q_3&:\text{ BFS tree as above}
\end{aligned}}$$

---

**27.** Draw all spanning trees of $C_5$, determine how many. Find its Laplacian and reduced Laplacian. Verify with Matrix-Tree Theorem. How many spanning trees does $C_n$ have?

**Solution.**
Step 1. $C_5$ is a 5-cycle (5 vertices, 5 edges). A spanning tree has 4 edges, so we remove exactly one edge. There are $\binom{5}{1}=5$ spanning trees (distinct as subgraphs, though all isomorphic to $P_5$).

Step 2. **All 5 spanning trees** (label vertices $1,2,3,4,5$ cyclically):
- Remove $\{1,5\}$: edges $\{1,2\},\{2,3\},\{3,4\},\{4,5\}$
- Remove $\{1,2\}$: edges $\{2,3\},\{3,4\},\{4,5\},\{5,1\}$
- Remove $\{2,3\}$: edges $\{1,2\},\{3,4\},\{4,5\},\{5,1\}$
- Remove $\{3,4\}$: edges $\{1,2\},\{2,3\},\{4,5\},\{5,1\}$
- Remove $\{4,5\}$: edges $\{1,2\},\{2,3\},\{3,4\},\{5,1\}$

Step 3. **Laplacian** $L=D-A$ (each vertex degree 2, adjacent to two cyclic neighbors):

$$L=\begin{pmatrix}
2 & -1 &  0 &  0 & -1\\
-1 &  2 & -1 &  0 &  0\\
0 & -1 &  2 & -1 &  0\\
0 &  0 & -1 &  2 & -1\\
-1 &  0 &  0 & -1 &  2
\end{pmatrix}$$

Step 4. Delete row 5, column 5 to get the $4\times4$ reduced Laplacian:

$$\tilde L=\begin{pmatrix}
2 & -1 &  0 &  0\\
-1 &  2 & -1 &  0\\
0 & -1 &  2 & -1\\
0 &  0 & -1 &  2
\end{pmatrix}$$

Step 5. Compute $\det\tilde L$ by cofactor expansion along row 1:

$\det\tilde L = 2\cdot\begin{vmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{vmatrix} - (-1)\cdot\begin{vmatrix}-1&-1&0\\0&2&-1\\0&-1&2\end{vmatrix}$

First $3\times3$: $2(4-1) + 1(-2-0) = 2\cdot3 -2 = 4$.

Second $3\times3$: $(-1)(4-1) - (-1)(0) + 0 = -3$.

$\det\tilde L = 2\cdot4 + 1\cdot(-3) = 8-3 = 5$.

Step 6. Matrix-Tree: $\kappa(C_5)=\det\tilde L=5$, matching the direct enumeration.

Step 7. **General $C_n$:** removing any one of $n$ edges yields a distinct spanning tree. So $\kappa(C_n)=n$. (The reduced Laplacian of $C_n$ is an $(n-1)\times(n-1)$ tridiagonal Toeplitz matrix with determinant $n$.)

$$\boxed{\kappa(C_5)=5,\qquad\kappa(C_n)=n}$$

---

**28.** How many trees are there in the spanning forest of a graph?

**Solution.**
Step 1. A spanning forest of $G$ contains a spanning tree within each connected component. The number of trees equals the number of connected components $c$.

$$\boxed{c\text{ (the number of connected components)}}$$

---

**29.** How many edges must be removed to produce the spanning forest of a graph with $n$ vertices, $m$ edges, and $c$ connected components?

**Solution.**
Step 1. A spanning forest has exactly $n-c$ edges (each component's spanning tree has $n_i-1$ edges; sum $=n-c$).
Step 2. Starting with $m$ edges, remove $m-(n-c)$ edges to reach $n-c$.

$$\boxed{m-(n-c)}$$

---

**30.** How many different spanning trees does each graph have?

**(a)** $K_{2,2}$: Formula $\kappa(K_{m,n})=m^{n-1}n^{m-1}=2^{1}\cdot2^{1}=4$.

$$\boxed{4}$$

**(b)** $C_n$: Removing any one of $n$ edges gives a spanning tree. $\kappa(C_n)=n$.

$$\boxed{n}$$

**(c)** $K_{1,n}$: It is itself a tree (star). Formula: $1^{n-1}\cdot n^{0}=1$.

$$\boxed{1}$$

**(d)** $K_{m,n}$: Known formula: $\kappa(K_{m,n})=m^{n-1}n^{m-1}$.

$$\boxed{m^{\,n-1}n^{\,m-1}}$$

**(e)** $Q_3$: The 3-cube has $v=8,e=12$. Known result (Matrix-Tree computation yields) $\kappa(Q_3)=384$. More generally, $\kappa(Q_n)=2^{2^n-n-1}\prod_{k=1}^{n}k^{\binom{n}{k}}$. For $n=3$: $2^{8-3-1}\cdot1^{3}\cdot2^{3}\cdot3^{1}=2^{4}\cdot8\cdot3=16\cdot24=384$.

$$\boxed{384}$$

**(f)** $W_n$ (wheel, $n\ge3$ rim vertices plus hub, total $n+1$ vertices): Known result $\kappa(W_n)=L_{2n}-2$, where $L_k$ is the $k$-th Lucas number ($L_1=1,L_2=3,L_{k}=L_{k-1}+L_{k-2}$). Equivalently,
$$\kappa(W_n)=\left(\frac{3+\sqrt5}{2}\right)^n+\left(\frac{3-\sqrt5}{2}\right)^n-2$$
Examples: $\kappa(W_3)=L_6-2=18-2=16$; $\kappa(W_4)=L_8-2=47-2=45$; $\kappa(W_5)=L_{10}-2=123-2=121$.

$$\boxed{\kappa(W_n)=L_{2n}-2}$$

---

**31.** Which connected simple graphs have exactly one spanning tree?

**Solution.**
Step 1. If $G$ is a tree, it is its own spanning tree and the unique one (any spanning tree must have the same edges since adding/removing any edge would disconnect or create a cycle).
Step 2. If $G$ has a cycle, removing different edges of that cycle yields at least two distinct spanning trees.
Step 3. Thus exactly one spanning tree iff $G$ itself is a tree.

$$\boxed{G\text{ is a tree itself.}}$$

---

**32.** When must an edge of a connected simple graph be in every spanning tree?

**Solution.**
Step 1. An edge whose removal disconnects the graph is called a **bridge** (cut-edge).
Step 2. Every spanning tree must be connected, so it must include every bridge.
Step 3. Conversely, if an edge lies on some cycle, there exists a spanning tree excluding it (remove that edge from the cycle, keep the rest of the cycle intact).
Step 4. Thus an edge is in every spanning tree iff it is a bridge.

$$\boxed{\text{The edge must be a bridge (cut-edge).}}$$

---

**33.** Prove that if $G$ is a connected, simple graph with $n$ vertices and $G$ does not contain a simple path of length $k$, then it contains at most $(k-1)n$ edges.

**Solution.**
Step 1. Let $P$ be a longest simple path in $G$, with vertices $v_1,v_2,\dots,v_{\ell}$ and $\ell\le k$ (since no path of length $k$ exists, path has at most $k$ vertices).

Step 2. Consider the endpoint $v_1$. All neighbors of $v_1$ must lie on $P$; otherwise $P$ could be extended, contradicting maximality. Since $v_1$ has at least one neighbor ($v_2$), its degree satisfies $\deg(v_1)\le\ell-1\le k-1$.

Step 3. Remove $v_1$ from $G$. In the remaining graph $G'=G-v_1$, there is still no path of length $k$ ($G'$ is a subgraph of $G$). The number of vertices decreases by 1.

Step 4. Repeating this argument $n$ times (each time removing an endpoint of a longest path), we remove at most $k-1$ edges per vertex deletion. Total edges removed $=m\le(k-1)n$.

Step 5. Formal induction: Base case $n=1$ trivial. Inductive step: remove an endpoint of a longest path (degree $\le k-1$), apply induction to the remaining $n-1$ vertex graph. Summing gives $m\le(k-1)n$.

$$\boxed{m\le(k-1)n\quad\text{(proved by repeated endpoint deletion).}}$$

---

**34.** Use the Matrix-Tree Theorem on $K_n$ to reprove Cayley's Theorem ($\kappa(K_n)=n^{n-2}$).

**Solution.**
Step 1. Laplacian of $K_n$: diagonal entries $n-1$, off-diagonal entries $-1$.
$$L=(n-1)I_n - J_n + I_n = nI_n - J_n$$
where $J_n$ is the $n\times n$ all-ones matrix.

Step 2. Delete row $n$, column $n$ to get the $(n-1)\times(n-1)$ reduced Laplacian:
$$\tilde L = nI_{n-1} - J_{n-1}$$

Step 3. Fact: for an $m\times m$ matrix $aI_m+bJ_m$, its determinant is $a^{m-1}(a+mb)$. Here $m=n-1$, $a=n$, $b=-1$.

Step 4. $\det\tilde L = n^{(n-1)-1}(n+(n-1)(-1)) = n^{n-2}(n-(n-1)) = n^{n-2}\cdot1 = n^{n-2}$.

Step 5. By the Matrix-Tree Theorem, $\kappa(K_n)=\det\tilde L=n^{n-2}$, which is Cayley's Theorem.

$$\boxed{\kappa(K_n)=n^{n-2}\text{, reproving Cayley's Theorem.}}$$

---

**35.** Prove $\kappa(G)=\kappa_1\kappa_2\cdots\kappa_k$ using the Matrix-Tree Theorem.

**Solution.**
Step 1. Let $v$ be a cut vertex of $G$, whose removal disconnects $G$ into components $G_1,\dots,G_k$. Let $H_i=G\setminus\bigcup_{j\neq i}G_j$ (the subgraph induced by $G_i\cup\{v\}$). Its complexity is $\kappa_i=\kappa(H_i)$.

Step 2. Order the vertices so that $v$ is the last vertex, vertices of $G_1$ come first, then $G_2$, etc. In the Laplacian $L$, there are no edges between distinct $G_i$ and $G_j$ ($i\neq j$), so the off-diagonal blocks connecting them are zero.

Step 3. Delete the row and column of $v$ to obtain the reduced Laplacian $\tilde L_G$. Because there are no edges between different $G_i$ blocks, the matrix $\tilde L_G$ is block-diagonal, with diagonal blocks $\tilde L_{H_i}$ (the reduced Laplacians of $H_i$ with $v$'s row/column deleted).

Step 4. The determinant of a block-diagonal matrix is the product of the determinants of its blocks:
$$\det\tilde L_G = \prod_{i=1}^{k}\det\tilde L_{H_i}$$

Step 5. By the Matrix-Tree Theorem, $\kappa(G)=\det\tilde L_G$ and $\kappa_i=\kappa(H_i)=\det\tilde L_{H_i}$. Hence $\kappa(G)=\kappa_1\kappa_2\cdots\kappa_k$.

$$\boxed{\kappa(G)=\kappa_1\kappa_2\cdots\kappa_k}$$

---

**36.** Rosen 11.5: Exercises 1, 8.

**Solution (Exercise 1):** "How many edges must be removed from a connected graph with $n$ vertices and $m$ edges to produce a spanning tree?"

Step 1. A spanning tree has exactly $n-1$ edges. Starting with $m$ edges, we must remove $m-(n-1)$ edges.

$$\boxed{m-(n-1)}$$

**Solution (Exercise 8):** "How many nonisomorphic spanning trees does each of these simple graphs have?"

Step 1. Since the exact figures from Rosen's textbook are not reproduced here, the general methodology is:
- For each graph, enumerate all spanning trees by systematically removing edges from cycles (or using the Matrix-Tree Theorem for the count).
- Group the resulting trees by isomorphism (as unlabeled trees).
- Count the number of distinct isomorphism classes.

Step 2. For common special cases:
- $C_n$: all spanning trees are $P_n$, so 1 nonisomorphic spanning tree.
- $K_n$: number of nonisomorphic unlabeled trees on $n$ vertices (e.g., for $n=4$: 2 trees $P_4$ and $K_{1,3}$).
- For specific small graphs: enumerate by edge-removal and check isomorphism through degree-sequence comparison.

$$\boxed{\text{Methodology: enumerate edge-removals from cycles; group by isomorphism.}}$$

---

**37.** Devise an algorithm for constructing a maximum spanning tree of a connected weighted graph.

**Solution.**
Step 1. A **maximum spanning tree** maximizes the sum of edge weights. This is equivalent to finding an MST on the graph with negated weights (or sorting edges descending).

Step 2. **Algorithm (Reverse Kruskal):**
1. Sort all edges in **descending** order by weight.
2. Initialize each vertex as its own component (union-find data structure).
3. Iterate through sorted edges: for edge $\{u,v\}$ with weight $w$, if $u$ and $v$ are in different components, add the edge to the tree and union the components.
4. Stop when $n-1$ edges have been added.

Step 3. Equivalently, run Prim's algorithm but always pick the **maximum-weight** edge crossing the cut (use a max-heap instead of min-heap).

Step 4. Correctness follows from the cut property: the heaviest edge crossing any cut belongs to some maximum spanning tree (by symmetry, negate weights and apply the standard MST cut property).

$$\boxed{\text{Reverse Kruskal (sort descending) or max-heap Prim.}}$$

---

**38.** Show that there is a unique minimum spanning tree in a connected weighted graph if the weights of the edges are all different.

**Solution.**
Step 1. Suppose for contradiction that $T_1$ and $T_2$ are two distinct MSTs.

Step 2. Let $e$ be the edge of **minimum weight** in the symmetric difference $T_1\triangle T_2=(T_1\setminus T_2)\cup(T_2\setminus T_1)$. WLOG, $e\in T_1\setminus T_2$.

Step 3. Adding $e$ to $T_2$ creates a unique cycle $C$. Since $T_1$ is acyclic, not all edges of $C$ can be in $T_1$. Choose $f\in C$ with $f\in T_2\setminus T_1$.

Step 4. Form $T'=T_2\setminus\{f\}\cup\{e\}$. This is a spanning tree. Its weight: $w(T')=w(T_2)-w(f)+w(e)$.

Step 5. Since $e$ is the **minimum-weight** edge in $T_1\triangle T_2$ and $f\in T_1\triangle T_2$ with $f\neq e$, we have $w(e)<w(f)$ (all weights distinct, and $e$ is uniquely minimum in the symmetric difference).

Step 6. Thus $w(T')<w(T_2)$, contradicting that $T_2$ is an MST. Hence no two distinct MSTs exist — the MST is unique.

$$\boxed{\text{Unique MST follows from the cut property with distinct weights.}}$$

---

**39.** Devise an algorithm for finding the second minimum spanning tree in a connected weighted graph.

**Solution.**
Step 1. Find an MST $T$ (using Kruskal's or Prim's).

Step 2. For each non-tree edge $e=uv\notin T$ (with weight $w(e)$):
- Add $e$ to $T$, creating a unique cycle $C_e$.
- Find the **maximum-weight** tree edge $f$ on $C_e$ (the heaviest edge of $T$ on the cycle).
- The candidate spanning tree is $T_e=T\setminus\{f\}\cup\{e\}$ with weight $w(T)-w(f)+w(e)$.

Step 3. Among all candidates $T_e$, take the one with **minimum weight**. This is the second minimum spanning tree (it may have the same weight as the MST if there were ties; if the MST is unique by Problem 38, the second MST is strictly heavier).

Step 4. **Complexity:** Naively $O(mn)$ (traverse the cycle for each of $m-n+1$ non-tree edges). Can be optimized to $O(m\log n)$ using binary lifting / LCA to find max-weight edges on tree paths.

$$\boxed{\begin{aligned}&\text{1. Find MST }T.\\
&\text{2. For each }e\notin T\text{: add }e,\text{ remove max-weight edge on created cycle.}\\
&\text{3. Take the minimum-weight candidate.}\end{aligned}}$$

---

**40.** Suppose all edge weights are integers in $[1,|V|]$. How fast can Kruskal's run? What if weights are in $[1,k]$ for constant $k$?

**Solution.**
Step 1. Kruskal's algorithm: sort edges + union-find operations. The sorting step dominates in standard implementations: $O(|E|\log|E|)$ with comparison sort.

Step 2. **Case $[1,|V|]$:** Since weights are small integers in a range proportional to $|V|$, we can sort using **counting sort** (or bucket sort) in $O(|E|+|V|)$ time. The union-find operations take $O(|E|\,\alpha(|V|))$. Total: $O(|E|+|V|)=O(|E|)$ (for connected graphs, $|E|\ge|V|-1$).

Step 3. **Case $[1,k]$ for constant $k$:** Counting sort takes $O(|E|+k)=O(|E|)$ time (since $k$ is constant). Total: $O(|E|\,\alpha(|V|))$, which is near-linear.

$$\boxed{\begin{aligned}
[1,|V|]&:\ O(|E|+|V|)\\
[1,k]\text{ (constant)}&:\ O(|E|\,\alpha(|V|))
\end{aligned}}$$

---

**41.** Represent $((x+2)^3)(y-(3+x))-5$ using a binary tree. Write in prefix, postfix, infix.

**Solution.**
Step 1. Parse by operator precedence. The last evaluated operator is the outer subtraction $-5$, so the root is $-$.
- Left subtree: product $((x+2)^3)\times(y-(3+x))$. Root $\times$.
  - Left of $\times$: $(x+2)^3$. Root exponentiation $\uparrow$.
    - Left of $\uparrow$: $x+2$. Root $+$, children $x$ and $2$.
    - Right of $\uparrow$: $3$.
  - Right of $\times$: $y-(3+x)$. Root $-$.
    - Left: $y$.
    - Right: $3+x$. Root $+$, children $3$ and $x$.
- Right subtree: $5$.

Step 2. Expression tree:

```
         -
       /   \
      x     5
    /   \
   ^     -
  / \   / \
 +   3 y   +
/ \       / \
x  2     3   x
```

Step 3. **Traversals:**
**(a) Prefix (pre-order: root, left, right):**
$- \times \uparrow + x 2 3 - y + 3 x 5$

**(b) Postfix (post-order: left, right, root):**
$x 2 + 3 \uparrow y 3 x + - \times 5 -$

**(c) Infix (in-order, fully parenthesized):**
$((((x+2)\uparrow3)\times(y-(3+x)))-5)$

$$\boxed{\begin{aligned}
\text{Prefix: }&-\times\uparrow + x 2 3 - y + 3 x 5\\
\text{Postfix: }&x 2 + 3 \uparrow y 3 x + - \times 5 -\\
\text{Infix: }&(((x+2)\uparrow3)\times(y-(3+x)))-5
\end{aligned}}$$

---

**42.** Represent the compound propositions using ordered rooted trees; give prefix, postfix, infix.

**(i)** $\lnot(p\land q)\leftrightarrow(\lnot p\lor\lnot q)$

**Solution.**
Step 1. Last operator: $\leftrightarrow$. Left subtree: $\lnot(p\land q)$. Right subtree: $(\lnot p\lor\lnot q)$.
- $\lnot(p\land q)$: root $\lnot$, child $\land(p,q)$.
- $(\lnot p\lor\lnot q)$: root $\lor$, children $\lnot p$ and $\lnot q$.

**(a) Prefix:** $\leftrightarrow \lnot \land p q \lor \lnot p \lnot q$

**(b) Postfix:** $p q \land \lnot p \lnot q \lnot \lor \leftrightarrow$

**(c) Infix:** $(\lnot(p\land q))\leftrightarrow((\lnot p)\lor(\lnot q))$

---

**(ii)** $(\lnot p\land(q\leftrightarrow\lnot p))\lor\lnot q$

**Solution.**
Step 1. Last operator: $\lor$. Left: $\lnot p\land(q\leftrightarrow\lnot p)$. Right: $\lnot q$.
- Left subtree: root $\land$, children $\lnot p$ and $(q\leftrightarrow\lnot p)$.
  - $(q\leftrightarrow\lnot p)$: root $\leftrightarrow$, children $q$ and $\lnot p$.

**(a) Prefix:** $\lor \land \lnot p \leftrightarrow q \lnot p \lnot q$

**(b) Postfix:** $p \lnot q p \lnot \leftrightarrow \land q \lnot \lor$

**(c) Infix:** $((\lnot p)\land(q\leftrightarrow(\lnot p)))\lor(\lnot q)$

$$\boxed{\begin{aligned}
\text{(i) Prefix: }&\leftrightarrow\lnot\land p q\lor\lnot p\lnot q\\
\text{Postfix: }&p q\land\lnot p\lnot q\lnot\lor\leftrightarrow\\
\text{Infix: }&(\lnot(p\land q))\leftrightarrow((\lnot p)\lor(\lnot q))\\[6pt]
\text{(ii) Prefix: }&\lor\land\lnot p\leftrightarrow q\lnot p\lnot q\\
\text{Postfix: }&p\lnot q p\lnot\leftrightarrow\land q\lnot\lor\\
\text{Infix: }&((\lnot p)\land(q\leftrightarrow(\lnot p)))\lor(\lnot q)
\end{aligned}}$$

---

**43.** Evaluate the prefix expressions. (Scan right to left with a stack.)

**(a)** $- * 2 / 8 4 3$

**Solution.**
- Push 3: $[3]$
- Push 4: $[3,4]$
- Push 8: $[3,4,8]$
- $/$: pop 8,4 $\to 8/4=2$, push: $[3,2]$
- Push 2: $[3,2,2]$
- $*$: pop 2,2 $\to 4$, push: $[3,4]$
- $-$: pop 3,4 $\to 3-4=-1$, push: $[-1]$

$$\boxed{-1}$$

**(b)** $\uparrow - * 3 3 * 4 2 5$

**Solution.** ($\uparrow$ = exponentiation)
- Push 5: $[5]$
- Push 2: $[5,2]$
- Push 4: $[5,2,4]$
- $*$: $2*4=8$, push: $[5,8]$
- Push 3: $[5,8,3]$
- Push 3: $[5,8,3,3]$
- $*$: $3*3=9$, push: $[5,8,9]$
- $-$: $8-9=-1$, push: $[5,-1]$
- $\uparrow$: $(-1)^5=-1$, push: $[-1]$

$$\boxed{-1}$$

**(c)** $+ - \uparrow 3 2 \uparrow 2 3 / 6 - 4 2$

**Solution.**
- Push 2: $[2]$
- Push 4: $[2,4]$
- $-$: $4-2=2$, push: $[2,2]$
- Push 6: $[2,2,6]$
- $/$: $2/6=\frac13$, push: $[2,\frac13]$
- Push 3: $[2,\frac13,3]$
- Push 2: $[2,\frac13,3,2]$
- $\uparrow$: $2^3=8$, push: $[2,\frac13,8]$
- Push 2: $[2,\frac13,8,2]$
- Push 3: $[2,\frac13,8,2,3]$
- $\uparrow$: $3^2=9$, push: $[2,\frac13,8,9]$
- $-$: $8-9=-1$, push: $[2,\frac13,-1]$
- $+$: $\frac13+(-1)=-\frac23$, push: $[2,-\frac23]$

$$\boxed{-\frac{2}{3}}$$

---

**44.** Evaluate the postfix expressions. (Scan left to right with a stack.)

**(a)** $5 2 1 - - 3 1 4 + + *$

**Solution.**
- Push 5,2,1: $[5,2,1]$
- $-$: pop 2,1 $\to 2-1=1$, push: $[5,1]$
- $-$: pop 5,1 $\to 5-1=4$, push: $[4]$
- Push 3,1,4: $[4,3,1,4]$
- $+$: pop 1,4 $\to 1+4=5$, push: $[4,3,5]$
- $+$: pop 3,5 $\to 3+5=8$, push: $[4,8]$
- $*$: pop 4,8 $\to 4\times8=32$, push: $[32]$

$$\boxed{32}$$

**(b)** $9 3 / 5 + 7 2 - *$

**Solution.**
- Push 9,3: $[9,3]$
- $/$: $9/3=3$, push: $[3]$
- Push 5: $[3,5]$
- $+$: $3+5=8$, push: $[8]$
- Push 7,2: $[8,7,2]$
- $-$: $7-2=5$, push: $[8,5]$
- $*$: $8\times5=40$, push: $[40]$

$$\boxed{40}$$

**(c)** $3 2 * 2 \uparrow 5 3 - 8 4 / * -$

**Solution.**
- Push 3,2: $[3,2]$
- $*$: $3\times2=6$, push: $[6]$
- Push 2: $[6,2]$
- $\uparrow$: $6^2=36$, push: $[36]$
- Push 5,3: $[36,5,3]$
- $-$: $5-3=2$, push: $[36,2]$
- Push 8,4: $[36,2,8,4]$
- $/$: $8/4=2$, push: $[36,2,2]$
- $*$: $2\times2=4$, push: $[36,4]$
- $-$: $36-4=32$, push: $[32]$

$$\boxed{32}$$

---

**45.** Which of these are well-formed formulas over symbols $\{x,y,z\}$ and binary operators $\{\times,+,\circ\}$?

**Solution.**
Recall: A well-formed formula (wff) in prefix notation satisfies:
(i) A single symbol is a wff.
(ii) If $X,Y$ are wffs and $*$ is an operator, then $*XY$ is a wff.

**(a)** $\times + + x y x$

Step 1. Parse: $\times$ expects two arguments. First argument parses as: $+$ expects two. Next $+$ expects two: $x$ (wff), $y$ (wff) $\to$ $+xy$ is wff. Then the first $+$ has arguments $+xy$ (wff) and $x$ (wff) $\to$ $++xyx$ is wff. Now $\times$ has only one argument — needs a second argument. **Not well-formed.**

**(b)** $\circ x y \times x z$

Step 1. $\circ x y$ is a wff. Then $\times x z$ is a separate wff. But a well-formed formula must be a single connected expression; this is two wffs concatenated without a unifying operator. **Not well-formed.**

**(c)** $\times \circ x z \times \times x y$

Step 1. $\times$ expects two arguments. First: $\circ x z$ (wff). Second: $\times \times x y$. Parse the second: $\times$ expects two args. First: $\times$ (operator, not a wff!) expects two args. Its first arg is $x$ (wff), expects second — only $y$ follows. So $\times x y$ is a wff. Then $\times \times x y$ has the first $\times$ with first argument $\times x y$ (wff) but needs a second argument — none left. **Not well-formed.**

**(d)** $\times + \circ x x \circ x x x$

Step 1. $\times$ expects two arguments.
- First: $+$ expects two. First: $\circ x x$ (wff). Second: $\circ x x$ (wff). So $+\circ x x\circ x x$ is a wff.
- Second: $x$ (symbol, wff).
So $\times(+\circ x x\circ x x)x$ uses all symbols as a single wff. **Well-formed.**

$$\boxed{\begin{aligned}
\text{(a) }&\text{Not well-formed}\\
\text{(b) }&\text{Not well-formed}\\
\text{(c) }&\text{Not well-formed}\\
\text{(d) }&\text{Well-formed}
\end{aligned}}$$

---

**46.** Show that any well-formed formula in prefix notation over a set of symbols and binary operators contains exactly one more symbol than the number of operators.

**Solution.**
Step 1. Proof by **structural induction** on the definition of wff.

Step 2. **Base case:** If $F$ is a single symbol $x$, it has $1$ symbol and $0$ operators. Then $1=0+1$. $\checkmark$

Step 3. **Inductive step:** Assume $X$ and $Y$ are wffs with $s_X$ symbols, $o_X$ operators, and $s_Y$ symbols, $o_Y$ operators. By induction hypothesis: $s_X=o_X+1$ and $s_Y=o_Y+1$.

Step 4. Form $F=*XY$ where $*$ is a binary operator. Then:
- Number of symbols in $F$: $s_F=s_X+s_Y$.
- Number of operators in $F$: $o_F=1+o_X+o_Y$.

Step 5. Compute:
$$s_F = s_X+s_Y = (o_X+1)+(o_Y+1) = (o_X+o_Y+1)+1 = o_F+1$$

Thus $s_F=o_F+1$ holds for $F$.

Step 6. By induction, every wff in prefix notation over symbols and binary operators has exactly one more symbol than operators.

$$\boxed{\text{Proved by structural induction.}}$$

---

**47.** Explain how to use breadth-first search to find the length of a shortest path between two vertices in an undirected graph.

**Solution.**
Step 1. Run BFS starting from the source vertex $s$. Maintain an array $\operatorname{dist}[]$ where $\operatorname{dist}[v]$ stores the distance (number of edges) from $s$ to $v$. Initialize $\operatorname{dist}[s]=0$ and all others to $\infty$.

Step 2. In BFS, when a vertex $u$ is dequeued, for each unvisited neighbor $v$, set $\operatorname{dist}[v]=\operatorname{dist}[u]+1$ and enqueue $v$. BFS visits vertices in order of increasing distance from $s$, guaranteeing that when $v$ is first discovered, $\operatorname{dist}[v]$ is the shortest path length.

Step 3. When the target vertex $t$ is dequeued (or first discovered), $\operatorname{dist}[t]$ is the length of the shortest path from $s$ to $t$. If $t$ is never reached, the graph is disconnected and there is no path.

Step 4. **Why BFS works for unweighted graphs:** BFS explores vertices level by level. All vertices at distance $k$ are discovered before any vertex at distance $k+1$. Thus the first time $t$ is reached, the path length is minimal.

$$\boxed{\text{BFS from source: } \operatorname{dist}[t] \text{ on first discovery is the shortest path length.}}$$

---

**48.** Devise an algorithm based on BFS/DFS that determines whether a graph has a cycle, and if so, finds one.

**Solution.**
Step 1. **DFS-based cycle detection:**
- Maintain a `visited[]` array (boolean) and a `parent[]` array.
- Perform DFS from an arbitrary unvisited vertex.

Step 2. During DFS, when exploring an edge $(u,v)$:
- If $v$ is **not visited**: set `parent[v]=u`, recurse on $v$.
- If $v$ is **already visited** and $v\neq$ `parent[u]`: a cycle has been found! The cycle consists of the tree path from $v$ up to $u$ (via parent pointers) plus the edge $(u,v)$.

Step 3. To extract the cycle: walk from $u$ back to $v$ using `parent[]` pointers, collecting vertices, then append $u$ to close the cycle.

Step 4. **BFS-based cycle detection:**
Similar: during BFS, if a neighbor $v$ has already been discovered (visited) and $v$ is not the parent of $u$, a cycle exists. The cycle can be reconstructed using parent pointers from both directions to their lowest common ancestor.

Step 5. If the traversal completes without finding any such edge, the graph is acyclic (a forest).

$$\boxed{\text{DFS/BFS with parent tracking: back edge to non-parent } \Rightarrow \text{ cycle.}}$$

---

**49.** Devise an algorithm based on BFS/DFS for finding the connected components of a graph.

**Solution.**
Step 1. Initialize an array `component[v]` to store the component ID of each vertex, and a counter `compID=0`.

Step 2. Iterate over all vertices $v$. If `component[v]` is unassigned:
- Increment `compID`.
- Run BFS (or DFS) starting from $v$. For every vertex $u$ reached during this traversal, assign `component[u]=compID`.

Step 3. After iterating over all vertices, `compID` equals the number of connected components. The vertices in each component are those sharing the same component ID.

Step 4. The algorithm runs in $O(|V|+|E|)$ time and uses $O(|V|)$ extra space.

$$\boxed{\text{Iterate unvisited vertices; BFS/DFS from each assigns a component ID.}}$$

---

**50.** Explain how BFS/DFS can be used to determine whether a graph is bipartite.

**Solution.**
Step 1. A graph is bipartite iff it can be 2-colored such that no edge connects vertices of the same color. Equivalently, it contains no odd-length cycle.

Step 2. **Algorithm (BFS or DFS coloring):**
- Initialize `color[v]` to unassigned (e.g., $-1$) for all vertices.
- For each uncolored vertex $v$, set `color[v]=0$ (say Red) and run BFS/DFS.

Step 3. During traversal, when examining edge $(u,v)$:
- If `color[v]` is unassigned: assign `color[v]=1-color[u]` (the opposite color) and enqueue/recurse.
- If `color[v]` is already assigned: check if `color[v]==color[u]`. If they are the same color, the graph is **not bipartite** (an edge connects two vertices of the same color, implying an odd cycle).

Step 4. If the traversal completes without any color conflict, the graph is bipartite. The algorithm runs in $O(|V|+|E|)$ time.

$$\boxed{\text{2-color via BFS/DFS: same-color neighbor } \Rightarrow \text{ not bipartite.}}$$

---

**51.** **Backtracking** algorithm for subset-sum. Apply to set $\{27,24,19,14,11,8\}$ with targets 20, 41, 60. Draw search trees.

**Solution.**
Step 1. **Algorithm:** Sort the set (given as $27,24,19,14,11,8$, already descending). Build the sum by including terms in order. If the sum exceeds $M$, backtrack by dropping the last term.

**(a) Target $M=20$:**

Search tree (pruned branches shown):
- Sum $0$:
  - Try $27$: exceeds 20. Skip.
  - Try $24$: exceeds 20. Skip.
  - Try $19$: sum $19$.
    - Try $14$: $33>20$. Skip.
    - Try $11$: $30>20$. Skip.
    - Try $8$: $27>20$. Skip.
  - Try $14$: sum $14$.
    - Try $11$: $25>20$. Skip.
    - Try $8$: $22>20$. Skip.
  - Try $11$: sum $11$.
    - Try $8$: $19<20$. No more numbers. $19\neq20$.
  - Try $8$: sum $8$. No more.

**No subset sums to 20.**

**(b) Target $M=41$:**

Search:
- Sum $0$:
  - Try $27$: sum $27$.
    - Try $24$: $51>41$. Skip.
    - Try $19$: $46>41$. Skip.
    - Try $14$: $41=41$ **$\to$ Found!** $\{27,14\}$.
    (Continue for completeness):
    - Try $11$: $38$. Try $8$: $46>41$. Skip.
    - Try $8$: $35$. No more.
  - Try $24$: sum $24$.
    - Try $19$: $43>41$. Skip.
    - Try $14$: $38$. Try $11$: $49>41$. Skip. Try $8$: $46>41$. Skip.
    - Try $11$: $35$. Try $8$: $43>41$. Skip.
    - Try $8$: $32$. No more.
  - Try $19$: sum $19$.
    - Try $14$: $33$. Try $11$: $44>41$. Skip. Try $8$: $41$ **$\to$ Found!** $\{19,14,8\}$.
    - Try $11$: $30$. Try $8$: $38$. No more.
    - Try $8$: $27$. No more.
  - Try $14$: $14+11=25+8=33$. No.

**Solutions:** $\{27,14\}$ and $\{19,14,8\}$.

**(c) Target $M=60$:**

Search (recording only solution paths):
- $27$:
  - $27+24=51$. $+19=70>60$. Skip. $+14=65>60$. Skip. $+11=62>60$. Skip. $+8=59$. $59<60$, no more numbers.
  - $27+19=46$. $+14=60$ **$\to$ Found!** $\{27,19,14\}$.
  - $27+14=41$. $+19=60$ (same set). $+11=52$. $+8=60$ **$\to$ Found!** $\{27,14,11,8\}$.
  - $27+11=38$. $+19=57$. $+8=65>60$. Skip. $+14=52$. $+8=60$ (same 4-element set).
  - $27+8=35$. $+19=54$. $+14=68>60$. $+11=65>60$. Skip. $+14=49$. $+11=60$ (same set).
- $24$:
  - $24+19=43$. $+14=57$. $+11=68>60$. $+8=65>60$. $+11=54$. $+8=62>60$.
  - $24+14=38$. $+19=57$. $+8=65>60$. $+11=49$. $+8=57$.
  - $24+11=35$. $+19=54$. $+8=62>60$. $+14=49$. $+8=57$.
  - $24+8=32$. No more.
- $19$: $19+14=33+11=44+8=52$. $19+11=30+8=38$. $19+8=27$. No more.
- $14$: max with remaining $14+11+8=33<60$. No solutions.

**Solutions:** $\{27,19,14\}$, $\{27,14,11,8\}$.

$$\boxed{\begin{aligned}
\text{(a) }M=20&:\text{ No solution.}\\
\text{(b) }M=41&:\{27,14\},\;\{19,14,8\}\\
\text{(c) }M=60&:\{27,19,14\},\;\{27,14,11,8\}
\end{aligned}}$$

---

**52.** There are 101 coins, and only one of them differs from the others (real ones) by weight. Using a balance scale, determine the counterfeit one with two weighings.

**Solution.**
Step 1. This is a variant of the classic counterfeit coin problem. We must determine whether 2 weighings on a balance scale suffice to identify one counterfeit among 101 coins.

Step 2. A balance scale has $m=3$ outcomes per weighing (left heavy, right heavy, balanced). With 2 weighings, we obtain at most $3^2=9$ distinguishable outcome sequences.

Step 3. If the counterfeit direction is unknown (heavier or lighter), there are $l=101\times2=202$ possibilities. Even if the direction is known (just heavier), there are $l=101$ possibilities.

Step 4. By the decision-tree lower bound:
$$h\ge\lceil\log_3 l\rceil$$
- For known direction: $h\ge\lceil\log_3 101\rceil=\lceil4.2\rceil=5$.
- For unknown direction: $h\ge\lceil\log_3 202\rceil=\lceil4.84\rceil=5$.

Step 5. Since $3^2=9<101$, it is **impossible** to determine the counterfeit coin among 101 coins in only 2 weighings with a standard balance scale. At least $\lceil\log_3 101\rceil=5$ weighings are required (even if the counterfeit is known to be heavier or lighter).

Step 6. The well-known 12-coin problem (counterfeit unknown direction) requires 3 weighings precisely because $3^2=9<24$ but $3^3=27\ge24$. Scaling up, 101 coins require 5 weighings.

$$\boxed{\text{Impossible. } 3^2=9<101,\text{ so at least } \lceil\log_3 101\rceil =5\text{ weighings are needed.}}$$

---
