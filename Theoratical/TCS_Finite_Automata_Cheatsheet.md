# 🧠 TCS Cheatsheet — Finite Automata
> Module 10: Theoretical Computer Science | Vietnamese-German University

---

## 1. DFA — Deterministic Finite Accepter

### Definition
$$M = (Q, \Sigma, \delta, q_0, F)$$

| Symbol | Meaning |
|--------|---------|
| $Q$ | Finite set of **internal states** |
| $\Sigma$ | Finite **input alphabet** |
| $\delta: Q \times \Sigma \to Q$ | **Transition function** (single next state) |
| $q_0 \in Q$ | **Initial state** |
| $F \subseteq Q$ | Set of **final/accepting states** |

### How DFA Works
1. Start in $q_0$, read input left-to-right, one symbol at a time.
2. Each symbol triggers a state transition via $\delta$.
3. After last symbol: **accept** if current state $\in F$, else **reject**.

### Transition Graph Notation
- Vertices = states
- Edges = transitions labeled with input symbol
- Initial state: arrow with no source
- Final states: **double circle**
- **Trap state**: state with no outgoing escape (can be final or non-final)

### Extended Transition Function $\delta^*$
$$\delta^*: Q \times \Sigma^* \to Q$$
- $\delta^*(q, \lambda) = q$
- $\delta^*(q, wa) = \delta(\delta^*(q, w), a)$

### Language of a DFA
$$L(M) = \{w \in \Sigma^* : \delta^*(q_0, w) \in F\}$$

### Regular Language
> A language $L$ is **regular** iff $\exists$ DFA $M$ such that $L = L(M)$.

---

## 2. NFA — Nondeterministic Finite Accepter

### Definition
$$M = (Q, \Sigma, \delta, q_0, F)$$

Same as DFA, **except**:
$$\delta: Q \times (\Sigma \cup \{\lambda\}) \to 2^Q$$

| Key difference | DFA | NFA |
|----------------|-----|-----|
| Next state | Single state | **Set** of states |
| $\lambda$-transitions | Not allowed | Allowed |
| Dead config | Halts in non-final | $\delta(q,a) = \emptyset$ → stops |

### Language of an NFA
$$L(M) = \{w \in \Sigma^* : \delta^*(q_0, w) \cap F \neq \emptyset\}$$
> Accept if **any** path leads to a final state.

---

## 3. Extended Transition for NFA

### Case 1: No $\lambda$-transitions
- $\delta^*(q, \lambda) = \{q\}$
- $\delta^*(q, wa) = \delta(\delta^*(q,w), a)$
- For a set $T$: $\delta(T, a) = \bigcup_{q \in T} \delta(q, a)$

### Case 2: With $\lambda$-transitions

**Key formulas:**
$$\delta^*(q, a) = \lambda\text{-closure}(\text{move}(\lambda\text{-closure}(q),\ a))$$
$$\delta^*(T, a) = \lambda\text{-closure}(\text{move}(\lambda\text{-closure}(T),\ a))$$

**$\lambda$-closure$(q)$** = all states reachable from $q$ using only $\lambda$-transitions (including $q$ itself).

**move$(T, a)$** = all states reachable from any state in $T$ via symbol $a$ (one step).

### Step-by-step: Compute $\delta^*(q_0, a)$ with $\lambda$-transitions
1. Compute $\lambda\text{-closure}(q_0)$
2. Compute $\text{move}(\lambda\text{-closure}(q_0),\ a)$
3. Compute $\lambda\text{-closure}$ of the result from step 2

> **Example** (from lecture slide 33):
> - $\lambda\text{-closure}(q_0) = \{q_0, q_1, q_2\}$
> - $\text{move}(\{q_0,q_1,q_2\}, a) = \{q_4, q_0, q_3\}$
> - $\lambda\text{-closure}(\{q_4,q_0,q_3\}) = \{q_0,q_1,q_2,q_3,q_4,q_5\}$
> - So $\delta^*(q_0,a) = \{q_0,q_1,q_2,q_3,q_4,q_5\}$

---

## 4. NFA → DFA Conversion (Subset Construction)

### Algorithm: `nfa-to-dfa`
1. Create initial DFA state = $\delta_N^*(q_0, \lambda)$ (i.e., $\lambda$-closure of $q_0$)
2. For each DFA state $S = \{q_i, q_j, \ldots\}$ and each $a \in \Sigma$:
   - Compute $\delta_N^*(S, a) = \bigcup_{q \in S} \delta_N^*(q, a)$
   - This becomes a new DFA state (if not already seen)
   - Add edge from $S$ to the result, labeled $a$
3. Repeat until no new states/edges
4. **Final states**: any DFA state whose label contains a state from $F_N$

### Key Insight
- Each **NFA state** = a **set of states** in the DFA
- Empty set $\emptyset$ = dead/trap state in DFA

> **Example** (lecture slide 47–48):
> NFA with $q_1$ as final:
> - $\delta^*(\{q_0\}, a) = \{q_1, q_2\}$, $\delta^*(\{q_0\}, b) = \emptyset$
> - $\delta^*(\{q_1,q_2\}, a) = \{q_1,q_2\}$, $\delta^*(\{q_1,q_2\}, b) = \{q_0\}$
> - DFA states: $\{q_0\}$, $\{q_1,q_2\}$, $\emptyset$
> - $\{q_1,q_2\}$ is final (contains $q_1 \in F_N$)

---

## 5. DFA State Minimization

### Concepts
- **Inaccessible state**: unreachable from $q_0$ → can be safely **removed**
- **Indistinguishable states** $p, q$: for all $w \in \Sigma^*$, $\delta^*(p,w) \in F \Leftrightarrow \delta^*(q,w) \in F$
- **Distinguishable states**: $\exists w$ such that one leads to final, the other does not

### Algorithm: `mark()` — Find Distinguishable Pairs
1. Remove all **inaccessible states**
2. Mark all pairs $(p, q)$ where one $\in F$ and the other $\notin F$
3. Repeat until no new marks:
   - For all pairs $(p,q)$ and all $a \in \Sigma$:
     - Let $p_a = \delta(p,a)$, $q_a = \delta(q,a)$
     - If $(p_a, q_a)$ is marked → mark $(p,q)$
4. Unmarked pairs = **indistinguishable** (can be merged)

### Algorithm: `reduce()` — Build Minimal DFA $\hat{M}$
1. Run `mark()` to get indistinguishability classes $\{q_i, q_j, \ldots\}$
2. Each class → one state in $\hat{M}$, labeled by indices
3. For transition $\delta(q_r, a) = q_p$: add $\hat{\delta}([\text{class of } q_r], a) = [\text{class of } q_p]$
4. Initial state: class containing $q_0$
5. Final states: classes containing any $q_f \in F$

> **Theorem 2.4**: The reduced DFA $\hat{M}$ is **minimal** — no DFA with fewer states accepts the same language.

### Example (lecture slide 65–66)
Transition table with $F = \{q_4\}$:

| | 0 | 1 |
|-|---|---|
| $q_0$ | $q_1$ | $q_3$ |
| $q_1$ | $q_2$ | $q_4$ |
| $q_2$ | $q_1$ | $q_4$ |
| $q_3$ | $q_2$ | $q_4$ |
| $q_4$ | $q_4$ | $q_4$ |

Indistinguishable groups: $\{q_0\}$, $\{q_1, q_2, q_3\}$, $\{q_4\}$

Minimal DFA states: **0**, **123**, **4**

---

## 6. Mock Test — Solution Guide

### Q1: DFA for strings starting with prefix `ab` on $\Sigma = \{a,b\}$

**States**: $q_0$ (start), $q_1$ (saw `a`), $q_2$ (saw `ab` → accepting), $q_3$ (trap/dead)

| | a | b |
|-|---|---|
| $\to q_0$ | $q_1$ | $q_3$ |
| $q_1$ | $q_3$ | $q_2$ |
| $*(q_2)$ | $q_2$ | $q_2$ |
| $q_3$ | $q_3$ | $q_3$ |

$F = \{q_2\}$

---

### Q2: Compute $\delta^*(q_0, a)$ for NFA with $\lambda$-transitions

From the mock test figure (NFA with $q_0, q_1, q_2, q_3$):

**Transition table:**

| | a | $\lambda$ |
|-|---|-----------|
| $q_0$ | $q_3$ | $q_1$ |
| $q_1$ | $q_1$ | — |
| $q_2$ | — | — |
| $q_3$ | $q_2$ | $q_3$, $\lambda$ |

**Steps:**
1. $\lambda\text{-closure}(q_0) = \{q_0, q_1\}$ (follow all $\lambda$ edges from $q_0$)
2. $\text{move}(\{q_0, q_1\}, a)$ = states reached on `a` from $q_0$ or $q_1$
   - $\delta(q_0, a) = \{q_3\}$, $\delta(q_1, a) = \{q_1\}$ → $\{q_1, q_3\}$
3. $\lambda\text{-closure}(\{q_1, q_3\})$ = $\{q_1, q_3\}$ + any $\lambda$ reachable
   - From $q_3$: follow $\lambda$ → $\{q_2\}$ (check diagram carefully)
4. $\delta^*(q_0, a) = \lambda\text{-closure}(\{q_1, q_3\}) = \{q_1, q_2, q_3\}$ *(verify with actual diagram)*

> ⚠️ Always draw out the λ-closure step by step from the diagram!

---

### Q3: DFA State Reduction

**General procedure for the exam:**
1. Build transition table if not given
2. Identify inaccessible states (BFS/DFS from $q_0$) and remove them
3. Initially mark pairs where exactly one state is final
4. Iteratively mark pairs whose successors are already marked
5. Group unmarked pairs → equivalence classes → new states

---

### Q4: NFA → DFA (from mock test)

Given NFA, $q_0$ initial, $q_4$ final:

| | a | b | $\lambda$ |
|-|---|---|-----------|
| $q_0$ | $q_1, q_3$ | $q_3$ | $q_3$ |
| $q_1$ | $q_2$ | $q_2$ | $q_0$ |
| $q_2$ | $q_1$ | — | — |
| $q_3$ | $q_4$ | — | $q_4$ |
| $q_4$ | $q_4$ | $q_3$ | — |

**Step 1:** $\lambda\text{-closure}(q_0)$
- From $q_0$: $\lambda \to q_3$; from $q_3$: $\lambda \to q_4$
- $\lambda\text{-closure}(q_0) = \{q_0, q_3, q_4\}$ ← **initial DFA state** ✅ (contains $q_4$ → **final**)

**Step 2:** Compute transitions from $\{q_0, q_3, q_4\}$:

On **a**:
- $\delta(q_0,a) = \{q_1,q_3\}$, $\delta(q_3,a) = \{q_4\}$, $\delta(q_4,a) = \{q_4\}$
- move = $\{q_1,q_3,q_4\}$
- $\lambda\text{-closure}(\{q_1,q_3,q_4\})$: $q_1 \xrightarrow{\lambda} q_0 \xrightarrow{\lambda} q_3 \xrightarrow{\lambda} q_4$
- = $\{q_0, q_1, q_3, q_4\}$ → **final** (contains $q_4$)

On **b**:
- $\delta(q_0,b) = \{q_3\}$, $\delta(q_3,b) = \emptyset$, $\delta(q_4,b) = \{q_3\}$
- move = $\{q_3\}$
- $\lambda\text{-closure}(\{q_3\}) = \{q_3, q_4\}$ → **final** (contains $q_4$)

**Step 3:** Continue for new states until closed. Key states found:
- $A = \{q_0, q_3, q_4\}$ → final ✅
- $B = \{q_0, q_1, q_3, q_4\}$ → final ✅
- $C = \{q_3, q_4\}$ → final ✅

> Continue expanding $B$ and $C$ until all transitions are defined.

---

## 7. Quick Reference Formulas

| Concept | Formula |
|---------|---------|
| DFA language | $L(M) = \{w : \delta^*(q_0,w) \in F\}$ |
| NFA language | $L(M) = \{w : \delta^*(q_0,w) \cap F \neq \emptyset\}$ |
| $\lambda$-closure of set | $\lambda\text{-closure}(T) = \bigcup_{q \in T} \lambda\text{-closure}(q)$ |
| NFA extended $\delta^*$ | $\lambda\text{-closure}(\text{move}(\lambda\text{-closure}(q), a))$ |
| DFA $\delta^*$ recursive | $\delta^*(q, wa) = \delta(\delta^*(q,w), a)$ |
| Indistinguishable | $\forall w: \delta^*(p,w) \in F \Leftrightarrow \delta^*(q,w) \in F$ |

---

## 8. Common Language Examples

| Language | Description |
|----------|-------------|
| $\{a^n b : n \geq 0\}$ | Any number of $a$'s followed by one $b$ |
| $\{awa : w \in \{a,b\}^*\}$ | Starts and ends with $a$ |
| $\{a^2 w b^2 : w \in \{a,b\}^*\}$ | Starts with $aa$, ends with $bb$ |
| $\{(10)^n : n \geq 0\}$ | Repeated `10` (including empty) |
| $\{w : w \text{ doesn't contain } 001\}$ | Avoid substring `001` |
| $\{ab^5 w b^2 : w \in \{a,b\}^*\}$ | Specific prefix/suffix counts |

---

## 9. DFA vs NFA Comparison

| Property | DFA | NFA |
|----------|-----|-----|
| Transition | $\delta: Q \times \Sigma \to Q$ | $\delta: Q \times (\Sigma \cup \{\lambda\}) \to 2^Q$ |
| Next state | Exactly one | Set of states (possibly empty) |
| $\lambda$-transitions | ✗ | ✓ |
| Dead config | N/A (always defined in full DFA) | $\delta(q,a) = \emptyset$ |
| Expressive power | **Equal** — every NFA has equivalent DFA |
| State count | May be exponential more | Often fewer states |

> **Theorem 2.2**: For every NFA $M_N$, there exists a DFA $M_D$ with $L(M_N) = L(M_D)$.

---

*Good luck on the midterm! 🍀*
