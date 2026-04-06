---
tags: [theoretical-computer-science, finite-automata, DFA, NFA, automata-theory]
topic: "Chapter 2: Finite Automata"
course: "THEORETICAL COMPUTER SCIENCE"
---

# Chapter 2: Finite Automata

> [!Note] 💡 Notation Conventions
> Throughout this note, the following conventions are standardised:
> - $Q$ = finite set of states; $\Sigma$ = input alphabet; $\delta$ = transition function; $q_0$ = initial state; $F$ = set of final (accepting) states.
> - $\lambda$ (lambda) = the **empty string** (zero symbols).
> - $\Sigma^*$ = the set of **all** strings over $\Sigma$, including $\lambda$.
> - $2^Q$ = the **power set** of $Q$ (set of all subsets of $Q$).
> - $\delta^*$ = the **extended transition function** (takes a string, not a single symbol).
> - DFA = Deterministic Finite Accepter; NFA = Nondeterministic Finite Accepter.

---

## 📑 Table of Contents

1. [[#1. Deterministic Finite Accepters (DFA)]]
   - [[#1.1 Definition]]
   - [[#1.2 DFA Operation]]
   - [[#1.3 Transition Graph]]
   - [[#1.4 Extended Transition Function δ*]]
   - [[#1.5 Language Accepted by a DFA]]
   - [[#1.6 Trap States]]
   - [[#1.7 Transition Table]]
   - [[#1.8 Regular Languages]]
2. [[#2. Nondeterministic Finite Accepters (NFA)]]
   - [[#2.1 Definition]]
   - [[#2.2 Key Differences from DFA]]
   - [[#2.3 Extended Transition Function for NFA]]
   - [[#2.4 Lambda-Closure and Move]]
   - [[#2.5 Language Accepted by an NFA]]
3. [[#3. Equivalence Between DFA and NFA]]
   - [[#3.1 Definition of Equivalence]]
   - [[#3.2 Theorem: NFA → DFA Conversion]]
   - [[#3.3 Algorithm: nfa-to-dfa]]
4. [[#4. Reduction of the Number of States in Finite Automata]]
   - [[#4.1 Inaccessible States]]
   - [[#4.2 Indistinguishable States]]
   - [[#4.3 Algorithm: mark()]]
   - [[#4.4 Algorithm: reduce()]]
   - [[#4.5 Minimality Theorem]]
5. [[#📘 Examples & Applications]]
6. [[#🗂️ Summary]]

---

## 1. Deterministic Finite Accepters (DFA)

### 1.1 Definition

> [!Definition] 📖 Definition 2.1 — Deterministic Finite Accepter (DFA)
> A **deterministic finite accepter (DFA)** is a quintuple:
> $$M = (Q,\; \Sigma,\; \delta,\; q_0,\; F)$$
> where:
> - $Q$ is a finite set of **internal states**,
> - $\Sigma$ is a finite set of symbols called the **input alphabet**,
> - $\delta : Q \times \Sigma \to Q$ is the **transition function** (maps a state and an input symbol to exactly one next state),
> - $q_0 \in Q$ is the **initial state**,
> - $F \subseteq Q$ is the set of **final (accepting) states**.

---

### 1.2 DFA Operation

> [!Note] 💡 How a DFA Processes Input
> **1.** The DFA starts in state $q_0$ with the read head on the **leftmost** symbol of the input string.
> **2.** The read head moves **left to right only**, consuming exactly **one symbol per step**.
> **3.** At each step, the current state and current symbol determine the **unique** next state via $\delta$.
> **4.** When the entire input is consumed:
> - If the current state $\in F$ → the string is **accepted**.
> - Otherwise → the string is **rejected**.

---

### 1.3 Transition Graph

> [!Note] 💡 Transition Graph Representation
> A DFA can be visualised as a **directed labelled graph**:
> - **Vertices** = states (circles).
> - **Edges** = transitions; an edge from $q_i$ to $q_j$ labelled $a$ means $\delta(q_i, a) = q_j$.
> - The **initial state** is marked with an unlabelled incoming arrow (not from any vertex).
> - **Final states** are drawn with a **double circle**.

---

### 1.4 Extended Transition Function δ*

> [!Definition] 📖 Extended Transition Function
> $\delta^* : Q \times \Sigma^* \to Q$ extends $\delta$ to accept a **string** as its second argument. It gives the state reached after reading an entire string from a given state.
>
> **Recursive definition:**
> $$\delta^*(q,\; \lambda) = q$$
> $$\delta^*(q,\; wa) = \delta\bigl(\delta^*(q,\; w),\; a\bigr) \quad \forall\, q \in Q,\; w \in \Sigma^*,\; a \in \Sigma$$
>
> **Intuition:** To compute $\delta^*(q, wa)$, first process the prefix $w$ to reach some intermediate state, then apply $\delta$ for the final symbol $a$.

> [!Example] 📘 Quick Example
> If $\delta(q_0, a) = q_1$ and $\delta(q_1, b) = q_2$, then:
> $$\delta^*(q_0,\; ab) = q_2$$

---

### 1.5 Language Accepted by a DFA

> [!Definition] 📖 Definition 2.2 — Language Accepted by a DFA
> The **language accepted** by a DFA $M = (Q, \Sigma, \delta, q_0, F)$ is:
> $$L(M) = \{\, w \in \Sigma^* : \delta^*(q_0, w) \in F \,\}$$
> The **language rejected** (complement within $\Sigma^*$) is:
> $$\overline{L(M)} = \{\, w \in \Sigma^* : \delta^*(q_0, w) \notin F \,\}$$

---

### 1.6 Trap States

> [!Definition] 📖 Trap State
> A **trap state** (also called a **dead state**) is a state from which the DFA can **never reach a final state** — once entered, the automaton is "stuck" there for all remaining input.
> - A trap state may or may not be a final state.
> - Multiple states can collectively act as a "trap state group."
> - Trap states are often used to handle **invalid** input prefixes.

> [!Example] 📘 Example — Trap State
> For the DFA recognising $L(M) = \{a^n b : n \geq 0\}$:
>
> | State | Role |
> |-------|------|
> | $q_0$ | Initial; reads $a$'s (self-loop on $a$) |
> | $q_1$ | Final; reached after one $b$ |
> | $q_2$ | Trap; reached on any symbol after $b$, or on $b$ from $q_0$ is invalid scenario |
>
> $q_2$ is the trap state — once entered (on $a$ or $b$ from $q_1$, or $b$ from initial), it loops on all inputs and is non-final.

---

### 1.7 Transition Table

> [!Note] 💡 Transition Table
> The function $\delta$ can be represented as a table:
> - **Rows** = current states.
> - **Columns** = input symbols.
> - **Cell entry** = next state $\delta(q, a)$.
>
> **Example** (for $L = \{a^n b : n \geq 0\}$, alphabet $\{a, b\}$):
>
> | | $a$ | $b$ |
> |---|---|---|
> | $q_0$ | $q_0$ | $q_1$ |
> | $q_1$ | $q_2$ | $q_2$ |
> | $q_2$ | $q_2$ | $q_2$ |
>
> Here $q_1$ is the only final state; $q_2$ is the trap state.

---

### 1.8 Regular Languages

> [!Definition] 📖 Definition 2.3 — Regular Language
> A language $L$ is called **regular** if and only if there exists some DFA $M$ such that $L = L(M)$.

> [!Note] 💡 Proving Regularity
> To show $L$ is regular: **construct a DFA** that accepts exactly $L$. The existence of such a DFA is both necessary and sufficient.

---

## 2. Nondeterministic Finite Accepters (NFA)

### 2.1 Definition

> [!Definition] 📖 Definition 2.4 — Nondeterministic Finite Accepter (NFA)
> A **nondeterministic finite accepter (NFA)** is a quintuple:
> $$M = (Q,\; \Sigma,\; \delta,\; q_0,\; F)$$
> where $Q$, $\Sigma$, $q_0$, $F$ are defined as for a DFA, but the transition function is:
> $$\delta : Q \times (\Sigma \cup \{\lambda\}) \to 2^Q$$
>
> Key differences from DFA $\delta$:
> - The **range** is $2^Q$ (a **set** of states), not a single state.
> - $\lambda$ (the empty string) is a valid **second argument** — allowing transitions without consuming input.

---

### 2.2 Key Differences from DFA

> [!Property] ⚙️ NFA vs DFA: Key Distinctions
> **1. Multiple possible next states:** $\delta(q_i, a)$ can be a set such as $\{q_0, q_2\}$ — the automaton may be in *either* state after that transition.
> **2. Lambda-transitions:** $\delta(q_i, \lambda)$ allows moving to a new state without reading any symbol (the read head is stationary).
> **3. Dead configuration:** $\delta(q_i, a) = \emptyset$ means no transition is defined — the automaton simply **stops** (this computation path fails; it does not mean rejection if other paths succeed).
> **4. Acceptance is existential:** a string is accepted if **at least one** computation path leads to a final state.

> [!Warning] ⚠️ Potential Confusion
> In an NFA, the *absence* of a transition ($\delta(q,a) = \emptyset$) does NOT mean the entire string is rejected — it means only *that particular path* dies. Other parallel paths may still succeed.

---

### 2.3 Extended Transition Function for NFA

> [!Definition] 📖 Extended Transition Function (NFA, no λ-transitions)
> **Case 1 — No λ-transitions:**
>
> $$\delta^*(q,\; \lambda) = \{q\}$$
> $$\delta^*(q,\; wa) = \bigcup_{p \,\in\, \delta^*(q,\, w)} \delta(p,\; a)$$
>
> Applying to a set $T \subseteq Q$:
> $$\delta(T,\; a) = \bigcup_{q \in T} \delta(q,\; a)$$

---

### 2.4 Lambda-Closure and Move

> [!Definition] 📖 λ-closure and move
> For a state $q$ or set $T \subseteq Q$:
>
> $$\text{move}(q, a) = \delta(q, a)$$
> $$\text{move}(T, a) = \delta(T, a) = \bigcup_{q \in T} \delta(q, a)$$
>
> $$\lambda\text{-closure}(q) = \delta^*(q, \lambda) \quad \text{(all states reachable from } q \text{ via } \lambda\text{-transitions only)}$$
> $$\lambda\text{-closure}(T) = \delta^*(T, \lambda) = \bigcup_{q \in T} \delta^*(q, \lambda)$$

> [!Definition] 📖 Extended Transition Function (NFA, with λ-transitions)
> **Case 2 — With λ-transitions:**
>
> $$\delta^*(q,\; a) = \lambda\text{-closure}\bigl(\text{move}(\lambda\text{-closure}(q),\; a)\bigr)$$
>
> $$\delta^*(T,\; a) = \lambda\text{-closure}\bigl(\text{move}(\lambda\text{-closure}(T),\; a)\bigr)$$
>
> **Step-by-step procedure for $\delta^*(q, a)$:**
> **1.** Compute $\lambda\text{-closure}(q)$ — find all states reachable from $q$ by $\lambda$-moves alone.
> **2.** From that set, compute $\text{move}(\cdot, a)$ — apply symbol $a$ to every state in the closure.
> **3.** Compute $\lambda\text{-closure}$ of the result — follow any further $\lambda$-moves.

---

### 2.5 Language Accepted by an NFA

> [!Definition] 📖 Definition 2.6 — Language Accepted by an NFA
> The **language accepted** by an NFA $M = (Q, \Sigma, \delta, q_0, F)$ is:
> $$L(M) = \{\, w \in \Sigma^* : \delta^*(q_0, w) \cap F \neq \emptyset \,\}$$
> A string $w$ is accepted if there **exists** at least one walk labelled $w$ from the initial vertex to some final vertex in the transition graph.

---

## 3. Equivalence Between DFA and NFA

### 3.1 Definition of Equivalence

> [!Definition] 📖 Definition 2.7 — Equivalent Finite Accepters
> Two finite accepters $M_1$ and $M_2$ are **equivalent** if they accept the same language:
> $$L(M_1) = L(M_2)$$

---

### 3.2 Theorem: NFA → DFA Conversion

> [!Theorem] 📌 Theorem 2.2 — Every NFA has an Equivalent DFA
> Let $L$ be the language accepted by an NFA $M_N = (Q_N, \Sigma, \delta_N, q_0, F_N)$.
> Then there exists a DFA $M_D = (Q_D, \Sigma, \delta_D, \hat{q}_0, F_D)$ such that:
> $$L = L(M_D)$$
>
> **Key insight:** Every DFA is a special case of an NFA (where $|\delta(q,a)| = 1$ for all $q, a$). The theorem states the **converse also holds** — NFAs and DFAs are **equally expressive**.

> [!Note] 💡 Correspondence
> - Each **state** of the DFA corresponds to a **subset** of states of the NFA (hence this is called the **subset construction** or **powerset construction**).
> - A DFA state is a **final state** iff its NFA-subset contains at least one NFA final state.

---

### 3.3 Algorithm: nfa-to-dfa

> [!Definition] 📖 Algorithm: nfa-to-dfa (Subset Construction)
> **Input:** NFA $M_N = (Q_N, \Sigma, \delta_N, q_0, F_N)$
> **Output:** Transition graph $G_D$ of an equivalent DFA $M_D$
>
> **1.** Create graph $G_D$ with initial vertex $\delta_N^*(q_0, \lambda)$ (the $\lambda$-closure of $q_0$). Mark it as the **initial vertex**.
> **2.** Repeat steps 3–6 until no edges are missing:
> **3.** Take any vertex $\{q_i, q_j, \ldots, q_k\}$ in $G_D$ that has **no outgoing edge** for some $a \in \Sigma$.
> **4.** Compute:
> $$\delta_N^*(\{q_i, q_j, \ldots, q_k\},\; a) = \delta_N^*(q_i, a) \cup \delta_N^*(q_j, a) \cup \cdots \cup \delta_N^*(q_k, a) = \{q_l, q_m, \ldots, q_n\}$$
> **5.** Create vertex $\{q_l, q_m, \ldots, q_n\}$ in $G_D$ if it does not already exist.
> **6.** Add edge from $\{q_i, q_j, \ldots, q_k\}$ to $\{q_l, q_m, \ldots, q_n\}$ labelled $a$.
> **7.** Every DFA state whose label contains any $q_f \in F_N$ is a **final state** of $M_D$.

> [!Warning] ⚠️ The Empty Set State
> The empty set $\emptyset$ is a valid DFA state (a trap/dead state). It must be included if any transition leads to it, with self-loops on all input symbols.

---

## 4. Reduction of the Number of States in Finite Automata

### 4.1 Inaccessible States

> [!Definition] 📖 Inaccessible State
> A state is **inaccessible** (unreachable) if it **cannot be reached** from the initial state $q_0$ by any input string.
>
> - Inaccessible states play **no role** in accepting or rejecting strings.
> - They can be **removed** (along with all their transitions) without changing $L(M)$.
> - Detection: enumerate all simple paths from $q_0$ in the transition graph; any state not appearing in any such path is inaccessible.

---

### 4.2 Indistinguishable States

> [!Definition] 📖 Definition 2.8 — Indistinguishable States
> Two states $p$ and $q$ of a DFA are **indistinguishable** if for **all** $w \in \Sigma^*$:
> $$\delta^*(q, w) \in F \iff \delta^*(p, w) \in F$$
>
> That is, starting from either $p$ or $q$, every string leads to either both accepting or both rejecting.
>
> States $p$ and $q$ are **distinguishable** by string $w$ if:
> $$\delta^*(q, w) \in F \quad \text{and} \quad \delta^*(p, w) \notin F \quad (\text{or vice versa})$$

> [!Property] ⚙️ Indistinguishability is an Equivalence Relation
> Indistinguishability is **reflexive**, **symmetric**, and **transitive**. Therefore it partitions $Q$ into **equivalence classes** — states in the same class can be **merged** into a single state.

---

### 4.3 Algorithm: mark()

> [!Definition] 📖 Algorithm: mark() — Finding Distinguishable Pairs
> **Input:** All $\binom{|Q|}{2}$ pairs $(p, q)$ from a **complete** (full) DFA.
> **Output:** All pairs marked as distinguishable.
>
> **1. Remove all inaccessible states** (via path enumeration from $q_0$).
>
> **2. Initial marking:** For all pairs $(p, q)$: if exactly one of $p$, $q$ is in $F$, **mark $(p, q)$ as distinguishable**.
>
> **3. Iterative marking:** Repeat until no new pairs are marked:
> - For all **unmarked** pairs $(p, q)$ and all $a \in \Sigma$:
>   - Compute $p_a = \delta(p, a)$ and $q_a = \delta(q, a)$.
>   - If the pair $(p_a, q_a)$ is **already marked** as distinguishable, then **mark $(p, q)$** as distinguishable.
>
> All pairs **not marked** at termination are **indistinguishable**.

> [!Theorem] 📌 Theorem 2.3 — Correctness of mark()
> The procedure `mark()`, applied to any DFA $M = (Q, \Sigma, \delta, q_0, F)$, **terminates** and correctly determines all pairs of distinguishable states.
>
> Specifically: states $q_i$ and $q_j$ are distinguishable by a string of length $n$ if and only if there exist transitions $\delta(q_i, a) = q_k$ and $\delta(q_j, a) = q_l$ for some $a \in \Sigma$, where $q_k$ and $q_l$ are distinguishable by a string of length $n - 1$.

---

### 4.4 Algorithm: reduce()

> [!Definition] 📖 Algorithm: reduce() — Constructing the Minimal DFA
> Given DFA $M = (Q, \Sigma, \delta, q_0, F)$, construct the **reduced DFA** $\hat{M} = (\hat{Q}, \Sigma, \hat{\delta}, \hat{q}_0, \hat{F})$:
>
> **1.** Run `mark()` to generate the **equivalence classes** of indistinguishable states, e.g., $\{q_i, q_j, \ldots, q_k\}$.
>
> **2.** For each equivalence class $\{q_i, q_j, \ldots, q_k\}$, create a state labelled $ij\ldots k$ in $\hat{M}$.
>
> **3.** For each transition $\delta(q_r, a) = q_p$ in $M$:
> - Find the class containing $q_r$, say $\{q_i, q_j, \ldots, q_k\}$ (class label $ij\ldots k$).
> - Find the class containing $q_p$, say $\{q_l, q_m, \ldots, q_n\}$ (class label $lm\ldots n$).
> - Add rule $\hat{\delta}(ij\ldots k,\; a) = lm\ldots n$.
>
> **4.** The initial state $\hat{q}_0$ is the class whose label **contains** $0$ (i.e., the class of $q_0$).
>
> **5.** $\hat{F}$ = all states of $\hat{M}$ whose label contains $i$ such that $q_i \in F$.

---

### 4.5 Minimality Theorem

> [!Theorem] 📌 Theorem 2.4 — Minimality of the Reduced DFA
> Given any DFA $M$, applying `reduce()` yields a DFA $\hat{M}$ such that:
> $$L(M) = L(\hat{M})$$
> Furthermore, $\hat{M}$ is **minimal** — no DFA with fewer states accepts $L(M)$.

---

## 📘 Examples & Applications

---

### Example 1 — Tracing a DFA

**Using:** DFA definition, extended transition function $\delta^*$, acceptance condition.

**Setup:** DFA $M = (Q, \Sigma, \delta, q_0, F)$ with:
$$Q = \{q_0, q_1, q_2\},\quad \Sigma = \{0, 1\},\quad F = \{q_1\}$$

Transition function:

| | $0$ | $1$ |
|---|---|---|
| $q_0$ | $q_0$ | $q_1$ |
| $q_1$ | $q_0$ | $q_2$ |
| $q_2$ | $q_2$ | $q_1$ |

**Question:** Is $w = 0001$ accepted?

**Solution:**

$$\delta^*(q_0,\; \lambda) = q_0$$

Step 1 — read $0$: $\delta(q_0, 0) = q_0$

Step 2 — read $0$: $\delta(q_0, 0) = q_0$

Step 3 — read $0$: $\delta(q_0, 0) = q_0$

Step 4 — read $1$: $\delta(q_0, 1) = q_1$

Final state $= q_1 \in F$ → **ACCEPTED** ✓

---

### Example 2 — Computing δ* for an NFA (no λ-transitions)

**Using:** NFA extended transition function (Case 1, no λ-transitions), set-union rule.

**Setup:** NFA with states $\{q_0, q_1, q_2\}$, alphabet $\{0, 1\}$, $F = \{q_2\}$:

| | $0$ | $1$ |
|---|---|---|
| $q_0$ | $\{q_0, q_1\}$ | $\{q_0\}$ |
| $q_1$ | $\emptyset$ | $\{q_2\}$ |
| $q_2$ | $\emptyset$ | $\emptyset$ |

**Question:** Compute $\delta^*(q_0,\; 00101)$ and determine if it is accepted.

**Solution:**

$$\delta^*(q_0,\; \lambda) = \{q_0\}$$

$$\delta^*(q_0,\; 0) = \delta(q_0, 0) = \{q_0, q_1\}$$

$$\delta^*(q_0,\; 00) = \delta(q_0, 0) \cup \delta(q_1, 0) = \{q_0, q_1\} \cup \emptyset = \{q_0, q_1\}$$

$$\delta^*(q_0,\; 001) = \delta(q_0, 1) \cup \delta(q_1, 1) = \{q_0\} \cup \{q_2\} = \{q_0, q_2\}$$

$$\delta^*(q_0,\; 0010) = \delta(q_0, 0) \cup \delta(q_2, 0) = \{q_0, q_1\} \cup \emptyset = \{q_0, q_1\}$$

$$\delta^*(q_0,\; 00101) = \delta(q_0, 1) \cup \delta(q_1, 1) = \{q_0\} \cup \{q_2\} = \{q_0, q_2\}$$

Result: $\{q_0, q_2\}$. Since $q_2 \in F$ and $\{q_0, q_2\} \cap F = \{q_2\} \neq \emptyset$ → **ACCEPTED** ✓

---

### Example 3 — Computing δ* for an NFA with λ-transitions

**Using:** $\lambda$-closure, move, extended transition function (Case 2).

**Setup:** NFA with states $\{q_0, q_1, q_2, q_3, q_4, q_5\}$, alphabet $\{a\}$:

| | $a$ | $\lambda$ |
|---|---|---|
| $q_0$ | $q_4$ | $q_1$ |
| $q_1$ | $q_0, q_3$ | $q_2$ |
| $q_2$ | — | — |
| $q_3$ | — | — |
| $q_4$ | — | $q_5$ |
| $q_5$ | — | — |

**Question:** Compute $\delta^*(q_0,\; a)$.

**Solution:**

$$\delta^*(q_0, a) = \lambda\text{-closure}\bigl(\text{move}(\lambda\text{-closure}(q_0),\; a)\bigr)$$

**Step 1 — $\lambda$-closure($q_0$):**
From $q_0$: $\lambda$-move → $q_1$; from $q_1$: $\lambda$-move → $q_2$; no further $\lambda$-moves.
$$\lambda\text{-closure}(q_0) = \{q_0, q_1, q_2\}$$

**Step 2 — move($\{q_0, q_1, q_2\}$, $a$):**
$$\delta(q_0, a) = \{q_4\},\quad \delta(q_1, a) = \{q_0, q_3\},\quad \delta(q_2, a) = \emptyset$$
$$\text{move}(\{q_0, q_1, q_2\}, a) = \{q_4\} \cup \{q_0, q_3\} \cup \emptyset = \{q_0, q_3, q_4\}$$

**Step 3 — $\lambda$-closure($\{q_0, q_3, q_4\}$):**
- From $q_0$: $\lambda \to q_1 \to q_2$.
- From $q_3$: no $\lambda$-moves.
- From $q_4$: $\lambda \to q_5$.
$$\lambda\text{-closure}(\{q_0, q_3, q_4\}) = \{q_0, q_1, q_2, q_3, q_4, q_5\}$$

**Result:**
$$\delta^*(q_0, a) = \{q_0, q_1, q_2, q_3, q_4, q_5\}$$

---

### Example 4 — NFA to DFA Conversion (Subset Construction)

**Using:** Algorithm nfa-to-dfa, $\lambda$-closure, subset construction.

**Setup:** NFA with states $\{q_0, q_1, q_2\}$, alphabet $\{a, b\}$, $F_N = \{q_1\}$:

| | $a$ | $b$ | $\lambda$ |
|---|---|---|---|
| $q_0$ | $q_1$ | — | — |
| $q_1$ | $q_1$ | — | $q_2$ |
| $q_2$ | — | $q_0$ | — |

**Solution:**

**Step 1:** Initial DFA state = $\delta_N^*(q_0, \lambda) = \{q_0\}$.

**Step 2:** Compute transitions from $\{q_0\}$:
$$\delta_N^*(\{q_0\}, a) = \{q_1, q_2\} \quad (\text{since } \delta(q_0,a) = q_1 \text{ and } \lambda\text{-closure}(q_1) = \{q_1, q_2\})$$
$$\delta_N^*(\{q_0\}, b) = \emptyset$$

**Step 3:** Compute transitions from $\{q_1, q_2\}$:
$$\delta_N^*(\{q_1, q_2\}, a) = \{q_1, q_2\}$$
$$\delta_N^*(\{q_1, q_2\}, b) = \{q_0\}$$

**Step 4:** Compute transitions from $\{q_0\}$ — already done. Compute from $\emptyset$:
$$\delta_N^*(\emptyset, a) = \emptyset,\quad \delta_N^*(\emptyset, b) = \emptyset$$

**Resulting DFA transition table:**

| DFA State | $a$ | $b$ | Final? |
|---|---|---|---|
| $\{q_0\}$ (initial) | $\{q_1, q_2\}$ | $\emptyset$ | No |
| $\{q_1, q_2\}$ | $\{q_1, q_2\}$ | $\{q_0\}$ | **Yes** ($q_1 \in F_N$) |
| $\emptyset$ | $\emptyset$ | $\emptyset$ | No |

---

### Example 5 — DFA State Reduction using mark() and reduce()

**Using:** Algorithms mark() and reduce(), indistinguishable states, equivalence classes.

**Setup:** DFA with $Q = \{q_0, q_1, q_2, q_3, q_4\}$, $\Sigma = \{0, 1\}$, $F = \{q_4\}$:

| | $0$ | $1$ |
|---|---|---|
| $q_0$ | $q_1$ | $q_3$ |
| $q_1$ | $q_2$ | $q_4$ |
| $q_2$ | $q_1$ | $q_4$ |
| $q_3$ | $q_2$ | $q_4$ |
| $q_4$ | $q_4$ | $q_4$ |

**Step 1 — Remove inaccessible states:**
All states reachable from $q_0$ → all five states are accessible.

**Step 2 — Initial marking (one in $F$, one not):**
$q_4 \in F$; all others $\notin F$. Mark all pairs involving $q_4$:
$(q_0, q_4)$✓, $(q_1, q_4)$✓, $(q_2, q_4)$✓, $(q_3, q_4)$✓.

Pairs among $\{q_0, q_1, q_2, q_3\}$ remain **unmarked** initially:
$(q_0,q_1)$, $(q_0,q_2)$, $(q_0,q_3)$, $(q_1,q_2)$, $(q_1,q_3)$, $(q_2,q_3)$.

**Step 3 — Iterative marking:**

Check $(q_0, q_1)$:
- On $1$: $\delta(q_0,1) = q_3$, $\delta(q_1,1) = q_4$ → pair $(q_3,q_4)$ is marked → **mark $(q_0,q_1)$** ✓

Check $(q_0, q_2)$:
- On $1$: $\delta(q_0,1) = q_3$, $\delta(q_2,1) = q_4$ → pair $(q_3,q_4)$ marked → **mark $(q_0,q_2)$** ✓

Check $(q_0, q_3)$:
- On $1$: $\delta(q_0,1) = q_3$, $\delta(q_3,1) = q_4$ → pair $(q_3,q_4)$ marked → **mark $(q_0,q_3)$** ✓

Check $(q_1, q_2)$:
- On $0$: $\delta(q_1,0) = q_2$, $\delta(q_2,0) = q_1$ → pair $(q_1,q_2)$ itself (not yet resolved). On $1$: $\delta(q_1,1) = q_4$, $\delta(q_2,1) = q_4$ → $(q_4,q_4)$ not marked. → **not marked yet**.
- On next iteration: $(q_1,q_2)$ on $0$ gives $(q_2,q_1)$ = same pair — still unmarked. → **$(q_1,q_2)$ remains unmarked**.

Check $(q_1, q_3)$:
- On $1$: $\delta(q_1,1) = q_4$, $\delta(q_3,1) = q_4$ → pair $(q_4,q_4)$ not marked. On $0$: $\delta(q_1,0) = q_2$, $\delta(q_3,0) = q_2$ → $(q_2,q_2)$ not marked. → **$(q_1,q_3)$ remains unmarked**.

Check $(q_2, q_3)$:
- On $0$: $\delta(q_2,0) = q_1$, $\delta(q_3,0) = q_2$ → pair $(q_1,q_2)$ unmarked. On $1$: both go to $q_4$ → not marked. → **$(q_2,q_3)$ remains unmarked**.

**Equivalence classes:**
$$\{q_0\},\quad \{q_1, q_2, q_3\},\quad \{q_4\}$$

**Step 4 — Build reduced DFA (rename classes):**

| Class | Label |
|---|---|
| $\{q_0\}$ | $0$ |
| $\{q_1, q_2, q_3\}$ | $123$ |
| $\{q_4\}$ | $4$ |

Transitions of reduced DFA:

| | $0$ | $1$ |
|---|---|---|
| $0$ (initial) | $123$ | $123$ |
| $123$ | $123$ | $4$ |
| $4$ (final) | $4$ | $4$ |

The original 5-state DFA reduces to a **3-state minimal DFA**.

---

### Example 6 — Exam-Style Combined Problem

**Using:** DFA construction, regularity, NFA-to-DFA, state reduction.

**Question:** 
**(a)** Show that $L = \{awa : w \in \{a,b\}^*\}$ is regular by constructing a DFA.
**(b)** How many states are needed? Is the DFA minimal?

**Solution (a) — DFA Construction:**

The language consists of strings that **start and end with** $a$, with anything in between.

States track progress:

| State | Meaning |
|---|---|
| $q_0$ | Initial; no input read yet |
| $q_1$ | Trap for strings starting with $b$ |
| $q_2$ | Read first $a$; in the middle portion |
| $q_3$ | **Final**: last symbol read was $a$ (after at least one $a$ at start) |

Transitions ($\Sigma = \{a,b\}$):

| | $a$ | $b$ |
|---|---|---|
| $q_0$ | $q_2$ | $q_1$ |
| $q_1$ | $q_1$ | $q_1$ |
| $q_2$ | $q_3$ | $q_2$ |
| $q_3$ | $q_3$ | $q_2$ |

$F = \{q_3\}$.

This DFA accepts: single $a$ (path $q_0 \xrightarrow{a} q_2 \xrightarrow{?}$... wait — $q_2$ reached after first $a$; to accept we need another $a$, so $q_3$ is reached on the second $a$). For $w = \lambda$: string is $aa$, path $q_0 \to q_2 \to q_3$ ✓. For $w = b$: string is $aba$, path $q_0 \to q_2 \to q_2 \to q_3$ ✓.

**Solution (b):** The DFA has 4 states. $q_1$ is a trap (non-final). To verify minimality, run `mark()`: $q_0$, $q_2$, $q_1$ are all non-final but distinguishable from each other (different future behaviours), and all are distinguishable from $q_3$ (final). The DFA is minimal with 4 states.

Since a DFA accepting $L$ exists → $L$ is **regular** ✓.

---

## 🗂️ Summary

### DFA
- Defined by $(Q, \Sigma, \delta, q_0, F)$; $\delta: Q \times \Sigma \to Q$ (exactly one next state).
- Accepts $w$ iff $\delta^*(q_0, w) \in F$.
- $\delta^*(q, \lambda) = q$; $\delta^*(q, wa) = \delta(\delta^*(q,w), a)$.
- **Trap state**: state from which $F$ is unreachable; safe to include for completeness.
- **Regular language**: $L$ is regular $\iff$ some DFA $M$ has $L(M) = L$.

### NFA
- Defined by $(Q, \Sigma, \delta, q_0, F)$; $\delta: Q \times (\Sigma \cup \{\lambda\}) \to 2^Q$ (set of next states).
- Accepts $w$ iff $\delta^*(q_0, w) \cap F \neq \emptyset$ (at least one accepting path).
- $\delta(q_i, a) = \emptyset$ is a dead configuration (that path fails; other paths may succeed).
- **λ-transition**: move without consuming input.
- **With λ-transitions**: $\delta^*(q, a) = \lambda\text{-closure}(\text{move}(\lambda\text{-closure}(q), a))$.

### DFA ↔ NFA Equivalence
- Every DFA is trivially an NFA.
- Every NFA can be converted to an equivalent DFA via **subset construction** (Theorem 2.2).
- DFA states = subsets of NFA states; DFA final states = subsets containing an NFA final state.
- Worst case: NFA with $n$ states → DFA with up to $2^n$ states.

### State Minimisation
- **Remove inaccessible states** first (states unreachable from $q_0$).
- Run **mark()**: iteratively mark pairs $(p,q)$ as distinguishable, starting from pairs where one is final and one is not.
- Run **reduce()**: merge all indistinguishable states into equivalence classes → one state per class.
- Result is the **unique minimal DFA** for $L(M)$ (Theorem 2.4).

### Quick Reference: Key Formulas

| Concept | Formula |
|---|---|
| DFA acceptance | $L(M) = \{w \in \Sigma^* : \delta^*(q_0, w) \in F\}$ |
| NFA acceptance | $L(M) = \{w \in \Sigma^* : \delta^*(q_0, w) \cap F \neq \emptyset\}$ |
| DFA $\delta^*$ (inductive) | $\delta^*(q, wa) = \delta(\delta^*(q,w), a)$ |
| NFA $\delta^*$ (with $\lambda$) | $\delta^*(q, a) = \lambda\text{-cl}(\text{move}(\lambda\text{-cl}(q), a))$ |
| NFA→DFA state | $\delta_D(S, a) = \bigcup_{q \in S} \delta_N(q, a)$ |
| Distinguishable | $\exists w: \delta^*(p,w) \in F \oplus \delta^*(q,w) \in F$ |
