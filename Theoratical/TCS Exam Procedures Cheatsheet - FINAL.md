> [!tip] 🎯 How to Use Each section = one exam task type. Read the **Procedure**, check the **Cases**, then verify with the **Worked Example**. Skip theory — just execute.

---

## 📌 Task 1 — Read a Regular Expression → Describe $L(r)$

### Procedure

1. Parse by **precedence**: ${}^*$ first, then $\cdot$, then $+$. Add parentheses mentally.
2. Translate each piece:
    - $a^*$ → zero or more $a$'s
    - $(xy)^*$ → zero or more repetitions of block $xy$
    - $r*1 + r*2$ → strings in $L(r*1)$ OR $L(r*2)$
    - $r*1 r*2$ → a string from $L(r*1)$ followed by one from $L(r*2)$
3. Express as set-builder notation ${w : \text{condition on } w}$.

### Cases to Watch

| Pattern                              | Meaning                                             |
| ------------------------------------ | --------------------------------------------------- |
| $(aa)^*$                             | Even-length strings of $a$'s: ${a^{2n} : n \geq 0}$ |
| $(aa)^* b$                           | Even $a$'s then one $b$                             |
| $(bb)^* b$                           | Odd number of $b$'s                                 |
| $(ab^*a + b)^*$                      | Each rep adds 0 or 2 $a$'s → $n*a(w)$ always even   |
| $r^*$ with $r$ containing only $a$'s | Controls parity or count of $a$                     |

### Worked Example

$$r = (aa)^*(bb)^*b$$

- $(aa)^*$ → ${a^{2n} : n \geq 0}$
- $(bb)^*b$ → ${b \cdot (bb)^m : m \geq 0} = {b^{2m+1} : m \geq 0}$ (odd $b$'s)

$$\boxed{L(r) = {a^{2n}b^{2m+1} : n \geq 0,\ m \geq 0}}$$

---

## 📌 Task 2 — Design a Regular Expression for a Given Language

### Procedure

1. **Identify constraints** on the strings (e.g. no consecutive 0s, even count, ends with something).
2. **Build blocks** that handle each constraint. Think: what can a single "unit" look like?
3. **Combine** with ${}^*$, $+$, concatenation.
4. **Check edge cases**: empty string ($\lambda$), single character, minimal strings.

### Cases to Watch

|Constraint|Strategy|
|---|---|
|No consecutive 0s|Unit = $1$ or $01$; trailing $0$ is optional → $(1+01)^*(0+\lambda)$|
|Strings starting with $a$|Prefix $a$, then $\Sigma^* = (a+b)^*$|
|Even number of $a$'s|Blocks that each contain exactly 2 $a$'s, with $b$'s anywhere: $(b^*ab^*a)^*b^*$|
|Ends with $ab$|$\Sigma^* \cdot ab = (a+b)^*ab$|
|At least one $a$|$(a+b)^*a(a+b)^*$|

### Worked Example

**Language:** $L = {w \in {0,1}^* : w \text{ has no pair of consecutive 0s}}$

**Reasoning:** Every 0 must be immediately followed by 1 (or be at the very end). So valid "units" are $1$ (safe alone) and $01$ (0 paired with 1). A trailing lone 0 is only okay at the end.

$$\boxed{r = (1+01)^*(0+\lambda)}$$

**Check:** $101$: match $(1)(01)(\lambda)$ ✓. $00$: after first 0 we need 1, but get 0 ✗.

---

## 📌 Task 3 — RE → NFA (via `re2nfa`)

### Procedure

**Build bottom-up.** Decompose $r$ into its parse tree, then assemble NFAs from leaves to root.

**Step 1 — Primitives:**

|Expression|NFA|
|---|---|
|$a \in \Sigma$|$q*0 \xrightarrow{a} q*f$ (one edge, $q*f$ final)|
|$\lambda$|$q*0 \xrightarrow{\lambda} q*f$ ($q*f$ final)|
|$\emptyset$|$q*0 \xrightarrow{\lambda} q*f$ (no final state)|

**Step 2 — Composites** (each sub-NFA must have no edges *into* its start or *out of* its final state):

**Union $r*1 + r*2$:**

- New start $s$, new final $f$
- $s \xrightarrow{\lambda} q*{01}$, $s \xrightarrow{\lambda} q*{02}$
- $q*{f1} \xrightarrow{\lambda} f$, $q*{f2} \xrightarrow{\lambda} f$

**Concatenation $r*1 r*2$:**

- Merge: $q*{f1} \xrightarrow{\lambda} q*{02}$
- Start = $q*{01}$, final = $q*{f2}$

**Star-closure $r^*$:**

- New start $s$, new final $f$
- $s \xrightarrow{\lambda} q*0$, $q*f \xrightarrow{\lambda} q*0$ (loop back), $s \xrightarrow{\lambda} f$ (accept $\lambda$), $q*f \xrightarrow{\lambda} f$

### Cases to Watch

- Always **name states** systematically: $q*0, q*1, \ldots$ or per sub-NFA.
- The final NFA has exactly **one** final state (by construction).
- $r^*$ must have a **direct $s \to f$ $\lambda$-skip** — otherwise $\lambda \notin L(r^*)$.

### Worked Example

**Build NFA for $r = (a + b)^*$**

1. $M(a)$: $q*0 \xrightarrow{a} q*1$
2. $M(b)$: $q*2 \xrightarrow{b} q*3$
3. $M(a+b)$ — Union:
    - New start $s*4$, new final $f*5$
    - $s*4 \xrightarrow{\lambda} q*0$, $s*4 \xrightarrow{\lambda} q*2$
    - $q*1 \xrightarrow{\lambda} f*5$, $q*3 \xrightarrow{\lambda} f*5$
4. $M((a+b)^*)$ — Star-closure of step 3:
    - New start $s*6$, new final $f*7$
    - $s*6 \xrightarrow{\lambda} s*4$, $f*5 \xrightarrow{\lambda} s*4$ (loop), $s*6 \xrightarrow{\lambda} f*7$, $f*5 \xrightarrow{\lambda} f*7$

Result: accepts any string of $a$'s and $b$'s including $\lambda$. ✓

---

## 📌 Task 4 — NFA → RE (via GTG State Removal)

### Procedure

**Goal:** Eliminate all intermediate states until only start $q*0$ and final $q*f$ remain. Then apply the 2-state formula.

**State removal rule:** To remove state $q$:

- For every pair $(q*i, q*j)$ where paths go $q*i \xrightarrow{a} q \xrightarrow{e^*} q \xrightarrow{b} q*j$ (with possible self-loop $e$ on $q$, direct edge $c: q*i \to q*j$):

$$q*i \xrightarrow{\ ae^*b\ +\ c\ } q*j$$

- If no self-loop on $q$: formula becomes $ae^*b = ab$ (i.e. $e = \emptyset$, so $e^* = \lambda$).
- If no direct edge $q*i \to q*j$: $c = \emptyset$, so just use $ae^*b$.

**Final 2-state formula** (start $q*0$, final $q*f$):

- $r*1$ = self-loop on $q*0$
- $r*2$ = edge $q*0 \to q*f$
- $r*3$ = edge $q*f \to q*0$ (back-edge; $\emptyset$ if none)
- $r*4$ = self-loop on $q*f$

$$\boxed{r = r*1^*\ r*2\ (r*4 + r*3 r*1^* r*2)^*}$$

### Cases to Watch

|Situation|What to do|
|---|---|
|Multiple final states|First merge them: add new $q*f$, add $\lambda$-edges from old finals to $q*f$|
|No self-loop on $q$ being removed|Use $e = \emptyset$, so $e^* = \lambda$ — simplify $ae^*b = ab$|
|No back-edge ($r*3 = \emptyset$)|Formula reduces to $r*1^* r*2 r*4^*$|
|$q*i$ and $q*j$ already have a direct edge|Combine: new label = $ae^*b + \text{existing label}$|
|Remove states one at a time|Order doesn't matter for correctness; pick the one with fewest connections first|

### Worked Example

**NFA:** $q*0 \xrightarrow{b} q*0$ (self), $q*0 \xrightarrow{a} q*1$, $q*1 \xrightarrow{b} q*1$ (self), $q*1 \xrightarrow{a} q*0$, $q*1 \xrightarrow{b} q*2$, $q*2 \xrightarrow{a+b} q*2$ (self). Start: $q*0$, Final: $q*2$.

**Remove $q*1$** (intermediate):

Pairs involving $q*1$: in-edges from $q*0 \xrightarrow{a}$; self-loop $\xrightarrow{b}$; out-edges $\xrightarrow{a} q*0$ and $\xrightarrow{b} q*2$.

- $(q*0, q*0)$: existing $b$ loop + path via $q*1$: $a \cdot b^* \cdot a$ → new label: $b + ab^*a$
- $(q*0, q*2)$: no existing direct edge + path via $q*1$: $a \cdot b^* \cdot b$ → label: $ab^*b$

Reduced GTG (2 states):

- $r*1 = b + ab^*a$ (self-loop on $q*0$)
- $r*2 = ab^*b$ (edge $q*0 \to q*2$)
- $r*3 = \emptyset$ (no back-edge)
- $r*4 = a+b$ (self-loop on $q*2$)

Apply formula: $$\boxed{r = (b + ab^*a)^*\ ab^*b\ (a+b)^*}$$

---

## 📌 Task 5 — Right-Linear Grammar → NFA (`GR*to*NFA`)

### Procedure

1. Each **variable** $V*i$ becomes a **state**.
2. Add a new **final state** $V*f$ (not in the grammar).
3. For each production **with a variable on the right** ($V*i \to a*1 \cdots a*m V*j$):
    - Draw path $V*i \xrightarrow{a*1} \bullet \xrightarrow{a*2} \cdots \xrightarrow{a*m} V*j$
4. For each production **without a variable** ($V*i \to a*1 \cdots a*m$):
    - Draw path $V*i \xrightarrow{a*1} \bullet \cdots \xrightarrow{a*m} V*f$
5. Start state = start variable $S$.

### Cases to Watch

- $V*i \to \lambda$: draw $V*i \xrightarrow{\lambda} V*f$ (i.e., $V*i$ itself becomes a final state, or add $\lambda$-edge to $V*f$).
- Multi-character terminal string $V*i \to abV*j$: requires **intermediate unnamed states** between $V*i$ and $V*j$.
- Multiple productions from same variable: draw **multiple** outgoing edges (NFA, not DFA — nondeterminism is fine).

### Worked Example

**Grammar:** $V*0 \to aV*1 \mid ba \quad V*1 \to aV*1 \mid abV*0 \mid b$

Variables → states: ${V*0, V*1}$. Add $V*f$.

Productions:

|Production|Type|Transition|
|---|---|---|
|$V*0 \to aV*1$|has variable|$V*0 \xrightarrow{a} V*1$|
|$V*0 \to ba$|terminal only|$V*0 \xrightarrow{b} \bullet \xrightarrow{a} V*f$|
|$V*1 \to aV*1$|has variable|$V*1 \xrightarrow{a} V*1$ (self-loop)|
|$V*1 \to abV*0$|has variable|$V*1 \xrightarrow{a} \bullet \xrightarrow{b} V*0$|
|$V*1 \to b$|terminal only|$V*1 \xrightarrow{b} V*f$|

Start: $V*0$. Final: $V*f$.

---

## 📌 Task 6 — NFA → Right-Linear Grammar (`NFA*to*GR`)

### Procedure

1. Each **state** $q*i$ becomes a **variable**. Start variable = $q*0$.
2. For each transition $\delta(q*i, a) = q*k$: add production $q*i \to a, q*k$.
3. For each **final state** $q*f \in F$: add production $q*f \to \lambda$.

### Cases to Watch

- If $q*f$ also has outgoing transitions, it gets **both** $q*f \to \lambda$ **and** $q*f \to a,q*k$ productions.
- $\lambda$-transitions in the NFA: add $q*i \to \lambda, q*k$ which simplifies to $q*i \to q*k$ (a unit production — technically allowed but makes it not right-linear in the strict sense; your notes use this form).

### Worked Example

**NFA:** states ${q*0, q*1, q*2}$, transitions: $\delta(q*0, a) = q*1$, $\delta(q*1, b) = q*2$, $\delta(q*2, a) = q*0$. Final: ${q*2}$.

Productions:

- $q*0 \to a,q*1$
- $q*1 \to b,q*2$
- $q*2 \to a,q*0$
- $q*2 \to \lambda$ (final state)

Grammar: $G = ({q*0,q*1,q*2}, {a,b}, q*0, P)$

---

## 📌 Task 7 — Right-Linear → Left-Linear Grammar (Reversal)

### Procedure

1. **Build NFA $M$** from the right-linear grammar (use Task 5 procedure).
2. **Reverse $M$** to get $M^R$:
    - Swap start and final: old final(s) become the new start(s); old start becomes new final.
    - **Reverse all edges**: every $q*i \xrightarrow{a} q*j$ becomes $q*j \xrightarrow{a} q*i$.
3. **Extract right-linear grammar $G^R$** from $M^R$ (use Task 6 procedure).
4. **Convert to left-linear $G^L$**: reverse each production body.
    - $A \to aB$ becomes $A \to Ba$
    - $A \to ab$ (terminal string) stays as $A \to ba$ (reversed terminals)
    - $A \to \lambda$ stays as $A \to \lambda$

### Cases to Watch

- If the original NFA had a single final state $q*f$, then $M^R$ has a single start state $q*f$ and a single final state $q*0$ (old start).
- If the original NFA had multiple final states, $M^R$ has multiple start states → may need to add a single new start with $\lambda$-transitions.
- Don't forget to reverse the **terminal string** too: $A \to abc$ reverses to $A \to cba$.

### Worked Example

**Grammar:** $S \to aS \mid bA \quad A \to bB \mid a \quad B \to aS \mid b$

**Step 1 — NFA $M$:** States ${S, A, B, F}$. Transitions: $S \xrightarrow{a} S$, $S \xrightarrow{b} A$, $A \xrightarrow{b} B$, $A \xrightarrow{a} F$, $B \xrightarrow{a} S$, $B \xrightarrow{b} F$. Final: ${F}$.

**Step 2 — Reverse to $M^R$:** Swap: start = $F$, final = ${S}$. Reverse edges: $S \xrightarrow{a} S$, $A \xrightarrow{b} S$, $B \xrightarrow{b} A$, $F \xrightarrow{a} A$, $S \xrightarrow{a} B$, $F \xrightarrow{b} B$.

**Step 3 — Extract right-linear grammar from $M^R$** (start = $F$, final = $S$): $$F \to aA \mid bB \quad A \to bS \quad B \to bA \quad S \to aS \mid aB \mid \lambda$$

**Step 4 — Reverse bodies to get left-linear $G^L$:** $$\boxed{F \to Aa \mid Bb \quad A \to Sb \quad B \to Ab \quad S \to Sa \mid Ba \mid \lambda}$$

---

## 📌 Task 8 — Design a CFG for a Given Language

### Procedure

**Identify the structure type, then apply the matching template:**

|Language Structure|Template Grammar|
|---|---|
|${a^n b^n}$ (equal counts)|$S \to aSb \mid \lambda$|
|${a^n b^m : n \neq m}$ (unequal)|Split: $n > m$ case + $n < m$ case; combine with $S \to S*1 \mid S*2$|
|${ww^R}$ (even palindromes)|$S \to aSa \mid bSb \mid \lambda$|
|${w : n*a(w) = n*b(w)}$ (balanced)|$S \to aSb \mid bSa \mid SS \mid \lambda$|
|Nested parentheses|$S \to aSb \mid SS \mid \lambda$|
|Concatenation of two CFLs $L*1 L*2$|$S \to S*1 S*2$ with grammars for $L*1, L*2$|
|Union $L*1 \cup L*2$|$S \to S*1 \mid S*2$ with grammars for $L*1, L*2$|

### Cases to Watch

- **$n \neq m$ trick:** Split into $n > m$ and $n < m$ sub-problems. For $n > m$: generate matched $a^k b^k$ via $S*1 \to aS*1b \mid \lambda$, then prepend surplus $a$'s via $A \to aA \mid a$.
- **Multiple constraints:** Handle each constraint with a sub-grammar, then combine.
- If the language uses both $a$-surplus and $b$-surplus, you need **two separate start productions** for each case.

### Worked Example

**Language:** $L = {a^n b^m : n \neq m,\ n,m \geq 0}$

**Case 1 ($n > m$):** Extra $a$'s prepended before a matched block. $$S \to AS*1, \quad S*1 \to aS*1b \mid \lambda, \quad A \to aA \mid a$$

**Case 2 ($n < m$):** Extra $b$'s appended after a matched block. $$S \to S*1 B, \quad B \to bB \mid b$$

**Combined:** $$\boxed{S \to AS*1 \mid S*1B \quad S*1 \to aS*1b \mid \lambda \quad A \to aA \mid a \quad B \to bB \mid b}$$

---

## 📌 Task 9 — Write a Derivation (Leftmost or Rightmost)

### Procedure

**Leftmost:** At each step, find the **leftmost variable** in the current sentential form. Replace it (and only it) using one production. Repeat.

**Rightmost:** At each step, find the **rightmost variable**. Replace it.

**Both derivations must yield the same string**, just in different orders.

### Cases to Watch

- Number the productions if given (e.g. (1) $S \to AB$, (2) $A \to aA$…); write the number above $\Rightarrow$ for clarity.
- "Which production to choose" — for the exam string $w$, work backwards: look at $w$, figure out which production the start symbol must have used, then continue.
- If a sentential form has only terminals → you're done; check it equals $w$.

### Worked Example

**Grammar:** $S \to AB$ (1), $A \to aaA$ (2), $A \to \lambda$ (3), $B \to Bb$ (4), $B \to \lambda$ (5). **Derive $aab$.**

**Leftmost** (always replace leftmost variable): $$S \overset{1}{\Rightarrow} AB \overset{2}{\Rightarrow} aaAB \overset{3}{\Rightarrow} aaB \overset{4}{\Rightarrow} aaBb \overset{5}{\Rightarrow} aab\ \checkmark$$

**Rightmost** (always replace rightmost variable): $$S \overset{1}{\Rightarrow} AB \overset{4}{\Rightarrow} ABb \overset{5}{\Rightarrow} Ab \overset{2}{\Rightarrow} aaAb \overset{3}{\Rightarrow} aab\ \checkmark$$

---

## 📌 Task 10 — Prove a Grammar is Ambiguous

### Procedure

1. Find a string $w \in L(G)$ (try short strings first: length 2, 3, 4).
2. Find **two distinct leftmost derivations** of $w$ (or equivalently, two distinct parse trees).
3. State: "Two distinct derivation trees for $w$ → grammar is ambiguous."

> [!warning] ⚠️ Key Point The derivations must use **different productions** or derive $w$ via **different structural paths** — not just different orderings of the same productions. (Same productions in different order → same parse tree → NOT ambiguous.)

### Cases to Watch

|Grammar type|Good test string|
|---|---|
|$S \to AB \mid aaB$, $A \to a \mid Aa$|Try $aab$|
|$S \to aSb \mid SS \mid \lambda$|Try $aabb$|
|$E \to E+E \mid E*E \mid I$|Try $a+b*c$|
|$S \to aSbS \mid bSaS \mid \lambda$|Try $ab$|

### Worked Example A — Two different top-level productions

**Grammar:** $S \to AB \mid aaB$, $A \to a \mid Aa$, $B \to b$. **String:** $w = aab$.

**Derivation 1** (via $S \to AB$): $$S \Rightarrow AB \Rightarrow AaB \Rightarrow aaB \Rightarrow aab$$

**Derivation 2** (via $S \to aaB$): $$S \Rightarrow aaB \Rightarrow aab$$

Two distinct leftmost derivations → **ambiguous**. ✓

### Worked Example B — Same top-level production, different sub-structure

**Grammar:** $S \to aSbS \mid bSaS \mid \lambda$. **String:** $w = ab$.

**Derivation 1** (replace left $S$ with $\lambda$ first): $$S \Rightarrow aSbS \Rightarrow abS \Rightarrow ab$$

**Derivation 2** (replace right $S$ with $\lambda$ first): $$S \Rightarrow aSbS \Rightarrow aSb \Rightarrow ab$$

Both use $S \to aSbS$ at the top but create different parse trees (left $S$-subtree is $\lambda$ in tree 1; right $S$-subtree is $\lambda$ in tree 2) → **ambiguous**. ✓

---

## 📌 Task 11 — Identify / Verify an s-Grammar

### Procedure

Check two conditions:

1. Every production has the form $A \to ax$ where $a \in T$ (starts with a **terminal**) and $x \in V^*$ (rest are variables only).
2. Each **pair $(A, a)$** appears **at most once** in $P$ — i.e., no two productions for the same variable start with the same terminal.

If both hold → **s-grammar**. If either fails → **not an s-grammar**.

### Worked Example

**(a)** $S \to aS \mid bSS \mid c$

- All productions start with a terminal ✓
- Pairs: $(S,a)$, $(S,b)$, $(S,c)$ — each appears once ✓ → **s-grammar**

**(b)** $S \to aS \mid bSS \mid aSS \mid c$

- Pair $(S,a)$ appears twice: $S \to aS$ and $S \to aSS$ ✗ → **not an s-grammar**

---

## 📌 Task 12 — Exhaustive Search Parsing

### Procedure

Round by round, expand **all** current sentential forms by replacing their **leftmost variable** with every applicable production. Keep only forms that could still yield $w$ (prune if length $> |w|$, or if prefix already mismatches).

**Stop when** $w$ appears, or all remaining forms have length $> |w|$ (→ $w \notin L(G)$).

> [!note] 💡 This only terminates as an algorithm if the grammar has **no $\lambda$-productions** and **no unit productions** (Theorem 5.2).

### Worked Example

**Grammar:** $S \to SS \mid aSb \mid bSa \mid \lambda$. **String:** $w = aabb$.

|Round|New sentential forms|
|---|---|
|0|$S$|
|1|$SS$, $aSb$, $bSa$, $\lambda$|
|2 (from $aSb$)|$aSSb$, $\mathbf{aaSbb}$, $abSab$, $ab$|
|3 (from $aaSbb$)|$aa,aSb,bb \Rightarrow \ldots \Rightarrow \mathbf{aabb}$ ✓|

Parse: $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aa\lambda bb = aabb$. ✓

---

## 🗂️ Quick Reference — Grand Equivalence

```
Regular Expression
      ⟺ (Thm 3.1 / 3.2)
DFA / NFA
      ⟺ (Thm 3.3 / 3.4)
Right-Linear Grammar
      ⟺ (Reversal)
Left-Linear Grammar
```

All four represent exactly the **regular languages**.

**CFL hierarchy:** $$\text{Regular} \subsetneq \text{Linear} \subseteq \text{Context-Free}$$

**Key non-regular / non-CFL signals:**

- Requires counting/matching ($a^n b^n$, $n*a(w) = n*b(w)$) → **not regular**, but **CFL**
- Requires double matching ($a^n b^n c^n$) → **not CFL** (needs pushdown + more)

---

## ⚡ Formulas to Memorize

|Formula|When to Use|
|---|---|
|$r = r*1^* r*2 (r*4 + r*3 r*1^* r*2)^*$|Final step of GTG state removal (Task 4)|
|Remove state $q$: $q*i \xrightarrow{ae^*b + c} q*j$|Each intermediate step of state removal|
|$L(r*1 + r*2) = L(r*1) \cup L(r*2)$|Reading REs (Task 1)|
|$L(r^*) = {\lambda} \cup L(r) \cup L(r)L(r) \cup \ldots$|Reading REs|
|$(r^*)^* = r^*$, $(r*1^* + r*2)^* = (r*1+r*2)^*$|Simplifying REs|