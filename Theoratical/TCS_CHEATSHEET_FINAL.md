---
tags: [tcs, exam-prep, automata, formal-languages, vgu]
aliases: [TCS Exam Cheatsheet]
created: 2025-06-17
---

# TCS Exam Cheatsheet — Zero to Full Marks

> [!info] How to use
> Each section = one problem type. Read the **procedure box** first, then follow the **worked example** step by step. Every step you write on paper is shown explicitly.

---

## NOTATION REFERENCE

| Symbol                | Meaning                                                                         |
| --------------------- | ------------------------------------------------------------------------------- |
| `→`                   | start state arrow                                                               |
| `(q)`                 | regular state                                                                   |
| `((q))`               | final state (double circle)                                                     |
| `--a-->`              | transition on symbol `a`                                                        |
| `λ`                   | empty string (lambda)                                                           |
| `r*`                  | zero or more repetitions of r                                                   |
| `r+`                  | one or more repetitions of r                                                    |
| `r1 + r2`             | union (either r1 or r2)                                                         |
| `r1r2`                | concatenation (r1 then r2)                                                      |
| `δ(q, a, X) = (p, α)` | NPDA: in state q, reading a, with X on top of stack → go to p, replace X with α |

---
## PROBLEM 1A — Build NFA from a Regular Expression (Thompson's Construction)

### What you're doing
You convert a regular expression into a diagram of states and arrows, following mechanical rules for each RE operator.

### Atomic building blocks

**Single symbol `a`:**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    q0;
    node [shape=doublecircle];
    q1;
    start -> q0;
    q0 -> q1 [label="a"];
}
```

**Union `r1 + r2`** — "either r1 or r2":

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    qs;
    r1s [label="NFA for r1"];
    r1e [label="NFA for r1 (end)"];
    r2s [label="NFA for r2"];
    r2e [label="NFA for r2 (end)"];
    node [shape=doublecircle];
    qf;
    start -> qs;
    qs -> r1s [label="λ"];
    qs -> r2s [label="λ"];
    r1e -> qf [label="λ"];
    r2e -> qf [label="λ"];
}
```

**Concatenation `r1r2`** — "r1 then r2":

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    r1s [label="r1 start"];
    r1e [label="r1 end"];
    r2s [label="r2 start"];
    node [shape=doublecircle];
    r2e [label="r2 end"];
    start -> r1s;
    r1s -> r1e [label="...r1..."];
    r1e -> r2s [label="λ"];
    r2s -> r2e [label="...r2..."];
}
```

**Star `r*`** — "zero or more r":

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    qs;
    rs [label="r start"];
    re [label="r end"];
    node [shape=doublecircle];
    qf;
    start -> qs;
    qs -> qf [label="λ(skip)"];
    qs -> rs [label="λ"];
    rs -> re [label="...r..."];
    re -> qf [label="λ"];
    re -> rs [label="λ(loop)"];
}
```

### Step-by-step procedure

```
Step 1. Parse the RE — identify the outermost operator
        Priority: star (*) first, then concatenation, then union (+)
Step 2. Recursively build NFA for each sub-expression
Step 3. Combine using the matching rule above
Step 4. Number all states q0, q1, q2, ...
Step 5. Mark the one start state (→) and one final state (double circle)
```

> [!warning] Operator priority (most to least binding)
> `*`  >  concatenation  >  `+`
> So `ab*+c` parses as `(a(b*))+c`, NOT `a(b*+c)`

## QUICK SANITY CHECK — Thompson NFA Node Count

### The Fast Counting Formula
Before drawing your NFA, calculate the exact number of nodes (states) it *should* have. Every symbol and operator adds a predictable number of states in a strict Thompson construction.

#  **N = 2 * (S + U + K)**

**Where:**
* **S (Symbols):** Total count of terminal characters (e.g., `a`, `b`).
* **U (Unions):** Total count of `+` operators.
* **K (Kleene Stars):** Total count of `*` operators.
* *(Note: Concatenations add 0 new states).*
---
> [!note] Practical note
> The worked examples below sometimes merge adjacent states (e.g., the end of one atom with the start of the next in concatenation, or use a flat multi-way union instead of nested binary unions). As a result, the drawn NFA may have **fewer** states than the strict formula predicts. The formula gives the maximum / strict-Thompson count — use it as an upper bound, not an exact target.
---

### ✏️ Fully Worked Example: r1 = b(ab + b)* + a\*b

**Parse the structure first:**

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    root [label="r1 = b(ab+b)* + a*b | UNION (+)"];
    partA [label="Part A: b(ab+b)* | CONCATENATION"];
    atom_b1 [label="atom: b"];
    star1 [label="(ab+b)* | STAR"];
    union1 [label="ab+b | UNION"];
    concat1 [label="ab | CONCAT"];
    concat_a [label="a | atom"];
    concat_b [label="b | atom"];
    atom_b2 [label="b | atom"];
    partB [label="Part B: a*b | CONCATENATION"];
    star2 [label="a* | STAR"];
    atom_a [label="a | atom"];
    atom_b3 [label="atom: b"];
    root -> partA;
    root -> partB;
    partA -> atom_b1;
    partA -> star1;
    star1 -> union1;
    union1 -> concat1;
    union1 -> atom_b2;
    concat1 -> concat_a;
    concat1 -> concat_b;
    partB -> star2;
    partB -> atom_b3;
    star2 -> atom_a;
}
```

**Build Part A bottom-up:**

1. NFA for `b` (states 0–1):

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s0;
    node [shape=doublecircle];
    s1;
    start -> s0;
    s0 -> s1 [label="b"];
}
```

2. NFA for `ab+b` (UNION, states 2–8):

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s2; s3; s4; s5; s6; s7;
    node [shape=doublecircle];
    s8;
    start -> s7;
    s7 -> s2 [label="λ"];
    s7 -> s5 [label="λ"];
    s2 -> s3 [label="a"];
    s3 -> s4 [label="b"];
    s5 -> s6 [label="b"];
    s4 -> s8 [label="λ"];
    s6 -> s8 [label="λ"];
}
```

3. STAR `(ab+b)*` — wrap the union NFA (states 9–10):

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s9;
    s7 [label="7 [union NFA start]"];
    s8 [label="8 [union NFA end]"];
    node [shape=doublecircle];
    s10;
    start -> s9;
    s9 -> s10 [label="λ(skip)"];
    s9 -> s7 [label="λ"];
    s8 -> s10 [label="λ"];
    s8 -> s7 [label="λ(loop)"];
}
```

4. CONCATENATE `b · (ab+b)*` — connect state 1 → state 9 via λ:

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s0; s1; s7; s8; s9;
    node [shape=doublecircle];
    s10;
    start -> s0;
    s0 -> s1 [label="b"];
    s1 -> s9 [label="λ"];
    s9 -> s10 [label="λ(skip)"];
    s9 -> s7 [label="λ"];
    s7 -> s8 [label="[union NFA]"];
    s8 -> s10 [label="λ"];
    s8 -> s7 [label="λ(loop)"];
}
```

**Build Part B: `a*b`**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s11; s12; s13; s14; s15;
    node [shape=doublecircle];
    s16;
    start -> s11;
    s11 -> s12 [label="λ(skip)"];
    s11 -> s13 [label="λ"];
    s13 -> s14 [label="a"];
    s14 -> s12 [label="λ"];
    s14 -> s13 [label="λ(loop)"];
    s12 -> s15 [label="λ"];
    s15 -> s16 [label="b"];
}
```

**Final UNION of Part A and Part B (states 17–18):**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s17;
    s0 [label="0 [Part A start]"];
    s11 [label="11 [Part B start]"];
    s10 [label="10 [Part A end]"];
    s16 [label="16 [Part B end]"];
    node [shape=doublecircle];
    s18;
    start -> s17;
    s17 -> s0 [label="λ"];
    s17 -> s11 [label="λ"];
    s10 -> s18 [label="λ"];
    s16 -> s18 [label="λ"];
}
```

---

### ✏️ Fully Worked Example: r2 = b + a\* + b\*a\*

**Parse structure:**

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    root [label="r2 = b + a* + b*a* | UNION of 3 parts"];
    part1 [label="Part 1: b | atom"];
    part2 [label="Part 2: a* | STAR"];
    atom_a [label="a (atom)"];
    part3 [label="Part 3: b*a* | CONCATENATION"];
    b_star [label="b* (STAR)"];
    b_atom [label="b (atom)"];
    a_star [label="a* (STAR)"];
    a_atom [label="a (atom)"];
    root -> part1;
    root -> part2;
    root -> part3;
    part2 -> atom_a;
    part3 -> b_star;
    part3 -> a_star;
    b_star -> b_atom;
    a_star -> a_atom;
}
```

**Final UNION (new start=14, new final=15):**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    s0; s1; s2; s3; s4; s5; s6; s7; s8; s9; s10; s11; s12; s13; s14;
    node [shape=doublecircle];
    s15;
    start -> s14;
    s14 -> s0 [label="λ"];
    s14 -> s2 [label="λ"];
    s14 -> s6 [label="λ"];
    s0 -> s1 [label="b"];
    s2 -> s3 [label="λ(skip)"];
    s2 -> s4 [label="λ"];
    s4 -> s5 [label="a"];
    s5 -> s3 [label="λ"];
    s5 -> s4 [label="λ(loop)"];
    s6 -> s7 [label="λ(skip)"];
    s6 -> s8 [label="λ"];
    s8 -> s9 [label="b"];
    s9 -> s7 [label="λ"];
    s9 -> s8 [label="λ(loop)"];
    s7 -> s10 [label="λ"];
    s10 -> s11 [label="λ(skip)"];
    s10 -> s12 [label="λ"];
    s12 -> s13 [label="a"];
    s13 -> s11 [label="λ"];
    s13 -> s12 [label="λ(loop)"];
    s1 -> s15 [label="λ"];
    s3 -> s15 [label="λ"];
    s11 -> s15 [label="λ"];
}
```

---

## PROBLEM 1B — Improve the NFA (Optimal Transition Graph / OTG)

### What you're doing
The Thompson NFA is bloated with λ-transitions. The OTG is the equivalent NFA with no λ-transitions and minimal states. You get there via **subset construction with λ-closure**.

### Key concept: λ-closure

`λ-closure(q)` = the set of ALL states you can reach from q using ONLY λ-arrows (including q itself).

### Step-by-step procedure

```
Step 1. Compute λ-closure of the start state → this is your NEW start state (a set)

Step 2. For that new state (set S) and each symbol a:
        MOVE(S, a) = all states reachable by one 'a' arrow from any state in S
        Then take λ-closure(MOVE(S, a)) → this is a new state

Step 3. Repeat Step 2 for every newly discovered state until no new states appear

Step 4. A state is FINAL if it contains any original final state

Step 5. Draw the result — states are sets, but rename them q0, q1, ... for neatness
```

> [!tip] Shortcut for the exam
> You do NOT need to mechanically compute all subsets. Look at the Thompson NFA and ask: "what can I reach from the start without reading anything?" Then trace real symbols. The answer key always gives a small clean graph — aim for 3–5 states.

---

### ✏️ Worked Example: OTG for r1 = b(ab+b)\* + a\*b

**Optimal TG (5 states):**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    q0; q_int; q2;
    node [shape=doublecircle];
    q1; qf;
    start -> q0;
    q0 -> q1 [label="b"];
    q0 -> q2 [label="a"];
    q1 -> q_int [label="a"];
    q_int -> q1 [label="b"];
    q1 -> q1 [label="b"];
    q1 -> qf [label="b"];
    q2 -> q2 [label="a"];
    q2 -> qf [label="b"];
}
```
	
### ✏️ Worked Example: OTG for r2 = b + a\* + b\*a\*

**Insight:** `a*` accepts λ, and `b*a*` accepts λ — so the start state is immediately final.

**Optimal TG (3 states):**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=doublecircle];
    q0; q1; q2;
    start -> q0;
    q0 -> q1 [label="b"];
    q0 -> q2 [label="a"];
    q1 -> q1 [label="b"];
    q1 -> q2 [label="a"];
    q2 -> q2 [label="a"];
}
```

---

## PROBLEM 2 — Find Regular Expression from Automaton (State Elimination)

### What you're doing
You eliminate states one by one, labelling edges with regular expressions, until only start and final remain.

### The formula
When you eliminate state `q`:

$$\text{new edge } i \to j = r_{iq} \cdot (r_{qq})^* \cdot r_{qj}$$

### Step-by-step procedure

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="Step 1\nAdd super-start qs\n(λ-arrow to original start)"];
    B [label="Step 2\nAdd super-final qf\n(λ-arrow from each final state)"];
    C [label="Step 3\nChoose any state to eliminate\n(NOT qs or qf)"];
    D [label="Step 4\nFor every i->q and q->j pair:\ncompute new i->j label using formula\nUnion (+) if edge already exists"];
    E [label="Step 5\nDelete q and all its edges"];
    F [shape=diamond, label="Only qs\nand qf\nremain?"];
    G [label="Step 6\nLabel on qs->qf edge\n= your Regular Expression ✓"];
    A -> B;
    B -> C;
    C -> D;
    D -> E;
    E -> F;
    F -> C [label="No"];
    F -> G [label="Yes"];
}
```

> [!tip] Eliminate states with **no self-loop** first — the formula simplifies to `r_iq · r_qj` (no star needed).

---

### ✏️ Fully Worked Example (mock exam Q2)

**The automaton:**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    q0; q1;
    node [shape=doublecircle];
    q2;
    start -> q0;
    q0 -> q0 [label="a"];
    q0 -> q1 [label="a"];
    q0 -> q2 [label="b"];
    q1 -> q2 [label="a"];
    q1 -> q0 [label="b"];
    q2 -> q0 [label="a"];
    q2 -> q1 [label="b"];
    q2 -> q2 [label="b"];
}
```

**After adding qs and qf:**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    qs; q0; q1; q2;
    node [shape=doublecircle];
    qf;
    start -> qs;
    qs -> q0 [label="λ"];
    q0 -> q0 [label="a"];
    q0 -> q1 [label="a"];
    q0 -> q2 [label="b"];
    q1 -> q2 [label="a"];
    q1 -> q0 [label="b"];
    q2 -> q0 [label="a"];
    q2 -> q1 [label="b"];
    q2 -> q2 [label="b"];
    q2 -> qf [label="λ"];
}
```

**Eliminate q1** (no self-loop — eliminate first to keep algebra simple):

Incoming edges to q1: `q0 --a--> q1`, `q2 --b--> q1`
Outgoing edges from q1: `q1 --a--> q2`, `q1 --b--> q0`

Compute new edges for every (i, j) pair where i→q1 and q1→j:

| i | j | r_iq1 | r_q1j | new label | existing edge? | combined |
|---|---|--------|--------|-----------|----------------|----------|
| q0 | q2 | a | a | aa | b | **b+aa** |
| q0 | q0 | a | b | ab | a | **a+ab** |
| q2 | q2 | b | a | ba | b | **b+ba** |
| q2 | q0 | b | b | bb | a | **a+bb** |

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    qs; q0; q2;
    node [shape=doublecircle];
    qf;
    start -> qs;
    qs -> q0 [label="λ"];
    q0 -> q0 [label="a+ab"];
    q0 -> q2 [label="b+aa"];
    q2 -> q0 [label="a+bb"];
    q2 -> q2 [label="b+ba"];
    q2 -> qf [label="λ"];
}
```

**Eliminate q0** (self-loop = `a+ab`):

Incoming edges to q0: `qs --λ--> q0`, `q2 --a+bb--> q0`
Outgoing edges from q0: `q0 --a+ab--> q0` (self-loop), `q0 --b+aa--> q2`

For each i→q0 and q0→j (excluding j=q0 since it is being eliminated):

- **(qs, q2):** `λ · (a+ab)* · (b+aa)` = **`(a+ab)*(b+aa)`**
- **(q2, q2):** `(a+bb) · (a+ab)* · (b+aa)` → combined with existing self-loop `b+ba`:
  **`b+ba + (a+bb)(a+ab)*(b+aa)`**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    qs; q2;
    node [shape=doublecircle];
    qf;
    start -> qs;
    qs -> q2 [label="(a+ab)*(b+aa)"];
    q2 -> q2 [label="b+ba + (a+bb)(a+ab)*(b+aa)"];
    q2 -> qf [label="λ"];
}
```

**Eliminate q2** (self-loop = `b+ba + (a+bb)(a+ab)*(b+aa)`):

Only remaining pair is (qs, qf):

`r_qs,q2 · (r_q2,q2)* · r_q2,qf`

= `(a+ab)*(b+aa) · (b+ba + (a+bb)(a+ab)*(b+aa))* · λ`

= `(a+ab)*(b+aa) (b+ba + (a+bb)(a+ab)*(b+aa))*`

```
RE = (a+ab)*(b+aa)(b+ba + (a+bb)(a+ab)*(b+aa))*
```

---

## PROBLEM 3 — Is This Grammar Ambiguous?

### Step-by-step procedure

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="Step 1\nScan for variables with multiple alternatives\nor nullable variables"];
    B [label="Step 2\nTry short strings:\na, b, ab, aa, aaa, λ"];
    C [label="Step 3\nFor chosen string w:\nWrite TWO different parse trees"];
    D [shape=diamond, label="Found 2\ndistinct trees?"];
    E [label="✓ AMBIGUOUS\nState: w = [string] has two parse trees"];
    F [label="Try next string or longer string"];
    A -> B;
    B -> C;
    C -> D;
    D -> E [label="Yes"];
    D -> F [label="No"];
    F -> C;
}
```

---

### ✏️ Fully Worked Example (mock exam Q3)

**Grammar:**
```
S → aSSa | A | B | ab
A → aB | b
B → aD | a | λ
D → a | aB
```
**Witness string: w = `aaa`**

**Parse Tree 1** (via `S → A`):

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    S1;
    A1 [label="A (S→A)"];
    a1 [label="a"];
    B1 [label="B (A→aB)"];
    a2 [label="a"];
    D1 [label="D (B→aD)"];
    a3 [label="a (D→a)"];
    S1 -> A1;
    A1 -> a1;
    A1 -> B1;
    B1 -> a2;
    B1 -> D1;
    D1 -> a3;
}
```

Derivation: S ⇒ A ⇒ aB ⇒ aaD ⇒ **aaa** ✓

**Parse Tree 2** (via `S → B`):

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    S2;
    B2 [label="B (S→B)"];
    a4 [label="a"];
    D2 [label="D (B→aD)"];
    a5 [label="a"];
    B3 [label="B (D→aB)"];
    a6 [label="a (B→a)"];
    S2 -> B2;
    B2 -> a4;
    B2 -> D2;
    D2 -> a5;
    D2 -> B3;
    B3 -> a6;
}
```

Derivation: S ⇒ B ⇒ aD ⇒ aaB ⇒ **aaa** ✓

**Conclusion: G is ambiguous** — `w = aaa` has two distinct parse trees.

---

## PROBLEM 4 — RLG ↔ NFA ↔ LLG

### Key grammar rules

| Grammar type | Production form | Example |
|---|---|---|
| Right Linear | `A → aB` or `A → a` or `A → λ` | `S → abA`, `A → b` |
| Left Linear | `A → Ba` or `A → a` or `A → λ` | `S → Aab`, `A → b` |

### Overview of the three phases

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    RLG [label="Right Linear\nGrammar GR"];
    NFA [label="NFA S1"];
    RNFA [label="Reversed\nNFA S2"];
    LLG [label="Left Linear\nGrammar GL"];
    RLG -> NFA [label="Phase 1\nVariables=States\nProductions=Arrows"];
    NFA -> RNFA [label="Phase 2\nSwap start<->final\nReverse all arrows"];
    RNFA -> LLG [label="Phase 3\nRead arrows as\nLeft Linear rules"];
}
```

### Phase 1: RLG → NFA (translation rules)

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    prod [label="Production", shape=plain];
    nfa [label="NFA Arrow", shape=plain];
    p1 [label="A → aB"];
    p2 [label="A → a"];
    p3 [label="A → λ"];
    p4 [label="A → abB"];
    r1 [label="A --a--> B"];
    r2 [label="A --a--> F (final state)"];
    r3 [label="A becomes a final state"];
    r4 [label="A --a--> (new) --b--> B"];
    { rank=same; p1; r1; }
    { rank=same; p2; r2; }
    { rank=same; p3; r3; }
    { rank=same; p4; r4; }
    p1 -> r1;
    p2 -> r2;
    p3 -> r3;
    p4 -> r4;
}
```

### Phase 2: Reverse the NFA

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    os [label="→ Old Start"];
    of [label="Old Final ⊗"];
    ns [label="→ New Start\n(was old final)"];
    nf [label="New Final ⊗\n(was old start)"];
    os -> of [label="a"];
    nf -> ns [label="a", dir=forward];
    of -> ns [label="becomes", style=dashed, constraint=false];
    os -> nf [label="becomes", style=dashed, constraint=false];
}
```

---

### ✏️ Fully Worked Example (mock exam Q4)

**Phase 1 — NFA from G_R:**

The given Right Linear Grammar G_R:
```
S → bA | aT | aC
A → aB | aU
T → bS
C → aA
B → bF
U → bF
F → λ
```

Translate each production to an NFA transition (variables → states, terminals → labels, final variable F → double circle):

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    S; A; T; C; B; U;
    node [shape=doublecircle];
    F;
    start -> S;
    S -> A [label="b"];
    S -> T [label="a"];
    T -> S [label="b"];
    S -> C [label="a"];
    A -> B [label="a"];
    A -> U [label="a"];
    B -> F [label="b"];
    U -> F [label="b"];
    C -> A [label="a"];
}
```

**Phase 2 — Reversed NFA S₂** (swap start↔final, flip all arrows):

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    F; B; U; A; C; T;
    node [shape=doublecircle];
    S;
    start -> F;
    F -> B [label="b"];
    F -> U [label="b"];
    B -> A [label="a"];
    U -> A [label="a"];
    A -> S [label="b"];
    A -> C [label="a"];
    C -> S [label="a"];
    T -> S [label="a"];
    S -> T [label="b"];
}
```

**Phase 3 — Read as Left Linear Grammar G_L:**

Rule: For each reversed arrow `Y --a--> X`, the LLG production is `X → Ya` (variable then terminal).

| Edge | Raw LLG Production | After F→λ substitution |
|------|-------------------|------------------------|
| F --b--> B | B → Fb | B → b |
| F --b--> U | U → Fb | U → b |
| B --a--> A | A → Ba | A → Ba |
| U --a--> A | A → Ua | A → Ua |
| A --b--> S | S → Ab | S → Ab |
| A --a--> C | C → Aa | C → Aa |
| C --a--> S | S → Ca | S → Ca |
| T --a--> S | S → Ta | S → Ta |
| S --b--> T | T → Sb | T → Sb |

Start variable `F → λ` (generates the empty string).

Substituting `F → λ`, `B → b`, `U → b`:

```
F → λ             (start variable)
B → b
U → b
A → Ba | Ua
C → Aa
S → Ab | Ca | Ta
T → Sb
```

After further substitution of `A` and `C`:

```
F → λ
B → b
U → b
A → ba
C → baa
S → bab | baaa | Ta
T → Sb
```

---

## PROBLEM 5 — Is It an s-grammar?

### Definition

A CFG is an **s-grammar** if and only if **BOTH** conditions hold:
1. Every production `A → aα` — **starts with a terminal**
2. For each pair `(A, a)`, there is **at most one** production

### Decision procedure

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="For each variable A,\nlist the first symbol of each production"];
    B [shape=diamond, label="Any production\nstarts with a\nnon-terminal or λ?"];
    C [label="× FAILS condition 1\nNOT an s-grammar\n(cite the offending production)"];
    D [shape=diamond, label="Any (variable, terminal)\npair appears in\n2+ productions?"];
    E [label="× FAILS condition 2\nNOT an s-grammar\n(cite the duplicate pair)"];
    F [label="✓ IS an s-grammar"];
    A -> B;
    B -> C [label="Yes"];
    B -> D [label="No"];
    D -> E [label="Yes"];
    D -> F [label="No"];
}
```

---

### ✏️ Worked Examples (mock exam Q5)

**a) S → aBD | bC | aD; B → a; C → bD | b; D → b**

| Variable | Productions | First symbols | Verdict |
|---|---|---|---|
| S | aBD, bC, aD | a, b, **a** | ❌ (S,a) twice |
| B | a | a | ✓ |
| C | bD, b | **b, b** | ❌ (C,b) twice |
| D | b | b | ✓ |

**→ NOT an s-grammar** — (S,a) and (C,b) both duplicated.

**b) S → aS | B; B → a**

| Variable | Productions | First symbols | Verdict |
|---|---|---|---|
| S | aS, **B** | a, **B** ← variable! | ❌ condition 1 |
| B | a | a | ✓ |

**→ NOT an s-grammar** — `S → B` starts with a variable.

**c) S → bAB | aB; A → aA | b**

| Variable | Productions | First symbols | Verdict |
|---|---|---|---|
| S | bAB, aB | b, a | ✓ |
| A | aA, b | a, b | ✓ |

**→ IS an s-grammar** ✓ — Pairs: (S,b), (S,a), (A,a), (A,b) each unique.

**d) S → c | cDD | bAD; A → aD | b; D → b**

| Variable | Productions | First symbols | Verdict |
|---|---|---|---|
| S | c, cDD, bAD | **c, c**, b | ❌ (S,c) twice |
| A | aD, b | a, b | ✓ |
| D | b | b | ✓ |

**→ NOT an s-grammar** — (S,c) appears for both `S → c` and `S → cDD`.

---

## PROBLEM 6A — Simplify a CFG (λ → unit → useless, in that order)

### The three passes — mandatory order

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    G [label="Original\nGrammar G"];
    P1 [label="Pass 1\nRemove λ-productions"];
    P2 [label="Pass 2\nRemove unit productions\n(A → B)"];
    P3 [label="Pass 3\nRemove useless productions"];
    Gp [label="Simplified\nGrammar G'"];
    G -> P1;
    P1 -> P2;
    P2 -> P3;
    P3 -> Gp;
}
```

### Pass 1: Remove λ-productions

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="Round 1: Mark X nullable if X → λ exists"];
    B [label="Round 2: Mark X nullable if X → Y1Y2...Yn\nand ALL Yi already marked nullable"];
    C [shape=diamond, label="Any new\nnullables\nfound?"];
    D [label="For each production, generate new productions\nby removing each subset of nullable variables"];
    E [label="Delete all X → λ productions\n(keep S → λ only if λ ∈ L(G))"];
    A -> B;
    B -> C;
    C -> B [label="Yes"];
    C -> D [label="No"];
    D -> E;
}
```

### Pass 2: Remove unit productions

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="Base unit pairs: (A,A) for all variables"];
    B [label="If (A,B) is a pair and B→C is unit:\nadd (A,C)"];
    C [shape=diamond, label="New pairs\nfound?"];
    D [label="For each unit pair (A,B):\ncopy all non-unit productions of B to A"];
    E [label="Delete all unit productions A → B"];
    A -> B;
    B -> C;
    C -> B [label="Yes"];
    C -> D [label="No"];
    D -> E;
}
```

### Pass 3: Remove useless productions

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    G1 [label="Mark X 'generating' if\nX → terminal string"];
    G2 [label="Mark X 'generating' if\nX → α where all symbols\nin α are generating/terminal"];
    G3 [label="Remove all non-generating\nvariables and their productions"];
    R1 [label="S is reachable"];
    R2 [label="If A is reachable and A→α:\nmark all variables in α reachable"];
    R3 [label="Remove all non-reachable\nvariables and their productions"];
    G1 -> G2;
    G2 -> G3;
    R1 -> R2;
    R2 -> R3;
}
```

---

### ✏️ Fully Worked Example (mock exam Q6a)

**Original grammar G:**
```
S → aS | A | aBD | c
A → bAD | λ
B → bC | C
C → AcDD | D
D → a | λ
E → b
```

**Pass 1 — Nullable variables:**

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    R1 [label="Round 1:\nA (A→λ)\nD (D→λ)"];
    R2 [label="Round 2:\nC (C→D, D nullable)\nB (B→C, C nullable)"];
    R3 [label="Round 3:\nS (S→A, A nullable)"];
    DONE [label="Nullable = {A, D, C, B, S}"];
    R1 -> R2;
    R2 -> R3;
    R3 -> DONE;
}
```

**Grammar after Pass 1 (P₁):**
```
S → aS | a | A | aBD | aD | aB | c | λ
A → bAD | bA | bD | b
B → bC | b | C
C → AcDD | cDD | AcD | Ac | cD | c | D
D → a
E → b
```

**Pass 2 — Unit pairs and resolutions:**

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    UP [label="Unit productions: S→A, B→C, C→D"];
    PA [label="(S,A): copy A's non-unit productions to S\n→ S gains: bAD, bA, bD, b"];
    PB [label="(B,C): copy C's non-unit productions to B\n→ B gains: AcDD, cDD, AcD, Ac, cD, c"];
    PC [label="(C,D): copy D's non-unit productions to C\n→ C gains: a"];
    PD [label="(B,D) transitive via C→D:\nB gains: a"];
    DEL [label="Delete S→A, B→C, and C→D"];
    UP -> PA;
    UP -> PB;
    UP -> PC;
    PA -> DEL;
    PB -> DEL;
    PC -> DEL;
    PD -> DEL;
}
```

**Grammar after Pass 2 (P₂):**
```
S → aS | a | aBD | aD | aB | c | bAD | bA | bD | b | λ
A → bAD | bA | bD | b
B → bC | b | AcDD | cDD | AcD | Ac | cD | c | a
C → AcDD | cDD | AcD | Ac | cD | c | a
D → a
E → b
```

**Pass 3 — Useless variables:**

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    GEN [label="All variables generate ✓\n(D→a, E→b, A→b, B→b|a, C→c|a, S→a)"];
    REA [label="Reachable from S:\nS ✓, A ✓, B ✓, C ✓, D ✓"];
    UNREA [label="E is NEVER mentioned\nin any production → NOT reachable"];
    REM [label="Remove E → b"];
    GEN -> REA;
    REA -> UNREA;
    UNREA -> REM;
}
```

**Final simplified grammar G':**
```
S → aS | a | aBD | aD | aB | c | bAD | bA | bD | b | λ
A → bAD | bA | bD | b
B → bC | b | AcDD | cDD | AcD | Ac | cD | c | a
C → AcDD | cDD | AcD | Ac | cD | c | a
D → a
```

---

## PROBLEM 6B — Convert to Chomsky Normal Form (CNF)

### What you're doing
Every production must be exactly:
- `A → BC` (exactly two non-terminals), OR
- `A → a` (exactly one terminal)

### Step-by-step procedure

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="Step 1: For every terminal a appearing in\na RHS of length ≥ 2:\n• Introduce Ba → a\n• Replace a in long RHS with Ba"];
    B [label="Step 2: For every RHS of length ≥ 3:\nchain it into pairs using new variables\nA → X1X2X3X4\nbecomes: A → X1D1, D1 → X2D2, D2 → X3X4"];
    C [label="Step 3: Productions of length 1 (A→a)\nand length 2 (A→BC) are already fine"];
    A -> B;
    B -> C;
}
```

> [!warning]
> `S → a` (length 1, all terminal) is already in CNF — do NOT touch it. Only productions of length ≥ 2 with terminals need modification.

### ✏️ Worked Example (from G')

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded];
    TERM [label="Introduce terminal variables:\nBa → a\nBb → b\nBc → c"];
    EX1 [label="S → aS (length 2 with terminal):\nreplace a → S → BaS ✓"];
    EX2 [label="S → aBD (length 3):\nS → BaBD → introduce D1→BD\n⇒ S → BaD1, D1 → BD"];
    EX3 [label="A → bAD (length 3):\nA → BbAD → introduce D2→AD\n⇒ A → BbD2, D2 → AD"];
    EX4 [label="B → AcDD (length 4):\nB → ABcDD → chain:\nB → AD3, D3 → BcD4, D4 → DD"];
    TERM -> EX1;
    TERM -> EX2;
    TERM -> EX3;
    TERM -> EX4;
}
```

**Applying the pattern to the rest of the grammar:**

- Step 1 (terminal rules): Every terminal `a`, `b`, `c` appearing in a RHS of length ≥ 2 is replaced by `Ba`, `Bb`, `Bc` respectively, and we add `Ba → a`, `Bb → b`, `Bc → c`.
- Step 2 (chaining): For every RHS of length ≥ 3, introduce new variables to chain into pairs, following the same pattern as the examples above.

After fully applying both steps, every production will have one of the two legal CNF forms: `A → BC` or `A → a`.

> [!tip] The examples above demonstrate the complete procedure. The full CNF grammar is long but mechanically follows the same pattern for each production in G'.

---

## PROBLEM 6C — Convert to Greibach Normal Form (GNF)

### What you're doing
Every production must start with a terminal:
- `A → a` ✓
- `A → aBC` ✓
- `A → AB` ✗ (starts with non-terminal — not allowed)

### Step-by-step procedure

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    A [label="Step 1: Start from simplified grammar G'"];
    B [label="Step 2: For every production starting\nwith a non-terminal:\nA → Bα and B → b1β1 | b2β2 | ...\nSubstitute: A → b1β1α | b2β2α | ..."];
    C [shape=diamond, label="Every RHS\nstarts with\na terminal?"];
    D [label="Step 3: Handle left recursion if needed:\nA → Aα | β becomes:\nA → β A'\nA' → α A' | α"];
    DONE [label="✓ Grammar is in GNF"];
    A -> B;
    B -> C;
    C -> B [label="No"];
    C -> D [label="Yes"];
    D -> DONE;
}
```

---

### ✏️ Worked Example (from simplified G')

Start from the simplified grammar G':

```
S → aS | aBD | aD | aB | c | bAD | bA | bD | b | λ
A → bAD | bA | bD | b
B → bC | b | AcDD | AcD | Ac | cDD | cD | c | a
C → AcDD | cDD | AcD | Ac | cD | c | a
D → a
```

**Step 2 — Substitute non-terminal starters:** B and C have productions starting with A (non-terminal). Look up A's productions and substitute each into B and C.

For B → AcDD, substitute A → bAD | bA | bD | b:
  ⇒ B → bADcDD | bAcDD | bDcDD | bcDD
Repeat for B → AcD and B → Ac similarly. After substitution:

```
S → aS | aBD | aD | aB | c | bAD | bA | bD | b | λ
A → bAD | bA | bD | b
B → bC | b | bADcDD | bAcDD | bDcDD | bcDD | bADcD | bAcD | bDcD | bcD | bADc | bAc | bDc | bc | cDD | cD | c | a
C → bADcDD | bAcDD | bDcDD | bcDD | bADcD | bAcD | bDcD | bcD | bADc | bAc | bDc | bc | cDD | cD | c | a
D → a
```

**Step 3 — All RHS start with a terminal** (a, b, or c) except S → λ ✓. No left recursion present ✓.

**Result: Grammar is in GNF** — every production has form `A → aα` (terminal followed by variables, or just terminal).

> [!tip] The NPDA example in Problem 6D below uses a separate, smaller GNF grammar for clarity. The conversion procedure shown here applies to any simplified CFG.

---

## PROBLEM 6D — Build NPDA from GNF Grammar

### What you're doing
Given a GNF grammar, mechanically write the NPDA. It always has exactly **3 states**.

### The fixed template (memorise this)

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    q0; q1;
    node [shape=doublecircle];
    q2;
    start -> q0;
    q0 -> q1 [label="λ, Z / SZ\n(push start variable)"];
    q1 -> q1 [label="a, A / α\n(for each rule A → aα)"];
    q1 -> q2 [label="λ, Z / λ\n(stack empty → accept)"];
}
```

> [!warning] Stack push order
> `δ(q₁, a, A) = (q₁, XY)` means **X is on top**. Write left-to-right as in the grammar production.

---

### ✏️ Fully Worked Example (mock exam Q6d)

**GNF Grammar:**
```
S → aA | bBD | c
A → a
B → bD
D → a
```

**NPDA transition diagram:**

```dot
digraph G {
    rankdir=LR;
    node [shape=point, width=0];
    start;
    node [shape=circle];
    q0; q1;
    node [shape=doublecircle];
    q2;
    start -> q0;
    q0 -> q1 [label="λ, Z / SZ\n(push start variable)", fontsize=10];
    q1 -> q1 [label="a, S / A\nb, S / BD\nc, S / λ\na, A / λ\nb, B / D\na, D / λ", fontsize=10];
    q1 -> q2 [label="λ, Z / λ\n(empty stack → accept)", fontsize=10];
}
```

**Transition function (all processing loops on q₁):**

```
δ(q₀, λ, Z)  = (q₁, SZ)     ← push start variable (always first)

δ(q₁, a, S)  = (q₁, A)      ← S → aA
δ(q₁, b, S)  = (q₁, BD)     ← S → bBD  (B on top of stack)
δ(q₁, c, S)  = (q₁, λ)      ← S → c     (pop S, push nothing)
δ(q₁, a, A)  = (q₁, λ)      ← A → a     (pop A)
δ(q₁, b, B)  = (q₁, D)      ← B → bD    (replace B with D)
δ(q₁, a, D)  = (q₁, λ)      ← D → a     (pop D)

δ(q₁, λ, Z)  = (q₂, λ)      ← empty stack → accept (always last)
```

**Trace — input `"c"` (accepted):**

```dot
digraph G {
    rankdir=TB;
    node [shape=box, style=rounded];
    header [label="Input | State | Stack", shape=plain];
    initial [label="Initial", style=dashed];
    step1 [label="q0, Z"];
    delta1 [label="δ(q0,λ,Z)=(q1,SZ)", style=dashed];
    step2 [label="q1, SZ"];
    read_c [label="read c"];
    delta2 [label="δ(q1,c,S)=(q1,λ) → pop S", style=dashed];
    step3 [label="q1, Z"];
    delta3 [label="δ(q1,λ,Z)=(q2,λ) → ACCEPT ✓", style=dashed];
    step4 [label="q2, ∅"];
    header -> initial;
    initial -> step1;
    step1 -> delta1;
    delta1 -> step2;
    step2 -> read_c;
    read_c -> delta2;
    delta2 -> step3;
    step3 -> delta3;
    delta3 -> step4;
}
```

---

## QUICK REFERENCE — One-Line Summaries

| Problem | What to do | Key thing to remember |
|---|---|---|
| **1A** NFA from RE | Bottom-up: atom → concat → union → star | Star adds back-loop AND skip-λ |
| **1B** Improve NFA | Compute λ-closure of each state, run subset construction | Start state = λ-closure(q₀) |
| **2** RE from automaton | State elimination: kill one state at a time | Formula: `r_iq · (r_qq)* · r_qj` |
| **3** Ambiguity | Find 1 string with 2 parse trees | Try "a", "aa", "aaa" first |
| **4** RLG→NFA→LLG | Variables=states → reverse arrows → re-read as LLG | Variable goes LEFT in LLG |
| **5** s-grammar | Check: starts with terminal AND no duplicate (Var, terminal) pairs | A→B (unit) instantly fails |
| **6a** Simplify | λ-nullable → unit pairs → useless (ALWAYS this order) | S stays if S was nullable |
| **6b** CNF | Bₐ for each terminal in long RHS; chain vars for length ≥ 3 | A→a and A→BC are the only legal forms |
| **6c** GNF | Substitute until every RHS starts with terminal | A→Bα: replace using B's productions; remove left recursion if needed |
| **6d** NPDA | 3-state template; one δ line per GNF production | δ(q₀,λ,Z)=(q₁,SZ) always first |

---

## COMMON EXAM MISTAKES

> [!warning] Do NOT make these mistakes
> 1. **λ-closure is transitive** — if q→p via λ and p→r via λ, then r is in λ-closure(q). Keep chaining.
> 2. **Nullable propagation** — if D→λ and C→D (unit), then C is nullable. Unit steps count.
> 3. **Unit pair closure** — if (S,A) and (A,B) are unit pairs, then (S,B) is also a unit pair.
> 4. **s-grammar with units** — `A → B` (unit production) automatically fails s-grammar (B is not a terminal).
> 5. **State elimination self-loop** — if no self-loop exists on the eliminated state, the term `(r_qq)*` simplifies to `λ` (since the only way to go from q to q is to take no transition at all). Effectively: just omit the star, write `r_iq · r_qj` directly.
> 6. **LLG direction** — `A → aB` (RLG) reverses to `B → Aa` (LLG), NOT `B → aA`.
> 7. **CNF terminal rule** — `A → a` (single terminal) is ALREADY in CNF. Don't introduce Bₐ for it — only for terminals inside longer productions.
> 8. **NPDA stack push order** — `δ(q₁, a, A) = (q₁, XY)` means X is top of stack. Write the string left-to-right as it appears in the grammar production.
> 9. **GNF substitution direction** — substitute FROM the variable that starts the RHS INTO the production. A → Bα: look up B's productions, substitute each in.
> 10. **Simplification order** — MUST be λ first, then unit, then useless. Doing unit before λ will give wrong results.
