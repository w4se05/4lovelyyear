---
tags: [DSA, linked-lists, cheatsheet, quiz-prep]
topic: "Lecture 6: Linked Lists — COMPLETE QUIZ CHEATSHEET"
course: "61CSE108 Algorithms and Data Structures"
---
## 0. The Core Mental Model — Before Anything Else

### What is a linked list, really?

Imagine a **treasure hunt**: each clue tells you where the next clue is hidden. You cannot jump to clue 5 without following clues 1→2→3→4 first. That is a linked list.

An **array** is like a row of numbered lockers — you can go directly to locker 5. A **linked list** is like that treasure hunt — you must follow the chain.

### The two things inside every node

```
┌─────────┬──────────┐
│  Info   │  pNext   │
│ (data)  │ (address)│
└─────────┴──────────┘
```

- `Info` — the actual value stored (an int, a struct, anything)
- `pNext` — the **memory address** of the next node (`NULL` if this is the last node)

### The two things that describe the whole list

- `pHead` — address of the **first** node (entry point — you always start here)
- `pTail` — address of the **last** node (useful for fast append)

### What NULL means

`NULL` means "nothing is here". The last node has `pNext = NULL` — there is no next node. An empty list has `pHead = NULL` and `pTail = NULL`.

---

## 1. C++ Struct Definitions — Memorize These

### Singly Linked List (SLL) — the main focus of this lecture

```cpp
typedef struct tagNode {
    Data Info;              // the stored value
    struct tagNode *pNext;  // pointer to the NEXT node (or NULL)
} NODE;

typedef struct tagList {
    NODE *pHead;   // pointer to the FIRST node
    NODE *pTail;   // pointer to the LAST node
} LIST;
```

### Doubly Linked List (DLL)

```cpp
typedef struct tagDNode {
    Data Info;
    struct tagDNode *pNext;  // forward pointer
    struct tagDNode *pPrev;  // backward pointer
} DNODE;
// List struct same shape: pHead and pTail
```

### Circular Singly Linked List (CSLL)

```cpp
// Same node as SLL, but after building the list:
pTail->pNext = pHead;   // last node loops back to first
```

### Circular Doubly Linked List (CDLL)

```cpp
// Same node as DLL, but after building:
pTail->pNext = pHead;
pHead->pPrev = pTail;
```

---

## 2. The Four Types — Visual Reference

### Singly Linked List

```
pHead                              pTail
  │                                  │
  ▼                                  ▼
┌───┬──┐   ┌───┬──┐   ┌───┬──┐   ┌───┬────┐
│ A │ ─┼──►│ B │ ─┼──►│ C │ ─┼──►│ D │NULL│
└───┴──┘   └───┴──┘   └───┴──┘   └───┴────┘
```

### Doubly Linked List

```
pHead                                         pTail
  │                                              │
  ▼                                              ▼
┌────┬───┬────┐    ┌────┬───┬────┐    ┌────┬───┬────┐
│NULL│ A │ ──►│◄──►│ ──│ B │ ──►│◄──►│ ──│ C │NULL│
└────┴───┴────┘    └────┴───┴────┘    └────┴───┴────┘
```

### Circular Singly Linked List

```
pHead                         pTail
  │                             │
  ▼                             ▼
┌───┬──┐   ┌───┬──┐   ┌───┬──┐   ┌───┬──┐
│ A │ ─┼──►│ B │ ─┼──►│ C │ ─┼──►│ D │ ─┼──┐
└───┴──┘   └───┴──┘   └───┴──┘   └───┴──┘  │
  ▲                                          │
  └──────────────────────────────────────────┘
         pTail->pNext = pHead
```

### Circular Doubly Linked List

```
     ┌─────────────────────────────────────┐
     │                                     │
     ▼                                     │
┌────┬───┬────┐    ┌────┬───┬────┐    ┌────┬───┬────┐
│ ──►│ A │ ──►│◄──►│ ──│ B │ ──►│◄──►│ ──│ C │ ──►│
└────┴───┴────┘    └────┴───┴────┘    └────┴───┴────┘
  ▲                                              │
  └──────────────────────────────────────────────┘
  pTail->pNext = pHead  AND  pHead->pPrev = pTail
```

---

## 3. Array vs Linked List — The Big Picture Table

| Question | Array | Linked List |
|---|---|---|
| Access element by index | $O(1)$ ✅ | $O(n)$ ❌ (must walk) |
| Insert / Delete (known position) | $O(n)$ ❌ (must shift) | $O(1)$ ✅ (rewire pointers) |
| Memory layout | Contiguous block | Scattered anywhere |
| Size fixed? | Yes (pre-allocated) | No (grows/shrinks freely) |
| Extra memory per element | None | One pointer per node |
| Best sort algorithm | QuickSort, MergeSort | MergeSort, QuickSort |
| Implementation difficulty | Easier | Harder (pointers) |
| Good for | Static data, frequent lookup | Dynamic data, frequent insert/delete |

---

## 4. Every Operation — Code + Diagram + Line-by-Line Explanation

### 4.1 Initialize an Empty List

```cpp
void Init(LIST &l) {
    l.pHead = l.pTail = NULL;
    //  ↑ Both pointers set to NULL = "no nodes exist"
}
```

**Memory state after Init:**
```
l.pHead ──► NULL
l.pTail ──► NULL
```

**Check if empty:**
```cpp
bool isEmpty(LIST &l) {
    return l.pHead == NULL;
    // true  → list has no nodes
    // false → list has at least one node
}
```

---

### 4.2 Create a New Node — GetNode

```cpp
NODE* GetNode(Data x) {
    NODE *p = new NODE;       // allocate memory on the heap
    if (p == NULL) {          // allocation failed (out of memory)
        cout << "Not enough memory" << endl;
        return NULL;
    }
    p->Info = x;              // store the data value
    p->pNext = NULL;          // this node points to nothing yet
    return p;                 // hand back the address of the new node
}
```

**What it produces:**
```
After: NODE* p = GetNode(42);

p ──► ┌────┬──────┐
      │ 42 │ NULL │
      └────┴──────┘
```

> [!Warning] ⚠️ Always check if GetNode returns NULL before using the pointer. If memory is full, it returns NULL and you must not dereference it.

---

### 4.3 Add at the Head — AddFirst / InsertHead

**What we want:** new node becomes the new first element.

```cpp
void AddFirst(LIST &l, NODE* new_e) {
    if (l.pHead == NULL) {          // CASE 1: list is empty
        l.pHead = l.pTail = new_e;  // new node is both head and tail
    } else {                        // CASE 2: list has nodes
        new_e->pNext = l.pHead;     // step A: new node points to old head
        l.pHead = new_e;            // step B: head now points to new node
    }
}

NODE* InsertHead(LIST &l, Data x) {
    NODE* new_e = GetNode(x);
    if (new_e == NULL) return NULL;
    AddFirst(l, new_e);
    return new_e;
}
```

**Case 1 — Empty list, inserting X:**
```
Before:  pHead──►NULL   pTail──►NULL

After:   pHead──►┌───┬────┐◄──pTail
                 │ X │NULL│
                 └───┴────┘
```

**Case 2 — Non-empty list [A→B→C], inserting X at head:**
```
Before:
pHead──►[A]──►[B]──►[C]──►NULL
                           ▲
                         pTail

Step A: new_e->pNext = pHead   →   [X]──►[A]──►[B]──►[C]──►NULL
Step B: pHead = new_e          →   pHead──►[X]──►[A]──►[B]──►[C]──►NULL
                                                               ▲
                                                             pTail
```

> [!Warning] ⚠️ Order matters! You MUST do Step A (new_e->pNext = l.pHead) BEFORE Step B (l.pHead = new_e). If you do B first, you lose the reference to the old list.

---

### 4.4 Add at the Tail — AddTail / InsertTail

**What we want:** new node becomes the new last element.

```cpp
void AddTail(LIST &l, NODE* new_e) {
    if (l.pHead == NULL) {           // CASE 1: empty list
        l.pHead = l.pTail = new_e;
    } else {                         // CASE 2: non-empty
        l.pTail->pNext = new_e;      // step A: old tail links forward to new node
        l.pTail = new_e;             // step B: tail pointer advances to new node
    }
}
```

**Case 2 — Non-empty list [A→B→C], appending X:**
```
Before:
pHead──►[A]──►[B]──►[C]──►NULL
                      ▲
                    pTail

Step A: pTail->pNext = new_e  →  [C]──►[X]──►NULL
Step B: pTail = new_e         →  pTail──►[X]──►NULL

After:
pHead──►[A]──►[B]──►[C]──►[X]──►NULL
                               ▲
                             pTail
```

> [!Warning] ⚠️ Step A BEFORE Step B. Also: new_e->pNext must already be NULL (GetNode sets this).

---

### 4.5 Insert After Node q — AddAfter

**What we want:** insert `new_e` immediately after the existing node `q`.

```cpp
void AddAfter(LIST &l, NODE *q, NODE* new_e) {
    if (q != NULL) {
        new_e->pNext = q->pNext;   // step A: new node takes q's old successor
        q->pNext = new_e;          // step B: q now points to new node
        if (q == l.pTail)          // step C: if q was the tail,
            l.pTail = new_e;       //         new node is now the tail
    } else {
        AddFirst(l, new_e);        // q==NULL means "insert before everything"
    }
}
```

**Inserting X after node B in [A→B→C→D]:**
```
Before:
[A]──►[B]──►[C]──►[D]──►NULL
       ▲
       q

Step A: new_e->pNext = q->pNext   →   [X]──►[C]
Step B: q->pNext = new_e          →   [B]──►[X]──►[C]

After:
[A]──►[B]──►[X]──►[C]──►[D]──►NULL
```

> [!Warning] ⚠️ Step A BEFORE Step B. If you do B first, q->pNext becomes new_e, so when you then try to do A (new_e->pNext = q->pNext), you get new_e->pNext = new_e — a self-loop!

---

### 4.6 Insert Before Node q — AddBefore

**Strategy:** Find the node `p` that comes just before `q`, then do `AddAfter(l, p, new_e)`.

```cpp
void AddBefore(LIST &l, NODE *q, NODE* new_e) {
    if (q != NULL) {
        NODE* p = findBefore(l, q);  // find predecessor of q
        AddAfter(l, p, new_e);       // insert new_e after p (= before q)
    } else {
        AddFirst(l, new_e);
    }
}
```

**`findBefore` helper — walks until it finds the node whose pNext == q:**
```cpp
NODE* findBefore(LIST l, NODE* q) {
    NODE* p = l.pHead;
    while (p != NULL && p->pNext != q)
        p = p->pNext;
    return p;   // NULL if q is the head (no predecessor)
}
```

**Inserting X before node C in [A→B→C→D]:**
```
findBefore returns B (because B->pNext == C)
Then AddAfter(l, B, X):

Before: [A]──►[B]──►[C]──►[D]
After:  [A]──►[B]──►[X]──►[C]──►[D]
```

> [!Note] 💡 If `q` is the head node, `findBefore` returns `NULL`. `AddAfter(l, NULL, new_e)` calls `AddFirst` — which is exactly correct.

---

### 4.7 Search — Linear Scan

```cpp
NODE* Search(LIST l, Data K) {
    NODE *p = l.pHead;               // start at the first node
    while ((p != NULL) &&            // not past the end
           (p->Info != K))           // haven't found it yet
        p = p->pNext;                // move to next node
    return p;   // p==NULL → not found; otherwise p points to the node
}
```

**Searching for K=C in [A→B→C→D→E]:**

| Step | p points to | p->Info == K? | Action |
|---|---|---|---|
| 0 | node A | A ≠ C | advance |
| 1 | node B | B ≠ C | advance |
| 2 | node C | C == C | STOP, return p |

**Result:** pointer to node C.

**Searching for K=Z (not in list):**
Walk all the way to NULL → return NULL.

---

### 4.8 Extract Head — PickHead

> [!Definition] 📖 Extract vs Delete
> **Extracting** = removing a node from the chain and returning its pointer (node still exists in memory).
> **Deleting** = extracting + calling `delete p` to free the memory.
> Always extract first, then decide whether to delete.

```cpp
NODE* PickHead(LIST &l) {
    NODE *p = NULL;
    if (l.pHead != NULL) {
        p = l.pHead;               // save pointer to node being removed
        l.pHead = l.pHead->pNext;  // head advances to the second node
        p->pNext = NULL;           // isolate the extracted node
        if (l.pHead == NULL)       // list just became empty
            l.pTail = NULL;        // tail must also be NULL
    }
    return p;   // NULL if list was already empty
}
```

**Extracting head from [A→B→C→D]:**
```
Before:  pHead──►[A]──►[B]──►[C]──►[D]──►NULL
                                     ▲
                                   pTail

Step 1: p = pHead                  → p──►[A]
Step 2: pHead = pHead->pNext       → pHead──►[B]──►[C]──►[D]──►NULL
Step 3: p->pNext = NULL            → [A]──►NULL  (isolated)

After:
p──►[A│NULL]   (extracted, isolated)
pHead──►[B]──►[C]──►[D]──►NULL
```

**Extract + Delete head — RemoveHead:**
```cpp
Data RemoveHead(LIST &l) {
    if (l.pHead == NULL) return NULLDATA;
    NODE* p = PickHead(l);    // detach
    Data x = p->Info;         // save the value
    delete p;                 // FREE memory
    return x;                 // return the value
}
```

---

### 4.9 Extract Node After q — PickAfter

```cpp
NODE* PickAfter(LIST &l, NODE *q) {
    NODE *p;
    if (q != NULL) {
        p = q->pNext;            // p is the node to remove
        if (p != NULL) {
            if (p == l.pTail)    // if removing the tail,
                l.pTail = q;     //   q becomes the new tail
            q->pNext = p->pNext; // bypass p: q jumps over p to p's successor
            p->pNext = NULL;     // isolate p
        }
    } else {
        p = PickHead(l);         // q==NULL → remove the head
    }
    return p;
}
```

**Extracting node C (after q=B) from [A→B→C→D→E]:**
```
Before:
[A]──►[B]──►[C]──►[D]──►[E]──►NULL
       ▲     ▲
       q     p = q->pNext

Step 1: p = q->pNext             → p points to C
Step 2: q->pNext = p->pNext      → B now points to D (bypassing C)
Step 3: p->pNext = NULL          → C is isolated

After:
[A]──►[B]──►[D]──►[E]──►NULL
p──►[C│NULL]  (extracted)
```

**Extract + Delete after q — RemoveAfter:**
```cpp
Data RemoveAfter(LIST &l, NODE *q) {
    NODE *p = PickAfter(l, q);
    if (p == NULL) return NULLDATA;
    Data x = p->Info;
    delete p;
    return x;
}
```

---

### 4.10 Extract Node With Value K — PickNode

**Idea:** walk the list tracking both the current node `p` AND the node just before it `q`. When you find `p->Info == K`, call `PickAfter(l, q)` to detach `p`.

```cpp
NODE* PickNode(LIST &l, Data K) {
    NODE *p = l.pHead, *q = NULL;
    while ((p != NULL) && (p->Info != K)) {
        q = p;          // q trails one step behind p
        p = p->pNext;
    }
    if (p == NULL) return NULL;   // K not found
    return PickAfter(l, q);       // q is the predecessor; detach p
}
```

**Finding and extracting C from [A→B→C→D→E]:**

| Step | q | p | p->Info==K? |
|---|---|---|---|
| start | NULL | A | no |
| 1 | A | B | no |
| 2 | B | C | YES → stop |

Call `PickAfter(l, B)` → extracts C. ✓

**What if K is the head?**
- `q` stays `NULL`, `p` is the head node.
- `PickAfter(l, NULL)` → calls `PickHead(l)`. ✓

---

### 4.11 Traverse the List

```cpp
void ProcessList(LIST &l) {
    NODE *p = l.pHead;        // start at head
    while (p != NULL) {       // stop when we fall off the end
        ProcessNode(p);       // do something with this node
        p = p->pNext;         // move to the next node
    }
}
```

**Common uses of traversal:**

| Goal | What ProcessNode does |
|---|---|
| Print all values | `cout << p->Info` |
| Count nodes | increment a counter |
| Find all even values | check `p->Info % 2 == 0` |
| Sum all values | add `p->Info` to accumulator |
| Delete entire list | `delete p` (but careful — save `p->pNext` first!) |

---

### 4.12 Delete the Entire List — RemoveList

```cpp
void RemoveList(LIST &l) {
    NODE *p;
    while (l.pHead != NULL) {
        p = l.pHead;            // save pointer to current head
        l.pHead = p->pNext;     // advance head BEFORE deleting
        delete p;               // free memory of old head
    }
    l.pTail = NULL;             // clean up tail pointer
}
```

> [!Warning] ⚠️ You MUST save `p->pNext` (or advance `pHead`) BEFORE calling `delete p`. After `delete p`, the memory at `p` is freed — accessing `p->pNext` after deletion is undefined behavior.

---

## 5. Sorting — Detailed Reference

### The Two Options (Exam Theory Question)

| | Option 1: Swap Info fields | Option 2: Rewire pNext pointers |
|---|---|---|
| How it works | Swap the data values inside nodes (nodes stay in place) | Change which node points to which (data stays, links change) |
| Code complexity | Simple (like array sort) | Complex (pointer manipulation) |
| Best algorithms | BubbleSort, QuickSort | MergeSort, QuickSort |
| Memory overhead | None extra | Extra pointers for relinking |
| Stability | Can be stable | Naturally stable |
| Best for | Simple data (int, small structs) | Large objects (avoid copying data) |

**The lecture covers ONLY Option 2.**

---

### 5.1 List-Based Selection Sort — Full Explanation

**The idea in plain English:**
- Maintain a new empty list `lResult`.
- Repeat until the original list is empty:
  - Scan the whole list to find the smallest element.
  - Pull that element out (detach it — don't copy it).
  - Attach it to the end of `lResult`.
- The original list drains; `lResult` fills up in sorted order.
- Set `l = lResult`.

**Helper: FindMinprev**
Returns the **predecessor** of the minimum node (not the minimum itself), because `PickAfter` needs the predecessor.

```cpp
NODE* FindMinprev(LIST l) {
    NODE *min, *minprev, *p, *q;
    minprev = q = NULL;       // q trails behind p
    min = p = l.pHead;        // start: assume head is minimum
    while (p != NULL) {
        if (p->Info < min->Info) {  // found a smaller element
            min = p;                // update minimum node
            minprev = q;            // update minimum's predecessor
        }
        q = p;                // advance trailer
        p = p->pNext;         // advance scanner
    }
    return minprev;   // predecessor of the minimum node
                      // NULL means minimum is at the head
}
```

**Main sort:**
```cpp
void ListSelectionSort(LIST &l) {
    LIST lResult;
    NODE *min, *minprev;
    lResult.pHead = lResult.pTail = NULL;  // empty result list
    while (l.pHead != NULL) {
        minprev = FindMinprev(l);          // find predecessor of min
        min = PickAfter(l, minprev);       // detach min from l
        AddTail(lResult, min);             // append to result
    }
    l = lResult;   // replace original list with sorted result
}
```

**Full trace on `[7, 2, 1, 5, 3, 6, 19, 9]`:**

| Pass | List l (remaining) | Min found | minprev | lResult after |
|---|---|---|---|---|
| 1 | 7→2→1→5→3→6→19→9 | 1 (pos 3) | node(2) | [1] |
| 2 | 7→2→5→3→6→19→9 | 2 (pos 2) | node(7) | [1→2] |
| 3 | 7→5→3→6→19→9 | 3 (pos 3) | node(5) | [1→2→3] |
| 4 | 7→5→6→19→9 | 5 (pos 2) | node(7) | [1→2→3→5] |
| 5 | 7→6→19→9 | 6 (pos 2) | node(7) | [1→2→3→5→6] |
| 6 | 7→19→9 | 7 (pos 1) | NULL | [1→2→3→5→6→7] |
| 7 | 19→9 | 9 (pos 2) | node(19) | [1→2→3→5→6→7→9] |
| 8 | 19 | 19 (pos 1) | NULL | [1→2→3→5→6→7→9→19] |

**Result:** `[1, 2, 3, 5, 6, 7, 9, 19]` ✓

**Time complexity:** $O(n^2)$ — $n$ passes, each scans up to $n$ nodes.

---

### 5.2 List-Based Quick Sort — Full Explanation

**The idea in plain English:**
- If the list has 0 or 1 element, it's already sorted — stop.
- Pull the **first** node off as the **pivot** `X`.
- Walk through the rest: if a node's value ≤ X, put it in `list1`; otherwise put it in `list2`.
- Recursively sort `list1` and `list2`.
- Reassemble: `list = list1 + [X] + list2`.

**Helper: LISTAppend — splice one list onto the end of another in O(1)**

```cpp
void LISTAppend(LIST &list, LIST &list2) {
    if (list2.pHead == NULL) return;        // nothing to append
    if (list.pHead == NULL) {
        list = list2;                        // list is empty → just adopt list2
    } else {
        list.pTail->pNext = list2.pHead;    // connect: old tail → list2's head
        list.pTail = list2.pTail;           // update tail to list2's tail
    }
    Init(list2);   // reset list2 to empty (it's been absorbed)
}
```

**Main sort:**
```cpp
void ListQuickSort(LIST &list) {
    NODE *X, *p;
    LIST list1, list2;

    if (list.pHead == list.pTail) return;  // 0 or 1 element → done

    Init(list1); Init(list2);

    X = PickHead(list);     // detach pivot (first element)

    while (list.pHead != NULL) {           // partition remaining nodes
        p = PickHead(list);
        if (p->Info <= X->Info)
            AddTail(list1, p);             // ≤ pivot → left partition
        else
            AddTail(list2, p);             // > pivot → right partition
    }

    ListQuickSort(list1);   // sort left
    ListQuickSort(list2);   // sort right

    LISTAppend(list, list1); // reassemble: left...
    AddTail(list, X);        //             ...pivot...
    LISTAppend(list, list2); //             ...right
}
```

**Full trace on `[7, 2, 1, 5, 3, 6, 19, 9]`:**

```
ListQuickSort([7, 2, 1, 5, 3, 6, 19, 9])
  Pivot X = 7
  list1 = [2, 1, 5, 3, 6]   (all ≤ 7)
  list2 = [19, 9]            (all > 7)

  ListQuickSort([2, 1, 5, 3, 6])
    Pivot X = 2
    list1 = [1]              (≤ 2)
    list2 = [5, 3, 6]        (> 2)

    ListQuickSort([1])  → base case, return

    ListQuickSort([5, 3, 6])
      Pivot X = 5
      list1 = [3]            (≤ 5)
      list2 = [6]            (> 5)
      Both base cases.
      Reassemble: [3] + [5] + [6] = [3, 5, 6]

    Reassemble: [1] + [2] + [3, 5, 6] = [1, 2, 3, 5, 6]

  ListQuickSort([19, 9])
    Pivot X = 19
    list1 = [9]              (≤ 19)
    list2 = []               (> 19 → empty)
    Reassemble: [9] + [19] + [] = [9, 19]

  Final reassemble: [1,2,3,5,6] + [7] + [9,19] = [1,2,3,5,6,7,9,19]  ✓
```

**Time complexity:** Average $O(n \log n)$, Worst $O(n^2)$ (sorted input with first-element pivot).

---

## 6. Pointer Manipulation — The Most Common Mistakes

### Mistake 1: Wrong order in AddFirst

```cpp
// ❌ WRONG — loses the list!
l.pHead = new_e;            // head now points to new node
new_e->pNext = l.pHead;     // new_e->pNext = new_e itself! (self-loop)

// ✅ CORRECT
new_e->pNext = l.pHead;     // save old head first
l.pHead = new_e;            // then update head
```

### Mistake 2: Wrong order in AddAfter

```cpp
// ❌ WRONG — loses q's successor!
q->pNext = new_e;           // q now points to new_e
new_e->pNext = q->pNext;    // new_e->pNext = new_e itself! (self-loop)

// ✅ CORRECT
new_e->pNext = q->pNext;    // save q's successor first
q->pNext = new_e;           // then update q
```

### Mistake 3: Forgetting to update pTail

Whenever you insert at the end OR extract the last node, **pTail must be updated**.

```cpp
// Forgetting this when list becomes empty after PickHead:
if (l.pHead == NULL)
    l.pTail = NULL;   // ← MUST DO THIS
```

### Mistake 4: Accessing memory after delete

```cpp
// ❌ WRONG
delete p;
p->pNext;   // undefined behavior — memory is freed

// ✅ CORRECT
NODE* next = p->pNext;   // save what you need BEFORE delete
delete p;
// now use 'next'
```

### Mistake 5: Not setting new_e->pNext = NULL after extraction

```cpp
// In PickHead and PickAfter, always isolate the extracted node:
p->pNext = NULL;   // the extracted node should not dangle into the list
```

---

## 7. Quick-Reference: What Each Function Does and Returns

| Function | Input | What it does | Returns |
|---|---|---|---|
| `Init(l)` | list | sets pHead=pTail=NULL | void |
| `isEmpty(l)` | list | checks if list is empty | bool |
| `GetNode(x)` | data value | allocates new isolated node | NODE* (or NULL) |
| `AddFirst(l, new_e)` | list, node | inserts new_e at head | void |
| `AddTail(l, new_e)` | list, node | inserts new_e at tail | void |
| `AddAfter(l, q, new_e)` | list, predecessor q, node | inserts new_e after q | void |
| `AddBefore(l, q, new_e)` | list, successor q, node | inserts new_e before q | void |
| `InsertHead(l, x)` | list, data | creates node + AddFirst | NODE* |
| `InsertTail(l, x)` | list, data | creates node + AddTail | NODE* |
| `Search(l, K)` | list, key | finds node with Info==K | NODE* (NULL if not found) |
| `PickHead(l)` | list | detaches head node | NODE* (the removed node) |
| `PickAfter(l, q)` | list, predecessor q | detaches q->pNext | NODE* (the removed node) |
| `PickNode(l, K)` | list, key | finds and detaches node with K | NODE* (NULL if not found) |
| `RemoveHead(l)` | list | PickHead + delete | Data value |
| `RemoveAfter(l, q)` | list, predecessor q | PickAfter + delete | Data value |
| `RemoveList(l)` | list | deletes every node | void |
| `FindMinprev(l)` | list | finds predecessor of minimum | NODE* (NULL if min is head) |
| `ListSelectionSort(l)` | list | sorts via selection sort (O(n²)) | void |
| `LISTAppend(list, list2)` | two lists | splices list2 onto end of list | void |
| `ListQuickSort(list)` | list | sorts via quick sort (O(n log n) avg) | void |

---

## 8. Step-by-Step Algorithm Templates

### Template: Any insertion

```
1. new_e = GetNode(x)
2. if new_e == NULL → error, return NULL
3. Call the appropriate Add* function
4. Return new_e
```

### Template: Any extraction + deletion

```
1. Call Pick* to detach the node → get pointer p
2. if p == NULL → node not found, return NULLDATA
3. Save p->Info into a variable x
4. delete p  ← free memory
5. Return x
```

### Template: Traversal

```
1. p = pHead
2. While p != NULL:
   a. Do something with p
   b. p = p->pNext
```

### Template: Two-pointer (predecessor tracking)

```
Used in: PickNode, FindMinprev
1. p = pHead  (scanner)
2. q = NULL   (trailer — one step behind p)
3. While p not at target:
   a. q = p
   b. p = p->pNext
4. Now: q is p's predecessor, p is the target
```

---

## 9. Exam Traps and Edge Cases

### Edge Case: Single-node list

```
pHead ──► [A│NULL] ◄── pTail
```

- Extracting the only node: `pHead = pTail = NULL` after extraction.
- Inserting when empty: new node becomes both pHead and pTail.

### Edge Case: Extracting the tail node via PickAfter

If `p == pTail`, then `pTail = q` (the predecessor becomes the new tail).

```cpp
if (p == l.pTail)
    l.pTail = q;
```

### Edge Case: q == NULL in AddAfter / PickAfter

`q == NULL` means "operate at the head position":
- `AddAfter(l, NULL, new_e)` → calls `AddFirst`
- `PickAfter(l, NULL)` → calls `PickHead`

### Edge Case: K is the head node in PickNode

- `q` stays `NULL` throughout (never updated because we stop immediately).
- `PickAfter(l, NULL)` → `PickHead` — correct!

### Edge Case: Quick Sort with empty list2

`LISTAppend(list, list2)` has a guard: `if (list2.pHead == NULL) return;` — safe to call with an empty list.

### Edge Case: Quick Sort base case

`if (list.pHead == list.pTail) return;` — this handles BOTH:
- Empty list: `pHead == pTail == NULL` → `NULL == NULL` → true → return ✓
- Single element: `pHead == pTail` (one node) → true → return ✓

---

## 10. Comparison Tables for Theory Questions

### When to use which list type?

| Need | Use |
|---|---|
| Simple sequential access, insertions at both ends | SLL |
| Need to traverse backwards | DLL |
| Circular buffer, round-robin scheduling | CSLL |
| Need both bidirectional + circular traversal | CDLL |

### Sorting algorithm fit for linked lists

| Algorithm | Works on LL? | Why |
|---|---|---|
| MergeSort | ✅ Best | Pointer-based merge is natural; stable; O(n log n) |
| QuickSort | ✅ Good | PickHead as pivot; partition in O(n); O(n log n) avg |
| SelectionSort | ✅ Works | O(n²) but clean pointer extraction |
| BubbleSort | ⚠️ OK with swap-info | Works but O(n²); awkward with link rewiring |
| HeapSort | ❌ Poor | Requires random access (array indexing) |
| BinarySearch | ❌ N/A | Not a sort; requires random access |

---

## 11. Memory Diagrams for Every Operation at a Glance

### After Init:
```
pHead ──► NULL
pTail ──► NULL
```

### After InsertHead(l, X) on empty list:
```
pHead ──► [X│NULL] ◄── pTail
```

### After InsertHead(l, X) on [A→B]:
```
pHead ──► [X]──►[A]──►[B│NULL] ◄── pTail
```

### After InsertTail(l, X) on [A→B]:
```
pHead ──► [A]──►[B]──►[X│NULL] ◄── pTail
```

### After AddAfter(l, B, X) on [A→B→C]:
```
pHead ──► [A]──►[B]──►[X]──►[C│NULL] ◄── pTail
```

### After AddBefore(l, B, X) on [A→B→C]:
```
pHead ──► [A]──►[X]──►[B]──►[C│NULL] ◄── pTail
```

### After PickHead on [A→B→C]:
```
Extracted:  [A│NULL]
Remaining:  pHead──►[B]──►[C│NULL]◄──pTail
```

### After PickAfter(l, A) on [A→B→C→D]:
```
Extracted:  [B│NULL]
Remaining:  pHead──►[A]──►[C]──►[D│NULL]◄──pTail
```

### After RemoveList on [A→B→C]:
```
pHead ──► NULL
pTail ──► NULL
(all nodes freed)
```

---

## 12. The Complete Sorting Flow — Side by Side

### Selection Sort Flow

```
Original: [7→2→1→5→3→6→19→9]
lResult:  []

Pass 1: min=1, extract, append → lResult=[1],  l=[7→2→5→3→6→19→9]
Pass 2: min=2, extract, append → lResult=[1→2], l=[7→5→3→6→19→9]
Pass 3: min=3, extract, append → lResult=[1→2→3], l=[7→5→6→19→9]
...
Final:    l = [1→2→3→5→6→7→9→19]
```

### Quick Sort Call Tree

```
QS([7,2,1,5,3,6,19,9])
├── pivot=7
├── list1=[2,1,5,3,6], list2=[19,9]
├── QS([2,1,5,3,6])
│   ├── pivot=2
│   ├── list1=[1], list2=[5,3,6]
│   ├── QS([1]) → done
│   └── QS([5,3,6])
│       ├── pivot=5
│       ├── list1=[3], list2=[6]
│       ├── QS([3]) → done
│       ├── QS([6]) → done
│       └── result: [3,5,6]
│   └── result: [1,2,3,5,6]
├── QS([19,9])
│   ├── pivot=19
│   ├── list1=[9], list2=[]
│   ├── QS([9]) → done
│   ├── QS([]) → done
│   └── result: [9,19]
└── Final: [1,2,3,5,6] + [7] + [9,19] = [1,2,3,5,6,7,9,19] ✓
```

---

## 13. Advantages and Disadvantages — Full Version

### Linked List Advantages

**1. No fixed size** — Arrays require you to declare a size upfront (e.g., `int arr[100]`). If you need 101 elements, you're stuck. Linked lists grow one node at a time, on demand. No wasted space.

**2. Efficient insertions and deletions** — Inserting into the middle of an array requires shifting all elements after the insertion point — $O(n)$. In a linked list, you only rewire 2-3 pointers — $O(1)$ once you have the position.

**3. Flexible memory allocation** — Array elements must occupy a contiguous block. If you need a large array but RAM is fragmented, the allocation may fail even if total free memory is sufficient. Linked list nodes can live anywhere.

### Linked List Disadvantages

**1. Memory overhead** — Every node carries at least one extra pointer (8 bytes on 64-bit systems). For a list of integers (4 bytes each), the pointer doubles the per-element cost.

**2. Slow random access** — To read the 50th element, you must walk from the head through 49 nodes. Arrays give you element $i$ in one step: `arr[i]`. This makes linked lists incompatible with algorithms needing random access (binary search, heap operations).

**3. Complex implementation** — Every operation requires careful pointer management. One wrong assignment corrupts the entire list. Arrays are indexed directly with no such risk.

---

## 14. Glossary — Every Term You Need

| Term | Meaning |
|---|---|
| **Node** | The basic unit of a linked list; contains data (Info) and one or more pointers |
| **pHead** | Pointer to the first node; entry point to the list |
| **pTail** | Pointer to the last node; enables O(1) tail append |
| **pNext** | Forward pointer inside a node |
| **pPrev** | Backward pointer inside a node (DLL only) |
| **Info** | The data payload stored in a node |
| **NULL** | Null pointer; indicates "no node here" |
| **Traverse** | Walk through every node in order from head to tail |
| **Extract (Pick)** | Remove a node from the list chain WITHOUT freeing memory |
| **Delete (Remove)** | Extract a node AND free its memory with `delete` |
| **Pivot** | The chosen element that partitions a list during QuickSort |
| **Partition** | Splitting a list into two groups relative to the pivot |
| **minprev** | The node immediately before the minimum node; needed for PickAfter |
| **lResult** | Temporary result list used in selection sort |
| **LISTAppend** | Splice one list onto the tail of another in O(1) |
| **Contiguous** | Stored in adjacent memory locations (arrays) |
| **Dynamic allocation** | Requesting memory at runtime with `new` |
| **Memory leak** | Forgetting to `delete` a node after removing it |
| **Dangling pointer** | A pointer that points to memory that has been freed |
