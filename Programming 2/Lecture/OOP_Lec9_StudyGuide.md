# Lec9: Polymorphism — Study Guide

---

## 1. CONCEPT CARD

### 1.1 What It Is

Polymorphism (in OOP, specifically **Inclusion Polymorphism / Overriding**) is the ability of different types of objects to respond differently to the **same function call** with the **same parameter types**. The correct version of the function is chosen at **runtime** based on the actual type of the object, not the type of the pointer or reference.

### 1.2 What Problem It Solves

Without polymorphism, code that works with heterogeneous collections of objects must explicitly check the type of each object and branch accordingly:

```cpp
if (type == CIRCLE)      drawCircle();
else if (type == RECTANGLE) drawRectangle();
else if (type == TRIANGLE)  drawTriangle();
```

Adding a new type (`Hexagon`) requires modifying **every** such if-else chain in the codebase. With polymorphism, you call `shape->draw()` and each object knows how to draw itself. Adding a new shape class requires **zero changes** to existing code.

### 1.3 How It Works

1. Declare a function as `virtual` in the base class.
2. Override it in each derived class (same signature — same name, same parameter types).
3. Create objects and store them via base-class pointers or references: `Base* p = new Derived();`.
4. Call `p->virtualFunction()` — the compiler generates code that looks up the correct function in the object's **vtable** (virtual table) at runtime.
5. Non-virtual functions use **static binding** (resolved at compile time — faster).
6. Virtual functions use **dynamic binding** (resolved at runtime via vtable lookup — slightly slower).
7. Each class with virtual functions has a hidden **vtable** — an array of function pointers.
8. Each object of such a class has a hidden **vptr** (virtual pointer) pointing to its class's vtable.

### 1.4 Concrete Example

A payment processing system:

- `PaymentMethod` declares `virtual void processPayment(double amount)`.
- `CreditCard`, `PayPal`, `BankTransfer` each override it with their own logic (contacting different payment APIs).
- The checkout system holds a `PaymentMethod*` chosen by the user at runtime.
- `method->processPayment(total)` — the correct implementation runs without the checkout code knowing which specific payment type it is handling.
- Adding `CryptoCurrency` later requires creating **one new class**. The checkout code **never changes**.

### 1.5 What It Is NOT

Polymorphism (overriding) is **NOT** overloading:

| Aspect | Overloading | Overriding (Polymorphism) |
|--------|------------|---------------------------|
| Parameters | **Different** types, count, or order | **Same** types and count |
| Resolution | Compile-time (static binding) | Runtime (dynamic binding) |
| `virtual` keyword | Not required | Required in base class |
| Inheritance | Not required | Required (base-derived relationship) |
| Also called | Ad-hoc polymorphism | Inclusion polymorphism |

Polymorphism is also **NOT** coercion — where the compiler automatically converts one type to another to match a function signature.

---

## 2. LITERAL MEANING AND DEFINITION

### 2.1 Etymology

- **poly** (πολύς, Greek) — many, multiple, different
- **morph** (μορφή, Greek) — form, shape, structure

Together: **"many forms"** — one entity taking on many shapes or behaviors.

### 2.2 Formal Definition

The ability to assign a **different meaning or usage** to something in **different contexts**. In programming, it means a single interface (function name) can represent multiple underlying behaviors, with the appropriate behavior being determined by context (argument types, or the runtime type of the object).

---

## 3. TYPES OF POLYMORPHISM

### 3.1 Overview of Four Types

Polymorphism in programming is broader than just OOP overriding. There are **four recognized types**:

| # | Type | Resolution | Mechanism in C++ |
|---|------|-----------|-----------------|
| 1 | Overloading | Compile-time | Multiple functions, same name, different signatures |
| 2 | Coercion | Compile-time | Implicit type casting by the compiler |
| 3 | Parametric | Compile-time | Templates (generic programming) |
| 4 | Inclusion / Overriding | Runtime | Virtual functions + inheritance |

**The type of polymorphism that the OOP paradigm refers to is #4 — Inclusion Polymorphism (Overriding).** The other three are compile-time (ad-hoc or parametric) mechanisms.

### 3.2 Overloading

Overloading means having the **same function name** operate on **different parameter types**. We overload when we want to do "essentially the **same thing**" but with **different parameters**.

```cpp
int  add(int a, int b)   { return a + b; }
float add(float a, float b) { return a + b; }
```

- The compiler resolves which version to call at **compile time** by matching argument types.
- This is a form of **ad-hoc polymorphism** — resolved syntactically at compile time, not dynamically.

### 3.3 Coercion

Coercion is when an object or primitive is **automatically cast** into another object/primitive type by the compiler to match a function signature. It goes beyond simple overloading — the compiler actively converts types.

```cpp
int  add(int a, int b)   { return a + b; }
float add(float a, float b) { return a + b; }

int main() {
    add(1, 1.0);   // The 1.0 (double) is COERCED to int 1
                   // Compiler picks add(int, int)
    add(1.0, 1);   // The 1.0 (double) is COERCED to int 1
                   // Compiler picks add(int, int)
}
```

- The compiler sees `add(1, 1.0)`. It looks for a match: `add(int, float)` — doesn't exist. It finds `add(int, int)` and `add(float, float)`. It converts (coerces) the `1.0` double to `int` to match.
- Coercion is a **compile-time** mechanism — no runtime lookup involved.
- Do **NOT** confuse coercion with overriding. Coercion converts **arguments**; overriding selects a different **function body** at runtime.

### 3.4 Parametric Polymorphism

Parametric polymorphism provides a way to execute the **same code** for **any type**. The code is written once, and the type is supplied as a parameter.

- In C++, implemented via **templates**:

```cpp
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    add<int>(1, 2);       // T = int
    add<float>(1.5, 2.3); // T = float
    add<string>("Hello ", "World"); // T = string
}
```

- The compiler generates a **separate copy** of the function for each type used — this is resolved at **compile time**.
- Originated from **functional programming** languages (e.g., ML, Haskell).
- Now popular in Java as **generic programming**.
- Note: in C++, templates are resolved at compile time, while in Java, generics use type erasure.

### 3.5 Inclusion Polymorphism (Overriding)

**This IS "polymorphism" in the OOP context.** Different types of objects respond differently to the **same function call** with the **same parameter types**.

- Achieved by **overriding** inherited virtual functions.
- We override an inherited function when we want to do something **slightly different** than what the base class does.
- Highly connected to the concept of **inheritance** — you cannot have overriding without a base-derived class relationship.

Illustration with cats:

```cpp
class Cat {
public:
    virtual void makeSound() { cout << "meow" << endl; }
};

class Lion : public Cat {
public:
    void makeSound() { cout << "MREOWWW" << endl; }
};

class Kitten : public Cat {
public:
    void makeSound() { cout << "mews" << endl; }
};
```

- Same message: `makeSound()`
- Same parameter types: `void`
- Different responses: `meow`, `MREOWWW`, `mews`
- Which sound plays is determined by the **runtime type** of the object, not the pointer type.

---

## 4. OOP PILLARS CONNECTION (REVIEW)

### 4.1 How Polymorphism Fits

The four pillars of OOP:

| Pillar | Description | Role |
|--------|-------------|------|
| **Encapsulation** | Bundling data and associated functionalities into a single unit; hiding internal details from the outside world. | Protects data integrity; provides a clean public interface. |
| **Inheritance** | Deriving a class from another, acquiring its properties and behaviors. | Enables code reuse and establishes "is-a" relationships. |
| **Abstraction** | Hiding the complexity of implementation; exposing only the essential specifications through interfaces or abstract classes. | Simplifies usage; focuses on *what* not *how*. |
| **Polymorphism (Overriding)** | Different types respond differently to the same function call. | Enables extensibility —new types can be added without changing existing code. |

Polymorphism depends on **inheritance** (to establish the base-derived relationship) and **abstraction** (to define the common interface via virtual or pure virtual functions). It works alongside **encapsulation** (each class encapsulates its own version of the behavior).

---

## 5. BINDING

### 5.1 What Is Binding?

Binding is the process of **connecting a method call to a method body** — determining which concrete function implementation will execute when a call is made.

### 5.2 Static / Early Binding

- Binding performed **before** the program runs (at **compile time**).
- The compiler determines which function to call based on the **type of the pointer or reference**, not the actual object.
- Used in C compilers by default.
- **Default behavior in C++** for non-virtual functions.
- **Faster** — no runtime lookup overhead.
- Enables compiler optimizations (e.g., inlining).

### 5.3 Dynamic / Late Binding

- Binding occurs at **runtime**, based on the **actual type of the object** being pointed to (not the pointer type).
- The runtime system follows the object's vptr → vtable to find the correct function address.
- **Slightly slower** than static binding due to the vtable indirection.
- **Polymorphism is a CONCEPT; dynamic binding is the MECHANISM that implements it.**
- In C++, functions must be declared `virtual` to enable dynamic binding.

### 5.4 Static Binding in C++ (Diagram in Mind)

```
Base* ptr = new Derived();
ptr->nonVirtualFunction();   // Calls Base::nonVirtualFunction()
                             // Because ptr is declared as Base*
                             // Compiler resolves this at compile time
```

When a function is **non-virtual**, the compiler resolves the call entirely at compile time using the **pointer/reference type** (`Base*`), regardless of what object the pointer actually points to. A `Base*` calling a non-virtual function **always** calls the `Base` version.

### 5.5 Dynamic Binding in C++ (Diagram in Mind)

```
Base* ptr = new Derived();
ptr->virtualFunction();      // Calls Derived::virtualFunction()
                             // Because the actual object is a Derived
                             // Resolved at runtime via vptr → vtable lookup
```

Key points:

- Methods are **NON-VIRTUAL by default** in C++.
- Use the `virtual` keyword to make a function dynamically bound.
- **Design decision**: C++ was designed to be "almost as efficient as C."
  - Dynamic binding is more costly than static binding (extra indirection).
  - "If you don't use it, you don't pay for it."
- If a method cannot be overridden (non-virtual), the compiler can:
  - Statically bind it (no runtime overhead).
  - Potentially inline it for further optimization.
- More compiler optimization techniques can be applied to non-virtual methods.

---

## 6. VIRTUAL FUNCTIONS

### 6.1 Definition

A **non-static member function** prefaced by the `virtual` keyword. It tells the compiler to generate code that **selects the appropriate version** of this function at **runtime** based on the actual object type.

```cpp
class Base {
public:
    virtual void draw();     // Virtual function
    void print();            // Non-virtual function (static binding)
};
```

### 6.2 Importance of Polymorphism (Why Virtual Functions Matter)

The true power of polymorphism emerges in this scenario:

1. You have a **collection** of generic reference variables (e.g., an array of `Base*` pointers).
2. Each element points to a **different type** of object (e.g., `Circle`, `Rectangle`, `Triangle` — all derived from `Shape`).
3. You step through the collection and call a **polymorphic function** on each element.
4. The **runtime system** automatically picks the correct method body for each object's type.

```cpp
Shape* shapes[3];
shapes[0] = new Circle(5);
shapes[1] = new Rectangle(4, 6);
shapes[2] = new Triangle(3, 4, 5);

for (int i = 0; i < 3; i++) {
    shapes[i]->draw();   // Each calls its own version
}
```

**Critical insight**: When a **new derived class** is added (e.g., `Cheetah` to a `Cat` hierarchy), you do **NOT** need to change any existing code. The existing `doMeowing()` loop that calls `cat->makeSound()` on an array of `Cat*` pointers works automatically with `Cheetah` — the vtable mechanism handles the dispatch.

---

## 7. VIRTUAL DESTRUCTORS

### 7.1 The Problem

Calling the **wrong destructor** can be disastrous, particularly when the destructor contains a `delete` statement:

```cpp
class Base {
    int* data;
public:
    Base()  { data = new int[100]; }
    ~Base() { delete[] data; }        // NON-virtual destructor
};

class Derived : public Base {
    char* buffer;
public:
    Derived()  { buffer = new char[1024]; }
    ~Derived() { delete[] buffer; }   // This NEVER runs if ~Base is non-virtual!
};

int main() {
    Base* ptr = new Derived();
    delete ptr;   // Calls ONLY Base::~Base() — Derived::~Derived() is skipped!
                  // buffer leaks (1024 bytes leaked)
}
```

- Destructors are **NOT inherited** in the traditional sense (each class has its own destructor).
- If the base destructor is non-virtual, `delete ptr` uses static binding and calls **only** the base destructor.
- The derived destructor never runs → resource leaks, dangling members, undefined behavior.

### 7.2 The Rule

**ALWAYS make base class destructors virtual when the class is meant to be manipulated polymorphically** (i.e., you intend to delete derived objects through base-class pointers).

```cpp
class Base {
public:
    virtual ~Base() { delete[] data; }  // Virtual destructor — always do this
};
```

Now when `delete ptr` is called:
1. Dynamic binding calls `Derived::~Derived()` first (cleaning up `buffer`).
2. Then automatically calls `Base::~Base()` (cleaning up `data`).

Both resources are properly freed. The cost of virtual destructors is negligible compared to the risk of resource leaks.

> Example file: `Lec9_ex1-VirtualDes.cpp` from the lecture.

---

## 8. ABSTRACT CLASSES (IN C++)

### 8.1 Interface vs Abstract Class

- In C++, an **interface** describes the behavior or capabilities of a class **without committing** to a particular implementation.
- C++ interfaces are implemented using **abstract classes**.
- Should NOT be confused with **data abstraction** (keeping implementation details separate from associated data — that's a different concept).

### 8.2 Making a Class Abstract

A class is made **abstract** by declaring **at least one** of its functions as a **pure virtual function**. A pure virtual function is specified by placing `= 0` in its declaration:

```cpp
class Box {
public:
    virtual double getVolume() = 0;   // Pure virtual function
                                      // Makes Box an abstract class
private:
    double length, breadth, height;
};
```

### 8.3 Pure Virtual Function Syntax

```cpp
virtual returnType functionName(parameters) = 0;
```

- The `= 0` is the **pure specifier** — it makes the virtual function "pure."
- A pure virtual function has NO body in the base class (though C++ does allow providing a body that derived classes can call explicitly via `Base::functionName()`).
- Any class inheriting from an abstract class **must override all pure virtual functions** to become a concrete class.

### 8.4 Properties of Abstract Classes

| Property | Explanation |
|----------|-------------|
| **Purpose** | Provide an appropriate **base class** from which other classes can inherit; define a common interface. |
| **Conceptual role** | Often represent **concepts** for which objects cannot meaningfully exist (e.g., `Shape` — you can draw a circle or a rectangle, but what does a generic "shape" look like?). |
| **Instantiation** | **CANNOT** be used to instantiate objects. `Shape s;` or `new Shape()` is a **compilation error**. |
| **Interface role** | Serves only as an **interface** — a contract that derived classes must fulfill. |
| **Concrete classes** | Classes that CAN be instantiated are called **concrete classes**. |
| **Pointers and references** | It IS possible to declare **pointer** and **reference** variables to abstract classes: `Shape* s;` is fine. You just can't create a bare `Shape` object. |

> Example file: `Lec9_ex2-Shapes.cpp` — Abstract `Shape` class with derived `Circle` and `Polygon`.

### 8.5 Abstract Derived Classes

- If a pure virtual function is **NOT defined** (overridden) in a derived class, that derived class is **also abstract**.
- If a derived class does NOT provide an implementation for a pure virtual function, it inherits the `= 0` and remains abstract.

```cpp
class Shape {
public:
    virtual void draw() = 0;
    virtual double area() = 0;
};

class Circle : public Shape {
public:
    void draw() { /* ... */ }       // Overridden
    // area() NOT overridden → Circle is STILL abstract!
};

class FilledCircle : public Circle {
public:
    double area() { return 3.14159 * r * r; }  // Now fully concrete
};
```

- For **non-pure** virtual functions, if a derived class does NOT provide an override, the **base class implementation is used** (inherited behavior).
- It IS possible to declare **pointer variables** to abstract classes, enabling polymorphic collections.

---

## 9. THE "this" KEYWORD

### 9.1 Definition

Within a member function, `this` is the name of an **implicit pointer** to the **current object** — the object that received the message (function call) associated with this function.

```cpp
class Point {
    int x, y;
public:
    void setX(int x) {
        this->x = x;   // this->x = member variable; x = parameter
    }
};
```

- `this` is automatically passed as a hidden parameter to every non-static member function.
- Its type is `ClassName* const` (a constant pointer to the class type).

### 9.2 Polymorphic Nature

`this` is really a **polymorphic word** — it can mean **any object** in the C++ language:

```cpp
class Animal {
public:
    virtual void identify() {
        cout << "I am an Animal at " << this << endl;
    }
};

class Dog : public Animal {
public:
    void identify() {
        cout << "I am a Dog at " << this << endl;
    }
};

int main() {
    Animal* a = new Dog();
    a->identify();  // Inside identify(), "this" points to the Dog object
                    // Even though the pointer type is Animal*
}
```

- When a virtual function is called through a base pointer, `this` inside that function points to the **actual derived object**, not the base type.
- This is essential for virtual function dispatch: `this` allows the function to access the correct object's data and vtable.

---

## 10. VIRTUAL TABLES (VTABLES)

### 10.1 Mechanism

C++ (and Java) use the **virtual table (vtable)** mechanism to implement dynamic binding:

- A class with **virtual member functions** has a hidden **virtual table** — a static array containing the **addresses** of its virtual functions.
- An object of such a class has a hidden pointer called the **vptr** (virtual pointer) that points to the virtual table of its class.
- The vptr is typically stored as the first hidden member of the object.

```
Object of Derived:               Class Derived's vtable:
┌──────────────┐                ┌──────────────────────┐
│    vptr      │──────────────> │ &Derived::action()   │
│  data members│                │ &Derived::draw()     │
│  ...         │                │ &Derived::~Derived() │
└──────────────┘                └──────────────────────┘
```

### 10.2 How Dynamic Binding Works (Step by Step)

When `ptr->virtualFunction()` is called:

1. **Follow the vptr** — the compiler generates code to access the object's vptr and reach the virtual table of the object's **actual class**.
2. **Look up the vtable** — at **runtime**, look up the virtual table entry for the appropriate function's address.
3. **Call the function** — jump to the address found in the vtable.

```
ptr -> [object]
      ├── vptr ──────> [vtable]
      │                ├── entry[0]: &Derived::func1()
      │                ├── entry[1]: &Derived::func2()
      │                └── entry[2]: &Derived::func3()
      └── data members
```

- Each virtual function occupies a fixed offset in the vtable.
- For a given class hierarchy, the vtable layout is consistent — the compiler knows the offset for each virtual function.
- Overriding a virtual function simply changes the address stored at that vtable slot for the derived class.

---

## 11. SUMMARY (from lecture)

### Four Types of Polymorphism

| Type | Binding Time | C++ Mechanism |
|------|-------------|---------------|
| Runtime / Inclusion / Overriding | Runtime | `virtual` functions + inheritance |
| Parametric | Compile time | Templates |
| Ad-hoc (Overloading) | Compile time | Multiple functions, same name, different signatures |
| Coercion (Casting) | Compile time | Implicit type conversion by compiler |

### Inclusion Polymorphism (Overriding) — Key Takeaways

- **Why is it important?** → Add new derived classes **without changing existing code**. The system is extensible.
- **Do NOT confuse** overriding with overloading:
  - Overriding = same name AND parameters, runtime dispatch, needs `virtual` + inheritance.
  - Overloading = same name, DIFFERENT parameters, compile-time resolution.
- Polymorphism **requires dynamic binding**.
- C++ defaults to **static binding** for efficiency; use the `virtual` keyword to enable dynamic binding.
- "If you don't use it, you don't pay for it" — C++ design philosophy.

---

## 12. MUST-MEMORIZE SYNTAX TEMPLATES

### Virtual Function Declaration

```cpp
class Base {
public:
    virtual void action();              // Virtual — can be overridden; dynamic binding
    virtual void mustImplement() = 0;   // Pure virtual — makes Base abstract
    virtual ~Base();                    // Virtual destructor — ALWAYS do this for base classes
    void nonVirtualFunc();              // Non-virtual — static binding; cannot be properly overridden
};
```

### Derived Class Override

```cpp
class Derived : public Base {
public:
    void action() override;            // Override (virtual optional in derived; override keyword C++11)
    void mustImplement() override;     // MUST implement all pure virtuals to be concrete
    ~Derived();                        // Destructor — automatically virtual if base's is virtual
};
```

### Dynamic Dispatch Pattern (Polymorphic Collection)

```cpp
// Abstract base
class Animal {
public:
    virtual void speak() = 0;           // Pure virtual → abstract
    virtual ~Animal() { }              // Virtual destructor
};

// Concrete derived classes
class Dog : public Animal {
public:
    void speak() { cout << "Woof!" << endl; }
};

class Cat : public Animal {
public:
    void speak() { cout << "Meow!" << endl; }
};

// Usage — polymorphic collection
int main() {
    Animal* animals[] = { new Dog(), new Cat() };
    for (Animal* a : animals) {
        a->speak();                    // Dynamic dispatch via vtable
    }
    for (Animal* a : animals) {
        delete a;                      // Correct destructor called (virtual)
    }
}
```

### Abstract Class Template

```cpp
class AbstractShape {
public:
    virtual double area() = 0;         // At least one pure virtual
    virtual void draw() = 0;
    virtual ~AbstractShape() { }       // Virtual destructor
    double getLabel() { return label; } // Non-virtual: shared implementation
private:
    double label;
};
// AbstractShape s;                    // ERROR: cannot instantiate abstract class
// AbstractShape* p;                   // OK: pointer to abstract class
```

### Virtual Destructor Template

```cpp
class BaseWithResources {
    int* data;
public:
    BaseWithResources() : data(new int[100]) { }
    virtual ~BaseWithResources() { delete[] data; }  // VIRTUAL — critical!
};
```

---

## 13. EXAM TRAPS

**1. Non-virtual methods use STATIC binding.** If `Base* p = new Derived();` and you call `p->nonVirtualFunc()`, it calls `Base`'s version — even if `Derived` has a function with the same name. The **pointer type** (`Base*`), not the object type, determines which function is called.

> [!success]- Show Answer
> Static binding means the compiler resolves the call at compile time using the declared type of the pointer. Since `p` is declared `Base*`, the compiler emits a call to `Base::nonVirtualFunc()`. The Derived version, even if it exists, is never reached through a base pointer.

---

**2. Forgetting `virtual` on the base class destructor.** `Base* p = new Derived; delete p;` — if `~Base()` is not virtual, only `Base`'s destructor runs. Derived's destructor never fires, causing resource leaks and dangling members.

> [!success]- Show Answer
> Without `virtual`, `delete p` uses static binding → calls only `Base::~Base()`. Derived-specific resources (dynamically allocated in Derived) are never freed. Fix: `virtual ~Base() { }` in the base class. Now dynamic binding calls `Derived::~Derived()` first, then automatically chains to `Base::~Base()`.

---

**3. Pure virtual function declared but not implemented in derived class.** The derived class remains abstract and cannot be instantiated. Attempting `new Derived` produces a compilation error.

> [!success]- Show Answer
> A class inheriting a pure virtual function inherits the `= 0` as well. Until ALL pure virtuals are overridden, the class remains abstract. Concrete instantiation requires all base pure virtuals to be implemented.

---

**4. Abstract classes CAN have pointers and references.** `Base* p;` is perfectly valid. `Base& r = someDerived;` is perfectly valid. Only direct instantiation is forbidden: `Base b;` or `new Base()` is an error.

> [!success]- Show Answer
> Abstract classes define an interface but lack complete implementation. Pointers and references don't create objects — they just refer to them. You can point to a concrete derived object through an abstract base pointer. This is exactly how polymorphic collections work.

---

**5. Calling a virtual function in a constructor/destructor does NOT dispatch dynamically.** Inside `Base::Base()`, calling `virtualFunc()` calls `Base`'s version even if the object being constructed is a `Derived` — the derived part hasn't been constructed yet.

> [!success]- Show Answer
> During construction, the object is built from base to derived. When `Base`'s constructor runs, the vptr still points to `Base`'s vtable (the derived parts don't exist yet). Similarly, during destruction, once `~Derived()` finishes, the vptr reverts to `Base`'s vtable before `~Base()` runs. Never call virtual functions in constructors/destructors expecting derived behavior.

---

**6. Virtual function overrides must match the EXACT signature.** Different return type (unless covariant), different const-ness, or different parameter types means you created a **new function** (hiding/overloading), not overriding the base virtual.

> [!success]- Show Answer
> The compiler matches overrides by exact signature. If the base has `virtual void foo(int)` and the derived defines `void foo(double)`, that's a completely different function — the base `foo(int)` remains inherited and callable. Use the `override` keyword in C++11+: `void foo(int) override` — the compiler errors if no matching base virtual exists.

---

**7. `this` is an implicit pointer to the CURRENT object.** Inside a member function, `*this` is the object that received the call. In a virtual function called through a base pointer, `this` points to the **actual derived object**.

> [!success]- Show Answer
> `this` is always the actual object, regardless of the pointer/reference type used to invoke the function. If you have `Base* p = new Derived(); p->virtualFunc();`, then inside `virtualFunc()`, `this` points to the `Derived` object. This is how virtual functions access the correct member data.

---

**8. Coercion is NOT the same as overriding.** `int add(int a, int b)` and `float add(float a, float b)` with a call `add(1, 1.0)` — the compiler converts (coerces) the `1.0` double to `int` to match the signature. This is compile-time magic, not runtime polymorphism.

> [!success]- Show Answer
> Coercion happens at compile time: the compiler implicitly converts argument types to match available function signatures. No virtual table, no runtime dispatch, no inheritance required. It's a convenient type conversion, not dynamic behavior selection based on object type.

---

**9. Overloading vs. Overriding confusion.** If you have `virtual void draw(int)` in the base and write `void draw(double)` in the derived, you have OVERLOADED, not overridden. The base's `draw(int)` remains intact and callable, while a new `draw(double)` exists in the derived scope.

> [!success]- Show Answer
> Different parameter types = different function. The derived class now has TWO `draw` functions: the inherited `draw(int)` and the new `draw(double)`. Through a base pointer, only `draw(int)` is accessible (because the base doesn't know about `draw(double)`). Always match the signature exactly when overriding.

---

**10. Slicing problem when passing by value.** Passing a derived object to a function expecting a base object by VALUE slices off the derived portion. The function receives only the base part — virtual dispatch still works (uses the base's vtable), but derived data is lost.

> [!success]- Show Answer
> Pass-by-value creates a copy. Since the parameter is of type `Shape` (not `Shape&` or `Shape*`), only enough memory for a `Shape` is allocated. The derived-specific data members are sliced off. Always pass polymorphic objects by pointer or reference to preserve the full object.

```cpp
void drawShape(Shape s) { s.draw(); }   // SLICING — only Shape part copied
void drawShape(Shape& s) { s.draw(); }  // CORRECT — full object preserved
```

---

**11. A class becomes abstract if it inherits a pure virtual function and doesn't override it.** Even if the class overrides MOST pure virtuals, one remaining pure virtual keeps the class abstract.

> [!success]- Show Answer
> Abstractness is "infectious" down the hierarchy. A derived class must override ALL inherited pure virtual functions to become concrete. If `AbstractBase` has 5 pure virtuals, a `Derived` that overrides 4 of them is still abstract and cannot be instantiated.

---

**12. You CAN provide a body for a pure virtual function.** `virtual void draw() = 0 { /* body */ }` is valid C++. Derived classes can call it explicitly via `Base::draw()`. But the class remains abstract because of the `= 0`.

> [!success]- Show Answer
> A pure virtual function CAN have an implementation. This is useful when you want to force derived classes to override but also provide a default implementation they can call. The class is still abstract despite having a body for the pure virtual — the `= 0` is what makes it abstract, not the lack of a body.

---

**13. Virtual functions work through REFERENCES too, not just pointers.** `Base& ref = someDerived; ref.virtualFunc();` performs dynamic dispatch exactly the same as through a pointer.

> [!success]- Show Answer
> Dynamic binding applies to both pointers and references. The vptr/vtable mechanism is the same — the compiler generates a vtable lookup for any access through a base-class reference. This is why pass-by-reference avoids slicing and preserves polymorphism.

---

**14. Multiple inheritance and virtual functions.** If a class inherits from two base classes that both have virtual functions, the derived class may have multiple vtables (one per base). Know that this complexity exists but focus on single inheritance for exams.

> [!success]- Show Answer
> With multiple inheritance, the derived object may contain multiple vptrs — one for each base class path. The compiler generates appropriate adjustments. This is why C++'s object model is more complex than single-inheritance languages. Know that multiple vtables exist in such cases.

---

**15. Static member functions CANNOT be virtual.** A static function belongs to the class, not to any object. Since there is no `this` pointer and no object, there is no vptr to follow — virtual dispatch is impossible.

> [!success]- Show Answer
> Virtual dispatch requires a vptr, which is stored per-object. Static functions have no object context — they belong to the class itself. Therefore they cannot be virtual. Also, constructors cannot be virtual (the vptr isn't set up until the constructor runs).

---

**16. The `virtual` keyword in derived classes is OPTIONAL but the `override` keyword (C++11) is recommended.** If you omit `virtual` in the derived class, the function is still virtual if the base declared it so. However, `override` catches signature mismatches.

> [!success]- Show Answer
> Once virtual, always virtual down the hierarchy. Writing `virtual void draw() override` in a derived class is redundant but explicit. Using just `void draw() override` is idiomatic C++11 — the compiler confirms there's a matching base virtual and errors if there isn't.

---

**17. vtable cost: one vptr per object + one vtable per class with virtual functions.** Memory overhead is small (one pointer per object, one vtable per class), but the indirection adds a small runtime cost per virtual call.

> [!success]- Show Answer
> Each object of a class with virtual functions gets a vptr (typically 4 or 8 bytes). Each class with virtual functions gets one vtable (shared by all objects of that class). The runtime cost is: follow vptr → index into vtable → call function. This is one extra indirection compared to a direct call. In practice, the cost is negligible for most applications.

---

## 14. HAND-CODING DRILLS

### Drill 1: Static vs Dynamic Binding

```cpp
#include <iostream>
using namespace std;

class Parent {
public:
    void hello() { cout << "Parent hello "; }
    virtual void bye() { cout << "Parent bye "; }
};

class Child : public Parent {
public:
    void hello() { cout << "Child hello "; }
    void bye() { cout << "Child bye "; }
};

int main() {
    Parent* p = new Child();
    p->hello();  // line A
    p->bye();    // line B
    Child c;
    c.hello();   // line C
    c.bye();     // line D
    delete p;
}
```

What is the EXACT output? Explain each line.

> [!success]- Show Answer
> Output: `Parent hello Child bye Child hello Child bye`
>
> - **Line A**: `hello()` is NON-virtual. Static binding uses the pointer type `Parent*` → calls `Parent::hello`.
> - **Line B**: `bye()` is virtual. Dynamic binding follows vptr to `Child`'s vtable → calls `Child::bye`.
> - **Line C**: `c` is a `Child` object on the stack. `hello()` resolves to `Child::hello` (hides the parent version via name hiding).
> - **Line D**: `bye()` is virtual, and `c` is a `Child` → dynamic dispatch calls `Child::bye`.

---

### Drill 2: Missing Virtual Destructor

```cpp
class FileHandler {
    char* buffer;
public:
    FileHandler() { buffer = new char[1024]; }
    ~FileHandler() { delete[] buffer; }
};

class EncryptedFileHandler : public FileHandler {
    char* key;
public:
    EncryptedFileHandler() { key = new char[32]; }
    ~EncryptedFileHandler() { delete[] key; }
};

int main() {
    FileHandler* f = new EncryptedFileHandler();
    delete f;
}
```

What is the bug? What exactly leaks? Fix it with the minimal change.

> [!success]- Show Answer
> `~FileHandler()` is NOT virtual. When `delete f` is called through a `FileHandler*`, static binding calls ONLY `~FileHandler()`. The `EncryptedFileHandler` destructor never runs → `key` (32 bytes) leaks. The `buffer` IS properly deleted (via `FileHandler`'s destructor).
>
> **Fix**: `virtual ~FileHandler() { delete[] buffer; }`
>
> Now dynamic binding calls `~EncryptedFileHandler()` first (deleting `key`), then automatically calls `~FileHandler()` (deleting `buffer`). Both resources are freed.

---

### Drill 3: Abstract Payment System

Design a payment system where `PaymentProcessor` is an abstract base class with:

- A pure virtual `bool charge(double amount)` that returns true if successful
- A virtual `void refund(double amount)` that prints `"Refunding [amount] via generic processor"`
- A concrete `double getFee(double amount)` that returns `amount * 0.03`

Then write `StripeProcessor` that:

- Overrides `charge` to print `"Stripe: charging [amount]"` and return true
- Does NOT override `refund`
- Cannot be instantiated if it doesn't override a certain function

Finally write `PayPalProcessor` that overrides both `charge` and `refund`, and is fully concrete.

> [!success]- Show Answer
> ```cpp
> class PaymentProcessor {
> public:
>     virtual bool charge(double amount) = 0;  // pure virtual → abstract
>     virtual void refund(double amount) {
>         cout << "Refunding " << amount << " via generic processor" << endl;
>     }
>     double getFee(double amount) {           // non-virtual: shared by all
>         return amount * 0.03;
>     }
>     virtual ~PaymentProcessor() { }          // virtual destructor
> };
>
> class StripeProcessor : public PaymentProcessor {
> public:
>     bool charge(double amount) {
>         cout << "Stripe: charging " << amount << endl;
>         return true;
>     }
>     // refund() NOT overridden — uses base version (generic message)
> };
>
> class PayPalProcessor : public PaymentProcessor {
> public:
>     bool charge(double amount) {
>         cout << "PayPal: charging " << amount << endl;
>         return true;
>     }
>     void refund(double amount) {
>         cout << "PayPal: refunding " << amount << endl;
>     }
> };
> ```

---

### Drill 4: Coercion vs. Overriding

```cpp
class Calculator {
public:
    int add(int a, int b) {
        cout << "Calculator::add(int,int) ";
        return a + b;
    }
    float add(float a, float b) {
        cout << "Calculator::add(float,float) ";
        return a + b;
    }
};

class Scientific : public Calculator {
public:
    int add(int a, int b) {
        cout << "Scientific::add(int,int) ";
        return a + b;
    }
};

int main() {
    Calculator* c1 = new Calculator();
    Calculator* c2 = new Scientific();

    c1->add(1, 2);        // line A
    c1->add(1.0f, 2.0f);  // line B
    c1->add(1, 2.0f);     // line C

    c2->add(3, 4);        // line D
    c2->add(3.0f, 4.0f);  // line E

    delete c1; delete c2;
}
```

What is the EXACT output? Explain whether each line uses coercion, overloading, overriding, or static binding.

> [!success]- Show Answer
> ```
> Calculator::add(int,int) Calculator::add(float,float) Calculator::add(int,int) Calculator::add(int,int) Calculator::add(float,float)
> ```
>
> - **Line A**: `add(int, int)` exactly matches → overloading resolution picks `Calculator::add(int,int)`.
> - **Line B**: `add(float, float)` exactly matches → overloading resolution picks `Calculator::add(float,float)`.
> - **Line C**: `add(int, double)` — no exact match. The `2.0f` would be float but `2.0` is double. The `int` version is the best match after coercion (double→int) → calls `Calculator::add(int,int)`. This is **coercion + overloading**.
> - **Line D**: `c2` is `Calculator*` pointing to `Scientific`. `add()` is NON-virtual (no `virtual` keyword in base). Static binding → calls `Calculator::add(int,int)`. The `Scientific` override is **NOT reached** because there's no dynamic dispatch!
> - **Line E**: Same reason — non-virtual, static binding → `Calculator::add(float,float)`.
>
> **Key lesson**: Without `virtual`, even if derived overrides a function, calls through base pointer use static binding and call the base version. Coercion is a compile-time argument conversion, separate from overriding.

---

### Drill 5: Virtual Table Conceptual Tracing

Given the following class hierarchy:

```cpp
class A {
public:
    virtual void f1() { cout << "A::f1 "; }
    virtual void f2() { cout << "A::f2 "; }
    void f3() { cout << "A::f3 "; }
};

class B : public A {
public:
    void f1() { cout << "B::f1 "; }
    virtual void f4() { cout << "B::f4 "; }
};

class C : public B {
public:
    void f2() { cout << "C::f2 "; }
    void f4() { cout << "C::f4 "; }
};
```

Answer these questions:
1. How many virtual functions does each class have in its vtable?
2. What does each call output?

```cpp
A* p1 = new A();   p1->f1(); p1->f2(); p1->f3();
A* p2 = new B();   p2->f1(); p2->f2(); p2->f3();
A* p3 = new C();   p3->f1(); p3->f2(); p3->f3();
```

> [!success]- Show Answer
> **Vtables**:
> - `A`'s vtable: 2 entries → `f1`, `f2`
> - `B`'s vtable: 3 entries → `f1` (overridden), `f2` (inherited from A), `f4` (new virtual in B)
> - `C`'s vtable: 3 entries → `f1` (inherited from B's override), `f2` (overridden), `f4` (overridden)
>
> **Output**: `A::f1 A::f2 A::f3 B::f1 A::f2 A::f3 B::f1 C::f2 A::f3`
>
> - `p1->f1()`: A object, virtual → `A::f1`
> - `p1->f2()`: A object, virtual → `A::f2`
> - `p1->f3()`: NON-virtual → static binding → `A::f3`
> - `p2->f1()`: B object, virtual → vtable lookup → `B::f1`
> - `p2->f2()`: B object, virtual → B's vtable entry still points to `A::f2` (B didn't override it) → `A::f2`
> - `p2->f3()`: NON-virtual → static binding → `A::f3`
> - `p3->f1()`: C object, virtual → vtable lookup (inherited from B) → `B::f1`
> - `p3->f2()`: C object, virtual → C's vtable has C's override → `C::f2`
> - `p3->f3()`: NON-virtual → static binding → `A::f3`

---

### Drill 6: Abstract Derived Classes

```cpp
class Shape {
public:
    virtual void draw() = 0;
    virtual double area() = 0;
    virtual void rotate(double angle) { cout << "Rotating by " << angle; }
    virtual ~Shape() { }
};

class Circle : public Shape {
    double r;
public:
    Circle(double radius) : r(radius) { }
    void draw() { cout << "Drawing Circle"; }
    double area() { return 3.14159 * r * r; }
    // rotate() NOT overridden — inherits base implementation
};

class Square : public Shape {
    double side;
public:
    Square(double s) : side(s) { }
    void draw() { cout << "Drawing Square"; }
    // area() NOT overridden
    // rotate() NOT overridden
};

class FilledSquare : public Square {
    string color;
public:
    FilledSquare(double s, string c) : Square(s), color(c) { }
    double area() { /* ... */ }
};

int main() {
    Shape s;              // line 1 — ERROR or OK?
    Circle c(5.0);        // line 2 — ERROR or OK?
    Square sq(4.0);       // line 3 — ERROR or OK?
    FilledSquare fs(3.0, "red"); // line 4 — ERROR or OK?
    Shape* shapes[2];
    shapes[0] = new Circle(2.0);
    shapes[1] = new FilledSquare(5.0, "blue");
    for (int i = 0; i < 2; i++) {
        shapes[i]->rotate(90);   // line 5 — which rotate runs?
    }
}
```

Which lines compile? Which are errors? Explain. For line 5, which `rotate()` runs for each shape?

> [!success]- Show Answer
> - **Line 1 — ERROR**: `Shape` is abstract (`draw` and `area` are pure virtual) — cannot instantiate.
> - **Line 2 — OK**: `Circle` overrides both pure virtuals → fully concrete.
> - **Line 3 — ERROR**: `Square` inherits `area() = 0` from `Shape` without overriding it → `Square` is still abstract → cannot instantiate.
> - **Line 4 — OK**: `FilledSquare` overrides `area()` — resolving the only remaining pure virtual from `Square`/`Shape`. It also inherits `draw()` from `Square`. Now concrete.
> - **Line 5**: Both call `Shape::rotate(90)` — the base implementation. Neither `Circle` nor `FilledSquare` override `rotate`. Since `rotate` is virtual but NOT overridden, the vtable entry points to `Shape::rotate` for both. Output: `Rotating by 90Rotating by 90`.

---

### Drill 7: Static vs Dynamic Binding Full Trace

```cpp
#include <iostream>
using namespace std;

class Vehicle {
public:
    void start() { cout << "Vehicle::start "; }
    virtual void drive() { cout << "Vehicle::drive "; start(); }
    virtual void stop() { cout << "Vehicle::stop "; }
    virtual ~Vehicle() { cout << "~Vehicle "; }
};

class Car : public Vehicle {
public:
    void start() { cout << "Car::start "; }
    void drive() { cout << "Car::drive "; start(); }
    void stop() { cout << "Car::stop "; }
    ~Car() { cout << "~Car "; }
};

class SportsCar : public Car {
public:
    void drive() { cout << "SportsCar::drive "; start(); }
    ~SportsCar() { cout << "~SportsCar "; }
};

int main() {
    Vehicle* v1 = new Car();
    v1->start();           // line A
    v1->drive();           // line B
    Vehicle* v2 = new SportsCar();
    v2->drive();           // line C
    v2->stop();            // line D
    delete v1;             // line E
    delete v2;             // line F
}
```

Write the EXACT output, differentiating between static binding and dynamic binding at each line.

> [!success]- Show Answer
> ```
> Vehicle::start Car::drive Car::start SportsCar::drive Car::start Car::stop ~Car ~Vehicle ~SportsCar ~Car ~Vehicle
> ```
>
> - **Line A**: `start()` is NON-virtual → static binding using `Vehicle*` → `Vehicle::start`
> - **Line B**: `drive()` is virtual → dynamic binding. Object is `Car` → `Car::drive` → prints `Car::drive `, then calls `start()`. `start()` is NON-virtual → static binding using `this` (which is a `Car*` inside `Car::drive`) → `Car::start`
> - **Line C**: `drive()` is virtual → dynamic binding. Object is `SportsCar` → `SportsCar::drive` → prints `SportsCar::drive `, then calls `start()`. `start()` is NON-virtual → static binding using `this` (which is a `SportsCar*` but `start` is not defined in `SportsCar`) → inherited `Car::start` (name resolution goes up the hierarchy) → `Car::start`
> - **Line D**: `stop()` is virtual → dynamic binding. `SportsCar` inherits `Car::stop` → `Car::stop`
> - **Line E**: `~Vehicle()` is virtual → dynamic binding calls `~Car()` first → prints `~Car `, then chains to `~Vehicle()` → prints `~Vehicle `
> - **Line F**: `~Vehicle()` is virtual → dynamic binding calls `~SportsCar()` first → prints `~SportsCar `, then `~Car()` → prints `~Car `, then `~Vehicle()` → prints `~Vehicle `

---

> [!NOTE]
> This study guide covers all lecture content for Lec9: Polymorphism. Review the four types of polymorphism, understand the difference between static and dynamic binding, memorize the syntax for virtual functions / pure virtual / virtual destructors / abstract classes, and practice the drills until you can trace any code snippet involving base-class pointers and virtual function calls without hesitation.
