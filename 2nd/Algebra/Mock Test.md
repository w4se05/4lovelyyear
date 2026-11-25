### 1. Binary Choice & Short Calculations (5 pts)

**A. True or False** Evaluate the following assertions. Circle **t** (true) or **f** (false).  

1.  **[ t / f ]** The set of vectors $\{(1,0,1), (0,1,0), (1,1,1)\}$ forms a basis for $\mathbb{R}^3$.
2.  **[ t / f ]** For any two square matrices $A$ and $B$, $\det(A+B) = \det(A) + \det(B)$.
3.  **[ t / f ]** The relation $R = \{(x,y) \in \mathbb{R}^2 : x \le y\}$ is an equivalence relation.
4.  **[ t / f ]** If $a \equiv b \pmod n$, then $a$ and $b$ leave the same remainder when divided by $n$. 
5.  **[ t / f ]** In an RSA cryptosystem with modulus $n=55$, $e=7$ is a valid public exponent.

**B. Short Calculations**

1.  Given vectors $\vec{u} = (1, -2, 3)$ and $\vec{v} = (2, 0, -1)$.  
    Compute the dot product $\vec{u} \cdot \vec{v}$:  
    __________________________________________________________________ 

2.  Given matrix $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.  
    Compute $A^T - 2I_2$:  
    __________________________________________________________________ 

---

### 2. Linear Systems (5 pts)

Consider the system of equations with parameter $\lambda \in \mathbb{R}$: 

$$
\begin{cases}
x + y + z = 1 \\
x + \lambda y + 2z = 2 \\
x + y + \lambda z = 3
\end{cases}
$$

**(a)** Write down the coefficient matrix $A$ and the augmented matrix for the system.

<br><br><br>

**(b)** Calculate $\det(A)$. For which values of $\lambda$ does the system have a **unique solution**? 

<br><br><br>

**(c)** Let $\lambda = 2$. Solve for $y$ using **Cramer's Rule**.  
*(Note: You must use Cramer's rule to receive points)*. 

<br><br><br>

---

### 3. Matrix Operations & Subspaces (4 pts)

Given the matrix $A$: 

$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ -1 & -2 & 0 & -1 \end{pmatrix}$$

**(a)** Use elementary row operations to reduce $A$ to its **Row Echelon Form**. 

<br><br><br>

**(b)** Identify the pivot columns and determine the **rank** of matrix $A$.

<br><br>

**(c)** Find a basis for the **Null Space** of $A$. 

<br><br><br>

---

### 4. Linear Transformations (4 pts)

Let $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ be a linear transformation defined by $T(x,y) = (x+y, x-y)$. 

**(a)** Find the images of the standard basis vectors $\vec{e}_1 = (1,0)$ and $\vec{e}_2 = (0,1)$. 

<br><br>

**(b)** Find the matrix representation $M$ of $T$ with respect to the standard basis. 

<br><br>

**(c)** Find the vector $\vec{v}$ such that $T(\vec{v}) = (4, 2)$.

<br><br>

---

### 5. Propositional Logic (4 pts)

**(a)** Construct a truth table for the formula $\neg p \wedge (p \Rightarrow q)$. 

<br><br><br>

**(b)** Prove the logical equivalence without using a truth table (use logical laws): 
$$\neg(p \vee q) \vee (\neg p \wedge q) \equiv \neg p$$

<br><br><br>

**(c)** Negate the following statement in English. Do **not** use the word "if" or "then" in your answer: 
*"If it rains today, I will not go to the park."*

<br><br>

---

### 6. Relations (4 pts)

Let $A = \{1, 2, 3, 4\}$. Consider the relation $R$ on $A$ defined by:
$$R = \{(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)\}$$

**(a)** Draw the directed graph (digraph) OR write the matrix representation $M_R$ for this relation. 

<br><br>

**(b)** Check the following properties for $R$. Circle **Yes** or **No** and justify your answer for "Transitive". 
* **Reflexive:** Yes / No
* **Symmetric:** Yes / No
* **Transitive:** Yes / No  
    *Justification:* _____________________________________________________

**(c)** Is $R$ an equivalence relation? If yes, find the partition of $A$ induced by $R$. 

<br><br>

---

### 7. RSA Encryption (4 pts)

Bob sets up a small RSA system with modulus $n = 33$.  
*(Hint: $33 = 3 \times 11$)* 

**(a)** Find Euler's totient function $\phi(n)$. 

<br><br>

**(b)** Check if $e = 3$ is a valid public exponent. Explain why or why not. 

<br><br>

**(c)** Assume Bob chooses the public exponent $e = 7$. Use the Extended Euclidean Algorithm to find the private key $d$.  
*(Condition: $d \cdot e \equiv 1 \pmod{\phi(n)}$)*. 

<br><br><br>

**(d)** Encrypt the message $m = 2$ using the public key $(n, e) = (33, 7)$.  
*(Calculate $c = m^e \pmod n$)*. 

<br><br>