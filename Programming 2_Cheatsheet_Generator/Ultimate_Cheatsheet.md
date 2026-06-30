# 🔥 ULTIMATE PROGRAMMING 2 CHEATSHEET 🔥
## OOP in C++ — Theory + Paper-Coding — Ace Every Question

---

# ═══════════════════════════════════════════════════
# SECTION 0: THE 4 PILLARS OF OOP (THEORY)
# ═══════════════════════════════════════════════════

| Pillar | Meaning | C++ How |
|--------|---------|---------|
| **Abstraction** | Hide complexity; show only WHAT, not HOW | `private` members, ADTs, `virtual` functions |
| **Encapsulation** | Bundle data + methods together | Class definition (`private` data + `public` methods) |
| **Inheritance** | "is-a" — child gets parent's stuff | `class D : public B { };` |
| **Polymorphism** | Same call, different behavior by object type | `virtual` + override + base pointer/reference |

**Abstraction ≠ Encapsulation**: Abstraction = hiding details (WHAT vs HOW). Encapsulation = bundling (WHERE). You can encapsulate without abstracting.

---

# ═══════════════════════════════════════════════════
# SECTION 1: CLASS BASICS (Lec3, Lec5, Lec6)
# ═══════════════════════════════════════════════════

## 🔑 CLASS SYNTAX TEMPLATE (MEMORIZE THIS)

```cpp
class ClassName {
private:                          // hidden data
    int data1;
    double data2;
public:                           // public interface
    ClassName(int d1, double d2);  // constructor
    int getData1() const;          // selector (const = won't modify)
    void setData2(double val);     // modifier
};  // ← SEMICOLON MANDATORY — forget this = LOSE MARKS
```

## 🔑 OBJECT LIFECYCLE

```
Class (blueprint) → constructor() → object BORN → methods called → destructor() → object DEAD
```

- Each object gets ITS OWN copy of data members
- All objects SHARE one copy of method code (efficiency)
- `static` members are the exception — SHARED across all objects

## 🔑 CONSTRUCTORS — 4 TYPES

```cpp
class Point {
    int x, y;
public:
    Point() { x = 0; y = 0; }                       // DEFAULT: no params
    Point(int xVal, int yVal) { x = xVal; y = yVal; } // PARAMETERIZED
    Point(const Point& other) { x = other.x; y = other.y; } // COPY ctor
};
Point p;              // default ctor
Point p2(5, 10);      // parameterized ctor
Point p3 = p2;        // COPY ctor (NOT assignment — p3 is NEW!)
Point p4(p2);         // COPY ctor (direct syntax)
```

**GOLDEN RULE**: If you define ANY constructor, compiler does NOT generate default ctor → `Point p;` fails if no default ctor written.

## 🔑 DESTRUCTOR

```cpp
~ClassName() { /* cleanup: delete[] dynamic memory */ }
```
- Only ONE destructor (no params → can't overload)
- Called automatically: stack object goes out of scope OR `delete` on heap object
- **VIRTUAL destructor if class is base class** (see Section 5)

## 🔑 INSTANTIATION: STATIC vs DYNAMIC

```cpp
Point p(5, 10);                     // STATIC: stack, auto-destroyed
Point* pp = new Point(5, 10);       // DYNAMIC: heap, MUST delete
delete pp;                          // single delete
Point* arr = new Point[10];         // array of 10
delete[] arr;                       // ARRAY delete — wrong match = CRASH
```

## 🔑 ACCESS CONTROL TABLE

| Access | Same Class | Friends | Derived Class | Outside |
|--------|:----------:|:-------:|:-------------:|:-------:|
| `public` | ✅ | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `private` | ✅ | ✅ | ❌ | ❌ |

**CRITICAL**: Access is per-CLASS, not per-OBJECT. Inside `Point::copy(const Point& other)`, you CAN access `other.x` even though `x` is private — because both are `Point`.

```cpp
class Point {
    int x, y;
public:
    void copy(const Point& other) {
        x = other.x;  // LEGAL! Same class access
        y = other.y;  // LEGAL!
    }
};
```

## 🔑 INLINE vs OUT-OF-LINE

```cpp
class Point {
public:
    void setX(int val) { x = val; }   // IN-LINE (inside class → implicitly inline)
    void setY(int val);               // OUT-OF-LINE (declared only)
};
void Point::setY(int val) { y = val; } // OUT-OF-LINE definition
```

## 🔑 const MEMBER FUNCTIONS

```cpp
int getX() const { return x; }  // const = "I promise not to modify *this"
```
- `const` goes AFTER parameter list
- `const` object can ONLY call `const` methods
- Cannot modify any data member inside `const` method (except `mutable`)

## 🔑 DEEP COPY vs SHALLOW COPY (MEGA IMPORTANT)

```cpp
// SHALLOW copy: copies pointer → two objects share same dynamic memory → DOUBLE DELETE!
// DEEP copy: allocates new memory → each object has own copy → safe

class Array {
    int* data;
    int len;
public:
    Array(int l) : len(l) { data = new int[len]; }
    
    Array(const Array& other) : len(other.len) {    // DEEP COPY ctor
        data = new int[len];                          // 1. Allocate NEW memory
        for (int i = 0; i < len; i++) data[i] = other.data[i]; // 2. Copy
    }
    
    ~Array() { delete[] data; }
};
```

**Rule of Three**: If you need destructor (cleanup dynamic memory), you likely also need custom copy constructor AND copy assignment operator.

## 🔑 COMPOSITE CLASS CONSTRUCTION ORDER

```cpp
class A { public: A() { cout << "A "; } ~A() { cout << "~A "; } };
class B { public: B() { cout << "B "; } ~B() { cout << "~B "; } };
class C : public A {
    B member;
public:
    C() { cout << "C "; }
    ~C() { cout << "~C "; }
};
// Output: A B C ~C ~B ~A
// Rule: Base ctor → Members (declaration order) → Body
//       Destructors: EXACT REVERSE
```

---

# ═══════════════════════════════════════════════════
# SECTION 2: INHERITANCE (Lec7, Lec8)
# ═══════════════════════════════════════════════════

## 🔑 INHERITANCE SYNTAX

```cpp
class Derived : public Base {   // public inheritance (most common)
    // additional members
};
// Also: protected Base, private Base (default for class)
```

## 🔑 INHERITANCE ACCESS SPECIFIER EFFECTS

| Inheritance Type | Base `public` → | Base `protected` → | Base `private` → | Outsider access? |
|:---:|:---:|:---:|:---:|:---:|
| **public** | `public` | `protected` | inaccessible | YES (to was-public) |
| **protected** | `protected` | `protected` | inaccessible | NO |
| **private** | `private` | `private` | inaccessible | NO |

**Mnemonic**: Inheritance specifier CAPS the max access. `private` inheritance cuts off everything for grandchildren.

## 🔑 CONSTRUCTOR INITIALIZER — REQUIRED when base has NO default ctor

```cpp
class Vehicle { int speed; public: Vehicle(int s) : speed(s) {} }; // NO DEFAULT
class Car : public Vehicle {
    int doors;
public:
    Car(int s, int d) : Vehicle(s), doors(d) {}  // MUST call base ctor
};
```

## 🔑 POINTER CONVERSION RULES

```cpp
Derived d;
Base* bp = &d;              // ✅ Upcast — IMPLICIT, always safe
Derived* dp = bp;           // ❌ Downcast — ERROR, no implicit
Derived* dp = (Derived*)bp; // ⚠️ C-cast — compiles but RISKY (may be wrong type)
Derived* dp = dynamic_cast<Derived*>(bp); // safest — nullptr if wrong
```

## 🔑 OVERRIDING (name hiding)

```cpp
class Base { public: void display() { } };
class Derived : public Base {
public:
    void display() { }               // hides Base::display()
    void test() {
        display();                   // calls Derived::display()
        Base::display();             // calls Base::display() — scope resolution
    }
};
```
Without `Base::`, calling `display()` calls itself → infinite recursion!

## 🔑 MULTIPLE INHERITANCE — AMBIGUITY

```cpp
class A : public B1, public B2 {
public:
    void setup() {
        B1::x = 5;         // MUST disambiguate! C++ has NO "first in list wins"
        B2::x = 10;        // Without scope resolution → COMPILE ERROR
    }
};
```

## 🔑 DIAMOND PROBLEM + VIRTUAL BASE CLASSES

```
    Person
   virtual virtual
   /              \
Student          Employee
   \              /
  GradAssistant
```

```cpp
class Student : virtual public Person { ... };
class Employee : virtual public Person { ... };
class GradAssistant : public Student, public Employee {
public:
    GradAssistant(...) : Person(...), Student(...), Employee(...) { }
    // MOST-DERIVED class MUST initialize virtual base!
    // Person() calls in Student/Employee ctors are IGNORED
};
```

**Without virtual**: TWO copies of Person → ambiguous `setName()`. **With virtual**: ONE shared Person → no ambiguity.

## 🔑 CONSTRUCTOR / DESTRUCTOR ARE NOT INHERITED

Derived class must define its own constructors, destructor, copy ctor, assignment operator.

## 🔑 RELATIONSHIP TYPES

| Relationship | Meaning | C++ |
|-------------|---------|-----|
| **IS-A** | Inheritance | `class D : public B` |
| **HAS-A** | Composition | Member object: `Engine e;` |
| **USES** | Dependency | Method parameter or pointer |

---

# ═══════════════════════════════════════════════════
# SECTION 3: POLYMORPHISM (Lec9) — THE BIG ONE
# ═══════════════════════════════════════════════════

## 🔑 VIRTUAL FUNCTIONS — THE KEY CONCEPT

```cpp
class Shape {
public:
    virtual void draw() { cout << "Shape\n"; }    // VIRTUAL → dynamic binding
    virtual ~Shape() { }                           // VIRTUAL destructor — ALWAYS!
    void print() { cout << "print\n"; }            // NON-virtual → static binding
};

class Circle : public Shape {
public:
    void draw() override { cout << "Circle\n"; }  // override (C++11 keyword)
    ~Circle() { }
};
```

## 🔑 STATIC vs DYNAMIC BINDING — EXAM GOLD

```cpp
Shape* p = new Circle();
p->draw();    // "Circle"  — draw() is virtual → dynamic binding → vtable lookup
p->print();   // "print"   — print() is non-virtual → static binding → Shape::print()
```

| | Static Binding | Dynamic Binding |
|---|---|---|
| When resolved | Compile time | Runtime (via vtable) |
| Uses | non-virtual functions | `virtual` functions |
| Based on | Pointer type (`Shape*`) | Actual object type (`Circle`) |
| Speed | Faster | Slightly slower |
| C++ default | YES | Only with `virtual` |

## 🔑 PURE VIRTUAL → ABSTRACT CLASS

```cpp
class Shape {
public:
    virtual void draw() = 0;     // pure virtual → Shape is ABSTRACT
    virtual double area() = 0;   // another pure virtual
    virtual ~Shape() { }
};
// Shape s;             // ❌ ERROR — cannot instantiate abstract class
Shape* p = new Circle(); // ✅ OK — pointer to abstract class is fine!
```

- Abstract class = has ≥1 pure virtual function (`= 0`)
- Derived class MUST override ALL pure virtuals to become CONCRETE
- If derived misses even ONE pure virtual → still abstract

## 🔑 VIRTUAL DESTRUCTOR — CRITICAL

```cpp
class Base {
    int* data;
public:
    Base() { data = new int[100]; }
    virtual ~Base() { delete[] data; }  // ← MUST be virtual
};

class Derived : public Base {
    char* buf;
public:
    Derived() { buf = new char[1024]; }
    ~Derived() { delete[] buf; }
};

Base* p = new Derived();
delete p;  // Without virtual ~Base(): only ~Base() runs → buf LEAKED!
           // With virtual ~Base(): ~Derived() runs → ~Base() runs → all cleaned
```

**Rule**: If a class has ANY virtual function, its destructor MUST be virtual. Always.

## 🔑 FOUR TYPES OF POLYMORPHISM

| # | Type | Resolution | C++ Mechanism |
|---|------|-----------|---------------|
| 1 | Overloading | Compile-time | Same name, different params |
| 2 | Coercion | Compile-time | Implicit type conversion |
| 3 | Parametric | Compile-time | Templates |
| 4 | Inclusion/Overriding | Runtime | `virtual` + inheritance |

**Polymorphism in OOP context = #4 (Inclusion/Overriding)**

## 🔑 OVERRIDE vs OVERLOAD — TRAP

| | Override | Overload |
|---|---|---|
| Parameters | **SAME** signature | **DIFFERENT** parameters |
| Resolution | Runtime (vtable) | Compile-time |
| `virtual` | Required in base | Not relevant |
| Inheritance | Required | Not required |

```cpp
class Base { public: virtual void foo(int x); };
class Derived : public Base {
public:
    void foo(int x) override;   // OVERRIDE — same (int)
    void foo(double x);         // OVERLOAD — different (double), NOT an override!
};
```

## 🔑 THE `this` POINTER

```cpp
void Point::setX(int x) {
    this->x = x;   // this->x = member, x = parameter
}
```
- `this` is an implicit pointer to the current object
- In virtual functions, `this` points to the ACTUAL derived object

## 🔑 VTABLE MECHANISM

```
Object           Class Vtable
┌────────┐      ┌─────────────────┐
│  vptr  │─────>│ &Derived::f1()  │
│  data  │      │ &Derived::f2()  │
└────────┘      │ &Derived::~D()  │
                └─────────────────┘
```
Every call `p->virtualFunc()`: follow vptr → index vtable → call function.

## 🔑 SLICING — PASS BY VALUE KILLS POLYMORPHISM

```cpp
void bad(Shape s) { s.draw(); }    // SLICES — only Shape part copied
void good(Shape& s) { s.draw(); }  // CORRECT — full object preserved
```
Always pass polymorphic objects by **pointer** or **reference**.

---

# ═══════════════════════════════════════════════════
# SECTION 4: OVERLOADING (Lec10)
# ═══════════════════════════════════════════════════

## 🔑 FUNCTION OVERLOADING

```cpp
void swap(int &a, int &b)    { int t=a; a=b; b=t; }
void swap(float &a, float &b){ float t=a; a=b; b=t; }
void swap(char &a, char &b)  { char t=a; a=b; b=t; }
// Same name, DIFFERENT parameter types → compiler picks best match at compile time
```

**SIGNATURE = name + (param count, types, order)** — Return type is NOT part of signature!

```cpp
int  getValue();     // OK
// double getValue(); // ❌ ERROR — same signature, different return type only
```

## 🔑 COERCION — Auto Type Conversion

```cpp
void f(int x);  void f(float x);
double d = 3.14;
f(d);  // ❌ AMBIGUOUS! double matches both int and float equally
f(static_cast<int>(d));  // ✅ Explicit cast resolves ambiguity
```

**Conversion ranking**: Exact match > Promotion (char→int) > Standard conversion (int→long, double→float) > User-defined conversion

## 🔑 OPERATOR OVERLOADING — SYNTAX

```cpp
class Complex {
    double re, im;
public:
    Complex operator+(const Complex& other) const {  // MEMBER binary operator
        return Complex(re + other.re, im + other.im);
    }
    Complex& operator++() { ++re; return *this; }     // PREFIX ++
    Complex operator++(int) {                         // POSTFIX ++ (dummy int)
        Complex old = *this; ++re; return old;
    }
    friend ostream& operator<<(ostream& os, const Complex& c) { // FRIEND for <<
        os << c.re << "+" << c.im << "i"; return os;
    }
};
```

## 🔑 PREFIX vs POSTFIX

| | Prefix `++x` | Postfix `x++` |
|---|---|---|
| Signature | `T& operator++()` | `T operator++(int)` |
| Returns | Reference (no copy) | Value (copy old state) |
| Chaining | `++(++x)` OK | `(x++)++` counterintuitive |

**Dummy `int`**: `operator++(int)` — the `int` is NEVER USED. It exists ONLY to make the signature different from the prefix version. When you write `x++`, compiler passes a dummy 0.

## 🔑 ASSIGNMENT OPERATOR vs COPY CONSTRUCTOR

```cpp
MyClass a;
MyClass b = a;   // COPY CONSTRUCTOR — b is NEW (the = here is initialization!)
b = a;           // ASSIGNMENT OPERATOR — b already exists
```

### Assignment Operator Full Pattern:
```cpp
MyClass& operator=(const MyClass& other) {
    if (this != &other) {           // 1. Self-assignment guard
        delete[] data;              // 2. Free old memory
        data = new int[other.size]; // 3. Allocate new
        size = other.size;          // 4. Copy data
        for (int i = 0; i < size; i++) data[i] = other.data[i];
    }
    return *this;                   // 5. Return ref for chaining (a = b = c)
}
```

## 🔑 OPERATORS THAT CANNOT BE OVERLOADED (4 ONLY)

| `.` | `.*` | `::` | `?:` |
|-----|------|------|------|

Everything else (`+`, `-`, `*`, `/`, `=`, `==`, `<`, `>`, `<<`, `>>`, `[]`, `()`, `->`, `new`, `delete`, etc.) CAN be overloaded.

**Also cannot**: change precedence, associativity, arity; use default args; invent new operators.

## 🔑 OVERLOAD RESOLUTION — BEST MATCH PRINCIPLE

```cpp
void f(int, double);  // v1
void f(double, int);  // v2

f(1, 2.0);    // v1 — exact match on first, exact on second → v1 wins
f(1.0, 2);    // v2 — exact match on first, exact on second → v2 wins
f(1, 1);      // ❌ AMBIGUOUS — both need one conversion → tie
f(1.0, 2.0);  // ❌ AMBIGUOUS — both need one conversion → tie
```

---

# ═══════════════════════════════════════════════════
# SECTION 5: TEMPLATES (Lec11)
# ═══════════════════════════════════════════════════

## 🔑 FUNCTION TEMPLATE

```cpp
template <class T>                    // OR template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}
// Usage: maximum(3, 7) → T=int; maximum(3.5, 2.1) → T=double
// Compiler generates SEPARATE code for each type at COMPILE TIME
```

## 🔑 CLASS TEMPLATE

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

// OUTSIDE DEFINITIONS: MUST prefix with template<class T> and use <T>
template <class T>
Array<T>::Array(unsigned sz) { values = new T[sz]; size = sz; }

template <class T>
T& Array<T>::operator[](unsigned i) { return values[i]; }

// Usage:
Array<int> ages(5);     // T=int
Array<string> names(5); // T=string
```

## 🔑 TEMPLATES + STATIC MEMBERS

```cpp
template <class T> class Counter { static int count; };
template <class T> int Counter<T>::count = 0;

Counter<int> a, b;      // Counter<int>::count = 2
Counter<float> c;       // Counter<float>::count = 1 (SEPARATE!)
// Each instantiation gets its OWN static members!
```

## 🔑 TEMPLATE ≠ CLASS

```cpp
// class D : public Array { };   // ❌ ERROR — template is not a class
class D : public Array<int> { };  // ✅ CORRECT — Array<int> IS a class
```

## 🔑 EXPLICIT OVERRIDE OF TEMPLATE

```cpp
template <class T>
long indexOf(T val, const T* table, unsigned size) { /* uses == */ }

// C-strings need strcmp, not == (which compares pointers!)
long indexOf(const char* val, const char* table[], unsigned size) { /* uses strcmp */ }
// Non-template version takes PRIORITY over template for exact matches
```

## 🔑 FRIEND CLASS / FUNCTION

```cpp
class A {
    int secret;
    friend class B;                    // B gets full access to A
    friend void peek(A& a);            // peek() gets full access to A
    friend ostream& operator<<(ostream&, const A&); // for stream output
};
```

**Three "NOTs" of friendship**:
- NOT symmetrical (A friends B ≠ B friends A)
- NOT transitive (A friends B, B friends C ≠ A friends C)
- NOT inherited (derived classes don't inherit base's friends)

---

# ═══════════════════════════════════════════════════
# SECTION 6: LINKED LISTS (Lec12)
# ═══════════════════════════════════════════════════

## 🔑 SINGLY LINKED LIST (Template-based: TList<T>)

```cpp
template <class T>
class TNode {
    friend class TList<T>;
    T value;
    TNode* next;
public:
    TNode() : next(nullptr) {}
    TNode(const T& val) : value(val), next(nullptr) {}
};

template <class T>
class TList {
    TNode<T> *head, *tail, *current;  // head/tail are DUMMY (sentinel) nodes
public:
    TList() {
        head = new TNode<T>; tail = new TNode<T>;
        head->next = tail; tail->next = head; current = head;
    }
    int isEmpty() const { return head->next == tail; }
    
    void insertAfter(const T& val) {
        TNode<T>* p = new TNode<T>(val);
        p->next = current->next;
        current->next = p;
        current = p;
    }
    void append(const T& val)  { goLast(); insertAfter(val); }   // O(n)
    void prepend(const T& val) { goTop();  insertAfter(val); }   // O(1)
    
    void clear() {
        current = head->next;
        while (current != tail) {
            head->next = current->next;
            delete current;
            current = head->next;
        }
        current = head;
        head->next = tail;
    }
    ~TList() { clear(); delete head; delete tail; }
};
```

**Empty list check**: `head->next == tail` (sentinel nodes point to each other)

## 🔑 DOUBLY LINKED LIST (Object-based: DblList)

```cpp
class DblNode {
    friend class DblList;
    virtual void printOn(ostream& os) const = 0;   // pure virtual
    virtual void readFrom(istream& is) = 0;
    DblNode *next, *prev;
public:
    DblNode() { next = prev = nullptr; }
    virtual ~DblNode() { }
    DblNode* getNext() const { return next; }
    DblNode* detach() {
        if (next) next->prev = prev;
        if (prev) prev->next = next;
        prev = next = nullptr;
        return this;
    }
    virtual int operator==(const DblNode&) const = 0;
};

class DblList {
    DblNode *first, *last;
    long size;
public:
    DblList() { first = last = nullptr; size = 0; }
    
    void append(DblNode* p) {
        if (!p) return;
        if (last) { last->next = p; p->prev = last; }
        else first = p;
        last = p; size++;
    }
    
    DblNode* remove(DblNode* p) {
        if (!p) return nullptr;
        if (p == first) first = first->next;
        if (p == last)  last = last->prev;
        p->detach(); size--;
        return p;   // NOTE: does NOT delete — caller must manage memory!
    }
    
    DblNode* find(const DblNode& n) const {
        DblNode* p = first;
        while (p) { if (n == *p) return p; p = p->next; }
        return nullptr;
    }
};
```

## 🔑 TList vs DblList Comparison

| | TList<T> | DblList |
|---|---|---|
| Link type | Singly (next only) | Doubly (next + prev) |
| Dummy nodes | Yes (head, tail) | No |
| Type safety | Templates (compile-time) | Polymorphism (runtime) |
| Heterogeneous | No (same T) | Yes (mixed derived types) |
| Insert before | O(n) | O(1) via prev |

---

# ═══════════════════════════════════════════════════
# SECTION 7: OO DESIGN (Lec13)
# ═══════════════════════════════════════════════════

## 🔑 THE 5 DESIGN STEPS

```
1. Find CLASSES      → Nouns in problem description
2. Specify OPERATIONS → Verbs (Foundation, Selectors, Modifiers, Iterators, Conversion)
3. Specify DEPENDENCIES → IS-A (inheritance), HAS-A (composition), USES (link)
4. Specify INTERFACES → public vs protected, exact types
5. REORGANIZE hierarchy → introduce common base, split classes
```

## 🔑 OPERATION CATEGORIES

| Category | Description | Example |
|----------|-------------|---------|
| Foundation | Constructor, destructor | `Student()`, `~Student()` |
| Selector | Doesn't modify state (const) | `getBalance() const` |
| Modifier | Modifies state | `deposit(amount)` |
| Conversion | Produce another type | `toString()` |
| Iterator | Traverse collections | `getNext()` |

## 🔑 UML NOTATION

```
┌──────────────────┐       △───────  Inheritance (triangle → base)
│   ClassName      │       ◇───────  Composition/contains (diamond → container)
├──────────────────┤       ────────  Association/uses
│  - privateAttr   │
│  # protectedAttr │       Cardinality: 1, 0..1, 1..*, *, 0..n
│  + publicAttr    │
├──────────────────┤       Object: rectangle with UNDERLINED name
│  + operation()   │
│  - helper()      │
└──────────────────┘
```

## 🔑 NOUN/VERB TECHNIQUE

Problem description → underline NOUNS (candidate classes) and VERBS (candidate operations). Operations belong in the class that OWNS the data they manipulate.

## 🔑 DESIGN PRINCIPLES

- **Divide and Conquer** — break into modules
- **Loose Coupling** — minimize dependencies
- **High Cohesion** — each class has one clear job
- **Design for Change** — anticipate future modifications

---

# ═══════════════════════════════════════════════════
# SECTION 8: COMMON CODE PATTERNS (PAPER-CODING)
# ═══════════════════════════════════════════════════

## 🔑 PATTERN 1: Class with Dynamic Array
```cpp
class Array {
    int* data; int size;
public:
    Array(int s) : size(s) { data = new int[size]; }
    Array(const Array& a) : size(a.size) {        // COPY CTOR
        data = new int[size];
        for (int i = 0; i < size; i++) data[i] = a.data[i];
    }
    Array& operator=(const Array& a) {             // ASSIGNMENT
        if (this != &a) {
            delete[] data;
            size = a.size;
            data = new int[size];
            for (int i = 0; i < size; i++) data[i] = a.data[i];
        }
        return *this;
    }
    ~Array() { delete[] data; }
};
```

## 🔑 PATTERN 2: E-Wallet / Bank Account
```cpp
class Account {
    string owner; double balance;
public:
    Account(string n, double b = 0) : owner(n), balance(b) {}
    double getBalance() const { return balance; }
    bool deposit(double amt) { if (amt <= 0) return false; balance += amt; return true; }
    bool withdraw(double amt) { if (amt <= 0 || amt > balance) return false; balance -= amt; return true; }
    bool transfer(Account& to, double amt) {
        if (amt <= 0 || amt > balance) return false;
        balance -= amt; to.balance += amt; return true;
    }
};
```

## 🔑 PATTERN 3: Shape Hierarchy with Virtual
```cpp
class Shape {
protected: double w, h;
public:
    Shape(double w=1, double h=1) : w(w), h(h) {}
    virtual double area() const = 0;                  // abstract
    virtual void print() const { cout << area(); }
    virtual ~Shape() {}
};
class Rectangle: public Shape {
public: Rectangle(double w, double h) : Shape(w,h) {}
    double area() const override { return w * h; }
};
class Triangle: public Shape {
public: Triangle(double b, double h) : Shape(b,h) {}
    double area() const override { return 0.5 * w * h; }
};
// Usage: vector<Shape*> shapes; — polymorphic collection
```

## 🔑 PATTERN 4: Rational / Fraction Class
```cpp
class Rational {
    int num, den;
    int gcd(int a, int b) { a=abs(a); b=abs(b); while(b){int t=b;b=a%b;a=t;} return a; }
    void reduce() {
        if (den==0) throw; if (den<0){num=-num;den=-den;}
        int g = gcd(num,den); num/=g; den/=g;
    }
public:
    Rational(int n=0, int d=1) : num(n), den(d) { reduce(); }
    Rational operator+(const Rational& r) const { return Rational(num*r.den+den*r.num, den*r.den); }
    bool operator>(const Rational& r) const { return num*r.den > r.num*den; }
    void print() const { cout<<num; if(den!=1)cout<<"/"<<den; }
};
```

## 🔑 PATTERN 5: Time Class with Overloaded Operators
```cpp
class Time {
    int h, m, s;
    void norm() { m+=s/60; s%=60; h+=m/60; m%=60; h%=24; }
public:
    Time(int h=0, int m=0, int s=0) : h(h), m(m), s(s) { norm(); }
    Time operator+(const Time& t) const { return Time(h+t.h, m+t.m, s+t.s); }
    bool operator>(const Time& t) const {
        if(h!=t.h)return h>t.h; if(m!=t.m)return m>t.m; return s>t.s;
    }
    Time& operator++() { s++; norm(); return *this; }           // prefix
    Time operator++(int) { Time old=*this; ++(*this); return old; } // postfix
};
```

## 🔑 PATTERN 6: Generic Stack Template
```cpp
template<class T>
class Stack {
    T* arr; int cap, top;
public:
    Stack(int size) : cap(size), top(-1) { arr = new T[cap]; }
    ~Stack() { delete[] arr; }
    bool isEmpty() const { return top == -1; }
    bool isFull() const { return top == cap-1; }
    void push(T val) { if(!isFull()) arr[++top] = val; }
    T pop() { return isEmpty() ? T() : arr[top--]; }
    T peek() const { return isEmpty() ? T() : arr[top]; }
};
```

## 🔑 PATTERN 7: Complex Number Class
```cpp
class Complex {
    double re, im;
public:
    Complex(double r=0, double i=0) : re(r), im(i) {}
    double modulus() const { return sqrt(re*re + im*im); }
    Complex operator+(const Complex& c) const { return Complex(re+c.re, im+c.im); }
    Complex operator-(const Complex& c) const { return Complex(re-c.re, im-c.im); }
    Complex operator*(const Complex& c) const {
        return Complex(re*c.re-im*c.im, re*c.im+im*c.re);
    }
    bool operator>(const Complex& c) const { return modulus() > c.modulus(); }
    friend ostream& operator<<(ostream& os, const Complex& c) {
        os<<c.re; if(c.im>=0)os<<"+"; os<<c.im<<"i"; return os;
    }
};
```

## 🔑 PATTERN 8: Matrix Template
```cpp
template<typename T>
class Matrix {
    vector<vector<T>> data; int n;
public:
    Matrix(int size) : n(size), data(size, vector<T>(size, 0)) {}
    void set(int i, int j, T v) { data[i][j] = v; }
    T get(int i, int j) const { return data[i][j]; }
    double frobeniusNorm() const {
        double sum = 0;
        for(int i=0;i<n;i++) for(int j=0;j<n;j++) sum += data[i][j]*data[i][j];
        return sqrt(sum);
    }
    double rowSumNorm() const {
        double maxS = 0;
        for(int i=0;i<n;i++) {
            double s=0; for(int j=0;j<n;j++) s+=fabs(data[i][j]); maxS=max(maxS,s);
        }
        return maxS;
    }
};
```

## 🔑 PATTERN 9: File I/O with Polymorphism
```cpp
// Read shapes from file, sort by area, write to output
ifstream fin("input.txt");
int n; fin >> n;
vector<Shape*> shapes;
for (int i = 0; i < n; i++) {
    char type; fin >> type;
    if (type == 't') { /* read coords, push new Triangle */ }
    else if (type == 'r') { /* push new Rectangle */ }
    else if (type == 's') { /* push new Square */ }
    else if (type == 'p') { /* push new Parallelogram */ }
}
sort(shapes.begin(), shapes.end(),
    [](Shape* a, Shape* b) { return a->area() > b->area(); });
ofstream fout("output.txt");
fout << n << "\n";
for (auto* s : shapes) { s->print(fout); fout << "\n"; delete s; }
```

## 🔑 PATTERN 10: Derived Class from DblNode (Polymorphic List)
```cpp
class Student : public DblNode {
    long id;
public:
    Student(long idNum=0) : id(idNum) {}
    int operator==(const DblNode& p) const override {
        return id == ((Student&)p).id;  // CAST REQUIRED!
    }
    void printOn(ostream& os) const override { os << id; }
    void readFrom(istream& is) override { is >> id; }
};
```

---

# ═══════════════════════════════════════════════════
# SECTION 9: COMMON EXAM TRAPS (DON'T LOSE EASY MARKS)
# ═══════════════════════════════════════════════════

| # | TRAP | FIX |
|---|------|-----|
| 1 | Missing `;` after class closing brace `}` | Always write `};` |
| 2 | `class` default access is `private`; `struct` is `public` | Explicitly write `private:`/`public:` |
| 3 | Return type alone can't distinguish overloads | Change parameter types/number/order |
| 4 | Copy ctor vs assignment: `T a = b;` is copy ctor (a is NEW) | `T a; a = b;` is assignment (a exists) |
| 5 | Non-virtual base destructor → derived leak | Always `virtual ~Base() { }` |
| 6 | Non-virtual function → static binding even with base pointer | Use `virtual` for overridable methods |
| 7 | Default copy ctor/assignment = SHALLOW (double delete with dynamic mem) | Write custom deep copy ctor/operator= |
| 8 | `new[]` must pair with `delete[]`, not `delete` | Always match allocation/deallocation |
| 9 | If base has no default ctor, derived MUST use ctor-initializer | `Derived(args) : Base(args) { }` |
| 10 | `private` base members exist but inaccessible in derived | Use `protected` or accessors |
| 11 | Multiple inheritance ambiguity → must scope-resolve | `B1::x`, `B2::getValue()` |
| 12 | Diamond problem without `virtual` → 2 copies of base | `class D : virtual public B` |
| 13 | Template member definitions need `template<class T>` prefix | `template<class T> MyClass<T>::MyClass(){}` |
| 14 | Cannot inherit from template directly | Use instantiation: `class D : Array<int>{}` |
| 15 | Pass-by-value SLICES polymorphic objects | Always pass by pointer/reference |
| 16 | Pure virtual `=0` in base → class is abstract → can't instantiate | Override all pure virtuals in derived |
| 17 | `const` method can't modify members or call non-const methods | Match const correctly |
| 18 | Self-assignment must be checked in `operator=` | `if (this != &other)` guard |
| 19 | `operator=` must return `*this` by reference | `Type& operator=(...) { return *this; }` |
| 20 | Prefix `++` returns ref; postfix `++(int)` returns value | Don't mix them up |
| 21 | DLL remove() does NOT delete — just unlinks | Must explicitly `delete` after remove |
| 22 | Explicit non-template function beats template version | Know the priority rule |
| 23 | `static` members in template → separate per instantiation | `C<int>::x` ≠ `C<float>::x` |

---

# ═══════════════════════════════════════════════════
# SECTION 10: QUICK-REFERENCE CHEAT TABLE
# ═══════════════════════════════════════════════════

## COMMON FORMULAS
- Merge Sort: O(n log n), O(n) space
- Triangle area (shoelace): ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|
- Trapezium area: (a+b)/2 × h
- Complex modulus: √(a² + b²)
- Matrix Frobenius norm: √(Σ|aᵢⱼ|²)
- Row sum norm: max(Σ|row|)
- Escape velocity: √(2G·M/r)

## SIGNATURE TEMPLATE CHECKLIST
```
class ________ : ________ ________ {     // class Name : public/protected/private Base
private:                                  // data hidden
    ________ ________;
protected:                                // shared with derived
    ________ ________;
public:                                   // interface
    ________();                           // default ctor
    ________(________);                   // parameterized ctor
    ________(const ________&);            // copy ctor
    ________& operator=(const ________&); // assignment
    virtual ~________();                  // destructor (virtual if base!)
    virtual ________ ________() const;    // selector
    virtual ________ ________() = 0;      // pure virtual (abstract)
    void ________();                      // modifier
};  // ← DON'T FORGET THIS SEMICOLON!
```

## OUTPUT TRACING ORDER
```
Construction:  Base ctor → Members (declaration order) → Body
Destruction:   Body → Members (reverse) → Base destructor (reverse)
```

## THE 10 MOST FREQUENTLY ASKED CODE PATTERNS
1. Complete a class with private data + public methods + constructor
2. Write a copy constructor and assignment operator (deep copy)
3. Trace construction/destruction order
4. Write a derived class with constructor initializer
5. Override virtual functions + trace dynamic dispatch
6. Overload operators (+, ==, <<, ++ prefix/postfix)
7. Fix diamond inheritance with virtual base classes
8. Write a template class/function
9. Trace linked list operations (insert/remove)
10. Read shapes from file → sort by area → write output
