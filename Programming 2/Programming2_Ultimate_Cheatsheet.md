---
tags: [OOP, C++, cheatsheet, exam, Programming2]
aliases: [P2 Cheatsheet, OOP Final]
created: 2026-06-22
---

# 🧠 Programming 2 — Ultimate Final Exam Cheatsheet

> [!tip] How to use this
> Scan the **Syntax Templates** first. Use **⚠️ Exam Traps** to avoid instant point losses. Use **🔥 Quick Drills** to test yourself before the exam.

---

# 📦 PART 1: OOP FOUNDATIONS (Lec3 & 5)

## Core OOP Concepts

> [!abstract] 4 Pillars
> 1. **Encapsulation** — bundle data + behavior; hide internals behind public interface
> 2. **Inheritance** — derived class acquires base class members ("is-a")
> 3. **Polymorphism** — same call → different behavior depending on runtime type
> 4. **Abstraction** — expose what, hide how

## Relationships

| Relationship | Keyword | Example |
|---|---|---|
| **IS-A** | Inheritance | `Car` is a `Vehicle` |
| **HAS-A** | Composition / member | `Car` has an `Engine` |
| **USES** | Parameter / local | `print()` uses a `Document` |

> [!warning] ⚠️ IS-A vs HAS-A Test
> Ask: "Is X actually a kind of Y?" If yes → **inherit**. If "X contains Y" → **compose**.
> `Library` DOES NOT inherit from `Book`. A library IS NOT a book.

## Object Properties (3-part definition)
An object has: **State** (data values) + **Behaviour** (methods) + **Identity** (unique name/address)

---

# 🏗️ PART 2: CLASSES IN C++ (Lec6)

## 📋 Syntax Template — Class Definition

```cpp
class ClassName {
private:
    int data;           // hidden state

protected:
    int sharedData;     // visible to derived classes only

public:
    ClassName();                        // default constructor
    ClassName(int val);                 // parameterized constructor
    ClassName(const ClassName& other);  // copy constructor
    ~ClassName();                       // destructor

    int getData() const;    // const = does NOT modify state
    void setData(int val);  // modifier

    static int getCount();  // belongs to CLASS, not object
};

// Out-of-line definition (outside class body):
int ClassName::getData() const { return data; }

// Out-of-line + inline keyword:
inline void ClassName::setData(int val) { data = val; }
```

## Access Modifiers Table

| Modifier | Same Class | Friends | Derived Classes | Outside |
|---|:---:|:---:|:---:|:---:|
| `private` | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

> [!warning] ⚠️ Access is CLASS-LEVEL, not OBJECT-LEVEL
> Two objects of the **same class** CAN access each other's `private` members inside a member function.
> ```cpp
> class Date {
>     int month;
> public:
>     Date(Date& d) { month = d.month; }  // LEGAL — same class
> };
> ```

## Constructor Rules

```cpp
class Widget {
    int val;
public:
    Widget()      { val = 0; }      // default ctor
    Widget(int v) { val = v; }      // parameterized ctor
    Widget(const Widget& w) { val = w.val; }  // copy ctor
    ~Widget() { }                   // destructor
};

// Instantiation:
Widget w1;           // stack — default ctor, auto-destroyed at scope end
Widget w2(42);       // stack — parameterized ctor
Widget* p = new Widget(10);   // HEAP — must manually delete
Widget* arr = new Widget[5];  // HEAP array — must delete[]
delete p;
delete[] arr;        // ⚠️ MUST use delete[] for arrays!
```

> [!danger] ⚠️ Auto-generation Rule
> - You define **any** constructor → compiler **STOPS** generating default ctor
> - `Widget w;` → COMPILE ERROR if only `Widget(int)` exists
> - If you write **no** ctor → compiler generates default ctor for free

## Initializer List (preferred over assignment in body)

```cpp
class Point {
    int x, y;
public:
    Point(int xv, int yv) : x(xv), y(yv) {}  // initializer list
};
```

> [!tip] Members are initialized in **DECLARATION ORDER**, not initializer list order

## `const` Member Functions

```cpp
int getX() const { return x; }   // promises not to modify any member
```

- Must use `const` on functions called from `const` objects
- Cannot call non-const functions from a const function
- `const Counter c; c.getCount();` → `getCount()` MUST be `const`

## `static` Members

```cpp
class Counter {
    static int count;      // ONE copy for ALL objects
public:
    Counter() { count++; }
    static int getCount() { return count; }
};
int Counter::count = 0;  // define outside class — REQUIRED
```

## `friend` — Bypass Access Control

```cpp
class Account {
    double balance;
public:
    friend class Bank;                  // Bank class has full access
    friend void audit(Account& a);      // single function has full access
    friend ostream& operator<<(ostream& os, const Account& a);
};
```

> [!warning] ⚠️ Friendship Rules
> - **NOT symmetric**: A friends B ≠ B friends A
> - **NOT transitive**: A friends B, B friends C ≠ A friends C
> - **NOT inherited**: friend of Base is NOT friend of Derived

## Construction / Destruction Order

```cpp
class Engine { Engine(){cout<<"E ";} ~Engine(){cout<<"~E ";} };
class Vehicle { Vehicle(){cout<<"V ";} ~Vehicle(){cout<<"~V ";} };
class Car : public Vehicle {
    Engine myEngine;
public:
    Car(){cout<<"C ";} ~Car(){cout<<"~C ";}
};
// Output: V E C ~C ~E ~V
```

> [!note] 🔑 Order Rule
> **CTOR**: Base first → members in declaration order → derived body
> **DTOR**: Derived body → members in reverse declaration order → base last
> *"Build foundation first, demolish roof first"*

---

# 🧬 PART 3: INHERITANCE (Lec7 & 8)

## 📋 Syntax Template — Inheritance

```cpp
class Derived : public Base {       // public inheritance (most common)
    int extra;
public:
    Derived(int b, int e) : Base(b), extra(e) {}  // must call Base ctor
    void display() {
        Base::display();    // call base version explicitly with ::
        cout << extra;
    }
};
```

## Inheritance Access Rules

When `class D : [specifier] B`:

| Member in B | `public` inheritance | `protected` inheritance | `private` inheritance |
|---|---|---|---|
| `public` | stays `public` | becomes `protected` | becomes `private` |
| `protected` | stays `protected` | stays `protected` | becomes `private` |
| `private` | **inaccessible** | **inaccessible** | **inaccessible** |

> [!warning] ⚠️ Private members are INHERITED but not ACCESSIBLE
> The private members exist inside the derived object's memory, but derived class code cannot directly access them.

## Three Aspects of Inheritance

| Aspect | What it means | Example |
|---|---|---|
| **Commonality** | Base captures shared data/behaviour | `Person` gives `name`, `id` to all |
| **Customization** | Derived modifies base behaviour | `SalariedEmployee` overrides `calculatePay()` |
| **Common Design Interface** | Base declares what derived MUST provide | `Shape` with pure virtual `draw()` |

## Multiple Inheritance & Diamond Problem

```cpp
// Diamond: GradAssistant → Student, Employee → Person
class Person { protected: int age; };
class Student : virtual public Person { };    // virtual = share ONE Person
class Employee : virtual public Person { };
class GradAssistant : public Student, public Employee {
public:
    GradAssistant(int a) : Person(a), Student(), Employee() {}
    //  ↑ Most-derived class MUST initialize the virtual base
};
```

### Multiple Inheritance Ambiguity

```cpp
class Scanner { public: int resolution; void start(); };
class Printer  { public: int resolution; void start(); };
class AllInOne : public Scanner, public Printer {
public:
    void setup() {
        Scanner::resolution = 600;  // ← MUST qualify
        Printer::resolution = 1200;
        Scanner::start();
        Printer::start();
    }
};
```

## Pointer Conversion in Inheritance

```cpp
// Upcast (derived* → base*) — ALWAYS safe, implicit
Student s;
Person* p = &s;      // OK — automatic

// Downcast (base* → derived*) — RISKY, needs explicit cast
Person* p2 = new Student;
Student* s2 = (Student*) p2;  // compiles, but verify it actually IS a Student!
```

---

# 🎭 PART 4: POLYMORPHISM (Lec9)

## 4 Types of Polymorphism

| #   | Type                       | Resolution   | C++ Mechanism                                |
| --- | -------------------------- | ------------ | -------------------------------------------- |
| 1   | **Overloading**            | Compile-time | Multiple functions, different signatures     |
| 2   | **Coercion**               | Compile-time | Implicit type conversion by compiler         |
| 3   | **Parametric**             | Compile-time | Templates                                    |
| 4   | **Inclusion / Overriding** | **Runtime**  | `virtual` + inheritance ← *OOP polymorphism* |

## 📋 Syntax Template — Virtual Functions

```cpp
class Shape {
public:
    virtual void draw() = 0;      // pure virtual → Shape is ABSTRACT
    virtual double area() = 0;
    virtual void rotate(double a) { cout << "Rotating"; }  // has default impl
    virtual ~Shape() { }          // ⚠️ virtual destructor MANDATORY if using base ptrs
};

class Circle : public Shape {
    double r;
public:
    Circle(double radius) : r(radius) {}
    void draw() override  { cout << "Drawing Circle"; }   // override keyword
    double area() override { return 3.14159 * r * r; }
    // rotate() — NOT overridden; inherits Shape's version
};
```

## Static vs Dynamic Binding

```cpp
Vehicle* v = new Car();
v->start();    // start() is NON-virtual → STATIC binding → always Vehicle::start
v->drive();    // drive() is virtual → DYNAMIC binding → runs Car::drive at runtime
```

> [!note] 🔑 Rule
> `virtual` = dynamic (runtime) dispatch via vtable
> No `virtual` = static (compile-time) dispatch via pointer type

## vtable / vptr Mental Model

Each class with virtual functions has a **vtable** (array of function pointers).
Each object has a hidden **vptr** pointing to its class's vtable.

```
Class A vtable: [ f1 → A::f1, f2 → A::f2 ]
Class B vtable: [ f1 → B::f1, f2 → A::f2 ]   ← B overrode f1 only

A* p = new B();
p->f1();  // lookup vptr → B's vtable → B::f1  ✅
p->f2();  // lookup vptr → B's vtable → A::f2  ✅ (B didn't override)
```

## Abstract Classes

```cpp
// A class is abstract if it has ≥ 1 pure virtual function
Shape s;         // ❌ COMPILE ERROR — can't instantiate abstract class
Shape* p;        // ✅ Pointer to abstract class is fine
Circle c(5.0);   // ✅ Circle overrides all pure virtuals → concrete
```

> [!warning] ⚠️ Abstract Trap — Partial Override
> If a derived class overrides SOME but not ALL pure virtuals, it is STILL abstract.
> ```cpp
> class Square : public Shape {
>     void draw() override { } // only draw — area() still pure virtual
>     // Square is STILL abstract! Cannot instantiate.
> };
> ```

## Virtual Destructor — MANDATORY Rule

```cpp
class Base {
public:
    virtual ~Base() { }   // ← ALWAYS add if using base class pointers
};
// Without virtual destructor:
// delete base_ptr_to_derived; → only Base's destructor runs → MEMORY LEAK
```

---

# ➕ PART 5: OVERLOADING (Lec10)

## Function Overloading

```cpp
// Same name, DIFFERENT signatures
void log(const char* msg);
void log(string msg);
void log(int code, string msg);
void log(string msg, int code);  // different ORDER — also valid

// ❌ CANNOT overload on return type alone:
// int getValue();
// double getValue();  // ERROR: redeclaration
```

> [!warning] ⚠️ Signature = name + param count + param types + param order
> Return type is **NOT** part of the signature.
> `const` on non-ref pass-by-value params does NOT distinguish overloads.
> `const` on member functions **IS** part of the signature.

## Overload Resolution Priority

**Exact match** → **Promotion** (char→int, float→double) → **Standard conversion** (int→long) → **User-defined conversion**

## Operator Overloading

```cpp
class Complex {
    double real, imag;
public:
    Complex(double r=0, double i=0) : real(r), imag(i) {}

    // Binary operator as member (left operand is *this):
    Complex operator+(const Complex& rhs) const {
        return Complex(real + rhs.real, imag + rhs.imag);
    }

    // Unary operator:
    Complex operator-() const { return Complex(-real, -imag); }

    // Prefix ++ (no extra param):
    Complex& operator++() { real++; return *this; }

    // Postfix ++ (dummy int param):
    Complex operator++(int) { Complex tmp = *this; ++(*this); return tmp; }

    // Assignment operator (handle self-assignment!):
    Complex& operator=(const Complex& rhs) {
        if (this != &rhs) { real = rhs.real; imag = rhs.imag; }
        return *this;   // ← must return *this
    }

    // Stream operators MUST be friend (left operand is ostream, not *this):
    friend ostream& operator<<(ostream& os, const Complex& c) {
        os << c.real << "+" << c.imag << "i";
        return os;   // ← must return os for chaining
    }
    friend istream& operator>>(istream& is, Complex& c) {
        is >> c.real >> c.imag;
        return is;
    }
};
```

## Operators That CANNOT Be Overloaded

| ❌ Cannot overload | Reason |
|---|---|
| `.` (member access) | Would break object.member syntax |
| `.*` (pointer-to-member) | Same |
| `::` (scope resolution) | Compile-time construct |
| `?:` (ternary) | Not a true function |

## Overloading vs Overriding — Quick Comparison

| | Overloading | Overriding (Polymorphism) |
|---|---|---|
| Parameters | **Different** | **Identical** |
| Resolution | Compile-time | **Runtime** |
| `virtual` needed | No | **Yes** (in base) |
| Inheritance needed | No | **Yes** |

---

# 🔧 PART 6: TEMPLATES (Lec11)

## 📋 Function Template Syntax

```cpp
template <class T>          // T is the type placeholder
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Usage — compiler INFERS T:
maximum(3, 7);              // T = int
maximum(3.5, 2.1);          // T = double
maximum<string>("a", "z");  // T = string (explicit)
```

## 📋 Class Template Syntax

```cpp
template <class T>
class Array {
    T* values;
    unsigned size;
public:
    Array(unsigned sz);
    ~Array();
    T& operator[](unsigned i);
};

// Member definitions outside class — MUST repeat template prefix:
template <class T>
Array<T>::Array(unsigned sz) {
    values = new T[sz];
    size = sz;
}

template <class T>
T& Array<T>::operator[](unsigned i) { return values[i]; }

// Usage:
Array<int>    ages(5);
Array<string> names(10);
```

## Multiple Template Parameters

```cpp
template <class T1, class T2>
class Pair {
    T1 first;
    T2 second;
public:
    Pair(T1 f, T2 s) : first(f), second(s) {}
    T1 getFirst() const { return first; }
    T2 getSecond() const { return second; }
};

Pair<int, string> p(42, "hello");
```

## Explicit (Non-Template) Override

```cpp
// Generic template — uses operator==
template <class T>
long indexOf(T val, const T* table, unsigned n) {
    for (unsigned i = 0; i < n; i++)
        if (val == table[i]) return i;
    return -1;
}

// Explicit override for const char* (operator== compares pointers, not content!)
long indexOf(const char* val, const char* table[], unsigned n) {
    for (unsigned i = 0; i < n; i++)
        if (strcmp(val, table[i]) == 0) return i;
    return -1;
}
// Non-template version WINS over template when both match
```

## Template Exam Traps

> [!danger] ⚠️ Template Traps
> 1. **Cannot inherit from raw template**: `class D : public Array { }` ❌ → `class D : public Array<int> { }` ✅
> 2. **Must repeat `template <class T>` prefix** for every out-of-class member definition
> 3. **Each instantiation gets its OWN static members**: `Array<int>::count ≠ Array<float>::count`
> 4. **Template must support all operators used** — if template uses `==`, your type MUST define `operator==`
> 5. **Friendship not symmetric/transitive/inherited** (same as regular classes)

---

# 🔗 PART 7: CONTAINER CLASSES — LINKED LISTS (Lec12)

## TList — Template Singly Linked List

```
head(dummy) → [10] → [20] → [30] → tail(dummy)
                              ↑ current
isEmpty() → head->next == tail
```

### Key Operations (mental model)

```cpp
// insertAfter(val) — inserts after current, current moves to new node
// Before: current → A → B
// After:  current → A → [NEW] → B, current = NEW

// append(val):
//   goLast() then insertAfter(val)  → O(n) because goLast traverses all
// prepend(val):
//   goTop() then insertAfter(val)   → O(1) because goTop just sets current = head
```

### Core TNode / TList Structure

```cpp
template <class T>
class TNode {
    friend class TList<T>;   // TList can access private members
    T value;
    TNode* next;
public:
    TNode() : next(NULL) {}
    TNode(const T& val) : value(val), next(NULL) {}
};

template <class T>
class TList {
    TNode<T>* head;     // dummy sentinel
    TNode<T>* tail;     // dummy sentinel
    TNode<T>* current;
public:
    TList() {
        head = new TNode<T>;
        tail = new TNode<T>;
        head->next = tail;
        tail->next = head;
        current = head;
    }
    ~TList() { clear(); delete head; delete tail; }
    int isEmpty() const { return head->next == tail; }
    // ... advance, get, replace, insertAfter, append, prepend, clear
};
```

## DblList — Object-Based Doubly Linked List

```
first ←→ [Node1] ←→ [Node2] ←→ [Node3] ←→ last
```

### DblNode Abstract Base

```cpp
class DblNode {
    friend class DblList;
    DblNode* next;
    DblNode* prev;
    virtual void printOn(ostream& os) const = 0;   // pure virtual
    virtual void readFrom(istream& is) = 0;         // pure virtual
public:
    DblNode() : next(NULL), prev(NULL) {}
    virtual ~DblNode() {}
    virtual int operator==(const DblNode& n) const = 0;  // pure virtual
    DblNode* detach();  // unlinks from list, does NOT delete
};
```

### Deriving from DblNode

```cpp
class Student : public DblNode {
    long id;
public:
    Student(long i) : id(i) {}
    int operator==(const DblNode& n) const {
        return id == ((Student&)n).id;  // ← MUST cast to access id
    }
    void printOn(ostream& os) const { os << id; }
    void readFrom(istream& is) { is >> id; }
};
```

## Singly vs Doubly Linked List Comparison

| Feature | TList (singly) | DblList (doubly) |
|---|---|---|
| Type safety | Template `<T>` | Polymorphism (abstract base) |
| Traversal | Forward only | Forward and backward |
| Insert before | O(n) — must find predecessor | O(1) — use `prev` pointer |
| Heterogeneous | No — all same type | Yes — any `DblNode` subclass |
| Sentinel nodes | Yes (head + tail dummy) | No sentinels |

---

# 🎨 PART 8: OO DESIGN (Lec13)

## 5-Step OOD Process

```
1. FIND CLASSES     → nouns in problem description
2. SPECIFY OPS      → verbs become methods; classify: Foundation / Selector / Modifier / Iterator
3. SPECIFY DEPS     → IS-A (inheritance) vs HAS-A (composition)
4. SPECIFY IFACE    → public vs protected; what's the minimal necessary interface?
5. REORGANIZE       → introduce common base? split responsibilities?
```

## Operation Categories

| Category | Description | Example |
|---|---|---|
| **Foundation** | Ctor, dtor, copy | `BankAccount(id, balance)` |
| **Selector** | Read state, `const` | `getBalance()` |
| **Modifier** | Change state | `deposit(amount)` |
| **Conversion** | Produce another type | `toString()` |
| **Iterator** | Traverse collection | `getStatement(dates)` |

## Noun/Verb Technique

```
Problem text:
  "The manager creates a purchase order, fills in the date, the supplier's name..."

Nouns → Classes:   Manager, PurchaseOrder, Date, Supplier
Verbs → Methods:   creates → createPurchaseOrder()
                   fills in → setDate(), setSupplier()
```

## UML Class Diagram Notation

```
┌─────────────────┐
│    ClassName     │
├─────────────────┤
│ -privateAttr     │    - = private
│ #protectedAttr   │    # = protected
│ +publicAttr      │    + = public
├─────────────────┤
│ +method()        │
│ +virtualMethod() │
└─────────────────┘

Relationships:
──────────────►    Dependency (USES)
────────────◇      Composition (HAS-A)  ◇ at the container
────────────▷      Inheritance (IS-A)   ▷ open arrow at base

Cardinality:
1        exactly one
0..1     zero or one
*  (or n) zero or more
1..*     one or more
```

---

# 🚨 MASTER EXAM TRAP LIST

> [!danger] ⚠️ TOP TRAPS — MEMORISE THESE

## Class & Objects
- `struct` defaults to `public`; `class` defaults to `private`
- Defining ANY constructor → compiler stops generating default ctor
- `Widget w;` fails if only `Widget(int)` exists
- `delete arr` vs `delete[] arr` — MUST match `new[]` with `delete[]`
- Shallow copy: compiler-generated copy ctor copies pointers, not deep data → **Rule of Three**: if you need dtor / copy ctor / assignment op, you need **all three**

## Inheritance
- Derived class CANNOT directly access base's `private` members
- Private members are inherited (exist in memory) but inaccessible by code
- Base constructor runs first, derived last; destructor exact reverse
- `Base::method()` inside derived = call base version without recursion
- Virtual base class: most-derived class MUST call virtual base ctor directly

## Polymorphism
- **No `virtual`** → static binding even through base pointer (calls base version always)
- Calling non-virtual via base pointer = base version, regardless of runtime type
- `virtual` destructor REQUIRED when deleting derived objects through base pointers
- Abstract class: cannot instantiate; even one pure virtual = abstract
- Partially overriding pure virtuals → derived is still abstract

## Overloading
- Return type is **NOT** part of the function signature
- Default args do NOT create new overloads
- `const` on member function qualifier **IS** part of signature
- `==` in line `Figure f6 = f2;` is **copy construction**, not assignment operator
- Self-assignment check in `operator=`: `if (this != &rhs) { ... }`
- `operator<<` and `operator>>` MUST be `friend` functions (left operand is `ostream`)

## Templates
- Cannot inherit from `template <class T> class X` directly — must use instantiation `X<int>`
- Every out-of-class member definition needs `template <class T>` prefix AND `ClassName<T>::`
- Each instantiation gets its own static members
- Non-template explicit override wins over template match
- `template <class T>` and `template <typename T>` are equivalent

## Linked Lists
- `head->next == tail` = empty list in TList (both are dummies)
- `detach()` unlinks but does NOT delete — caller must `delete`
- `DblNode*` parameter in `operator==` requires cast to access derived members: `((Student&)n).id`
- `delete arr` on `TList` dummies: always `clear()` first, then delete head, then delete tail
- Cannot instantiate `DblNode` — it's abstract (3 pure virtuals)

---

# ⚡ QUICK REFERENCE — COMPLETE CODE PATTERNS

## Rule of Three (for classes with dynamic memory)

```cpp
class Buffer {
    int* data;
    int size;
public:
    Buffer(int n) : size(n) { data = new int[n]; }

    // 1. DESTRUCTOR
    ~Buffer() { delete[] data; }

    // 2. COPY CONSTRUCTOR (deep copy)
    Buffer(const Buffer& other) : size(other.size) {
        data = new int[size];
        for (int i = 0; i < size; i++) data[i] = other.data[i];
    }

    // 3. ASSIGNMENT OPERATOR (deep copy + self-assign check)
    Buffer& operator=(const Buffer& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (int i = 0; i < size; i++) data[i] = other.data[i];
        }
        return *this;
    }
};
```

## Full Polymorphism Pattern

```cpp
class Animal {
public:
    virtual void speak() = 0;       // pure virtual
    virtual ~Animal() {}            // virtual destructor
};

class Dog : public Animal {
public:
    void speak() override { cout << "Woof\n"; }
};

class Cat : public Animal {
public:
    void speak() override { cout << "Meow\n"; }
};

// Polymorphic usage:
Animal* animals[2];
animals[0] = new Dog();
animals[1] = new Cat();
for (int i = 0; i < 2; i++) {
    animals[i]->speak();   // Dog: Woof, Cat: Meow — runtime dispatch
    delete animals[i];     // virtual dtor → correct cleanup
}
```

## Template Class with Operator Support

```cpp
template <class T>
class Stack {
    T data[100];
    int top;
public:
    Stack() : top(0) {}
    void push(const T& val) { data[top++] = val; }
    T pop() { return data[--top]; }
    bool isEmpty() const { return top == 0; }
};

// For custom types in templates — must overload operators the template uses:
class Student {
    long id;
public:
    Student(long i) : id(i) {}
    bool operator==(const Student& s) const { return id == s.id; }
    bool operator>(const Student& s) const { return id > s.id; }
};
```

## Constructor Chaining (Inheritance)

```cpp
class Person {
protected:
    string name;
    int age;
public:
    Person(string n, int a) : name(n), age(a) {}
    virtual void introduce() const { cout << "I am " << name; }
    virtual ~Person() {}
};

class Student : public Person {
    int studentID;
public:
    Student(string n, int a, int id) : Person(n, a), studentID(id) {}
    void introduce() const override {
        Person::introduce();               // call base version
        cout << " Student #" << studentID;
    }
};
```

---

# 🔥 EXAM-STYLE QUICK DRILLS

> [!question]- Q1: What is the output?
> ```cpp
> class A { public: A(){cout<<"A ";} ~A(){cout<<"~A ";} };
> class B { public: B(){cout<<"B ";} ~B(){cout<<"~B ";} };
> class C : public A { B b; public: C(){cout<<"C ";} ~C(){cout<<"~C ";} };
> int main() { C c; }
> ```
> > [!success]- Answer
> > `A B C ~C ~B ~A`
> > Base A first, then member B, then C body. Destruction is exact reverse.

> [!question]- Q2: Legal or Compile Error?
> ```cpp
> class Shape { public: virtual void draw() = 0; };
> class Circle : public Shape { public: void draw(){} };
> Shape s;         // (A)
> Circle c;        // (B)
> Shape* p = &c;   // (C)
> p->draw();       // (D)
> ```
> > [!success]- Answer
> > (A) ❌ ERROR — Shape is abstract
> > (B) ✅ OK — Circle overrides all pure virtuals
> > (C) ✅ OK — upcast is always safe
> > (D) ✅ OK — virtual dispatch → Circle::draw()

> [!question]- Q3: Which function is called?
> ```cpp
> void f(int a, double b)  { cout << "1"; }
> void f(double a, int b)  { cout << "2"; }
> void f(int a, int b)     { cout << "3"; }
> int main() { f(1, 2); f(1.0, 2); f(1, 2.0); }
> ```
> > [!success]- Answer
> > `f(1, 2)` → "3" (both int exact match)
> > `f(1.0, 2)` → "2" (double exact, int exact)
> > `f(1, 2.0)` → "1" (int exact, double exact)

> [!question]- Q4: Template instantiation — each class or shared?
> ```cpp
> template <class T> class Box { static int count; };
> template <class T> int Box<T>::count = 0;
> Box<int> a, b;
> Box<float> x;
> ```
> > [!success]- Answer
> > `Box<int>::count = 2`, `Box<float>::count = 1`
> > Each template instantiation has its **own** static member. They are independent.

> [!question]- Q5: `Figure f6 = f2;` — copy ctor or assignment?
> > [!success]- Answer
> > **Copy constructor**. `f6` is being **declared and initialized** in the same statement. The `=` is initialization syntax. Assignment operator would apply if `f6` already existed: `Figure f6; f6 = f2;`

> [!question]- Q6: Access through protected inheritance
> ```cpp
> class A { public: int x; protected: int y; private: int z; };
> class B : protected A { };
> class C : public B { void f() { x = 1; y = 2; z = 3; } };  // which compile?
> ```
> > [!success]- Answer
> > - `x`: A's `public` → `protected` in B → `protected` in C → ✅ accessible inside C
> > - `y`: A's `protected` → `protected` in B → `protected` in C → ✅ accessible inside C
> > - `z`: A's `private` → **inaccessible** everywhere in chain → ❌ COMPILE ERROR

---

# 📐 UML AT A GLANCE

```
Doctor's Office System Example:
                    ┌──────────────┐
              uses  │  Scheduler   │
  ┌──────────────── │ +schedule()  │ ───────────────┐ uses
  ↓                 └──────┬───────┘                ↓
┌──────────┐        1      │ uses         ┌──────────────┐
│ Patient  │               │              │   Doctor     │
│ -name    │        ┌──────┴────────┐ 1──◇│ -name        │
│ +input() │        │ DailySchedule │     │ +addAppt()   │
└──────────┘        │ +setAppt()    │     └──────────────┘
                    │ +isSlotFree() │
                    └──────┬────────┘
                     1..*  │ contains
                    ┌──────┴────────┐
                    │  Appointment  │
                    │ -timeSlot     │
                    │ -patientName  │
                    └───────────────┘
```

---

*Good luck on the exam! 🎯 Remember: read the question carefully, check access modifiers, verify virtual/non-virtual before tracing output, and always match `new[]` with `delete[]`.*
