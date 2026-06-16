# Lec13: Object-Oriented Design — Study Guide

---

## 1. CONCEPT CARD: OO Design Methodology

**What it is:** OO Design (OOD) is the process of translating real-world requirements into a blueprint of classes, their data, their operations, and their relationships — before writing a single line of implementation code.

**What problem it solves:** Jumping straight to coding without design leads to tangled, unmaintainable systems. Classes get the wrong responsibilities, dependencies form circular messes, and adding a feature later means rewriting everything. OOD forces you to think about WHAT classes exist, WHAT they do, and HOW they relate BEFORE HOW they're implemented. This produces software that survives requirement changes, new team members, and years of maintenance.

**How it works (step by step):**
1. **Find the classes:** Read the problem description. Underline NOUNS — these are candidate classes. Physical things (Doctor, Patient), conceptual things (Appointment, Schedule), and system interfaces (Scheduler).
2. **Find the relationships:** Determine how classes connect. Inheritance ("is-a"), Composition ("has-a" / contains), Link ("uses" / sends messages to).
3. **Specify operations:** For each class, identify what it must DO. Verbs in the description become methods. Classify them as: constructors/destructors (foundation), selectors (read state, don't modify), modifiers (change state), conversion operators (produce a different type), iterators (traverse collections).
4. **Specify dependencies:** Decide inheritance chains and which classes use which others. Avoid overuse — too many dependencies make the system rigid.
5. **Specify interfaces:** Separate public from protected. Public = what outsiders can call. Protected = what derived classes can use. Private = internal implementation (decided later, in coding).
6. **Refine and reorganize:** Look for shared behavior → extract a common base class. Look for classes doing too much → split into two. Iterate until the design feels minimal, complete, and convenient.

**Concrete example:** The lecture's doctor's office scheduling system:
- Nouns → Classes: Doctor, Patient, DailySchedule, Appointment, TimeSlot, Scheduler.
- Doctor "has a" DailySchedule (composition). Scheduler "uses" Doctor, Patient (link).
- Doctor operations: `addToSchedule()`, `showAppointments()`.
- Patient operations: `inputName()`, `chooseDoctor()`, `chooseTimeSlot()`.
- DailySchedule operations: `setAppointment()`, `isTimeSlotFree()`, `showAppointments()`.
- After analysis, a new class `TimeSlot` emerged to handle time formatting — refining the design.

**What it is NOT:** OOD is NOT the same as UML. UML is a drawing LANGUAGE for expressing designs. OOD is the THINKING PROCESS that produces the design. You can do OOD on a whiteboard with no UML at all — but UML helps communicate it.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

This lecture is about design, not C++ syntax. The key template is the design process itself:

```
1. READ the problem description
2. UNDERLINE nouns      → Candidate CLASSES
3. UNDERLINE verbs      → Candidate OPERATIONS (methods)
4. IDENTIFY relationships:
   - "is a"             → Inheritance (base/derived)
   - "has a" / "contains" → Composition (member objects)
   - "uses" / "sends"   → Link (method parameter/return)
5. CLASSIFY operations:
   - Foundation: constructors, destructor, copy
   - Selectors: getX(), isY(), findZ()
   - Modifiers: setX(), addY(), removeZ()
6. SEPARATE interface:
   - public: what other classes call
   - protected: what derived classes can access
7. ITERATE:
   - Extract common base classes
   - Split over-bloated classes
   - Check: minimal, complete, convenient
```

UML Class Diagram (minimal):
```
+---------------+          +---------------+
|   ClassName   |          |   Container   |
+---------------+<>--------+---------------+
| - privateData |          |               |
| # protectedData|         +---------------+
+---------------+
| + publicMethod()|
+---------------+
    ^
    | (inheritance: empty triangle arrowhead)
    |
+---------------+
|   Derived     |
+---------------+
```

---

## 3. EXAM TRAPS

- **Nouns map to classes, NOT every noun in the description is a class.** "The store manager creates a purchase order" → Manager might just be an attribute of Store, not a separate class. Use judgment: does this thing need to store unique state and have behavior?
- **Verbs map to methods, but must be assigned to the RIGHT class.** "The clerk locates the original purchase order" → `locate()` belongs to a PurchaseOrderList (or Clerk), not to PurchaseOrder itself. The object that performs the action or owns the collection should have the method.
- **Don't confuse UML relationships.** Inheritance = solid line with hollow triangle. Composition/aggregation = line with diamond. Link/association = plain line. Wrong arrowheads on an exam diagram signal you don't understand the relationships.
- **Class diagram cardinality matters.** `1` (exactly one), `0..n` (zero or more), `1..n` (one or more), `10..30` (range). These describe how many instances participate in a relationship — getting them wrong changes the system's rules.
- **Design for CHANGE.** The lecture emphasizes flexibility, extensibility, and portability. If your design requires modifying 10 files to add a new doctor schedule view, it's rigid. If adding a new appointment type only requires one new class, it's flexible.
- **Don't mix interface specification with implementation.** During OOD, you decide WHAT methods a class exposes (public/protected). You do NOT write the method bodies — that's coding, not design.
- **The most common reorganization is extracting a common base class.** If two classes share 70% of their interface, create an abstract base class holding the shared parts.
- **The second most common is splitting a class.** If one class has responsibilities for two distinct concepts, split it.

---

## 4. HAND-CODING DRILLS

### Drill 1: Find Classes from a Narrative

Read this description and list the candidate classes. Then identify which should be dropped or merged.

> "A library allows members to borrow books. Each book has a title, author, and ISBN. Members have a name and membership number. When a member borrows a book, the system records the due date (14 days from today). The librarian can view all overdue books and send reminder emails to the members who have them."

> [!success]- Show Answer
> Candidate classes: Library, Member, Book, System, Librarian, Email
>
> Analysis:
> - **Library** — probably just the system name, not a class. The system IS the library software.
> - **Member** — KEEP. Has name, membership number. Operations: borrow.
> - **Book** — KEEP. Has title, author, ISBN. Operations: (passive, mostly data).
> - **System** — KEEP (or rename to LoanManager). Records due dates, finds overdue books.
> - **Librarian** — DROP. Just a user role, not a class with unique state. The "view" and "send" actions belong to the system.
> - **Email** — DROP (or KEEP as simple data). An email is just a message string; doesn't need its own class unless it has complex formatting/queueing behavior.
>
> Also consider: **Loan** — not explicitly named, but "borrows a book" implies a relationship between Member and Book with a due date. This is a candidate class.

### Drill 2: Class Diagram from Operations

Given these already-identified classes for a food delivery app, assign each operation to the correct class. Then draw the relationships (inheritance, composition, link).

```
CLASSES: Customer, Restaurant, Order, MenuItem, DeliveryDriver

OPERATIONS:
  placeOrder(Restaurant, list of MenuItems)
  addToOrder(MenuItem)
  calculateTotal()
  acceptOrder(Order)
  updateLocation()
  markDelivered(Order)
  getEstimatedTime()
```

> [!success]- Show Answer
> ```
> Customer:
>   - placeOrder(restaurant, items) → creates an Order
>
> Restaurant:
>   - acceptOrder(order)   → confirms it can fulfill
>
> Order:
>   - addToOrder(item)      → builds the list
>   - calculateTotal()      → sums prices
>   - getEstimatedTime()    → based on restaurant prep + driver distance
>
> DeliveryDriver:
>   - updateLocation()      → GPS position
>   - markDelivered(order)  → completes the delivery
>
> MenuItem: data only (name, price, description) — no operations listed.
>
> Relationships:
>   Customer --uses--> Order (link: customer places order)
>   Order <>--contains-- MenuItem (composition: order has menu items)
>   Restaurant --accepts--> Order (link)
>   DeliveryDriver --delivers--> Order (link)
> ```

### Drill 3: Full Mini-Design

Design the classes for a **parking garage payment system** from this specification:

> "Drivers enter the garage and take a ticket with an entry time. When leaving, they insert the ticket at a pay station. The pay station calculates the fee: $3 per hour, rounded up. The driver pays by card or cash. After payment, the ticket is validated. At the exit gate, the driver inserts the validated ticket and the gate opens. The garage manager can view daily revenue and occupancy."

Produce: (a) List of classes with key attributes, (b) Key operations per class, (c) Relationships and cardinalities.

> [!success]- Show Answer
> **(a) Classes and Attributes:**
> - **Ticket**: ticketId, entryTime, exitTime, fee, isPaid
> - **PayStation**: stationId, location
> - **Payment**: amount, method (card/cash), timestamp
> - **Gate**: gateId, isOpen
> - **Garage**: totalSpots, occupiedSpots, dailyRevenue
>
> **(b) Operations:**
> - **Ticket**: `setExitTime(time)`, `calculateFee()` → returns $3 * ceil(hours), `validate()` → sets isPaid = true
> - **PayStation**: `processPayment(ticket, method)` → creates Payment, calls ticket.validate()
> - **Payment**: constructor (amount, method, time)
> - **Gate**: `open(ticket)` → if ticket.isPaid, opens; increments Garage count
> - **Garage**: `enter()` → increments occupiedSpots, creates Ticket; `exit(ticket)` → verifies paid, decrements; `getDailyRevenue()`; `getOccupancy()`
>
> **(c) Relationships:**
> - Garage **contains** (1..n) Gates → composition
> - Garage **contains** (1..n) PayStations → composition
> - Garage **creates** (0..n) Tickets → factory relationship
> - PayStation **creates** Payment → one per transaction
> - Ticket is used by Gate and PayStation
> - Gate and PayStation don't inherit from anything common in this design (they share no meaningful data)
>
> Cardinality: Garage has 1..n Gates (at least one entrance and one exit). Garage has 1 totalSpots limit. A Ticket belongs to exactly one Garage.
