# Finite Automata — A Complete Beginner's Guide
*From zero knowledge to a working C++ implementation*

---

## Table of Contents

- [[#Part 1 — What is a Finite Automaton?]]
- [[#Part 2 — Deterministic Finite Accepter (DFA)]]
- [[#Part 3 — Nondeterministic Finite Accepter (NFA)]]
- [[#Part 4 — Converting NFA to DFA]]
- [[#Part 5 — Minimizing a DFA]]
- [[#Part 6 — The C++ Implementation]]
- [[#Part 7 — How to Use the Program]]

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

```
        a           b
  ┌──────────►[q1]──────────►((q2))
  │            │                │
  │      a     │          a     │ b
  │      └─────┘          ┌─────┘
[q0]◄───────────────────────────────
  │
  └──► b ──► [q0]   (b loops back to start)
```

More clearly as a table (called a **transition table**):

| State | `a` | `b` |
|-------|-----|-----|
| `→q0` (initial) | `q1` | `q0` |
| `q1` | `q1` | `q2` |
| `q2` ★ (final) | `q1` | `q0` |

**Reading `"aab"`:**

```
Start:   currentState = q0
Read 'a': δ(q0, a) = q1  →  currentState = q1
Read 'a': δ(q1, a) = q1  →  currentState = q1
Read 'b': δ(q1, b) = q2  →  currentState = q2
End: q2 is a final state → ACCEPTED ✓
```

**Reading `"ba"`:**

```
Start:   currentState = q0
Read 'b': δ(q0, b) = q0  →  currentState = q0
Read 'a': δ(q0, a) = q1  →  currentState = q1
End: q1 is NOT a final state → REJECTED ✗
```

## The Transition Function δ

The rule `δ(q, a) = p` means:

> "If I am currently in state `q` and I read character `a`, I move to state `p`."

This is the heart of any DFA. In code, the transition table is stored as a 2D array where rows are states and columns are alphabet symbols.

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
     Otherwise             → "Invalid"
```

### The Code

```cpp
void exercise1()
{
    freopen("dfa.inp", "r", stdin);
    int n, m;
    cin >> n >> m;
    string dfa[n][m];          // the full table (n rows, m columns)
    vector<string> fstate;     // list of final states
    vector<string> sigma;      // list of alphabet symbols

    // Read the table, detect final states (marked with '*')
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
        {
            cin >> dfa[i][j];
            if (dfa[i][j][0] == '*')
            {
                dfa[i][j].erase(0, 1);          // remove the '*'
                fstate.push_back(dfa[i][j]);    // remember it's final
            }
        }

    // Row 0 is the header; columns 1..m-1 are the alphabet symbols
    for (int i = 1; i < m; ++i)
        sigma.push_back(dfa[0][i]);

    cin >> s;
    string currentState = dfa[1][0];   // initial state = first data row

    for (int i = 0; i < s.length(); ++i)
    {
        // Which column does s[i] belong to?
        auto it = find(begin(sigma), end(sigma), string(1, s[i]));
        int index = distance(sigma.begin(), it) + 1;

        if (index == m)   // not found in alphabet
        {
            cout << "\nInvalid!";
            return;
        }

        // Find the row for currentState and move
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
Instead of typing input in the terminal every time, this redirects `cin` to read from the file `dfa.inp`. Every `cin >>` after this reads from the file automatically.

**`string dfa[n][m]`**
A 2D array of strings. Row 0 is the header (`NULL a b ...`). Rows 1 to n-1 are the actual states. Column 0 is the state name, columns 1 onwards are transition destinations.

**`if (dfa[i][j][0] == '*')`**
The `[0]` gets the first character of the string. If it's `*`, this state is final. We strip the `*` with `erase(0, 1)` so the name is clean.

**`find(...) + distance(...)`**
`find` returns an iterator pointing to where `s[i]` is in `sigma`. `distance` converts that iterator to an index number. We add `1` because column 0 is the state name, not a symbol column.

**`index == m`**
If `find` reaches the end of `sigma` without finding the character, `distance` returns `sigma.size()`, and `+1` makes it equal to `m` (number of columns). That means the character is not in the alphabet — reject.

---

# Part 3 — Nondeterministic Finite Accepter (NFA)

## What Makes It "Nondeterministic"?

In an NFA, a state can have:
- **Zero** transitions for some input (no rule for that character)
- **Multiple** transitions for the same input (go to several states at once)
- **Lambda (λ) transitions** — also called **epsilon (ε) transitions** — moves to another state **without reading any character**

> [!tip] Intuition
> Think of an NFA as a machine that can **split into parallel copies** of itself. When there are multiple possible transitions, the machine explores all of them simultaneously. If **any one** of the parallel copies ends up in a final state, the string is accepted.

## Lambda (λ) Transitions

A λ-transition lets the machine jump to another state for free — without consuming any input character. This makes NFAs much easier to design, even though they are harder to simulate directly.

**Example:** An NFA where `q0` has a λ-transition to `q1`:

```
q0 --λ--> q1 --a--> q2 (final)
```

Even before reading any input, the machine is already "in both `q0` and `q1`" at the same time.

## The λ-closure

The **λ-closure** of a state `q` is the set of all states reachable from `q` using **only λ-transitions** (zero or more of them), including `q` itself.

**Example:**

```
q0 --λ--> q1 --λ--> q2
q2 --λ--> q3
```

```
λ-closure(q0) = {q0, q1, q2, q3}
λ-closure(q1) = {q1, q2, q3}
λ-closure(q2) = {q2, q3}
λ-closure(q3) = {q3}
```

The algorithm is a simple **BFS or DFS** starting from `q` and only following λ-edges.

## The Extended Transition Function δ*

Since an NFA can be in many states at once, we need a function that works on **sets** of states.

`δ*(q, a)` answers: "starting from state `q`, after reading character `a`, which states can I possibly be in?"

The formula from the slide is:

```
δ*(q, a) = λ-closure( move( λ-closure(q), a ) )
```

Breaking it down step by step:

| Step | Operation | What it does |
|------|-----------|-------------|
| 1 | `λ-closure(q)` | Find all states reachable from `q` via λ-transitions |
| 2 | `move(T, a)` | From each state in set `T`, follow the `a`-transition (no λ) |
| 3 | `λ-closure(result)` | From wherever we landed, follow any λ-transitions again |

## Exercise 2 — Computing λ-closure and δ*

**The task:** Read an NFA from a file, then for a given starting state `q` and symbol `a`, compute and print `λ-closure(q)` and `δ*(q, a)`.

### The NFA Table Format

Because NFA cells can hold **multiple states**, each cell is written as `{q1,q2}` or `{}` for empty. The λ-column is marked with `~` in the header.

**Example `nfa.inp`:**

```
4 3
NULL  a    ~
q0   {q0}  {q1}
q1   {q1}  {q2}
*q2  {q2}  {}
q0 a
```

This NFA has: `q0` reads `a` → stays at `q0`; `q0` has λ → `q1`; `q1` has λ → `q2`; `q2` is final.

### `parseCell()` — Reading Multi-State Cells

```cpp
vector<string> parseCell(string cell)
{
    // Remove '{' and '}'
    cell.erase(remove(cell.begin(), cell.end(), '{'), cell.end());
    cell.erase(remove(cell.begin(), cell.end(), '}'), cell.end());
    // Split by ','
    vector<string> res;
    stringstream ss(cell);
    string tok;
    while (getline(ss, tok, ','))
        if (!tok.empty()) res.push_back(tok);
    return res;
}
```

`remove` moves all `{` characters to the end of the string; `erase` then cuts them off. Then `stringstream` + `getline` splits the remaining text by commas — the standard C++ way to split a string.

### `lambdaClosure()` — BFS Over λ-Edges

```cpp
set<string> lambdaClosure(const string& state, int n, int m,
                           string nfa[][100], int lambdaCol)
{
    set<string> closure;
    stack<string> stk;
    stk.push(state);
    closure.insert(state);      // a state is always in its own closure

    while (!stk.empty())
    {
        string cur = stk.top(); stk.pop();

        // Find the row for 'cur' in the table
        for (int i = 1; i < n; ++i)
            if (nfa[i][0] == cur)
            {
                // Read the λ-column for this state
                vector<string> nexts = parseCell(nfa[i][lambdaCol]);
                for (auto& nx : nexts)
                    if (!closure.count(nx))   // not visited yet
                    {
                        closure.insert(nx);
                        stk.push(nx);         // explore from nx next
                    }
                break;
            }
    }
    return closure;
}
```

This is a standard **depth-first search**:
- Push the starting state onto a stack
- Pop a state, look at all its λ-transitions, push any unvisited ones
- Stop when the stack is empty (no more new states reachable via λ)

### Computing δ*(q, a)

```cpp
// Step 1: lambda-closure of the query state
set<string> lc = lambdaClosure(q0, n, m, nfa, lambdaCol);

// Step 2: move — for each state in lc, follow symbol 'a'
set<string> mv = moveSet(lc, col, n, nfa);

// Step 3: lambda-closure of the result
set<string> ds = lambdaClosureSet(mv, n, m, nfa, lambdaCol);
```

### Trace for the Example

Query: `q0 a`

```
Step 1 — λ-closure(q0):
  Start: {q0}
  q0 has λ → q1 → add q1: {q0, q1}
  q1 has λ → q2 → add q2: {q0, q1, q2}
  q2 has no λ-transitions
  Result: {q0, q1, q2}

Step 2 — move({q0, q1, q2}, a):
  q0 on a → {q0}
  q1 on a → {q1}
  q2 on a → {q2}
  Result: {q0, q1, q2}

Step 3 — λ-closure({q0, q1, q2}):
  Same as step 1: {q0, q1, q2}

δ*(q0, a) = {q0, q1, q2}
```

---

# Part 4 — Converting NFA to DFA

## Why Convert?

NFAs are easy to design but hard to run directly (you'd have to track all parallel states). DFAs are easy to run. The **subset construction** algorithm converts any NFA into an equivalent DFA that accepts exactly the same strings.

## The Key Insight

Each **DFA state** will represent a **set of NFA states** — specifically, all the NFA states the machine could possibly be in at that point.

> [!example] Analogy
> Imagine watching 10 different movies at once, each on a different TV. The "state" of your viewing session is the tuple of which scene each movie is on. When you press a button (read a character), all TVs advance according to their own rules. The subset construction turns this "all TVs at once" view into a single new machine.

## The Algorithm (page 46)

```
1. Create the initial DFA state = λ-closure(q0 of NFA)
2. Repeat until no DFA state has a missing transition:
   3. Take any DFA state S = {qi, qj, ..., qk} that has
      no outgoing edge for some symbol a
   4. Compute the target:
      δ_N*({qi, qj, ..., qk}, a) = λ-closure(move({qi,...,qk}, a))
   5. If this target set is new, create a new DFA state for it
   6. Add an edge from S to the target, labeled a
7. Any DFA state that contains a final NFA state → mark as final
```

## Exercise 3 — nfa2dfa

**The task:** Read an NFA, apply the subset construction, and print the resulting DFA table.

### The Worklist Approach

Instead of "take any state with a missing edge", we use a **queue** (called a worklist). New DFA states are added to the queue as they are discovered, and we process them one by one until the queue is empty.

```cpp
void exercise3()
{
    // ... read NFA table same as exercise 2 ...

    // Represent each DFA state as a string like "{q0,q1,q2}"
    auto setToLabel = [](const set<string>& s) -> string { ... };

    // Initial DFA state = λ-closure(NFA initial state)
    set<string> init = lambdaClosure(nfa[1][0], ...);
    string initLabel = setToLabel(init);

    map<string, vector<string>> dfaTable;   // label → list of transitions
    map<string, set<string>> labelToSet;    // label → actual set of NFA states
    queue<string> worklist;

    labelToSet[initLabel] = init;
    worklist.push(initLabel);

    while (!worklist.empty())
    {
        string curLabel = worklist.front(); worklist.pop();
        set<string>& cur = labelToSet[curLabel];

        for each symbol in sigma:
        {
            // Compute δ*(curSet, symbol)
            set<string> mv   = moveSet(cur, col, ...);
            set<string> next = lambdaClosureSet(mv, ...);
            string nextLabel = setToLabel(next);

            dfaTable[curLabel].push_back(nextLabel);

            // If this is a brand new DFA state, add it to the queue
            if (!next.empty() && !dfaTable.count(nextLabel))
            {
                labelToSet[nextLabel] = next;
                worklist.push(nextLabel);
            }
        }
    }
}
```

### Detecting Final States

A DFA state (which is a set of NFA states) is **final** if it contains **at least one** NFA final state:

```cpp
for (auto& fs : nfaFinal)
    if (st.count(fs)) { prefix += "*"; break; }
```

### Example

NFA with states `{q0, q1, q2}`, λ-transitions from `q0→q1→q2`, symbol `a` loops each state to itself:

```
DFA state       on 'a'
→*{q0,q1,q2}   {q0,q1,q2}    ← loops to itself
```

Because the λ-closure of `q0` immediately reaches all states (including final `q2`), the single DFA state is both initial and final, and it loops on `a`.

---

# Part 5 — Minimizing a DFA

## Why Minimize?

A DFA produced by the subset construction can have many redundant states — states that behave identically. **Minimization** merges these redundant states to produce the **smallest possible DFA** that accepts the same language.

## The Concept of Distinguishable States

Two states `p` and `q` are **distinguishable** if there exists some string `w` such that:
- Starting from `p`, reading `w` → ends in a final state
- Starting from `q`, reading `w` → does NOT end in a final state (or vice versa)

If no such `w` exists, `p` and `q` are **indistinguishable** — they behave identically for all inputs — and can be safely merged.

## The Three Phases

### Phase 1 — Remove Inaccessible States

A state is **inaccessible** if there is no path to it from the initial state `q0`. Such states can never be reached during any computation, so they are useless.

We find all accessible states using **BFS from q0**:

```
Accessible = {q0}
Queue = [q0]

While queue is not empty:
    cur = dequeue
    For each transition δ(cur, a) = dest:
        If dest not in Accessible:
            Add dest to Accessible
            Enqueue dest
```

Only the states in `Accessible` are kept.

### Phase 2 — The `mark()` Algorithm (Table-Filling)

This is the core of minimization. We fill a **triangular table** of all state pairs `(p, q)` where `p < q`. Each cell records whether the pair is **distinguishable**.

#### Step 1 — Base Case (obvious distinguishable pairs)

Mark every pair `(p, q)` where **one is final and the other is not**. We can distinguish them with the empty string `ε` — the final one accepts ε, the non-final one does not.

```
For all pairs (p, q):
    if (p ∈ F and q ∉ F) or (p ∉ F and q ∈ F):
        mark (p, q) as DISTINGUISHABLE
```

#### Step 2 — Propagation (inductive step)

Now we propagate: if reading symbol `a` from `p` and `q` leads to a pair that is already distinguishable, then `p` and `q` are distinguishable too.

```
Repeat until no new pairs are marked:
    For each UNMARKED pair (p, q):
        For each symbol a in Σ:
            Let pa = δ(p, a)
            Let qa = δ(q, a)
            If pa ≠ qa and (pa, qa) is already MARKED:
                Mark (p, q) as DISTINGUISHABLE
                Break
```

> [!example] Why this works
> If `δ(p, a)` and `δ(q, a)` are distinguishable by some string `w`, then `p` and `q` are distinguishable by the string `aw` — just prepend `a` to the distinguishing string.

#### Step 3 — Group Unmarked Pairs

After the loop, any pair `(p, q)` that was **never marked** is indistinguishable. Group all mutually indistinguishable states together — these become the **equivalence classes**.

```cpp
vector<int> group(ns, -1);
int numGroups = 0;

for (int i = 0; i < ns; ++i)
{
    if (group[i] != -1) continue;      // already assigned
    group[i] = numGroups++;            // new class
    for (int j = i+1; j < ns; ++j)
        if (!dist[i][j])               // i and j are indistinguishable
            group[j] = group[i];       // put j in the same class as i
}
```

### Phase 3 — The `reduce()` Algorithm (Building M̂)

Now we build the **minimized DFA M̂** from the equivalence classes:

| Component | How to build it |
|-----------|----------------|
| **States** | One state per equivalence class |
| **Initial state** | The class that contains the original `q0` |
| **Final states** | Any class that contains at least one original final state |
| **Transitions** | Pick any representative from each class; its transitions define the class's transitions |

The representative's transition `δ(rep, a) = dest` becomes `δ̂(class_of_rep, a) = class_of_dest`.

This works because all states in a class are indistinguishable — they all go to the same class on each symbol (otherwise they would have been marked as distinguishable!).

## Exercise 4 — Putting It Together

**The task:** Read a DFA, remove inaccessible states, run `mark()`, group states into equivalence classes, then run `reduce()` and print the minimized DFA.

### Full Worked Example

**Original DFA** (6 states, alphabet `{a, b}`):

| State | `a` | `b` |
|-------|-----|-----|
| `→q0` | `q1` | `q2` |
| `q1` | `q1` | `q3` |
| `q2` | `q1` | `q4` ★ |
| `q3` | `q1` | `q5` |
| `q4` ★ | `q1` | `q5` |
| `q5` | `q1` | `q5` |

All 6 states are accessible (BFS from q0 reaches all). Final states: `{q4}`.

Wait — let's use the example from the code where `{q4, q5}` are both marked as final, making 3 classes emerge:

| State | `a` | `b` | Final? |
|-------|-----|-----|--------|
| `→q0` | `q1` | `q2` | No |
| `q1` | `q1` | `q3` | No |
| `q2` | `q1` | `q4` | No |
| `q3` | `q1` | `q5` | No |
| `q4` ★ | `q1` | `q5` | **Yes** |
| `q5` ★ | `q1` | `q5` | **Yes** |

**Step 1 — Base case marking:**
Final states: `{q4, q5}`. Non-final: `{q0, q1, q2, q3}`.
Mark all pairs with one final and one non-final:
`(q0,q4)`, `(q0,q5)`, `(q1,q4)`, `(q1,q5)`, `(q2,q4)`, `(q2,q5)`, `(q3,q4)`, `(q3,q5)` → all **MARKED**

**Step 2 — Propagation:**

Check `(q0, q1)`:
- on `a`: δ(q0,a)=q1, δ(q1,a)=q1 → same, no info
- on `b`: δ(q0,b)=q2, δ(q1,b)=q3 → is `(q2,q3)` marked? Not yet.

Check `(q2, q3)`:
- on `a`: δ(q2,a)=q1, δ(q3,a)=q1 → same
- on `b`: δ(q2,b)=q4, δ(q3,b)=q5 → is `(q4,q5)` marked? `q4` and `q5` are BOTH final → **NOT marked**.

Check `(q4, q5)`:
- on `a`: δ(q4,a)=q1, δ(q5,a)=q1 → same
- on `b`: δ(q4,b)=q5, δ(q5,b)=q5 → same
→ `(q4,q5)` stays **UNMARKED** ✓

Back to `(q2, q3)`: `(q4,q5)` not marked → `(q2,q3)` stays **UNMARKED** ✓
Back to `(q0, q1)`: `(q2,q3)` not marked → `(q0,q1)` stays **UNMARKED** ✓

**Step 3 — Equivalence classes:**

```
Class 0: {q0, q1}   ← never marked as distinguishable
Class 1: {q2, q3}   ← never marked
Class 2: {q4, q5}   ← never marked (both final)
```

**Step 4 — Minimized DFA:**

Using `q0` as rep for Class 0, `q2` for Class 1, `q4` for Class 2:

| State | `a` | `b` |
|-------|-----|-----|
| `→q0,q1` | `q0,q1` | `q2,q3` |
| `q2,q3` | `q0,q1` | `q4,q5` |
| `q4,q5` ★ | `q0,q1` | `q4,q5` |

**6 states → 3 states** ✓

---

# Part 6 — The C++ Implementation

## Program Structure

```
main()
  └─ asks: which exercise? (1-4)
       ├─ exercise1()  →  reads dfa.inp, simulates DFA
       ├─ exercise2()  →  reads nfa.inp, computes λ-closure and δ*
       ├─ exercise3()  →  reads nfa.inp, runs subset construction
       └─ exercise4()  →  reads dfa.inp, runs mark() + reduce()
```

## Coding Style Conventions

This code follows a consistent style throughout:

| Convention | Example | Reason |
|-----------|---------|--------|
| `freopen` for file input | `freopen("dfa.inp","r",stdin)` | No manual typing during testing |
| VLA for the table | `string dfa[n][m]` | Size read at runtime from file |
| `find` + `distance` | `auto it = find(...); int idx = distance(...)` | Convert iterator to index |
| `*` prefix in input | `*q2` | Marks final states directly in the table |
| Raw loops everywhere | `for(int i=0; ...)` | Explicit, easy to trace |

## Key Helper Functions

### `parseCell(string cell)` — used in Ex 2, 3

Converts `"{q1,q2}"` into a `vector<string> {"q1","q2"}`.

```
Input:  "{q1,q2,q3}"
After remove '{' '}':  "q1,q2,q3"
After split by ',':    ["q1", "q2", "q3"]
```

### `lambdaClosure(state, ...)` — used in Ex 2, 3

DFS from `state` following only λ-column transitions. Returns `set<string>` of all reachable states.

### `lambdaClosureSet(set, ...)` — used in Ex 2, 3

Calls `lambdaClosure` for each state in the set and unions all results.

### `moveSet(states, col, ...)` — used in Ex 2, 3

For each state in `states`, reads column `col` from the NFA table, collects all destination states (parsing multi-state cells).

### `setToLabel(set)` — used in Ex 3

Converts `{"q0","q1","q2"}` to the string `"{q0,q1,q2}"` — used as the DFA state name.

## Data Structures Explained

### `map<string, vector<string>> dfaTable` (Ex 3)

Maps each DFA state label to its list of transition targets (one per alphabet symbol). Using `map` instead of an array because DFA states are strings like `"{q0,q1}"`, not integers.

### `map<string, set<string>> labelToSet` (Ex 3)

Maps each DFA state label back to the actual set of NFA states it represents. Needed to compute further transitions.

### `vector<vector<bool>> dist` (Ex 4)

The distinguishability table. `dist[i][j] = true` means states at positions `i` and `j` in the accessible-rows list are distinguishable.

### `vector<int> group` (Ex 4)

`group[i]` = which equivalence class state `i` belongs to. Built by scanning the `dist` table.

---

# Part 7 — How to Use the Program

## Step 1 — Compile

```bash
g++ -std=c++17 -o Theoratical Theoratical.cpp
```

> [!warning] Compiler Note
> The code uses **Variable Length Arrays** (`string dfa[n][m]`) which is a GCC extension. It compiles fine with `g++` but may fail on MSVC (Visual Studio). Always use `g++` with `-std=c++17`.

## Step 2 — Prepare Input Files

### For Exercise 1 and 4 — `dfa.inp`

```
<rows> <cols>
NULL  a  b  ...
state  dest  dest  ...
*finalstate  dest  dest  ...
stringtocheck
```

**Concrete example** (Ex 1 — DFA for strings ending in `ab`):

```
4 3
NULL a b
q0 q1 q0
q1 q1 q2
*q2 q1 q0
aab
```

**Concrete example** (Ex 4 — 6-state DFA to minimize):

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

*(No string needed for Ex 4 — just omit it or the program won't ask for it)*

### For Exercise 2 and 3 — `nfa.inp`

```
<rows> <cols>
NULL  a  ~  ...       ← use ~ for lambda column
state  {dest,...}  {dest,...}  ...
*finalstate  ...
querystate querysymbol    ← only for Ex 2
```

**Concrete example:**

```
4 3
NULL a ~
q0 {q0} {q1}
q1 {q1} {q2}
*q2 {q2} {}
q0 a
```

## Step 3 — Run

```bash
./Theoratical
Choose exercise (1-4): 1
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
State           a
->*{q0,q1,q2}  {q0,q1,q2}
```

### Exercise 4

```
Accessible states: q0 q1 q2 q3 q4 q5

Equivalence classes:
  Class 0: {q0,q1}
  Class 1: {q2,q3}
  Class 2: {q4,q5}

=== Minimized DFA ===
State       a         b
->q0,q1    q0,q1     q2,q3
  q2,q3    q0,q1     q4,q5
 *q4,q5    q0,q1     q4,q5
```

---

## Summary

| Exercise | Algorithm | Input | Output |
|----------|-----------|-------|--------|
| 1 — DFA Acceptance | Simulate δ step by step | `dfa.inp` + string | Valid / Invalid |
| 2 — NFA δ* | λ-closure (BFS) + move | `nfa.inp` + query | Closure and δ* sets |
| 3 — NFA→DFA | Subset construction (worklist) | `nfa.inp` | Full DFA table |
| 4 — DFA Minimize | BFS + table-filling + reduce | `dfa.inp` | Equivalence classes + minimized DFA |

> [!tip] Learning Path
> If this is your first time with automata: read Parts 1 and 2 first, run Exercise 1 with your own `dfa.inp`, and trace through the output manually. Once that clicks, move to Part 3 and Exercise 2. The NFA concepts build directly on the DFA ones.
