# Lec8: Inheritance in C++ — Study Guide

---

## 1. CONCEPT CARD: C++ Inheritance Mechanics

### 1.1 What It Is

Inheritance in C++ is a **language mechanism** where a new class (derived class) is built from an existing class (base class). The derived class **automatically inherits ALL data and function members** of the base class, plus its own explicitly declared members. C++ provides three forms of inheritance — `public`, `protected`, and `private` — each controlling how base members are exposed in the derived class.

Key C++ syntax: `class NewClass : access_specifier BaseClass { /* new members */ };`
- `access_specifier` is one of `public`, `protected`, or `private` (default is `private` for `class`, `public` for `struct`).
- Unlike the conceptual lecture (Lec7), Lec8 gives **exact rules** for member accessibility after inheritance.

### 1.2 What Problem It Solves (Beyond "Is-A")

Knowing that a `Student` IS A `Person` is not enough. You need concrete answers to:

- **Access levels after inheritance**: If `Person::name` is `protected`, is it still `protected` in `Student` under `public` inheritance? Under `private` inheritance?
- **Constructor chaining**: How does `Student("Alice", 12345)` call `Person("Alice")`? What happens if `Person` has no default constructor?
- **The diamond problem**: `GradAssistant` inherits from both `Student` and `Employee`, both of which inherit from `Person`. Does `GradAssistant` have one `Person` or two? How do you resolve ambiguity?
- **Pointer conversion rules**: Can a `Person*` be assigned to a `Student*`? When is it safe? When is it necessary?
- **Override mechanics in C++**: What happens when base and derived have functions with the same name? How do you still call the base version?

This lecture answers all of these with exact C++ rules.

### 1.3 How It Works (Step by Step)

1. **Define the base class** with members marked `private`, `protected`, or `public`.
2. **Declare the derived class** choosing an inheritance access specifier: `public`, `protected`, or `private`.
3. **At object creation**, the compiler chains constructors: base constructor runs FIRST, then member objects in declaration order, then the derived constructor body.
4. **At destruction**, the order reverses exactly: derived destructor body → member destructors → base destructors.
5. **Member access** is resolved at compile time based on both the member's original access level AND the inheritance access specifier.
6. **For multiple inheritance**, if ambiguity exists (same member name from two base paths), the compiler requires explicit scope resolution.
7. **For diamond inheritance** with a shared ancestor, `virtual` base classes guarantee a SINGLE shared instance of the common base.

### 1.4 Concrete Example (University HR System)

```
                 Person (name, id, getContactInfo())
                /                          \
        Student (major, gpa)          Employee (salary, department)
                \                          /
           GradAssistant (stipend, supervisor)
```

- `Person` is the common base with `name` and `id`.
- `Student` inherits from `Person` and adds `major`, `gpa`.
- `Employee` (or `Salaried`) inherits from `Person` and adds `salary`, `department`.
- `GradAssistant` inherits from BOTH `Student` and `Employee`.

**Without virtual inheritance**, `GradAssistant` has TWO `Person` subobjects (one from `Student`, one from `Employee`). Calling `setAge()` or `getAge()` is ambiguous — which `Person`?

**With virtual inheritance** (`class Student : virtual public Person`, `class Employee : virtual public Person`), `GradAssistant` has ONE shared `Person`. Ambiguity resolved.

### 1.5 What It Is NOT

- **Inheritance access specifiers (`public`, `protected`, `private`) are NOT the same as member access specifiers.** Member access controls who can access a member. Inheritance access controls how those members are **further exposed** in the derived class.
- **Inheritance is NOT the same as friendship.** A derived class does NOT automatically become a `friend` of the base class — it cannot access `private` base members directly.
- **A derived class does NOT inherit constructors, destructors, copy constructors, or assignment operators.** It must define its own (or the compiler generates them), and the derived constructor must call the base constructor.

---

## 2. BASE AND DERIVED CLASSES

### 2.1 Definitions

- **Base class**: A previously defined class that is used to define new classes. It provides the foundation of data and behavior.
- **Derived class**: A class that inherits ALL data and function members of a base class, in addition to its own explicitly declared members.

> **Critical detail**: The derived class inherits ALL members, including `private` ones. `private` base members EXIST inside the derived object but are NOT directly accessible by the derived class's code.

### 2.2 Single Inheritance

- Implements the **"is-a"** relationship.
- The derived class has exactly **ONE** base class.
- Forms a clean tree hierarchy (no diamond or ambiguity issues yet).

### 2.3 Declaration Syntax

```
class class_name : access_specifier base_class {
    // optional additional member list
};
```

Where `access_specifier` is one of:
- `public` — most common, preserves base member access levels
- `protected` — restricts inherited public members to protected
- `private` — restricts all inherited members to private (DEFAULT for `class` keyword)

### 2.4 Examples from Lecture

**Example 1 — Student Hierarchy:**
```
Student (name, id)
  ├── Undergraduate (year, major, minor)
  └── Graduate (advisor, thesis, research)
```
Each derived class IS A Student with extra specialization.

**Example 2 — Publication Hierarchy:**
```
Publication (publisher, date)
  ├── Magazine (circulation, # of issues per year)
  └── Book (ISBN, author)
```

**Example 3 — Different Views of an Employee:**
An `Employee` can be viewed along two orthogonal dimensions:
| Dimension | Variants |
|-----------|----------|
| **Employment type** | Full-time vs Part-time |
| **Tenure** | Permanent vs Temporary (different Social Insurance behavior) |

This demonstrates that inheritance is about modeling **alternative views** of the same core concept, not just one hierarchy.

---

## 3. ORDER OF CONSTRUCTOR & DESTRUCTOR EXECUTION

### 3.1 Constructor Order

**Base class constructors are ALWAYS executed FIRST.**

The full construction order for a derived object:
1. **Base class constructor** — first
2. **Member objects** — in declaration order (not initializer list order!)
3. **Derived constructor body** — last

This means by the time the derived constructor body runs, the base part and all member objects are fully initialized and safe to use.

### 3.2 Destructor Order

**EXACT REVERSE** of construction:
1. **Derived destructor body** — first
2. **Member destructors** — in reverse declaration order
3. **Base destructor** — last

### 3.3 Lecture Reference

See `Lec8_ex2-Employee.cpp` for a concrete trace of construction/destruction order.

**Memory aid:** "Constructor: base first, derived last. Destructor: derived first, base last." — Like building a house foundation-first but demolishing roof-first.

---

## 4. OVERRIDING

### 4.1 Definition

A function in the derived class with the **same function name** will **override** (hide/shadow) the function in the base class.

When you call `obj.functionName()` on a derived object, the derived version runs — the base version is hidden.

### 4.2 Accessing Overridden Functions

You can still retrieve the overridden base function using the **scope resolution operator** `::`:

```cpp
class Base {
public:
    void display() { /* base version */ }
};

class Derived : public Base {
public:
    void display() { /* overrides base version */ }
    void test() {
        display();           // calls Derived::display()
        Base::display();     // calls Base::display() explicitly
    }
};
```

> **Important:** Without `Base::`, calling `display()` inside `Derived` recursively calls `Derived::display()` — infinite recursion. The scope resolution operator is essential.

---

## 5. TYPES OF CLASS MEMBERS (Review + Diagram)

### 5.1 `private`

- Accessible to: the **class** itself + **friends** of that class.
- NOT accessible to derived classes.
- NOT accessible to outside functions/instances.

### 5.2 `protected`

- Accessible to: the **class** itself + **friends** + **derived classes**.
- NOT accessible to outside functions/instances.
- **Purpose:** Share with derived classes without exposing to the public.

### 5.3 `public`

- Accessible to: **everyone** — the class, friends, derived classes, outside instances.

### 5.4 Visual Diagram (from Lecture)

```
Accessible to derived    Public              Accessible to derived
classes AND instances ────►   Protected ◄──── classes only
                                    ▲
                                    │
                              Private ──── NOT accessible
                                            (to derived)
```

**Summary Table:**

| Member Access | Same Class | Friends | Derived Classes | Outside/Instances |
|---------------|:----------:|:-------:|:---------------:|:-----------------:|
| `public`      | Yes | Yes | Yes | Yes |
| `protected`   | Yes | Yes | Yes | No |
| `private`     | Yes | Yes | No | No |

---

## 6. TYPES OF INHERITANCE (THE CRITICAL SECTION)

This is the most important section for exams. Inheritance type determines what access level inherited members have in the derived class.

### 6.1 `public` Inheritance (MOST COMMON)

**Mapping:**
- Base `public` → **public** in derived
- Base `protected` → **protected** in derived
- Base `private` → **inaccessible** (exists but can't be touched)

**Outside access:** Outside functions CAN access inherited `public` members.

**Lecture example:**
```cpp
// Lec8_ex3-public-inher.cpp
int main() {
    p = aStack.removeFirst();  // WORKS — removeFirst() is public in derived
}
```

### 6.2 `private` Inheritance (DEFAULT for `class`)

**Mapping:**
- Base `public` → **PRIVATE** in derived
- Base `protected` → **PRIVATE** in derived
- Base `private` → **inaccessible**

**Outside access:** Outside functions CANNOT access ANYTHING inherited. Everything is private.

**Lecture example:**
```cpp
// Lec8_ex4-private-inher.cpp
int main() {
    p = aStack.removeFirst();  // ERROR — inherited member is now PRIVATE
}
```

> **Cascading effect:** Grandchildren inherit from this derived class via `public` but see NOTHING accessible from the original base. `private` inheritance cuts off the inheritance chain for all further descendants.

### 6.3 `protected` Inheritance

**Mapping:**
- Base `public` → **PROTECTED** in derived
- Base `protected` → **PROTECTED** in derived
- Base `private` → **inaccessible**

**Outside access:** Outside functions CANNOT access inherited members. Only further derived classes can.

**Lecture example:**
```cpp
// Lec8_ex5-protected-inher.cpp
int main() {
    p = aStack1.removeFirst();  // ERROR — inherited member is now PROTECTED, not public
}
```

### 6.4 Summary Table (The Key Table for Exams)

| Inheritance Type | Base `public` → | Base `protected` → | Base `private` → | Outside access to inherited? |
|:---:|:---:|:---:|:---:|:---:|
| **public** | `public` | `protected` | inaccessible | YES (to original public) |
| **private** | `private` | `private` | inaccessible | NO |
| **protected** | `protected` | `protected` | inaccessible | NO |

**Mnemonic:** The inheritance specifier caps the maximum access level. `private` inheritance caps everything at `private`. `protected` caps everything at `protected`. `public` doesn't cap anything — access levels are preserved.

---

## 7. CONSTRUCTORS IN DERIVED CLASSES

### 7.1 The Rule

When an object of a derived class is created, the constructor of the derived class **MUST FIRST** call the constructor of the base class (either explicitly or implicitly).

### 7.2 Constructor-Initializers

**Syntax:**
```cpp
class_name::class_name(param-list) : ctor-initializer {
    // function body
}
```

The **ctor-initializer** transfers parameters to base-class constructors and/or member initializers:

```cpp
// ctor-initializer examples:
Student::Student(string n, int i, string m)
    : Person(n, i),      // init base Person
      major(m)            // init member
{
    // body — base and members already initialized
}
```

### 7.3 Why Use ctor-initializer?

**Without it:**
- The **default** constructor for the base class would be called.
- You would then need **access functions** (setters) to set specific data members.
- This is wasteful — the base is initialized to default, then immediately overwritten.

**Critical case — base has NO default constructor:**
- If the base class has NO default constructor, the ctor-initializer is **REQUIRED**.
- The compiler will NOT compile derived class code without it.
- Error: no matching function for call to `BaseClass::BaseClass()`.

**Example (compilation fails without ctor-initializer):**
```cpp
class Person {
    string name;
public:
    Person(string n) : name(n) {}   // NO default constructor
};

class Student : public Person {
    // Student(string n) { }       // ERROR — can't call Person::Person()
    Student(string n) : Person(n) { }  // REQUIRED ctor-initializer
};
```

### 7.4 Destructors

Destructors are called **implicitly** starting with the **last derived class** and moving in the direction of the base class. You never need to call base destructors explicitly — the compiler handles the chain automatically.

**Lecture references:** `Lec8_ex6-ctor_derived.cpp`, `Lec8_ex7-ctor_init.cpp`

---

## 8. COMPATIBILITY AND POINTER CONVERSION

### 8.1 Compatibility Rule

- An object of a **derived** class can be treated as an object of its **base** class (a `Student` IS A `Person`).
- **The reverse is NOT true.** You cannot treat a `Person` as a `Student` — the `Person` may not have `major` or `gpa`.

### 8.2 Nested Class Scope

- A public or protected base class member that is **hidden** from the derived class can be accessed using the scope resolution operator: `base_class::member`.
- **The base class CANNOT access members of its derived classes.** Inheritance is one-way.

### 8.3 Implicit Conversion of Derived Pointers to Base Pointers

**Upcasting (derived → base):** Always safe, always implicit.

```cpp
Point3D * cp = new Point3D;   // Point3D derives from Point
Point * p;
p = cp;                        // OK — derived→base, implicit conversion
```

**Downcasting (base → derived):** NOT implicit. Explicit cast required. RISKY.

```cpp
Point3D *cp1;
cp1 = p;                       // ERROR — base→derived, NOT implicit
cp1 = (Point3D*) p;            // OK syntax BUT risky — may be wrong type
```

### 8.4 Why Downcasting Is Risky

The base pointer might point to:
- An actual base object (not a derived object)
- A DIFFERENT derived class (`Point3D` pointer from a `Point2D` object)

The derived class is expected to contain **more** (attributes & behaviors) than the base object. If the pointer doesn't actually point to a `Point3D`, accessing those extra members is **undefined behavior**.

> **Best practice:** Forcing class users to use explicit casting often leads to **poor code**. Prefer `dynamic_cast` (with RTTI) if downcasting is necessary — it checks at runtime and returns `nullptr` on failure.

---

## 9. MULTIPLE INHERITANCE

### 9.1 Concept

A class can have **more than one** base class. The derived class inherits from all bases simultaneously.

### 9.2 Example from Lecture — GraduateAssistant

```
        Student                 Employee / Salaried
            \                        /
             →  GraduateAssistant  ←
```

`GradAssistant` inherits from BOTH `Student` AND `Employee/Salaried`. It has all the members of both — `name` from `Student`, `salary` from `Employee`, plus its own `stipend` and `supervisor`.

### 9.3 The Ambiguity Problem

If `Student` and `Salaried` BOTH have a `setAge()` method (inherited from `Person` in two separate paths), calling `setAge()` on a `GradAssistant` is ambiguous:

```cpp
GradAssistant ga;
ga.setAge(25);  // ERROR — Student::setAge() or Salaried::setAge()?
```

**Lecture reference:** `Lec8_ex8_GradAssistant.cpp`

### 9.4 Solution: Virtual Base Classes

Declare the common base class as **virtual** in the intermediate classes:

```cpp
class Student : virtual public Person { /* ... */ };
class Employee : virtual public Person { /* ... */ };
```

**The diagram (from lecture):**
```
                Person
              virtual   virtual
             /               \
       Employee             Student
            \                /
             →  Salaried    ←
                    \
                 GradAssistant
```

**What virtual inheritance guarantees:**
- Only a **SINGLE instance** of the common base class (`Person`).
- `GradAssistant` has only ONE `Person` subobject, shared by both `Student` and `Employee`.
- Ambiguity is **resolved** — `getAge()` in `GradAssistant::display()` is no longer ambiguous.
- The `virtual` keyword lets the compiler decide which function and which variable to access (since there is now only one copy).

**Critical rule:** With virtual bases, the **most-derived class** must initialize the virtual base. `GradAssistant` must call `Person`'s constructor directly, not rely on `Student` or `Employee` to do it.

**Lecture reference:** `Lec8_ex9_GradAssistant.cpp`

> **Memory aid:** *Virtual inheritance = shared ancestor.* Without `virtual`, each inheritance path gets its own copy. With `virtual`, all paths share one copy.

---

## 10. MUST-MEMORIZE SYNTAX TEMPLATES

### Template 1: Single Inheritance Declaration (All 3 Types)

```cpp
// public inheritance — preserves base access levels
class Derived : public Base {
    // inherited public stays public, protected stays protected
};

// private inheritance — everything becomes private
class Derived : private Base {
    // inherited public and protected both become private
};

// protected inheritance — everything becomes protected
class Derived : protected Base {
    // inherited public and protected both become protected
};
```

### Template 2: Constructor Initializer Passing Args to Base

```cpp
class Base {
    int a, b;
public:
    Base(int x, int y) : a(x), b(y) {}  // NO default constructor
};

class Derived : public Base {
    int c;
public:
    Derived(int x, int y, int z)
        : Base(x, y),     // REQUIRED — base has no default ctor
          c(z)             // member initializer
    { }
};
```

### Template 3: Virtual Base Class Declaration (Diamond Solution)

```cpp
class Person {
public:
    string name;
    int age;
    Person(string n, int a) : name(n), age(a) { }
    void setAge(int a) { age = a; }
    int getAge() { return age; }
};

class Student : virtual public Person {
    string major;
public:
    Student(string n, int a, string m) : Person(n, a), major(m) { }
};

class Employee : virtual public Person {
    double salary;
public:
    Employee(string n, int a, double s) : Person(n, a), salary(s) { }
};

class GradAssistant : public Student, public Employee {
    double stipend;
public:
    GradAssistant(string n, int a, string m, double s, double st)
        : Person(n, a),                  // MOST-DERIVED inits virtual base
          Student(n, a, m),              // Person() call here is IGNORED
          Employee(n, a, s),             // Person() call here is IGNORED
          stipend(st)
    { }
};
```

### Template 4: Pointer Upcast and Downcast

```cpp
Derived d;
Base* bp = &d;           // upcast — IMPLICIT, always safe

Derived* dp = bp;        // ERROR — no implicit downcast
Derived* dp = (Derived*) bp;  // C-style cast — compiles but RISKY
Derived* dp = static_cast<Derived*>(bp);   // slightly safer, still no runtime check
Derived* dp = dynamic_cast<Derived*>(bp);  // safest — nullptr if wrong type
```

### Template 5: Override with Scope Resolution Fallback

```cpp
class Base {
public:
    void display() { cout << "Base"; }
};

class Derived : public Base {
public:
    void display() { cout << "Derived"; }
    void showBoth() {
        display();           // Derived::display()
        Base::display();     // Base::display() — scope resolution fallback
    }
};
```

### Template 6: Constructor/Destructor Order Trace

```cpp
class A {
public:
    A() { cout << "A ctor "; }
    ~A() { cout << "A dtor "; }
};
class B {
public:
    B() { cout << "B ctor "; }
    ~B() { cout << "B dtor "; }
};
class C : public A {
    B memberB;
public:
    C() { cout << "C ctor "; }
    ~C() { cout << "C dtor "; }
};

// Trace: A ctor → B ctor → C ctor → C dtor → B dtor → A dtor
// Rule: Base constructors → members (declaration order) → derived body
//       Destructors: exact reverse
```

### Template 7: Multiple Inheritance with Disambiguation

```cpp
class A : public B1, public B2, public B3 {
public:
    void setup() {
        B1::x = 5;            // disambiguate — pick B1's x
        B2::x = 10;           // disambiguate — pick B2's x
        B1::getValue();       // disambiguate — pick B1's getValue()
    }
};
```

### Template 8: Access Specifier Effect Summary

```cpp
// Use this as a quick reference during tracing:

// IF public inheritance:
//    Base public    → stays public
//    Base protected → stays protected
//    Base private   → inaccessible

// IF protected inheritance:
//    Base public    → becomes protected
//    Base protected → becomes protected
//    Base private   → inaccessible

// IF private inheritance:
//    Base public    → becomes private
//    Base protected → becomes private
//    Base private   → inaccessible
```

---

## 11. EXAM TRAPS

### Trap 1 — Access Specifier on Inheritance ≠ Access Specifier on Members
`class D : public B { }` — the `public` controls HOW base members are exposed. It does NOT make B's private members public. `public`/`protected`/`private` on inheritance is a separate concept from `public`/`protected`/`private` on individual members.

### Trap 2 — Private Inheritance Cascading Effect
If `class B : private A { }` and `class C : public B { }`, then `C` sees NOTHING from `A` directly. `private` inheritance made everything from `A` into `B`'s private members, which `C` cannot access. The chain is severed.

### Trap 3 — Non-Inherited `private` Base Members Are Still There
A `private` base member EXISTs inside the derived object's memory layout. It is simply not directly accessible by name from the derived class. You can access it indirectly through inherited `public`/`protected` base functions that manipulate it.

### Trap 4 — Virtual Base: Most-Derived Must Initialize
With virtual base classes, the **most-derived class** is responsible for calling the virtual base constructor. Constructor calls to the virtual base from intermediate classes (`Student`, `Employee`) are **ignored** by the compiler. Forgetting to initialize the virtual base in the most-derived class results in the virtual base's default constructor being called (or a compile error if no default exists).

### Trap 5 — No Implicit Downcast
`Person* p = new Student; Student* s = p;` — DOES NOT COMPILE. Downcast never implicit. Must use explicit cast (`static_cast<Student*>(p)` or `dynamic_cast<Student*>(p)`). Even `static_cast` is dangerous if `p` doesn't actually point to a `Student`.

### Trap 6 — Ctor-Initializer REQUIRED When Base Has No Default Constructor
If the base class defines ONLY a parameterized constructor (no default), the derived class MUST use a ctor-initializer to call it. The compiler will NOT generate a call to a non-existent default constructor.

### Trap 7 — Diamond Ambiguity Without `virtual`
Without virtual inheritance, `GradAssistant` (inheriting from both `Student` and `Employee`, both inheriting from `Person`) has TWO copies of `Person`. Any access to a `Person` member without qualification is ambiguous. You must use `Student::Person::member` or `Employee::Person::member` — but there are TWO copies, which is almost certainly not what you want.

### Trap 8 — Destructor Order Is REVERSE of Constructor Order
Easy to forget on pressure. Constructor: base → members → derived body. Destructor: derived body → members → base. Not "base first and last" — it reverses.

### Trap 9 — Override ≠ Replacement
When a derived class defines `void display()` and the base also has `void display()`, the base version is **hidden**, not deleted. Both coexist. Use `Base::display()` to access the hidden version. This is critical when calling `display()` from inside the derived class — without `Base::`, you call the derived version (which may recurse infinitely).

### Trap 10 — Constructors and Destructors Are NOT Inherited
A derived class does NOT inherit the base class's constructors, destructor, copy constructor, or assignment operator. The derived class must define its own (or the compiler generates them). The derived constructor must call the base constructor explicitly or implicitly.

### Trap 11 — Protected Inheritance Makes Public Members Protected
After `protected` inheritance, even originally `public` base members become `protected`. Outside instances CANNOT access them. Only further derived classes can.

### Trap 12 — Default Inheritance for `class` Is `private`
```cpp
class D : B { };  // equivalent to: class D : private B { }
```
```cpp
struct D : B { }; // equivalent to: struct D : public B { }
```
Forgetting the access specifier in a `class` declaration defaults to `private` inheritance, which is almost never what you want.

### Trap 13 — Member Initialization Order ≠ Initializer List Order
Members are initialized in **declaration order**, not the order they appear in the ctor-initializer. If `b` is declared before `a`, then `: a(valA), b(valB)` initializes `b` first and `a` second. This can cause subtle bugs when one member depends on another.

### Trap 14 — Compatibility: Derived Can Go to Base, but Base Cannot Go to Derived
A function expecting `Base&` can accept a `Derived` object. A function expecting `Derived&` CANNOT accept a `Base` object. The derived has everything the base has (plus more), but not vice versa. Passing a `Base` where a `Derived` is expected would leave the extra `Derived` fields uninitialized.

### Trap 15 — Friend Access Does Not Propagate Through Inheritance
Friendship is NOT inherited. If `class B` is a friend of `class A`, and `class D` derives from `B`, then `D` is NOT automatically a friend of `A`. Conversely, if `A` has friend `F`, derived classes of `A` do NOT automatically treat `F` as a friend for their own private members.

### Trap 16 — Hiding vs Overriding
In the absence of `virtual`, a function with the same name in the derived class hides the base function(s). ALL base overloads with that name are hidden, not just the one with the matching signature. To bring them back into scope, use `using Base::functionName;` in the derived class.

### Trap 17 — Scope Resolution in Multiple Inheritance
When two base classes define a member with the same name, EVERY access to that name through the derived class must be qualified with `Base1::` or `Base2::`. There is no "first in list wins" rule in standard C++ — ambiguity is a compile error until resolved explicitly.

---

## 12. HAND-CODING DRILLS

### Drill 1: Public/Private/Protected Inheritance Effects on Grandchild

**Scenario:** Given the base class:
```cpp
class Animal {
public:
    void eat();
protected:
    int age;
private:
    int dna;
};
```

A derived class `Mammal` inherits from `Animal` (all three inheritance types below). Another class `Dog` inherits `public`ly from `Mammal`. For EACH inheritance type between `Animal` and `Mammal`, trace what `Dog` can access and what `main()` can access.

> [!success]- Show Answer
> **Case 1: `class Mammal : public Animal`**
> - `eat()` → `public` in Mammal → `public` in Dog → main() CAN call
> - `age` → `protected` in Mammal → `protected` in Dog → main() CANNOT access
> - `dna` → inaccessible in Mammal → inaccessible in Dog
>
> **Case 2: `class Mammal : private Animal`**
> - `eat()` → `private` in Mammal → inaccessible in Dog → main() CANNOT call
> - `age` → `private` in Mammal → inaccessible in Dog → main() CANNOT access
> - `dna` → inaccessible → inaccessible
> - Everything from Animal is cut off from Dog!
>
> **Case 3: `class Mammal : protected Animal`**
> - `eat()` → `protected` in Mammal → `protected` in Dog → main() CANNOT call
> - `age` → `protected` in Mammal → `protected` in Dog → main() CANNOT access
> - `dna` → inaccessible → inaccessible
> - Dog CAN access `eat()` and `age` internally, but clients CANNOT

### Drill 2: Ctor-Initializer Required When Base Has No Default

**Scenario:** Fix the compilation errors:

```cpp
class Vehicle {
    int maxSpeed;
public:
    Vehicle(int ms) { maxSpeed = ms; }   // no default ctor
};

class Car : public Vehicle {
    int doors;
public:
    Car(int ms, int d) {                 // COMPILE ERROR
        doors = d;
    }
};
```

> [!success]- Show Answer
> ```cpp
> class Car : public Vehicle {
>     int doors;
> public:
>     Car(int ms, int d)
>         : Vehicle(ms),    // REQUIRED — base has no default ctor
>           doors(d)         // init member
>     { }
> };
> ```
> The error was that `Car(int, int)` tried to implicitly call `Vehicle()` which doesn't exist. The ctor-initializer `: Vehicle(ms)` fixes this by explicitly passing the parameter to the base constructor.

### Drill 3: Diamond Problem WITHOUT Virtual

**Scenario:** Trace the compilation error:

```cpp
class Person {
public:
    string name;
    void setName(string n) { name = n; }
};

class Student : public Person {
public:
    int studentID;
};

class Employee : public Person {
public:
    double salary;
};

class GradAssistant : public Student, public Employee {
public:
    void setup() {
        setName("Alice");   // (A) — COMPILE ERROR: ambiguous
        name = "Alice";     // (B) — COMPILE ERROR: ambiguous
    }
};
```

Explain the ambiguity and fix it WITHOUT using virtual (just resolve explicit base).

> [!success]- Show Answer
> `GradAssistant` has TWO `Person` subobjects — one via `Student` and one via `Employee`. Both contain `name` and `setName()`. The compiler doesn't know which one you mean.
>
> **Fix without virtual:**
> ```cpp
> void setup() {
>     Student::setName("Alice");     // use Student's Person copy
>     Student::name = "Alice";       // use Student's Person copy
>     // OR
>     Employee::setName("Alice");    // use Employee's Person copy
> }
> ```
> But note: this creates TWO separate names — one in Student's Person and one in Employee's Person. They can diverge. Virtual base classes are the correct solution.

### Drill 4: Diamond Problem WITH Virtual

**Scenario:** Rewrite the hierarchy from Drill 3 using virtual base classes so that `GradAssistant` has a single `name`.

> [!success]- Show Answer
> ```cpp
> class Person {
> public:
>     string name;
>     void setName(string n) { name = n; }
>     Person(string n) : name(n) { }
> };
>
> class Student : virtual public Person {
> public:
>     int studentID;
>     Student(string n, int id) : Person(n), studentID(id) { }
> };
>
> class Employee : virtual public Person {
> public:
>     double salary;
>     Employee(string n, double s) : Person(n), salary(s) { }
> };
>
> class GradAssistant : public Student, public Employee {
> public:
>     double stipend;
>     GradAssistant(string n, int id, double s, double st)
>         : Person(n),              // MOST-DERIVED inits virtual base
>           Student(n, id),         // Person(n) here is IGNORED
>           Employee(n, s),         // Person(n) here is IGNORED
>           stipend(st)
>     { }
>
>     void setup() {
>         setName("Alice");   // NOW compiles fine — single Person
>         name = "Alice";     // NOW compiles fine — single Person
>     }
> };
> ```
> With `virtual` inheritance, `GradAssistant` has ONE shared `Person`. All ambiguity resolved.

### Drill 5: Pointer Casting — Up and Down

**Scenario:** Mark each line as OK (compiles + safe), ERROR (doesn't compile), or RISKY (compiles but unsafe):

```cpp
class Shape { public: virtual void draw(); };
class Circle : public Shape { public: double radius; void draw() override; };
class Square : public Shape { public: double side; void draw() override; };

int main() {
    Circle c;
    Square sq;

    Shape* s1 = &c;                 // (1)
    Circle* c1 = s1;                // (2)
    Circle* c2 = (Circle*) s1;      // (3)
    Shape* s2 = &sq;
    Circle* c3 = (Circle*) s2;      // (4)
}
```

> [!success]- Show Answer
> **(1):** OK — Upcast from `Circle*` to `Shape*`, implicit and safe.
>
> **(2):** ERROR — Downcast not implicit. Compilation fails.
>
> **(3):** RISKY — C-style cast compiles but `s1` actually does point to a `Circle`, so this happens to be safe. But the compiler doesn't check.
>
> **(4):** RISKY — `s2` points to a `Square`, but is cast to `Circle*`. The cast compiles, but accessing `c3->radius` is **undefined behavior** — `Square` doesn't have `radius` at that offset. This is the classic downcast hazard.

### Drill 6: Multiple Inheritance Ambiguity Resolution

**Scenario:** Implement the `setup()` function with proper disambiguation:

```cpp
class Scanner {
public:
    int resolution;
    void start() { cout << "Scanner started"; }
};

class Printer {
public:
    int resolution;
    void start() { cout << "Printer started"; }
};

class AllInOne : public Scanner, public Printer {
public:
    void setup() {
        // (1) Set Scanner resolution to 600
        // (2) Set Printer resolution to 1200
        // (3) Call Scanner's start()
        // (4) Call Printer's start()
    }
};
```

> [!success]- Show Answer
> ```cpp
> void setup() {
>     Scanner::resolution = 600;    // (1) explicit scope
>     Printer::resolution = 1200;   // (2) explicit scope
>     Scanner::start();             // (3) explicit scope
>     Printer::start();             // (4) explicit scope
> }
> ```
> Without `Scanner::` and `Printer::`, both `resolution` and `start()` are ambiguous compile errors. C++ requires explicit scope resolution for conflicting members in multiple inheritance.

### Drill 7: Construction Order — Composition + Inheritance

**Scenario:** Given the classes below, write the output of the program:

```cpp
class Engine {
public:
    Engine() { cout << "Engine ctor "; }
    ~Engine() { cout << "Engine dtor "; }
};

class Vehicle {
public:
    Vehicle() { cout << "Vehicle ctor "; }
    ~Vehicle() { cout << "Vehicle dtor "; }
};

class Car : public Vehicle {
    Engine myEngine;
public:
    Car() { cout << "Car ctor "; }
    ~Car() { cout << "Car dtor "; }
};

int main() {
    Car c;
    return 0;
}
```

> [!success]- Show Answer
> **Output:** `Vehicle ctor Engine ctor Car ctor Car dtor Engine dtor Vehicle dtor`
>
> **Constructor order:** Base `Vehicle` first → member `Engine` (declaration order) → `Car` body.
>
> **Destructor order:** Exact reverse — `Car` body → `Engine` → `Vehicle`.

### Drill 8: Full Design from Scratch — Library System

**Scenario:** Design a library system with inheritance.

Requirements:
- All items have a `title`, `callNumber`, and a `checkout(string patron)` method.
- `Book` items add an `author` and `ISBN`.
- `Journal` items add a `volume` and `issueNumber`.
- `DigitalMedia` items add a `fileSize` and `format`.
- `AudioBook` IS A `Book` AND IS A `DigitalMedia` — it needs a `narrator` and `duration`.

Write the full class declarations including constructors. Use virtual inheritance where needed.

> [!success]- Show Answer
> ```cpp
> class LibraryItem {
> protected:
>     string title;
>     string callNumber;
> public:
>     LibraryItem(string t, string cn) : title(t), callNumber(cn) {}
>     virtual void checkout(string patron) {
>         cout << title << " checked out to " << patron;
>     }
>     virtual ~LibraryItem() {}
> };
>
> class Book : virtual public LibraryItem {
> protected:
>     string author;
>     string ISBN;
> public:
>     Book(string t, string cn, string a, string isbn)
>         : LibraryItem(t, cn), author(a), ISBN(isbn) {}
> };
>
> class DigitalMedia : virtual public LibraryItem {
> protected:
>     double fileSize;
>     string format;
> public:
>     DigitalMedia(string t, string cn, double fs, string fmt)
>         : LibraryItem(t, cn), fileSize(fs), format(fmt) {}
> };
>
> class Journal : public LibraryItem {
>     int volume;
>     int issueNumber;
> public:
>     Journal(string t, string cn, int v, int i)
>         : LibraryItem(t, cn), volume(v), issueNumber(i) {}
> };
>
> class AudioBook : public Book, public DigitalMedia {
>     string narrator;
>     double duration;
> public:
>     AudioBook(string t, string cn, string a, string isbn,
>               double fs, string fmt, string narr, double dur)
>         : LibraryItem(t, cn),    // most-derived inits virtual base
>           Book(t, cn, a, isbn),  // LibraryItem() call ignored
>           DigitalMedia(t, cn, fs, fmt), // LibraryItem() call ignored
>           narrator(narr),
>           duration(dur)
>     {}
>
>     void checkout(string patron) override {
>         cout << "Audiobook \"" << title << "\" (narrated by "
>              << narrator << ") checked out to " << patron;
>     }
> };
> ```
>
> **Design justification:**
> - `LibraryItem` is virtual base because `AudioBook` inherits from BOTH `Book` AND `DigitalMedia` which both derive from `LibraryItem` → diamond problem.
> - `Book` uses `virtual public` so `AudioBook` gets ONE `LibraryItem`.
> - `DigitalMedia` uses `virtual public` for the same reason.
> - `AudioBook` must explicitly call `LibraryItem(t, cn)` as the most-derived class.

### Drill 9: Access Level Tracing Through Multiple Generations

**Scenario:** Trace each numbered access attempt as LEGAL or ILLEGAL:

```cpp
class A {
private:   int a1;
protected: int a2;
public:    int a3;
};

class B : protected A {
public:
    void testB() {
        a1 = 1;    // (1)
        a2 = 2;    // (2)
        a3 = 3;    // (3)
    }
};

class C : public B {
public:
    void testC() {
        a1 = 1;    // (4)
        a2 = 2;    // (5)
        a3 = 3;    // (6)
    }
};

int main() {
    B b;
    b.a2 = 5;     // (7)
    b.a3 = 5;     // (8)

    C c;
    c.a3 = 5;     // (9)
}
```

> [!success]- Show Answer
> **(1):** ILLEGAL — `a1` is `private` in A, inaccessible in B.
>
> **(2):** LEGAL — `a2` is `protected` in A → `protected` in B (protected inheritance preserves protected) → accessible inside B.
>
> **(3):** LEGAL — `a3` is `public` in A → `protected` in B (protected inheritance caps at protected) → accessible inside B.
>
> **(4):** ILLEGAL — `a1` was `private` in A → inaccessible in B → still inaccessible in C.
>
> **(5):** LEGAL — `a2` was `protected` in A → `protected` in B → `protected` in C (public inheritance preserves it) → accessible inside C.
>
> **(6):** LEGAL — `a3` was `public` in A → `protected` in B → `protected` in C (public inheritance preserves it) → accessible inside C.
>
> **(7):** ILLEGAL — `a2` is `protected` in B → outside main() cannot access.
>
> **(8):** ILLEGAL — `a3` is `protected` in B → outside main() cannot access (was capped by protected inheritance).
>
> **(9):** ILLEGAL — `a3` is `protected` in C → outside main() cannot access. Protected inheritance from A→B permanently made formerly-public members protected, and public inheritance B→C doesn't "undo" that.

