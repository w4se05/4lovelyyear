# Lec7: Inheritance (Conceptual) — Study Guide

---

## 1. CONCEPT CARD

### 1.1 What It Is

Inheritance is a mechanism where a new class (subclass / derived class) automatically acquires all the data and behavior of an existing class (superclass / base class), and can then add or modify what it needs. It is a natural property of classification — the idea that one category of things is a refinement of a broader category.

In OOP: if "A inherits from B", objects of class A have access to attributes and methods of class B without redefining them.

### 1.2 What Problem It Solves

- **Code duplication.** Without inheritance, if `Student` and `Professor` share 80% of their code (name, ID, address, email), you duplicate that code in both classes. When a bug is found in the shared logic, you must fix it in every location. Forgetting one fix causes divergence.
- **Reuse of existing design** reduces software development and testing costs.
- **Modular design.** A new class inherits data and functionalities of an existing class, promoting a structured, layered class hierarchy.
- **Polymorphism enablement.** A base class can define a common interface; derived classes can be treated uniformly through base-class pointers or references.

### 1.3 How It Works

1. Identify the common data and behavior among related concepts and place them in a **base class** (superclass).
2. Create **derived classes** (subclasses) that inherit from the base.
3. The derived class automatically has all public and protected members of the base.
4. The derived class can add **new** members that only it needs.
5. The derived class can **override** base class methods to customize behavior.
6. A derived object **can** be used anywhere a base object is expected — a `Student` IS a `Person`. This is the "is-a" relationship.
7. Inheritance works along three dimensions: static vs dynamic sharing, implicit vs explicit sharing, per-object vs per-group sharing.

### 1.4 Concrete Example

A university personnel system. `Person` is the base class with `name`, `id`, `address`, and `getContactInfo()`. `Administrator` inherits from `Person` and adds `department`, `clearanceLevel`. `Faculty` inherits from `Person` and adds `coursesTaught`, `officeHours`. `Student` inherits from `Person` and adds `major`, `gpa`, `coursesEnrolled`.

The registration system stores a list of `Person*` pointers. It calls `getContactInfo()` on each without knowing the specific type — inheritance guarantees the function exists. Each derived class can override `getContactInfo()` to return role-specific information.

### 1.5 What It Is NOT

- **NOT "code copying."** The subclass does not receive a duplicate paste of the base class. It genuinely **shares** the base class definition. Changes to the base propagate to all subclasses.
- **NOT composition ("has-a").** Inheritance models "is-a" (`Car` IS A `Vehicle`). Composition models "has-a" (`Car` HAS A `Engine`). Do not inherit when composition makes more sense.
- **NOT always a code-reuse tool.** In the case of abstract classes, inheritance is about defining a common design interface — sometimes with no executable code at all. It is a specification-sharing mechanism, not just an implementation-sharing mechanism.

---

## 2. ADDITIONS TO LAST LECTURE (Lec6 review from Lec7)

### 2.1 Constructor Auto-Generation

- If you define **no** constructor at all, the compiler **generates** a default constructor that default-initializes members. Same goes for the destructor: if you write none, the compiler generates one that does nothing.
- If you define **any** constructor (even a parameterized one), the compiler does **not** generate a default constructor. Calling `ClassName obj;` without a manually written default constructor becomes a compile error.
- Same principle applies to the **copy constructor**: if you do not write one, the compiler generates a memberwise (shallow) copy constructor.

### 2.2 Access Modifiers — Class Level vs Object Level

Access modifiers (`private`, `protected`, `public`) operate on **class** level, NOT **object** level.

This means: two objects of the **same** class can access each other's `private` and `protected` members. The compiler checks access against the **class scope**, not the particular instance.

**Date example with full explanation:**

```cpp
class Date {
private:
    int month, day, year;
public:
    Date(int mo, int dy, int yr) {
        month = mo;
        day = dy;
        year = yr;
    }

    Date(Date & d) {
        month = d.month;   // ← Why is this OK? month is PRIVATE in Date!
        day = d.day;       // ← Same — accessing d's private members
        year = d.year;     // ← Same
    }
};
```

**Explanation:** The `private` modifier enforces the **Encapsulation** principle. The "outer world" should not manipulate a `Date` object's internal state directly, because `Date`'s internal implementation may change over time (e.g., you might switch from three `int` fields to a single `long` timestamp).

When an instance of `Date` accesses internals of **another** `Date` instance — both instances always "know" the details of `Date`'s implementation. Both are compiled against the same `Date` class definition. If the internal logic of `Date` changes, only the single `Date` class code needs to change — and everything inside it is updated together.

This per-class access is what makes **copy constructors**, **assignment operators**, `operator==`, and other member functions that accept objects of the same type possible to write without getters and setters for every private field.

**Key exam fact:** If you see `obj.privateField` inside a member function of the same class — it is LEGAL. If you see it outside (in `main()`, in a non-friend function, in a different class that is not a friend) — it is a COMPILE ERROR.

---

## 3. CLASSIFICATION AND SHARING

### 3.1 Classification

Classification arises from the universal human need to describe **uniformities** among collections of instances. We group similar things into categories, then sub-categories, forming hierarchies. Classification is the foundational idea for understanding inheritance.

**Diagram — Classification vs Inheritance hierarchy:**

```
            Animal
          /        \
     Mammal         Bird
    /      \          \
People     Dog      Sparrow
 /    \      |
man  woman  Rex
 |      |
John   Mary
```

- **Classification:** Animal → Mammal → People → man → John. Each arrow means "is a kind of." John is a specific instance (object) at the leaf of the classification tree.
- **Inheritance:** Animal is the base class. Mammal and Bird inherit from Animal. People and Dog inherit from Mammal. man and woman inherit from People. John and Mary are **objects** (instances), not classes — they are at the bottom of the tree where classification ends and instantiation begins.

The distinction: classification goes all the way to individual instances. Inheritance (in OOP) stops at the class level — classes inherit from classes; instances are created from classes.

### 3.2 Three Aspects of Classification / Inheritance

Inheritance serves three distinct purposes in object-oriented design:

1. **Commonality:** The base class captures **common information** (attributes) and **common features** (operations) shared by all derived classes. Example: `Person` captures `name` and `getContactInfo()` which every `Student`, `Faculty`, and `Administrator` shares.

2. **Customization:** An existing class is used to create a **customized version** — a specialized variant that adds or modifies behavior. Example: `SalariedEmployee` customizes `Employee::calculatePay()` to divide annual salary by 12 instead of computing hourly wages.

3. **Common Design Interface:** A base class may define **design requirements** for derived classes by specifying member functions that **MUST** be provided by every derived class. The base class declares the "what"; derived classes provide the "how." This is the essence of abstract classes and, in C++, pure virtual functions.

### 3.3 Sharing

Sharing is ubiquitous in the real world, and therefore critically important in object-orientation:
- Look around: people share transportation (buses), housing (apartment blocks), knowledge (books), infrastructure (roads).
- In OOP, **inheritance is a technique that promotes sharing**.

**What sharing means in inheritance:**
- Inheritance means **new classes can be derived from existing classes**.
- A **subclass inherits** attributes and operations of a superclass; it can also define additional ones.
- Inheritance can be seen as a **specialization** mechanism: subclass instances are specializations of superclass instances (a `Square` is a specialized `Rectangle`).
- Inheritance can be seen as a **generalization** mechanism: a superclass generalizes subclass instances (a `Vehicle` is a generalization of `Car`, `Truck`, `Motorcycle`).
- **The ability of one class to share the behavior of another class without explicit redefinition.**
- **An approach which allows classes to be created based on an old class.**

### 3.4 Three Dimensions of Sharing

Sharing through inheritance can be classified along three independent dimensions:

| Dimension | Options | Meaning |
|-----------|---------|---------|
| **Static vs Dynamic** | Static: fixed at object creation. Dynamic: determined when object receives a message. | In static sharing, the behavior an object inherits is fixed when the object is instantiated. In dynamic sharing (delegation-based), behavior can change at runtime. |
| **Implicit vs Explicit** | Implicit: system does it automatically. Explicit: programmer directs patterns. | In implicit sharing, the language/runtime handles sharing (e.g., C++ inheritance by default). In explicit sharing (delegation), the programmer manually forwards calls. |
| **Per Object vs Per Group** | Per object: behaviors attached to a single object. Per group: behaviors specified for entire class. | Most OOP languages use per-group (class-level) inheritance. Prototype-based languages use per-object sharing. |

**Important:** C++ inheritance is predominantly **static, implicit, and per-group**. A derived class's inheritance structure is fixed at compile time, the compiler automatically resolves inherited members, and behavior is defined for the entire class — not individual objects.

### 3.5 Purposes of Inheritance

1. **Reusing existing design** reduces software development and testing costs. Instead of building a payroll module from scratch for hourly, salaried, and contract employees, you build one `Employee` base and derive the variants.

2. **Modular Design:** A new class inherits data and functionalities of an existing class, promoting:
   - Cleaner separation of concerns
   - Smaller, more testable units
   - Easier maintenance — fix the base, all derived classes benefit

---

## 4. WHAT IS INHERITANCE?

### 4.1 Definitions

Inheritance has several equivalent definitions that emphasize different facets:

1. **Inheritance is a mechanism for expressing similarity.** When two classes share structure or behavior, inheritance explicitly declares that relationship in code rather than duplicating it.

2. **Inheritance is a natural property of classification.** Classification naturally implies inheritance — if `Dog` is classified under `Mammal`, then every `Dog` inherently possesses the properties of `Mammal` (warm-blooded, fur, live birth).

3. **Inheritance is a mechanism that allows (a class) A to inherit properties of (a class) B.** This is the direct, operational definition: whatever B has, A gets (subject to access rules).

### 4.2 In OOP

If "A inherits from B" (equivalently: A is derived from B):
- Objects of class A have access to **all public and protected** attributes and methods of class B **without redefining them**.
- Class A can add its **own** attributes and methods.
- Class A can **override** methods of B to provide its own implementation.
- An object of class A **is** an object of class B — substitutability at the type level.

---

## 5. SUPERCLASS AND SUBCLASS

### 5.1 Definitions

- If class **A** inherits from class **B**, then:
  - **B** is called the **superclass** (base class / parent class) of A.
  - **A** is called the **subclass** (derived class / child class) of B.
- Objects of a subclass can be used **wherever** objects of the corresponding superclass are expected — this is called the **substitutability principle**: a subclass object has the same signature behavior as a superclass object (and may have more).

### 5.2 Example Diagram from Lecture

```
                Person
              /   |    \
    Administrator Faculty Student
```

- `Person` is the **superclass**: captures `name`, `id`, `address`, `getInfo()`.
- `Administrator`, `Faculty`, `Student` are **subclasses**: each inherits everything from `Person` and adds its own specialized data and behavior.
- A function that expects a `Person*` parameter can accept a `Student*`, `Faculty*`, or `Administrator*` — the program does not need to know the specific derived type.

### 5.3 Subclasses as Reusability Mechanism

Subclasses refer to **two kinds** of reuse:

1. **Inheritance of specification:** The subclass inherits the **interface** — the set of public/protected method signatures that the superclass declares. This is what enables polymorphism.

2. **Inheritance of implementation:** The subclass inherits the **actual code** (method bodies) from the superclass. The subclass does not need to re-implement inherited behavior unless it wants to customize it.

The combination of both makes subclasses a powerful reusability mechanism: you get the design contract AND the working code without duplication.

---

## 6. IMPORTANT ASPECTS OF SUBCLASSES

### 6.1 Modifiability

The **degree of modifiability** determines how attributes and methods inherited from a superclass can be modified in the subclass. There are two categories of modification:

1. **Modifying object states** (attributes / data members)
2. **Modifying object behaviors** (operations / member functions)

Each category has its own levels of permitted modification.

### 6.2 Attributes — Four Modification Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | **No redefinition** | Modification is **not allowed** at all. The inherited attribute is sealed — the subclass cannot change its type, visibility, initial value, or domain. |
| 2 | **Arbitrary redefinition** | Redefinition is allowed **without constraint**. The subclass can change the attribute's type, access level, initial value — anything. |
| 3 | **Constrained redefinition** | The **domain** of the attribute is constrained. The subclass can redefine the attribute but must stay within bounds. Example: a `numWheels` attribute in `Vehicle` with domain [0..∞); `Bicycle` constrains it to [2..2]. |
| 4 | **Hidden redefinition** | The definitions of attributes are **hidden** in the subclass to avoid naming conflicts. The subclass can define its own attribute with the same name, and the inherited version is shadowed. The subclass's version is the one visible. |

**Exam note:** In standard C++, attributes in a derived class **hide** (shadow) attributes of the same name in the base class — this corresponds to level 4 (Hidden redefinition). Level 1 (no redefinition) is effectively what `final` does in other languages.

### 6.3 Operations — Two Modification Types

1. **Arbitrary redefinition:** All changes to operations are allowed — the subclass can completely rewrite the body, change parameter types, change return type — no restrictions. This is the most permissive model.

2. **Constrained redefinition:** Parts of the method signature in the subclass must be **subtypes** of the corresponding parts in the superclass method. Specifically:
   - **Return type** must be covariant (same type or a subtype).
   - **Parameter types** must be contravariant (same type or a supertype).
   - This constraint ensures **type safety** — a subclass object used through a superclass reference must still behave as expected.

**This is critically important for overriding and overloading of methods.** When you override, you cannot arbitrarily change every part of the signature. In C++ specifically:
- Overriding requires matching function signature (name + parameter types + constness).
- Return type can be covariant (pointer/reference to derived type).
- Violating constrained redefinition causes the method to be a **new overload** rather than an override, which changes polymorphic behavior.

### 6.4 Naming Conflicts

A **naming conflict** occurs when attributes or methods defined in a subclass have **the same names** as those in the superclass.

- **Between superclass and subclass:** If a subclass defines a member with the same name as a member in the superclass, the subclass version wins. The inherited version is **hidden** (shadowed), not deleted.
- **Resolution:** Naming conflicts are resolved by **OVERRIDING**. The subclass's version overrides the superclass's version.
- To access the hidden superclass version, use the **scope resolution operator**: `SuperclassName::memberName`.

**Example:**
```cpp
class Base {
public:
    void display() { cout << "Base display"; }
};

class Derived : public Base {
public:
    void display() { cout << "Derived display"; }  // overrides Base::display
    void test() {
        display();          // calls Derived::display
        Base::display();    // calls Base::display (explicit scope)
    }
};
```

---

## 7. CATEGORIES OF INHERITANCE

### 7.1 Whole / Partial Inheritance

| Category | Definition |
|----------|------------|
| **Whole Inheritance** | A class inherits **ALL** properties and operations from its superclass. Nothing is suppressed. |
| **Partial Inheritance** | Only **SOME** properties are inherited; others are **suppressed** (excluded). The subclass picks and chooses what to inherit. |

**In C++:** Inheritance is **whole** — a derived class inherits everything (subject to access rules: private members are inherited but not directly accessible). Partial inheritance is a **theoretical concept** — not standard C++.

### 7.2 Default / Strict Inheritance

| Category | Definition |
|----------|------------|
| **Default Inheritance** | Inherited properties and constraints **can be modified** by the subclass. This is the normal case in C++ — derived classes can override methods, change access levels, etc. |
| **Strict Inheritance** | Inheritance **does not allow** the user to modify inherited properties or constraints. The inherited members are frozen — cannot be overridden or redefined. |

**In C++:** By default, C++ uses default inheritance (overridable). C++11 introduced the `final` keyword to opt into strict inheritance: `class Derived final : public Base { };` prevents further derivation; `void foo() final { }` prevents overriding of that specific method.

### 7.3 Single (Simple) Inheritance

A class can inherit from **ONE** superclass only. The inheritance hierarchy forms a **tree** — each node has at most one parent.

```
         A
       / | \
      B  C  D
     / \    |
    E   F   G
```

- Each class has exactly one direct superclass (except the root).
- Clean, simple, no ambiguity issues.
- Supported by all OOP languages.
- By default, C++ uses single inheritance.

### 7.4 Multiple Inheritance

A class can have **MORE THAN ONE** superclass. The inheritance hierarchy forms a **directed acyclic graph** (DAG) instead of a tree.

```
      B1      B2      B3
      |       |       |
      +---+---+---+---+
              |
              A
```

**Diagram from lecture:** `B1`, `B2`, `B3` all have `int x` and `getValue()`. Class `A` inherits from all three.

**The key problem — Naming Conflicts:** If attributes or methods defined in **one** superclass have the same name as those in **another** superclass, which one does the derived class inherit?

Example:
```cpp
class B1 { public: int x; int getValue(); };
class B2 { public: int x; int getValue(); };
class B3 { public: int x; int getValue(); };
class A : public B1, public B2, public B3 { };
```

When `A` references `x` or calls `getValue()`, the compiler faces **ambiguity** — three superclasses each contribute a candidate. Resolution methods are covered in Section 8.

**Advantages:** Powerful modeling — a `TeachingAssistant` IS A `Student` AND IS AN `Employee`.
**Disadvantages:** Ambiguity, diamond problem, increased complexity.

---

## 8. CONFLICT RESOLUTION IN MULTIPLE INHERITANCE

When multiple superclasses define members with the same name, the derived class must resolve the conflict.

### 8.1 Method 1: Using Order of Superclass

If multiple attributes or methods with the same name appear in different superclasses, the ones in the **FIRST** class in the list of superclasses are the ones inherited.

**Done BY THE COMPILER** — automatically, no programmer intervention needed.

**Example:** If the inheritance order is `class A : public B1, public B2, public B3`:
- `x` → means `x` of `B1` (first in the list)
- `getValue()` → means `getValue()` of `B1` (first in the list)
- This is a **left-to-right priority** rule.

**Pros:** No programmer effort needed, compiler handles it.
**Cons:** Subtle — changing the order of base classes changes behavior. The programmer must remember the order. Not all C++ compilers implement this (C++ standard does not define this as the default resolution — in standard C++, the ambiguity persists until explicitly resolved).

### 8.2 Method 2: Determined by User

The user can inherit conflicting attributes or methods but must **EXPLICITLY RENAME** them in the subclass using the scope resolution operator.

**Done BY THE USER** — programmer explicitly chooses which base's version to use.

**Syntax:**
```cpp
class A : public B1, public B2, public B3 {
public:
    // Explicitly select which version to inherit:
    using B1::x;             // x comes from B1
    using B2::getValue();    // getValue() comes from B2, etc.
};

// OR, in code:
void someFunction() {
    B1::x = 10;              // B1's x
    B2::x = 20;              // B2's x
    int v = B3::getValue();  // B3's getValue()
}
```

**In C++:** Standard C++ uses method 2 — the user resolves ambiguity with scope resolution (`BaseClass::member`). Simply accessing `x` or `getValue()` without qualification is a **compile error** (ambiguous reference). Method 1 (compiler picks first in list) is NOT how standard C++ resolves multiple inheritance conflicts.

---

## 9. ABSTRACT CLASS

### 9.1 Definition

An **abstract class** is a class **WITHOUT ANY INSTANCE**. You cannot create objects of an abstract class. It exists purely for classification and as a base for inheritance.

**Example:** `Mammal` is an abstract class. You never create a generic "mammal" object — you create a `Dog`, a `Cat`, a `Human`. Mammal exists only to capture the shared characteristics (warm-blooded, fur/hair, live birth, mammary glands) and serve as a superclass for concrete species.

It is also possible to have a classification **without any (executable) code behind it** — the abstract class may define only the interface (pure declarations) with zero implementation.

### 9.2 Formal Definition

Class A is called an **abstract class** if:
1. It is **used ONLY as a superclass** for other classes.
2. Class A only **specifies PROPERTIES** — it is never used to create objects directly.
3. **Derived classes MUST define** the properties (implement the interface) of A.

In C++, an abstract class is implemented with **pure virtual functions**: `virtual void func() = 0;`. This forces every concrete derived class to provide its own implementation. Attempting to instantiate an abstract class is a compile error.

### 9.3 Reuse

Many take inheritance as a **code reusing tool** — inheriting existing implementations to avoid rewriting.

In the context of abstract classes, inheritance serves as a **code reusing tool** in a different sense:
- The abstract class provides a **design contract** — a reusable architecture.
- Derived classes provide **implementations** that fit the contract.
- Code at the abstract class level (e.g., algorithms that call virtual functions) is reused across all derived classes without modification.

Example: An abstract `Shape` class defines a pure virtual `draw()`. A rendering engine iterates over `Shape*` pointers and calls `draw()` on each. The rendering engine code is written once and reused for every shape type — `Circle`, `Rectangle`, `Triangle` — without changes.

---

## 10. INHERITANCE vs CLASSIFICATION

These two concepts are closely related but not identical:

| Aspect | Classification | Inheritance |
|--------|---------------|-------------|
| **Direction** | Top-down grouping into categories | Bottom-up: derived classes inherit from base |
| **Scope** | Goes all the way to individual instances (John IS A man) | Stops at the class level (class hierarchy) |
| **Relationship** | "is a kind of" | "derives from / inherits from" |
| **Entity level** | Can describe relationships between classes AND instances | Describes relationships between classes only |

**Key insight from the lecture:**
- **Classification implies inheritance** — specifically **whole** and **simple** (single) inheritance. When you classify organisms, species inherit all properties of their genus (whole), and each species has exactly one genus (simple).
- **Inheritance may affect the clarity of classification** — specifically when **multiple inheritance** and **partial inheritance** are used. A class that inherits from three unrelated bases blurs the clean classification hierarchy. Partial inheritance (selectively suppressing members) breaks the assumption that a subclass has everything its superclass has.

---

## 11. DECLARING DERIVED CLASSES (Syntax Preview)

```cpp
class derived_class_name : access_specifier base_class_name {
    // additional members...
};
```

**Components:**
- `derived_class_name`: the name of the new (sub)class
- `access_specifier`: `public`, `protected`, or `private` — determines how base class members are exposed in the derived class (full details in Lec8)
- `base_class_name`: the existing class being inherited from

**Examples:**
```cpp
class Student : public Person { /* ... */ };          // public inheritance
class Faculty : protected Person { /* ... */ };        // protected inheritance
class Administrator : private Person { /* ... */ };    // private inheritance
```

**Note:** This is a syntax preview. The semantic differences between `public`, `protected`, and `private` inheritance are covered in detail in Lec8 (Inheritance in C++).

---

## 12. MUST-MEMORIZE SYNTAX TEMPLATES

### Template 1: Base Class Declaration
```cpp
class BaseClassName {
protected:                          // accessible by derived classes, NOT outsiders
    int sharedData;
public:
    BaseClassName();                // default constructor
    BaseClassName(int d);           // parameterized constructor
    void commonMethod();            // inherited as-is by derived
    virtual void customizable();    // designed to be overridden
};
```

### Template 2: Derived Class Declaration (Single Inheritance)
```cpp
class DerivedClassName : public BaseClassName {
private:
    int extraData;                  // additional state
public:
    DerivedClassName();             // default constructor
    DerivedClassName(int baseData, int extraData);  // must init base
    void customizable() override;   // OVERRIDES base version
    void extraMethod();             // new behavior not in base
};
```

### Template 3: Multiple Inheritance Declaration
```cpp
class Derived : public Base1, public Base2, public Base3 {
public:
    // Resolve naming conflicts explicitly:
    void setup() {
        Base1::x = 5;               // disambiguate: use Base1's x
        Base2::x = 10;              // disambiguate: use Base2's x
        Base1::getValue();          // disambiguate: call Base1's version
    }
};
```

### Template 4: Abstract Class (Conceptual)
```cpp
class AbstractBase {
public:
    virtual void mustImplement() = 0;   // pure virtual → makes class abstract
    virtual ~AbstractBase() { }         // virtual destructor for safe deletion
    // AbstractBase obj;                // ERROR — cannot instantiate
};
```

### Template 5: Conflict Resolution by User (Multiple Inheritance)
```cpp
class A : public B1, public B2, public B3 {
public:
    void resolve() {
        B1::x = value;            // explicitly use B1's version
        int v = B2::getValue();   // explicitly use B2's version
    }
};
```

---

## 13. EXAM TRAPS

### Trap 1 — Access Is Per-Class, Not Per-Object (Lec6 Review)
Two objects of the same class can access each other's `private` members. This is why `Date(Date& d) { month = d.month; }` compiles. Access control is checked at the class boundary, not the instance boundary.

### Trap 2 — Derived Class Does NOT Inherit Constructors, Destructors, Copy Constructor, or Assignment Operator
These special member functions must be defined (or compiler-generated) for the derived class itself. The derived constructor must **call** the base constructor (explicitly or implicitly). A derived class does NOT automatically get a copy of the base constructor.

### Trap 3 — Private Base Members Are Inaccessible in Derived Class
`private` members of the base class are inherited (they exist in the derived object's memory) but are **not directly accessible** in the derived class. Use `protected` if derived classes need access. Accessing via getters/setters from the base class is the only way to reach private members.

### Trap 4 — Naming Conflicts Resolved by Overriding, Not Overloading
If both base and derived define `void display()`, the derived version **hides** (shadows) the base version. The base version does not participate in overload resolution in the derived class. Access the hidden base version with `BaseClassName::display()`. Both versions exist — the derived's version simply wins by name lookup rules.

### Trap 5 — "Is-a" vs "Has-a"
- Inheritance models **"is-a"**: a `Car` IS A `Vehicle`.
- Composition models **"has-a"**: a `Car` HAS A `Wheel`. (Member objects)
Do not use inheritance when composition is the correct relationship. This is a common design mistake that leads to fragile hierarchies.

### Trap 6 — Abstract Class Cannot Be Instantiated
An abstract class exists only as a base. You CAN write `AbstractBase* ptr;` (a pointer is fine) but NOT `AbstractBase obj;` (an object is a compile error). Abstract classes are for classification and interface definition, not object creation.

### Trap 7 — Abstract Class ≠ Class with Protected Constructor
An abstract class is a design concept — "a class without instances, used only as a base." The lecture covers this **conceptually**. In C++, abstractness is implemented with pure virtual functions (`= 0`), not with access control tricks. A class with a `protected` constructor may prevent direct instantiation, but that is a different mechanism — do not confuse the two.

### Trap 8 — Multiple Inheritance Naming Conflicts
When two (or more) base classes each have a member with the same name (`int x`), the derived class must resolve the ambiguity. The compiler does NOT automatically pick one. Use scope resolution: `Base1::x` to specify which one. Unqualified access is a compile error.

### Trap 9 — Default vs Strict Inheritance Is a Conceptual Distinction
In C++, default inheritance (overridable) is the norm. Strict inheritance (frozen/unchangeable) is achieved with `final` in C++11 and later. The lecture covers both as conceptual categories — do not assume strict inheritance is a built-in feature of every language.

### Trap 10 — Whole vs Partial Inheritance
C++ uses **whole** inheritance — a derived class inherits everything from the base (subject to access rules). Partial inheritance (selectively suppressing individual members) is a theoretical concept discussed for completeness. On exams, if asked "does C++ support partial inheritance?", the answer is no.

### Trap 11 — Overriding Is Not the Same as Replacement
When a derived class overrides a base method, the base method **still exists**. It is hidden from the derived class's name scope but accessible via `Base::method()`. Both implementations coexist in the vtable / class layout.

### Trap 12 — Conflict Resolution by Compiler Order vs User
Method 1 (compiler resolves by order) is a conceptual approach discussed in the lecture but is NOT how standard C++ handles multiple inheritance conflicts. In standard C++, the user MUST explicitly resolve with scope resolution (Method 2). Do not confuse the theoretical option with the C++ standard behavior.

### Trap 13 — Substitutability Principle Consequences
A `Derived*` can be assigned to a `Base*` (upcasting — always safe). But the reverse (downcasting from `Base*` to `Derived*`) is NOT automatically safe — the base pointer might actually point to a different derived class. In C++ this requires `dynamic_cast`.

### Trap 14 — Classification Tree ≠ Inheritance Hierarchy
Classification can describe both class-to-class AND class-to-instance relationships. Inheritance only describes class-to-class relationships. Do not write `class John : public Person` on an exam — John is an instance, not a class.

---

## 14. HAND-CODING DRILLS

### Drill 1: Inheritance Hierarchy Identification

**Scenario:** "A ride-sharing app has `Driver` (with `licensePlate`, `rating`) and `Rider` (with `paymentMethod`, `homeAddress`). Both have a `name`, `phoneNumber`, and `profilePhoto`."

Identify the base class and derived classes. What properties go in each?

> [!success]- Show Answer
> **Base class:** `User`
> - `name`, `phoneNumber`, `profilePhoto`
>
> **Derived class:** `Driver`
> - Inherits all of `User`
> - Adds: `licensePlate`, `rating`
>
> **Derived class:** `Rider`
> - Inherits all of `User`
> - Adds: `paymentMethod`, `homeAddress`

---

### Drill 2: Access Modifiers — Class Level vs Object Level

```cpp
class BankAccount {
private:
    double balance;
    int accountNumber;
public:
    BankAccount(double bal, int accNum) {
        balance = bal;
        accountNumber = accNum;
    }
    BankAccount(const BankAccount& other) {
        balance = other.balance;          // Is line (A) legal?
        accountNumber = other.accountNumber; // Is line (B) legal?
    }
    bool isRicherThan(const BankAccount& other) {
        return balance > other.balance;   // Is line (C) legal?
    }
};
```

Explain why lines (A), (B), and (C) compile or do not compile.

> [!success]- Show Answer
> **Line (A):** LEGAL. The copy constructor is a member of `BankAccount`, so it can access `other.balance` even though `balance` is `private`. Access control is per-class — two `BankAccount` objects can see each other's private members.
>
> **Line (B):** LEGAL. Same reasoning as (A). `other.accountNumber` is `private` but accessed from within `BankAccount`'s member function.
>
> **Line (C):** LEGAL. `isRicherThan` is a member of `BankAccount`. It can access `other.balance` — `other` is the same class.
>
> **Key insight:** If `main()` tried `cout << acc1.balance;`, that would be ILLEGAL because `main()` is outside the class. But inside any `BankAccount` member function, accessing another `BankAccount`'s privates is perfectly fine.

---

### Drill 3: Resolving a Naming Conflict (Override + Scope Resolution)

```cpp
class Logger {
public:
    void log(const char* msg) {
        cout << "[LOG] " << msg << endl;
    }
};

class TimestampLogger : public Logger {
public:
    void log(const char* msg) {
        // (a) Print current time, then delegate to base's log
        // (b) Print message TWICE using only base's log
    }
};
```

Implement the `log()` function body to satisfy (a) and (b).

> [!success]- Show Answer
> ```cpp
> void log(const char* msg) {
>     // (a) Custom prepend + delegate to base
>     cout << "[14:30:00] ";
>     Logger::log(msg);
>
>     // (b) Print message twice via base
>     // Logger::log(msg);
>     // Logger::log(msg);
> }
> ```
> Without `Logger::`, `log(msg)` would recursively call the **derived** `TimestampLogger::log()` — infinite recursion and stack overflow. The scope resolution operator is essential to call the **base** version.

---

### Drill 4: Multiple Inheritance Ambiguity

```cpp
class Bluetooth {
public:
    int version;
    void connect() { cout << "BT connect v" << version; }
};

class WiFi {
public:
    float version;
    void connect() { cout << "WiFi connect v" << version; }
};

class SmartSpeaker : public Bluetooth, public WiFi {
public:
    void setup() {
        // (1) Assign 5 to Bluetooth's version
        // (2) Assign 2.4 to WiFi's version
        // (3) Call Bluetooth's connect()
        // (4) Call WiFi's connect()
    }
};
```

Implement `setup()` with proper disambiguation.

> [!success]- Show Answer
> ```cpp
> void setup() {
>     Bluetooth::version = 5;       // (1) explicit scope
>     WiFi::version = 2.4f;         // (2) explicit scope
>     Bluetooth::connect();         // (3) explicit scope
>     WiFi::connect();              // (4) explicit scope
> }
> ```
> Without `Bluetooth::` and `WiFi::`, both `version` and `connect()` are **ambiguous**. The compiler cannot guess which one you mean. This is **conflict resolution by user** (Method 2 from the lecture) — explicit scope resolution.

---

### Drill 5: Multiple Inheritance — Order-Based Resolution

Given three base classes:
```cpp
class B1 {
public:
    int x;
    int getValue() { return x; }
};
class B2 {
public:
    int x;
    int getValue() { return x * 2; }
};
class B3 {
public:
    int x;
    int getValue() { return x * 3; }
};
```

If a language uses **Method 1** (compiler resolves by order, left to right), which `x` and which `getValue()` does `class A : public B3, public B1, public B2` inherit?

> [!success]- Show Answer
> Under Method 1 (order-based resolution, left to right):
> - `x` → `x` of **B3** (first in the inheritance list)
> - `getValue()` → `getValue()` of **B3** (first in the inheritance list)
>
> The order is `B3`, `B1`, `B2` in the declaration `class A : public B3, public B1, public B2`. B3 is first → B3's members win.
>
> **Exam reminder:** Method 1 is theoretical. In standard C++, this would be a compile error — you must use scope resolution (Method 2) to disambiguate.

---

### Drill 6: Modifiability Levels — Identify the Category

Match each scenario to the correct modification level:

| Scenario | Category |
|----------|----------|
| A derived class defines `int speed` even though base already has `int speed` | ? |
| A `Vehicle` base has `int numWheels`; `Motorcycle` constrains it to exactly 2 | ? |
| The base class marks a member as `final` — derived classes cannot touch it | ? |
| A derived class changes the type of `price` from `int` to `double` without any restriction | ? |

> [!success]- Show Answer
> - "A derived class defines `int speed` even though base already has `int speed`" → **Hidden redefinition** (Level 4). The derived class hides the inherited attribute with its own.
> - "`Motorcycle` constrains `numWheels` to exactly 2" → **Constrained redefinition** (Level 3). The domain of the attribute is constrained.
> - "Base marks a member as `final` — cannot touch" → **No redefinition** (Level 1). Modification is not allowed.
> - "Changes `price` from `int` to `double` without restriction" → **Arbitrary redefinition** (Level 2). Any redefinition is allowed without constraint.
>
> **Context:** These four levels describe the spectrum of attribute modifiability in subclassing — from completely sealed (1) to completely open (2), with varying degrees of constraint in between.

---

### Drill 7: Whole vs Partial Inheritance (Conceptual)

A `Vehicle` base class has: `int speed`, `int fuelCapacity`, `float emissions`, `void startEngine()`, `void accelerate()`.

1. If `ElectricCar` uses **whole** inheritance, what does it inherit?
2. If `ElectricCar` uses **partial** inheritance (suppressing `fuelCapacity` and `emissions`), what does it inherit?
3. Which model does C++ use?

> [!success]- Show Answer
> **1. Whole inheritance:** `ElectricCar` inherits ALL five members: `speed`, `fuelCapacity`, `emissions`, `startEngine()`, `accelerate()`. It may then override or add to them, but nothing is suppressed.
>
> **2. Partial inheritance:** `ElectricCar` inherits only: `speed`, `startEngine()`, `accelerate()`. `fuelCapacity` and `emissions` are suppressed (excluded). The subclass only keeps what it needs.
>
> **3. C++ uses whole inheritance.** A derived class inherits everything from the base (subject to access rules). There is no mechanism to selectively suppress individual inherited members.

---

### Drill 8: Abstract Class Identification

Consider these class descriptions. Which are abstract classes?

| Class | Description | Abstract? |
|-------|-------------|-----------|
| `Animal` | Has `eat()`, `sleep()`. No instances — only `Dog`, `Cat`, `Bird` are created. | |
| `Person` | Has `name`, `age`. Instances like `Student s("John", 20)` are created. | |
| `Shape` | Has `draw()`. Only `Circle`, `Square`, `Triangle` are instantiated. | |
| `Printable` | Has `print()` interface. Exists only to declare a contract for other classes. | |

> [!success]- Show Answer
> - `Animal` → **Abstract.** Used only as a superclass. No direct instances. Exists for classification.
> - `Person` → **NOT abstract.** `Student s("John", 20)` creates a direct instance. It is a concrete class.
> - `Shape` → **Abstract.** `draw()` may be pure virtual. Only specific shapes are instantiated.
> - `Printable` → **Abstract.** Exists only as a design contract / interface. No direct instances or executable code — classification without code behind it.
>
> **Key:** An abstract class is defined by its usage — if it's used ONLY as a superclass and never to create objects, it is abstract.

---

### Drill 9: Inheritance vs Classification — Identify the Relationship Type

Given this diagram:
```
        Vehicle
        /     \
      Car    Motorcycle
      /  \
  Sedan SUV
    |
  HondaCivic
```

1. Is `Sedan → HondaCivic` classification, inheritance, or both?
2. Is `Vehicle → Car` classification, inheritance, or both?
3. Is a specific `HondaCivic` with VIN `XYZ123` an example of classification or instantiation?
4. Why does multiple inheritance "affect clarity of classification"?

> [!success]- Show Answer
> 1. `Sedan → HondaCivic` is **both** classification AND inheritance (single, whole). `HondaCivic` IS A `Sedan`. This is clean classification.
> 2. `Vehicle → Car` is **both** classification AND inheritance. `Car` IS A `Vehicle`. Clean single inheritance.
> 3. A specific `HondaCivic` with VIN `XYZ123` is an **instance** (object), not a class. This is **classification to instantiation** — the point where the tree stops being classes and starts being objects.
> 4. Multiple inheritance "affects clarity of classification" because a class now has **multiple parents**. Where does `TeachingAssistant` go in a clean tree? It IS A `Student` AND IS AN `Employee`. The classification hierarchy stops being a clean tree and becomes a graph — harder to reason about.

---

### Drill 10: Default vs Strict Inheritance (Conceptual Comparison)

Compare the behavior of default and strict inheritance for this base class:

```cpp
class Base {
public:
    int data;
    void process() { data *= 2; }
};
```

1. Under **default** inheritance, what can a derived class do to `data` and `process()`?
2. Under **strict** inheritance, what restrictions apply?
3. In C++, what keyword enables strict inheritance on `process()`?

> [!success]- Show Answer
> 1. **Default inheritance:** The derived class can freely:
>    - Reassign `data` to any `int` value
>    - Override `process()` with a new implementation
>    - Change the access level of inherited members
>    - Add new members alongside the inherited ones
> 2. **Strict inheritance:** The derived class:
>    - Cannot override `process()` — it is frozen
>    - Cannot modify constraints on `data`
>    - All inherited members retain their original definitions and behaviors
> 3. In C++11+, the `final` keyword: `void process() final { data *= 2; }` prevents derived classes from overriding `process()`. This is the C++ mechanism for strict inheritance on individual methods. For preventing an entire class from being inherited: `class Base final { };`.

---

### Drill 11: Three Aspects of Classification — Match the Description

Match each design scenario to the correct aspect of classification/inheritance:

| Scenario | Aspect |
|----------|--------|
| All `Employee` subclasses share `name`, `id`, `getDetails()` | ? |
| `SalariedEmployee` changes `calculatePay()` to divide salary by 12 instead of using hourly rate | ? |
| `Shape` declares `draw()` but provides no implementation — each subclass must implement it | ? |

> [!success]- Show Answer
> - "All `Employee` subclasses share `name`, `id`, `getDetails()`" → **Commonality.** The base class captures the common information and features shared across derived classes.
> - "`SalariedEmployee` changes `calculatePay()`" → **Customization.** An existing class (`Employee`) is used to create a customized version (`SalariedEmployee`) with modified behavior.
> - "`Shape` declares `draw()` but provides no implementation" → **Common Design Interface.** The base class defines design requirements for derived classes by specifying member functions that MUST be provided.

---

### Drill 12: Three Dimensions of Sharing — Categorize

Classify each described sharing mechanism along the three dimensions (static/dynamic, implicit/explicit, per-object/per-group):

| Mechanism | Static/Dynamic | Implicit/Explicit | Per-Object/Per-Group |
|-----------|---------------|-------------------|---------------------|
| C++ class inheritance: `class Dog : public Animal` | ? | ? | ? |
| JavaScript prototype delegation (object `dog` delegates to `animal`) | ? | ? | ? |

> [!success]- Show Answer
> - **C++ class inheritance:** **Static** (fixed at compile time), **Implicit** (compiler auto-resolves), **Per-Group** (defined at class level for all instances).
> - **JavaScript prototype delegation:** **Dynamic** (prototype chain is traversed at runtime when property is accessed), **Implicit** (lookup happens automatically), **Per-Object** (each object can have its own prototype; changing `dog.__proto__` at runtime changes behavior for that single object).
>
> **Exam fact:** The lecture presents these three dimensions to show that C++'s inheritance model is only one point in a broader design space. Understanding the alternatives helps you recognize what C++ does AND does not do.

---

### Drill 13: Constructor Auto-Generation (Lec6 Review from Lec7)

Given this class:

```cpp
class Widget {
private:
    int value;
public:
    Widget(int v) { value = v; }
};
```

1. Does `Widget` have a default constructor?
2. Will `Widget w;` compile? Why or why not?
3. If no constructors were defined at all, would `Widget w;` compile? Why?

> [!success]- Show Answer
> 1. **No.** `Widget` defines a parameterized constructor `Widget(int)`. Because the programmer wrote ANY constructor, the compiler does NOT generate a default constructor.
> 2. **No.** `Widget w;` tries to call the default constructor, which does not exist. Compile error: no matching function for call to `Widget::Widget()`.
> 3. **Yes.** If no constructors were defined at all, the compiler would generate a default constructor. `Widget w;` would compile and `value` would be uninitialized (garbage value for built-in types).
>
> **Rule:** Write any constructor → compiler stops generating the default constructor. Same logic applies to destructor auto-generation.

---

### Drill 14: Composition vs Inheritance — Design Decision

You are designing a `Library` class. It stores a collection of `Book` objects. Should `Library` inherit from `Book` or contain a `Book` array as a member?

Justify with "is-a" vs "has-a."

> [!success]- Show Answer
> **A `Library` SHOULD NOT inherit from `Book`.**
>
> - **"Is-a" test:** Is a `Library` a `Book`? **No.** A library is a collection of books, not a specific kind of book. Inheritance would model that a `Library` IS A `Book`, which is false.
> - **"Has-a" test:** Does a `Library` HAVE `Book` objects? **Yes.** A library contains books as part of its state.
>
> **Solution:** Use composition — `Library` has a member like `Book* books` (array) or `vector<Book> books`.
>
> **Rule of thumb:** If you can say "X IS A Y," use inheritance. If you can say "X HAS A Y," use composition. Misapplying inheritance creates fragile, confusing hierarchies.

---

### Drill 15: Substitutability Principle

```cpp
class Person {
public:
    string name;
    virtual void introduce() { cout << "I am " << name; }
};

class Student : public Person {
public:
    int studentID;
    void introduce() override { cout << "Student " << name << " #" << studentID; }
};

void greet(Person& p) {
    p.introduce();
}

int main() {
    Student s;
    s.name = "Alice";
    s.studentID = 12345;
    greet(s);             // (A) Legal?
    Person* ptr = &s;     // (B) Legal?
    Student* sptr = ptr;  // (C) Legal? (Assume explicit cast)
}
```

Answer: Is (A) legal? Is (B) legal? Is (C) safe? Explain each.

> [!success]- Show Answer
> **Line (A):** LEGAL. `greet()` expects a `Person&`. A `Student` IS A `Person`, so a `Student` object can be passed where a `Person` reference is expected. This is the substitutability principle. The call resolves to `Student::introduce()` (dynamic dispatch).
>
> **Line (B):** LEGAL. Upcasting from `Student*` to `Person*` is always safe and implicit. `ptr` now points to the `Person` subobject of `s`.
>
> **Line (C):** NOT SAFE (compile error without a cast). Downcasting from `Person*` back to `Student*` requires an explicit cast because the compiler cannot guarantee that `ptr` actually points to a `Student`. If `ptr` pointed to a plain `Person`, the cast would succeed syntactically but accessing `studentID` would be undefined behavior.
