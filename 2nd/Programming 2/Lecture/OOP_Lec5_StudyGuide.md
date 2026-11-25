# Lec5: Objects and Classes (Conceptual) — Study Guide

---

## 1. CONCEPT CARD

### 1.1 What It Is

A **class** is a template (blueprint) that defines two things for a group of objects:
- **Data structure** — the state descriptors (attributes, data members) each object will carry
- **Methods** — the operations (behaviors, member functions) each object can perform

An **object** is one concrete instance created from that template. It has:
- **Identity** (a unique name or reference that distinguishes it from all other objects)
- **State** (the current values of its attributes at a particular time)
- **Behavior** (what it can do, defined by the class's methods)

> [!success]- Show Answer — Three-Part Definition (Booch)
> > "Something that has state, behavior, and identity."

> [!success]- Show Answer — Martin/Odell Definition
> > "Anything, real or abstract, about which we store data and those methods that manipulate the data."

> [!success]- Show Answer — Peter Müller Definition
> > "An object is an instance of a class. It can be uniquely identified by its name and it defines a state which is represented by the values of its attributes at a particular time."

### 1.2 What Problem It Solves

Before classes, data and functions lived separately. If you needed three bank accounts, you declared three separate balance variables, three separate deposit functions, etc. There was no way to say "these balances and these deposit rules belong together as one logical unit."

Classes solve this by:
- **Bundling** data and the functions that operate on it into one named unit
- **Encapsulating** — hiding internal details behind a public interface so callers can't corrupt the object
- **Reusing** — defining the pattern once, then stamping out as many independent instances as you need
- **Modeling** — letting you map real-world entities directly to program constructs (a `Student` in code corresponds to a student in reality)

### 1.3 How It Works

1. You write a **class definition** listing data members (state) and member functions (behavior).
2. The class acts as a **factory**: you call its constructor to create objects.
3. The class acts as a **classifier**: all objects of that class share the same structure.
4. Each object gets its own **independent copy** of data members.
5. All objects of the same class **share** the same function code (one copy in memory).
6. Objects communicate by **sending messages** — calling each other's public methods.
7. The **interface** (set of public methods) determines what outsiders can ask the object to do.

> [!success]- Show Answer — The 7-Step Mental Model
> > ```
> > Class Definition → Factory (constructor) → Objects (instances)
> >                                          ↕
> >                             each has own data, shared code
> >                                          ↕
> >                             communicate via messages (method calls)
> >                                          ↕
> >                     only public methods form the interface
> > ```

### 1.4 Concrete Example

A hotel reservation system. The class `Room` defines that every room has a number, a type, a rate, and a status (vacant/occupied). You create object `room_301` and object `room_302`. Both follow the same blueprint but hold different actual data (different room numbers, possibly different rates). The `book()` method exists once in the class code, but when you call `room_301.book("Alice")`, it modifies `room_301`'s data only.

### 1.5 What It Is NOT

- **NOT a C struct.** A C struct is a passive bag of data with no built-in behavior. A class bundles data WITH functions and controls access.
- **NOT the same as an instance.** The class is the blueprint; the object is the house built from that blueprint. Confusing the two is like confusing the recipe with the cake.
- **NOT a namespace.** A class provides encapsulation and instantiation; a namespace only groups names.
- **NOT necessarily a physical thing.** Objects can represent abstract concepts: a `Transaction`, a `Reservation`, a `Set`, a `Payment`.

---

## 2. UNDERSTANDING OBJECTS

### 2.1 Object-Based Programming

Object-based programming views the world as a **collection of autonomous, interacting objects**. Instead of a single procedural flow, the system is composed of entities that each know how to do their own job and communicate with others.

Key idea: you don't tell an object *how* to do something step-by-step; you send it a message asking it to do something, and it figures out how.

Examples of real-world objects viewable this way:
- **People** (autonomous, communicative, have names, are born/die)
- **Animals, plants** (living entities with behaviors)
- **Buildings, rooms, stairs** (structural entities with properties)
- **Computers, phones** (devices that process and communicate)

> [!success]- Show Answer — What makes a program "object-based"?
> > A program is object-based when its primary organizing principle is objects — not functions, not procedures, not data flows. Objects hold their own state and respond to messages. Even without inheritance or polymorphism, if you organize code around objects with encapsulated state and message-passing interfaces, you're doing object-based programming.

### 2.2 Real-World Object Properties

Real-world objects exhibit five key properties. Understanding these helps you design better virtual objects:

| Property | Meaning | Real-World Example |
|---|---|---|
| **Active / Autonomous** | Each object has its own behaviors; not directly controlled from outside | A person thinks independently; a dog barks on its own |
| **Communicative** | Objects can send and receive messages to/from other objects | A person speaks to another; a phone sends a signal to a tower |
| **Collaborative** | Long-term relationships between objects arise through repeated interaction | A teacher and student collaborate over a semester |
| **Nested** | Complex objects contain other objects as components | A car contains an engine, wheels, seats |
| **Uniquely named / identifiable** | Every object has an identity that distinguishes it | A person has an NRIC; a computer has a serial number |
| **Created / Destroyed** | Objects come into and go out of existence | A person is born and dies; a building is constructed and demolished |

> [!success]- Show Answer — Why are these six properties important for design?
> > When you design a class, ask yourself: Is my object autonomous (or is it just a passive data holder)? Does it communicate with others through a well-defined interface? Does it collaborate (maintain references to other objects)? Is it composed of sub-objects (composition)? Does it have a unique identity? Is its lifecycle (creation/destruction) properly managed? These checks produce robust OO designs.

### 2.3 Concrete Examples of Real-World Objects

**A Person:**
- Autonomous: thinks, decides, acts
- Communicative: speaks, writes, gestures
- Collaborative: has friends, colleagues, family relationships
- Identifiable: has a name, NRIC, passport number
- Lifecycle: born (created), dies (destroyed)

**A Computer:**
- Autonomous: processes instructions, runs programs
- Communicative: network cards, USB, Bluetooth
- Collaborative: part of a network, interacts with peripherals
- Identifiable: serial number, MAC address, hostname
- Lifecycle: manufactured (created), decommissioned (destroyed)

### 2.4 Virtual Objects

Virtual objects are objects that exist **only in programs** (not in the physical world). They share the same six properties but are:

- **More precise** in names, boundaries, and interactions (no ambiguity)
- **Fully defined** — every possible state and behavior is specified by the programmer
- The **basic building blocks** of object-oriented programs

Examples from the lecture:

| Virtual Object | State (Data) | Behavior (Methods) |
|---|---|---|
| **Bank Account** | balance, accountNumber | deposit(amt), withdraw(amt), getBalance() |
| **Set** | collection of elements | add(e), remove(e), contains(e), size() |
| **E-Ticket** | eventName, seatNumber, paymentStatus | confirmPayment(), isPaid(), getSeat() |
| **Payment** | amount, payer, payee, timestamp | process(), refund(), getStatus() |

> [!success]- Show Answer — What makes a virtual object different from a real-world object?
> > Virtual objects are fully specified by the programmer — every boundary, behavior, and interaction is exact. Real-world objects have fuzzy boundaries (where does a "river" end?), ambiguous behaviors (what does "thinking" mean precisely?), and uncontrolled interactions. Virtual objects are idealized, simplified models of whatever they represent.

### 2.5 Virtual Object Example: a Set

A `Set` is one of the cleanest examples from the lecture. It understands four messages:

| Message | Effect (internal change) | Return Value |
|---|---|---|
| `add(anElement)` | Inserts element if not present | none (void) |
| `remove(anElement)` | Deletes element if present | none (void) |
| `contains(anElement)` | No internal change | true/false |
| `size()` | No internal change | integer count |

Each message has **both** an effect (what changes inside the object or what messages it triggers) **and** a return value (what it sends back to the caller). Users only need to know the **external view** (the interface) to use the Set — they never see the internal data structure.

### 2.6 Sets in Non-OOP Languages

This is a critical contrast the lecture draws. In a procedural (non-OOP) language:

- A `Set` is a **passive structure** (just data, like a C struct)
- Operations are **active but stateless functions** — they don't remember anything between calls
- You write: `procedure add(s: Set, e: Element)` — the set is passed as a **parameter**, not using dot notation
- **No encapsulation**: the programmer can directly manipulate the internal data, possibly putting it in a compromised (inconsistent) state
- The function `add` doesn't "belong" to the Set — it's just a standalone procedure that happens to take a Set as an argument

> [!success]- Show Answer — OOP vs. Procedural Set Operations, side-by-side
> >
> > **OOP Style:**
> > ```
> > mySet.add(42);        // message to object
> > mySet.contains(42);   // object responds
> > ```
> >
> > **Procedural Style:**
> > ```
> > add(mySet, 42);       // function with set as parameter
> > contains(mySet, 42);  // set has no agency
> > ```
> >
> > The key difference: in OOP, the object is the **receiver** of the message. In procedural, the object is just another argument. The OOP version also guarantees encapsulation — you can't bypass `add()` and directly tamper with the internal array.

### 2.7 Definitions of "Object" (from different authors)

The lecture presents three formal definitions. Exams may ask you to compare or match them:

| Author | Definition | Emphasis |
|---|---|---|
| **Booch** | "Something that has state, behavior, and identity." | The three essential properties |
| **Martin / Odell** | "Anything, real or abstract, about which we store data and those methods that manipulate the data." | The data + methods bundle |
| **Peter Müller** | "An object is an instance of a class. It can be uniquely identified by its name and it defines a state which is represented by the values of its attributes at a particular time." | The class-instance relationship and temporal state |

> [!success]- Show Answer — Which definition is most operational (code-oriented)?
> > Müller's, because it explicitly ties the object to its class and defines state concretely as attribute values at a point in time — this maps directly to how you write and debug code.

> [!success]- Show Answer — Which definition is most abstract?
> > Booch's, because "state, behavior, identity" applies to literally anything — a person, a bank account, a process, a file handle. It's a philosophical definition rather than an implementation one.

---

## 3. MESSAGES AND INTERFACES

### 3.1 Definition: Message

A **message** is a request sent to an object to invoke one of its methods. It contains two parts:

1. The **name** of the method to invoke
2. The **arguments** (actual parameters) that the method requires

Key points:
- **Invocation of a method is a reaction** caused by receipt of a message
- A message only succeeds if the method is **actually known** to the object (i.e., defined in its class and accessible)
- In C++, sending a message to a private method is rejected at **compile time**
- Messages have both an **effect** (what the object does internally) and a **return value** (what it sends back)

> [!success]- Show Answer — Message vs. Method Call: are they the same?
> > In C++, "sending a message" IS calling a method — they are synonymous in implementation. But conceptually, "message" emphasizes the **request-receiver** model: you ask the object to do something, and it decides how. "Method call" emphasizes the **mechanical invocation**. The distinction matters in design discussions and in languages (like Smalltalk) where the runtime can handle unknown messages dynamically.

> [!success]- Show Answer — Can a message have an effect but no return value?
> > Yes. `void add(Element e)` in a Set changes the Set's contents but returns nothing. Conversely, `contains(e)` returns a boolean but has no effect on the Set. Every message has BOTH slots — one or both may be empty.

### 3.2 The Interface

The **interface** is the list of operation names (method signatures) that are **open to other objects** — what outsiders are allowed to call.

Critical distinctions:
- If an object has a function but does not expose it publicly, it is **useless to the public** (it is **private**)
- In C++, only **public** functions belong to the interface and can be called by outsiders
- The interface defines the **contract**: "if you send me this message with these arguments, I guarantee this behavior"
- Private members are **implementation details** — the class author can change them freely without breaking any caller

> [!success]- Show Answer — What belongs in the interface vs. hidden internally?
> >
> > | Interface (public) | Hidden (private) |
> > |---|---|
> > | Methods that define what the object CAN DO | Helper methods that support public methods |
> > | Accessors that reveal state safely | Raw data members |
> > | Mutators that change state with validation | Internal counters, caches, flags |
> >
> > Rule of thumb: expose as little as possible. Every public method is a commitment you must maintain.

> [!success]- Show Answer — "A method exists but is not in the interface." When is this true?
> > When the method is declared `private`. The object knows how to perform it, and can call it internally, but no outside object can send that message. In C++, attempting to call a private method from outside the class is a compile-time error.

---

## 4. PROPERTIES AND ADVANTAGES OF OBJECTS

### 4.1 Properties of Objects

| Property | Meaning |
|---|---|
| **Encapsulation** | Data and the operations that manipulate it are bundled together into one unit (the object). You don't have data here and functions there — they live inside the same boundary. |
| **Information Hiding** | Internal implementation details are hidden behind a public interface. Callers only know WHAT an object does, not HOW it does it. The internal data representation can change without affecting callers. |
| **Data Abstraction** (with classes) | The class defines an abstract view of data. Users work with `deposit(amount)` not with `balance += amount`. The abstraction hides the concrete representation. |
| **Abstract Data Type** (with classes) | A class, together with its encapsulation and information hiding, creates an ADT — a user-defined type that behaves like a built-in type. You declare `Set s;` and use `s.add(5)` just as naturally as `int x; x = 5;`. |

> [!success]- Show Answer — Encapsulation vs. Information Hiding: aren't they the same?
> > **Encapsulation** is the MECHANISM — bundling data and methods together. **Information hiding** is the DESIGN PRINCIPLE — deliberately restricting access to internal details. You can have encapsulation without information hiding (e.g., everything public in a class — bundled, but not hidden). Good OO design requires both.

### 4.2 Advantages of Objects

| Advantage | Explanation |
|---|---|
| **Same benefits as ADTs** | Information hiding, data abstraction, and procedural abstraction all apply |
| **Inheritance provides further abstraction** | Subclasses refine and specialize behavior without rewriting base functionality (covered in Lec7 and Lec8) |
| **Easier and less error-prone development** | Objects map directly to real-world concepts; each object has a limited, well-defined responsibility; fewer unintended side effects |
| **Easier maintenance** | Changes to one class's internals don't ripple through the entire program; the interface remains stable; bugs are localized |
| **Modularity** | Objects are natural modules — self-contained, independently testable, independently understandable |
| **Reusability** | Well-designed classes can be reused across projects (e.g., a `Set`, a `Date`, a `BankAccount`) |

> [!success]- Show Answer — Which advantage is most relevant for a large team working on a long-lived product?
> > Easier maintenance. In a large team over years, the original authors leave, requirements change, and bugs are found. Information hiding means a new developer can fix or change a class's internals without understanding the entire system — as long as the public interface stays the same.

---

## 5. CLASSIFICATION AND CLASSES

### 5.1 Classification

Classification is the process of grouping things based on common characteristics. It is **not unique to OOP** — it is applied in biology, library science, chemistry, and many other domains.

The lecture uses a hierarchy diagram:

```
Animal
├── Mammal
│   ├── People
│   │   ├── man
│   │   │   ├── John
│   │   │   └── ...
│   │   └── woman
│   │       ├── Jane
│   │       └── ...
│   └── Dog
│       ├── Fido
│       └── ...
└── Bird
    ├── Sparrow
    └── ...
```

Classification is the **basic idea for understanding inheritance**: a subclass IS-A more specific kind of its superclass. This conceptual foundation is what Lec7 builds on.

> [!success]- Show Answer — Why does the lecture introduce classification before classes?
> > Because a class IS a classification mechanism. When you write `class Dog { ... }`, you are classifying all dogs as sharing certain attributes and behaviors. Seeing classification as a general cognitive tool (not just a programming construct) helps you understand why classes are a natural way to model the world.

### 5.2 What Is a Class?

From the lecture, a class serves two distinct roles:

**Role 1 — Classification (specification only):**
A class is a definition of what it means to be a member of that category. It specifies the structure (what data) and behavior (what methods). This is the **abstract, conceptual** role.

**Role 2 — Implementation (code + specification):**
A class is a practical programming mechanism — a template that the compiler uses to allocate memory and generate code. This is the **concrete, mechanical** role.

Two formal definitions from the lecture:
- "Class — a definition of an implementation (methods and data structures) shared by a group of objects."
- "Class — a template from which objects may be created. Contains definition of state descriptors and methods for the objects."

> [!success]- Show Answer — OOP is "programming with classes." Why not "programming with objects"?
> > Because the class is the central organizing mechanism. Objects are created from classes, their structure is defined by classes, and their behavior is implemented in classes. Without classes, you'd have ad-hoc objects with no shared structure — which is just procedural programming with structs. The class gives you classification, instantiation, encapsulation, and (later) inheritance all in one construct.

### 5.3 Intentional Notion of Class

The **intentional notion** is the class viewed as a **template or blueprint**:

- New objects are **instances** of a class
- The **state** (data members) and **behavior** (methods) of every instance are determined by the class definition
- The intentional notion determines the **structure** of instances — what slots (attributes) every instance will have and what operations it can perform
- Think of it as: "Here is what an X looks like" — the definition, not the collection

> [!success]- Show Answer — Intentional notion in one sentence
> > The intentional notion is the class as a definition of structure — it says what every instance will look like before any instances exist.

### 5.4 Extensional Notion of Class

The **extensional notion** is the class viewed as a **warehouse and factory**:

- **Object warehouse**: the class implicitly maintains a **class extent** — the collection of all instances that currently exist
- **Object factory**: each class has a **constructor** — a mechanism to generate new instances
- The extensional notion tracks **how many** objects exist and **which** objects exist
- Think of it as: "Here are all the X's that currently exist" — the collection, not the definition

> [!success]- Show Answer — Extensional notion in one sentence
> > The extensional notion is the class as a container/creator — it keeps track of and produces actual instances.

> [!success]- Show Answer — Intentional vs. Extensional — the key test question
> >
> > | Aspect | Intentional | Extensional |
> > |---|---|---|
> > | What it describes | Structure/blueprint | Collection of instances |
> > | Answers the question | "What IS an X?" | "Which X's exist?" |
> > | C++ manifestation | The class definition itself | `static` member tracking instances, constructors |
> > | Exists before any objects? | Yes | No (empty extent) |

### 5.5 Understanding Classes — Summary

A class provides:
1. A definition of the **structure** of instances of that class (intentional)
2. The **names** and types of attributes (state) that objects belonging to the class will hold
3. The **names** and signatures of methods (behavior) that objects belonging to the class can execute

Together: class → structure definition → instances with that structure → objects that share the definition but hold independent state.

### 5.6 Examples of Class (from lecture)

**Example 1 — Integer:**

```
class Integer {
    Ds: int I;                          // data: the integer value
    Ops: setValue(int n);               // operation: assign a value
         Integer addValue(Integer j);   // operation: add another Integer
};
```

This shows the "Ds + Ops" notation used in the lecture. Data members (Ds) define state; operations (Ops) define behavior.

**Example 2 — Horse:**

```
class Horse {
    Ds: Age, Weight, Color;    // attributes every horse has
    Ops: Drag, Run, Ride;      // behaviors every horse can do
};
```

> [!success]- Show Answer — What do the Ds/Ops examples teach us?
> > That a class is defined by TWO things, always: data and operations. If you only have data (like a C struct) it's not a class. If you only have functions (like a namespace) it's not a class. A class always bundles both.

### 5.7 Relationships Among Classes

Classes don't exist in isolation. The lecture identifies two fundamental relationships (plus one previewed for later):

| Relationship | Also Called | Meaning | Example |
|---|---|---|---|
| **Link** | "use-a" | An instance of one class sends a message to an instance of another. The two classes need to communicate. | A `Driver` uses a `Car` — calls `car.start()`, `car.accelerate()` |
| **Composition** | "has-a" | One class contains data members that are themselves objects of another class. The part belongs to the whole. | A `Car` has an `Engine` — `Engine` is a data member of `Car` |
| **Inheritance** | "is-a" | One class is a specialized kind of another. Previewed here, covered in Lec7/8. | A `Dog` is an `Animal` |

UML (Unified Modeling Language) is introduced as the standard visual notation for representing classes and their relationships.

> [!success]- Show Answer — "use-a" vs. "has-a": how to tell them apart
> >
> > | Question | "use-a" (Link) | "has-a" (Composition) |
> > |---|---|---|
> > | Is the other object a **data member**? | No — it's passed in or accessed via a method call | Yes — it's declared as an attribute |
> > | Does the object **own** the other? | No — temporary relationship | Yes — lifetime is tied |
> > | If this object dies, does the other die too? | No | Usually yes |
> >
> > Think of it this way: if you can draw an arrow labeled "sends message to" between them, it's use-a. If you can say "is part of," it's has-a.

---

## 6. INSTANTIATION

### 6.1 What Is Instantiation?

**Instantiation** is the mechanism of creating new objects from a class definition. Every class has such a mechanism — typically a **constructor**. The class is the cookie cutter; instantiation is the act of pressing it into dough to make a cookie.

### 6.2 Static vs. Dynamic Instantiation

| Aspect | Static | Dynamic |
|---|---|---|
| **When?** | Compile time | Run time |
| **Who allocates?** | Compiler (on the stack) | Programmer requests (on the heap) via `new` |
| **Lifetime** | Automatic — destroyed when out of scope | Manual — must call `delete` to destroy |
| **Syntax** | `ClassName obj(args);` | `ClassName* obj = new ClassName(args);` |
| **Memory location** | Stack | Heap |
| **Overhead** | None (fast) | Runtime allocation cost |

Dynamic instantiation requires **run-time support** for allocation (`new`) and deallocation (`delete`) of memory.

> [!success]- Show Answer — When would you use dynamic over static?
> > Use dynamic when: (1) you don't know how many objects you need at compile time, (2) the object needs to outlive the scope where it's created, (3) the object is very large (stack space is limited). Use static for small, short-lived objects with known quantity.

### 6.3 Making Objects from Class Templates

```java
aSet = new Set();        // Set is the class; new Set() makes an object
anotherSet = new Set();  // Same factory (class), different object (contents)
```

- Both `aSet` and `anotherSet` share the same class definition (same structure)
- They are **different objects** — each has its own independent data
- `aSet.add(5)` does NOT affect `anotherSet` in any way
- Each call to `new` produces a **new and unique** object

### 6.4 Object Structure

The lecture gives a formal decomposition of an object:

```
Object ::= <Oid, Cid, Body>
```

| Component | Meaning |
|---|---|
| **Oid** | Object Identifier — the unique identity of this specific object |
| **Cid** | Class Identifier — the name (or identity) of the class this object belongs to |
| **Body** | The actual memory space holding the object's data (attribute values) |

Critical note: the **operations** (methods) of the object are implemented in the **CLASS**, not duplicated in every object. Each object only stores its own data; all objects of the same class share one copy of the code.

> [!success]- Show Answer — Why aren't methods stored in the Body?
> > Efficiency. If you have 10,000 `Student` objects, you don't want 10,000 copies of `attendLecture()` in memory. The methods live in the class; each object just stores a pointer (Cid) back to its class so the right code is executed. The Body only holds per-instance data.

### 6.5 Example of Class in C++ (Student class from lecture)

```cpp
class Student {
private:
    unsigned numCoursesRequired;
    unsigned age;
public:
    Student(unsigned nCourses);      // constructor
    void attendLecture();            // behavior
    void selfStudy();                // behavior
    void play();                     // behavior
};
```

This demonstrates:
- `private` data (encapsulated — outsiders cannot touch `age` directly)
- `public` interface (the three methods + constructor are callable from outside)
- Constructor with a parameter (initialization at creation time)
- Each `Student` object gets its own `numCoursesRequired` and `age`

> [!success]- Show Answer — Trace: what happens when we write `Student s(5); s.attendLecture();`?
> > 1. Constructor `Student(5)` allocates memory (Body) with Oid=Cid=Student.
> > 2. `numCoursesRequired` is set to 5, `age` is uninitialized (or defaulted).
> > 3. `s.attendLecture()` sends a message to object `s`.
> > 4. The method is found via Cid → `Student::attendLecture()` executes.
> > 5. The method modifies `s`'s Body only — other Student objects are unaffected.

---

## 7. META-CLASSES

### 7.1 What Is a Meta-class?

A **meta-class** is the class of a class. If you treat a class itself as an object, then: what class does that object belong to? The answer is a **meta-class**.

```
Regular level:   object   → instance of →   class
Meta level:      class    → instance of →   meta-class
```

- A meta-class defines the **structure and behavior of classes**
- Just as a class defines what its instances look like, a meta-class defines what classes look like

### 7.2 Purpose and Properties

| Purpose / Property | Explanation |
|---|---|
| **Class-level attributes** | Meta-class attributes can describe a class itself (e.g., number of instances of a class, author, version, creation date) |
| **Uniform treatment** | In languages with explicit meta-class support, objects, classes, AND meta-classes are treated uniformly — they're all objects |
| **Run-time class creation** | Classes can be created at run-time by sending a message to a special meta-class (e.g., `MetaClass.new("MyNewClass")`) |
| **Reflection** | Meta-classes enable reflection — a program can inspect and modify its own structure at run time |

> [!success]- Show Answer — Does C++ have meta-classes?
> > **No.** C++ does not have meta-classes as a language feature. There is no built-in way to treat a class as a runtime object, no class-level attributes (beyond `static` members, which are per-class data, not an external meta-object), and no way to create new classes at runtime. This lecture material is theoretical — it won't appear as C++ syntax on an exam, but understanding the concept helps you grasp what languages like Smalltalk, Python (with metaclasses), and Ruby offer.

> [!success]- Show Answer — If C++ has no meta-classes, why learn about them?
> > Because the concept completes the abstraction ladder: object → class → meta-class. It shows that classes are not the final word in OOP theory. It also explains why, in some languages, you CAN ask a class "how many instances do you have?" or create new classes programmatically. Understanding the ceiling of the abstraction helps you understand the floor.

---

## 8. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
class ClassName {                    // Template/blueprint definition
private:                             // State: data members (per-object)
    int attribute1;                  // Each OBJECT gets its own copy
    double attribute2;
public:                              // Behavior: member functions (shared)
    ClassName(int a, double b);      // Constructor: creates new object
    void method1();                  // Message receiver (mutator)
    int method2() const;             // const = won't modify object (accessor)
};                                   // MANDATORY semicolon — FORGET THIS = -2 marks

// Creating objects (instantiation):
ClassName obj1(5, 3.14);                      // Static: on the stack, auto-destroyed
ClassName *obj2 = new ClassName(10, 2.71);    // Dynamic: on the heap, must delete

// Cleanup:
delete obj2;    // single object deletion
// obj1 auto-destroyed when out of scope — no manual delete needed
```

> [!success]- Show Answer — The semicolon after the class closing brace
> > `class Foo { ... };` ← That semicolon is NOT optional. In C++, a class definition is a declaration, and declarations end with semicolons. Forgetting it is one of the most common compile errors and a guaranteed mark deduction on handwritten code.

> [!success]- Show Answer — Static vs. Dynamic: the complete syntax reference
> >
> > ```cpp
> > // STATIC (stack)
> > ClassName obj;                 // default constructor
> > ClassName obj(args);           // parameterized constructor
> > ClassName arr[10];             // array of 10, default ctor each
> >
> > // DYNAMIC (heap)
> > ClassName* p = new ClassName;          // single, default ctor
> > ClassName* p = new ClassName(args);    // single, parameterized ctor
> > ClassName* arr = new ClassName[10];    // array of 10, default ctor each
> >
> > // CLEANUP (heap only — stack auto-destroys)
> > delete p;        // single object
> > delete[] arr;    // array — WRONG PAIRING = undefined behavior
> > ```

---

## 9. EXAM TRAPS

### 9.1 Static vs. Dynamic Instantiation

- **Wrong:** `ClassName obj = new ClassName();` (mixing stack declaration with heap allocation)
- **Right:** `ClassName obj(args);` (static) or `ClassName* obj = new ClassName(args);` (dynamic)
- **Trap:** Static = compiler allocates on stack, auto-destroyed when out of scope. Dynamic = heap, you must `delete` manually.
- **Trap:** Forgetting `delete[]` for arrays. `new ClassName[5]` must be paired with `delete[] arr;` — NOT `delete arr;`

### 9.2 Data Members Are Per-Object, Functions Are Shared

- **Wrong:** Believing all objects share data members. They don't. Each object has its own `age`, `balance`, etc.
- **Right:** Only member functions are shared (one copy in code memory). Data members are duplicated per object.
- **Trap:** A `static` data member IS shared — but that's the exception, not the rule.

### 9.3 Class Relationships — NOT Interchangeable

- **"use-a" (Link):** One object calls another's method. `Driver` uses `Car`. No ownership, temporary relationship.
- **"has-a" (Composition):** One class contains another as a data member. `Car` has `Engine`. Ownership, lifetime tied.
- **"is-a" (Inheritance):** Covered in Lec7/8. `Dog` is an `Animal`. NOT the same as use-a or has-a.
- **Trap:** Exams will ask you to classify a relationship. If `Car` has a method `void setEngine(Engine e)`, that's use-a, not has-a — the Engine is passed in, not stored as a member.

### 9.4 Messages = Method Calls

- In OOP theory, "sending a message" means calling a method. If the method is private, the message is rejected at **compile time** in C++.
- **Trap:** Writing `obj.privateMethod()` in code that's supposed to work. If it's private, it won't compile.

### 9.5 The Class Definition IS the Interface

- Only `public` members form the interface. Private members are implementation details — outsiders can't call them even if they know the names.
- **Trap:** Listing a private method as part of the "interface" on a theory question. The interface = public methods only.

### 9.6 Meta-class Is a Theoretical Concept

- **Trap:** Trying to write `class ClassName : public meta_class` — C++ doesn't have meta-classes as a language feature. This lecture is conceptual/theoretical.
- Meta-class questions on exams will be definitional: "What is a meta-class?" "Why might a language support them?" — not "Write C++ code using meta-classes."

### 9.7 Intentional vs. Extensional Notion

- **Trap:** Confusing "what structure instances have" (intentional) with "which instances exist right now" (extensional).
- **Trap:** Thinking extensional notion is unnecessary. It's the concept behind `static` member tracking (counting instances), factories, and object pools.

### 9.8 Encapsulation vs. Information Hiding

- **Trap:** Using them as synonyms on an exam. Encapsulation is the mechanism (bundling). Information hiding is the design principle (restricting access). You can have encapsulation without information hiding.

### 9.9 Objects vs. ADTs

- **Trap:** Thinking Abstract Data Types and objects are different concepts. A well-designed class IS an ADT — it creates a user-defined type that behaves like a built-in type. The terms are closely related in OOP.

### 9.10 Classification vs. Instantiation

- **Trap:** Saying "Dog is an instance of Animal." This is WRONG. `Dog` IS-A `Animal` (classification/inheritance). `Fido` IS-AN-INSTANCE of `Dog` (instantiation). Classification relates classes to superclasses; instantiation relates objects to classes.

---

## 10. HAND-CODING DRILLS

### Drill 1: Class from Description

A digital music player tracks songs. Each song has a title, artist name, and duration in seconds. Users can play a song (prints "Playing [title] by [artist]"), get the title, and get the duration. Write the full class definition with private data and public interface.

> [!success]- Show Answer
> > ```cpp
> > class Song {
> > private:
> >     char title[100];
> >     char artist[100];
> >     int duration; // in seconds
> > public:
> >     Song(const char t[], const char a[], int d) {
> >         int i = 0;
> >         while (t[i]) { title[i] = t[i]; i++; }
> >         title[i] = '\0';
> >         i = 0;
> >         while (a[i]) { artist[i] = a[i]; i++; }
> >         artist[i] = '\0';
> >         duration = d;
> >     }
> >     void play() {
> >         cout << "Playing " << title << " by " << artist << endl;
> >     }
> >     const char* getTitle() const { return title; }
> >     int getDuration() const { return duration; }
> > };
> > ```

> [!success]- Show Answer — Drill 1 Concept Check
> > - Which members form the **interface**? `Song()`, `play()`, `getTitle()`, `getDuration()` — all the public ones.
> > - Which members form the **state**? `title`, `artist`, `duration` — all the private data.
> > - Does this class demonstrate **encapsulation**? Yes — data and methods are bundled together.
> > - Does it demonstrate **information hiding**? Yes — callers cannot access `title`/`artist`/`duration` directly; they must use accessors.
> > - Is this a virtual object? Yes — a Song in a music player is a program construct, not a physical thing.
> > - Does `Song` have the six object properties (Section 2.2)? Autonomous (has its own behavior), Communicative (responds to messages), Nested (could contain other objects), Identifiable (each Song object is distinct), Created/Destroyed (constructor/destructor), Collaborative (could interact with Playlist objects).

### Drill 2: Instantiation Styles

Given `class Widget { public: Widget(); Widget(int x); };`, write code that creates:
(a) A single Widget with default constructor on the stack
(b) An array of 5 default Widgets on the heap
(c) A single Widget with parameter 42 on the heap
Then show the `delete` statements needed to clean up (b) and (c).

> [!success]- Show Answer
> > ```cpp
> > Widget w1;                        // (a) stack, default ctor
> > Widget* arr = new Widget[5];      // (b) heap array, 5x default ctor
> > Widget* w2 = new Widget(42);      // (c) heap, parameterized ctor
> >
> > delete[] arr;  // array delete for (b)
> > delete w2;     // single delete for (c)
> > // w1 is auto-destroyed when it goes out of scope
> > ```

> [!success]- Show Answer — Drill 2 Concept Check
> > - Which is static instantiation? (a). Compiler allocates on the stack at compile time.
> > - Which are dynamic instantiation? (b) and (c). `new` allocates on the heap at run time.
> > - What happens if you write `delete arr;` instead of `delete[] arr;`? Undefined behavior — only the first element's destructor runs. Always match `new[]` with `delete[]`.
> > - Why doesn't (a) need a `delete`? It's on the stack — automatically destroyed when the enclosing block ends (scope exit).

### Drill 3: Classification vs. Instantiation

Explain the difference between a class's "intentional notion" and "extensional notion" from the lecture. Then demonstrate both by writing a class `Library` that:
- Intentionally defines what a library is (shelves, books, name)
- Extensionally maintains a count of how many Library objects exist

> [!success]- Show Answer
> > **Intentional notion** = the class as a template that defines STRUCTURE (what data and methods instances will have). It's the blueprint.
> > **Extensional notion** = the class as a warehouse/factory that TRACKS all its instances. It knows what objects have been created.
> >
> > ```cpp
> > class Library {
> > private:
> >     int numShelves;
> >     int numBooks;
> >     char name[50];
> >     static int totalLibraries;  // extensional: tracks all instances
> > public:
> >     Library(const char n[], int shelves, int books) {
> >         int i = 0;
> >         while (n[i]) { name[i] = n[i]; i++; }
> >         name[i] = '\0';
> >         numShelves = shelves;
> >         numBooks = books;
> >         totalLibraries++;        // each new object increments count
> >     }
> >     ~Library() { totalLibraries--; }
> >     static int getTotalLibraries() { return totalLibraries; }
> > };
> > int Library::totalLibraries = 0;
> > ```

> [!success]- Show Answer — Drill 3 Concept Check
> > - Which part is intentional? The private data members (`numShelves`, `numBooks`, `name`) and the public methods — they define what every Library looks like.
> > - Which part is extensional? `totalLibraries` and `getTotalLibraries()` — they track the collection of all Library instances.
> > - Does `static int totalLibraries` belong to any specific object? No — it belongs to the class itself (the extensional notion). It's one shared variable, not per-instance.
> > - How does this relate to meta-classes (Section 7)? A true meta-class would make `totalLibraries` a property of the class-as-object. In C++, `static` members are a partial workaround — they give class-level data but without true meta-class support.

### Drill 4: Interface Identification

Given the `Student` class from Section 6.5, identify:
(a) The state (data members)
(b) The interface (what outsiders can call)
(c) What messages a `Student` object responds to

> [!success]- Show Answer
> > (a) **State:** `numCoursesRequired` and `age` (both `private unsigned`).
> > (b) **Interface:** `Student(unsigned nCourses)`, `attendLecture()`, `selfStudy()`, `play()`.
> > (c) **Messages:** `attendLecture`, `selfStudy`, `play` — plus the constructor message at creation time.
> >
> > Note: `age` and `numCoursesRequired` are NOT part of the interface — they're private. Outsiders cannot send a "read age" or "write age" message unless a public getter/setter is added.

### Drill 5: Relationship Classification

For each pair below, state whether the relationship is "use-a" (link), "has-a" (composition), or "is-a" (inheritance — preview):
(a) A `Student` registers for a `Course`. The `Student` object calls `course.enroll(this)`.
(b) A `Car` class has a data member of type `Engine`.
(c) A `Library` class stores an array of `Book` objects as a member.
(d) A `Person` class has a method that takes a `Phone` parameter and calls `phone.dial(number)`.

> [!success]- Show Answer
> > (a) **use-a** — Student sends a message to Course, no ownership, temporary interaction.
> > (b) **has-a** — Engine is a data member of Car (composition). It's part of the Car.
> > (c) **has-a** — The array of Books is a data member. Library contains Books.
> > (d) **use-a** — The Phone is passed as a parameter, not stored as a member. Person uses Phone temporarily.

### Drill 6: Real-World Object Identification

For each of the following, identify which of the six real-world object properties (Section 2.2) apply:
(a) A university course registration system
(b) A bank ATM machine
(c) A `Payment` object in an e-commerce system

> [!success]- Show Answer
> > (a) **Course Registration System:**
> > - Active/autonomous: processes registrations independently
> > - Communicative: interacts with Student objects, Course objects
> > - Collaborative: maintains relationships between students and courses
> > - Nested: contains Student objects, Course objects, Registration objects
> > - Identifiable: has a unique semester ID
> > - Created/Destroyed: instantiated for each semester
> >
> > (b) **ATM Machine:**
> > - Active/autonomous: validates cards, dispenses cash independently
> > - Communicative: talks to bank server, interacts with customer
> > - Collaborative: part of banking network
> > - Nested: contains card reader, cash dispenser, screen components
> > - Identifiable: has a unique terminal ID
> > - Created/Destroyed: installed and decommissioned
> >
> > (c) **Payment:**
> > - Active/autonomous: validates amount, processes transaction
> > - Communicative: interacts with Account objects, Order objects
> > - Collaborative: part of a transaction between buyer and seller
> > - Nested: contains transaction details, timestamp
> > - Identifiable: has a unique transaction ID
> > - Created/Destroyed: created when payment occurs, cannot be "undone" (refund creates a new Payment)

### Drill 7: OOP vs. Procedural Set

Rewrite the following procedural Set operations in OOP style. Identify what changes about who is active vs. passive:

```
// Procedural
Set mySet;
add(mySet, 5);
add(mySet, 10);
int count = size(mySet);
bool found = contains(mySet, 5);
remove(mySet, 10);
```

> [!success]- Show Answer
> > ```cpp
> > // OOP Style
> > Set mySet;
> > mySet.add(5);
> > mySet.add(10);
> > int count = mySet.size();
> > bool found = mySet.contains(5);
> > mySet.remove(10);
> > ```
> >
> > **What changed:** In procedural style, the Set is a passive data structure — functions operate ON it. In OOP style, the Set is an active object — it receives messages and responds. The Set is now the agent; the functions are now methods owned by the Set. This is the fundamental shift from procedural to object-oriented thinking: **objects are active, not passive.**
