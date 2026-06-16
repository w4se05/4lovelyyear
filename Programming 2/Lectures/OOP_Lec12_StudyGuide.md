# Lec12: Container Classes (Linked Lists) — Study Guide

---

## 1. CONCEPT CARD: Template-Based & Object-Based Linked Lists

**What it is:** A linked list is a dynamic data structure where each node holds data and a pointer to the next node (singly-linked) or to both next and previous nodes (doubly-linked). Template-based lists work with any type at compile time; object-based lists use a common base class so different object types can coexist in the same list.

**What problem it solves:** Arrays have fixed size — you must know the maximum ahead of time or reallocate when full. Inserting in the middle requires shifting everything. Linked lists solve both: they grow and shrink one node at a time, and insertion/deletion only requires changing a couple of pointers. The template version gives type safety (a list of ints can't accidentally hold a Student); the object-based version gives runtime flexibility (a list can hold Students, Faculty, and Administrators together through base class pointers).

**How it works (template-based singly-linked):**
1. `TNode<T>` holds a `T value` and a `TNode<T>* next` pointer.
2. `TList<T>` maintains `head` (dummy node before first real node), `tail` (dummy node after last), and `current` (cursor).
3. Head and tail are dummy nodes — they never hold data, they exist to make edge cases disappear (you never have a null list).
4. `insertAfter(const T& val)`: creates a new TNode, splices it between current and current->next, advances current.
5. `append(val)`: calls `goLast()` then `insertAfter(val)`. `prepend(val)`: calls `goTop()` then `insertAfter(val)`.

**How it works (object-based doubly-linked):**
1. `DblNode` is an abstract base with `next`, `prev`, and pure virtual functions (`printOn`, `readFrom`, `operator==`).
2. Concrete node types (Student, Faculty) inherit from `DblNode` and implement the virtual functions.
3. `DblList` holds pointers to `first`, `last`, and a `size` counter.
4. `append(DblNode* n)`: links n to the end, updating `prev` and `next` on both sides.
5. `remove(DblNode* n)`: updates `first`/`last` if needed, calls `n->detach()`, decrements size.
6. `detach()` disconnects a node from its neighbors by rewiring their pointers to skip over it.

**Concrete example:** A university registration system. `TList<Student*>` holds a class roster — quick prepend/append for add/drop. `DblList` (object-based) holds the full college enrollment — `Student`, `Faculty`, `Administrator` objects all stored together. The object-based list can `find()` any node type via the virtual `operator==`, and `printOn()` calls the correct display for each type.

**What it is NOT:** A linked list is NOT a random-access structure. You cannot do `list[5]` (unless you overload `operator[]` and traverse from head each time, which is slow). Access is always sequential — start from head and follow `next` pointers.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
// ===== TEMPLATE-BASED SINGLY LINKED LIST =====

template <class T>
class TNode {
    friend class TList<T>;          // TList can touch private members
    T value;                         // Data stored in this node
    TNode<T>* next;                  // Pointer to next node
public:
    TNode() : next(0) {}            // Default: null next
    TNode(const T& val);            // Initialize with value
};

template <class T>
class TList {
    TNode<T>* head;                 // Dummy: first "node" (no data)
    TNode<T>* tail;                 // Dummy: after last real node
    TNode<T>* current;              // Cursor for traversal
public:
    TList();                         // Create with dummy head/tail linked
    ~TList();                        // Clear + delete dummies
    void append(const T& val);       // Add to end
    void prepend(const T& val);      // Add to beginning
    T get() const;                   // Get value at current
    int isEmpty() const;             // head->next == tail?
    void goTop();                    // current = head
    void goLast();                   // Walk to node before tail
    int advance();                   // Move current forward; return 1 if ok
    void insertAfter(const T& val);   // Splice new node after current
    void clear();                    // Delete all real nodes
};

// Key constructor: dummy nodes form a circle
template <class T>
TList<T>::TList() {
    head = new TNode<T>;
    tail = new TNode<T>;
    head->next = tail;
    tail->next = head;              // Circle: enables edge-case handling
    current = head;
}

// Empty check:
template <class T>
int TList<T>::isEmpty() const {
    return head->next == tail;      // No real nodes between dummies
}

// Insert after current:
template <class T>
void TList<T>::insertAfter(const T& val) {
    TNode<T>* p = new TNode<T>(val);
    p->next = current->next;        // New node points to what current pointed to
    current->next = p;              // Current now points to new node
    current = p;                    // Advance cursor to new node
}
```

```cpp
// ===== OBJECT-BASED DOUBLY LINKED LIST =====

class DblNode {
    friend class DblList;
    virtual void printOn(ostream& os) const = 0;  // Pure virtual
    virtual void readFrom(istream& is) = 0;
    DblNode* next;
    DblNode* prev;
public:
    DblNode() : next(0), prev(0) {}
    virtual ~DblNode() {}
    DblNode* getNext() const { return next; }
    DblNode* getPrev() const { return prev; }
    DblNode* detach();                              // Unlink from neighbors
    virtual int operator==(const DblNode& n) const = 0;
};

DblNode* DblNode::detach() {
    if (next) next->prev = prev;    // Next node's prev skips over us
    if (prev) prev->next = next;    // Prev node's next skips over us
    prev = 0;                       // Disconnect from this node
    next = 0;
    return this;
}
```

---

## 3. EXAM TRAPS

- **The dummy head/tail circle: `tail->next = head;`** — this is NOT a bug. It ensures that even in an empty list, `goLast()` won't dereference NULL because it walks until `next == tail`, not until `next == NULL`.
- **`insertAfter` assumes `current` is valid.** If you forget to call `goTop()` before the first insert, `current` might be garbage. Always set `current` to a known position first.
- **Inserting BEFORE the current node in a singly-linked list requires traversal from head.** There's no `prev` pointer, so you can't go backwards. That's why `append` and `prepend` in the template list both use `insertAfter` — they just position `current` differently first.
- **`detach()` does NOT `delete this`.** It only unlinks. The caller must `delete` the node after detaching (or the list destructor handles it). Two separate responsibilities.
- **Virtual `operator==` in DblNode requires a downcast inside the override.** In `Student::operator==(const DblNode& p)`, you must cast: `return id == ((Student&)p).id;`. If `p` is actually a Faculty, this is undefined behavior. Assumption: `find()` only compares matching types.
- **Template class out-of-line definitions need `template<class T>` AND `ClassName<T>::` on every method.** Forget the `<T>` on the class name and it won't compile.
- **In object-based lists, nodes are allocated on the heap with `new`.** The list typically does NOT delete the data inside — the caller might still need it. The contract is important. In `DblList::remove`, the node is detached but NOT deleted (returned to caller).
- **`append` and `prepend` in the template list position `current` then call `insertAfter`.** They don't contain their own pointer logic — they reuse `insertAfter` after moving. If you reimplement the pointer logic in each, you'll introduce bugs.

---

## 4. HAND-CODING DRILLS

### Drill 1: Empty List State

Draw (in words) the state of a `TList<int>` immediately after construction, before any nodes are added. What does each pointer point to? What does `isEmpty()` return and why?

> [!success]- Show Answer
> ```
> head -> TNode (dummy, no value)
> tail -> TNode (dummy, no value)
> head->next = tail
> tail->next = head    (the circle!)
> current = head
> ```
> `isEmpty()` returns `1` (true) because `head->next == tail` — there are no real nodes between the two dummies.

### Drill 2: Insert Sequence Trace

Starting with an empty `TList<int>`, trace the pointer state after these operations:
```
list.prepend(10);   // step 1
list.prepend(20);   // step 2
list.append(30);    // step 3
```
For each step, show: (a) which function is called, (b) what `current` points to before `insertAfter`, (c) where the new node goes, (d) final `current` position.

> [!success]- Show Answer
> **Step 1: `prepend(10)`**
> - `goTop()` → `current = head`
> - `insertAfter(10)` → new node(10) inserted between head and tail
> - Pointers: head → node(10) → tail; tail → head
> - `current = node(10)`
>
> **Step 2: `prepend(20)`**
> - `goTop()` → `current = head` (back to head!)
> - `insertAfter(20)` → new node(20) inserted between head and node(10)
> - Pointers: head → node(20) → node(10) → tail
> - `current = node(20)`
>
> **Step 3: `append(30)`**
> - `goLast()` → walks current from head to node(10) (stops before tail)
> - `insertAfter(30)` → new node(30) inserted between node(10) and tail
> - Pointers: head → node(20) → node(10) → node(30) → tail
> - `current = node(30)`
>
> Final list order: 20, 10, 30

### Drill 3: Object-Based List — Node and Find

Write a `Book` class that inherits from `DblNode` for use in a `DblList`. A Book has an `isbn` (long). Implement:
- Constructor from ISBN
- `printOn` that prints `[Book: <isbn>]`
- `readFrom` that reads the ISBN from input
- `operator==` that compares ISBNs
- `clone()` that returns a new Book with the same ISBN (not part of DblNode, but needed for real use)

Then write code that creates a `DblList`, appends 3 books, and finds one by ISBN.

> [!success]- Show Answer
> ```cpp
> class Book : public DblNode {
>     long isbn;
> public:
>     Book() : isbn(0) {}
>     Book(long i) : isbn(i) {}
>
>     void printOn(ostream& os) const {
>         os << "[Book: " << isbn << "]";
>     }
>     void readFrom(istream& is) {
>         is >> isbn;
>     }
>     int operator==(const DblNode& n) const {
>         return isbn == ((Book&)n).isbn;
>     }
> };
>
> // Usage:
> DblList shelf;
> shelf.append(new Book(97801));
> shelf.append(new Book(97802));
> shelf.append(new Book(97803));
>
> Book key(97802);
> DblNode* found = shelf.find(key);
> if (found) cout << "Found: " << *found;
> ```
