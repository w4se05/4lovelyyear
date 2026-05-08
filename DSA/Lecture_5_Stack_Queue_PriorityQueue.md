---
tags: [61CSE108, stack, queue, priority-queue, data-structures]
topic: "Lecture 5: Stack, Queue, and Priority Queue"
course: "61CSE108: Algorithms and Data Structures"
---

# Lecture 5: Stack, Queue, and Priority Queue

> [!Note] 💡 Notation Conventions
> - $n$ — number of elements in the structure
> - **LIFO** — Last-In-First-Out (Stack ordering)
> - **FIFO** — First-In-First-Out (Queue ordering)
> - **PQ** — Priority Queue
> - **MAX** — compile-time constant for array capacity
> - `top` — index (array) or pointer (linked list) to the topmost stack element
> - `front` / `rear` — pointers to the front (dequeue side) and back (enqueue side) of a queue
> - `pHead` / `pTail` — head and tail pointers of a singly linked list
> - All code examples are in **C++**

---

## Part 1 — Conceptual Section

---

## 1. Stack

> [!Definition] 📖 Stack
> A **Stack** is a collection of data accessed in a **Last-In-First-Out (LIFO)** manner: the most recently inserted element is the first to be removed.

### 1.1 Operations

> [!Definition] 📖 Stack Operations
> **1.** `push(item)` — Insert `item` onto the top of the stack.
> **2.** `pop()` — Remove the top element. Reports underflow if empty.
> **3.** `peek()` — Return (without removing) the top element.
> **4.** `isEmpty()` — Return `true` if stack has no elements.
> **5.** `isFull()` — Return `true` if stack has reached capacity (array implementation only).

```
        In ──► [top]
                 |
                ...
                 |
              [bottom] ──► Out (pop)
```

### 1.2 Uses

> [!Note] 💡 Stack Applications
> - **Function calls / recursion** — the call state is saved on the runtime stack before a call, so execution can resume afterward.
> - **Bracket/parenthesis matching** — verify that all opening brackets have correct closing counterparts.
> - **Arithmetic expression evaluation** — postfix (RPN) calculation.
> - **Infix-to-postfix conversion** — re-order operators according to precedence.
> - **Maze traversal** — track visited paths with backtracking.

---

## 2. Stack Implementation via Array

> [!Definition] 📖 Array-Based Stack
> Maintain a fixed-size array `arr[0..MAX-1]` and an integer `top` (initially $-1$) pointing to the index of the current top element.
> - **Empty condition:** `top == -1`
> - **Full condition:** `top == MAX - 1`
> - **Push:** increment `top`, then write to `arr[top]`
> - **Pop:** decrement `top`
> - **Peek:** return `arr[top]`

> [!Property] ⚙️ Complexity — Array Stack
> All operations (`push`, `pop`, `peek`, `isEmpty`, `isFull`) run in $O(1)$ time. Space is $O(\text{MAX})$.

```cpp
#define MAX 100

class Stack {
private:
    int top;
    int arr[MAX]; // replace int with any abstract item type

public:
    Stack() { top = -1; }

    bool isEmpty() const { return top == -1; }
    bool isFull()  const { return top == MAX - 1; }

    void push(int value) {
        if (isFull()) { std::cout << "Stack Overflow\n"; return; }
        arr[++top] = value;
    }

    void pop() {
        if (isEmpty()) { std::cout << "Stack Underflow\n"; return; }
        --top;
    }

    int peek() const {
        if (isEmpty()) { std::cout << "Stack is empty\n"; return -1; }
        return arr[top];
    }

    void display() const {
        for (int i = top; i >= 0; i--)
            std::cout << arr[i] << " ";
        std::cout << "\n";
    }
};
```

> [!Example] 📘 Array Stack — Execution Trace
> **Using:** push, pop, peek, display
>
> ```
> s.push(10); s.push(20); s.push(30);
> s.display();   // → 30 20 10   (top to bottom)
> s.pop();       // removes 30
> s.display();   // → 20 10
> s.peek();      // → 20
> ```
> **Step-by-step:**
> **1.** push(10) → arr[0]=10, top=0
> **2.** push(20) → arr[1]=20, top=1
> **3.** push(30) → arr[2]=30, top=2
> **4.** display prints from top=2 down → `30 20 10`
> **5.** pop() → top=1; top element is now 20
> **6.** display → `20 10`
> **7.** peek() → arr[1] = **20**

---

## 3. Stack Implementation via Singly Linked List

> [!Definition] 📖 Linked-List-Based Stack
> Each element is a `Node` holding `data` and a `next` pointer. The `top` pointer always refers to the **head** of the list (most recently pushed node).
> - **Push:** create a new node, set `newNode->next = top`, then `top = newNode` — $O(1)$
> - **Pop:** save `top`, advance `top = top->next`, delete saved node — $O(1)$
> - **Peek:** return `top->data` — $O(1)$
> - **No fixed capacity** — `isFull()` is always `false` (bounded only by heap memory)

```
top ──► [30 | •]──► [20 | •]──► [10 | null]
         (most recent)             (oldest)
```

```cpp
class Stack {
private:
    struct Node {
        int data;
        Node* next;
        Node(int value) : data(value), next(nullptr) {}
    };
    Node* top;

public:
    Stack() : top(nullptr) {}
    ~Stack() { while (!isEmpty()) pop(); }

    bool isEmpty() const { return top == nullptr; }

    void push(int value) {
        Node* newNode = new Node(value);
        newNode->next = top;
        top = newNode;
    }

    void pop() {
        if (isEmpty()) { std::cout << "Stack Underflow\n"; return; }
        Node* temp = top;
        top = top->next;
        delete temp;
    }

    int peek() const {
        if (isEmpty()) { std::cout << "Stack is empty\n"; return -1; }
        return top->data;
    }
};
```

> [!Note] 💡 StackLL Structure
> The **Top = Head** convention means push/pop both happen at the head — both $O(1)$ without needing a tail pointer.

---

## 4. Stack Applications

### 4.1 Bracket Matching

> [!Definition] 📖 Bracket Matching Problem
> Given a string, determine whether all bracket pairs are **properly matched and nested**. Three types of errors:
> - Too many closing brackets: `(..)`  `)`  → underflow on pop
> - Too many opening brackets: `(..(..` → stack non-empty at end
> - Mismatched types: `[..(..]..)` → popped bracket ≠ expected closing bracket

> [!Property] ⚙️ Algorithm
> ```
> create empty stack
> for every character ch in input:
>     if ch is an opening bracket: push(ch)
>     if ch is a closing bracket:
>         if isEmpty() or peek() doesn't match ch: FLAG ERROR
>         else: pop()
> if stack is not empty: FLAG ERROR (unmatched opens)
> ```

> [!Example] 📘 Bracket Matching Trace
> **Using:** push, pop, isEmpty
>
> Input: `{ a + ( b + c[1] ) * 2 * d + e[2] }`
>
> | Char | Action | Stack (bottom→top) |
> |------|--------|--------------------|
> | `{`  | push   | `{`                |
> | `(`  | push   | `{ (`              |
> | `[`  | push   | `{ ( [`            |
> | `]`  | pop `[` matches | `{ (` |
> | `)`  | pop `(` matches | `{`  |
> | `[`  | push   | `{ [`              |
> | `]`  | pop `[` matches | `{`  |
> | `}`  | pop `{` matches | empty |
>
> Stack empty at end → **VALID** ✓

---

### 4.2 Arithmetic Expressions & Postfix Calculation

> [!Definition] 📖 Expression Notations
> For operands $A$, $B$ and operator $\odot$:
> - **Infix:** $A \odot B$ — operator between operands; **ambiguous** without parentheses or precedence rules
> - **Prefix:** $\odot A B$ — operator before operands
> - **Postfix (RPN):** $A B \odot$ — operator after operands; **unambiguous**, no parentheses needed

> [!Note] 💡 Precedence Rules
> Operators are evaluated in priority order (high → low):
> **1.** `^` (power)
> **2.** `*`, `/`
> **3.** `+`, `-`
> Operators of equal precedence evaluate **left to right**.

> [!Property] ⚙️ Postfix Evaluation Algorithm
> ```
> create empty stack
> for each token t in postfix expression:
>     if t is an operand: push(t)
>     if t is an operator:
>         arg2 = pop()
>         arg1 = pop()
>         push(arg1 ⊙ arg2)
> result = pop()
> ```

> [!Example] 📘 Postfix Evaluation: `4 2 3 + *`
> **Using:** push, pop
> (Represents infix: $4 \times (2 + 3)$)
>
> | Token | Action | Stack |
> |-------|--------|-------|
> | `4`   | push   | `[4]` |
> | `2`   | push   | `[4, 2]` |
> | `3`   | push   | `[4, 2, 3]` |
> | `+`   | arg2=3, arg1=2, push(2+3)=5 | `[4, 5]` |
> | `*`   | arg2=5, arg1=4, push(4×5)=20 | `[20]` |
>
> **Result = 20** ✓

---

> [!Property] ⚙️ Infix-to-Postfix Conversion Algorithm (Shunting-Yard)
> **1.** Initialize empty operator stack and empty output list.
> **2.** Scan expression left to right. For each token:
>    - **Operand** → append to output.
>    - **`(`** → push onto stack.
>    - **`)`** → pop and output until `(` is reached; discard the `(`.
>    - **Operator** $op$ → while stack is non-empty AND `top` has precedence $\geq$ $op$ AND `top ≠ (`: pop to output. Then push $op$.
> **3.** After scanning: pop all remaining stack operators to output.

> [!Example] 📘 Infix-to-Postfix: `a + ( b - c / d ) * e`
> **Using:** Shunting-Yard algorithm
>
> | ch  | Stack (bottom→top) | Postfix Output |
> |-----|--------------------|----------------|
> | `a` |                    | `a`            |
> | `+` | `+`                | `a`            |
> | `(` | `+ (`              | `a`            |
> | `b` | `+ (`              | `a b`          |
> | `-` | `+ ( -`            | `a b`          |
> | `c` | `+ ( -`            | `a b c`        |
> | `/` | `+ ( - /`          | `a b c`        |
> | `d` | `+ ( - /`          | `a b c d`      |
> | `)` | pop `/`→ output, pop `-`→ output, discard `(` | `a b c d / -` |
> |     | `+`                | `a b c d / -`  |
> | `*` | `+ *`  (prec(`*`) > prec(`+`), no pop) | `a b c d / -` |
> | `e` | `+ *`              | `a b c d / - e` |
> | END | pop `*`, pop `+`   | `a b c d / - e * +` |
>
> **Result:** `a b c d / - e * +`

---

## 5. Queue

> [!Definition] 📖 Queue
> A **Queue** is a collection of data accessed in a **First-In-First-Out (FIFO)** manner: elements are inserted at the **back (rear)** and removed from the **front**.

### 5.1 Operations

> [!Definition] 📖 Queue Operations
> **1.** `enqueue(item)` — Insert `item` at the rear.
> **2.** `dequeue()` — Remove the front element. Reports underflow if empty.
> **3.** `peek()` — Return (without removing) the front element.
> **4.** `isEmpty()` / `isFull()` — Check capacity.

```
enqueue ──► [ back | ... | front ] ──► dequeue
                peek ↑
```

### 5.2 Uses

> [!Note] 💡 Queue Applications
> - **Print queue** — jobs processed in submission order.
> - **Simulations** — model real-world waiting lines.
> - **Breadth-first traversal** of trees and graphs.
> - **Palindrome checking** (illustration; not a primary real-world use).

---

## 6. Queue Implementation via Array

> [!Definition] 📖 Array-Based Queue
> Uses a fixed array `arr[0..MAX-1]` with two index pointers:
> - `front` — index of the element to dequeue next (initially $-1$)
> - `rear` — index of the last enqueued element (initially $-1$)
>
> - **Empty:** `front == -1` or `front > rear`
> - **Full:** `rear == MAX - 1`
> - **Enqueue:** increment `rear`, write to `arr[rear]`; set `front = 0` if was empty
> - **Dequeue:** increment `front`

> [!Warning] ⚠️ Array Queue Limitation
> This linear array implementation does **not** recycle space freed at the front. As `front` advances, positions `arr[0..front-1]` are wasted. A **circular array** variant (not shown in lecture) fixes this.

```cpp
class Queue {
private:
    int arr[MAX], front, rear;
public:
    Queue() { front = -1; rear = -1; }

    bool isEmpty() const { return front == -1 || front > rear; }
    bool isFull()  const { return rear == MAX - 1; }

    void enqueue(int value) {
        if (isFull()) { std::cout << "Queue Overflow\n"; return; }
        if (isEmpty()) front = 0;
        arr[++rear] = value;
    }

    void dequeue() {
        if (isEmpty()) { std::cout << "Queue Underflow\n"; return; }
        front++;
    }

    int peek() const {
        if (isEmpty()) { std::cout << "Queue is empty\n"; return -1; }
        return arr[front];
    }
};
```

> [!Example] 📘 Array Queue — Execution Trace
> **Using:** enqueue, dequeue, peek, display
>
> ```
> q.enqueue(10); q.enqueue(20); q.enqueue(30);
> q.display();   // → 10 20 30
> q.dequeue();   // removes 10
> q.display();   // → 20 30
> q.peek();      // → 20
> ```
> **Step-by-step:**
> **1.** enqueue(10): front=0, rear=0, arr=[10]
> **2.** enqueue(20): rear=1, arr=[10,20]
> **3.** enqueue(30): rear=2, arr=[10,20,30]
> **4.** display prints front→rear: `10 20 30`
> **5.** dequeue(): front=1; arr[1]=20 is now the front
> **6.** display: `20 30`
> **7.** peek(): arr[front] = arr[1] = **20**

---

## 7. Queue Implementation via Singly Linked List

> [!Definition] 📖 Linked-List-Based Queue
> Maintains two pointers:
> - `front` (= **head** of list) — dequeue happens here
> - `rear` (= **tail** of list) — enqueue appends here
>
> - **Enqueue:** allocate new node; if `rear` exists set `rear->next = newNode`, else set `front = newNode`; update `rear = newNode`. $O(1)$
> - **Dequeue:** advance `front = front->next`; if `front == nullptr` also set `rear = nullptr`. $O(1)$

```
front ──► [10|•]──► [20|•]──► [30|null] ◄── rear
           dequeue                            enqueue
```

```cpp
class Queue {
    struct Node {
        int data; Node* next;
        Node(int v) : data(v), next(nullptr) {}
    };
    Node* front = nullptr;
    Node* rear  = nullptr;
public:
    ~Queue() { while (front) dequeue(); }
    bool isEmpty() const { return front == nullptr; }

    void enqueue(int val) {
        Node* node = new Node(val);
        if (rear) rear->next = node;
        else front = node;
        rear = node;
    }

    void dequeue() {
        if (isEmpty()) { std::cout << "Underflow\n"; return; }
        Node* temp = front;
        front = front->next;
        if (!front) rear = nullptr;
        delete temp;
    }

    int peek() const {
        if (isEmpty()) return -1;
        return front->data;
    }
};
```

---

## 8. Application: Palindrome Checking

> [!Definition] 📖 Palindrome
> A string that reads the same left-to-right and right-to-left.
> Examples: `"radar"`, `"deed"`, `"aibohphobia"`
> Non-examples: `"data"`, `"little"`

> [!Property] ⚙️ Algorithm (Stack + Queue)
> **1.** Feed each alphanumeric character (lowercased) simultaneously into a **stack** and a **queue**.
> **2.** The stack reverses the order; the queue preserves it.
> **3.** Pop/dequeue simultaneously and compare characters. If any mismatch → **not a palindrome**. If all match → **palindrome**.

> [!Note] 💡 Why This Works
> After loading, `stack.pop()` gives characters in **reverse** order while `queue.dequeue()` gives them in **original** order. A palindrome produces identical sequences.

```cpp
bool isPalindrome(const std::string& str) {
    std::stack<char> s;
    std::queue<char> q;
    for (char ch : str) {
        if (isalnum(ch)) {
            char lower = tolower(ch);
            s.push(lower);
            q.push(lower);
        }
    }
    while (!s.empty()) {
        if (s.top() != q.front()) return false;
        s.pop(); q.pop();
    }
    return true;
}
```

> [!Warning] ⚠️ Pedagogical Note
> The lecture explicitly states: palindrome checking via this stack+queue method is used **for illustration only** — it is not a real-world application of a queue, as you can check palindromes more simply.

---

## 9. Priority Queue

> [!Definition] 📖 Priority Queue (PQ)
> A queue variant where each element has an associated **priority**. Dequeue always returns the element with the **highest priority** (not necessarily the one inserted first). Among elements of equal priority, the **first-inserted** is returned (FIFO tie-breaking).

> [!Definition] 📖 Priority Queue Operations
> **1.** `Enqueue(x)` — Insert element $x$ into the PQ at the correct position according to its priority.
> **2.** `y ← Dequeue()` — Remove and return the element $y$ with the highest priority key.

### 9.1 Heap-Based Priority Queue (Max-Heap)

> [!Definition] 📖 Max-Heap
> A complete binary tree where every parent node has a value **≥** both its children. The maximum element is always at the root. Internally stored as an array using the index mapping:
> - Parent of index $i$: $\lfloor (i-1)/2 \rfloor$
> - Left child of $i$: $2i + 1$
> - Right child of $i$: $2i + 2$

> [!Note] 💡 heapify()
> `heapify()` is the procedure that restores the heap property after an insertion or deletion by "bubbling up" or "sifting down" the displaced element.

### 9.2 Insertion into a Max-Heap

> [!Property] ⚙️ Insertion Algorithm
> **1.** Append the new element to the end of the array (next leaf position in the tree).
> **2.** Call `heapify()` (bubble-up) to restore the heap property.

> [!Example] 📘 Heap Insertion: insert 9 into {7, 2, 1, 5, 3, 6, 19}
> **Using:** heap insertion, heapify
>
> Initial array representation (not a heap yet after naïve append):
> `[7, 2, 1, 5, 3, 6, 19, 9]`
>
> After `heapify()` → max-heap: `[19, 9, 7, 5, 3, 6, 1, 2]`
>
> ```mermaid
> graph TD
>     A[19] --> B[9]
>     A --> C[7]
>     B --> D[5]
>     B --> E[3]
>     C --> F[6]
>     C --> G[1]
>     D --> H[2]
> ```

### 9.3 Deletion from a Max-Heap

> [!Property] ⚙️ Deletion Algorithm
> **1.** Identify and remove the target element (typically the root for dequeue, or any element by position).
> **2.** Replace the deleted position with the last element in the array.
> **3.** Call `heapify()` (sift-down) to restore the heap property.

> [!Example] 📘 Heap Deletion: delete element 5 from {7, 2, 1, 5, 3, 6, 19}
> **Using:** heap deletion, heapify
>
> Remove 5 (position 3), replace with last element:
> Array after removal: `[7, 2, 1, _, 3, 6, 19]` → fill gap → apply heapify
>
> After `heapify()` → max-heap: `[19, 6, 7, 2, 3, 1]`
>
> ```mermaid
> graph TD
>     A[19] --> B[6]
>     A --> C[7]
>     B --> D[2]
>     B --> E[3]
>     C --> F[1]
> ```

### 9.4 Use Cases

> [!Note] 💡 Priority Queue Variants
> **1. Max-Heap (default):** Largest element dequeues first. Used in heapsort, leaderboards.
> **2. Min-Heap (Dijkstra-style pairs):** Stores `(distance, node_id)`; smallest distance dequeues first. Used in shortest-path algorithms.
> **3. Custom comparator:** Stores objects (e.g., `Task{name, priority}`) with a user-defined ordering. Used in CPU job scheduling, to-do apps.

---

## 📘 Examples & Applications

### Example 1 — Stack Operations Trace

> [!Example] 📘 Stack Usage Walkthrough
> **Using:** push, pop, peek
>
> ```
> Stack s;
> s.push(7);  s.push(2);  s.push(1);
> d = s.peek();    // d = 1 (top)
> s.pop();         // removes 1; top is now 2
> s.push(5);       // stack: [7, 2, 5]  (top=5)
> s.pop();         // removes 5; top is now 2
> ```
> Final stack (top→bottom): **2, 7**

---

### Example 2 — Queue Operations Trace

> [!Example] 📘 Queue Usage Walkthrough
> **Using:** enqueue, dequeue, peek
>
> ```
> Queue q;
> q.enqueue("a"); q.enqueue("b"); q.enqueue("c");
> p = q.peek();    // p = "a" (front)
> q.dequeue();     // removes "a"; front is now "b"
> q.enqueue("d"); // queue: [b, c, d]
> q.dequeue();     // removes "b"; front is now "c"
> ```
> Final queue (front→back): **c, d**

---

### Example 3 — Full Infix-to-Postfix + Evaluation (Exam-Style)

> [!Example] 📘 Combined: Convert and Evaluate `(1 + 2) / 3`
> **Using:** infix-to-postfix conversion, postfix evaluation
>
> **Step 1: Convert to postfix**
>
> | ch  | Stack | Output |
> |-----|-------|--------|
> | `(` | `(`   |        |
> | `1` | `(`   | `1`    |
> | `+` | `( +` | `1`    |
> | `2` | `( +` | `1 2`  |
> | `)` | empty | `1 2 +`|
> | `/` | `/`   | `1 2 +`|
> | `3` | `/`   | `1 2 + 3` |
> | END | empty | `1 2 + 3 /` |
>
> **Postfix:** `1 2 + 3 /`
>
> **Step 2: Evaluate**
>
> | Token | Stack |
> |-------|-------|
> | `1`   | `[1]` |
> | `2`   | `[1, 2]` |
> | `+`   | arg2=2, arg1=1 → push(3) → `[3]` |
> | `3`   | `[3, 3]` |
> | `/`   | arg2=3, arg1=3 → push(1) → `[1]` |
>
> **Result:** $\dfrac{1+2}{3} = 1$ ✓

---

### Example 4 — Palindrome Check (Stack + Queue)

> [!Example] 📘 Palindrome: `"radar"`
> **Using:** stack (reversal), queue (preservation), character comparison
>
> Input characters (all alphanumeric, lowercased): `r, a, d, a, r`
>
> After loading:
> - Stack (top→bottom): `r, a, d, a, r`
> - Queue (front→back): `r, a, d, a, r`
>
> Comparison rounds:
>
> | Stack.pop() | Queue.dequeue() | Match? |
> |-------------|-----------------|--------|
> | `r`         | `r`             | ✓      |
> | `a`         | `a`             | ✓      |
> | `d`         | `d`             | ✓      |
> | `a`         | `a`             | ✓      |
> | `r`         | `r`             | ✓      |
>
> All match → **"radar" IS a palindrome** ✓

---

## 🗂️ Summary

### Stack (LIFO)

- Data structure accessed Last-In-First-Out.
- Operations: `push`, `pop`, `peek` — all $O(1)$.
- **Array:** `top` integer pointer; empty when `top == -1`; full when `top == MAX-1`.
- **Linked list:** `top` = head pointer; push/pop at head; no capacity limit.
- Applications: function calls, recursion, bracket matching, postfix evaluation, infix→postfix conversion.

### Queue (FIFO)

- Data structure accessed First-In-First-Out.
- Operations: `enqueue`, `dequeue`, `peek` — all $O(1)$.
- **Array:** `front` and `rear` indices; empty when `front == -1` or `front > rear`; full when `rear == MAX-1`. (Linear array wastes space at front after dequeues.)
- **Linked list:** `front` = head, `rear` = tail; enqueue at tail, dequeue at head; no capacity limit.
- Applications: print queues, simulations, BFS traversal.

### Infix → Postfix (Shunting-Yard)

1. Operand → output immediately.
2. `(` → push.
3. `)` → pop to output until `(`, discard `(`.
4. Operator → pop operators of ≥ precedence (excluding `(`), then push current.
5. End → pop remaining stack to output.

### Postfix Evaluation

- Read left-to-right: push operands; on operator pop two operands, compute, push result.
- Final stack value is the result.

### Priority Queue

- Elements ordered by priority; dequeue always yields highest-priority element (FIFO tie-breaking).
- Typically implemented as a **max-heap** (or min-heap) using an array with `heapify()`.
- **Insertion:** append at end, `heapify()` up.
- **Deletion:** remove target, replace with last element, `heapify()` down.
- Use cases: heapsort, Dijkstra's algorithm (min-heap with pairs), task scheduling.

### Complexity at a Glance

| Structure       | push/enqueue | pop/dequeue | peek |
|-----------------|:-----------:|:-----------:|:----:|
| Stack (array/LL)| $O(1)$      | $O(1)$      | $O(1)$ |
| Queue (array/LL)| $O(1)$      | $O(1)$      | $O(1)$ |
| Priority Queue (heap) | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
