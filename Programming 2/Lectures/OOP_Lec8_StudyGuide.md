# Lec8: Inheritance in C++ — Study Guide

---

## 1. CONCEPT CARD: C++ Inheritance Mechanics

**What it is:** The concrete C++ syntax and rules for deriving classes — access specifiers on inheritance (`public`, `protected`, `private`), constructor chaining, order of construction/destruction, and solving the diamond problem with virtual base classes.

**What problem it solves:** Knowing that inheritance means "is-a" (Lec7) isn't enough. You need to know exactly how access levels transform during inheritance, in what order constructors fire, how to pass parameters up the chain, and why inheriting from two classes that share a grandparent creates duplicate base subobjects. This lecture is the wiring diagram.

**How it works:**
1. Derive with `class Derived : public Base { };`. The access specifier (`public`/`protected`/`private`) controls how base members get re-labeled in the derived class.
2. **public inheritance:** public→public, protected→protected. This is the standard "is-a" relationship.
3. **protected inheritance:** public→protected, protected→protected. All base members become protected in derived.
4. **private inheritance:** public→private, protected→private. This implements "is-implemented-in-terms-of."
5. Constructor order: base first (top to bottom in hierarchy), then members in declaration order, then the derived class body.
6. Destructor order: exactly reverse.
7. A base pointer can point to a derived object (`Base* p = new Derived;`). Reverse requires explicit cast.
8. Virtual base classes solve the diamond problem: when two intermediate classes both inherit from the same grandparent, `virtual` inheritance ensures only ONE copy of the grandparent exists.

**Concrete example:** A university HR system. `Person` has `name` and `age`. `Student` inherits from `Person` and adds `GPA`. `Employee` inherits from `Person` and adds `salary`. `GraduateAssistant` inherits from BOTH `Student` and `Employee`. Without virtual inheritance, `GraduateAssistant` gets TWO copies of `Person` — two names, two ages — and calling `getAge()` is ambiguous. With `virtual` on both intermediate classes, there's only ONE `Person` subobject, shared by all paths.

**What it is NOT:** Inheritance access specifiers (`public`, `protected`, `private`) are NOT the same as member access specifiers. `class A : private B` does NOT mean B's members become private to outsiders of A; it means B's public and protected members become private within A itself.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
// Base class
class Base {
protected:
    int baseData;                     // For derived classes only
public:
    Base(int val);                    // Constructor
    virtual ~Base();                  // Virtual destructor (Lec9)
    int getBaseData() const;
};

// Public inheritance — standard "is-a"
class Derived : public Base {         // Access specifier matters!
private:
    int derivedData;
public:
    Derived(int baseVal, int derivedVal); // Must initialize Base
    int getDerivedData() const;
};

// Constructor initializer chains upward:
Derived::Derived(int baseVal, int derivedVal)
    : Base(baseVal)                   // Pass param to Base ctor
{
    derivedData = derivedVal;         // Then initialize own members
}

// Virtual base class (diamond solution):
class Student : virtual public Person { };  // virtual keyword
class Employee : virtual public Person { };
class GradAssistant : public Student, public Employee { };
// Now Person exists only once in GradAssistant.
```

---

## 3. EXAM TRAPS

- **Base class constructor is ALWAYS called first.** Even if you don't write it explicitly, the compiler inserts a call to the default base constructor. If Base has NO default constructor, you MUST use the constructor initializer list: `Derived(int x) : Base(x) { }`.
- **Destructor order is the exact reverse of constructor order.** Derived destructor body runs first, then member destructors, then base destructor. Easy to get backwards.
- **`private` inheritance does NOT mean the base class is hidden from you.** It means all inherited members become private in the derived class. Further derived classes cannot access them.
- **A `Base*` can point to a `Derived` object, but you can only call base-class methods through it.** `Base* p = new Derived; p->baseMethod();` is fine. `p->derivedOnlyMethod();` is a compile error.
- **Implicit downcast (base→derived pointer) is illegal.** `Derived* d = basePtr;` won't compile. You need `Derived* d = (Derived*)basePtr;` — but this is dangerous. Never do it unless you're 100% sure.
- **Diamond problem without `virtual`:** If `GradAssistant` inherits from both `Student` (derived from `Person`) and `Employee` (derived from `Person`), calling `getAge()` is ambiguous because there are TWO `Person` subobjects. Adding `virtual` to both intermediate classes collapses them into one.
- **`protected` access in base class = accessible inside derived class body, but NOT from outside through a derived object.** Outside users cannot touch protected members.
- **Scope resolution `::` resolves hidden members, but the hidden member is still there.** `Derived::Base::hiddenMethod()` still works.

---

## 4. HAND-CODING DRILLS

### Drill 1: Access Specifier Effects

```cpp
class Base {
private:   int a;
protected: int b;
public:    int c;
};
class Derived : private Base {
public:
    void test() {
        a = 1;  // line 1
        b = 2;  // line 2
        c = 3;  // line 3
    }
};
class FurtherDerived : public Derived {
public:
    void test2() {
        b = 4;  // line 4
        c = 5;  // line 5
    }
};
int main() {
    Derived d;
    d.c = 6;    // line 6
}
```
Which lines compile, which fail, and why?

> [!success]- Show Answer
> - Line 1: FAIL. `a` is private in Base. Derived never has access.
> - Line 2: COMPILES. `b` is protected in Base, becomes private in Derived via `private` inheritance. Accessible WITHIN Derived.
> - Line 3: COMPILES. `c` is public in Base, becomes private in Derived via `private` inheritance. Accessible WITHIN Derived.
> - Line 4: FAIL. Both `b` and `c` became private in Derived (via private inheritance). FurtherDerived cannot access private members of its base.
> - Line 5: FAIL. Same reason as line 4 — `c` is private in Derived.
> - Line 6： FAIL. Outside Derived's class scope, `c` is private. Cannot be accessed via dot operator.

### Drill 2: Constructor Chain with No Default

```cpp
class Engine {
    int horsepower;
public:
    Engine(int hp) : horsepower(hp) { }  // NO default constructor
};
class Car : public Engine {
    int numDoors;
public:
    Car(int hp, int doors);
};
```
Implement `Car`'s constructor. Explain what happens if you write it as `Car(int hp, int doors) { horsepower = hp; numDoors = doors; }`.

> [!success]- Show Answer
> Correct:
> ```cpp
> Car(int hp, int doors) : Engine(hp) {
>     numDoors = doors;
> }
> ```
>
> What happens with the wrong version: The compiler tries to call `Engine()` (default constructor) BEFORE entering the Car constructor body. But `Engine` has NO default constructor (you wrote `Engine(int hp)` which suppresses auto-generation). Compilation fails with "no default constructor for Engine." The initializer list `: Engine(hp)` is the ONLY way to pass arguments to a base constructor.

### Drill 3: Virtual Base — Diamond

```cpp
class Device {
protected:
    int serialNumber;
public:
    Device(int s) : serialNumber(s) {}
    int getSerial() const { return serialNumber; }
};
class Scanner : /* ??? */ public Device {
public:
    Scanner(int s) : Device(s) {}
};
class Printer : /* ??? */ public Device {
public:
    Printer(int s) : Device(s) {}
};
class AllInOne : public Scanner, public Printer {
public:
    AllInOne(int s);
};
```
Fill in the `/* ??? */` and implement `AllInOne`'s constructor so that `AllInOne aio(12345); aio.getSerial();` compiles without ambiguity.

> [!success]- Show Answer
> ```cpp
> class Scanner : virtual public Device {  // virtual!
> public:
>     Scanner(int s) : Device(s) {}
> };
> class Printer : virtual public Device {   // virtual!
> public:
>     Printer(int s) : Device(s) {}
> };
> class AllInOne : public Scanner, public Printer {
> public:
>     AllInOne(int s) : Device(s), Scanner(s), Printer(s) { }
>     // Device(s) MUST be called directly by the most-derived class
>     // when virtual base classes are involved
> };
> ```
> With virtual inheritance, `Device` exists only once in `AllInOne`. `getSerial()` is no longer ambiguous. The rule: the most-derived class must explicitly initialize the virtual base — `Scanner(s)` and `Printer(s)` will NOT initialize Device when constructing an `AllInOne`.
