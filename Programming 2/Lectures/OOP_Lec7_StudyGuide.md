# Lec7: Inheritance (Conceptual) — Study Guide

---

## 1. CONCEPT CARD: Inheritance

**What it is:** Inheritance is a mechanism where a new class (subclass) automatically acquires all the data and behavior of an existing class (superclass), and can then add or modify what it needs.

**What problem it solves:** Without inheritance, if you have `Student` and `Professor` classes that share 80% of their code (name, ID, address, email), you'd duplicate that code in both places. When a bug is found in the shared logic, you must fix it in both files. When you forget one, they diverge. Inheritance lets you write the shared part ONCE in a base class, then both derived classes extend it. One fix propagates everywhere.

**How it works:**
1. Identify the common data and behavior among related concepts and put them in a **base class** (superclass).
2. Create **derived classes** (subclasses) that inherit from the base.
3. The derived class automatically has all public and protected members of the base.
4. The derived class can add NEW members that only it needs.
5. The derived class can **override** base class methods to customize behavior.
6. A derived object CAN be used anywhere a base object is expected (an `Administrator` IS a `Person`).

**Concrete example:** A payroll system. `Employee` is the base class with `id`, `name`, `department`, and `calculatePay()`. `HourlyEmployee` inherits from it and adds `hourlyRate` and `hoursWorked`; its `calculatePay()` multiplies them. `SalariedEmployee` adds `annualSalary`; its `calculatePay()` divides by 12. The accounting system calls `calculatePay()` on a list of `Employee*` pointers — it doesn't need to know the specific type, inheritance guarantees the function exists.

**What it is NOT:** Inheritance is NOT "code copying." The subclass doesn't get a duplicate paste of the base class code — it genuinely SHARES the base class definition. Changes to the base class affect all subclasses (unlike copy-paste where each copy is frozen).

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
// Base class (superclass)
class BaseClassName {                    // Defines common interface
protected:                               // Accessible by derived classes
    int sharedData;                      // but NOT by outsiders
public:
    BaseClassName(int d);                // Constructor
    void commonMethod();                 // Inherited as-is
};

// Derived class (subclass)
class DerivedClassName : public BaseClassName {  // "is-a" relationship
private:
    int extraData;                       // Additional state
public:
    DerivedClassName(int baseData, int extraData); // Must init base
    void commonMethod();                 // OVERRIDES base version
    void extraMethod();                  // New behavior
};
```

---

## 3. EXAM TRAPS

- **Access is per-class (review from Lec6).** Two objects of the same class can access each other's private members. This is why a copy constructor `Date(Date& d)` can read `d.month` directly.
- **Derived class does NOT inherit constructors, destructors, or assignment operators.** These must be defined (or compiler-generated) for the derived class. The derived constructor must CALL the base constructor.
- **Naming conflicts resolved by overriding.** If both base and derived define `void display()`, the derived version wins. Access the hidden base version with `BaseClassName::display()`.
- **Private base members are inaccessible in the derived class.** Not just hidden — genuinely unreachable. Use `protected` if derived classes need access.
- **"Is-a" vs "Has-a".** Inheritance models "is-a" (a `Car` IS a `Vehicle`). Composition models "has-a" (a `Car` HAS a `Wheel`). Don't inherit when composition makes more sense.
- **Multiple inheritance naming conflicts.** When two base classes each have a member `int x`, the derived class must resolve ambiguity: `Base1::x` or `Base2::x`.
- **Abstract class ≠ class with protected constructor.** An abstract class is a design concept — "a class without instances, used only as a base." This lecture covers it conceptually; C++ implements it with pure virtual functions (covered in Lec9).
- **Default inheritance = whole inheritance (conceptually).** In C++, a derived class inherits everything. Partial inheritance (inheriting only some members) is a theoretical concept, not standard C++.

---

## 4. HAND-CODING DRILLS

### Drill 1: Inheritance Hierarchy Identification

Given this scenario: "A ride-sharing app has `Driver` (with license plate, rating) and `Rider` (with payment method, home address). Both have a name, phone number, and profile photo." Identify the base class and derived classes. What goes in each?

> [!success]- Show Answer
> Base class: `User` — contains `name`, `phoneNumber`, `photo`.
> Derived class: `Driver` — inherits all of `User`, adds `licensePlate`, `rating`.
> Derived class: `Rider` — inherits all of `User`, adds `paymentMethod`, `homeAddress`.

### Drill 2: Resolving a Naming Conflict

```cpp
class Logger {
public:
    void log(const char* msg) { cout << "[LOG] " << msg; }
};
class TimestampLogger : public Logger {
public:
    void log(const char* msg) {
        // (a) Print current time, then delegate to base's log
        // (b) Print message TWICE using only base's log
    }
};
```
Implement the `log` function body for (a) and (b), using scope resolution to access the base version.

> [!success]- Show Answer
> ```cpp
> void log(const char* msg) {
>     // (a) Custom prepend + delegate
>     cout << "[14:30:00] ";
>     Logger::log(msg);    // explicit call to base version
>
>     // (b) Print message twice via base
>     // Logger::log(msg);
>     // Logger::log(msg);
> }
> ```
> Without `Logger::`, `log(msg)` would recursively call the derived `log` — infinite recursion.

### Drill 3: Multiple Inheritance Ambiguity

```cpp
class Bluetooth {
public:
    int version;
    void connect() { cout << "BT connect v" << version; }
};
class WiFi {
public:
    float version;   // note: float
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
>     Bluetooth::connect();          // (3) explicit scope
>     WiFi::connect();               // (4) explicit scope
> }
> ```
> Without `Bluetooth::` and `WiFi::`, both `version` and `connect()` are ambiguous. The compiler can't guess which one you mean. Conflict resolution by user (option 2 from the lecture) requires explicit scoping.
