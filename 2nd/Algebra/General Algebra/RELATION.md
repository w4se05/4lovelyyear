# Relations & Set Theory

## I. Conceptual Section (Teach Mode)

### 1. Set Theory Review
> [!Definition] Set Operations
> Let $A, B$ be subsets of a universal set $U$.
> * **Union ($A \cup B$):** Elements in $A$ OR $B$.
> * **Intersection ($A \cap B$):** Elements in $A$ AND $B$.
> * **Difference ($A \setminus B$):** Elements in $A$ but NOT in $B$.
> * **Symmetric Difference ($A \oplus B$):** $(A \cup B) \setminus (A \cap B)$.
> * **Complement ($\bar{A}$):** Elements in $U$ but not in $A$.
> * **Power Set $\mathcal{P}(A)$:** Set of all subsets of $A$. Cardinality $|\mathcal{P}(A)| = 2^{|A|}$.

> [!Note] Representation
> Sets can be represented by **Bit Strings** of length $n$ (where $n=|U|$).
> * Union $\to$ Bitwise OR
> * Intersection $\to$ Bitwise AND

A function is invertible if it is **injective** (one-to-one). That is, if $f(a) = f(b)$, then $a$ must equal $b$.
### 2. Binary Relations
> [!Definition] Relation
> A binary relation $R$ from set $X$ to $Y$ is a subset of the Cartesian product $X \times Y$.
> $$R \subseteq \{(x,y) \mid x \in X, y \in Y\}$$

**Matrix Representation ($M_R$):**
If $X = \{x_1, \dots, x_m\}$ and $Y = \{y_1, \dots, y_n\}$, $M_R$ is an $m \times n$ binary matrix where entry $a_{ij} = 1$ if $(x_i, y_j) \in R$, else $0$.

**Operations:**
* **Inverse ($R^{-1}$):** $\{(y,x) \mid (x,y) \in R\}$. Matrix: $M_{R^{-1}} = (M_R)^T$.
* **Composition ($S \circ R$):** Relation from $X$ to $Z$ via $Y$. $(x, z) \in S \circ R$ if $\exists y$ such that $(x,y) \in R$ and $(y,z) \in S$.  Matrix: Boolean product $M_R \odot M_S$.

### 3. Properties of Relations (on Set X)
Let $R$ be a relation on $X$ ($R \subseteq X \times X$).

| Property           | Definition                                            | Matrix Characteristic                         |
| :----------------- | :---------------------------------------------------- | :-------------------------------------------- |
| **Reflexive**      | $\forall x, (x,x) \in R$                              | Main diagonal is all 1s.                      |
| **Symmetric**      | $(x,y) \in R \implies (y,x) \in R$                    | $M_R = (M_R)^T$ (Symmetric matrix).           |
| **Anti-Symmetric** | $(x,y) \in R \wedge (y,x) \in R \implies x=y$         | $a_{ij}=1 \wedge i \neq j \implies a_{ji}=0$. |
| **Transitive**     | $(x,y) \in R \wedge (y,z) \in R \implies (x,z) \in R$ | $M_{R^2} \le M_R$ (Boolean).                  |

### 4. Closures
If a relation $R$ lacks a property (e.g., transitivity), we can add the minimum edges necessary to satisfy it.

* **Reflexive Closure:** $R \cup \{(x,x) \mid \forall x\}$.
* **Symmetric Closure:** $R \cup R^{-1}$.
* **Transitive Closure ($R^*$):** $R \cup R^2 \cup R^3 \dots \cup R^n$.
    * Computed efficiently using **Warshall's Algorithm**: $$M_{k} = M_{k-1} \lor (C_{k-1} \odot R_{k-1})$$ with K = size of R i.g 3x3 => 3 step, $M_{R^*}=M_{3}$
	    and $M_{0}=M_{R}$

### 5. Equivalence Relations & Partial Orders

> [!Definition] Equivalence Relation
> A relation that is **Reflexive**, **Symmetric**, and **Transitive**.
> * **Equivalence Class $[a]_R$:** $\{x \mid (a,x) \in R\}$.
> * **Partition:** Equivalence classes partition the set $X$ into disjoint blocks.

> [!Definition] Partial Order (Poset)
> A relation that is **Reflexive**, **Anti-Symmetric**, and **Transitive**.
> * Notation: $(X, \preceq)$.
> * **Hasse Diagrams:** A visual representation of a finite poset. Edges point upwards; transitive and self-loops are omitted. "Covers" relations are drawn.

---

## II. Application Section (Exam Mode)

### 📘 Examples & Applications

#### Example 1: Matrix Operations & Composition
**(Using: Matrix Representation, Composition)**
Let $X = \{1, 2\}$, $Y=\{a, b\}$, $Z=\{\alpha, \beta\}$.
$R = \{(1, a), (1, b), (2, a)\}$ and $S = \{(a, \alpha), (b, \beta)\}$.
Find $M_R, M_S$ and $M_{S \circ R}$.

**Solution:**
1.  $M_R$ (rows 1,2; cols a,b):
    $$M_R = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
2.  $M_S$ (rows a,b; cols $\alpha, \beta$):
    $$M_S = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
3.  $M_{S \circ R} = M_R \odot M_S$ (Boolean multiplication):
    Row 1 $\times$ Col 1: $(1 \wedge 1) \vee (1 \wedge 0) = 1$.
    Row 1 $\times$ Col 2: $(1 \wedge 0) \vee (1 \wedge 1) = 1$.
    Row 2 $\times$ Col 1: $(1 \wedge 1) \vee (0 \wedge 0) = 1$.
    Row 2 $\times$ Col 2: $(1 \wedge 0) \vee (0 \wedge 1) = 0$.
    $$M_{S \circ R} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
    Relation: $S \circ R = \{(1, \alpha), (1, \beta), (2, \alpha)\}$.

#### Example 2: Analyzing Properties
**(Using: Relation definitions)**
Let $A = \{1, 2, 3\}$. $R = \{(1,1), (1,2), (2,1), (2,2), (3,3)\}$.
Determine the properties of $R$.

**Solution:**
* **Reflexive?** Yes. $(1,1), (2,2), (3,3)$ are all present.
* **Symmetric?** Yes. $(1,2) \in R$ and $(2,1) \in R$.
* **Anti-Symmetric?** No. $(1,2)$ and $(2,1)$ exist, but $1 \neq 2$.
* **Transitive?** Yes. Checking combinations: $(1,2) \wedge (2,1) \to (1,1)$ (Present).
* **Conclusion:** $R$ is an **Equivalence Relation**.

#### Example 3: Warshall's Algorithm (Conceptual Step)
**(Using: Transitive Closure)**
To find $R^*$ for matrix $M_R$:
Iterate $k$ from $1$ to $n$.
$$w_{ij}^{[k]} = w_{ij}^{[k-1]} \vee (w_{ik}^{[k-1]} \wedge w_{kj}^{[k-1]})$$
*Meaning:* If there is a path from $i \to k$ and $k \to j$, add a path $i \to j$.

---

## III. Summary

* **Cardinality:** $|A \times B| = |A| \cdot |B|$. $|\mathcal{P}(A)| = 2^{|A|}$.
* **Properties:**
    * Reflexive: Diagonals are 1.
    * Symmetric: $M = M^T$.
    * Transitive: $R^2 \subseteq R$.
* **Equivalence Rel:** Partition the set.
* **Poset:** Used for scheduling/ordering. Hasse diagrams visualize "covering".