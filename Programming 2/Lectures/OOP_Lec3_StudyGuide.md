# Lec3: Introduction to OOP — Study Guide

---

## 1. CONCEPT CARD: Object-Oriented Programming (OOP)

**What it is:** OOP is a way of writing programs by organizing code into "objects" — self-contained units that hold both data and the functions that work on that data.

**What problem it solves:** Before OOP, programs used structured programming where global data floated around and any function could touch any data. When requirements changed (which they always do), you had to rewrite large chunks of code because data and functions were scattered everywhere. OOP fixes this by bundling data with the operations that belong to it, so changing one part of the system doesn't break everything else.

**How it works:**
1. You identify the real-world things your program deals with (a bank account, a sensor reading, a network packet).
2. For each thing, you create a **class** — a blueprint that declares what data it stores and what operations it supports.
3. You create **objects** from the class — actual instances with their own copy of the data.
4. Objects communicate by sending **messages** (calling each other's public functions).
5. You hide internal data behind **private** access so outsiders can't corrupt it.

**Concrete example:** A GPS navigation app. You have a `Waypoint` class holding latitude/longitude. You have a `Route` class containing a list of Waypoints. You have a `Navigator` class that computes the next turn. If the GPS chip vendor changes, you only rewrite the `GPSChip` class — the `Route` and `Navigator` classes are untouched because they never directly touched the chip's raw data. That's encapsulation saving you.

**What it is NOT:** OOP is NOT "putting all your code inside classes." A class with only static methods and no meaningful state is just a namespace — that's procedural programming wearing OOP syntax. OOP requires objects that hold state AND behavior together.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

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

---

## 3. EXAM TRAPS

- **Missing semicolon after the closing brace of a class.** `class Foo { };` — that semicolon is required. Forget it and you get cascading errors.
- **Confusing class (blueprint) with object (instance).** `Student` is the class; `Student alice;` creates an object. You cannot call methods on the class name itself.
- **Thinking "private means absolutely nobody can see it."** Two objects of the *same class* CAN access each other's private members — access control is per-class, not per-object. A `Date` copy constructor can read `d.month` directly.
- **Default access in a class is `private`.** If you don't write `public:`, everything is locked down. Structs default to `public`.
- **Confusing abstraction with encapsulation.** Abstraction = hiding complexity behind a simple interface (you drive a car without knowing engine internals). Encapsulation = bundling data + functions together and restricting access (the engine is sealed, you can't randomly tweak the spark plugs from the steering wheel).
- **Thinking "everything must be an object."** C++ has free functions, primitives (`int`, `double`), and doesn't force pure OOP like Java or C#.

---

## 4. HAND-CODING DRILLS

### Drill 1: Identify the Four Pillars

You are given this description of a payroll system. For each numbered item, name which OOP principle it demonstrates (Abstraction / Encapsulation / Inheritance / Polymorphism):

1. All employee types (hourly, salaried, contractor) share a common `calculatePay()` signature, but each computes pay differently.
2. A `FullTimeEmployee` automatically gets all fields and methods from `Employee` without re-declaring them.
3. The `TaxCalculator` class exposes only `computeTax(Employee e)` — callers never see the bracket tables or deduction rules inside.
4. The `Employee` class keeps its `salary` field private with `getSalary()` and `setSalary()` as the only access points.

> [!success]- Show Answer
> 1. Polymorphism — same function name, different behaviors per derived class.
> 2. Inheritance — derived class reuses base class members.
> 3. Abstraction — complex internals hidden behind a simple function signature.
> 4. Encapsulation — data bundled with controlled access functions.

### Drill 2: Spot the Broken OOP

```cpp
class BankAccount {
    int balance;
public:
    void deposit(int amount) { balance += amount; }
};

int main() {
    BankAccount acc;
    acc.balance = 5000;        // line A
    acc.deposit(100);          // line B
    cout << acc.balance;       // line C
}
```

Which lines will fail to compile, and why? Fix the class so only `deposit` can change the balance and a new `getBalance()` function allows reading it.

> [!success]- Show Answer
> Lines A and C fail because `balance` is private (the default in a class). Outsiders cannot read or write private members directly.
>
> Fixed version:
> ```cpp
> class BankAccount {
>     int balance;
> public:
>     BankAccount() : balance(0) {}
>     void deposit(int amount) { balance += amount; }
>     int getBalance() const { return balance; }
> };
> ```

### Drill 3: Bottom-Up vs Top-Down Design

You are designing software for a smart home system. The requirements are unclear — the client keeps adding new device types (lights, thermostats, cameras, locks). Which design approach (top-down or bottom-up) does the lecture recommend, and why? Then write the skeleton of a `SmartDevice` class that captures the *common interface* all devices must support, using only lecture knowledge (no `virtual` yet — just show what the class should conceptually contain).

> [!success]- Show Answer
> Bottom-up approach. When requirements keep changing and features accumulate, you build small, independent modules (one per device type) and compose them upward. Top-down requires you to know the full picture upfront, which fails when the client changes their mind.
>
> ```cpp
> class SmartDevice {
> private:
>     bool poweredOn;
>     int deviceId;
> public:
>     SmartDevice(int id) : poweredOn(false), deviceId(id) {}
>     void turnOn()  { poweredOn = true; }
>     void turnOff() { poweredOn = false; }
>     bool isOn()    { return poweredOn; }
>     int getId()    { return deviceId; }
> };
> ```
