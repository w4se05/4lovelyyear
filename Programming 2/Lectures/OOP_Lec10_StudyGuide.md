# Lec10: Overloading — Study Guide

---

## 1. CONCEPT CARD: Function & Operator Overloading

**What it is:** Overloading means giving the same name to multiple functions (or operators) that differ in their parameter types, number, or order. The compiler picks the right version based on the arguments you pass.

**What problem it solves:** Without overloading, you'd need names like `addInts`, `addFloats`, `addDoubles`, `addComplex` for essentially the same operation. With operator overloading, you'd need awkward syntax like `complexMultiply(a, complexAdd(b, c))` instead of `a * (b + c)`. Overloading lets you write natural, readable code where the same name adapts to the types you use.

**How it works:**
1. Write multiple functions with the same name but different **signatures** (parameter types, count, or order).
2. At compile time, the compiler uses **overloading resolution** to find the best match for each call.
3. For each argument, the compiler finds ALL functions that could match. If exactly one function fits best, it's chosen. If zero or more than one match equally well, it's an error.
4. For operator overloading, you define a function named `operator+`, `operator=`, `operator[]`, etc. When the compiler sees `a + b`, it calls `a.operator+(b)`.
5. Return type is NOT part of the signature — you cannot overload solely on return type.

**Concrete example:** A `Currency` class for an e-commerce system. You want `price + tax` to work naturally. Overloading `operator+` lets you write `Currency total = price + tax;` instead of `Currency total = price.add(tax);`. Overloading `operator<<` lets you write `cout << total;` instead of `total.print(cout);`. The code reads like a math formula, reducing bugs from misreading verbose function names.

**What it is NOT:** Overloading is NOT overriding. Overloading = same name, DIFFERENT parameters, compile-time resolution, no `virtual` needed. Overriding = same name AND parameters, runtime resolution, requires `virtual` in base class. These are completely different mechanisms.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
// FUNCTION OVERLOADING — same name, different signatures:
void process(int x);              // version 1
void process(double x);           // version 2: different type
void process(int x, int y);       // version 3: different count
void process(int x, double y);    // version 4: different order

// OPERATOR OVERLOADING — inside class:
class Money {
    int cents;
public:
    Money(int c) : cents(c) {}
    Money operator+(const Money& other) {   // member binary operator
        return Money(cents + other.cents);
    }
    Money& operator++() {                   // prefix: ++m
        cents++;
        return *this;
    }
    Money operator++(int) {                 // postfix: m++ (dummy int)
        Money old = *this;
        cents++;
        return old;
    }
};

// Assignment operator pattern (member function):
Money& operator=(const Money& other) {
    if (this != &other) {       // Check for self-assignment!
        cents = other.cents;
    }
    return *this;               // Return reference for chaining
}
```

---

## 3. EXAM TRAPS

- **Return type alone cannot distinguish overloads.** `int foo();` and `double foo();` cannot coexist — the compiler can't tell which one you mean at the call site.
- **Overloading resolution with `double` arguments and `float`/`int` parameters.** `display(double d);` is ambiguous when called with `display(5);` if both `display(int)` and `display(float)` exist — the compiler has multiple valid conversions and can't pick.
- **Copy constructor vs. assignment operator.** Copy constructor: `Money m2 = m1;` or `Money m2(m1);` — called when a NEW object is created. Assignment: `m2 = m1;` — called when an EXISTING object is overwritten. The copy constructor creates; the assignment operator replaces.
- **Self-assignment in operator=.** `a = a;` — if you `delete[]` your data before copying, you've just freed the source data. Always check `if (this != &other)`.
- **Assignment operator must return `*this` by reference.** `return *this;` enables chaining like `a = b = c;`. Returning by value creates unnecessary copies.
- **Prefix `++` returns a reference (`Type&`). Postfix `++` returns a value (`Type`).** The postfix takes a dummy `int` parameter to distinguish it from prefix.
- **Operators you CANNOT overload:** `.` (member access), `.*` (member access-dereference), `::` (scope resolution), `?:` (ternary). Know this list.
- **Operator overloading cannot change precedence, associativity, or arity.** `+` always takes two operands (unary + is a different operator). `*` always has higher precedence than `+`.
- **Default arguments don't work with overloaded operators.** You can't write `Money operator+(const Money& other, int x = 0);` as a member function (members take only one explicit argument anyway).
- **Functions with same name should do semantically similar things.** Don't overload `getCredits()` to sometimes return credits and sometimes SET credits. That's confusing.

---

## 4. HAND-CODING DRILLS

### Drill 1: Overloading Resolution Puzzle

```cpp
void show(int x)          { cout << "int "; }
void show(double x)       { cout << "double "; }
void show(int x, int y)   { cout << "int,int "; }
void show(float x)        { cout << "float "; }

int main() {
    show(5);        // A
    show(5.0);      // B
    show(5, 10);    // C
    show(3.14f);    // D
    show('A');      // E
}
```
What is the output for each call? Explain any conversions.

> [!success]- Show Answer
> `int double int,int float int`
>
> - A: `5` is `int` → exact match with `show(int)`.
> - B: `5.0` is `double` → exact match with `show(double)`.
> - C: Two `int` arguments → exact match with `show(int, int)`.
> - D: `3.14f` is `float` → exact match with `show(float)`.
> - E: `'A'` is `char` → promotes to `int` (closest match, no `show(char)`). Calls `show(int)`.

### Drill 2: Assignment Operator — Complete Pattern

Write the full `operator=` for a `String` class that owns a dynamic `char*` buffer. Include the self-assignment check.

```cpp
class String {
    char* data;
public:
    String(const char* s);
    String(const String& other);   // copy constructor
    ~String();
    // TODO: write operator=
};
```

> [!success]- Show Answer
> ```cpp
> String& String::operator=(const String& other) {
>     if (this != &other) {              // (1) Guard against self-assignment
>         delete[] data;                 // (2) Free old buffer
>         int len = 0;
>         while (other.data[len]) len++; // (3) Measure source
>         data = new char[len + 1];      // (4) Allocate new buffer
>         for (int i = 0; i <= len; i++) // (5) Copy including '\0'
>             data[i] = other.data[i];
>     }
>     return *this;                      // (6) Return reference for chaining
> }
> ```

### Drill 3: Complex Number Operator Overloading

Implement a `Complex` class with `real` and `imag` as private `double` members. Overload:
- `operator+` to add two Complex numbers: (a+bi) + (c+di) = (a+c) + (b+d)i
- `operator==` to compare: equal if both real AND imag parts match
- Postfix `operator++` that increments only the real part by 1

> [!success]- Show Answer
> ```cpp
> class Complex {
> private:
>     double real;
>     double imag;
> public:
>     Complex(double r = 0, double i = 0) : real(r), imag(i) {}
>
>     Complex operator+(const Complex& other) const {
>         return Complex(real + other.real, imag + other.imag);
>     }
>
>     int operator==(const Complex& other) const {
>         return (real == other.real) && (imag == other.imag);
>     }
>
>     Complex operator++(int) {           // postfix: dummy int
>         Complex old = *this;
>         real = real + 1;
>         return old;
>     }
> };
> ```
