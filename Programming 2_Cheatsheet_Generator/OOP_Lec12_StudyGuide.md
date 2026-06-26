# Lec12: Container Classes — Study Guide

---

## 1. CONCEPT CARD: CONTAINER CLASSES

### 1.1 What They Are

A **container class** is a class whose instances hold collections of other objects. This lecture focuses on **linked lists** — both **template-based singly linked lists** and **object-based doubly linked lists**. A list consists of a set of sequentially organized elements (nodes), where each node (except the first) has a single preceding node, and each node (except the last) has a single following node.

### 1.2 What Problem They Solve

Arrays are fixed-size or require manual resizing, and inserting/deleting elements in the middle is O(n) due to shifting. Linked lists solve this:
- **Dynamic sizing** — grows and shrinks as needed (dynamic memory allocation).
- **Efficient insert/delete** at any position without shifting elements (just relinking pointers).
- **Memory efficiency** — only allocate what you need, when you need it.

The tradeoff: nodes are accessed **sequentially** (no random access like arrays).

### 1.3 How They Work

1. Each element (node) stores **data** and a **pointer** to the next node (and optionally the previous node).
2. The list maintains pointers to the **head** (first element) and **tail** (last element), and optionally a **current** position pointer.
3. Operations like insert/remove work by manipulating node pointers — no data shifting required.

### 1.4 Two Approaches Covered

| Approach | Basis | Advantage |
|----------|-------|-----------|
| **Template-based** singly linked list (`TList<T>`) | Type-parameterized | Strongly typed; one list template works for all types |
| **Object-based** doubly linked list (`DblList` with `DblNode`) | Polymorphism-based (abstract base class) | Nodes of different types can coexist in the same list (via base pointers) |

### 1.5 What It Is NOT

- Linked lists are **NOT** arrays — no O(1) random access by index.
- The object-based list is **NOT** template-based — it uses inheritance and polymorphism instead of generics.
- A template is **NOT** a class — `TList` is a template, `TList<int>` is a class.

---

## 2. LISTS — FUNDAMENTAL CONCEPTS

### 2.1 Definition

A list contains **0 to n nodes**. Each element is called a **node**, and a connection between any two nodes is called a **link**. It is a specific type of graph where each node except the first has a single preceding node, and each node except the last has a single following node.

### 2.2 Operations on a List

| Operation | Description |
|-----------|-------------|
| `append` | Add a node at the end |
| `prepend` | Add a node at the beginning |
| `insert` | Insert a node at a specific position |
| `find` | Find a specific node |
| `get` | Get data at the current position |
| `replace` | Replace the content of a node |
| `isEmpty` | Check if the list is empty |
| `remove` | Remove a node |
| `clear` | Remove all nodes |

---

## 3. TEMPLATE-BASED SINGLY LINKED LIST — `TList<T>`

### 3.1 The Node — `TNode<T>`

```cpp
template <class T>
class TNode {
    friend class TList<T>;            // TList can access private members
    T value;                          // data stored in node
    TNode *next;                      // points to the next node
public:
    TNode() : next(NULL) {}           // next pointer is NULL by default
    TNode(const T &val);
    TNode<T> *getNext() const;
    template <class X>
    friend ostream & operator<<(ostream &, const TNode<X> &);
};

// Constructor with value
template <class T>
TNode<T>::TNode(const T &val) {
    value = val;
    next = NULL;
}

template <class T>
TNode<T> *TNode<T>::getNext() const { return next; }

// Overloaded << for printing a node
template <class T>
ostream & operator<<(ostream &os, const TNode<T> &node) {
    os << node.value << "->";
    return os;
}
```

**Key design decisions:**
- `TList<T>` is declared as a **friend class** — gives TList direct access to `value` and `next`.
- The node uses a **raw pointer** `TNode *next` — NOT a reference, NOT a smart pointer.
- `operator<<` is a **friend function template** with its own template parameter `<class X>` to avoid shadowing.

### 3.2 The List — `TList<T>`

```cpp
template <class T>
class TList {
    TNode<T> *head;       // dummy head node (sentinel)
    TNode<T> *tail;       // dummy tail node (sentinel)
    TNode<T> *current;    // current position pointer
public:
    TList();
    ~TList();
    int advance();                     // move current to next node
    void append(const T &nodeVal);     // add node at end
    void clear();                      // remove all nodes
    T get() const;                     // get data at current position
    void goLast();                     // set current to last node
    void goTop();                      // set current to head node
    void insertAfter(const T &nodeVal);// insert new node after current
    int isEmpty() const;               // 1 if empty, 0 otherwise
    void prepend(const T &nodeVal);    // insert at beginning
    void replace(const T &newVal);     // replace data in current node
    template <class X>
    friend ostream & operator<<(ostream &, const TList<X> &);
};
```

**Sentinel nodes**: `head` and `tail` are **dummy nodes** that contain no real data. They simplify edge-case logic:
- Empty list: `head->next == tail` (and `tail->next == head`).
- First real node is `head->next`.
- Last real node is the one whose `next == tail`.

### 3.3 Constructor and Destructor

```cpp
template <class T>
TList<T>::TList() {
    head = new TNode<T>;
    tail = new TNode<T>;
    head->next = tail;       // head points to tail (circular)?
    tail->next = head;       // tail points back to head
    current = head;
}

template <class T>
TList<T>::~TList() {
    clear();
    delete head;
    delete tail;
}
```

**Initial state**: `head` and `tail` are linked to each other. The list is empty (`head->next == tail`). `current` starts at `head`.

### 3.4 Core Operations

**isEmpty:**
```cpp
template <class T>
int TList<T>::isEmpty() const {
    return head->next == tail;   // if head's next is tail → no real nodes
}
```

**clear — remove all real nodes:**
```cpp
template <class T>
void TList<T>::clear() {
    current = head->next;
    while (current != tail) {
        head->next = current->next;
        delete current;
        current = head->next;
    }
    current = head;
    head->next = tail;          // reset to empty state
}
```

**advance — move current forward:**
```cpp
template <class T>
int TList<T>::advance() {
    if (!current) abort();
    if (current->next != tail) {
        current = current->next;
        return 1;                // successfully advanced
    }
    return 0;                    // already at last real node
}
```

**goLast / goTop:**
```cpp
template <class T>
void TList<T>::goLast() {
    if (!current) abort();
    while (current->next != tail)
        current = current->next;
}

template <class T>
void TList<T>::goTop() {
    current = head;
}
```

**get / replace:**
```cpp
template <class T>
T TList<T>::get() const {
    if (!current) abort();
    return current->value;
}

template <class T>
void TList<T>::replace(const T &newVal) {
    if (!current) abort();
    current->value = newVal;
}
```

### 3.5 Insert Operations

**insertAfter — insert a new node after current:**
```cpp
template <class T>
void TList<T>::insertAfter(const T &nodeVal) {
    if (!current) abort();
    TNode<T> *p = new TNode<T>(nodeVal);   // create new node
    p->next = current->next;                // new node points to current's next
    current->next = p;                      // current points to new node
    current = p;                            // advance current to new node
}
```

Visual:
```
Before:  current → A → B
After:   current → A → [NEW] → B
                        ↑ current now here
```

**append and prepend — convenience wrappers:**
```cpp
template <class T>
void TList<T>::append(const T &nodeVal) {
    goLast();                // move current to before tail
    insertAfter(nodeVal);    // insert after last real node
}

template <class T>
void TList<T>::prepend(const T &nodeVal) {
    goTop();                 // current = head (dummy)
    insertAfter(nodeVal);    // insert after head → first real node
}
```

### 3.6 The "Insert Before" Problem

**Inserting before current is difficult** in a singly linked list — you must search from `head` to find the node whose `next == current`, then insert after that node. This is O(n).

A doubly linked list solves this by maintaining `prev` pointers.

### 3.7 Printing the List — `operator<<`

```cpp
template <class T>
ostream & operator<<(ostream &os, const TList<T> &list) {
    if (list.isEmpty()) return os;
    TNode<T> *p = list.head->getNext();   // skip dummy head
    while (p != list.tail) {              // stop before dummy tail
        os << *p;                         // uses TNode's operator<<
        p = p->getNext();
    }
    os << endl;
    return os;
}
```

**Note**: We use `getNext()` (public) rather than `p->next` (private) because this function is not a member and accesses the list via `const` reference — though it's a friend, using the public accessor is cleaner.

---

## 4. OBJECT-BASED DOUBLY LINKED LIST — `DblList` with `DblNode`

### 4.1 Motivation — Lists with Heterogeneous Types

Template-based lists (`TList<T>`) store nodes of **one specific type**. What if you want a list containing `Student`s, `Faculty`s, and `Administrator`s together?

Solution: Object-based list with **inheritance and polymorphism**. Nodes all derive from a common abstract base class (`DblNode`), and the list stores pointers to the base class. Each derived node type can have different data while still being part of the same list.

### 4.2 The Node — `DblNode` (Abstract Base)

```cpp
class DblNode {
    friend class DblList;                    // DblList can access private members
    virtual void printOn(ostream &os) const = 0;  // pure virtual — derived MUST implement
    virtual void readFrom(istream &is) = 0;       // pure virtual — derived MUST implement
    DblNode *next;     // pointer to next node
    DblNode *prev;     // pointer to previous node
public:
    DblNode();
    virtual ~DblNode() { }
    DblNode *getNext() const;
    DblNode *getPrev() const;
    DblNode *detach();                       // detach node from its neighbors
    virtual int operator==(const DblNode &N) const = 0;  // pure virtual comparison
    friend ostream & operator<<(ostream &os, const DblNode &N);
    friend istream & operator>>(istream &inp, DblNode &N);
};
```

**Pure virtual functions**: `printOn`, `readFrom`, and `operator==` are all `= 0` — making `DblNode` an **abstract class**. You cannot instantiate a bare `DblNode`.

**Doubly linked**: Each node has both `next` and `prev` pointers.

### 4.3 DblNode Implementation

```cpp
DblNode::DblNode() { next = prev = NULL; }

DblNode *DblNode::getNext() const { return next; }
DblNode *DblNode::getPrev() const { return prev; }

DblNode *DblNode::detach() {
    if (next)                    // any next node? let it point to prev
        next->prev = prev;
    if (prev)                    // any previous node? let it point to next
        prev->next = next;
    prev = NULL;                 // detach current node from the chain
    next = NULL;
    return this;
}

ostream & operator<<(ostream &os, const DblNode &n) {
    n.printOn(os);               // polymorphic call to derived printOn()
    return os;
}

istream & operator>>(istream &is, DblNode &n) {
    n.readFrom(is);              // polymorphic call to derived readFrom()
    return is;
}
```

**`detach()`** is critical for deletion — it removes the node from the chain by bypassing it (connecting `prev` to `next`), then sets its own pointers to NULL.

### 4.4 The List — `DblList`

```cpp
class DblList {
    virtual void printOn(ostream &os) const;
    DblNode *first;    // first node in the list
    DblNode *last;     // last node in the list
    long size;         // number of elements
public:
    DblList();
    ~DblList();
    void append(DblNode *n);                   // add node to end
    void deleteAll();                          // delete all nodes
    DblNode *find(const DblNode &n) const;     // find a matching node
    DblNode *remove(DblNode *n);               // remove and return a node
    int isEmpty() const;
    DblNode *getFirst() const;
    DblNode *getLast() const;
    long getSize() const;
    friend ostream & operator<<(ostream &os, const DblList &);
};
```

**No dummy nodes** — `first` and `last` point directly to real nodes (or are NULL when empty). This is a different design choice from `TList`'s sentinel approach.

### 4.5 DblList Implementation

**Constructor / Destructor / Basic Accessors:**
```cpp
DblList::DblList() { first = NULL; last = NULL; size = 0; }
DblList::~DblList() { deleteAll(); }
int DblList::isEmpty() const { return first == NULL; }
long DblList::getSize() const { return size; }
DblNode *DblList::getFirst() const { return first; }
DblNode *DblList::getLast() const { return last; }
```

**append:**
```cpp
void DblList::append(DblNode *p) {
    if (!p) return;
    if (last) {              // is there a last node?
        last->next = p;      // yes: attach new node after it
        p->prev = last;
    } else {
        first = p;           // no: this is the first node
    }
    last = p;                // new node becomes the last
    size++;
}
```

Visual for appending to a non-empty list:
```
Before:  A ⇄ B (last=B)
After:   A ⇄ B ⇄ [NEW] (last=NEW)
```

**remove:**
```cpp
DblNode *DblList::remove(DblNode *p) {
    if (!p) return NULL;
    if (p == first)              // removing first node?
        first = first->next;     // move first forward
    if (p == last)               // removing last node?
        last = last->prev;       // move last backward
    p->detach();                 // detach from neighbors
    size--;
    return p;
}
```

**find:**
```cpp
DblNode *DblList::find(const DblNode &n) const {
    DblNode *p = first;
    while (p) {
        if (n == *p) return p;  // uses polymorphic operator== (virtual)
        p = p->next;
    }
    return 0;                    // not found
}
```

> **Note**: `n == *p` invokes `operator==`, which is **pure virtual** in `DblNode`. The derived class (e.g., `Student`) must provide the actual comparison logic. Also note: `n == *p` compares `(const DblNode &n)` with `*p`. Since the function signature receives `const DblNode &n`, it must be cast inside the derived class's `operator==`.

**printOn:**
```cpp
void DblList::printOn(ostream &os) const {
    DblNode *n = first;
    while (n) {
        os << (*n);         // polymorphic print — calls Node's operator<< → printOn()
        n = n->next;
    }
}

ostream & operator<<(ostream &os, const DblList &aList) {
    aList.printOn(os);
    return os;
}
```

### 4.6 The `current` Pointer

We can add a `current` pointer as a data member to `DblList` (just like `TList` has one). This is not in the base design but is a natural extension.

---

## 5. EXAMPLE: POLYMORPHIC LIST — Students in a College

### 5.1 Student as a DblNode

```cpp
class Student : public DblNode {
    long id;
public:
    Student() { id = 0; }
    Student(long idNum) { id = idNum; }
    void setId(long idNum) { id = idNum; }

    int operator==(const DblNode &p) const {
        return id == ((Student &)p).id;     // cast needed: p is DblNode ref
    }

    void printOn(ostream &os) const {       // override pure virtual
        os << id;
    }

    void readFrom(istream &is) {            // override pure virtual
        is >> id;
    }
};
```

### 5.2 Using Two Lists Together

```cpp
int registerStudents(TList<Student *> &classRoll, const DblList &college) {
    Student student;
    long id;
    cout << "Enter student id: ";
    cin >> id;
    if (id == -1) return 0;

    student.setId(id);
    Student *p = (Student *) college.find(student); // find in college DB
    if (p) {
        cout << "Adding student to the class roll.\n";
        classRoll.append(p);                 // add pointer to class roll
    } else
        cout << "Student not found in college list!!!\n";
    return 1;
}

int main() {
    Student *sp;
    DblList college;                         // object-based: heterogeneous possible

    for (long i = 10000; i < 10050; i++) {
        sp = new Student(i);
        college.append(sp);                  // populate college list
    }

    TList<Student *> classRoll;              // template-based: stores Student*

    cout << "Register students for a class.\n" << "(enter -1 to quit)\n\n";
    while (registerStudents(classRoll, college))
        continue;

    cout << "Finished.\n" << classRoll << endl;
    return 0;
}
```

**Design insight**: `DblList` stores heterogeneous objects (all derive from `DblNode`). `TList<Student*>` is a **template-based list of pointers** — it stores `Student*` values. The two list types serve different purposes and can interoperate.

---

## 6. TList vs DblList — COMPARISON

| Aspect | `TList<T>` | `DblList` |
|--------|-----------|-----------|
| Node type | Template parameter `T` | `DblNode` abstract base |
| Link direction | Singly linked (`next` only) | Doubly linked (`next` + `prev`) |
| Sentinel nodes | Yes (dummy head + tail) | No (NULL-terminated) |
| Homogeneous/heterogeneous | Homogeneous (all nodes same type) | Heterogeneous (mixed derived types) |
| Polymorphism | No — compile-time via templates | Yes — runtime via virtual functions |
| Insert before current | Hard (O(n)) — must search from head | Easy (O(1)) — follow `prev` pointer |
| `current` pointer | Yes | Optional (not in base design) |
| Node comparison | Uses `operator==` on type `T` | Uses pure virtual `operator==` |

---

## 7. MUST-MEMORIZE SYNTAX TEMPLATES

### 7.1 TNode Declaration

```cpp
template <class T>
class TNode {
    friend class TList<T>;
    T value;
    TNode *next;
public:
    TNode() : next(NULL) {}
    TNode(const T &val);
    TNode<T> *getNext() const;
};
```

### 7.2 TList Core Structure

```cpp
template <class T>
class TList {
    TNode<T> *head;      // dummy
    TNode<T> *tail;      // dummy
    TNode<T> *current;   // position
public:
    TList();
    ~TList();
    void append(const T &val);
    void prepend(const T &val);
    void insertAfter(const T &val);
    void clear();
    int isEmpty() const;
    int advance();
    T get() const;
    void replace(const T &val);
    void goLast();
    void goTop();
};
```

### 7.3 TList Constructor (Sentinel Pattern)

```cpp
template <class T>
TList<T>::TList() {
    head = new TNode<T>;
    tail = new TNode<T>;
    head->next = tail;
    tail->next = head;
    current = head;
}
```

### 7.4 TList::insertAfter

```cpp
template <class T>
void TList<T>::insertAfter(const T &nodeVal) {
    TNode<T> *p = new TNode<T>(nodeVal);
    p->next = current->next;
    current->next = p;
    current = p;
}
```

### 7.5 DblNode Abstract Base

```cpp
class DblNode {
    friend class DblList;
    virtual void printOn(ostream &os) const = 0;
    virtual void readFrom(istream &is) = 0;
    DblNode *next;
    DblNode *prev;
public:
    DblNode();
    virtual ~DblNode() {}
    DblNode *getNext() const;
    DblNode *getPrev() const;
    DblNode *detach();
    virtual int operator==(const DblNode &N) const = 0;
};
```

### 7.6 DblList Core Structure

```cpp
class DblList {
    DblNode *first;
    DblNode *last;
    long size;
public:
    DblList();
    ~DblList();
    void append(DblNode *n);
    DblNode *remove(DblNode *n);
    DblNode *find(const DblNode &n) const;
    void deleteAll();
    int isEmpty() const;
    long getSize() const;
};
```

### 7.7 DblList::append

```cpp
void DblList::append(DblNode *p) {
    if (!p) return;
    if (last) {
        last->next = p;
        p->prev = last;
    } else {
        first = p;
    }
    last = p;
    size++;
}
```

### 7.8 DblList::remove

```cpp
DblNode *DblList::remove(DblNode *p) {
    if (!p) return NULL;
    if (p == first) first = first->next;
    if (p == last) last = last->prev;
    p->detach();
    size--;
    return p;
}
```

### 7.9 DblNode::detach

```cpp
DblNode *DblNode::detach() {
    if (next) next->prev = prev;
    if (prev) prev->next = next;
    prev = NULL;
    next = NULL;
    return this;
}
```

---

## 8. EXAM TRAPS

### Trap 1: `head->next == tail` Means the List Is Empty (in TList)
In `TList`, both `head` and `tail` are dummy nodes. An empty list has `head->next == tail`. Don't confuse this with value-holding nodes.

### Trap 2: `insertBefore` Is Difficult in a Singly Linked List
To insert before `current` in `TList`, you must traverse from `head` to find the predecessor (O(n)). There is no `prev` pointer. Use doubly linked lists if you need frequent before-insertion.

### Trap 3: Forgetting the Template Prefix on Member Definitions
```cpp
// ERROR — needs template prefix and <T>
// TList::TList() { ... }

// CORRECT:
template <class T>
TList<T>::TList() { ... }
```
Every member definition outside the class MUST be preceded by `template <class T>` and use `ClassName<T>::`.

### Trap 4: `DblNode` Is Abstract — Cannot Instantiate Directly
```cpp
DblNode n;               // ERROR — pure virtual functions (printOn, readFrom, operator==)
DblNode *p = new Student(12345);  // OK — Student is concrete
```

### Trap 5: `operator==` in `DblNode` Requires Casting
Inside `Student::operator==`, the parameter is `const DblNode &p`. To access `id`, you must cast: `((Student &)p).id`. Without the cast → compile error.

### Trap 6: `detach()` Does NOT `delete` the Node — Just Unlinks It
`detach()` removes the node from the chain but does NOT free memory. The caller (`DblList::remove`, `deleteAll`) is responsible for `delete`.

### Trap 7: Destroying a List with Dummy Nodes — Delete Dummies After Clearing
```cpp
~TList() {
    clear();         // delete all real nodes first
    delete head;     // then delete the dummy nodes
    delete tail;
}
```
Deleting dummies before real nodes would create dangling pointers.

### Trap 8: Polymorphism in `DblList` — `operator<<` Calls `printOn()` Virtually
`os << (*n)` where `n` is `DblNode*` calls `operator<<(ostream&, const DblNode&)`, which calls `n.printOn(os)`. Since `printOn` is virtual, the correct derived version runs. This is how heterogeneous lists print correctly.

### Trap 9: Templates Generate Separate Code per Type
`TList<int>` and `TList<float>` are completely separate classes — separate code, separate static members, separate vtables. They share only the template source code.

---

## 9. HAND-CODING DRILLS

### Drill 1: Trace TList Insertion

```cpp
TList<int> list;
list.append(10);
list.append(20);
list.prepend(5);
```

Trace the list contents after each operation. Draw the node chain.

> [!success]- Show Answer
> After `append(10)`: head → 10 → tail (current at 10)
> After `append(20)`: head → 10 → 20 → tail (current moves to last then inserts after)
> After `prepend(5)`: head → 5 → 10 → 20 → tail (insert after head)
>
> Final: head(dummy) → 5 → 10 → 20 → tail(dummy)

### Drill 2: Write DblList::deleteAll

```cpp
// TODO: Implement deleteAll — remove and delete ALL nodes from the list
void DblList::deleteAll() {
    // ...
}
```

> [!success]- Show Answer
> ```cpp
> void DblList::deleteAll() {
>     DblNode *p = first;
>     while (p) {
>         DblNode *next = p->getNext();
>         delete p;
>         p = next;
>     }
>     first = NULL;
>     last = NULL;
>     size = 0;
> }
> ```

### Drill 3: Derive Faculty from DblNode

Implement a `Faculty` class that inherits from `DblNode` with members `string name` and `string department`. Override `printOn`, `readFrom`, and `operator==`.

> [!success]- Show Answer
> ```cpp
> class Faculty : public DblNode {
>     string name;
>     string department;
> public:
>     Faculty() {}
>     Faculty(string n, string d) : name(n), department(d) {}
>
>     int operator==(const DblNode &n) const {
>         const Faculty &f = (const Faculty &)n;
>         return name == f.name && department == f.department;
>     }
>
>     void printOn(ostream &os) const {
>         os << name << " (" << department << ")";
>     }
>
>     void readFrom(istream &is) {
>         is >> name >> department;
>     }
> };
> ```

### Drill 4: Trace DblList Removal

```cpp
DblList list;
list.append(new Student(100));
list.append(new Student(200));
list.append(new Student(300));

Student s(200);
DblNode *found = list.find(s);
list.remove(found);   // Note: remove does NOT delete — just unlinks
```

What does the list look like after removal? What is `first`? What is `last`? What is `size`?

> [!success]- Show Answer
> List: Student(100) ⇄ Student(300). `first` points to 100, `last` points to 300, `size` = 2.
>
> `found` (pointing to Student(200)) is now detached (prev=NULL, next=NULL) but NOT deleted — memory leak if not explicitly `delete`d by the caller.
>
> **Note**: The `remove` operation returns the detached node but does NOT `delete` it. The caller must manage the memory.

### Drill 5: Append and Prepend in TList — Are They Efficient?

Explain why `append` in `TList` (which calls `goLast()` then `insertAfter`) is O(n) while `prepend` (which calls `goTop()` then `insertAfter`) is O(1).

> [!success]- Show Answer
> `goLast()` traverses the entire list from `head` to find the node whose `next == tail` — O(n). `goTop()` simply sets `current = head` — O(1). Therefore, `append` is O(n) and `prepend` is O(1) in this implementation.
>
> To make `append` O(1), you could maintain a `last` pointer that directly identifies the last real node (like `DblList` does). Since `tail` is a dummy in `TList`, you'd need to track the node before `tail`.

---

> [!NOTE]
> This study guide covers all lecture content for Lec12: Container Classes. Master both the template-based singly linked list (`TList<T>` with sentinel nodes) and the object-based doubly linked list (`DblList` / `DblNode` with polymorphism). Be able to trace insert/remove operations and understand the tradeoffs between the two approaches.
