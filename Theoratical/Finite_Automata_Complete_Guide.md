# Finite Automata — A Complete Beginner's Guide
*From zero knowledge to a working C++ implementation*

---

## Table of Contents

- [[#Part 1 — What is a Finite Automaton?]]
- [[#Part 2 — Deterministic Finite Accepter (DFA)]]
- [[#Part 3 — Nondeterministic Finite Accepter (NFA)]]
- [[#Part 4 — Converting NFA to DFA]]
- [[#Part 5 — Minimizing a DFA]]
- [[#Part 6 — Regular Expressions and re2nfa]]
- [[#Part 7 — The C++ Implementation]]
- [[#Part 8 — How to Use the Program]]

---

# Part 1 — What is a Finite Automaton?

## The Big Picture

Imagine a very simple machine. It has a set of **states** (like different "moods" or "conditions"), and it reads a string of characters one by one. After reading each character, it **moves to a new state** based on a rule. When it finishes reading the string, it either says **"yes, I accept this"** or **"no, I reject this"**.

That machine is called a **Finite Automaton**.

## A Real-Life Analogy

Think of a **vending machine**:

- It has states: `waiting`, `got_10_cents`, `got_20_cents`, `dispense`
- It reads inputs: you insert coins
- It has rules: if you are in `got_10_cents` and insert another 10 cents → move to `got_20_cents`
- It accepts when it reaches `dispense`

A finite automaton works the exact same way — it just reads characters from a string instead of coins.

## Core Vocabulary

Before going further, here are the terms you will see everywhere:

| Term | Symbol | Plain English |
|------|--------|---------------|
| **State** | `q` | A "situation" the machine can be in |
| **Alphabet** | `Σ` (Sigma) | The set of allowed input characters, e.g. `{a, b}` |
| **Transition function** | `δ` (delta) | The rule: "if I am in state X and read character Y, go to state Z" |
| **Initial state** | `q0` | Where the machine starts |
| **Final / Accepting state** | `F` | States where the machine says "yes" |
| **String** | `w` | A sequence of characters from the alphabet, e.g. `"abba"` |

## What Does "Accept" Mean?

A machine **accepts** a string if, after reading every character, it ends up in a **final state**.

It **rejects** a string if it ends up in any other state, or if at any point it has no valid move.

---

# Part 2 — Deterministic Finite Accepter (DFA)

## What Makes It "Deterministic"?

In a DFA, every state has **exactly one** transition for each possible input character. There is no ambiguity — given your current state and the character you just read, there is only one place to go.

> [!tip] Key rule
> In a DFA: for every state `q` and every character `a`, there is **exactly one** next state. No more, no less.

## Drawing a DFA

DFAs are usually drawn as **directed graphs**:
- **Circles** = states
- **Arrows** = transitions (labeled with the input character)
- **Double circle** = final/accepting state
- **Arrow with no source** = initial state

### Example: DFA that accepts strings ending in `ab`

Over alphabet `{a, b}`, we want to accept `ab`, `aab`, `bab`, `ababab` — any string whose last two characters are `ab`.

Transition table:

| State | `a` | `b` |
|-------|-----|-----|
| `→q0` (initial) | `q1` | `q0` |
| `q1` | `q1` | `q2` |
| `q2` ★ (final) | `q1` | `q0` |

**Reading `"aab"`:**

```
Start:    currentState = q0
Read 'a': δ(q0, a) = q1  →  currentState = q1
Read 'a': δ(q1, a) = q1  →  currentState = q1
Read 'b': δ(q1, b) = q2  →  currentState = q2
End: q2 is a final state → ACCEPTED ✓
```

**Reading `"ba"`:**

```
Start:    currentState = q0
Read 'b': δ(q0, b) = q0  →  currentState = q0
Read 'a': δ(q0, a) = q1  →  currentState = q1
End: q1 is NOT a final state → REJECTED ✗
```

## Exercise 1 — Checking if a String is Accepted

**The task:** Given a DFA (as a table) and a string `s`, simulate the machine and output `Valid!` or `Invalid`.

### Algorithm

```
1. Start at the initial state q0
2. For each character c in the string s:
     a. Find which column c belongs to in the table
     b. If c is not in the alphabet → reject immediately
     c. Find the row for the current state
     d. Move to the state in that cell
3. After reading all characters:
     If current state is in F → "Valid!"
     Otherwise               → "Invalid"
```

### The Code

```cpp
void exercise1()
{
    freopen("dfa.inp", "r", stdin);
    int n, m;
    cin >> n >> m;
    string dfa[n][m];       // the full table (n rows, m columns)
    vector<string> fstate;  // list of final states
    vector<string> sigma;   // list of alphabet symbols

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
        {
            cin >> dfa[i][j];
            if (dfa[i][j][0] == '*')
            {
                dfa[i][j].erase(0, 1);        // remove the '*'
                fstate.push_back(dfa[i][j]);  // remember it's final
            }
        }

    for (int i = 1; i < m; ++i)
        sigma.push_back(dfa[0][i]);  // header row → alphabet

    cin >> s;
    string currentState = dfa[1][0];  // initial state = first data row

    for (int i = 0; i < s.length(); ++i)
    {
        auto it    = find(begin(sigma), end(sigma), string(1, s[i]));
        int  index = distance(sigma.begin(), it) + 1;

        if (index == m) { cout << "\nInvalid!"; return; }

        for (int j = 1; j < n; ++j)
            if (dfa[j][0] == currentState)
            {
                currentState = dfa[j][index];
                break;
            }
    }

    if (find(begin(fstate), end(fstate), currentState) != fstate.end())
        cout << "\nValid!";
    else
        cout << "\nInvalid";
}
```

### Code Explanation — Line by Line

**`freopen("dfa.inp", "r", stdin)`**
Redirects `cin` to read from the file `dfa.inp` instead of the keyboard. Every `cin >>` after this line reads from the file automatically — no manual typing during testing.

**`string dfa[n][m]`**
A 2D array of strings. Row 0 is the header (`NULL a b ...`). Rows 1 to n-1 are the actual states. Column 0 is always the state name; columns 1 onwards are transition destinations.

**`if (dfa[i][j][0] == '*')`**
`[0]` gets the first character of the string. If it is `*`, this state is final. We strip it with `erase(0, 1)` so the name is clean for comparisons later.

**`find(...) + distance(...)`**
`find` searches `sigma` for the character and returns an iterator. `distance` turns that iterator into a plain integer index. We add `1` because column 0 is the state name column, not a symbol column.

**`index == m`**
If `find` reaches the end without a match, `distance` returns `sigma.size()`, so `+1` equals `m`. That means the character is not in the alphabet — reject immediately.

---

# Part 3 — Nondeterministic Finite Accepter (NFA)

## What Makes It "Nondeterministic"?

In an NFA, a state can have:
- **Zero** transitions for some input (no rule for that character)
- **Multiple** transitions for the same input (go to several states at once)
- **Lambda (λ) transitions** — moves to another state **without reading any character**

> [!tip] Intuition
> Think of an NFA as a machine that **splits into parallel copies** of itself. When there are multiple possible transitions, all paths are explored simultaneously. If **any one** copy ends up in a final state, the string is accepted.

## Lambda (λ) Transitions

A λ-transition lets the machine jump to another state for free — without consuming any input. This makes NFAs much easier to design, even though they are harder to simulate directly.

## The λ-closure

The **λ-closure** of a state `q` is the set of all states reachable from `q` using **only λ-transitions** (zero or more), including `q` itself.

```
q0 --λ--> q1 --λ--> q2
                q2 --λ--> q3

λ-closure(q0) = {q0, q1, q2, q3}
λ-closure(q1) = {q1, q2, q3}
λ-closure(q2) = {q2, q3}
λ-closure(q3) = {q3}
```

The algorithm is a simple **DFS** starting from `q`, following only λ-edges.

## The Extended Transition Function δ*

`δ*(q, a)` answers: "starting from `q`, after reading `a`, which states can I possibly be in?"

The formula:

```
δ*(q, a) = λ-closure( move( λ-closure(q), a ) )
```

| Step | Operation | What it does |
|------|-----------|-------------|
| 1 | `λ-closure(q)` | All states reachable via λ from `q` |
| 2 | `move(T, a)` | Follow symbol `a` from every state in T (no λ) |
| 3 | `λ-closure(result)` | Follow any λ-transitions from the landing states |

## Exercise 2 — Computing λ-closure and δ*

**The task:** Read an NFA, then for a given state `q` and symbol `a`, compute and print `λ-closure(q)` and `δ*(q, a)`.

### NFA Table Format

NFA cells hold **sets** of states written as `{q1,q2}` or `{}`. The λ-column uses `~` in the header.

### `parseCell()` — Reading Multi-State Cells

```cpp
vector<string> parseCell(string cell)
{
    cell.erase(remove(cell.begin(), cell.end(), '{'), cell.end());
    cell.erase(remove(cell.begin(), cell.end(), '}'), cell.end());
    vector<string> res;
    stringstream ss(cell);
    string tok;
    while (getline(ss, tok, ','))
        if (!tok.empty()) res.push_back(tok);
    return res;
}
```

`remove` shuffles all `{` characters to the end; `erase` cuts them off. Then `stringstream + getline` splits by commas — the standard C++ string-split idiom.

### `lambdaClosure()` — DFS Over λ-Edges

```cpp
set<string> lambdaClosure(const string& state, ...)
{
    set<string> closure;
    stack<string> stk;
    stk.push(state);
    closure.insert(state);      // always include the start

    while (!stk.empty())
    {
        string cur = stk.top(); stk.pop();
        for (int i = 1; i < n; ++i)
            if (nfa[i][0] == cur)
            {
                vector<string> nexts = parseCell(nfa[i][lambdaCol]);
                for (auto& nx : nexts)
                    if (!closure.count(nx))  // not yet visited
                    {
                        closure.insert(nx);
                        stk.push(nx);
                    }
                break;
            }
    }
    return closure;
}
```

Standard DFS: push a state, pop it, look at all its λ-destinations, push unvisited ones. Stops when the stack is empty.

---

# Part 4 — Converting NFA to DFA

## Why Convert?

NFAs are easy to design but hard to execute (you would need to track all parallel states). DFAs are easy to run. The **subset construction** converts any NFA into an equivalent DFA accepting exactly the same strings.

## The Key Insight

Each **DFA state** = a **set of NFA states** — all the NFA states the machine could possibly be in at that point.

## The Algorithm (page 46)

```
1. Initial DFA state = λ-closure(q0 of NFA)
2. Repeat until no DFA state has a missing edge:
   - Take a DFA state S with no outgoing edge for symbol a
   - Compute target = λ-closure(move(S, a))
   - If target is new, create a new DFA state for it
   - Add edge S --a--> target
3. Any DFA state containing a final NFA state → mark as final
```

## Exercise 3 — nfa2dfa

**The task:** Read an NFA, run the subset construction, print the resulting DFA table.

### Code Walkthrough

```cpp
set<string> init = lambdaClosure(nfa[1][0], ...);

map<string, vector<string>> dfaTable;  // label → transitions
map<string, set<string>>   labelToSet; // label → actual NFA state set
queue<string> worklist;

labelToSet[initLabel] = init;
worklist.push(initLabel);

while (!worklist.empty())
{
    string curLabel = worklist.front(); worklist.pop();

    for each symbol in sigma:
    {
        set<string> mv   = moveSet(cur, col, ...);
        set<string> next = lambdaClosureSet(mv, ...);
        string nextLabel = setToLabel(next);

        dfaTable[curLabel].push_back(nextLabel);

        if (!next.empty() && !dfaTable.count(nextLabel))
            worklist.push(nextLabel);  // newly discovered DFA state
    }
}
```

A DFA state is **final** if its NFA-state set contains at least one NFA final state:

```cpp
for (auto& fs : nfaFinal)
    if (st.count(fs)) { prefix += "*"; break; }
```

---

# Part 5 — Minimizing a DFA

## Why Minimize?

A DFA converted from an NFA often has redundant states — states that behave identically for all inputs. Minimization merges them into the smallest possible equivalent DFA.

## Distinguishable vs Indistinguishable States

Two states `p` and `q` are **distinguishable** if there is some string `w` accepted from `p` but rejected from `q` (or vice versa). If no such string exists, they are **indistinguishable** and can be safely merged.

## The Three Phases

### Phase 1 — Remove Inaccessible States

BFS from the initial state. Any state not reached is useless and is discarded.

### Phase 2 — `mark()`: Table-Filling Algorithm

Build a triangular table of all state pairs. Mark a pair as distinguishable if:

**Base case:** one state is final, the other is not. Distinguishable by the empty string.

**Propagation:** For unmarked pair `(p, q)` and symbol `a`, if `(δ(p,a), δ(q,a))` is already marked → mark `(p, q)` too. Repeat until no changes.

```cpp
bool changed = true;
while (changed)
{
    changed = false;
    for each unmarked pair (i, j):
        for each symbol column k:
        {
            string ti = dfa[rows[i]][k];  // δ(p, a)
            string tj = dfa[rows[j]][k];  // δ(q, a)
            if (ti == tj) continue;
            if dist[ti][tj] is marked:
                mark dist[i][j] = true; changed = true;
        }
}
```

### Phase 3 — `reduce()`: Build the Minimized DFA

Any pair never marked → indistinguishable → group into one **equivalence class**.

| Component | Rule |
|-----------|------|
| States | One per equivalence class |
| Initial state | Class containing original `q0` |
| Final states | Any class containing an original final state |
| Transitions | Follow transitions of any representative from each class |

## Exercise 4 — Worked Example

Original 6-state DFA (final states `q4`, `q5`):

| State | `a` | `b` |
|-------|-----|-----|
| `→q0` | `q1` | `q2` |
| `q1` | `q1` | `q3` |
| `q2` | `q1` | `q4`★ |
| `q3` | `q1` | `q5`★ |
| `q4`★ | `q1` | `q5`★ |
| `q5`★ | `q1` | `q5`★ |

After marking, three equivalence classes emerge:

```
Class 0: {q0, q1}   ← both non-final, same transition pattern
Class 1: {q2, q3}
Class 2: {q4, q5}   ← both final, same transitions

=== Minimized DFA ===
  ->q0,q1   →  q0,q1  |  q2,q3
    q2,q3   →  q0,q1  |  q4,q5
   *q4,q5   →  q0,q1  |  q4,q5
```

**6 states → 3 states ✓**

---

# Part 6 — Regular Expressions and re2nfa

## What is a Regular Expression?

A **regular expression** (regex) is a compact textual notation for describing a language. Instead of drawing an automaton, you write a pattern. The `re2nfa` procedure converts any regular expression into an NFA that accepts exactly the same language.

## Regular Expression Syntax

| Operator | Written as | Meaning | Example |
|----------|-----------|---------|---------|
| **Union** | `r1+r2` | strings in r1 **or** r2 | `a+b` accepts `a` or `b` |
| **Concatenation** | `r1r2` | r1 **followed by** r2 | `ab` accepts only `"ab"` |
| **Kleene star** | `r*` | zero or more repetitions of r | `a*` accepts `""`, `"a"`, `"aa"`, ... |
| **Grouping** | `(r)` | override precedence | `(a+b)*` = any string of a's and b's |
| **Empty language** | `#` | accepts nothing | no string is accepted |
| **Lambda** | `~` | accepts only the empty string ε | accepts `""` only |

**Precedence** (highest to lowest): `*` → concatenation → `+`

So `ab+c` means `(ab)+c`, not `a(b+c)`. Use parentheses to override.

## The re2nfa Procedure (pages 17–19)

The idea: build a tiny NFA for each atomic piece of the regex, then combine those NFAs using three construction rules — one for each operator.

### Step 1 — Primitive NFAs (page 17)

Every basic element becomes a two-state NFA:

**a) Empty language `#`**
Two isolated states, no transitions. Nothing is ever accepted.
```
→[q0]     [q1★]      (no arrows)
```

**b) Lambda `~`**
One λ-transition. Accepts only the empty string.
```
→[q0] --λ--> [q1★]
```

**c) Single symbol `a`**
One `a`-transition. Accepts only the single character `a`.
```
→[q0] --a--> [q1★]
```

In code, each is a factory function that calls `newState()` twice (getting two fresh IDs) and optionally adds one transition.

There are no globals. Instead, `exercise5()` declares `counter` and `nfa` as local variables and passes them down by reference — the same pattern used throughout the codebase with `dfa[n][m]`, `sigma`, and `fstate`:

```cpp
typedef map<int,map<string,set<int>>> NfaMap;  // type alias to keep signatures readable

int newState(int& counter) { return counter++; }

pair<int,int> makeEmpty(int& counter, NfaMap& nfa)
{
    int q0 = newState(counter), qf = newState(counter);
    return {q0, qf};  // no transition added
}

pair<int,int> makeLambda(int& counter, NfaMap& nfa)
{
    int q0 = newState(counter), qf = newState(counter);
    nfa[q0]["~"].insert(qf);
    return {q0, qf};
}

pair<int,int> makeSymbol(const string& a, int& counter, NfaMap& nfa)
{
    int q0 = newState(counter), qf = newState(counter);
    nfa[q0][a].insert(qf);
    return {q0, qf};
}
```

Each `make*` function returns a `pair<int,int>` — `.first` is the initial state, `.second` is the final state. All actual transitions live in the `NfaMap` passed by reference, so combining two NFAs only means adding a few entries to that map.

### Step 2 — Combining NFAs (pages 18–19)

#### Union: `r1 + r2` (page 18)

Create a new start state that branches λ into both machines, and a new final state that both machines feed into via λ:

```
          λ --> [M(r1)] --λ
→[new q0]                    --> [new qf★]
          λ --> [M(r2)] --λ
```

**Conditions from the slide:** no edges coming into `q01`/`q02`, no edges going out of `qf1`/`qf2`. The primitive constructors guarantee this because each primitive's start and end states are brand new.

```cpp
pair<int,int> makeUnion(pair<int,int> a, pair<int,int> b, int& counter, NfaMap& nfa)
{
    int q0 = newState(counter), qf = newState(counter);
    nfa[q0]["~"].insert(a.first);    // λ into first NFA
    nfa[q0]["~"].insert(b.first);    // λ into second NFA
    nfa[a.second]["~"].insert(qf);   // λ out of first NFA
    nfa[b.second]["~"].insert(qf);   // λ out of second NFA
    return {q0, qf};
}
```

#### Concatenation: `r1 r2` (page 19)

Wire the final state of M(r1) directly to the initial state of M(r2) with a λ-transition:

```
→[M(r1)] --λ--> [M(r2)★]
```

**Conditions from the slide:** no edges out of `qf1`, no edges into `q02` — again guaranteed by construction.

```cpp
pair<int,int> makeConcat(pair<int,int> a, pair<int,int> b, NfaMap& nfa)
{
    nfa[a.second]["~"].insert(b.first);  // bridge: end of r1 → start of r2
    return {a.first, b.second};           // spans from r1's start to r2's end
}
```

No new states are created. We only add one λ-edge and return new outer endpoints.

#### Kleene Star: `r*` (page 19 / image 1)

Wrap M(r) with a new start and end state. Wire them so the machine can:
- Accept ε immediately by skipping M(r)
- Go through M(r) once, then loop back to repeat
- Exit after any repetition

```
→[new q0] --λ--> [M(r)] --λ--> [new qf★]
     |                               ↑
     └──────────λ────────────────────┘   (skip = accept ε)
                [M(r)'s qf] --λ--> [M(r)'s q0]   (loop)
```

**Conditions from the slide:** no edges into the original `q0`, no edges out of the original `qf`.

```cpp
pair<int,int> makeStar(pair<int,int> a, int& counter, NfaMap& nfa)
{
    int q0 = newState(counter), qf = newState(counter);
    nfa[q0]["~"].insert(a.first);     // enter M(r)
    nfa[q0]["~"].insert(qf);          // skip M(r) entirely (accept ε)
    nfa[a.second]["~"].insert(a.first); // loop: repeat M(r)
    nfa[a.second]["~"].insert(qf);    // exit after this repetition
    return {q0, qf};
}
```

## Exercise 5 — re2nfa

**The task:** Read a regular expression from `re.inp`, build its NFA using the construction rules above, and print the NFA transition table (ready to use as `nfa.inp`) plus a human-readable transition list.

### The Recursive Descent Parser

To turn text like `(a+b)*ab` into the right sequence of `makeUnion / makeConcat / makeStar` calls, we use a **recursive descent parser** — one function per level of operator precedence. Each level calls the higher-precedence level first, then handles its own operator in a loop.

**Grammar:**
```
expr   →  term ( '+' term )*      ← union, lowest precedence
term   →  factor factor*          ← concatenation (implicit)
factor →  base '*'*               ← Kleene star
base   →  '(' expr ')' | '#' | '~' | any letter
```

All four parser functions receive `re` (the string), `pos` (current read position), `counter`, and `nfa` by reference — no globals anywhere:

```cpp
pair<int,int> parseExpr(const string& re, int& pos, int& counter, NfaMap& nfa)
{
    pair<int,int> result = parseTerm(re, pos, counter, nfa);
    while (pos < re.size() && re[pos] == '+')
    {
        pos++;   // consume '+'
        result = makeUnion(result, parseTerm(re, pos, counter, nfa), counter, nfa);
    }
    return result;
}

pair<int,int> parseTerm(const string& re, int& pos, int& counter, NfaMap& nfa)
{
    pair<int,int> result = parseFactor(re, pos, counter, nfa);
    while (pos < re.size() && re[pos] != '+' && re[pos] != ')')
        result = makeConcat(result, parseFactor(re, pos, counter, nfa), nfa);
    return result;
}

pair<int,int> parseFactor(const string& re, int& pos, int& counter, NfaMap& nfa)
{
    pair<int,int> result = parseBase(re, pos, counter, nfa);
    while (pos < re.size() && re[pos] == '*')
    {
        pos++;
        result = makeStar(result, counter, nfa);
    }
    return result;
}

pair<int,int> parseBase(const string& re, int& pos, int& counter, NfaMap& nfa)
{
    char c = re[pos];
    if (c == '(') { pos++; auto r = parseExpr(re, pos, counter, nfa); pos++; return r; }
    if (c == '#') { pos++; return makeEmpty(counter, nfa); }
    if (c == '~') { pos++; return makeLambda(counter, nfa); }
    pos++;
    return makeSymbol(string(1, c), counter, nfa);
}
```

And `exercise5()` is where everything is initialised — clean local scope, nothing leaking out:

```cpp
void exercise5()
{
    freopen("re.inp","r",stdin);
    string re;
    cin>>re;
    fclose(stdin);

    int counter=0;       // state ID counter — local, passed by ref
    NfaMap nfa;          // all transitions — local, passed by ref
    int pos=0;           // parser position — local, passed by ref

    pair<int,int> result=parseExpr(re,pos,counter,nfa);
    int q0=result.first, qf=result.second;
    // ... print table ...
}
```

### Why Recursive Descent?

Each function handles exactly one level of precedence by calling the next-higher level first. `parseExpr` calls `parseTerm` (which handles `*` and concatenation) before dealing with `+`. This naturally gives `*` higher precedence than concatenation, and concatenation higher precedence than `+` — exactly what we want.

### Full Worked Example — `(a+b)*ab`

This is the classic NFA for "all strings over `{a,b}` that end in `ab`".

**Parse tree:**

```
concat
├── star
│   └── union
│       ├── symbol 'a'
│       └── symbol 'b'
├── symbol 'a'
└── symbol 'b'
```

**Construction steps, state by state:**

```
makeSymbol('a')      → q0 --a--> q1★
makeSymbol('b')      → q2 --b--> q3★
makeUnion(↑, ↑)      → q4 --λ--> q0, q4 --λ--> q2
                        q1 --λ--> q5, q3 --λ--> q5   [q5★ = union exit]
makeStar(union)      → q6 --λ--> q4  (enter union)
                        q6 --λ--> q7  (skip, accept ε)
                        q5 --λ--> q4  (loop back)
                        q5 --λ--> q7  (exit star)     [q7★ = star exit]
makeSymbol('a')      → q8 --a--> q9★
makeConcat(star, 'a')→ q7 --λ--> q8               [result: q6..q9]
makeSymbol('b')      → q10 --b--> q11★
makeConcat(↑, 'b')   → q9 --λ--> q10              [result: q6..q11★]
```

**Complete transition list:**

```
q6  --λ--> q4        enter the (a+b)* star
q6  --λ--> q7        exit star immediately (accept ε for the star part)
q4  --λ--> q0        enter 'a' branch of union
q4  --λ--> q2        enter 'b' branch of union
q0  --a--> q1
q1  --λ--> q5        exit union
q2  --b--> q3
q3  --λ--> q5        exit union
q5  --λ--> q4        loop: one more repetition of (a+b)
q5  --λ--> q7        done with the star part
q7  --λ--> q8        begin reading the suffix 'a'
q8  --a--> q9
q9  --λ--> q10       begin reading the suffix 'b'
q10 --b--> q11★      final state — string accepted
```

**Acceptance trace for `"bab"`:**
- Read `b`: q6 →λ→ q4 →λ→ q2 →b→ q3 →λ→ q5 →λ→ q4 (loop) ... then q5 →λ→ q7 (exit star)
- Read `a`: q7 →λ→ q8 →a→ q9
- Read `b`: q9 →λ→ q10 →b→ q11★ ✓ **Accepted**

---

# Part 7 — The C++ Implementation

## Program Structure

```
main()
  └─ asks: which exercise? (1-5)
       ├─ exercise1()  →  reads dfa.inp, simulates DFA
       ├─ exercise2()  →  reads nfa.inp, computes λ-closure and δ*
       ├─ exercise3()  →  reads nfa.inp, runs subset construction
       ├─ exercise4()  →  reads dfa.inp, runs mark() + reduce()
       └─ exercise5()  →  reads re.inp,  runs re2nfa parser + prints NFA
```

## Coding Style Conventions

| Convention | Example | Reason |
|-----------|---------|--------|
| `freopen` for file input | `freopen("dfa.inp","r",stdin)` | No manual typing during testing |
| VLA for the table | `string dfa[n][m]` | Size known only at runtime |
| `find` + `distance` | `auto it = find(...); int idx = distance(...)` | Convert iterator to index |
| `*` prefix in input | `*q2` | Marks final states directly in the table |
| Raw `for` loops | `for(int i=0; ...)` | Explicit, easy to trace by hand |

## Key Helper Functions

| Function | Used in | Purpose |
|----------|---------|---------|
| `parseCell(cell)` | Ex 2, 3 | Parse `{q1,q2}` string into `vector<string>` |
| `lambdaClosure(state,...)` | Ex 2, 3 | DFS over λ-edges from one state |
| `lambdaClosureSet(set,...)` | Ex 2, 3 | λ-closure for a whole set of states |
| `moveSet(states, col,...)` | Ex 2, 3 | Follow symbol `a` from a set of states |
| `setToLabel(set)` | Ex 3 | `{"q0","q1"}` → `"{q0,q1}"` (DFA state name) |
| `newState(counter)` | Ex 5 | Increments `counter` by ref and returns the new state ID |
| `makeEmpty(counter, nfa)` | Ex 5 | Build NFA for `#` — two isolated states, no transitions |
| `makeLambda(counter, nfa)` | Ex 5 | Build NFA for `~` — `q0 --~--> qf` |
| `makeSymbol(a, counter, nfa)` | Ex 5 | Build NFA for a single character `a` |
| `makeUnion(a, b, counter, nfa)` | Ex 5 | Combine two NFAs with `+` |
| `makeConcat(a, b, nfa)` | Ex 5 | Chain two NFAs for concatenation (no new states needed) |
| `makeStar(a, counter, nfa)` | Ex 5 | Wrap NFA with Kleene star |
| `parseExpr/Term/Factor/Base(re, pos, counter, nfa)` | Ex 5 | Recursive descent parser — all state passed by ref |

## Key Data Structures

| Structure | Exercise | What it stores |
|-----------|---------|----------------|
| `string dfa[n][m]` | 1, 4 | Transition table as 2D string array |
| `string nfa[n][100]` | 2, 3 | Same, fixed width for multi-state cells |
| `vector<string> fstate` | 1–4 | Names of final states |
| `vector<string> sigma` | 1–4 | Alphabet symbols |
| `vector<vector<bool>> dist` | 4 | Distinguishability table for `mark()` |
| `vector<int> group` | 4 | Equivalence class index per state |
| `map<string,vector<string>> dfaTable` | 3 | DFA label → list of transition targets |
| `map<string,set<string>> labelToSet` | 3 | DFA label → actual NFA state set |
| `int counter` (local in `exercise5`) | 5 | Passed by ref to `newState()` — hands out fresh state IDs |
| `NfaMap nfa` (local in `exercise5`) | 5 | `typedef map<int,map<string,set<int>>>` — all transitions built during parsing |
| `pair<int,int>` | 5 | Return type of every `make*` and `parse*` — `.first` = initial state, `.second` = final state |

---

# Part 8 — How to Use the Program

## Step 1 — Compile

```bash
g++ -std=c++17 -o Theoratical Theoratical.cpp
```

> [!warning] Compiler Note
> `string dfa[n][m]` is a **Variable Length Array** — a GCC extension. It compiles fine with `g++` but will fail on MSVC. Always use `g++` with `-std=c++17`.

## Step 2 — Prepare Input Files

### `dfa.inp` — Exercise 1 and 4

```
<rows> <cols>
NULL   sym1  sym2  ...
state  dest  dest  ...
*finalstate  dest  dest  ...
stringtocheck          ← only for Exercise 1
```

**Exercise 1 example** — DFA accepting strings ending in `ab`:

```
4 3
NULL a b
q0 q1 q0
q1 q1 q2
*q2 q1 q0
aab
```

**Exercise 4 example** — 6-state DFA to minimize:

```
7 3
NULL a b
q0 q1 q2
q1 q1 q3
q2 q1 q4
q3 q1 q5
*q4 q1 q5
*q5 q1 q5
```

### `nfa.inp` — Exercise 2 and 3

```
<rows> <cols>
NULL   sym1  ~             ← use ~ for the lambda column
state  {dest,...}  {dest,...}
*finalstate  ...
querystate  querysymbol    ← only for Exercise 2
```

**Example:**

```
4 3
NULL a ~
q0 {q0} {q1}
q1 {q1} {q2}
*q2 {q2} {}
q0 a
```

### `re.inp` — Exercise 5

One line: the regular expression.

```
(a+b)*ab
```

**Supported syntax:**

| Symbol | Meaning |
|--------|---------|
| `+` | union |
| `*` | Kleene star (postfix) |
| `( )` | grouping |
| `#` | empty language ∅ |
| `~` | lambda / ε |
| `a`–`z` | any single lowercase letter |

> [!note] Concatenation is implicit
> Just write `ab` for "a followed by b". No dot or operator needed between characters.

## Step 3 — Run

```bash
./Theoratical
Choose exercise (1-5): 5
```

## Expected Outputs

### Exercise 1

```
NULL a b
q0 q1 q0
q1 q1 q2
q2 q1 q0

The string to check: aab
Valid!
```

### Exercise 2

```
NFA table:
NULL    a       ~
q0      {q0}    {q1}
q1      {q1}    {q2}
q2      {q2}    {}

lambda-closure(q0): {q0,q1,q2}
delta*(q0, a): {q0,q1,q2}
```

### Exercise 3

```
=== DFA (converted from NFA) ===
State            a
->*{q0,q1,q2}   {q0,q1,q2}
```

### Exercise 4

```
Accessible states: q0 q1 q2 q3 q4 q5

Equivalence classes:
  Class 0: {q0,q1}
  Class 1: {q2,q3}
  Class 2: {q4,q5}

=== Minimized DFA ===
State       a        b
->q0,q1    q0,q1    q2,q3
  q2,q3    q0,q1    q4,q5
 *q4,q5    q0,q1    q4,q5
```

### Exercise 5 — input `(a+b)*ab`

```
Regular expression : (a+b)*ab
Initial state      : q6
Final state        : q11

=== NFA table (nfa.inp format) ===
13 4
NULL    a       b       ~
q6      {}      {}      {q4,q7}
q0      {q1}    {}      {}
q1      {}      {}      {q5}
q2      {}      {q3}    {}
q3      {}      {}      {q5}
q4      {}      {}      {q0,q2}
q5      {}      {}      {q4,q7}
q7      {}      {}      {q8}
q8      {q9}    {}      {}
q9      {}      {}      {q10}
q10     {}      {q11}   {}
*q11    {}      {}      {}

=== Transitions ===
  q6 --~--> q4
  q6 --~--> q7
  q0 --a--> q1
  q1 --~--> q5
  q2 --b--> q3
  q3 --~--> q5
  q4 --~--> q0
  q4 --~--> q2
  q5 --~--> q4
  q5 --~--> q7
  q7 --~--> q8
  q8 --a--> q9
  q9 --~--> q10
  q10 --b--> q11
```

---

## Full Summary Table

| Exercise | Slide | Algorithm | Input file | Output |
|----------|-------|-----------|------------|--------|
| 1 — DFA Acceptance | DFA | Simulate δ step by step | `dfa.inp` + string | `Valid!` / `Invalid` |
| 2 — NFA δ* | NFA | λ-closure (DFS) + move | `nfa.inp` + query | Closure and δ* sets |
| 3 — NFA→DFA | page 46 | Subset construction (worklist) | `nfa.inp` | Full DFA table |
| 4 — DFA Minimize | pages 59–64 | BFS + table-filling + reduce | `dfa.inp` | Equivalence classes + minimized DFA |
| 5 — RE→NFA | pages 17–19 | Recursive descent + Thompson construction | `re.inp` | NFA table + transition list |

> [!tip] The Full Pipeline
> You can chain all five exercises: write a regex in `re.inp` → run **Ex 5** to get an NFA → copy that output into `nfa.inp` → run **Ex 3** to get a DFA → copy into `dfa.inp` → run **Ex 4** to minimize → test a string with **Ex 1**. That is the complete path: **regex → NFA → DFA → minimized DFA → string test**.

> [!tip] Learning Path
> Work through in order: **Ex 1 → 2 → 3 → 4 → 5**. Each one builds on the previous. Once Ex 5 feels natural, try the full pipeline above end-to-end with a regex of your own.
