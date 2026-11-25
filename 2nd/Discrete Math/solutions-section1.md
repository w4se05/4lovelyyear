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


