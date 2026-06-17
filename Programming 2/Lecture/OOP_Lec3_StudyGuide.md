# Lec3: Introduction to OOP — Study Guide

## 1. CONCEPT CARD: Object-Oriented Programming
### 1.1 What It Is
A way of writing programs by grouping related data and the functions that operate on that data together into self-contained units called objects.
### 1.2 What Problem It Solves
Before OOP, programs were written in a structured (procedural) style. Data was stored globally, and any function anywhere in the program could reach out and modify it. When requirements changed — which they always do in real software — a small tweak could silently break distant, unrelated parts of the program because everything shared the same global data. OOP fixes this by bundling data together with the functions (methods) that are allowed to touch it. Each object protects its own data; other parts of the program can only interact through well-defined interfaces. Changing one object's internals no longer ripples through the entire codebase.
### 1.3 How It Works
1. Identify the real-world "things" in your problem (a student, a course, a GPS waypoint).
2. For each thing, define a **class** — a blueprint listing what data it stores and what actions it can perform.
3. Create **objects** (instances) from the class blueprint. Each object holds its own copy of the data.
4. Objects communicate by sending **messages** (calling methods on each other).
5. A program becomes a society of interacting objects, each responsible for its own behaviour.
### 1.4 Concrete Example
A GPS navigation system:
- `Waypoint` class stores a latitude, longitude, and altitude. Its methods let you calculate the distance to another Waypoint.
- `Route` class holds an ordered list of Waypoints. Its methods compute total distance and estimated travel time.
- `Navigator` class uses a Route and the current GPS position to determine the next turn instruction.
- Each class owns its data. `Route` does not directly fiddle with `Waypoint`'s lat/lon — it asks the Waypoint to compute the distance itself.
### 1.5 What It Is NOT
OOP is NOT just "putting code inside classes." If you write classes that are merely namespaces for a pile of unrelated functions sharing no cohesive state, you are doing structured programming in a class-shaped costume. True OOP requires objects to bundle meaningful **state** together with the **behaviour** that acts on that state.

## 2. PROGRAMMING PARADIGMS & METHODOLOGY
### 2.1 Steps in Solving a Programming Problem
```
Analysis  →  Design  →  Coding  →  Programming languages  →  Management
```
Every software solution follows this chain. You first analyze the requirements, then design a solution, code it using a programming language, and manage the project through its lifecycle.
### 2.2 Thinking Methodology: Induction
Induction goes **from specialization to generalization**. You observe many specific examples and extract the common concept.

Example: You see different buses — a luxury bus, a school bus, a city bus. By noticing their shared characteristics (large passenger vehicle, multiple seats, used for public transport), you induce the abstract concept **"Bus."** Even higher: you induce **"Vehicle"** from Automobile, Motorcycle, and Bus.

```
        Vehicle
           |
   ┌───────┼───────┐
Automobile Motorcycle  Bus
   |                    |
Sedan  Sports Car    Luxury Bus  School Bus
```

> [!success]- Show Answer
> Induction travels UP the hierarchy — from concrete instances to an abstract class. The diagram shows how specific vehicles (bottom) generalize to Vehicle (top).

### 2.3 Thinking Methodology: Deduction
Deduction goes **from generalization to specialization**. You start with a known concept and reason about whether a particular case fits.

Example: Once you have learned the concept **"Bus,"** you can look at a new vehicle and deduce whether it IS or IS NOT a bus by checking it against the properties that define bus-hood (large size, multiple passenger seats, public transport purpose).

> [!success]- Show Answer
> Deduction travels DOWN the hierarchy — from an abstract class to concrete instances. You use the definition to classify specific things.

### 2.4 Concepts and Relationships
Understanding how concepts relate to each other is fundamental to OO design:

| Relationship | Example | Meaning |
|---|---|---|
| **USES** | A rectangle **uses** lines | One object calls or depends on another without owning it. Temporary, loose coupling. |
| **IS-A** (Inheritance) | A circle **is an** ellipse | One class is a specialized version of another. A circle is an ellipse where both radii are equal. |
| **HAS-A / IS PART OF** (Composition) | A wheel **is part of** an automobile | One object contains another as a component. The wheel's lifetime is tied to the car. |
| **CREATES** (Factory) | A set **creates** its elements | One object is responsible for instantiating and managing another. |

> [!success]- Show Answer
> - **USES**: rectangle → lines (drawing operation, loose dependency)
> - **IS-A**: circle → ellipse (inheritance hierarchy)
> - **HAS-A**: wheel → automobile (the wheel is a part; composition)
> - **CREATES**: set → elements (factory pattern; the set manages element lifecycle)

### 2.5 Top-Down vs Bottom-Up Approaches
#### Top-Down
- A single large module is split into progressively smaller modules.
- Flows **General → Specific**.
- Use when **requirements are clear at the first instance** and unlikely to change.

#### Bottom-Up
- Many small modules are grouped together to form a single large module.
- Flows **Specific → General**.
- Use when **requirements keep adding / changing** over time.

> [!success]- Show Answer
> **Top-Down** starts with the big picture and carves it into pieces. **Bottom-Up** starts with tiny, reusable pieces and assembles them. Most real-world software uses bottom-up (or a mix) because requirements inevitably change.

### 2.6 Structured Programming (Pre-OOP)
Structured programming organises code using functions and divides the program into modules. Each module has its own data and functions that can be called by other modules.

```
        MAIN PROGRAM
              |
         GLOBAL DATA
              |
   ┌──────────┼──────────┐
FUNCTION 1  FUNCTION 2  FUNCTION 3
   └──────────┼──────────┘
         FUNCTION 4    FUNCTION 5
```

**The fundamental problem:** There is no encapsulation. Global data sits exposed in the open. Any function can read or modify any piece of global data at any time. As the program grows, tracking down which function changed what becomes a nightmare. A tiny modification to global data in one module can silently corrupt behaviour in a completely unrelated module.

> [!success]- Show Answer
> Structured programming = functions + modules + global data. It works for small programs but collapses under complexity because nothing protects the data from indiscriminate access.

### 2.7 Why OOP? (Significance)
- **Real-world requirements keep changing and accumulating.** The bottom-up nature of OOP accommodates this naturally — you can add new classes without disrupting existing ones.
- **Easy representation of real-world objects, their states, and their abilities.** You map the problem domain directly into code.
- **Interaction with same-type and other-type objects.** Objects collaborate naturally through method calls.
- **Polymorphism and Overloading support.** One interface, many behaviours.
- **Save development time via code reuse.** Once a class is created and tested, it can be used in other applications without rewriting.
- **Easier debugging.** Classes can be tested independently (unit testing), and reused objects have already been battle-tested in previous projects.

> [!success]- Show Answer
> OOP's key win: it models the real world, tolerates changing requirements, reuses tested code, and isolates bugs. You debug a class, not the entire program at once.

## 3. OBJECT-ORIENTATION PHILOSOPHY
### 3.1 Core Principles
- **Everything is an object.**
- **Any system is composed of objects** — and a system is itself an object that can be part of a larger system.
- **The evolution and development of a system** is caused by the interactions of objects inside and outside that system.

> [!success]- Show Answer
> Three philosophical pillars: (1) everything is an object, (2) systems are built from objects, (3) change happens through object interactions.

### 3.2 Object Properties
- Objects have **both data AND methods** (state + behaviour bundled together).
- Objects **of the same class** have the same data elements and methods (same blueprint, different values).
- Objects **send and receive MESSAGES** to invoke actions. A message is a call to a method on a destination object.
- **Key idea:** *"The real world can be accurately described as a collection of objects that interact."*

```
┌──────────┐     Message     ┌──────────┐
│ Object A │ ──────────────→ │ Object B │
│  Data    │                 │  Data    │
│ Methods  │ ←────────────── │ Methods  │
└──────────┘     Message     └──────────┘
```

> [!success]- Show Answer
> Objects hold data + methods. Same-class objects share structure but hold different values. They communicate exclusively through messages (method calls). The whole world is just objects talking to objects.

### 3.3 "Everything is an Object" Examples
From smallest to largest scale — all of these can be modeled as objects:
- A **student**, a **professor**
- A **desk**, a **chair**, a **classroom**, a **building**
- A **university**, a **city**, a **country**
- The **world**, the **universe**
- A subject: **CS**, **IS**, **Math**, **History**

> [!success]- Show Answer
> Every noun in the problem domain can be an object. Nothing is too small (a chair) or too large (the universe) to be represented as an object with data and behaviour.

### 3.4 Systems Composed of Objects
Systems are themselves objects, built from smaller objects:
- An **education system** (composed of schools, students, curricula)
- An **economic system** (composed of markets, currencies, transactions)
- An **information system** (composed of databases, users, queries)
- A **computer system** (composed of CPU, memory, storage, OS)

> [!success]- Show Answer
> Every system is an object made of smaller objects. This nesting continues recursively — a system's components are objects, and the system itself is an object inside a larger system.

### 3.5 Development Through Interactions
A system evolves through interactions among its internal and external objects.

**Example — VGU (Vietnamese-German University):**

Inside VGU (internal interactions):
- **Students** interact with **professors** (learning, research)
- **Staff** interact with **board governance** (administration, policy)

Outside VGU (external interactions):
- VGU interacts with **state governance** (compliance, funding, regulation)

> [!success]- Show Answer
> VGU is defined NOT by any single component but by the ongoing interactions among students, professors, staff, board governance (internal), and state governance (external). Change any interaction and you change the system.

## 4. DESIGN METHODOLOGY
### 4.1 Object-Orientation as Design (OOD)
Object-Oriented Design uses **objects as the building blocks** of a program. Each object represents a real-world abstraction within the application domain. Rather than thinking in terms of functions and data flow, you think in terms of objects and their collaborations.

> [!success]- Show Answer
> OOD = designing software by identifying objects (real-world abstractions) and defining how they interact. Objects are the construction material.

### 4.2 Induction and Deduction in Design
- **Induction:** objects → a class. You look at several concrete objects, find their commonalities, and create a class definition. *Tools can do this automatically* (reverse engineering, refactoring tools).
- **Deduction:** a class → objects. You take an existing class blueprint and instantiate specific objects from it. *Usually done by programmers* when writing code.

> [!success]- Show Answer
> Induction: observing objects to infer a class (tool-assisted). Deduction: using a class to create objects (programmer's daily job — `Student s;` creates an object from the Student class).

### 4.3 Top-Down and Bottom-Up in Design
- **Top-Down:** from a **super-class to sub-classes**. Start with the most general concept and progressively specialise. (Vehicle → Automobile, Motorcycle, Bus)
- **Bottom-Up:** from **sub-classes to a super-class**. Start with many specific classes and extract commonalities into a parent class. (Sedan, Sports Car → Automobile)

> [!success]- Show Answer
> Top-Down design creates sub-classes from a super-class. Bottom-Up design creates a super-class by extracting shared features from existing sub-classes. Both directions are valid and often used together.

## 5. THE FOUR PILLARS OF OOP
### 5.1 Abstraction
Abstraction means **focusing only on the important facts** about the problem at hand and ignoring unnecessary details. You design, produce, and describe something so it can be used without knowing how it works internally.

**Analogy:** When you drive a car, you don't need to know how gasoline and air are mixed and ignited in the engine. You only need to know how to use the controls — steering wheel, accelerator, brake. The complex internal combustion details are **abstracted away** behind a simple interface.

#### Abstract Data Types (ADT)
An ADT defines the **interface** to a data abstraction **without specifying implementation details**.

ADT properties:
1. It **exports a type** (a new data type name, like `Complex` or `Stack`).
2. It **exports a set of operations** (functions that work on that type).
3. **Axioms and preconditions** define the application domain — the rules that all implementations must obey.

#### ADT in C++
- **Access modifiers** (`private`, `public`, `protected`) provide abstraction — they hide what outsiders shouldn't see.
- **Functions** also provide abstraction — the function name (`sort()`) hides the sorting algorithm inside.
- **Private variables** are hidden from other classes; only the owning class can access them.
- The **function name** in a call hides implementation details — `computeGPA()` shows the outline of functionality without revealing the calculation algorithm.

> [!success]- Show Answer
> Abstraction: expose WHAT something does, hide HOW it does it. Access modifiers hide data, functions hide algorithms. An ADT exports a type + operations + rules, with no implementation exposed.

### 5.2 Encapsulation
Encapsulation is the process of **bringing together the data and methods** of an object into a single unit. The class definition provides this feature.

Encapsulation enables:
- **Modularity** — each class is a self-contained module.
- **Controlled access to data** — data is private; outsiders use public methods.
- **Separation of implementation from interface** — change the internals; callers see no difference.
- **Extension of built-in types** — you create new types that behave like built-in ones.

#### Complex Numbers Example
A complex number has a **real part** and an **imaginary part**, both represented by real numbers. Operations include addition, subtraction, multiplication, and division.

To represent a complex number, you must define its data structure. There are at least two ways:

**Approach 1 — Two-valued array:**
```cpp
c[0] = real part    // x = c[0]
c[1] = imaginary part  // y = c[1]
```

**Approach 2 — Two-valued record (struct):**
```cpp
c.r = real part     // x = c.r
c.i = imaginary part  // y = c.i
```

In both cases, `x` equals "the real part of `c`." The **semantics** (meaning) are identical — but the **data structure** differs. The ADT definition says that each access to the data structure **should have an operation defined**. Direct array access (`c[0]`) contradicts this principle — it exposes the raw storage details.

**The encapsulation solution:**
Once the ADT `Complex` is created, you use it like any built-in type:
```cpp
Complex a;
```

For operations like addition, the `add` operation **encapsulates** the details. The caller simply *"adds two complex numbers"* without knowing which internal data structure is used:
```cpp
Complex result = a.add(b);   // caller knows nothing about arrays vs. records inside
```

> [!success]- Show Answer
> Encapsulation bundles data + methods together. The Complex example proves that two different internal representations (array vs. struct) can have identical external behaviour. Encapsulation hides which representation is used, so the caller never depends on internal details. Changing internals never breaks external code.

### 5.3 Inheritance
Inheritance enables **code reusability**. A new abstract data type (derived class) can **inherit** the data and functionality of an existing type (parent class), and is allowed to **modify** some of those entities and **add new ones**.

#### Terminology

| Term | Definition |
|---|---|
| **Class** | The abstract data type (ADT) in object-oriented languages. |
| **Object** | An instance of a class — a concrete entity with actual data values. |
| **Derived class (subclass)** | A class defined through inheritance from another class. |
| **Parent class (superclass)** | A class from which a new class is derived. |
| **Methods** | The subprograms that define the operations on objects of a class. |
| **Messages** | Calls to methods. A message has two parts: a method name and the destination object. |
| **Message Protocol (Message Interface)** | The entire collection of an object's methods — its public API. |

#### Inheritance Hierarchy

```
               Superclass
                Vehicle
                   |
       ┌───────────┼───────────┐
   Automobile    Motorcycle     Bus
       |                        |
   Sedan  Sports Car    Luxury Bus  School Bus
```

Each level inherits properties from all levels above it. A `School Bus` inherits everything from `Bus`, which inherits from `Vehicle`.

#### Student Example
```
          New Class
          Students
              |
    ┌─────────┴─────────┐
  Objects            Objects
  Trung (Data+Methods)   Linh (Data+Methods)
              |
    Master's Student IS-A Student
    (Derived class of Student class)
         Master Students
```

A Master's Student **IS-A** Student — it inherits all properties of Student and adds or modifies its own.

> [!success]- Show Answer
> Inheritance = "is-a" relationship. A derived class inherits data + methods from its parent, can modify inherited behaviour, and can add new features. Think Vehicle → Bus → School Bus: each level gets everything from above plus its own specialisations.

### 5.4 Polymorphism
Polymorphism is the **ability of objects to respond differently to the same message or function call**.

- **Poly** = Many
- **Morph** = Form
- **Polymorphism** = the ability to co-exist in more than one form

**In C++:** Polymorphism is implemented through **function overloading** and **operator overloading** — the same function name or operator symbol behaves differently depending on the types or number of arguments.

> [!success]- Show Answer
> Same message, different behaviour depending on who receives it. In C++, function overloading (`add(int, int)` vs `add(double, double)`) and operator overloading (`+` for Complex vs `+` for int) are concrete implementations of polymorphism.

## 6. MUST-MEMORIZE SYNTAX TEMPLATE
```cpp
class ClassName {          // Declare a class (blueprint)
private:                   // Data hidden from outsiders
    int dataMember;        // Each object gets its own copy
public:                    // Interface visible to everyone
    ClassName(int val);    // Constructor: initializes new objects
    int getData();         // Accessor: reads data safely
    void setData(int v);   // Mutator: changes data with validation
};                         // SEMICOLON IS MANDATORY
```

> [!success]- Show Answer
> Every class needs: (1) the `class` keyword + name, (2) `private:` data members, (3) `public:` constructor + accessor + mutator, (4) a semicolon after the closing brace. Missing the semicolon is the most common exam compiler error.

## 7. EXAM TRAPS
### Trap 1: Missing Semicolon After Class Closing Brace
```cpp
class Foo {
    int x;
}     // ← NO SEMICOLON — compiler error!

class Bar {
    int y;
};    // ← Correct
```
> [!success]- Show Answer
> A class definition MUST end with `};`. The semicolon is not optional. Forgetting it is one of the most common syntax errors in C++ class declarations.

### Trap 2: Confusing Class (Blueprint) with Object (Instance)
```
"Student" is a class — it describes what every student has.
"Trung" is an object — it is one specific student with actual data.
```
You cannot store data in a class; you store data in objects created from the class.
> [!success]- Show Answer
> A class = blueprint (design). An object = instance (a real thing built from the design). You write code in the class; your program creates and manipulates objects. You can't call `Student.getName()` — you call `trung.getName()` on an object.

### Trap 3: "Private Means Absolutely Nobody Can See It" — FALSE
```cpp
class X {
private:
    int secret;
public:
    void peek(X& other) {
        int leaked = other.secret;  // LEGAL! Same class.
    }
};
```
> [!success]- Show Answer
> Private access is **per-class, not per-object**. Two objects of the same class CAN access each other's private members. The compiler checks the class, not which specific object you're poking.

### Trap 4: Default Access in `class` vs `struct`
```cpp
class Foo { int x; };     // x is PRIVATE by default
struct Bar { int y; };    // y is PUBLIC by default
```
> [!success]- Show Answer
> In a `class`, members default to `private`. In a `struct`, members default to `public`. They are otherwise identical. Adding `private:` and `public:` labels explicitly is considered best practice regardless.

### Trap 5: Confusing Abstraction with Encapsulation
- **Abstraction** = hiding unnecessary details (WHAT, not HOW). Focus on essential features.
- **Encapsulation** = bundling data together with the methods that operate on that data (WHERE, together).
> [!success]- Show Answer
> Abstraction is about **perspective** — the user sees a simple interface. Encapsulation is about **packaging** — data and methods live inside the same box. They work together but are distinct concepts. A class can be encapsulated without being well-abstracted, and vice versa in theory (though OOP combines both).

### Trap 6: Thinking "Everything Must Be an Object"
C++ is a **multi-paradigm** language. It has:
- Free (standalone) functions that belong to no class
- Primitive types (`int`, `double`, `char`) that are not class objects
- Global variables (though you should avoid them)
> [!success]- Show Answer
> "Everything is an object" is a **philosophy** for design thinking, not a language constraint in C++. Not every line of C++ code must live inside a class. Free functions and primitives are valid and often necessary.

### Trap 7: Confusing "IS-A" vs "HAS-A" vs "USES" Relationships
| Relationship | OOP Feature | Example |
|---|---|---|
| IS-A | Inheritance | A sports car IS-A car |
| HAS-A / IS PART OF | Composition | An engine IS PART OF a car |
| USES | Dependency | A driver USES a car |
> [!success]- Show Answer
> IS-A = inheritance (subclassing). HAS-A = composition (member objects). USES = dependency (parameter or local variable). Picking the wrong relationship leads to bad class hierarchies. If you inherit when you should compose, you get fragile, over-coupled code.

### Trap 8: ADT — Confusing Interface with Implementation
An ADT defines **WHAT** operations exist, NOT **HOW** they work. The interface is the contract; the implementation is the hidden mechanism.
```cpp
// Interface (ADT definition):
//   Type: Stack
//   Operations: push(item), pop() → item, isEmpty() → bool
// (Implementation: could use array, linked list, or vector — user doesn't care!)
```
> [!success]- Show Answer
> The ADT is the promise (interface). The implementation is the secret (how it actually works). Exams will ask you to write an ADT interface — only declare the operations, don't implement them.

### Trap 9: Induction vs Deduction — Which Direction Is Which?
- **Induction:** Concrete → Abstract. Example: seeing a luxury bus, a school bus, a city bus → forming the concept "Bus."
- **Deduction:** Abstract → Concrete. Example: given the concept "Bus," you deduce whether a particular vehicle is a bus.
> [!success]- Show Answer
> Induction goes UP (specifics to general idea). Deduction goes DOWN (general idea to specific case). Memory aid: **In**duction gathers **in**dividual examples to **in**fer a rule. **De**duction **de**termines if something fits a rule you already know.

### Trap 10: Top-Down vs Bottom-Up — Knowing When to Use Each
- **Top-Down:** Requirements are **CLEAR and STABLE** at the start. You can plan the entire architecture from the top.
- **Bottom-Up:** Requirements are **EVOLVING / ACCUMULATING**. New features keep appearing. You build small, reusable pieces and compose them.

> [!success]- Show Answer
> Top-Down = fixed requirements, clear picture. Bottom-Up = changing requirements, uncertain future. In practice, most real projects are bottom-up (or hybrid) because requirements ALWAYS change. The lecture explicitly says OOP follows the bottom-up strategy.

### Trap 11: Polymorphism vs Overloading
- **Polymorphism** is the broad concept: objects responding differently to the same message.
- **Overloading** (function and operator) is one specific **implementation technique** to achieve polymorphism in C++.
> [!success]- Show Answer
> Polymorphism is the "what" (many forms). Overloading is the "how" (same name, different parameter types). Overloading is a subset of polymorphism. Don't use the terms interchangeably — polymorphism also includes virtual functions, templates, and subtype polymorphism.

### Trap 12: OOP Is Not Just "Code in Classes"
Writing a bunch of classes that are just namespaces full of static utility functions is **NOT** OOP. True OOP requires:
- Objects that hold **state** (data members)
- Objects that exhibit **behaviour** (methods operating on that state)
- Objects that **interact** by sending messages to each other

> [!success]- Show Answer
> If your class has no data members and only static methods, you are doing procedural programming dressed in class syntax. OOP demands the union of state + behaviour + encapsulation + interaction. An anemic class that just holds data (getters/setters only) is also not really OOP — it's a data structure.

### Trap 13: Structured Programming Modules vs OOP Classes
In structured programming, each module has its own data and functions — this sounds like a class, but there is a critical difference: the data in structured programming is still **globally accessible** to any other module that calls the function. There is no true encapsulation barrier.

> [!success]- Show Answer
> Structured modules may LOOK encapsulated, but any module can call any other module's function and thereby touch its data. Only OOP classes enforce access control (`private`) that the compiler physically enforces. The structured programming diagram in the lecture shows GLOBAL DATA at the center, exposed to all functions — that's the fatal flaw.

## 8. HAND-CODING DRILLS
### Drill 1: Identify the Four Pillars from a Scenario
**Scenario:** A banking application has `Account` (stores balance privately, provides `deposit()` and `withdraw()` with validation). `SavingsAccount` inherits from `Account` (overrides `withdraw()` to prevent overdraft, add `addInterest()`). Multiple `Account` types exist — `deposit()` works differently for checking vs savings. The customer never sees the database queries used to save account data to disk.

Identify all four pillars in this scenario.

> [!success]- Show Answer
> - **Abstraction:** The customer sees `deposit()` and `withdraw()` — they never see the database queries that persist data to disk. The internal storage mechanism is hidden.
> - **Encapsulation:** The balance is `private` inside `Account`. Only `deposit()` and `withdraw()` can modify it. Data and methods are bundled together.
> - **Inheritance:** `SavingsAccount` inherits from `Account` — it gets all of Account's data and methods, then overrides `withdraw()` and adds `addInterest()`.
> - **Polymorphism:** `deposit()` behaves differently for checking vs savings accounts. The same method name produces different results depending on the account type.

### Drill 2: Spot Broken OOP (Private Member Access Violation)
Which of the following code fragments contain a private member access violation?

```cpp
class Player {
private:
    int hp;
public:
    int getHP() { return hp; }
    void attack(Player& other) {
        other.hp -= 10;    // (A)
    }
};

void gameLoop() {
    Player p1, p2;
    p1.hp = 100;          // (B)
    int x = p2.getHP();   // (C)
    int y = p1.hp;        // (D)
}
```

> [!success]- Show Answer
> (B) and (D) are violations. `hp` is private, and `gameLoop()` is not a member function of `Player`.
> (A) is LEGAL — `attack()` is a member of `Player`, and two objects of the same class CAN access each other's private members.
> (C) is LEGAL — `getHP()` is a public accessor.

### Drill 3: Bottom-Up vs Top-Down Design Choice with Justification
**Scenario A:** You are hired to build a payroll system for a company with well-documented, unchanging payroll rules that have been the same for 15 years. All requirements are fully specified in a 200-page document.

**Scenario B:** You are building a startup's MVP (minimum viable product). The founder says "We need user accounts and payment processing now, but we'll figure out the rest as we go."

Which approach (Top-Down or Bottom-Up) for each scenario? Justify.

> [!success]- Show Answer
> **Scenario A → Top-Down.** Requirements are clear, stable, and fully documented. You can design the entire system architecture (Main → Payroll Engine → Tax Calculator, Salary Calculator, etc.) from the top down without fear of major changes.
> **Scenario B → Bottom-Up.** Requirements are vague and guaranteed to change. Build small, independent modules (User module, Payment module) as reusable building blocks. When the founder changes direction next week, you rearrange blocks instead of tearing down a monolith.

### Drill 4: ADT Design — Write Interface for Complex Number
Write ONLY the interface (no implementation) for a `Complex` ADT. Include:
- A type for complex numbers
- Operations: create (with real and imaginary parts), add, subtract, get real part, get imaginary part
- Precondition: the imaginary unit `i` satisfies `i² = -1`

> [!success]- Show Answer
> ```cpp
> // ADT Complex: represents a complex number a + bi where i² = -1
> // Exports type: Complex
> // Exports operations:
> class Complex {
> private:
>     double real;
>     double imag;
> public:
>     Complex(double r, double im);           // create: r + im*i
>     Complex add(Complex other);             // returns this + other
>     Complex subtract(Complex other);        // returns this - other
>     double getReal();                       // returns real part
>     double getImag();                       // returns imaginary part
> };
> // Axioms:
> //   add is commutative: a.add(b) == b.add(a)
> //   add is associative: (a.add(b)).add(c) == a.add(b.add(c))
> ```

### Drill 5: Class vs Object — Identify Which Is Which
**Scenario:** A university registration system has: `Course`, `Student`, the specific course "Programming 2" that meets Tuesdays at 8 AM, the student "Nguyen Van A" with ID 20240001, `Professor`, and Professor "Dr. Tran" who teaches three courses.

Identify each item as a CLASS or an OBJECT.

> [!success]- Show Answer
> | Item | Class or Object? |
> |---|---|
> | `Course` | Class (blueprint for all courses) |
> | `Student` | Class (blueprint for all students) |
> | "Programming 2" (Tues 8 AM) | Object (one specific course instance) |
> | "Nguyen Van A" (ID 20240001) | Object (one specific student instance) |
> | `Professor` | Class (blueprint for all professors) |
> | "Dr. Tran" (teaches 3 courses) | Object (one specific professor instance) |
> 
> Rule: If it describes a category of things with common structure, it's a class. If it's one specific thing with actual values, it's an object.

### Drill 6: Relationship Identification — IS-A, HAS-A, USES
Identify the relationship for each pair:
1. A car and its steering wheel
2. A checking account and a bank account
3. A print function and a document object
4. A house and its rooms
5. A student and a library card

> [!success]- Show Answer
> | Pair | Relationship | Type |
> |---|---|---|
> | Car ↔ Steering Wheel | A steering wheel IS PART OF a car | HAS-A (Composition) |
> | Checking Account ↔ Bank Account | A checking account IS-A bank account | IS-A (Inheritance) |
> | Print function ↔ Document | A print function USES a document | USES (Dependency) |
> | House ↔ Rooms | A room IS PART OF a house | HAS-A (Composition) |
> | Student ↔ Library Card | A student HAS-A library card | HAS-A (Aggregation — card can exist independently) |
> 
> Key distinction: Composition (HAS-A where part cannot exist independently — rooms don't survive demolition) vs Aggregation (HAS-A where part can exist independently — a library card exists even if the student graduates).

### Drill 7: Design from Scratch — Library System
**Scenario:** Design a library management system. The library has books (each with title, author, ISBN, and availability status). Members can borrow and return books. Some members are students (with student ID and course) and some are faculty (with department and employee ID). A librarian manages the catalog. The library charges fines for late returns.

Identify ALL candidate classes and their relationships. Specify IS-A, HAS-A, and USES relationships. For each class, list 2-3 key data members and 2-3 key methods.

> [!success]- Show Answer
> **Candidate Classes and Relationships:**
> 
> | Class | Key Data | Key Methods | Relationships |
> |---|---|---|---|
> | `Book` | title, author, ISBN, isAvailable | `checkOut()`, `returnBook()`, `isOverdue()` | USES `Date` for due dates |
> | `Member` (abstract) | name, memberID, borrowedBooks[] | `borrow(Book)`, `returnBook(Book)` | HAS-A list of `Book` |
> | `Student` | studentID, course | (inherits from Member) | IS-A `Member` |
> | `Faculty` | department, employeeID | (inherits from Member) | IS-A `Member` |
> | `Librarian` | staffID, shift | `addBook(Book)`, `removeBook(ISBN)`, `collectFine(Member, amount)` | USES `Book`, USES `Member` |
> | `Catalog` | books[] | `searchByTitle(string)`, `searchByAuthor(string)` | HAS-A collection of `Book` |
> | `Loan` | book, member, dueDate, returnDate | `calculateFine()`, `isLate()` | USES `Book`, USES `Member`, USES `Date` |
> | `Fine` | member, amount, reason, isPaid | `pay()`, `waive()` | USES `Member` |
> 
> **Inheritance hierarchy:** `Member` (superclass) → `Student` and `Faculty` (subclasses). This IS-A relationship means students and faculty share all membership features but add their own specialisations.
> 
> **Composition:** `Catalog` HAS-A collection of `Book`. The books exist inside the catalog.
> 
> **Dependencies:** `Loan` USES `Book` and `Member` — they are passed in but not owned by Loan.
> 
> **Key operations flow:** `Student.borrow(book)` → checks availability → creates `Loan` → updates `book.isAvailable` → if overdue, creates `Fine`. Each step is an object sending a message to another object.
