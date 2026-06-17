# Lec10: Overloading — Study Guide

---

## 1. CONCEPT CARD

### 1.1 What It Is — Same Name, Different Signatures; Compiler Picks Right Version at Compile Time

Overloading is the ability to define multiple functions (or operators) with the **same name** but **different parameter lists** — differing in **number**, **type**, or **order** of parameters. The compiler selects which version to call at **compile time** based on the arguments provided. This is a form of **ad-hoc polymorphism** (static/dispatch polymorphism).

It applies to:
- **Function overloading** — standalone or member functions with the same name, different signatures
- **Operator overloading** — giving new meaning to standard C++ operators when used with user-defined types
- **Constructor overloading** — multiple constructors with different parameter lists

### 1.2 What Problem It Solves — No More `addInts`/`addFloats`/`addDoubles`; Natural Syntax Like `a + b` for Custom Types

Without overloading, you would need uniquely named functions for every combination of parameter types:

```cpp
// WITHOUT overloading — ugly, hard to remember, non-scalable
int    addInts(int a, int b)       { return a + b; }
float  addFloats(float a, float b) { return a + b; }
double addDoubles(double a, double b) { return a + b; }
// ... and so on for every type
```

With overloading:

```cpp
// WITH overloading — clean, natural, compiler figures it out
int    add(int a, int b)    { return a + b; }
float  add(float a, float b) { return a + b; }
double add(double a, double b) { return a + b; }
add(3, 5);       // calls int version
add(3.0f, 5.0f); // calls float version
```

This is about **expressiveness** and **natural syntax**. For operator overloading, it lets you write `c1 + c2` for `Complex` numbers, `m1 + m2` for `Money` objects, `t1 < t2` for `Time` objects — making custom types behave as intuitively as built-in types.

### 1.3 How It Works

1. The **compiler** examines every argument at each call site.
2. For each overload candidate with the same name, the compiler checks how well each argument matches the declared parameter types.
3. A match is ranked (best to worst): **exact match** > **promotion** (e.g., `char` → `int`) > **standard conversion** (e.g., `int` → `long`, `float` → `double`) > **user-defined conversion**.
4. The compiler selects the **single best-matching** function across ALL arguments.
5. If **zero** functions match or **more than one** function ties for best → **compilation error**.
6. The **return type is NOT part of the signature** — the compiler does NOT use the return type to distinguish overloads. Two functions with the same name and same parameter list but different return types produce a compilation error.
7. All of this happens at **compile time** (static resolution), unlike overriding which is resolved at **runtime** via vtables.

### 1.4 Concrete Example — Currency Class for E-Commerce: Price + Tax

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Currency {
    long dollars;
    int  cents;
public:
    Currency(long d = 0, int c = 0) : dollars(d), cents(c) {
        normalize();
    }

    void normalize() {
        if (cents >= 100) { dollars += cents / 100; cents %= 100; }
        if (cents < 0)    { dollars -= 1 + (-cents) / 100; cents = 100 - (-cents) % 100; }
    }

    // Overloaded + operator — adds two Currency objects naturally
    Currency operator+(const Currency& other) const {
        return Currency(dollars + other.dollars, cents + other.cents);
    }

    // Overloaded << for easy printing
    friend ostream& operator<<(ostream& os, const Currency& c) {
        os << "$" << c.dollars << "." << setw(2) << setfill('0') << c.cents;
        return os;
    }
};

int main() {
    Currency price(19, 99);     // $19.99
    Currency tax(1, 50);        // $1.50 — 7.5% sales tax
    Currency total = price + tax;

    cout << "Price:      " << price << endl;   // $19.99
    cout << "Tax:        " << tax   << endl;   // $1.50
    cout << "Total:      " << total << endl;   // $21.49
    // No addCurrency(price, tax) nonsense — just price + tax!
}
```

**What the compiler does**: When it sees `price + tax`, it translates this to `price.operator+(tax)`. The `operator+` is resolved statically — the compiler knows both operands are `Currency`, so it calls the `Currency::operator+` defined in the class. No runtime dispatch, no vtable.

### 1.5 What It Is NOT — NOT Overriding (Same Name + Params, Runtime, Virtual Required)

This is perhaps the most confusing distinction in C++. Overloading and overriding are fundamentally different:

| Aspect | Overloading | Overriding (Polymorphism) |
|--------|------------|---------------------------|
| Parameters | **Different** — must differ in number, type, or order | **Same** — identical signature |
| Resolution time | **Compile-time** (static binding) | **Runtime** (dynamic binding) |
| `virtual` keyword | Not required, irrelevant | Required in base class |
| Inheritance | Not required | Required (base-derived relationship) |
| Return type | Cannot distinguish overloads (not part of signature) | Must be **covariant** (same or derived) in C++ |
| Mechanism | Compiler mangles function name with parameter types | Compiler generates vtable; call resolved via vptr at runtime |
| Also known as | Ad-hoc polymorphism, static polymorphism | Inclusion polymorphism, dynamic polymorphism |

```cpp
class Base {
public:
    // These are OVERLOADS of each other — different parameters
    void print(int x)     { cout << "int: "   << x << endl; }
    void print(double x)  { cout << "double: " << x << endl; }
    void print(string s)  { cout << "string: " << s << endl; }

    // This would be OVERRIDDEN in a derived class (needs virtual!)
    virtual void display() { cout << "Base::display" << endl; }
};

class Derived : public Base {
public:
    // OVERRIDES Base::display — same signature, virtual, inheritance
    void display() { cout << "Derived::display" << endl; }
};
```

---

## 2. FUNCTION OVERLOADING

### 2.1 Definition — Several Functions with Same Name, Parameters Differ in Number, Type, or Order

Function overloading allows multiple functions in the **same scope** to share the same name, provided they have **different signatures**. The signature consists of:
- Function **name**
- **Number** of parameters
- **Types** of parameters
- **Order** of parameter types

Key rule: the parameter lists must be **distinguishable**. The compiler uses the argument types at the call site to determine which overload to invoke.

```cpp
// Valid overloading — different parameter types
void log(const char* msg);     // C-string
void log(string msg);          // std::string
void log(int code, string msg); // two params
void log(string msg, int code); // different ORDER — also valid

// INVALID — same signature, only return type differs
int  getValue();  // ERROR: redeclaration
double getValue(); // ERROR: cannot overload on return type alone
```

### 2.2 Signature — Function Identified by Name + Number + Order + Types of Parameters (= the SIGNATURE). Return Type NOT Part of Signature!

The **signature** is the unique identifier the compiler uses for name mangling and overload resolution:

```
SIGNATURE = function-name + (parameter-count, parameter-types-in-order)
```

**What is NOT in the signature:**
- **Return type** — two functions with the same name and same parameters but different return types are a compile error, not an overload.
- **`const` qualifier on non-member parameters** — `void f(int)` and `void f(const int)` have the same signature (pass-by-value).
- **Default arguments** — `void f(int x)` and `void f(int x = 5)` are the same function (the default just provides a value when omitted).

```cpp
int  compute(int a);     // #1
// double compute(int a); // ERROR: redeclaration — same signature, different return type

void process(int& ref);  // #2
void process(const int& ref); // VALID overload — different parameter type (const ref vs non-const ref)

// Default arguments do NOT create overloads:
void display(int x = 10); // #3
// void display(int x);   // ERROR — this is the same function as #3
```

**What IS in the signature (for member functions):**
- **`const` member function qualifier** — `void foo() const` vs `void foo()` are different signatures.
- **`volatile` qualifier**
- **`&` and `&&` ref-qualifiers** (C++11)

### 2.3 Examples from Lecture

```cpp
void swap(unsigned long &, unsigned long &);
void swap(double &, double &);
void swap(char &, char &);
void swap(Point &, Point &);
```

**"Each is a different function!!!"**

Despite all being called `swap`, these are four **distinct** functions with four **distinct** addresses in memory. The compiler generates different names internally (name mangling). When you call:

```cpp
unsigned long a = 100, b = 200;
swap(a, b);          // Compiler: "ah, unsigned long& — call swap(unsigned long&, unsigned long&)"

double x = 1.5, y = 2.5;
swap(x, y);          // Compiler: "ah, double& — call swap(double&, double&)"

char c = 'A', d = 'B';
swap(c, d);          // Compiler: "ah, char& — call swap(char&, char&)"

Point p1(0,0), p2(1,1);
swap(p1, p2);        // Compiler: "ah, Point& — call swap(Point&, Point&)"
```

The decision is made **statically** — the compiler simply looks at the declared type of each argument and picks the matching function. No runtime lookup, no vtable, no overhead beyond an ordinary function call.

### 2.4 Poor Practice Warning — Functions with Same Name Should Have SIMILAR Functionality

The lecture explicitly warns against using overloading for functions with **different semantics**:

```cpp
class Student {
public:
    unsigned credits();          // GET the credits
    unsigned credits(unsigned n); // SET the credits — different semantics, BAD!
};
```

This is **poor practice** because:
- The name `credits` suggests a single conceptual operation — yet one form queries and the other mutates.
- Readers of code using `Student` see `s.credits(30)` and may not immediately realize this is a **setter**, not some calculation.
- Overloading should be used for **conceptually similar operations** that differ only in the types or number of inputs.
- A getter and setter with the same name violates the **principle of least surprise**.

**Good alternative:**

```cpp
class Student {
public:
    unsigned getCredits() const;      // clear: this queries
    void     setCredits(unsigned n);  // clear: this mutates
};
```

The rule: if the parameter difference implies a **fundamentally different behavior**, use **different names**.

### 2.5 Overloading Constructors

Constructors are special member functions — they can be overloaded just like any other function, enabling multiple ways to initialize an object.

**Point class — single constructor with defaults:**

```cpp
class Point {
    int x, y;
public:
    Point(int xx = 0, int yy = 0) { x = xx; y = yy; }
};
```

This single constructor serves three purposes via default arguments:
- `Point p1;` — both defaults → `(0, 0)`
- `Point p2(5);` — `xx=5, yy=0`
- `Point p3(5, 10);` — `xx=5, yy=10`

**Figure class — three distinct constructors:**

```cpp
class Figure {
public:
    Figure() { }                                    // default constructor — no arguments
    Figure(const Point & center) { }                // create figure from a center Point
    Figure(const Point vertices[], int count) { }   // create figure from array of Points
};

int main() {
    Figure fig1[3];                  // default constructor called 3 times
    Point center(25, 50);
    Figure fig2(center);             // 2nd constructor — Point reference
    const int VCount = 5;
    Point verts[VCount];             // default Point called 5 times → all (0,0)
    Figure fig3(verts, VCount);      // 3rd constructor — Point array + count
}
```

**Trace:**
- `Figure fig1[3]` — creates an array of 3 `Figure` objects. Each one invokes the **default constructor** `Figure()` because no arguments are passed.
- `Figure fig2(center)` — compiler sees one argument of type `Point` → matches `Figure(const Point &)` exactly → 2nd constructor.
- `Figure fig3(verts, VCount)` — compiler sees two arguments: `Point[]` and `int` → matches `Figure(const Point[], int)` → 3rd constructor.

Constructor overloading follows the same resolution rules as function overloading: best-match wins, ambiguity is an error.

---

## 3. COERCION (REVISITED)

### 3.1 Definition — Object or Primitive Automatically Cast into Another Type (More Than Just Overloading)

**Coercion** is the automatic/implicit conversion of a value from one type to another. This is a **separate concept** from overloading, but the two interact intimately during overload resolution. The compiler uses coercion to *make arguments fit* the parameters of an overload candidate.

Types of coercion:
- **Promotion** (no data loss): `char` → `int`, `float` → `double`, `bool` → `int`
- **Standard conversion** (possible data loss): `int` → `long`, `double` → `float`, `int` → `char`
- **User-defined conversion**: via constructors with single argument or conversion operators
- **Trivial conversion**: `int` → `const int`, array → pointer

### 3.2 Example — `calculate` Function

```cpp
void calculate(long p1, long p2, double p3, double p4);

long   a1 = 12345678;
int    a2 = 1;
double a3 = 2.3455555;
float  a4 = 3.1;

calculate(a1, a2, a3, a4); // OK — compiler coerces:
                            // a1: long → long  (exact match)
                            // a2: int  → long  (standard conversion)
                            // a3: double → double (exact match)
                            // a4: float → double (promotion)

Student s;
calculate(s, 10, 5.5, 6);  // ERROR: Student → long? No viable conversion path
```

The key insight: the compiler tries **each argument individually** against the expected parameter type. If every argument has a valid conversion path, the call succeeds. If **any** argument has no viable conversion path → error.

### 3.3 `add` Function Coercion Example (from Lecture)

```cpp
int add(int a, int b)     { return a + b; }
float add(float a, float b) { return 1.0 + a + b; }

int main() {
    cout << add(1, 1.0) << endl; // Which one is called?
}
```

**Resolution:**
- `add(1, 1.0)` — arguments are `int` and `double`.
- Candidate 1: `add(int, int)` — first argument exact match, second needs `double → int` conversion.
- Candidate 2: `add(float, float)` — both arguments need conversion (`int → float`, `double → float`).
- Candidate 1 is **better** (one exact match + one conversion) than Candidate 2 (two conversions).
- Result: calls `add(int, int)`, returns `1 + 1 = 2`. The `1.0` is **coerced** (truncated) to `1`.

**Key caution**: coercion can cause **silent data loss**. `1.0` becomes `1` — the fractional part is discarded without warning. This is why compilers sometimes warn about narrowing conversions.

---

## 4. OVERLOADING RESOLUTION

### 4.1 Best-Matching Function Principle

The C++ standard defines a rigorous algorithm for overload resolution:

1. **Candidate set**: All functions with the correct name visible at the call site (including those brought in by `using` declarations or argument-dependent lookup).
2. **Viable set**: Candidates that can accept the given number of arguments and for which each argument has a valid implicit conversion to the corresponding parameter type.
3. **Best match selection**: For each viable function, the compiler ranks the conversion required for each argument. The function requiring the "best" conversions across all arguments is selected.

**If zero viable functions exist** → "no matching function" error.
**If more than one is equally "best" (tie)** → "ambiguous call" error.

### 4.2 Example 1 — Ambiguous `double`

```cpp
void display(int x);   // version 1
void display(float y); // version 2

int i; float f; double d;

display(i); // version 1 — int→int exact match. float would need int→float conversion.
display(f); // version 2 — float→float exact match. int would need float→int conversion.
display(d); // ERROR! double matches BOTH int and float equally poorly.
             // double→int: standard conversion (floating-integral)
             // double→float: standard conversion (floating point)
             // Neither is better → AMBIGUITY → compilation error
```

**Why `double` is ambiguous**: Both `int` and `float` are equally "far" from `double`. Neither conversion is ranked higher than the other. The compiler cannot choose, so it reports an ambiguity error.

### 4.3 Example 2 — Mixed Types (from Lecture)

```cpp
void print(float a, float b) { cout << "version 1\n"; }
void print(float a, int b)  { cout << "version 2\n"; }

int main() {
    int i = 0, j = 0;
    float f = 0.0;
    double d = 0.0;

    print(i, j);   // version 2 — why?
                   // Candidate 1: print(float, float) — both i,j need int→float conversion
                   // Candidate 2: print(float, int)  — i needs int→float, j is int→int exact
                   // Candidate 2 wins: one exact match + one conversion beats two conversions

    print(i, f);   // version 1 — why?
                   // Candidate 1: print(float, float) — i:int→float, f:float→float exact
                   // Candidate 2: print(float, int)  — i:int→float, f:float→int conversion
                   // Candidate 1 wins: one exact + one conversion beats one conversion + one conversion
                   // (the exact match on f makes v1 better)

    print(d, f);   // version 1 — why?
                   // Candidate 1: print(float, float) — d:double→float, f:float→float exact
                   // Candidate 2: print(float, int)  — d:double→float, f:float→int conversion
                   // Candidate 1 wins: same conversion for first arg, exact match for second vs conversion
}
```

Resolution summary table:

| Call | v1: `(float,float)` | v2: `(float,int)` | Winner | Reason |
|------|---------------------|-------------------|--------|--------|
| `print(i, j)` | i: int→float, j: int→float | i: int→float, j: **exact** | v2 | Exact match on j |
| `print(i, f)` | i: int→float, j: **exact** | i: int→float, j: float→int | v1 | Exact match on f |
| `print(d, f)` | d: double→float, f: **exact** | d: double→float, f: float→int | v1 | Exact match on f |

### 4.4 Example 3 — Errors Requiring Explicit Cast

```cpp
print(d, 3.5);  // ERROR — why?
                // Candidate 1: print(float, float) — d:double→float, 3.5:double→float
                // Candidate 2: print(float, int)  — d:double→float, 3.5:double→int
                // First argument identical in both. Second argument: double→float vs double→int.
                // Both are standard conversions, neither is better → AMBIGUITY

print(i, 4.5);  // ERROR — same logic
                // Candidate 1: print(float, float) — i:int→float, 4.5:double→float
                // Candidate 2: print(float, int)  — i:int→float, 4.5:double→int
                // First arg same, second arg tie → AMBIGUITY

print(d, 3.0);  // ERROR — 3.0 is a double literal
                // Same ambiguity: double→float vs double→int tie on second argument

print(i, d);    // ERROR — i:int→float (both), d:double→float vs double→int → tie
```

**Explicit casting resolves ambiguity:**

```cpp
print(d, float(3.5));  // version 1 — unambiguous: float(float) is exact match
print(i, int(4.5));    // version 2 — unambiguous: int(int) is exact match
print(d, float(3.0));  // version 1 — unambiguous
print(i, int(d));      // version 2 — unambiguous (d truncated to int)
```

**Key lesson**: When overload resolution is ambiguous, explicitly cast arguments to select the desired overload. This tells the compiler exactly which type you intend, removing the tie.

---

## 5. OPERATOR OVERLOADING

### 5.1 Definition — Ascribing New Meaning to Standard Operators (+, >>, =, ...) When Used with Class Operands

Operator overloading allows you to define (or redefine) the behavior of C++'s built-in operators when they are applied to user-defined types. Internally, an overloaded operator is just a **function** with a special name (`operator +`, `operator =`, `operator <<`, etc.).

### 5.2 Why? — A Way to Name a Function; Makes Program MORE READABLE

Without operator overloading:

```cpp
// Without operator overloading — verbose, unnatural
Complex c1(1, 2), c2(3, 4), c3;
c3 = add(multiply(c1, c2), c1);  // c3 = c1*c2 + c1 — hard to parse
```

With operator overloading:

```cpp
// With operator overloading — clean, mathematical
Complex c1(1, 2), c2(3, 4), c3;
c3 = c1 * c2 + c1;  // immediately obvious what's happening
```

The operator syntax makes custom types feel like first-class citizens of the language. It reduces cognitive load — the reader sees `a + b` and understands it as addition, regardless of whether `a` and `b` are `int`s, `double`s, or `Complex` numbers.

### 5.3 Basic Syntax

```cpp
class AClass {
public:
    int operator+(AClass &a) { return 1; }
};

int main() {
    AClass a, b;
    int i;
    i = a + b;        // i = a.operator+(b); ← the compiler rewrites it this way
}
```

**Key syntactic rules:**
- The operator name is `operator` followed by the operator symbol: `operator+`, `operator=`, `operator<<`, etc.
- For a **member function** unary operator: `Type operator-() const;` (no parameters — the operand is `*this`).
- For a **member function** binary operator: `Type operator+(const Type& other) const;` (one parameter — the right operand; the left operand is `*this`).
- For a **non-member function** binary operator: `Type operator+(const Type& a, const Type& b);` (two parameters — both operands explicit).
- The call `a + b` is syntactic sugar for either `a.operator+(b)` (member) or `operator+(a, b)` (non-member).

### 5.4 Already Overloaded in C++

The `+` operator is already overloaded in standard C++:
- **Integer addition**: `int + int`
- **Floating-point addition**: `float + float`, `double + double`
- **Pointer addition**: `int* + int` (pointer arithmetic — adds `int * sizeof(element)` bytes)

This demonstrates that operator overloading is not exotic — it's a **fundamental part** of how C++ works. The language itself uses overloading extensively in its built-in types. You're simply extending the same capability to your own types.

### 5.5 Operators ALLOWING Overloading

**Unary operators** (most can be overloaded as member or non-member):

| Category | Operators |
|----------|-----------|
| Memory management | `new`, `delete`, `new[]`, `delete[]` |
| Arithmetic | `+`, `-` (unary plus/minus) |
| Increment/decrement | `++` (prefix), `++` (postfix), `--` (prefix), `--` (postfix) |
| Dereference | `*`, `->` |
| Address-of | `&` |
| Logical/Bitwise | `!`, `~` |
| Function call / indexing | `()`, `[]` |

**Binary operators** (most can be overloaded as member or non-member):

| Category | Operators |
|----------|-----------|
| Arithmetic | `+`, `-`, `*`, `/`, `%` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `%=` |
| Bitwise | `&`, `\|`, `^`, `<<`, `>>` |
| Compound bitwise | `&=`, `\|=`, `^=`, `<<=`, `>>=` |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical | `&&`, `\|\|` |
| Member access | `->`, `->*` |
| Stream | `<<`, `>>` |

### 5.6 Operators NOT Allowing Overloading

These four operators **CANNOT** be overloaded — period:

| Operator | Name | Why it can't be overloaded |
|----------|------|---------------------------|
| `.` | Member access | Fundamental to the object model; overloading would break the language |
| `.*` | Member access-dereference (pointer-to-member) | Same reason as `.` |
| `::` | Scope resolution | Operates on names, not values; fundamentally a compile-time mechanism |
| `?:` | Ternary conditional (arithmetic-IF) | Only ternary operator; short-circuit evaluation semantics can't be replicated |

**Mnemonics to remember**:
- "**D**on't **o**verload **t**hings **w**ith **d**ots **a**nd **c**olons" — `.`, `.*`, `::`, `?:`
- Or: "The four forbidden operators all deal with **name resolution** or **conditional evaluation**, not value computation."

### 5.7 Restrictions

Three critical restrictions apply to **all** operator overloading:

1. **Neither precedence nor associativity can be changed** — The compiler determines precedence and associativity based on the **operator symbol**, not the operand types. You cannot make `+` bind tighter than `*` or make `=` right-to-left.

2. **Default arguments CANNOT be used** — Operator functions cannot have default parameters. Every argument must be explicitly provided at the call site (which translates to the number of operands in the expression).

   ```cpp
   class Bad {
   public:
       // ERROR: default arguments on overloaded operator
       int operator+(int x, int y = 5);  // NOT ALLOWED
   };
   ```

3. **"Arity" of the operator cannot be changed** — A binary operator stays binary, a unary operator stays unary. You cannot turn `+` into a unary operator that takes three operands, nor can you make `++` a binary operator.

4. **Only EXISTING operators may be overloaded** — You cannot invent new operators (e.g., `**` for exponentiation, `$` for a custom operation). You may only overload operators that are already part of the C++ language grammar.

---

## 6. THE TIME CLASS (PREFIX vs POSTFIX ++)

### 6.1 Prefix `++a` → Compiler Generates `Time::operator++()`

The **prefix** increment (and decrement) operator is straightforward:

```cpp
class Time {
    int hours, minutes, seconds;
public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) {}

    // Prefix ++: increment and return the modified object
    Time& operator++() {
        seconds++;
        if (seconds >= 60) { seconds = 0; minutes++; }
        if (minutes >= 60) { minutes = 0; hours++; }
        return *this;  // return reference to the modified object
    }
};

int main() {
    Time t(0, 59, 59);
    ++t;    // calls t.operator++() — t becomes 1:00:00
            // Returns Time& (reference to t)
}
```

**Signature**: `Time& operator++()` — no parameters. The compiler sees `++t` and generates a call to the parameterless `operator++()`.

**Return value**: Returns by **reference** (`Time&`) — this enables `++(++t)` to work correctly (double increment). It also avoids an unnecessary copy.

### 6.2 Postfix `a++` → Compiler Calls `Time::operator++(int)`

The **postfix** increment is more subtle. It must return the **old value** before incrementing:

```cpp
class Time {
    int hours, minutes, seconds;
public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) {}

    // Postfix ++: save old value, increment, return OLD value
    Time operator++(int) {
        Time old = *this;  // save a copy of the current state
        ++(*this);         // reuse prefix operator to do the increment
        return old;        // return the OLD value (by value, not reference!)
    }
};

int main() {
    Time t(0, 59, 59);
    Time old = t++;  // old = 0:59:59, t = 1:00:00
                     // t++ returns Time (a copy), NOT Time&
}
```

**Signature**: `Time operator++(int)` — has a **dummy `int` parameter**. This is the mechanism C++ uses to distinguish prefix from postfix.

**Return value**: Returns by **value** (`Time`, NOT `Time&`). Returning a reference to the local `old` would be a dangling reference — it's destroyed when the function exits. Postfix is inherently less efficient because it requires a copy.

| Aspect | Prefix `++t` | Postfix `t++` |
|--------|-------------|---------------|
| Signature | `Type& operator++()` | `Type operator++(int)` |
| Return type | `Type&` (reference) | `Type` (value/copy) |
| Returns | Modified object (`*this`) | Old value (copy) |
| Efficiency | No copy needed | Requires copy of old state |
| Chaining | `++(++t)` works | `(t++)++` works but semantically odd |

### 6.3 The Dummy `int` — Compiler Passes a Dummy Constant for the `int` Argument (Never Used, No Identifier Given) to Generate DIFFERENT Signatures for Prefix and Postfix

The dummy `int` parameter exists **solely** to make the signature different:

```cpp
// Without the dummy int — SAME SIGNATURE — would be a redefinition error
Time& operator++();      // prefix  — WRONG if both have same sig
Time  operator++();      // postfix — WRONG: return type alone doesn't distinguish overloads

// WITH the dummy int — DIFFERENT SIGNATURES — valid overloading
Time& operator++();      // prefix  — no parameters
Time  operator++(int);   // postfix — one int parameter (dummy)
```

When you write `t++`, the compiler automatically passes a dummy integer value (typically `0`) as the `int` argument. The parameter is typically **left unnamed** (just `int`, not `int dummy`) because the value is never used — it exists only for overload resolution:

```cpp
Time operator++(int) {   // note: no parameter name — the int is never used
    Time old = *this;
    // ... increment ...
    return old;
}
```

This convention applies equally to `--` (prefix and postfix decrement).

---

## 7. ASSIGNMENT OPERATOR vs COPY CONSTRUCTOR

### 7.1 Copy Constructor

The copy constructor initializes a **new** object as a copy of an existing object of the same type:

```cpp
Transcript::Transcript(const Transcript & T) {
    count = T.count;
    courses = new string[MAXCOURSE];
    for (unsigned i = 0; i < count; i++)
        courses[i] = T.courses[i];
}
```

**When the copy constructor is called:**

```cpp
Transcript t1;                // default constructor
Transcript t2 = t1;           // COPY CONSTRUCTOR — new object being created
Transcript t3(t1);            // COPY CONSTRUCTOR — same, direct syntax
Transcript t4(t1 + t2);       // COPY CONSTRUCTOR — temporary result copied to new object
void foo(Transcript t);       // COPY CONSTRUCTOR — pass by value copies the argument
foo(t1);
Transcript bar() {
    Transcript t;
    return t;                 // COPY CONSTRUCTOR — return value copied (may be elided by RVO)
}
```

**Key characteristic**: The object being constructed **does not exist yet** — it has no prior state, so there's nothing to clean up first. The copy constructor just initializes.

### 7.2 Assignment Operator (FULL Pattern from Lecture)

The assignment operator overwrites an **existing** object with the value of another:

```cpp
Transcript & Transcript::operator=(const Transcript & T) {
    if (this != &T) {                      // 1. Self-assignment check
        delete[] courses;                  // 2. Free old memory
        courses = new string[MAXCOURSE];   // 3. Allocate new memory
        count = T.count;                   // 4. Copy data
        for (int i = 0; i < count; i++)
            courses[i] = T.courses[i];
    }
    return *this;                          // 5. Return reference for chaining
}
```

**Step-by-step explanation of the pattern:**

1. **Self-assignment check** (`if (this != &T)`): If `t = t;` is written (or aliasing causes self-assignment), skipping the work prevents `delete[]` from destroying your own data before you copy it. Without this check, `t = t` would delete the array, then try to copy from the deleted (garbage) array — disaster.

2. **Free old memory** (`delete[] courses`): The object already exists and owns resources. Before overwriting with new data, you must release the old resources to prevent memory leaks. If you skip this step and just `new` over the pointer, the old allocation is leaked.

3. **Allocate new memory** (`courses = new string[MAXCOURSE]`): Get fresh memory for the incoming data.

4. **Copy data**: Copy values from the source object.

5. **Return `*this` by reference** (`return *this`): Returns a reference to the now-modified object, enabling assignment chaining (`a = b = c`). The return type is `Transcript &`, NOT `Transcript` (which would make an unnecessary copy) and NOT `void` (which would prevent chaining).

### 7.3 When Each Is Called

```cpp
Transcript t1;            // default constructor
Transcript t2 = t1;       // COPY CONSTRUCTOR — t2 is being created (new object)
Transcript t3(t2);        // COPY CONSTRUCTOR — t3 is being created (new object)

t2 = t1;                  // ASSIGNMENT OPERATOR — t2 already exists, being overwritten
t1 = t2 = t3;             // ASSIGNMENT — chained: t2 = t3 assigns, returns ref, then t1 = ref

// Tricky case — looks like assignment but is actually copy construction:
Transcript t4 = t1;       // COPY CONSTRUCTOR — NOT assignment! t4 is being created.
                          // The '=' here is initialization syntax, not operator=.
```

**The crucial distinction**: 

| Situation | Example | What's called | Why |
|-----------|---------|---------------|-----|
| Object being **declared** with an initializer | `Transcript t2 = t1;` | Copy constructor | `t2` didn't exist before this line |
| Object being **declared** with direct init | `Transcript t2(t1);` | Copy constructor | Same — `t2` is new |
| **Existing** object on LHS of `=` | `t2 = t1;` | `operator=` | `t2` already exists, overwriting |
| Pass-by-value to function | `void f(Transcript t); f(t1);` | Copy constructor | Parameter `t` is initialized as a copy |
| Return by value | `return t;` | Copy constructor | Return value object is initialized (may be elided) |

---

## 8. MUST-MEMORIZE SYNTAX TEMPLATES

### 8.1 Function Overloading (Different Signatures)

```cpp
// Same name, different parameter types
void swap(unsigned long &a, unsigned long &b) {
    unsigned long tmp = a; a = b; b = tmp;
}
void swap(double &a, double &b) {
    double tmp = a; a = b; b = tmp;
}
void swap(char &a, char &b) {
    char tmp = a; a = b; b = tmp;
}
void swap(Point &a, Point &b) {
    Point tmp = a; a = b; b = tmp;
}
```

### 8.2 Operator Overloading (Member Function)

```cpp
class AClass {
public:
    // Binary operator as member — left operand is *this
    int operator+(const AClass &a) const { return /* ... */; }

    // Unary operator as member — no parameters
    AClass operator-() const { return /* ... */; }
};
```

### 8.3 Assignment Operator (Full Pattern)

```cpp
class MyClass {
public:
    MyClass& operator=(const MyClass& other) {
        if (this != &other) {          // Self-assignment guard
            // 1. Free existing resources
            delete[] data;
            // 2. Allocate new resources
            data = new int[other.size];
            // 3. Copy data
            size = other.size;
            for (int i = 0; i < size; i++)
                data[i] = other.data[i];
        }
        return *this;                  // Enable chaining: a = b = c
    }
};
```

### 8.4 Copy Constructor

```cpp
class MyClass {
public:
    MyClass(const MyClass& other) {
        // No self-assignment check needed — this is a NEW object
        data = new int[other.size];
        size = other.size;
        for (int i = 0; i < size; i++)
            data[i] = other.data[i];
    }
};
```

### 8.5 Prefix vs Postfix `operator++`

```cpp
class Counter {
    int value;
public:
    // PREFIX ++x: increment, return CHANGED object by reference
    Counter& operator++() {
        value++;
        return *this;
    }

    // POSTFIX x++: return OLD value by copy, dummy int distinguishes
    Counter operator++(int) {
        Counter old = *this;   // save copy
        ++(*this);             // reuse prefix to increment
        return old;            // return OLD value
    }
};
```

### 8.6 Operators that CANNOT be Overloaded (Memorize This List)

| Operator | Name |
|----------|------|
| `.`      | Member access |
| `.*`     | Member access-dereference |
| `::`     | Scope resolution |
| `?:`     | Ternary conditional (arithmetic-IF) |

**Only these four cannot be overloaded.** Everything else (`+`, `-`, `*`, `/`, `%`, `=`, `==`, `<`, `>`, `<<`, `>>`, `[]`, `()`, `new`, `delete`, `->`, etc.) CAN be overloaded.

---

## 9. EXAM TRAPS

### Trap 1: Return Type Alone Cannot Distinguish Overloads

```cpp
int  getValue();      // OK
// double getValue(); // ERROR: redeclaration — same signature
                       // Return type is NOT part of the signature
```

### Trap 2: `double` Argument Ambiguity with `int`/`float` Overloads

```cpp
void f(int x);
void f(float x);
double d = 3.14;
f(d);  // ERROR — double matches BOTH int and float equally
```

### Trap 3: Copy Constructor vs Assignment — WHEN Each Is Called

```cpp
MyClass a;
MyClass b = a;  // COPY CONSTRUCTOR — b is NEW (looks like = but it's init)
b = a;          // ASSIGNMENT OPERATOR — b already exists
```

The `=` in a **declaration** is initialization syntax (copy constructor), NOT the assignment operator!

### Trap 4: Self-Assignment Must Be Checked or You Delete Your Own Data

```cpp
Transcript& Transcript::operator=(const Transcript& T) {
    if (this != &T) {    // WITHOUT THIS CHECK:
        delete[] courses; // If t = t, this deletes t's own courses!
        // ...
    }
    return *this;
}
```

### Trap 5: `operator=` Must Return `*this` by Reference

```cpp
MyClass& MyClass::operator=(const MyClass& other) {  // Return by REFERENCE
    // ...
    return *this;  // Return reference to self
}
```

Returning `void` would prevent `a = b = c` chaining.
Returning by value (`MyClass`) would create an unnecessary copy.

### Trap 6: Prefix Returns `Type&`, Postfix Returns `Type`

```cpp
Type& operator++();   // PREFIX  — returns reference (no copy)
Type  operator++(int); // POSTFIX — returns value (must copy old state)
```

Postfix returning by reference would be a **dangling reference** — returning a reference to a local variable that's destroyed when the function exits.

### Trap 7: Cannot Overload `.` `.*` `::` `?:`

Only these four operators are forbidden. Know this cold — it's a guaranteed exam question.

### Trap 8: Cannot Change Precedence, Associativity, or Arity

```cpp
// NONE of this works:
// int operator+(int a, int b, int c);  // ERROR: arity changed (3 operands)
// int operator+(int a);                // ERROR: arity changed (unary + is different operator)
// int operator**(int a, int b);        // ERROR: cannot invent new operators
```

### Trap 9: Default Arguments Can't Be Used with Overloaded Operators

```cpp
class Bad {
public:
    // int operator+(int x, int y = 5);  // ERROR: default arguments not allowed
};
```

### Trap 10: Functions with Same Name Should Do Similar Things

Using the same name for a getter and setter (e.g., `credits()` vs `credits(unsigned)`) is bad practice because the semantics differ dramatically. Use `getCredits()` and `setCredits()` instead.

### Trap 11: Best-Matching Function: Zero or Multiple Matches = Error

```cpp
void f(int, double);
void f(double, int);
f(1, 1);  // ERROR — ambiguous! int→int exact vs int→double in first vs second
```

### Trap 12: Explicit Casting Resolves Ambiguity

```cpp
void f(int);
void f(float);
double d = 3.14;
f(static_cast<int>(d));    // OK — explicitly calls f(int)
f(static_cast<float>(d));  // OK — explicitly calls f(float)
```

### Trap 13: Coercion vs Overloading — Different Concepts

- **Coercion**: Automatic type conversion (`int` → `long`, `float` → `double`).
- **Overloading**: Multiple functions with the same name, different signatures.
- They **interact**: coercion makes arguments fit overload candidates, which can cause ambiguity.

### Trap 14: Poor Practice — Getter/Setter with Same Name

```cpp
class Student {
    unsigned credits();          // getter
    unsigned credits(unsigned n); // setter — DIFFERENT semantics, BAD design
};
```

### Trap 15: Dummy `int` in Postfix Operator

```cpp
Time operator++(int);   // postfix — the 'int' is a DUMMY, never used
                        // Its only purpose is to create a different signature
                        // from the prefix version: Time& operator++()
```

### Bonus Trap 16: `=` in Declaration vs Assignment

```cpp
int x = 5;        // Initialization (constructor), NOT operator=
x = 10;           // Assignment (operator=)

MyClass a;
MyClass b = a;    // COPY CONSTRUCTOR — initialization syntax
b = a;            // operator= — assignment
```

### Bonus Trap 17: Constness of `*this` in Operator Overloading

```cpp
class MyClass {
    int operator+(const MyClass& a) { /* modifies *this? */ }     // non-const
    int operator+(const MyClass& a) const { /* doesn't modify */ } // const — valid overload!
};
// These have DIFFERENT signatures because const on member functions IS part of the signature.
```

---

## 10. HAND-CODING DRILLS

---

### Drill 1: Overload Resolution Puzzle — `f(int, double)` vs `f(double, int)`

```cpp
#include <iostream>
using namespace std;

void f(int a, double b) { cout << "f(int, double): " << a << ", " << b << endl; }
void f(double a, int b) { cout << "f(double, int): " << a << ", " << b << endl; }

int main() {
    int i = 1;
    double d = 2.0;

    f(i, d);       // line A — which f?
    f(d, i);       // line B — which f?
    f(i, i);       // line C — which f?
    f(d, d);       // line D — which f?
    f(1, 2);       // line E — which f?
    f(1.0, 2.0);   // line F — which f?
    f(1, 2.0);     // line G — which f?
}
```

For each line, state which overload is called, or explain why it's ambiguous.

> [!success]- Show Answer
> - **Line A**: `f(int, double)` — both arguments exact match. `f(double, int)` would need int→double and double→int. Exact wins.
> - **Line B**: `f(double, int)` — both arguments exact match. Symmetric to A.
> - **Line C**: `f(int→int, double→int)` beats `f(int→double, int→int)`? Wait — 
>   - Candidate 1: `f(int, double)` — i exact match, i needs int→double conversion
>   - Candidate 2: `f(double, int)` — i needs int→double conversion, i exact match
>   - Both have one exact + one conversion → **AMBIGUITY → ERROR**
> - **Line D**: `f(double, double)` — 
>   - Candidate 1: `f(int, double)` — d needs double→int, d exact
>   - Candidate 2: `f(double, int)` — d exact, d needs double→int
>   - Symmetric → **AMBIGUITY → ERROR**
> - **Line E**: Both `1` and `2` are `int` literals → same situation as Line C → **AMBIGUITY → ERROR**
> - **Line F**: Both `1.0` and `2.0` are `double` literals → same as Line D → **AMBIGUITY → ERROR**
> - **Line G**: `1` is int (exact for first param of f1), `2.0` is double (exact for second param of f1) → `f(int, double)`
>
> **Key insight**: Lines C-F are ALL errors because the overloads are perfectly symmetric — each candidate has one exact match and one conversion requirement. The compiler cannot break the tie.

---

### Drill 2: Operator Overloading — Complex Number Class

Implement a `Complex` class with `operator+`, `operator-`, `operator*`, and `operator<<`:

```cpp
#include <iostream>
using namespace std;

class Complex {
    double real, imag;
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    // TODO: Implement these
    Complex operator+(const Complex& other) const { /* ... */ }
    Complex operator-(const Complex& other) const { /* ... */ }
    Complex operator*(const Complex& other) const { /* ... */ }
    friend ostream& operator<<(ostream& os, const Complex& c) { /* ... */ }
};

int main() {
    Complex a(3, 2), b(1, 7);
    Complex c = a + b;     // Should be (4, 9)
    Complex d = a - b;     // Should be (2, -5)
    Complex e = a * b;     // Should be (3*1 - 2*7, 3*7 + 2*1) = (-11, 23)
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "a+b = " << c << endl;
    cout << "a-b = " << d << endl;
    cout << "a*b = " << e << endl;
}
```

> [!success]- Show Answer
> ```cpp
> #include <iostream>
> using namespace std;
> 
> class Complex {
>     double real, imag;
> public:
>     Complex(double r = 0, double i = 0) : real(r), imag(i) {}
> 
>     Complex operator+(const Complex& other) const {
>         return Complex(real + other.real, imag + other.imag);
>     }
> 
>     Complex operator-(const Complex& other) const {
>         return Complex(real - other.real, imag - other.imag);
>     }
> 
>     Complex operator*(const Complex& other) const {
>         // (a+bi)(c+di) = (ac-bd) + (ad+bc)i
>         return Complex(
>             real * other.real - imag * other.imag,
>             real * other.imag + imag * other.real
>         );
>     }
> 
>     friend ostream& operator<<(ostream& os, const Complex& c) {
>         os << "(" << c.real;
>         if (c.imag >= 0) os << " + " << c.imag << "i";
>         else             os << " - " << -c.imag << "i";
>         os << ")";
>         return os;
>     }
> };
> ```
>
> **Key points**:
> - `operator+`, `operator-`, `operator*` are `const` member functions — they don't modify `*this`.
> - They return by **value** (a new `Complex`), not by reference — the result is a temporary.
> - `operator<<` must be a `friend` (or non-member) because the left operand is `ostream`, not `Complex`. It also returns `ostream&` to enable chaining (`cout << a << b`).

---

### Drill 3: Operator Overloading — Money Class with `+` and `<`

```cpp
class Money {
    long dollars;
    int  cents;
public:
    Money(long d = 0, int c = 0) : dollars(d), cents(c) { normalize(); }

    void normalize() {
        if (cents >= 100) { dollars += cents / 100; cents %= 100; }
        if (cents < 0)    { dollars -= 1 + (-cents) / 100; cents = 100 - (-cents) % 100; }
    }

    // TODO: Implement operator+, operator<, operator==, operator<<
    Money operator+(const Money& m) const { /* ... */ }
    bool operator<(const Money& m) const { /* ... */ }
    bool operator==(const Money& m) const { /* ... */ }
    friend ostream& operator<<(ostream& os, const Money& m) { /* ... */ }
};

int main() {
    Money m1(10, 50), m2(5, 75), m3(16, 25);
    cout << (m1 + m2) << endl;       // $16.25
    cout << ((m1 + m2) == m3) << endl; // 1 (true)
    cout << (m1 < m2) << endl;       // 0 (false — 10.50 > 5.75)
    cout << (m2 < m1) << endl;       // 1 (true — 5.75 < 10.50)
}
```

> [!success]- Show Answer
> ```cpp
> class Money {
>     long dollars;
>     int  cents;
> public:
>     Money(long d = 0, int c = 0) : dollars(d), cents(c) { normalize(); }
> 
>     void normalize() {
>         if (cents >= 100) { dollars += cents / 100; cents %= 100; }
>         if (cents < 0)    { dollars -= 1 + (-cents) / 100; cents = 100 - (-cents) % 100; }
>     }
> 
>     Money operator+(const Money& m) const {
>         return Money(dollars + m.dollars, cents + m.cents);
>     }
> 
>     bool operator<(const Money& m) const {
>         if (dollars != m.dollars) return dollars < m.dollars;
>         return cents < m.cents;
>     }
> 
>     bool operator==(const Money& m) const {
>         return dollars == m.dollars && cents == m.cents;
>     }
> 
>     friend ostream& operator<<(ostream& os, const Money& m) {
>         os << "$" << m.dollars << ".";
>         if (m.cents < 10) os << "0";
>         os << m.cents;
>         return os;
>     }
> };
> ```
>
> **Key points**:
> - `operator==`, `operator<` return `bool`.
> - `operator+` delegates to the constructor which normalizes automatically.
> - Comparison operators (`<`, `==`) check `dollars` first, then `cents` — efficient short-circuit.

---

### Drill 4: Assignment Operator Pattern — Deep Copy for Dynamic Array

Complete the `Transcript` class with proper copy constructor and assignment operator:

```cpp
#include <iostream>
#include <string>
using namespace std;

class Transcript {
    const static int MAXCOURSE = 100;
    string* courses;
    unsigned count;
public:
    Transcript() : courses(new string[MAXCOURSE]), count(0) {}
    ~Transcript() { delete[] courses; }

    // TODO: Implement these
    Transcript(const Transcript& T) { /* ... */ }
    Transcript& operator=(const Transcript& T) { /* ... */ }
    void addCourse(const string& name) { if (count < MAXCOURSE) courses[count++] = name; }
    void print() const {
        cout << "Courses (" << count << "): ";
        for (unsigned i = 0; i < count; i++) cout << courses[i] << " ";
        cout << endl;
    }
};

int main() {
    Transcript t1;
    t1.addCourse("CS101"); t1.addCourse("MATH201");

    Transcript t2 = t1;        // copy constructor
    Transcript t3;
    t3.addCourse("PHYS101");
    t3 = t1;                   // assignment operator — overwrites existing PHYS101

    t1.print();  // Courses (2): CS101 MATH201
    t2.print();  // Courses (2): CS101 MATH201
    t3.print();  // Courses (2): CS101 MATH201

    t1 = t1;     // self-assignment — must not crash!
    t1.print();  // Courses (2): CS101 MATH201
}
```

> [!success]- Show Answer
> ```cpp
> Transcript::Transcript(const Transcript& T) {
>     count = T.count;
>     courses = new string[MAXCOURSE];
>     for (unsigned i = 0; i < count; i++)
>         courses[i] = T.courses[i];
> }
> 
> Transcript& Transcript::operator=(const Transcript& T) {
>     if (this != &T) {                     // Self-assignment check
>         delete[] courses;                 // Free old memory
>         courses = new string[MAXCOURSE];  // Allocate new
>         count = T.count;
>         for (int i = 0; i < count; i++)
>             courses[i] = T.courses[i];
>     }
>     return *this;
> }
> ```
>
> **Key differences between copy constructor and assignment**:
> - Copy constructor: NO self-assignment check (new object), NO `delete[]` (nothing to free), NO `return *this`.
> - Assignment: MUST check `this != &T`, MUST free old resources first (`delete[]`), MUST return `*this` by reference.

---

### Drill 5: Prefix vs Postfix — Time Class Increment

```cpp
#include <iostream>
using namespace std;

class Time {
    int hours, minutes, seconds;
    void normalize() {
        if (seconds >= 60) { minutes += seconds / 60; seconds %= 60; }
        if (minutes >= 60) { hours += minutes / 60; minutes %= 60; }
        hours %= 24;
    }
public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) { normalize(); }

    // TODO: Implement prefix ++ and postfix ++
    Time& operator++() { /* ... */ }
    Time operator++(int) { /* ... */ }

    void print() const { cout << hours << ":" << minutes << ":" << seconds << endl; }
};

int main() {
    Time t(23, 59, 50);
    Time old = t++;
    old.print();  // 23:59:50 — old value
    t.print();    // 23:59:51

    ++t;
    t.print();    // 23:59:52

    ++(++t);
    t.print();    // 23:59:54 — double prefix works (returns reference)

    Time t2(23, 59, 59);
    t2++;
    t2.print();   // 0:0:0 — wraparound at midnight
}
```

> [!success]- Show Answer
> ```cpp
> Time& Time::operator++() {
>     seconds++;
>     normalize();
>     return *this;
> }
> 
> Time Time::operator++(int) {
>     Time old = *this;
>     ++(*this);          // reuse prefix operator
>     return old;
> }
> ```
>
> **Key points**:
> - Prefix (`++t`): `Time& operator++()` — returns reference to modified `*this`. Enables `++(++t)`.
> - Postfix (`t++`): `Time operator++(int)` — returns by value (the old state). The `int` parameter is never used — it exists ONLY to distinguish from prefix.
> - Best practice: implement postfix by calling prefix — avoids duplicating the increment logic.

---

### Drill 6: Coercion Scenarios — Which Overload?

```cpp
#include <iostream>
using namespace std;

void display(int x)    { cout << "display(int): "    << x << endl; }
void display(float x)  { cout << "display(float): "  << x << endl; }
void display(double x) { cout << "display(double): " << x << endl; }

void func(long a, float b)  { cout << "func(long, float)" << endl; }
void func(int a, double b)  { cout << "func(int, double)" << endl; }

int main() {
    char c = 'A';
    short s = 10;
    int i = 42;
    float f = 3.14f;
    double d = 2.718;
    long l = 100L;

    display(c);       // line A
    display(s);       // line B
    display(i);       // line C
    display(f);       // line D
    display(d);       // line E
    display(l);       // line F

    func(i, f);       // line G
    func(l, d);       // line H
}
```

For each line, identify which overload is called (or if it's ambiguous), and explain why.

> [!success]- Show Answer
> - **Line A** `display(c)`: `char` promotes to `int` (best match) → `display(int)`. Could also convert to `float` or `double`, but promotion to `int` is better than conversion to `float`.
> - **Line B** `display(s)`: `short` promotes to `int` → `display(int)`. Same reasoning.
> - **Line C** `display(i)`: `int` exact match → `display(int)`.
> - **Line D** `display(f)`: `float` exact match → `display(float)`.
> - **Line E** `display(d)`: `double` exact match → `display(double)`.
> - **Line F** `display(l)`: `long` — no exact `long` overload. `long → int` is a conversion (possible data loss), `long → float` and `long → double` are also conversions. `long → float` and `long → double` are **floating-integral conversions**, `long → int` is an **integral conversion**. Neither is strictly better → **AMBIGUITY → ERROR**.
> - **Line G** `func(i, f)`: `func(int, double)` — i exact match, f needs float→double promotion. `func(long, float)` — int→long conversion, f exact match. Exact + promotion beats exact + conversion → `func(int, double)` wins.
> - **Line H** `func(l, d)`: `func(long, float)` — l exact, d needs double→float conversion. `func(int, double)` — l needs long→int conversion, d exact. Both have one exact + one conversion → **AMBIGUITY → ERROR**.

---

### Drill 7: Constructor Overloading — Complete the Figure/Point Class

Expand the `Figure` class with additional constructors and trace which constructor is called in each case:

```cpp
#include <iostream>
#include <string>
using namespace std;

class Point {
public:
    int x, y;
    Point(int xx = 0, int yy = 0) : x(xx), y(yy) {
        cout << "  Point(" << x << ", " << y << ") constructed" << endl;
    }
};

class Figure {
    string name;
    Point* vertices;
    int vertexCount;
public:
    Figure() : name("Empty"), vertices(nullptr), vertexCount(0) {
        cout << "Figure() — default" << endl;
    }
    Figure(const string& n) : name(n), vertices(nullptr), vertexCount(0) {
        cout << "Figure(string) — named: " << name << endl;
    }
    Figure(const Point& center) : name("Centered"), vertices(new Point[1]), vertexCount(1) {
        vertices[0] = center;
        cout << "Figure(Point) — center-based" << endl;
    }
    Figure(const Point verts[], int count) : name("Polygon"), vertices(new Point[count]), vertexCount(count) {
        for (int i = 0; i < count; i++) vertices[i] = verts[i];
        cout << "Figure(Point[], int) — " << count << " vertices" << endl;
    }
    ~Figure() { delete[] vertices; }
};

int main() {
    // TODO: For each line below, write which constructor is called
    // and whether a Figure or Point constructor runs at each step.

    Figure f1;                                           // line 1
    Figure f2("Triangle");                               // line 2
    Point p(10, 20);                                     // line 3
    Figure f3(p);                                        // line 4

    Point verts[3];                                      // line 5
    Figure f4(verts, 3);                                 // line 6

    const int N = 3;
    Point arr[N] = { Point(1,2), Point(3,4), Point(5,6) }; // line 7
    Figure f5(arr, N);                                   // line 8

    Figure f6 = f2;                                      // line 9 — what constructor is this?
}
```

Trace all constructor calls and identify what happens at line 9 (is it copy constructor or assignment?).

> [!success]- Show Answer
> **Line 1** `Figure f1;`:
> - Calls `Figure()` — default constructor.
> - Output: `Figure() — default`
>
> **Line 2** `Figure f2("Triangle");`:
> - Calls `Figure(const string&)` — string constructor.
> - Output: `Figure(string) — named: Triangle`
>
> **Line 3** `Point p(10, 20);`:
> - Calls `Point(int, int)` — two-argument constructor.
> - Output: `Point(10, 20) constructed`
>
> **Line 4** `Figure f3(p);`:
> - Calls `Figure(const Point&)` — center-based constructor.
> - Output: `Figure(Point) — center-based`
>
> **Line 5** `Point verts[3];`:
> - Calls `Point()` (default constructor) **3 times** — once per array element.
> - Output: `Point(0, 0) constructed` three times
>
> **Line 6** `Figure f4(verts, 3);`:
> - Calls `Figure(const Point[], int)` — array + count constructor.
> - Output: `Figure(Point[], int) — 3 vertices`
>
> **Line 7** `Point arr[N] = { Point(1,2), Point(3,4), Point(5,6) };`:
> - Calls `Point(int, int)` three times (once per initializer).
> - Output: `Point(1, 2) constructed`, `Point(3, 4) constructed`, `Point(5, 6) constructed`
>
> **Line 8** `Figure f5(arr, N);`:
> - Calls `Figure(const Point[], int)` — array + count constructor.
> - Output: `Figure(Point[], int) — 3 vertices`
>
> **Line 9** `Figure f6 = f2;`:
> - This is a **COPY CONSTRUCTOR** call, NOT assignment. `f6` is being declared and initialized in the same line. The `=` here is initialization syntax.
> - Since we didn't define a copy constructor, the compiler generates a **default copy constructor** (shallow copy). This is **dangerous** — it copies the pointer `vertices` instead of doing a deep copy. When both `f2` and `f6` go out of scope, the destructors will try to `delete[]` the same pointer twice → **double-free / undefined behavior**.
>
> **Full output order**:
> ```
> Figure() — default
> Figure(string) — named: Triangle
>   Point(10, 20) constructed
> Figure(Point) — center-based
>   Point(0, 0) constructed
>   Point(0, 0) constructed
>   Point(0, 0) constructed
> Figure(Point[], int) — 3 vertices
>   Point(1, 2) constructed
>   Point(3, 4) constructed
>   Point(5, 6) constructed
> Figure(Point[], int) — 3 vertices
> ```
>
> **Line 9 trap**: `Figure f6 = f2;` is **copy construction**, not assignment. Without a user-defined copy constructor, the compiler-generated one does a **shallow copy**, sharing the `vertices` pointer → double-delete at destruction. This highlights why classes with dynamic memory MUST define their own copy constructor (the **Rule of Three**).

---

### Drill 8: Comprehensive Overload Resolution — Multiple Candidates

```cpp
#include <iostream>
using namespace std;

void foo(int a, int b)          { cout << "foo(int, int)" << endl; }
void foo(int a, double b)       { cout << "foo(int, double)" << endl; }
void foo(double a, int b)       { cout << "foo(double, int)" << endl; }
void foo(double a, double b)    { cout << "foo(double, double)" << endl; }

int main() {
    int    i = 1;
    float  f = 2.5f;
    double d = 3.0;
    char   c = 'A';

    foo(i, i);   // A
    foo(i, d);   // B
    foo(d, i);   // C
    foo(d, d);   // D
    foo(i, c);   // E
    foo(f, f);   // F
    foo(c, c);   // G
    foo(i, f);   // H
    foo(f, d);   // I
}
```

> [!success]- Show Answer
> - **A**: `foo(int, int)` — both exact match → `foo(int, int)`
> - **B**: `foo(int, double)` — i exact match, d exact match → `foo(int, double)`
> - **C**: `foo(double, int)` — d exact match, i exact match → `foo(double, int)`
> - **D**: `foo(double, double)` — both exact match → `foo(double, double)`
> - **E**: `foo(int, c)` — i exact match. c is `char`:
>   - `foo(int, int)` — c: char→int (promotion)
>   - `foo(int, double)` — c: char→double (promotion... but int promotion is better)
>   - Note: `char → int` is promotion, `char → double` is a longer conversion. `foo(int, int)` wins.
> - **F**: `foo(f, f)` — both `float`:
>   - `foo(int, int)` — both need float→int (conversion)
>   - `foo(int, double)` — float→int, float→double (conversion + promotion)
>   - `foo(double, int)` — float→double, float→int (promotion + conversion)
>   - `foo(double, double)` — both float→double (promotion)
>   - `foo(double, double)` is **best** (two promotions) beats mixed conversion+promotion or two conversions → `foo(double, double)`
> - **G**: `foo(c, c)` — both `char`:
>   - `foo(int, int)` — both char→int (promotion) → best: two promotions
>   - Others have conversion + promotion or longer chains → `foo(int, int)` wins.
> - **H**: `foo(i, f)` — i is int exact, f is float:
>   - `foo(int, int)` — f: float→int (conversion)
>   - `foo(int, double)` — f: float→double (promotion)
>   - `foo(int, double)` wins (promotion beats conversion for the float arg) → `foo(int, double)`
> - **I**: `foo(f, d)` — f is float, d is double:
>   - `foo(int, double)` — f: float→int (conversion), d exact
>   - `foo(double, double)` — f: float→double (promotion), d exact
>   - `foo(double, double)` wins → `foo(double, double)`

---

> [!NOTE]
> This study guide covers all lecture content for Lec10: Overloading. Master the distinction between overloading (compile-time, different signatures) and overriding (runtime, same signatures, virtual). Memorize the four forbidden operators (`.`, `.*`, `::`, `?:`), the prefix/postfix `++` signature difference, the assignment operator self-assignment pattern, and the copy-ctor-vs-assignment distinction. Practice overload resolution drills until you can predict the compiler's choice without hesitation.
