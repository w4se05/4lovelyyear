---
tags:
  - TCS
  - midterm
  - finite-automata
  - cheatsheet
course: Theoretical Computer Science
topic: Finite Automata
date: 2026-04-21
---

# 📘 TCS Midterm Cheatsheet — Finite Automata

> [!info] Source
> 100% based on lecture slides: **"Theoretical Computer Science — FINITE AUTOMATA"** (76 slides)
> Lecturers: Ngoc H. Tran, Ph.D. & Viet Vu, Ph.D. — Vietnamese-German University

---

## 1️⃣ Deterministic Finite Accepters (DFA)

### 📐 Formal Definition (Definition 2.1)

> [!important] Definition 2.1
> A **Deterministic Finite Accepter (DFA)** is defined by the quintuple:
> $$M = (Q,\; \Sigma,\; \delta,\; q_0,\; F)$$
> where:
> - $Q$ — finite set of **internal states**
> - $\Sigma$ — finite set of symbols called the **input alphabet**
> - $\delta: Q \times \Sigma \to Q$ — **transition function** (total function)
> - $q_0 \in Q$ — **initial state**
> - $F \subseteq Q$ — set of **final (accepting) states**

### 🔁 Extended Transition Function ($\delta^*$)

> [!note] Definition
> The extended transition function $\delta^*$ is defined recursively:
> $$\delta^*(q, \lambda) = q$$
> $$\delta^*(q, wa) = \delta(\delta^*(q, w),\; a)$$
> where $w \in \Sigma^*$ and $a \in \Sigma$.

**Meaning:** $\delta^*(q, w)$ gives the state reached after reading the entire string $w$ starting from state $q$.

### ✅ Language Accepted by a DFA (Definition 2.2)

> [!important] Definition 2.2
> The language accepted by a DFA $M = (Q, \Sigma, \delta, q_0, F)$ is:
> $$L(M) = \{w \in \Sigma^* : \delta^*(q_0, w) \in F\}$$

- A string $w$ is **accepted** if $\delta^*(q_0, w) \in F$
- A string $w$ is **rejected** if $\delta^*(q_0, w) \notin F$

### 📋 Key Concepts

| Concept | Description |
|---|---|
| **Configuration** | A pair $(q, w)$ where $q$ is current state, $w$ is unread input |
| **Trap State** | A non-final state with all transitions looping back to itself |
| **Transition Table** | Tabular representation of $\delta$ |
| **Transition Graph** | Directed graph representation of the DFA |
| **Dead Configuration** | Configuration from which no further moves are possible |

### 🔄 Transition Table Format

> [!tip] How to read a Transition Table
> - One **row** per state in $Q$
> - One **column** per input symbol in $\Sigma$
> - The entry at row $q$, column $a$ gives $\delta(q, a)$
> - Mark initial state with $\to$ and final states with $*$

### 📝 DFA Examples from Slides

#### Example (a): Prefix "ab"
Find a DFA recognizing all strings on $\Sigma = \{a, b\}$ starting with prefix **"ab"**.

| | $a$ | $b$ |
|---|---|---|
| $\to q_0$ | $q_1$ | $q_3$ |
| $q_1$ | $q_3$ | $q_2$ |
| $*q_2$ | $q_2$ | $q_2$ |
| $q_3$ | $q_3$ | $q_3$ |

- $q_0$: start, waiting for $a$
- $q_1$: read $a$, waiting for $b$
- $q_2$: **final** — read "ab", accept everything after
- $q_3$: **trap** — wrong prefix, reject

#### Example (b): No substring "001"
Find a DFA on $\Sigma = \{0, 1\}$ that accepts all strings **except** those containing "001".

| | $0$ | $1$ |
|---|---|---|
| $\to *\lambda$ | $0$ | $\lambda$ |
| $*0$ | $00$ | $\lambda$ |
| $*00$ | $00$ | $001$ |
| $001$ | $001$ | $001$ |

- States track how much of "001" has been seen
- $001$ is a **trap state** (non-final)

### ✏️ DFA Construction Exercises

For $\Sigma = \{a, b\}$, construct DFAs accepting:
- (a) All strings with **exactly one** $a$
- (b) All strings with **at least one** $a$
- (c) All strings with **no more than three** $a$'s
- (d) All strings with **at least one $a$ and exactly two $b$'s**

---

## 2️⃣ Nondeterministic Finite Accepters (NFA)

### 📐 Formal Definition (Definition 2.4)

> [!important] Definition 2.4
> A **Nondeterministic Finite Accepter (NFA)** is defined by:
> $$M = (Q,\; \Sigma,\; \delta,\; q_0,\; F)$$
> where:
> - $Q$ — finite set of internal states
> - $\Sigma$ — input alphabet
> - $\delta: Q \times (\Sigma \cup \{\lambda\}) \to 2^Q$ — **transition function**
> - $q_0 \in Q$ — initial state
> - $F \subseteq Q$ — set of final states

### 🆚 DFA vs NFA — Key Differences

| Feature | DFA | NFA |
|---|---|---|
| **Transition function range** | $Q$ (single state) | $2^Q$ (set of states) |
| **$\lambda$-transitions** | ❌ Not allowed | ✅ Allowed |
| **Determinism** | Exactly one next state | Zero or more next states |
| **$\delta(q, a) = \emptyset$** | Not possible | Allowed (**dead configuration**) |
| **Transition function** | $\delta: Q \times \Sigma \to Q$ | $\delta: Q \times (\Sigma \cup \{\lambda\}) \to 2^Q$ |

### 🔑 NFA Key Properties

> [!note] Key properties of NFA transitions
> - The range of $\delta$ is the **power set** $2^Q$: the value is **not a single state** but a **subset of** $Q$
> - $\lambda$ is allowed as the second argument of $\delta$ — the NFA can transition **without consuming input**
> - $\delta(q, a)$ may be $\emptyset$ — **no transition** defined (**dead configuration**, automaton stops)

### 🔗 Lambda Closure ($\lambda$-closure)

> [!important] Lambda Closure
> The **$\lambda$-closure** of a state $q$ is the set of all states reachable from $q$ by following only $\lambda$-transitions (including $q$ itself):
> $$\lambda\text{-closure}(q) = \{q\} \cup \{p : p \text{ is reachable from } q \text{ via } \lambda\text{-transitions}\}$$

**For a set of states** $S$:
$$\lambda\text{-closure}(S) = \bigcup_{q \in S} \lambda\text{-closure}(q)$$

### 🔁 NFA Extended Transition Function ($\delta^*$)

> [!note] Extended Transition for NFA
> $$\delta^*(q, \lambda) = \lambda\text{-closure}(q)$$
> $$\delta^*(q, wa) = \lambda\text{-closure}\left(\bigcup_{p \in \delta^*(q,w)} \delta(p, a)\right)$$

### ✅ Language Accepted by NFA (Definition 2.6)

> [!important] Definition 2.6
> The language $L$ accepted by an NFA $M = (Q, \Sigma, \delta, q_0, F)$ is:
> $$L(M) = \{w \in \Sigma^* : \delta^*(q_0, w) \cap F \neq \emptyset\}$$

**In words:** A string $w$ is accepted if **at least one** computation path from $q_0$ on $w$ leads to a final state.

### 📝 NFA Example: $L = \{(10)^n : n \geq 0\}$

**NFA with 3 states:** $q_0$ (initial & final), $q_1$, $q_2$ (trap)

Transitions:
- $q_0 \xrightarrow{1} q_1$, $q_0 \xrightarrow{0} q_2$
- $q_1 \xrightarrow{0} q_0$, $q_1 \xrightarrow{0,1} q_2$
- $q_2$: self-loop on $\{0, 1\}$ (trap)
- $q_1 \xrightarrow{\lambda} q_0$

---

## 3️⃣ Equivalence between DFA and NFA

### 🏛️ Theorem 2.2 (Equivalence)

> [!important] Theorem 2.2
> Let $L$ be the language accepted by a nondeterministic finite accepter $M_N = (Q_N, \Sigma, \delta_N, q_0, F_N)$.
> Then there exists a deterministic finite accepter $M_D = (Q_D, \Sigma, \delta_D, q_0', F_D)$ such that:
> $$L = L(M_D)$$

**Corollary:** DFA and NFA are **equally powerful** — they recognize the same class of languages (regular languages).

### 📋 Procedure: NFA-to-DFA (Subset Construction)

> [!tip] Algorithm: NFA → DFA Conversion
> **Input:** NFA $M_N = (Q_N, \Sigma, \delta_N, q_0, F_N)$
> **Output:** Transition graph $G_D$ of associated DFA $M_D$
>
> 1. Create a graph $G_D$ with vertex $\delta_N^*(q_0, \lambda) = \lambda\text{-closure}(q_0)$. Identify this vertex as the **initial vertex**.
> 2. Repeat steps 3–6 until no more edges are missing.
> 3. Take any vertex $\{q_i, q_j, \ldots, q_k\}$ of $G_D$ that has **no outgoing edge** for some $a \in \Sigma$.
> 4. Compute:
>    $$\delta_N^*(\{q_i, q_j, \ldots, q_k\}, a) = \lambda\text{-closure}\left(\delta_N^*(q_i, a) \cup \delta_N^*(q_j, a) \cup \ldots \cup \delta_N^*(q_k, a)\right) = \{q_l, q_m, \ldots, q_n\}$$
> 5. Create a vertex for $G_D$ labeled $\{q_l, q_m, \ldots, q_n\}$ if it does not already exist.
> 6. Add to $G_D$ an edge from $\{q_i, q_j, \ldots, q_k\}$ to $\{q_l, q_m, \ldots, q_n\}$ and label it with $a$.
> 7. Every state of $G_D$ whose label contains any $q_f \in F_N$ is identified as a **final vertex**.

### 🧮 Step-by-Step Conversion Example

> [!example] Converting NFA for $L = \{(10)^n : n \geq 0\}$
>
> **Step 1:** Initial DFA state = $\lambda\text{-closure}(q_0) = \{q_0\}$
>
> **Step 2:** For each DFA state and each input symbol, compute transitions:
>
> | DFA State | Input $0$ | Input $1$ |
> |---|---|---|
> | $\{q_0\}$ | $\{q_2\}$ | $\{q_1\}$ |
> | $\{q_1\}$ | $\{q_0, q_2\}$ | $\{q_2\}$ |
> | $\{q_2\}$ | $\{q_2\}$ | $\{q_2\}$ |
> | $\{q_0, q_2\}$ | $\{q_2\}$ | $\{q_1, q_2\}$ |
> | $\{q_1, q_2\}$ | $\{q_0, q_2\}$ | $\{q_2\}$ |
>
> **Step 3:** Final DFA states = those containing $q_0$ (original final state): $\{q_0\}$, $\{q_0, q_2\}$

---

## 4️⃣ Reduction of the Number of States (DFA Minimization)

### 📖 Key Concepts

> [!note] Distinguishable & Indistinguishable States
> - Two states $p$ and $q$ are **indistinguishable** if $\delta^*(p, w) \in F \iff \delta^*(q, w) \in F$ for **all** $w \in \Sigma^*$
> - Two states $p$ and $q$ are **distinguishable** if there exists some string $w$ such that exactly one of $\delta^*(p, w)$ and $\delta^*(q, w)$ is in $F$
> - **Indistinguishability** is an **equivalence relation** (reflexive, symmetric, transitive)

### 📋 Procedure: Mark (State Minimization Algorithm)

> [!tip] Algorithm: DFA State Reduction
>
> 1. **Remove all inaccessible states** (states not reachable from $q_0$).
> 2. **Consider all pairs** of states $(p, q)$. If $p \in F$ and $q \notin F$ (or vice versa), **mark** the pair $(p, q)$ as **distinguishable**.
> 3. **Repeat** the following step until no previously unmarked pairs are marked:
>    - i. For all unmarked pairs $(p, q)$ and all $a \in \Sigma$, compute $\delta(p, a) = p_a$ and $\delta(q, a) = q_a$.
>    - ii. If the pair $(p_a, q_a)$ is marked as distinguishable, **mark** $(p, q)$ as distinguishable.
> 4. **Group** all remaining **indistinguishable** (unmarked) pairs into equivalence classes.
> 5. **Construct** the reduced DFA:
>    - Each equivalence class becomes a **single state**
>    - Transitions are defined based on the representative of each class

### 🧮 Minimization Properties

> [!important] Theorem 2.3
> The procedure *mark*, applied to any DFA $M = (Q, \Sigma, \delta, q_0, F)$, terminates and determines all pairs of **distinguishable** states.

> [!note] Key Property
> - The states $p$ and $q$ are distinguishable with a string of length $k$ if and only if $\delta(p, a) = p_a$ and $\delta(q, a) = q_a$ for some $a \in \Sigma$, with $p_a$ and $q_a$ distinguishable by a string of length $k - 1$.
> - Any state not part of some pair is its own equivalence class.

### 📝 Minimization Example from Mock Test

> [!example] Reduce the DFA with states $\{q_0, q_1, q_2, q_3, q_4, q_5, q_6\}$
>
> **Given:** $F = \{q_5, q_6\}$, $q_0$ is initial state
>
> | | $0$ | $1$ |
> |---|---|---|
> | $\to q_0$ | $q_2$ | $q_1$ |
> | $q_1$ | $q_3$ | $q_5$ |
> | $q_2$ | $q_0$ | $q_4$ |
> | $q_3$ | $q_3$ | $q_5$ |
> | $q_4$ | $q_3$ | $q_6$ |
> | $*q_5$ | $q_6$ | $q_5$ |
> | $*q_6$ | $q_6$ | $q_6$ |
>
> **Step 1:** Mark all (final, non-final) pairs as distinguishable.
> **Step 2:** Iteratively mark remaining pairs.
> **Step 3:** Merge indistinguishable states into equivalence classes.

---

## 5️⃣ Quick Reference — Formulas & Notation

### Symbols

| Symbol | Meaning |
|---|---|
| $\Sigma$ | Input alphabet |
| $\Sigma^*$ | Set of all strings over $\Sigma$ (including $\lambda$) |
| $\lambda$ ($\varepsilon$) | Empty string |
| $\delta$ | Transition function |
| $\delta^*$ | Extended transition function |
| $2^Q$ | Power set of $Q$ |
| $q_0$ | Initial state |
| $F$ | Set of final/accepting states |
| $L(M)$ | Language accepted by machine $M$ |

### Core Formulas

$$\boxed{\text{DFA accepts } w \iff \delta^*(q_0, w) \in F}$$

$$\boxed{\text{NFA accepts } w \iff \delta^*(q_0, w) \cap F \neq \emptyset}$$

$$\boxed{\delta^*(q, wa) = \delta(\delta^*(q, w), a) \quad \text{(DFA)}}$$

$$\boxed{\delta^*(q, wa) = \lambda\text{-closure}\!\left(\bigcup_{p \in \delta^*(q,w)} \delta(p, a)\right) \quad \text{(NFA)}}$$

---

---

## 7️⃣ Problem-Solving Strategies

### 🔧 Strategy: Building a DFA

1. Identify what information you need to **remember** at each point
2. Each "piece of information" becomes a **state**
3. Draw transitions for **every** symbol from **every** state
4. Identify which states should be **final**
5. Look for **trap states** — once you know the string will be rejected, all paths go here

### 🔧 Strategy: Computing $\delta^*(q_0, w)$ for NFA

1. Start with $\lambda\text{-closure}(q_0)$
2. For each symbol $a$ in the string (left to right):
   - From each state in your current set, follow $a$-transitions
   - Take the **union** of all reached states
   - Compute $\lambda\text{-closure}$ of the result
3. Check if the final set **intersects** $F$

### 🔧 Strategy: NFA → DFA Conversion

1. The **initial DFA state** = $\lambda\text{-closure}(q_0)$
2. Build a **transition table** where each row is a **set of NFA states**
3. For each set and each input symbol:
   - Apply transitions from all states in the set
   - Take $\lambda\text{-closure}$ of the result
4. Mark DFA states as **final** if they contain any NFA final state
5. Rename states for simplicity (e.g., $A, B, C, \ldots$)

### 🔧 Strategy: DFA Minimization

1. **Remove inaccessible states** first
2. Create a table of all **state pairs**
3. **Round 0:** Mark pairs where exactly one state is final
4. **Iterate:** For each unmarked pair, check if transitions lead to a marked pair
5. **Merge** all unmarked pairs into equivalence classes
6. **Redraw** the minimized DFA

---

## 8️⃣ Mock Test 1 — Worked Problem: Computing $\delta^*(q_0, a)$

> [!example] Problem 2: Given NFA, compute $\delta^*(q_0, a)$
> 
> **NFA transitions:**
> - $q_0 \xrightarrow{\lambda} q_1$, $q_0 \xrightarrow{a} q_3$
> - $q_1 \xrightarrow{a} q_2$, $q_1 \xrightarrow{a} q_3$
> - $q_2 \xrightarrow{\lambda} q_1$
> - $q_3 \xrightarrow{a} q_3$ (self-loop), $q_3 \xrightarrow{\lambda} q_2$
> 
> **Solution Steps:**
> 
> **Step 1:** $\lambda\text{-closure}(q_0) = \{q_0, q_1\}$ (follow $q_0 \xrightarrow{\lambda} q_1$)
> 
> **Step 2:** From $\{q_0, q_1\}$, follow $a$-transitions:
> - $\delta(q_0, a) = \{q_3\}$
> - $\delta(q_1, a) = \{q_2, q_3\}$
> - Union: $\{q_2, q_3\}$
> 
> **Step 3:** $\lambda\text{-closure}(\{q_2, q_3\})$:
> - $\lambda\text{-closure}(q_2) = \{q_2, q_1\}$ (follow $q_2 \xrightarrow{\lambda} q_1$)
> - $\lambda\text{-closure}(q_3) = \{q_3, q_2, q_1\}$ (follow $q_3 \xrightarrow{\lambda} q_2 \xrightarrow{\lambda} q_1$)
> - Union: $\{q_1, q_2, q_3\}$
> 
> $$\boxed{\delta^*(q_0, a) = \{q_1, q_2, q_3\}}$$

---

## 9️⃣ Mock Test 1 — Worked Problem: NFA to DFA Conversion

> [!example] Problem 4: Convert NFA to DFA
>
> **Given NFA transition table:**
>
> | State | $a$ | $b$ | $\lambda$ |
> |---|---|---|---|
> | $q_0$ | $\{q_1, q_3\}$ | $\{q_3\}$ | $\{q_3\}$ |
> | $q_1$ | $\{q_2\}$ | $\{q_2\}$ | $\{q_0\}$ |
> | $q_2$ | $\{q_1\}$ | $\emptyset$ | $\emptyset$ |
> | $q_3$ | $\{q_4\}$ | $\emptyset$ | $\{q_4\}$ |
> | $q_4$ | $\{q_4\}$ | $\{q_3\}$ | $\emptyset$ |
>
> Final state: $q_4$
>
> **Step 1:** Initial DFA state = $\lambda\text{-closure}(q_0)$
> - $q_0 \xrightarrow{\lambda} q_3 \xrightarrow{\lambda} q_4$
> - $\lambda\text{-closure}(q_0) = \{q_0, q_3, q_4\}$ ← contains $q_4$, so this is a **final** DFA state
>
> **Step 2:** Build DFA transition table by computing transitions for each DFA state and each input symbol, then taking $\lambda$-closures.

---

## 🔟 Additional Topics (From CSE2023 Mock Exam)

### Regular Expressions → NFA

> [!note] Building NFA from Regex
> Use Thompson's construction:
> - **Base cases:** Single symbol $a$, empty string $\lambda$
> - **Union** $r_1 + r_2$: Add new start/final states with $\lambda$-transitions
> - **Concatenation** $r_1 \cdot r_2$: Chain end of $r_1$ to start of $r_2$
> - **Kleene star** $r^*$: Add $\lambda$-loops and bypass

### Finding Regex from Automaton

> [!tip] State Elimination Method
> 1. Add a new unique **start** and **final** state if needed
> 2. Eliminate states one by one (not start/final)
> 3. Update transition labels with regex expressions
> 4. Final regex is the label on the edge from start to final

### Grammar Concepts (CSE2023)

#### S-Grammar
> [!note] S-Grammar Definition
> A grammar is an **s-grammar** (simple grammar) if:
> - Every production is of the form $A \to a\alpha$ where $a \in T$ (terminal) and $\alpha \in V^*$ (string of variables)
> - The pair $(A, a)$ appears **at most once** on the left side of any production

#### Right-Linear vs Left-Linear Grammar
| Type | Production Form | Generates |
|---|---|---|
| **Right-linear** | $A \to wB$ or $A \to w$ | Regular languages |
| **Left-linear** | $A \to Bw$ or $A \to w$ | Regular languages |

#### Context-Free Grammar Simplification

> [!tip] Steps to Simplify CFG
> 1. **Remove $\lambda$-productions** (except possibly $S \to \lambda$)
> 2. **Remove unit-productions** ($A \to B$)
> 3. **Remove useless variables** (non-generating or unreachable)
> 4. Convert to **Chomsky Normal Form (CNF)** or **Greibach Normal Form (GNF)**

### Greibach Normal Form (GNF)

> [!note] GNF Definition
> Every production is of the form:
> $$A \to a\alpha$$
> where $a$ is a **terminal** and $\alpha$ is a (possibly empty) string of **variables**.

### Pushdown Automata (PDA) from GNF

> [!tip] Constructing PDA from GNF
> For each production $A \to a B_1 B_2 \ldots B_n$:
> - Create transition: $\delta(q, a, A) = \{(q, B_1 B_2 \ldots B_n)\}$
> - Start by pushing start symbol $S$ onto stack
> - Accept when stack is empty

---

> [!success] Good luck on your midterm! 🎓
> Remember: Practice the **NFA→DFA conversion** and **DFA minimization** procedures step by step — they appear on every exam!
