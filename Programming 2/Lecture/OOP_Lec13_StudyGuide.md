# Lec13: Object-Oriented Design — Study Guide

---

## 1. CONCEPT CARD: OBJECT-ORIENTED DESIGN

### 1.1 What It Is

Object-Oriented Design (OOD) is the process of planning a software system as a set of interacting **objects** that collaborate to solve a problem. It involves identifying classes, their responsibilities, and their relationships. OOD is the bridge between **requirements analysis** (what the system should do) and **implementation** (coding).

### 1.2 What Problem It Solves

Without systematic design, software becomes:
- **Hard to understand** — no clear architecture.
- **Hard to modify** — changes ripple unpredictably.
- **Hard to extend** — new features require rewriting large portions.
- **Hard to maintain** — bugs are difficult to isolate.

OOD produces software with a **clean internal structure** that is easier to test, port, maintain, extend, and understand.

### 1.3 How It Works

The design process follows structured steps:
1. **Find classes** (nouns in the problem description).
2. **Specify operations** (verbs — what each class can do).
3. **Specify dependencies** (inheritance and use relationships).
4. **Specify interfaces** (public vs protected, exact types).
5. **Reorganize** the hierarchy as needed (introduce common bases, split classes).
6. **Model visually** using UML diagrams.

### 1.4 Overarching Strategy — Divide and Conquer

The system is divided into **modules** (objects and classes). The challenge is to ensure **effective communication** between different parts of the software **without destroying the divisions** (i.e., maintain loose coupling).

### 1.5 What It Is NOT

- OOD is **NOT** coding — it's the design phase that precedes implementation.
- OOD is **NOT** just drawing diagrams — it's making deliberate decisions about class structure and relationships.
- OOD is **NOT** a one-time activity — designs evolve iteratively.

---

## 2. THE SOFTWARE DEVELOPMENT CYCLE

### 2.1 Phases

| Phase | Description |
|-------|-------------|
| **Problem Analysis** | Understand what the user needs |
| **Solution Design** | Plan the architecture (classes, relationships) |
| **Coding** | Implement the design |
| **Documenting** | Record decisions, interfaces, usage |
| **Testing** | Verify correctness |
| **Maintenance** | Fix bugs, adapt to new requirements |

### 2.2 Best Practices (How Object Technology Helps)

1. **Develop iteratively** — tolerate changing requirements, integrate elements progressively, facilitate reuse.
2. **Use component-based architectures** — design with reusable components.
3. **Model visually** — use UML for easy understanding and modification.

---

## 3. WHY CLEAN INTERNAL STRUCTURE MATTERS

A well-designed system simplifies:

| Concern | How Clean Structure Helps |
|---------|--------------------------|
| **Testing** | Independent units can be tested in isolation |
| **Porting** | Platform-specific code is encapsulated |
| **Maintenance** | Bugs are localized to specific classes |
| **Extension** | New classes can be added without modifying existing code (Open-Closed Principle) |
| **Re-organization** | Components can be rearranged with minimal impact |
| **Understanding** | Clear class boundaries and responsibilities |

### 3.1 Characteristics of Successful Software

Successful software has an **extended life** where it might be:
- Worked on by a **succession of programmers and designers**.
- **Ported** to new hardware.
- **Adapted** to unanticipated uses.

---

## 4. THE OO DESIGN STEPS

### 4.1 Step 1 — Find the Concepts / Classes

Look at the **application** rather than abstractions. **Nouns** in the problem description typically correspond to **classes**. **Verbs** represent **functions** (operations).

### 4.2 Step 2 — Refine Classes by Specifying Operations

Classify operations into categories:
- **Foundation**: Constructors, destructors, copy operators.
- **Selectors**: Operations that do NOT modify the state of an object (const functions).
- **Modifiers**: Operations that DO modify the state of an object.
- **Conversion Operators**: Produce an object of another type based on the object's state.
- **Iterators**: Traverse collections of objects to process data members.

Consider:
- **Minimalism**: Only include essential operations.
- **Completeness**: Provide all operations users reasonably need.
- **Convenience**: Add operations that improve usability (but don't bloat the interface).
- Which operations should be **virtual**.

### 4.3 Step 3 — Specify Dependencies on Other Classes

Key dependency types:

| Dependency | Description |
|------------|-------------|
| **Inheritance** | "is-a" relationship — derived class depends on base class |
| **Use / Composition** | "has-a" relationship — one class uses or contains another |

**Warning**: Overuse of dependencies leads to inefficient and incomprehensible designs. Keep coupling loose.

### 4.4 Step 4 — Specify Interfaces

- Private functions are **not considered** at this stage (implementation details).
- The interface should be **implementable independently** — more than one implementation should be possible.
- All operations in a class should support the **same level of abstraction**.
- Separate functions into **public** and **protected**:
  - `public` — available to all users of the class.
  - `protected` — available to derived classes only.

### 4.5 Step 5 — Reorganize the Class Hierarchy

Two most common reorganizations:

| Reorganization | When to use |
|----------------|-------------|
| **Introduce a common base** | Two classes share significant functionality — extract shared members into a new base class |
| **Split a class** | A class has too many responsibilities (violates Single Responsibility Principle) — break into two or more classes |

---

## 5. FINDING CLASSES — THE NOUN/VERB TECHNIQUE

### 5.1 Method

1. Take the problem description / requirements document.
2. Underline **nouns** — these are candidate **classes**.
3. Underline **verbs** — these are candidate **operations** (member functions).

### 5.2 Worked Example — Video Store Inventory

**Problem description:**

> When ordering new videotapes from a supplier, the store manager creates a purchase order, fills in the date, the supplier's name, address, and enters a list of videotapes to be ordered. The purchase order is added to a permanent list of purchases. When one or more video tapes are received from a supplier, a clerk locates the original purchase order and makes a record of each tape that was received. A record of the videotape is then added to the store's inventory. When all tapes listed on a particular purchase order have been received, the manager sends a payment to the supplier and the purchase order is given a completion date.

**Candidate classes (nouns):**
- **Videotape** — represents a specific tape title/item
- **Supplier** — name, address
- **PurchaseOrder** — date, supplier, list of tapes, completion date
- **List of Purchases** — collection of purchase orders (permanent list)
- **Inventory** — store's current stock of videotapes
- **Payment** — payment to supplier
- **Store Manager** — actor (might be a class or might just be a permission level)
- **Clerk** — actor

**Candidate operations (verbs):**

| Verb | Likely Class | Operation |
|------|-------------|-----------|
| creates | (Manager) | `createPurchaseOrder()` |
| fills in | PurchaseOrder | `setDate()`, `setSupplier()` |
| enters | PurchaseOrder | `addTape()` |
| added to | List of Purchases | `add()` |
| received | Inventory | `receive()` |
| locates | List of Purchases | `find()` |
| makes a record | PurchaseOrder | `recordReceipt()` |
| added to | Inventory | `addTape()` |
| sends a payment | (Manager) | `sendPayment()` |
| given a completion date | PurchaseOrder | `setCompletionDate()` |

---

## 6. WORKED EXAMPLE — DOCTOR'S OFFICE SCHEDULING

### 6.1 Specification

- Allow scheduling appointments for patients.
- Multiple doctors, each with a daily schedule divided into **15-minute slots** from 8:00am to 6:00pm.
- Print separate daily schedules for each doctor (time + patient name).
- Output to **screen** (except schedules → file).
- For simplicity: each doctor has only **one appointment day**.

### 6.2 Finding Classes

From the specification, candidate classes:
- **Doctor** — has a daily schedule
- **Patient** — has a name, can schedule appointments
- **DailySchedule** — collection of time slots for one doctor
- **Appointment** — a specific booking (doctor + patient + time)
- **Scheduler** — interface to the user (orchestrates the process)

### 6.3 Scenarios (Use Cases)

1. Scheduler requests the patient's name.
2. Patient chooses a doctor.
3. Scheduler displays the doctor's schedule (available slots).
4. Patient requests a specific slot.
5. Scheduler adds the appointment to the doctor's schedule and to the patient's record.
6. Scheduler confirms the appointment.

### 6.4 Class Dependencies

```
Scheduler ────uses────> Patient
    │                      │
    │ uses                 │ uses
    ↓                      ↓
  Doctor ──contains──> DailySchedule ──contains──> Appointment
```

- **Composition (contains)**: Doctor HAS A DailySchedule. DailySchedule HAS Appointments.
- **Use/Link**: Scheduler uses Patient and Doctor. Patient uses Doctor.

### 6.5 Operations

**Doctor:**

| Operation | Description |
|-----------|-------------|
| `addToSchedule` | Add an appointment to the doctor's schedule |
| `showAppointment` | Display the schedule |

**Patient:**

| Operation | Description |
|-----------|-------------|
| `inputName` | Enter patient's name |
| `chooseDoctor` | Select a doctor |
| `chooseTimeSlot` | Pick an available time slot |
| `setAppointment` | Schedule an appointment |

**DailySchedule:**

| Operation | Description |
|-----------|-------------|
| `setAppointment` | Add an appointment to the schedule |
| `isTimeSlotFree` | Check if a particular slot is available |
| `showAppointments` | Display scheduled appointments |

**Appointment:**

| Operation     | Description                       |
| ------------- | --------------------------------- |
| Constructor   | Create an appointment             |
| `isScheduled` | Check if an appointment is booked |

**Scheduler:**

| Operation                | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `scheduleOneAppointment` | Orchestrate the booking process                  |
| `printAllAppointment`    | Print all scheduled appointments for all doctors |

### 6.6 Additional Helper Classes

- **TimeSlot** — handles translation and formatting of appointment times.
- **string** — for string data members (patient name, etc.).

---

## 7. THE DEVELOPMENT CYCLE (ITERATIVE PROCESS)

```
Create overall design
    → Find standard components → customize for this design
    → Create new standard components → customize for this design
    → Assemble design
    → (repeat)
```

**Design for change**: The system must remain as simple as possible under a sequence of changes. Aim for:
- **Flexibility** — easy to modify behavior.
- **Extensibility** — easy to add new features.
- **Portability** — easy to move to new platforms.

---

## 8. CLASS DIAGRAMS AND UML

### 8.1 What Is UML?

**Unified Modeling Language** — a visual language for specifying, constructing, and documenting software systems. It provides many diagram types so that **all stakeholders** (analysts, designers, coders, testers, QA, customers, technical authors) can benefit from at least one UML diagram.

### 8.2 UML Diagram Types

| Diagram | Purpose |
|---------|---------|
| **Use Case Diagram** | Description of system behavior from a user's viewpoint; aids requirements analysis |
| **Class Diagram** | Shows classes, their attributes, operations, and relationships; essential for OO design |
| **Collaboration Diagram** | Shows how objects collaborate (interact) to achieve a task |
| **Sequence Diagram** | Same as collaboration but shows **time ordering** (dotted lines = timeline) |

### 8.3 Representing Objects

An object is represented as a **rectangle with an underlined name**:
```
┌──────────────────┐       ┌──────────────────┐
│   Kenji: Professor│       │   : Professor    │
└──────────────────┘       └──────────────────┘
  Named Object               Unnamed Object
```

### 8.4 Representing Classes

A class is represented as a **rectangle with compartments**:
```
┌──────────────────┐
│   ClassName      │  ← Class name
├──────────────────┤
│   attribute1     │  ← Attributes (data members)
│   attribute2     │
├──────────────────┤
│   operation1()   │  ← Operations (member functions)
│   operation2()   │
└──────────────────┘
```

### 8.5 Relationship Notation (Class Diagrams)

| Notation | Meaning |
|----------|---------|
| ◇─────── | **Containment/Composition** — one class maintains instances of another (has-a) |
| ─────── | **Link/Association** — objects request services or send messages |
| △─────── | **Inheritance** — "is-a" relationship (triangle points to base class) |

### 8.6 Cardinality (Multiplicity)

Specifies how many instances participate in a relationship:

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `n` or `*` | Zero or more |
| `0..n` or `0..*` | Zero or more |
| `1..n` or `1..*` | One or more |
| `10..30` | Range: 10 to 30 |
| `2..4, 8` | Range or specific number |

Example: `Doctor 1 ────contains───> 1 DailySchedule` (each doctor has exactly one daily schedule, each daily schedule belongs to exactly one doctor).

---

## 9. PROTOTYPING, EXPERIMENTATION, AND ANALYSIS

- **Prototyping** is frequently used for experimenting with designs before committing.
- Different aspects of a system may be prototyped independently (e.g., the GUI, the data layer).
- **Analysis** of a design and/or implementation provides critical insight — review your design before and during implementation.

---

## 10. MAINTENANCE AND RE-USE

### 10.1 Software Maintenance

Maintenance usually means **redesign and re-implementation**. When **flexibility, extensibility, and portability** are emphasized in the design, maintenance problems are addressed more easily.

Object-Oriented paradigm promotes maintenance because:
- Product consists of **independent units** (classes).
- **Encapsulation** provides conceptual independence.
- **Information hiding** provides physical independence.
- **Message-passing** is the sole communication mechanism (controlled interfaces).

### 10.2 Software Re-use

Re-use of **code** and **design** are often reasons for choosing OOP.

Software is **reusable** if:
1. It **works** (correct, reliable).
2. It is **comprehensible** (well-documented, clean design).
3. It can **co-exist** with other software not written to co-exist with it (standard interfaces).
4. It is **supported** (maintained, updated).
5. It is **economical** (maintenance cost is lower than building from scratch).

Object-Orientation **supports** re-use but needs **tools and standards** (libraries, frameworks, design patterns, UML).

---

## 11. DESIGN PRINCIPLES SUMMARY

| Principle | Meaning |
|-----------|---------|
| **Divide and Conquer** | Break system into modules (objects/classes) |
| **Encapsulation** | Bundle data with operations; hide internal details |
| **Information Hiding** | Private data, public interfaces |
| **Loose Coupling** | Minimize dependencies between classes |
| **High Cohesion** | Each class has a single, well-defined responsibility |
| **Design for Change** | Anticipate future modifications |
| **Iterative Development** | Design → prototype → refine → repeat |

---

## 12. MUST-MEMORIZE FRAMEWORKS

### 12.1 The OO Design Steps (In Order)

```
1. Find CLASSES (nouns from problem description)
2. Specify OPERATIONS (verbs → constructors, selectors, modifiers, iterators, conversions)
3. Specify DEPENDENCIES (inheritance: is-a; use/composition: has-a)
4. Specify INTERFACES (public vs protected, exact types)
5. REORGANIZE hierarchy (introduce common bases, split classes)
```

### 12.2 Operations Classification

| Category | Description | Example |
|----------|-------------|---------|
| Foundation | Constructors, destructors, copy ops | `Doctor()`, `~Doctor()` |
| Selectors | Don't modify state (const) | `getSchedule() const` |
| Modifiers | Modify state | `addAppointment()` |
| Conversion | Produce object of another type | `toString()`, `toJson()` |
| Iterators | Traverse collections | `getNextAppointment()` |

### 12.3 Class Diagram Relationship Types

| Relationship | UML Notation | C++ Implementation |
|-------------|-------------|-------------------|
| Inheritance (is-a) | △─────── | `class D : public B` |
| Composition (has-a) | ◇─────── | Member object or pointer |
| Association (uses) | ─────── | Method parameter or pointer |

### 12.4 UML Class Representation

```
┌──────────────────────────┐
│       ClassName           │
├──────────────────────────┤
│  - privateAttr: type     │   ← minus = private
│  # protectedAttr: type   │   ← hash = protected
│  + publicAttr: type      │   ← plus = public
├──────────────────────────┤
│  + operation(): retType  │
│  - helper(): void        │
└──────────────────────────┘
```

### 12.5 Use Case Scenario Template

```
1. Actor/system does X
2. System responds with Y
3. Actor chooses Z
4. System updates W
...
```

---

## 13. EXAM TRAPS

### Trap 1: Confusing Analysis (What) with Design (How)
Analysis describes **what** the system should do (requirements). Design describes **how** it will do it (classes, operations, relationships). Keep them separate in your mind — even though in practice they overlap.

### Trap 2: Finding Too Many or Too Few Classes
Not every noun is a class (e.g., "date" might just be a string attribute). Not every class is a noun in the problem statement (helper classes like `TimeSlot` may be implicit). Use judgment.

### Trap 3: Putting Operations in the Wrong Class
Operations should live in the class that **owns the data** they manipulate. `addTape()` belongs to `PurchaseOrder`, not to `Supplier`, because the order owns the tape list.

### Trap 4: Forgetting Helper/Utility Classes
Classes like `string`, `TimeSlot`, `Date` are often needed but not mentioned as nouns. They emerge during the design refinement step.

### Trap 5: Over-Specifying Implementation in Design
During design, focus on **what** a class does (its interface), not **how** it does it (private implementation). Implementation details come later.

### Trap 6: UML Cardinality Confusion
- `1` is NOT the same as `0..1` — `0..1` means optional.
- `*` (or `n`) means zero or more, INCLUDING zero.
- If a doctor MUST have exactly one schedule: `1 ──── 1`, not `1 ──── 0..1`.

### Trap 7: Inheritance vs Composition
- "Is-a" → **Inheritance** (a `Car` IS A `Vehicle`).
- "Has-a" → **Composition** (a `Car` HAS an `Engine`).
- Wrong choice leads to inflexible designs. Prefer composition when in doubt.

### Trap 8: Design Is Iterative — First Attempt Is Rarely Final
The initial class organization may need reorganization (introduce common base, split classes). This is normal and expected.

### Trap 9: Forgetting Virtual Operations
Consider which operations should be virtual in the design phase. If derived classes might need different behavior, mark it virtual in the base.

### Trap 10: Interface Should Support the Same Level of Abstraction
Don't mix low-level and high-level operations in the same class interface. All public operations should operate at a consistent conceptual level.

---

## 14. HAND-CODING DRILLS

### Drill 1: Find Classes and Operations from a Problem Description

**Problem**: A library management system allows members to borrow and return books. Each book has a title, author, and ISBN. Each member has a name and membership ID. The system must track which books are currently borrowed and by whom. Members can have at most 5 books at a time. The librarian can add new books and register new members.

> Identify candidate classes, their key attributes, and at least two operations for each.

> [!success]- Show Answer
> **Classes:**
>
> **Book**
> - Attributes: title, author, ISBN, isBorrowed
> - Operations: `borrow()`, `returnBook()`, `isAvailable()`
>
> **Member**
> - Attributes: name, membershipID, booksBorrowed (collection)
> - Operations: `borrowBook(Book*)`, `returnBook(Book*)`, `canBorrow()` (check limit)
>
> **Library** (or LibrarySystem)
> - Attributes: books (collection), members (collection)
> - Operations: `addBook(Book*)`, `registerMember(Member*)`, `findBook(ISBN)`
>
> **Librarian** (actor — might be a class or just an interface user)
> - Operations: `addNewBook()`, `registerNewMember()`

### Drill 2: Class Diagram — Draw the Doctor's Office System

Draw a UML-style class diagram for the doctor's office scheduling system showing:
- All five main classes
- Key attributes and operations
- Relationships with cardinality

> [!success]- Show Answer
> ```
> ┌──────────────┐         ┌──────────────┐
> │   Scheduler  │────────>│   Patient    │
> ├──────────────┤  uses   ├──────────────┤
> │ +schedule()  │         │ -name        │
> │ +printAll()  │         │ +inputName() │
> └──────┬───────┘         │ +chooseDr()  │
>        │                 │ +chooseSlot()│
>        │ uses            └──────┬───────┘
>        ↓                       │ uses
> ┌──────────────┐ 1     1 ┌─────┴────────┐
> │   Doctor     │◇───────│DailySchedule │
> ├──────────────┤contains ├──────────────┤
> │ -name        │         │ +setAppt()   │
> │ +addToSched()│         │ +isSlotFree()│
> │ +showAppt()  │         │ +showAppts() │
> └──────────────┘         └──────┬───────┘
>                                 │ 1..n contains
>                          ┌──────┴───────┐
>                          │ Appointment  │
>                          ├──────────────┤
>                          │ -timeSlot    │
>                          │ -patientName │
>                          │ +isBooked()  │
>                          └──────────────┘
> ```

### Drill 3: Reorganize a Class Hierarchy

Two classes share significant behavior:
```cpp
class Car {
    string make, model;
    int year;
    void drive();
    void park();
    double fuelCapacity;
    void refuel();
};

class Motorcycle {
    string make, model;
    int year;
    void drive();
    void park();
    int engineCC;
    void wheelie();
};
```

> Reorganize: introduce a common base class. What does it contain? What stays in the derived classes?

> [!success]- Show Answer
> ```cpp
> class Vehicle {              // NEW common base
> protected:
>     string make, model;
>     int year;
> public:
>     virtual void drive() = 0;   // pure virtual — different implementations possible
>     virtual void park() = 0;
>     // Getters for make, model, year
> };
>
> class Car : public Vehicle {
>     double fuelCapacity;
> public:
>     void drive() override { /* car-specific */ }
>     void park() override { /* car-specific */ }
>     void refuel() { /* car-specific */ }
> };
>
> class Motorcycle : public Vehicle {
>     int engineCC;
> public:
>     void drive() override { /* motorcycle-specific */ }
>     void park() override { /* motorcycle-specific */ }
>     void wheelie() { /* motorcycle-specific */ }
> };
> ```
> Shared attributes (`make`, `model`, `year`) and operation signatures (`drive`, `park`) move to `Vehicle`. Type-specific members stay in the derived classes.

### Drill 4: Identify Operations by Category

Given a `BankAccount` class with the following candidate operations, classify each as Foundation, Selector, Modifier, or Iterator:

```
BankAccount(id, balance)  // constructor
getBalance()              // returns balance
deposit(amount)           // adds to balance
withdraw(amount)          // subtracts from balance
getStatement(dates)       // returns transactions in date range
applyInterest()           // calculates and adds interest
```

> [!success]- Show Answer
> | Operation | Category |
> |-----------|----------|
> | `BankAccount(id, balance)` | **Foundation** (constructor) |
> | `getBalance()` | **Selector** (doesn't modify state) |
> | `deposit(amount)` | **Modifier** (changes balance) |
> | `withdraw(amount)` | **Modifier** (changes balance) |
> | `getStatement(dates)` | **Iterator** (traverses transaction collection) |
> | `applyInterest()` | **Modifier** (changes balance) |

### Drill 5: Write a Use Case Scenario

Write a step-by-step use case scenario for a student registering for a course in a university registration system.

> [!success]- Show Answer
> 1. Student enters their student ID.
> 2. System validates the ID and displays the student's name.
> 3. System displays available courses (not full, no time conflicts).
> 4. Student selects a course.
> 5. System checks prerequisites — if not met, displays error.
> 6. System checks capacity — if full, displays error with waitlist option.
> 7. System adds the student to the course roster.
> 8. System updates the student's schedule.
> 9. System confirms registration and displays updated schedule.

---

> [!NOTE]
> This study guide covers all lecture content for Lec13: Object-Oriented Design. Master the five OO design steps, the noun/verb technique for finding classes/operations, UML class diagram notation (including cardinality), and the worked examples (video store, doctor's office). Focus on the design process — identifying classes, operations, dependencies, and interfaces — not on implementation details.
