---
tags: [theoretical-computer-science, pushdown-automata, context-free-languages]
topic: "Pushdown Automata (PDA)"
course: "Theoretical Computer Science – Automata and Formal Languages"
---

# Pushdown Automata (PDA)

> [!Note] 💡 Notation Conventions
> - $\lambda$ — the empty string (used for both input and stack positions)
> - $\Sigma$ — input alphabet; $\Gamma$ — stack alphabet
> - $z$ — the designated start stack symbol (bottom-of-stack marker)
> - $\delta$ — transition function
> - $\vdash$ — one move (step) of the automaton; $\vdash^*$ — zero or more moves
> - $(q, w, u)$ — instantaneous description: state $q$, unread input $w$, stack contents $u$ (leftmost = top)
> - $n_a(w)$ — number of occurrences of symbol $a$ in string $w$
> - NPDA / NDPDA — nondeterministic pushdown automaton (used interchangeably in the source)
> - DPDA — deterministic pushdown automaton

---

## 1 — Motivation

> [!Note] 💡 Why Finite Automata Are Insufficient
> Finite automata have **strictly finite memory**: they cannot count arbitrarily or store and recall sequences of symbols.
>
> **Example 1:** Recognising $L = \{a^n b^n : n \geq 0\}$ requires counting $n$ a's, but $n$ is unbounded.
>
> **Example 2:** Recognising $L = \{ww^R : w \in \{a,b\}^+\}$ requires storing an entire substring and matching it in reverse — beyond any finite memory.
>
> **Solution:** Augment the finite control unit with an **unbounded stack** — yielding a **Pushdown Automaton (PDA)**.

---

## 2 — Nondeterministic Pushdown Automata (NPDA)

### 2.1 Informal Description

Each move of the PDA:
- **Reads** one symbol from the input (or makes a $\lambda$-transition without reading).
- **Inspects** the top symbol of the stack.
- **Updates** the stack top (push, pop, or replace).
- **Transitions** to a (possibly nondeterministically chosen) new state.

```
Input tape: [ a | b | b | a | ... ]  →
                  ↓
          [ Control Unit ] ↔ [ Stack ]
                                top
                                 ↓
                              [ s₁ ]
                              [ s₂ ]
                              [  ⋮  ]
```

> [!Note] 💡 Stack Operations via $\delta$
> The result $x \in \Gamma^*$ placed on the stack replaces the single symbol that was on top:
> - $x = \lambda$: **pop** (remove top symbol)
> - $x = a$: **replace** top with $a$
> - $x = ab$: **replace** top with $a$ (new top) then $b$ below it — i.e., push $b$ then $a$

---

### 2.2 Formal Definition

> [!Definition] 📖 NPDA (Definition 7.1)
> A **nondeterministic pushdown accepter (NPDA)** is a 7-tuple
> $$M = (Q,\, \Sigma,\, \Gamma,\, \delta,\, q_0,\, z,\, F)$$
> where:
> - $Q$ — finite set of **internal states**
> - $\Sigma$ — **input alphabet**
> - $\Gamma$ — **stack alphabet** (finite set of stack symbols)
> - $\delta : Q \times (\Sigma \cup \{\lambda\}) \times \Gamma \to \text{finite subsets of } Q \times \Gamma^*$ — **transition function**
> - $q_0 \in Q$ — **initial state**
> - $z \in \Gamma$ — **start stack symbol** (initially on the stack)
> - $F \subseteq Q$ — **set of final (accepting) states**

> [!Property] ⚙️ Transition Function Properties
> Given $\delta(q,\, a,\, b)$ where $q \in Q$, $a \in \Sigma \cup \{\lambda\}$, $b \in \Gamma$:
>
> **1.** The result is a **finite** set of pairs $(q', x)$: $q'$ is the next state, $x \in \Gamma^*$ replaces $b$ on top of the stack.
>
> **2.** If $a = \lambda$: the move is a **$\lambda$-transition** — no input symbol is consumed.
>
> **3.** If the stack is **empty**, no move is possible ($\delta$ requires a stack symbol as its third argument).
>
> **4.** An **unspecified** transition is treated as mapping to $\emptyset$ — a **dead configuration** (same convention as NFA).

---

### 2.3 Instantaneous Descriptions and Moves

> [!Definition] 📖 Instantaneous Description (ID)
> A **triple** $(q,\, w,\, u)$ fully describes the current situation of the NPDA:
> - $q \in Q$ — current state
> - $w \in \Sigma^*$ — **unread** portion of the input
> - $u \in \Gamma^*$ — current stack contents (**leftmost symbol = top**)

> [!Definition] 📖 Move Relation $\vdash$
> A **single move** is written:
> $$(q_1,\, aw,\, bx) \;\vdash\; (q_2,\, w,\, yx)$$
> This move is possible if and only if $(q_2,\, y) \in \delta(q_1,\, a,\, b)$, where:
> - $a \in \Sigma \cup \{\lambda\}$ — input symbol consumed (or $\lambda$)
> - $b \in \Gamma$ — top stack symbol consumed
> - $y \in \Gamma^*$ — string placed on top of stack in its place
> - $x \in \Gamma^*$ — remaining stack contents (unchanged)
>
> **Zero or more moves:** $(q_1, w_1, x_1) \;\vdash^*\; (q_2, w_2, x_2)$
>
> When specifying which machine: $\vdash_M$

---

### 2.4 Transition Graphs

> [!Note] 💡 Transition Graph Notation
> Edges are labelled with **three items**: $a,\, b,\, x$ — meaning:
> - $a$ — input symbol read (or $\lambda$)
> - $b$ — stack symbol popped from top
> - $x$ — string pushed to top
>
> This corresponds to: $\delta(q_i,\, a,\, b) \ni (q_j,\, x)$, drawn as $q_i \xrightarrow{a,\,b,\,x} q_j$.
>
> **Limitation:** transition graphs track state and input well, but are less suited to tracking stack contents step-by-step — use IDs for that.

---

### 2.5 Language Accepted by an NPDA

> [!Definition] 📖 Accepted Language (Definition 7.2)
> Let $M = (Q, \Sigma, \Gamma, \delta, q_0, z, F)$ be an NPDA. The **language accepted** by $M$ is:
> $$L(M) = \{ w \in \Sigma^* : (q_0,\, w,\, z) \;\vdash_M^*\; (q_f,\, \lambda,\, u),\; q_f \in F,\; u \in \Gamma^* \}$$
>
> That is: $w$ is accepted if there **exists** a computation that:
> **1.** Starts in $q_0$ with $w$ on the input and $z$ on the stack.
> **2.** Consumes the **entire** input ($\lambda$ remaining).
> **3.** Ends in a **final state** $q_f \in F$.
>
> The **final stack content** $u$ is **irrelevant** to acceptance.

> [!Warning] ⚠️ Nondeterminism
> An NPDA **accepts** $w$ if **at least one** computation path leads to a final state after reading all of $w$. Other paths may die or loop — they do not affect acceptance.

---

## 3 — NPDA and Context-Free Languages

### 3.1 From CFG (GNF) to NPDA

> [!Theorem] 📌 Theorem 7.1
> For every context-free language $L$, there exists an NPDA $M$ such that $L = L(M)$.

The construction works by simulating a **leftmost derivation** in a grammar in **Greibach Normal Form (GNF)**.

> [!Note] 💡 Greibach Normal Form (GNF) Reminder
> Every production has the form $A \to a\,u$ where $a \in T$ (a terminal) and $u \in V^*$ (a string of variables). This ensures every derivation step begins by producing a terminal.

> [!Property] ⚙️ Simulation Invariant
> At any point in the simulation:
> - The **stack** holds the **variable suffix** of the current sentential form.
> - The **input already read** equals the **terminal prefix** of the sentential form.
>
> Applying production $A \to a\,x$: when $A$ is on top and $a$ is the next input, pop $A$ and push $x$.

> [!Definition] 📖 GNF-to-NPDA Procedure (Procedure GGreibach2NPDA)
> **Input:** $G = (V, T, S, P)$ in Greibach Normal Form
> **Output:** NPDA $M = (Q, \Sigma, \Gamma, \delta, q_0, z, F)$ with $L(M) = L(G)$
>
> **S1.** $M = (\{q_0, q_1, q_f\},\; T,\; V \cup \{z\},\; \delta,\; q_0,\; z,\; \{q_f\})$, where $z \notin V$.
>
> **S2.** $\delta(q_0, \lambda, z) = \{(q_1, Sz)\}$ — push start symbol $S$ onto the stack; $z$ remains as end-marker.
>
> **S3.** For each production $A \to a\,u$ in $P$: $\quad \delta(q_1, a, A) \ni (q_1, u)$
> — reads terminal $a$, pops variable $A$, pushes variable string $u$.
>
> **S4.** $\delta(q_1, \lambda, z) = \{(q_f, z)\}$ — when only $z$ remains (derivation complete), enter final state.

---

### 3.2 From NPDA to CFG

> [!Theorem] 📌 Theorem 7.2
> If $L = L(M)$ for some NPDA $M$, then $L$ is a context-free language.

The construction reverses Theorem 7.1 — the grammar **simulates** the NPDA's moves.

> [!Property] ⚙️ NPDA Normal Form Requirements
> Before applying the construction, the NPDA must satisfy:
>
> **1.** It has a **single final state** $q_f$, entered if and only if the stack is empty.
>
> **2.** Every transition has one of exactly two forms:
> $$\delta(q_i, a, A) \ni (q_j, \lambda) \tag{7.5 — pop}$$
> $$\delta(q_i, a, A) \ni (q_j, BC) \tag{7.6 — replace with two symbols}$$
> where $a \in \Sigma \cup \{\lambda\}$. Every move either **decreases** or **increases** the stack by exactly one symbol.

> [!Definition] 📖 NPDA-to-CFG Variable Scheme
> Grammar variables have the form $(q_i A q_j)$, interpreted as:
> > **"The NPDA erases $A$ from the stack while reading some string $w$ and transitioning from state $q_i$ to state $q_j$."**
>
> Formally: $(q_i A q_j) \Rightarrow^* w \iff (q_i, w, A\gamma) \vdash^* (q_j, \lambda, \gamma)$ for any $\gamma$.

> [!Property] ⚙️ Production Rules from Transitions
> **(7.5)** $\delta(q_i, a, A) \ni (q_j, \lambda)$
> $$\implies (q_i A q_j) \to a$$
>
> **(7.6)** $\delta(q_i, a, A) \ni (q_j, BC)$
> $$\implies (q_i A q_k) \to a\,(q_j B q_l)(q_l C q_k) \quad \text{for all } q_k, q_l \in Q$$
>
> **Start variable:** $(q_0\, z\, q_f)$ where $q_f$ is the single final state.
>
> **Useless variables:** Any $(q_i A q_j)$ that never appears on the **left side** of a surviving production is useless — eliminate by standard useless-variable removal.

> [!Warning] ⚠️ Handling Transitions Not in Normal Form
> If a transition $\delta(q_i, a, A) = \{(q_j, A)\}$ (replace with same symbol — neither pop nor push) appears, it violates both (7.5) and (7.6). Fix by introducing an **intermediate state** $q_{\text{new}}$:
> $$\delta(q_i, a, A) = \{(q_{\text{new}}, \lambda)\}, \quad \delta(q_{\text{new}}, \lambda, z) = \{(q_j, Az)\}$$
> This decomposes the single move into a pop followed by a push.

---

## 4 — Deterministic Pushdown Automata (DPDA)

### 4.1 Definition

> [!Definition] 📖 Deterministic PDA (Definition 7.3)
> An NPDA $M = (Q, \Sigma, \Gamma, \delta, q_0, z, F)$ is **deterministic** (a DPDA) if for every $q \in Q$, $a \in \Sigma \cup \{\lambda\}$, $b \in \Gamma$:
>
> **1.** $|\delta(q, a, b)| \leq 1$ — at most one choice per configuration.
>
> **2.** If $\delta(q, \lambda, b) \neq \emptyset$, then $\delta(q, c, b) = \emptyset$ for all $c \in \Sigma$ — no $\lambda$-transition and symbol-reading transition can coexist on the same stack top.

> [!Note] 💡 DPDA vs DFA
> - The domain of $\delta$ still includes $\lambda$ (unlike a DFA). $\lambda$-transitions are permitted — they don't cause nondeterminism by themselves since **condition 2** prevents simultaneous symbol-reading.
> - Some transitions may be undefined (dead configurations). This is allowed — the only criterion is **at most one move** at any point.

> [!Definition] 📖 Deterministic CFL (Definition 7.4)
> A language $L$ is a **deterministic context-free language (DCFL)** if and only if there exists a DPDA $M$ such that $L = L(M)$.

### 4.2 DPDA vs NPDA

> [!Warning] ⚠️ Key Difference from Finite Automata
> Unlike DFAs and NFAs (which are equivalent in power), **DPDAs and NPDAs are NOT equivalent**.
>
> There exist context-free languages that **cannot** be recognised by any DPDA — e.g., $L = \{ww^R : w \in \{a,b\}^+\}$ (shown below). Thus:
> $$\text{DCFLs} \subsetneq \text{CFLs}$$

---

## 📘 Examples & Applications

### Example 1 — Recognising $L = \{a^n b^n : n \geq 0\} \cup \{a\}$

**Using:** NPDA definition, transition function, instantaneous descriptions, transition graphs.

> [!Example] 📘
> Consider the NPDA $M$ with:
> - $Q = \{q_0, q_1, q_2, q_3\}$, $\Sigma = \{a,b\}$, $\Gamma = \{0,1\}$, $z = 0$, $F = \{q_3\}$
>
> Transitions:
> $$\delta(q_0, a, 0) = \{(q_1, 10),\,(q_3, \lambda)\}$$
> $$\delta(q_0, \lambda, 0) = \{(q_3, \lambda)\}$$
> $$\delta(q_1, a, 1) = \{(q_1, 11)\}$$
> $$\delta(q_1, b, 1) = \{(q_2, \lambda)\}$$
> $$\delta(q_2, b, 1) = \{(q_2, \lambda)\}$$
> $$\delta(q_2, \lambda, 0) = \{(q_3, \lambda)\}$$
>
> **Transition graph:**
>
> ```mermaid
> flowchart LR
>   start(( )) --> q0((q0))
>   q0 -->|"a, 0, 10"| q1((q1))
>   q0 -->|"a, 0, λ; λ, 0, λ"| q3(((q3)))
>   q1 -->|"a, 1, 11"| q1
>   q1 -->|"b, 1, λ"| q2((q2))
>   q2 -->|"b, 1, λ"| q2
>   q2 -->|"λ, 0, λ"| q3
> ```
>
> **Behaviour:** $q_1$ stays active while reading $a$'s (pushing 1's). On first $b$, transitions to $q_2$ (ensuring no $b$ precedes the last $a$). Each $b$ pops one 1. When stack bottom $0$ is exposed, $\lambda$-transition to final state $q_3$.
>
> **Result:** $L(M) = \{a^n b^n : n \geq 0\} \cup \{a\}$

---

### Example 2 — Recognising $L = \{w \in \{a,b\}^* : n_a(w) = n_b(w)\}$

**Using:** NPDA construction, instantaneous descriptions.

> [!Example] 📘
> $M = (\{q_0, q_f\},\; \{a,b\},\; \{0, 1, z\},\; \delta,\; q_0,\; z,\; \{q_f\})$
>
> **Design idea:** Use stack symbol $0$ to track excess $a$'s, $1$ to track excess $b$'s. When counts balance, stack returns to $z$ and we accept via $\lambda$-transition.
>
> Transitions:
> $$\delta(q_0, \lambda, z) = \{(q_f, z)\}$$
> $$\delta(q_0, a, z) = \{(q_0, 0z)\} \qquad \delta(q_0, b, z) = \{(q_0, 1z)\}$$
> $$\delta(q_0, a, 0) = \{(q_0, 00)\} \qquad \delta(q_0, b, 1) = \{(q_0, 11)\}$$
> $$\delta(q_0, b, 0) = \{(q_0, \lambda)\} \qquad \delta(q_0, a, 1) = \{(q_0, \lambda)\}$$
>
> **Trace for $w = baab$:**
>
> $$
> (q_0,\; baab,\; z)
> \;\vdash\; (q_0,\; aab,\; 1z)
> \;\vdash\; (q_0,\; ab,\; z)
> \;\vdash\; (q_0,\; b,\; 0z)
> \;\vdash\; (q_0,\; \lambda,\; z)
> \;\vdash\; (q_f,\; \lambda,\; z)
> $$
>
> Final state $q_f$ reached after consuming all input. ✓

---

### Example 3 — Recognising $L = \{ww^R : w \in \{a,b\}^+\}$

**Using:** NPDA construction, $\lambda$-transitions for nondeterministic midpoint guessing.

> [!Example] 📘
> $M = (\{q_0, q_1, q_f\},\; \{a,b\},\; \{a,b,z\},\; \delta,\; q_0,\; z,\; \{q_f\})$
>
> **Phase 1** ($q_0$): Push all input symbols onto the stack.
> $$\delta(q_0, a, z) = \{(q_0, az)\}, \quad \delta(q_0, b, z) = \{(q_0, bz)\}$$
> $$\delta(q_0, a, a) = \{(q_0, aa)\}, \quad \delta(q_0, b, a) = \{(q_0, ba)\}$$
> $$\delta(q_0, a, b) = \{(q_0, ab)\}, \quad \delta(q_0, b, b) = \{(q_0, bb)\}$$
>
> **Midpoint guess** (nondeterministic $\lambda$-transition):
> $$\delta(q_0, \lambda, a) = \{(q_1, a)\}, \quad \delta(q_0, \lambda, b) = \{(q_1, b)\}$$
>
> **Phase 2** ($q_1$): Match remaining input against stack (reversed $w$).
> $$\delta(q_1, a, a) = \{(q_1, \lambda)\}, \quad \delta(q_1, b, b) = \{(q_1, \lambda)\}$$
>
> **Accept** when only $z$ remains:
> $$\delta(q_1, \lambda, z) = \{(q_f, z)\}$$
>
> **Trace for $w = abba$:**
>
> $$
> (q_0,\; abba,\; z)
> \;\vdash\; (q_0,\; bba,\; az)
> \;\vdash\; (q_0,\; ba,\; baz)
> \;\vdash\; (q_1,\; ba,\; baz)
> \;\vdash\; (q_1,\; a,\; az)
> \;\vdash\; (q_1,\; \lambda,\; z)
> \;\vdash\; (q_f,\; \lambda,\; z)
> $$
>
> ✓ Accepted. Note: this NPDA is **not** deterministic — $\delta(q_0, a, a)$ and $\delta(q_0, \lambda, a)$ both exist, violating condition 2 of Definition 7.3.

---

### Example 4 — GNF Grammar to NPDA

**Using:** GNF-to-NPDA procedure (Theorem 7.1), leftmost derivation simulation.

> [!Example] 📘
> **Grammar:** $S \to aSbb \mid a$
>
> **Step 1 — Convert to GNF:**
> $$S \to aSA \mid a, \quad A \to bB, \quad B \to b$$
>
> **Step 2 — Build NPDA** ($Q = \{q_0, q_1, q_2\}$, initial $q_0$, final $q_2$):
>
> $$\delta(q_0, \lambda, z) = \{(q_1, Sz)\}$$
> $$\delta(q_1, a, S) = \{(q_1, SA),\; (q_1, \lambda)\}$$
> $$\delta(q_1, b, A) = \{(q_1, B)\}$$
> $$\delta(q_1, b, B) = \{(q_1, \lambda)\}$$
> $$\delta(q_1, \lambda, z) = \{(q_2, \lambda)\}$$
>
> **Trace for $w = aabb$:**
>
> $$
> (q_0,\; aabb,\; z)
> \;\vdash\; (q_1,\; aabb,\; Sz)
> \;\vdash\; (q_1,\; abb,\; SAz)
> \;\vdash\; (q_1,\; bb,\; Az)
> \;\vdash\; (q_1,\; b,\; Bz)
> \;\vdash\; (q_1,\; \lambda,\; z)
> \;\vdash\; (q_2,\; \lambda,\; z)
> $$
>
> **Corresponding leftmost derivation in $G$:**
> $$S \Rightarrow aSA \Rightarrow aaA \Rightarrow aabB \Rightarrow aabb$$

---

### Example 5 — GNF Grammar to NPDA (Full Example)

**Using:** GNF-to-NPDA procedure, multi-variable GNF grammar.

> [!Example] 📘
> **Grammar:**
> $$S \to aA, \quad A \to aABC \mid bB \mid a, \quad B \to b, \quad C \to c$$
>
> **NPDA transitions:**
> $$\delta(q_0, \lambda, z) = \{(q_1, Sz)\}$$
> $$\delta(q_1, a, S) = \{(q_1, A)\}$$
> $$\delta(q_1, a, A) = \{(q_1, ABC),\; (q_1, \lambda)\}$$
> $$\delta(q_1, b, A) = \{(q_1, B)\}$$
> $$\delta(q_1, b, B) = \{(q_1, \lambda)\}$$
> $$\delta(q_1, c, C) = \{(q_1, \lambda)\}$$
> $$\delta(q_1, \lambda, z) = \{(q_f, z)\}$$
>
> **Trace for $w = aaabc$:**
>
> $$
> (q_0,\; aaabc,\; z)
> \;\vdash\; (q_1,\; aaabc,\; Sz)
> \;\vdash\; (q_1,\; aabc,\; Az)
> \;\vdash\; (q_1,\; abc,\; ABCz)
> \;\vdash\; (q_1,\; bc,\; BCz)
> \;\vdash\; (q_1,\; c,\; Cz)
> \;\vdash\; (q_1,\; \lambda,\; z)
> \;\vdash\; (q_f,\; \lambda,\; z)
> $$
>
> Derivation: $S \Rightarrow aA \Rightarrow aaABC \Rightarrow aaaBC \Rightarrow aaabC \Rightarrow aaabc$

---

### Example 6 — NPDA to CFG (Full Worked Construction)

**Using:** NPDA-to-CFG procedure (Theorem 7.2), normal form conditions (7.5) and (7.6), useless variable elimination.

> [!Example] 📘
> **Given NPDA** ($q_0$: start, $q_2$: final):
> $$\delta(q_0, a, z) = \{(q_0, Az)\} \tag{1}$$
> $$\delta(q_0, a, A) = \{(q_0, A)\} \tag{2}$$
> $$\delta(q_0, b, A) = \{(q_1, \lambda)\} \tag{3}$$
> $$\delta(q_1, \lambda, z) = \{(q_2, \lambda)\} \tag{4}$$
>
> **Step 1 — Normalize transition (2):**
> Transition (2) is neither (7.5) nor (7.6) — it replaces $A$ with $A$ (no net stack change). Introduce state $q_3$:
> $$\delta(q_0, a, A) = \{(q_3, \lambda)\} \tag{2'}$$
> $$\delta(q_3, \lambda, z) = \{(q_0, Az)\} \tag{3'}$$
>
> New full set: (1), (2'), (3'), (3), (4). Now $Q = \{q_0, q_1, q_2, q_3\}$.
>
> **Step 2 — Apply (7.5) to pop-transitions:**
>
> | Transition | Rule produced |
> |---|---|
> | $\delta(q_0, a, A) = \{(q_3, \lambda)\}$ | $(q_0 A q_3) \to a$ |
> | $\delta(q_0, b, A) = \{(q_1, \lambda)\}$ | $(q_0 A q_1) \to b$ |
> | $\delta(q_1, \lambda, z) = \{(q_2, \lambda)\}$ | $(q_1 z q_2) \to \lambda$ |
>
> **Step 3 — Apply (7.6) to push-transitions:**
> Both (1) $\delta(q_0, a, z) = \{(q_0, Az)\}$ and (3') $\delta(q_3, \lambda, z) = \{(q_0, Az)\}$ push two symbols. For each, enumerate all $(q_k, q_l) \in Q^2$:
>
> From (1): $(q_0 z q_k) \to a\,(q_0 A q_l)(q_l z q_k)$ for all $q_k, q_l \in Q$.
>
> From (3'): $(q_3 z q_k) \to (q_0 A q_l)(q_l z q_k)$ for all $q_k, q_l \in Q$.
>
> **Step 4 — Eliminate useless variables.**
>
> Variables that never appear on the left of any surviving production:
> $(q_0Aq_0)$, $(q_0Aq_2)$, $(q_1zq_0)$, $(q_1zq_1)$, $(q_1zq_3)$, all $(q_2 z q_j)$.
>
> Also: $(q_3zq_0)$, $(q_3zq_1)$, $(q_3zq_3)$ are self-referential with no base case — useless.
>
> **Step 5 — Surviving rules:**
>
> $$\boxed{
> \begin{aligned}
> (q_0 A q_3) &\to a \\
> (q_0 A q_1) &\to b \\
> (q_1 z q_2) &\to \lambda \\
> (q_3 z q_2) &\to (q_0 A q_1)(q_1 z q_2) \mid (q_0 A q_3)(q_3 z q_2) \\
> (q_0 z q_2) &\to a(q_0 A q_1)(q_1 z q_2) \mid a(q_0 A q_3)(q_3 z q_2)
> \end{aligned}
> }$$
>
> **Start variable:** $(q_0\, z\, q_2)$
>
> **Step 6 — Rename and simplify** (substituting known rules):
>
> Let $S = (q_0 z q_2)$, $X = (q_3 z q_2)$, $A = (q_0 A q_3)$, $B = (q_0 A q_1)$, $C = (q_1 z q_2)$:
> $$S \to aBC \mid aAX, \quad X \to BC \mid AX, \quad A \to a, \quad B \to b, \quad C \to \lambda$$
>
> Simplifying ($C \to \lambda$, $A \to a$, $B \to b$):
> $$S \to ab \mid aaX, \quad X \to b \mid aX$$
>
> $$\boxed{L = \{a^n b : n \geq 1\}}$$
>
> **Verification for $w = aab$** (successive IDs of the NPDA, cross-checked with grammar derivation):
>
> NPDA path:
> $$(q_0, aab, z) \vdash (q_0, ab, Az) \vdash (q_3, b, z) \vdash (q_0, b, Az) \vdash (q_1, \lambda, z) \vdash (q_2, \lambda, \lambda)$$
>
> Grammar derivation:
> $$(q_0 z q_2) \Rightarrow a(q_0 A q_3)(q_3 z q_2) \Rightarrow aa(q_3 z q_2) \Rightarrow aa(q_0 A q_1)(q_1 z q_2) \Rightarrow aab(q_1 z q_2) \Rightarrow aab$$

---

### Example 7 — DPDA for $L = \{a^n b^n : n \geq 0\}$

**Using:** Definition 7.3 (DPDA), Definition 7.4 (DCFL).

> [!Example] 📘
> $M = (\{q_0, q_1, q_2\},\; \{a,b\},\; \{0,1\},\; \delta,\; q_0,\; 0,\; \{q_0\})$
>
> $$\delta(q_0, a, 0) = \{(q_1, 10)\}$$
> $$\delta(q_1, a, 1) = \{(q_1, 11)\}$$
> $$\delta(q_1, b, 1) = \{(q_2, \lambda)\}$$
> $$\delta(q_2, b, 1) = \{(q_2, \lambda)\}$$
> $$\delta(q_2, \lambda, 0) = \{(q_0, \lambda)\}$$
>
> **Verification of determinism:**
> - Each $\delta(q, a, b)$ has at most one element. ✓ (condition 1)
> - Only $\delta(q_2, \lambda, 0)$ uses $\lambda$; $\delta(q_2, c, 0)$ is undefined for all $c \in \Sigma$. ✓ (condition 2)
>
> Therefore $M$ is deterministic, and $L = \{a^n b^n : n \geq 0\}$ is a **DCFL**.

---

## 🗂️ Summary

- An **NPDA** extends an NFA with a stack, giving it **unbounded memory** for counting and matching.
- Formally: $M = (Q, \Sigma, \Gamma, \delta, q_0, z, F)$; $\delta : Q \times (\Sigma \cup \{\lambda\}) \times \Gamma \to \text{finite subsets of } Q \times \Gamma^*$.
- **Instantaneous description** $(q, w, u)$: state, unread input, stack (left = top). Move: $(q_1, aw, bx) \vdash (q_2, w, yx)$ iff $(q_2, y) \in \delta(q_1, a, b)$.
- **Acceptance:** $w \in L(M)$ iff $\exists$ path $(q_0, w, z) \vdash^* (q_f, \lambda, u)$ with $q_f \in F$. Stack content at end is irrelevant.
- **Unspecified transitions** → dead configuration (same as NFA).
- **Theorem 7.1:** Every CFL has an accepting NPDA. Construction: convert grammar to GNF, then apply GNF-to-NPDA (3 states, simulate leftmost derivation).
  - $\delta(q_0, \lambda, z) = \{(q_1, Sz)\}$; for $A \to au$: $\delta(q_1, a, A) \ni (q_1, u)$; $\delta(q_1, \lambda, z) = \{(q_f, z)\}$.
- **Theorem 7.2:** Every NPDA recognises a CFL. Construction: variables $(q_i A q_j)$, rules from (7.5) and (7.6), start variable $(q_0 z q_f)$.
  - (7.5) pop: $(q_i A q_j) \to a$; (7.6) push-two: $(q_i A q_k) \to a(q_j B q_l)(q_l C q_k)$ for all $q_k, q_l$.
  - Eliminate useless variables; the NPDA must first be put in normal form (only pop or push-exactly-one moves).
- **DPDA (Definition 7.3):** at most one transition per configuration; no simultaneous $\lambda$-transition and symbol-reading transition on same stack top.
- **DCFL (Definition 7.4):** language of some DPDA.
- **DPDAs $\subsetneq$ NPDAs** in power: $L = \{ww^R\}$ is CFL but **not** DCFL.
- DCFLs $\subsetneq$ CFLs (strict containment).
