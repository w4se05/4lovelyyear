# Lec9: Polymorphism — Study Guide

---

## 1. CONCEPT CARD: Polymorphism (Inclusion / Overriding)

**What it is:** Polymorphism is the ability to call the same function name on different types of objects and have each object respond with its own version of that function — the correct version is chosen at runtime based on the actual object type, not the pointer type.

**What problem it solves:** Without polymorphism, if you have a collection of different shapes (circles, rectangles, triangles), you must check the type of each one before drawing it: `if (type == CIRCLE) drawCircle(); else if (type == RECTANGLE) drawRectangle();` etc. Adding a new shape means modifying EVERY such if-else chain in your codebase. With polymorphism, you just call `shape->draw()` and the object knows how to draw itself. Adding a new shape class requires ZERO changes to existing code.

**How it works:**
1. Declare a function as `virtual` in the base class.
2. Override it in each derived class (same signature).
3. Create objects via base-class pointers: `Base* p = new Derived();`
4. Call `p->virtualFunction()` — the compiler generates code to look up the correct function in the object's **vtable** (virtual table) at runtime.
5. Each class with virtual functions gets a hidden vtable — an array of function pointers.
6. Each object of such a class gets a hidden `vptr` pointing to its class's vtable.
7. Non-virtual functions use static binding (resolved at compile time, faster).
8. Virtual functions use dynamic binding (resolved at runtime via vtable lookup, slightly slower).

**Concrete example:** A payment processing system. `PaymentMethod` has a virtual `processPayment(double amount)` function. `CreditCard`, `PayPal`, and `BankTransfer` each override it with their own logic (contacting different APIs). The checkout system holds a `PaymentMethod*` chosen by the user. It calls `method->processPayment(total)` without knowing or caring which specific type it is. Adding `CryptoCurrency` later means creating one new class — the checkout code never changes.

**What it is NOT:** Polymorphism (overriding) is NOT overloading. Overloading = same function name, DIFFERENT parameter types, resolved at compile time. Overriding = same function name AND same parameter types, different implementation in derived class, resolved at RUNTIME via virtual functions.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
class Base {
public:
    virtual void action();            // Can be overridden; dynamic binding
    virtual void mustImplement() = 0; // PURE virtual — makes Base abstract
    virtual ~Base();                  // ALWAYS virtual if class is a base
    void nonVirtualFunc();            // Static binding; cannot be overridden
};

class Derived : public Base {
public:
    void action();           // Overrides Base::action (virtual is optional here)
    void mustImplement();    // MUST implement all pure virtuals to be concrete
};

// Usage:
Base* ptr = new Derived();          // Base pointer to Derived object
ptr->action();                      // Calls Derived::action (dynamic binding)
ptr->nonVirtualFunc();              // Calls Base::nonVirtualFunc (static binding!)
// Base b;                          // ERROR: Base is abstract (has pure virtual)
```

---

## 3. EXAM TRAPS

- **Non-virtual methods use STATIC binding.** If `Base* p = new Derived;` and `p->nonVirtualFunc()` calls a non-virtual function, it calls `Base`'s version, NOT `Derived`'s — even if Derived has a function with the same name. The pointer type (Base) determines which function is called.
- **Forgetting `virtual` on the base class destructor.** `Base* p = new Derived; delete p;` — if `~Base()` is not virtual, only `Base`'s destructor runs. Derived's destructor never fires → resource leaks, dangling members. Always `virtual ~Base() { }`.
- **Pure virtual function declared but not implemented in derived class.** The derived class remains abstract and cannot be instantiated. Compiler error if you try `new Derived`.
- **Abstract classes CAN have pointers and references.** `Base* p;` is fine. `p = new Derived;` is fine. You just can't do `new Base` or `Base b;` if Base has any pure virtual.
- **Calling a virtual function in a constructor/destructor does NOT dispatch dynamically.** Inside `Base::Base()`, calling `virtualFunc()` calls `Base`'s version even if the object being constructed is a `Derived` — the Derived part hasn't been built yet.
- **Virtual function overrides must match the EXACT signature.** Different return type, const-ness, or parameter type = you created a new function (overloading), not overriding the base virtual. Use `override` keyword in C++11+ to catch this (but for handwritten exams, triple-check your signatures).
- **"this" is an implicit pointer to the CURRENT object** — inside a member function, `*this` is the object that received the call. In a virtual function call through a base pointer, `this` points to the actual derived object.
- **Coercion is NOT the same as overriding.** `int add(int a, int b)` and `float add(float a, float b)` with a call `add(1, 1.0)` — the compiler converts (coerces) the `1.0` double to an int to match the signature. This is compile-time magic, not runtime polymorphism.

---

## 4. HAND-CODING DRILLS

### Drill 1: Static vs Dynamic Binding

```cpp
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
> - Line A: `hello()` is NON-virtual. Static binding uses pointer type `Parent*` → calls `Parent::hello`.
> - Line B: `bye()` is virtual. Dynamic binding follows vptr to `Child`'s vtable → calls `Child::bye`.
> - Line C: `c` is a `Child` object. `hello()` resolves to `Child::hello` (hides parent version).
> - Line D: `bye()` is virtual and `c` is a `Child` → calls `Child::bye`.

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
> `~FileHandler()` is NOT virtual. When `delete f` is called through a `FileHandler*`, static binding calls ONLY `~FileHandler()`. The `EncryptedFileHandler` destructor never runs → `key` (32 bytes) leaks. The `buffer` IS properly deleted (via FileHandler's destructor).
>
> Fix: `virtual ~FileHandler() { delete[] buffer; }`
>
> Now dynamic binding calls `~EncryptedFileHandler()` first (deleting `key`), then automatically calls `~FileHandler()` (deleting `buffer`). Both resources freed.

### Drill 3: Abstract Payment System

Design a payment system where `PaymentProcessor` is an abstract base class with:
- A pure virtual `bool charge(double amount)` that returns true if successful
- A virtual `void refund(double amount)` that prints "Refunding [amount] via generic processor"
- A concrete `double getFee(double amount)` that returns `amount * 0.03`

Then write `StripeProcessor` that:
- Overrides `charge` to print "Stripe: charging [amount]" and return true
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
