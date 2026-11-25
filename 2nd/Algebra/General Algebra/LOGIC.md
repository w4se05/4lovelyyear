# Propositional Logic & Proofs

## I. Conceptual Section (Teach Mode)

### 1. Propositions and Connectives
> [!Definition] Proposition
> A **proposition** (or statement) is a declarative sentence that is either **True (T)** or **False (F)**, but not both.
> * *Example:* "Messi is a football player" (T). "$x+1=5$" is **not** a proposition (it depends on $x$).

**Logical Connectives:**
Let $p$ and $q$ be propositions.

| Name | Symbol | Meaning | False Condition |
| :--- | :---: | :--- | :--- |
| **Negation** | $\neg p$ | Not $p$ | True if $p$ is F. |
| **Conjunction** | $p \wedge q$ | $p$ AND $q$ | False if any is F. |
| **Disjunction** | $p \vee q$ | $p$ OR $q$ | False only if **both** are F. |
| **Implication** | $p \rightarrow q$ | If $p$, then $q$ | False only if $p=T$ and $q=F$. |
| **Biconditional** | $p \leftrightarrow q$ | $p$ iff $q$ | False if truth values differ. |

> [!Note] Priority of Operations
> 1. $\neg$ (Negation)
> 2. $\wedge$ (Conjunction)
> 3. $\vee$ (Disjunction)
> 4. $\rightarrow$ (Implication)
> 5. $\leftrightarrow$ (Equivalence)

### 2. Logical Equivalence & Normal Forms

> [!Definition] Classifications
> * **Tautology:** A statement that is always **True** regardless of inputs (e.g., $p \vee \neg p$).
> * **Contradiction:** A statement that is always **False** (e.g., $p \wedge \neg p$).
> * **Satisfiable:** A statement that yields True for **at least one** assignment.

> [!Property] Important Equivalences
> * **Double Negation:** $\neg(\neg p) \equiv p$
> * **Idempotent:** $p \vee p \equiv p$
> * **De Morgan's Laws:**
>     * $\neg(p \wedge q) \equiv \neg p \vee \neg q$
>     * $\neg(p \vee q) \equiv \neg p \wedge \neg q$
> * **Implication:** $p \rightarrow q \equiv \neg p \vee q$
> * **Contrapositive:** $p \rightarrow q \equiv \neg q \rightarrow \neg p$
> *  **Distributive Law:** $p \wedge (\neg q \vee \neg r) = (p \wedge \neg q) \vee (p \wedge \neg r)$

> [!Definition] Normal Forms
> * **Literal:** A variable ($p$) or its negation ($\neg p$).
> * **Disjunctive Normal Form (DNF):** Sum of products (OR of ANDs). Example: $(p \wedge q) \vee (\neg p \wedge r)$.
> * **Conjunctive Normal Form (CNF):** Product of sums (AND of ORs). Example: $(p \vee q) \wedge (\neg p \vee r)$.

**Boolean Functions:**
For $n$ variables, there are $2^n$ rows in a truth table, and $2^{2^n}$ possible boolean functions.

### 3. Predicates and Quantifiers
Used when statements depend on variables (e.g., $P(x)$).

> [!Definition] Quantifiers
> * **Universal ($\forall$):** "For all $x$, $P(x)$ is true."
> * **Existential ($\exists$):** "There exists an $x$ such that $P(x)$ is true."

> [!Property] Negating Quantifiers (De Morgan for Quantifiers)
> * $\neg (\forall x P(x)) \equiv \exists x \neg P(x)$
> * $\neg (\exists x P(x)) \equiv \forall x \neg P(x)$

### 4. Inference and Proofs

> [!Definition] Inference Rules
> Mechanisms to derive new true statements from premises.
## Tautologies (Valid Logical Forms)

These are statements that are true under all possible interpretations, proving valid arguments.

### 1. Law of Excluded Middle

Formula:$$P \lor \neg P$$
> Meaning: "It's raining or not raining."
> A proposition is either true or false; there is no middle ground.

### 2. Modus Ponens (Affirming the Antecedent)

Formula:
$$[(P \to Q) \land P] \to Q$$

> **Meaning:** If $P$ implies $Q$, and $P$ is true, then $Q$ is true.

### 3. Modus Tollens (Denying the Consequent)
Formula:
$$[(P \to Q) \land \neg Q] \to \neg P$$
> **Meaning:** If $P$ implies $Q$, and $Q$ is false, then $P$ is false.
### 4. Disjunctive Syllogism
Formula:
$$[(P \lor Q) \land \neg P] \to Q$$
> **Meaning:** If $P$ or $Q$ is true, and $P$ is false, then $Q$ must be true.

### 5. Law of Syllogism (Transitivity)
Formula:
$$[(P \to Q) \land (Q \to R)] \to (P \to R)$$

> **Meaning:** Transitivity of implication. If $P$ leads to $Q$, and $Q$ leads to $R$, then $P$ leads to $R$.

> [!Definition] Proof Methods
> 1.  **Direct Proof:** Assume $p$, show $q$.
> 2.  **Contrapositive:** Assume $\neg q$, show $\neg p$ (Equivalent to $p \rightarrow q$).
> 3.  **Contradiction:** Assume $\neg p$ is true, derive a contradiction ($r \wedge \neg r$).

---

## II. Application Section (Exam Mode)

### 📘 Examples & Applications

#### Example 1: Constructing CNF/DNF
**(Using: Truth Tables, Normal Forms)**
Find the CNF and DNF for $f(p, q) = p \leftrightarrow q$.

**Solution:**
Construct the truth table:

| $p$ | $q$ | $p \leftrightarrow q$ |
| :---: | :---: | :---: |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

* **DNF (Look at T rows):** Take the conjunction of literals for True rows.
    Row 1 ($p, q$): $(p \wedge q)$
    Row 4 ($\neg p, \neg q$): $(\neg p \wedge \neg q)$
    $$DNF: (p \wedge q) \vee (\neg p \wedge \neg q)$$

* **CNF (Look at F rows):** Take the disjunction of **negated** literals for False rows.
    Row 2 ($p=T, q=F$): $(\neg p \vee q)$
    Row 3 ($p=F, q=T$): $(p \vee \neg q)$
    $$CNF: (\neg p \vee q) \wedge (p \vee \neg q)$$

#### Example 2: Proof by Contrapositive
**(Using: Proof Methods, Number Theory definitions)**
Prove: If $n^2$ is even, then $n$ is even.

**Solution:**
* **Statement:** $P \rightarrow Q$, where $P$: "$n^2$ is even", $Q$: "$n$ is even".
* **Contrapositive ($\neg Q \rightarrow \neg P$):** If $n$ is odd, then $n^2$ is odd.
* **Proof:**
    Assume $n$ is odd. Then $n = 2k + 1$ for some integer $k$.
    $$n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
    Let $m = 2k^2 + 2k$. Then $n^2 = 2m + 1$.
    By definition, $2m + 1$ is an odd number.
    Therefore, $n^2$ is odd.
    Since the contrapositive is true, the original statement is true.

#### Example 3: Simplifying Logical Expressions
**(Using: Logical Equivalences)**
Simplify: $\neg (p \vee q) \vee (\neg p \wedge q)$.

**Solution:**
1.  Apply De Morgan's to first part:
    $(\neg p \wedge \neg q) \vee (\neg p \wedge q)$
2.  Apply Distributive Law (factor out $\neg p$):
    $\neg p \wedge (\neg q \vee q)$
3.  Apply Inverse Law ($\neg q \vee q \equiv T$):
    $\neg p \wedge T$
4.  Apply Identity Law:
    $\neg p$

---

## III. Summary

* **Order:** $\neg, \wedge, \vee, \rightarrow, \leftrightarrow$.
* **Implication:** $p \rightarrow q \equiv \neg p \vee q$.
* **Negation:** $\neg(A \rightarrow B) \equiv A \wedge \neg B$.
* **Quantifiers:** Negating flips the symbol ($\forall \leftrightarrow \exists$) and negates the predicate.
* **SAT Problem:** Determining if a boolean formula is satisfiable is generally hard (no efficient algorithm known).