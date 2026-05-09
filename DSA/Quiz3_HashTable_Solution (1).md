---
tags: [dsa, hash-table, quiz, solution]
course: Data Structures and Algorithms
date: 2026-05-08
topic: Open Addressing — Linear Probing, Quadratic Probing, Double Hashing
---

# Quiz 3 — Hash Table Full Solution

## Problem Setup

> **m = 13**, hash function: $h(k) = k \bmod 13$
>
> Insert sequence: **40, 31, 53, 44, 66, 77, 17, 90, 30, 102**
>
> Collision resolution:
> - **Linear probing:** $h(k, i) = (h(k) + i) \bmod m$
> - **Quadratic probing:** $h(k, i) = (h(k) + 2i^2 + 1) \bmod m$ for $i \geq 1$; try $h(k)$ first ($i=0$)
> - **Double hashing:** $h(k, i) = (h(k) + i \cdot h_2(k)) \bmod m$, where $h_2(k) = 7 - (k \bmod 7)$

---

## Part (a) — Build the Hash Table

### Insertion Trace

| Key | $h(k)$ | $h_2(k)$ | Linear → slot (probes) | Quadratic → slot (probes) | Double → slot (probes) |
|-----|--------|----------|------------------------|---------------------------|------------------------|
| 40  | 1      | 2        | 1 (1)                  | 1 (1)                     | 1 (1)                  |
| 31  | 5      | 4        | 5 (1)                  | 5 (1)                     | 5 (1)                  |
| 53  | 1      | 3        | 2 (2)                  | 4 (2)                     | 4 (2)                  |
| 44  | 5      | 5        | 6 (2)                  | 8 (2)                     | 10 (2)                 |
| 66  | 1      | 4        | 3 (3)                  | 10 (3)                    | 9 (3)                  |
| 77  | 12     | 7        | 12 (1)                 | 12 (1)                    | 12 (1)                 |
| 17  | 4      | 4        | 4 (1)                  | 7 (2)                     | 8 (2)                  |
| 90  | 12     | 1        | 0 (2)                  | 2 (2)                     | 0 (2)                  |
| 30  | 4      | 5        | 7 (4)                  | 0 (3)                     | 6 (4)                  |
| 102 | 11     | 3        | 11 (1)                 | 11 (1)                    | 11 (1)                 |

### Quadratic Probing — Collision Details

For key **53** ($h=1$, occupied by 40):
$$i=1: (1 + 2(1)^2 + 1)\bmod 13 = 4 \checkmark$$

For key **44** ($h=5$, occupied by 31):
$$i=1: (5 + 2(1)^2 + 1)\bmod 13 = 8 \checkmark$$

For key **66** ($h=1$, occupied by 40):
$$i=1: (1+3)\bmod 13 = 4 \text{ (53 there)},\quad i=2: (1+9)\bmod 13 = 10 \checkmark$$

For key **17** ($h=4$, occupied by 53):
$$i=1: (4+3)\bmod 13 = 7 \checkmark$$

For key **90** ($h=12$, occupied by 77):
$$i=1: (12+3)\bmod 13 = 2 \checkmark$$

For key **30** ($h=4$, occupied by 53):
$$i=1: (4+3)=7 \text{ (17)},\quad i=2: (4+9)=0 \checkmark$$

### Double Hashing — Collision Details

For key **53** ($h=1$, $h_2=3$): slot $(1+1\cdot3)\bmod13=4\ \checkmark$

For key **44** ($h=5$, $h_2=5$): slot $(5+1\cdot5)\bmod13=10\ \checkmark$

For key **66** ($h=1$, $h_2=4$): i=1→5 (31), i=2→9 $\checkmark$

For key **17** ($h=4$, $h_2=4$): i=1→8 $\checkmark$

For key **90** ($h=12$, $h_2=1$): i=1→0 $\checkmark$

For key **30** ($h=4$, $h_2=5$): i=1→9 (66), i=2→14%13=1 (40), i=3→19%13=6 $\checkmark$

### Final Tables

| Index | Linear Probing | Quadratic Probing | Double Hashing |
|-------|---------------|-------------------|----------------|
| 0     | 90            | 30                | 90             |
| 1     | 40            | 40                | 40             |
| 2     | 53            | 90                | —              |
| 3     | 66            | —                 | —              |
| 4     | 17            | 53                | 53             |
| 5     | 31            | 31                | 31             |
| 6     | 44            | —                 | 30             |
| 7     | 30            | 17                | —              |
| 8     | —             | 44                | 17             |
| 9     | —             | —                 | 66             |
| 10    | —             | 66                | 44             |
| 11    | 102           | 102               | 102            |
| 12    | 77            | 77                | 77             |

---

## Part (b) — How many probes to **find 31**?

$h(31) = 31 \bmod 13 = 5$

| Method            | Probe sequence       | Probes |
|-------------------|----------------------|--------|
| Linear probing    | slot 5 → **31** ✓   | **1**  |
| Quadratic probing | slot 5 → **31** ✓   | **1**  |
| Double hashing    | slot 5 → **31** ✓   | **1**  |

> All three methods find 31 immediately at its home slot.

---

## Part (c) — How many probes to **find 17**?

$h(17) = 17 \bmod 13 = 4$, $h_2(17) = 7 - (17 \bmod 7) = 7 - 3 = 4$

**Linear probing:** slot 4 → **17** ✓ → **1 probe**

**Quadratic probing:**
- $i=0$: slot 4 → 53 ✗
- $i=1$: $(4 + 2 + 1)\bmod 13 = 7$ → **17** ✓ → **2 probes**

**Double hashing:**
- $i=0$: slot 4 → 53 ✗
- $i=1$: $(4 + 4)\bmod 13 = 8$ → **17** ✓ → **2 probes**

| Method            | Probes |
|-------------------|--------|
| Linear probing    | **1**  |
| Quadratic probing | **2**  |
| Double hashing    | **2**  |

---

## Part (d) — How many probes to **find 28**? (not in table)

$h(28) = 28 \bmod 13 = 2$, $h_2(28) = 7 - (28 \bmod 7) = 7 - 0 = 7$

Search terminates when a **None** (empty) slot is encountered → key not found.

**Linear probing:**

| $i$ | Slot | Value |
|-----|------|-------|
| 0   | 2    | 53    |
| 1   | 3    | 66    |
| 2   | 4    | 17    |
| 3   | 5    | 31    |
| 4   | 6    | 44    |
| 5   | 7    | 30    |
| 6   | 8    | **—** (None) |

→ **7 probes**

**Quadratic probing:**

| $i$ | Slot $(2 + 2i^2 + 1)\bmod 13$ | Value |
|-----|-------------------------------|-------|
| 0   | 2                             | 90    |
| 1   | 5                             | 31    |
| 2   | 11                            | 102   |
| 3   | $(2+19)\bmod 13=8$            | 44    |
| 4   | $(2+33)\bmod 13=9$            | **—** (None) |

→ **5 probes**

**Double hashing:**

| $i$ | Slot $(2 + i \cdot 7)\bmod 13$ | Value |
|-----|-------------------------------|-------|
| 0   | 2                             | **—** (None) |

→ **1 probe**

| Method            | Probes |
|-------------------|--------|
| Linear probing    | **7**  |
| Quadratic probing | **5**  |
| Double hashing    | **1**  |

---

## Part (e) — Remove {44, 77, 17}, then insert 43

Removed slots are marked **DEL** (tombstone). A tombstone is skipped during search but reusable during insertion.

- **Linear:** 44 @ slot 6, 77 @ slot 12, 17 @ slot 4 → all marked DEL
- **Quadratic:** 44 @ slot 8, 77 @ slot 12, 17 @ slot 7 → all marked DEL
- **Double:** 44 @ slot 10, 77 @ slot 12, 17 @ slot 8 → all marked DEL

### Tables after removing 44, 77, 17

| Index | Linear Probing | Quadratic Probing | Double Hashing |
|-------|---------------|-------------------|----------------|
| 0     | 90            | 30                | 90             |
| 1     | 40            | 40                | 40             |
| 2     | 53            | 90                | —              |
| 3     | 66            | —                 | —              |
| 4     | **DEL**       | 53                | 53             |
| 5     | 31            | 31                | 31             |
| 6     | **DEL**       | —                 | 30             |
| 7     | 30            | **DEL**           | —              |
| 8     | —             | **DEL**           | **DEL**        |
| 9     | —             | —                 | 66             |
| 10    | —             | 66                | **DEL**        |
| 11    | 102           | 102               | 102            |
| 12    | **DEL**       | **DEL**           | **DEL**        |

### Insert 43

$h(43) = 43 \bmod 13 = 4$, $h_2(43) = 7 - (43 \bmod 7) = 7 - 1 = 6$

**Linear probing:**

| $i$ | Slot | Value    |
|-----|------|----------|
| 0   | 4    | **DEL** → insert here |

→ **1 probe**, placed at slot **4**

**Quadratic probing:**

| $i$ | Slot | Value |
|-----|------|-------|
| 0   | 4    | 53    |
| 1   | $(4+3)\bmod 13=7$ | **DEL** → insert here |

→ **2 probes**, placed at slot **7**

**Double hashing:**

| $i$ | Slot $(4 + i \cdot 6)\bmod 13$ | Value |
|-----|-------------------------------|-------|
| 0   | 4                             | 53    |
| 1   | 10                            | **DEL** → insert here |

→ **2 probes**, placed at slot **10**

| Method            | Probes |
|-------------------|--------|
| Linear probing    | **1**  |
| Quadratic probing | **2**  |
| Double hashing    | **2**  |

---

## Part (f) — How many probes to **insert 56**?

> State of tables: after part (e) — i.e., after removals and insertion of 43.
> 43 now occupies: slot 4 (Linear), slot 7 (Quadratic), slot 10 (Double).

$h(56) = 56 \bmod 13 = 4$, $h_2(56) = 7 - (56 \bmod 7) = 7 - 0 = 7$

**Linear probing** (slot 4 = 43, slot 6 = DEL):

| $i$ | Slot | Value |
|-----|------|-------|
| 0   | 4    | 43    |
| 1   | 5    | 31    |
| 2   | 6    | **DEL** → insert here |

→ **3 probes**, placed at slot **6**

**Quadratic probing** (slot 7 = 43):

| $i$ | Slot | Value |
|-----|------|-------|
| 0   | 4    | 53    |
| 1   | 7    | 43    |
| 2   | $(4+9)\bmod 13=0$ | 30    |
| 3   | $(4+19)\bmod 13=10$ | 66  |
| 4   | $(4+33)\bmod 13=11$ | 102 |
| 5   | $(4+51)\bmod 13=3$  | **—** (None) → insert here |

→ **6 probes**, placed at slot **3**

**Double hashing** (slot 10 = 43):

| $i$ | Slot $(4 + i \cdot 7)\bmod 13$ | Value |
|-----|-------------------------------|-------|
| 0   | 4                             | 53    |
| 1   | 11                            | 102   |
| 2   | $(4+14)\bmod 13=5$            | 31    |
| 3   | $(4+21)\bmod 13=12$           | **DEL** → insert here |

→ **4 probes**, placed at slot **12**

| Method            | Probes |
|-------------------|--------|
| Linear probing    | **3**  |
| Quadratic probing | **6**  |
| Double hashing    | **4**  |

---

## Summary of All Answers

| Part | Question                            | Linear | Quadratic | Double |
|------|-------------------------------------|--------|-----------|--------|
| b    | Find 31                             | 1      | 1         | 1      |
| c    | Find 17                             | 1      | 2         | 2      |
| d    | Find 28 (not present)               | 7      | 5         | 1      |
| e    | Insert 43 (after removing 44,77,17) | 1      | 2         | 2      |
| f    | Insert 56 (after part e)            | 3      | 6         | 4      |
