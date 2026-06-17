# Lec6: Objects and Classes in C++ — Study Guide

---

## 1. CONCEPT CARD: Class Definition & Object Lifecycle in C++

### 1.1 What It Is

In C++, a **class** is a user-defined type that bundles **data members** (the state/attributes) and **member functions** (the behavior/operations) into a single named unit. The syntax is:

```
class class_name { Member_List };
```

Where `Member_List` consists of `MemberVariables | MemberFunctions`. From this template you create **objects** (instances) by declaring a variable of that class type: `class_name identifier;`

> [!success]- Show Answer — Class Definition Formal Syntax
> > ```
> > class class_name { Member_List };  // Class
> > class_name identifier;              // Object
> > Member_List ::= MemberVariables | MemberFunctions
> > ```

### 1.2 What Problem It Solves

Before classes in C, you managed related data with structs but functions lived separately. If you needed a `Point` with x,y coordinates, you wrote a struct and standalone functions like `getX(Point* p)`. There was no enforcement that only approved functions manipulate the data.

Classes solve:
- **Bundling** — data and the functions that operate on it live inside one boundary
- **Access control** — you declare what outsiders can touch (public) vs. what's internal (private)
- **Automatic lifecycle** — constructors and destructors handle initialization and cleanup
- **Copy semantics** — you control how objects are duplicated (deep vs. shallow)
- **Type safety** — the compiler enforces who can call what on which object

> [!success]- Show Answer — Struct vs. Class: practical difference
> > In C++, `struct` and `class` are nearly identical. The ONLY difference: `struct` defaults to `public` access, `class` defaults to `private`. By convention, `struct` is used for passive data bags, `class` for encapsulated types with invariants.

### 1.3 How It Works (step by step)

1. You **define** a class listing private data members and public member functions.
2. The **compiler** allocates memory for the class's vtable and code; no data memory yet.
3. When you **declare** an object (e.g., `Point p;`), the constructor runs, allocating per-object memory for data members.
4. Each object gets its **own copy** of every data member (non-static). All objects **share** one copy of the member function code.
5. The **access labels** (public/private/protected) are enforced at compile time — not runtime.
6. When an object goes out of scope (stack) or is `delete`d (heap), the **destructor** runs.
7. The object's memory is reclaimed; its identity ceases to exist.

> [!success]- Show Answer — Lifecycle Trace
> > ```
> > class definition → compiler records layout
> >                        ↓
> > constructor call → memory allocated, members initialized → object BORN
> >                        ↓
> > member function calls → messages received, state modified
> >                        ↓
> > destructor call → cleanup, memory freed → object DEAD
> > ```

### 1.4 Concrete Example (Transcript class for university registration)

```cpp
class Transcript {
private:
    char studentID[20];
    char courseCode[20];
    float grade;
    int credits;
public:
    Transcript(const char* sid, const char* cc, float g, int cr);
    float getGrade() const;
    int getCredits() const;
    void setGrade(float newGrade);
    float calculateGradePoint() const;
};
```

A university creates a `Transcript` object for each student-course pairing. Each transcript holds its own `grade`, `studentID`, etc. The `calculateGradePoint()` method code is written once but executes on each transcript independently. The `setGrade()` method provides controlled mutation — the professor cannot directly write `transcript.grade = 4.0;` because `grade` is private.

> [!success]- Show Answer — Trace: what happens with `Transcript t("A123", "CS101", 3.5, 4);`?
> > 1. Constructor runs: copies "A123" into `studentID`, "CS101" into `courseCode`, stores `grade=3.5`, `credits=4`.
> > 2. Object `t` now exists with its own copy of all four data members.
> > 3. Code for `getGrade()`, `getCredits()`, `setGrade()`, `calculateGradePoint()` is shared with all other Transcript objects.
> > 4. Only `public` members are callable from outside — `t.getGrade()` works; direct `t.grade` is a compile error.

### 1.5 What It Is NOT

- **NOT automatically memory-safe like Java/C#.** C++ gives you raw pointers, manual `new`/`delete`, and no garbage collector. Forgetting `delete` leaks memory; calling `delete` twice crashes.
- **NOT providing automatic deep copy.** The compiler-generated copy constructor does a **shallow copy** — if your class has pointers to dynamic memory, both objects will point to the same memory. This is the **Rule of Three** problem: if you need a destructor, copy constructor, or assignment operator, you likely need all three.
- **NOT equivalent to a C struct.** A struct in C has no member functions, no access control, no constructors, no destructors.
- **NOT the same as an object.** The class is the blueprint; the object is the instance. Many students confuse `Point` (the class) with `Point p` (the object).

> [!success]- Show Answer — The Rule of Three
> > If your class needs any one of: destructor, copy constructor, or copy assignment operator, it almost certainly needs ALL THREE. The compiler-generated versions do shallow copies, which are disastrous when you own dynamic memory.

---

## 2. CLASS DEFINITION SYNTAX

### 2.1 Basic Structure

```
class class_name { Member_List };
```

- `Member_List` consists of zero or more member variables and member functions
- `class_name identifier;` creates an object (an instance) of that class
- The **semicolon** after the closing brace is MANDATORY

> [!success]- Show Answer — Minimum valid class
> > ```cpp
> > class Empty { };
> > // Class with no members — still valid C++. Takes 1 byte.
> > ```

### 2.2 The Point Class Example (FULL from lecture)

```cpp
class Point {
private:
    int x, y;  // coordinates — hidden from outsiders
public:
    Point(int xVal = 0, int yVal = 0) { x = xVal; y = yVal; }
    int getX() { return x; }
    int getY() { return y; }
};
```

This is `Lec6_ex1-Point.cpp` from the lecture. Key observations:
- `x` and `y` are `private` — no outside code can read or write them directly.
- `Point(int xVal = 0, int yVal = 0)` is a constructor with default parameter values. This makes `Point p;` valid (defaults to `Point(0,0)`).
- `getX()` and `getY()` are `public` — they form the read-only access interface.
- No setter methods — this Point is immutable after construction (no `setX`/`setY`).

> [!success]- Show Answer — Trace: `Point p(5,10); cout << p.getX();`
> > 1. Constructor `Point(5,10)` runs: `x = 5`, `y = 10`.
> > 2. `p.getX()` calls the public method.
> > 3. The method returns `p.x` which is `5`.
> > 4. Prints `5`.
> > 5. Direct `p.x` would be a compile error — `x` is private.

### 2.3 Member Functions

A **member function** (also called a **method**) is a function whose definition or prototype appears within the class definition.

Critical rule: **Function code is SHARED among all objects; data members are NOT shared.**

```
Point P(5,10);   // P has own x=5, y=10
Point Q(20,10);  // Q has own x=20, y=10
Point R(50,60);  // R has own x=50, y=60

// In memory:
// P: [x=5][y=10]  ——+
// Q: [x=20][y=10] ——+——→ shared code: getX() { return x; }, getY() { return y; }
// R: [x=50][y=60] ——+
//
// Each object stores its own x,y. The getX/getY code exists ONCE.
```

> [!success]- Show Answer — Why is code shared?
> > Memory efficiency. If you have 10,000 Point objects, you don't want 10,000 copies of `getX()` in RAM. The compiler generates one copy of each member function. At call time, the object's address is implicitly passed (via the `this` pointer) so the function knows which object's data to access.

> [!success]- Show Answer — static data members are the exception
> > A `static` data member IS shared among all objects. It belongs to the class, not any particular instance. Only one copy exists regardless of how many objects are created.

### 2.4 Inline Functions

Three styles in C++:

| Style | Location of Definition | inline? |
|---|---|---|
| **In-line** | Inside the class body | Implicitly inline |
| **Out-of-line** | Outside the class body | NOT inline (unless `inline` keyword added) |
| **Out-of-line + inline** | Outside the class body with `inline` keyword | Explicitly inline |

Lecture example:

```cpp
class Point {
    ...
public:
    void setX(int valX) { x = valX; }   // In-line: defined INSIDE class → implicitly inline
    void setY(int valY);                  // Out-of-line: only DECLARED here
    void delta(int dx, int dy);           // Out-of-line: only DECLARED here
};

void Point::setY(int valY) {            // Out-of-line definition
    y = valY;
}

inline void Point::delta(int dx, int dy) {  // Out-of-line + inline keyword
    x += dx;
    y += dy;
}
```

> [!success]- Show Answer — Omitting return type in out-of-line — why bad
> > The lecture mentions "Omitting the name is allowed but don't do it." For out-of-line definitions, you MUST include the return type. For in-line definitions, the return type is still required — the lecture slide is likely referring to something else or contains an artifact. Always write the full return type.

> [!success]- Show Answer — inline is a suggestion, not a command
> > The compiler decides whether to actually inline. `inline` is a hint that you'd prefer the function body to be inserted at the call site (avoiding function call overhead). The compiler may ignore it. Modern compilers inline aggressively on their own with optimization flags.

> [!success]- Show Answer — When MUST you use out-of-line?
> > When the function definition depends on types or classes not yet fully defined at the point of the class definition (forward declaration scenarios), or when you want to separate interface (.h) from implementation (.cpp).

### 2.5 Constant Member Functions

A `const` member function **guarantees** that the current object's state is NOT modified.

**Syntax:** `const` goes AFTER the parameter list:

```cpp
class Point {
public:
    int getX() const { return x; }   // const: will NOT modify this object
    int getY() const { return y; }   // const: will NOT modify this object
};
```

Key rules:
- Only `const` member functions can be called on `const` objects.
- A `const` member function cannot modify ANY data member (non-static).
- A `const` member function cannot call non-`const` member functions on the same object.
- Lecture reference: `Lec6_ex4_ConstantMember_Function.cpp`

> [!success]- Show Answer — const object, non-const method = compile error
> > ```cpp
> > const Point p(5, 10);
> > p.getX();        // OK: getX() is const
> > p.setX(20);      // ERROR: setX() is NOT const, can't call on const object
> > ```

> [!success]- Show Answer — mutable keyword exception
> > A data member declared `mutable` CAN be modified inside a `const` member function. This is for cached values, reference counts, mutexes — metadata that doesn't change the object's logical state.

---

## 3. MEMBER ACCESS CONTROL

### 3.1 The Three Modifiers

```cpp
class class_name {
public:      // accessible from anywhere
protected:   // accessible from this class and derived classes
private:     // accessible ONLY from this class (DEFAULT in class)
};
```

> [!success]- Show Answer — Default access level
> > In a `class`, members are `private` by default until a different access label is encountered. In a `struct`, members are `public` by default.

### 3.2 Access Rules Table

| Type of Member | Member of Same Class | Friend | Member of Derived Class | Non-Member Function |
|---|---|---|---|---|
| Private (Default) | X | X | — | — |
| Protected | X | X | X | — |
| Public | X | X | X | X |

- **X** = access is ALLOWED
- **—** = access is DENIED
- A `friend` is NOT a member — it is an external entity granted special access.

> [!success]- Show Answer — Access is per-CLASS, not per-OBJECT
> > A member function of `Point` can access private members of ANY `Point` object passed to it — not just `this`. Two objects of the same class can touch each other's private data:
> > ```cpp
> > class Point {
> > private: int x, y;
> > public:
> >     void copyFrom(const Point& other) { x = other.x; y = other.y; } // OK!
> > };
> > ```

### 3.3 Practical Rules

- **Public members:** accessed with the `.` dot operator — `p.getX();`
- **Private/Protected members from outside:** ABSOLUTELY NO ACCESS. `p.x` is a compile error if `x` is private.

> [!success]- Show Answer — Common misconception
> > "If I have a pointer, can I bypass private?" NO. Access control is enforced at compile time. Even with raw pointers and casts, undefined behavior is the result — the compiler assumes you follow the rules.

### 3.4 Point Example ex2 (public y, private x)

```cpp
class Point {
private:
    int x;
public:
    int y;
    int getX() { return x; }
    int getY() { return y; }
    void setX(int xVal) { x = xVal; }
    void setY(int yVal) { y = yVal; }
};

Point p;
p.setX(300);
p.setY(500);
cout << "x = " << p.getX() << endl;   // works: getX() is public
cout << "y = " << p.y << endl;         // works: y is public
// p.x = 300;                          // ERROR: x is private
```

This is `Lec6_ex2-Point.cpp` from the lecture. Printed values: `x = 300`, `y = 500`.

> [!success]- Show Answer — Why would anyone make y public?
> > Bad practice in general, but the lecture uses it to demonstrate the contrast. Making `y` public means anyone can write `p.y = -999;` with no validation. Making it private with a setter allows validation: `void setY(int val) { if (val >= 0) y = val; }`.

### 3.5 Friend Class

A **friend class** has full access to ALL members (private AND protected) of the granting class.

**Syntax:** `friend class B;` inside class A's definition.

Full example from `Lec6_ex3_FriendClass.cpp`:

```cpp
#include <iostream>

class A {
private:
    int a;
public:
    A() { a = 10; }
    void seta(int value);
    friend class B;      // B is now a friend of A
};

void A::seta(int value) { a = value; }

class B {
private:
    int b;
public:
    void showA(A& x) {
        std::cout << "A::a=" << x.a;   // B accesses A's PRIVATE member a
    }
};

int main() {
    A a;
    B b;
    a.seta(15);
    b.showA(a);   // prints: A::a=15
    return 0;
}
```

> [!success]- Show Answer — Friendship is NOT symmetric
> > `friend class B` inside `A` means B can access A's members. It does NOT mean A can access B's members. If A also needs access to B, B must separately declare `friend class A`.

> [!success]- Show Answer — Friendship is NOT transitive
> > If A friends B, and B friends C, then C is NOT a friend of A. Each friendship is independently granted.

> [!success]- Show Answer — Friendship is NOT inheritable
> > If A friends B, and `class D : public B {}`, then D is NOT a friend of A. Derived classes do not inherit friendship.

> [!success]- Show Answer — Friend functions
> > You can also declare individual functions as friends: `friend void foo(A& a);` — grants that specific function access to A's private members.

---

## 4. CONSTRUCTORS

### 4.1 Purpose

A **constructor** is called to CREATE an object. It initializes the object's data members and establishes its initial state. Declared with: `classname(...);`

Key characteristics:
- Same name as the class
- NO return type (not even `void`)
- Called automatically when an object is created — you NEVER call it explicitly on an existing object
- Can be overloaded (multiple constructors with different parameter lists)

> [!success]- Show Answer — Can a constructor fail?
> > A constructor CANNOT return an error value. If initialization fails, the only standard way to signal it is to throw an exception. The destructor will NOT be called for a partially-constructed object if the constructor throws.

### 4.2 Types

| Type | Description | Example |
|---|---|---|
| **Default constructor** | No parameters (or all parameters have defaults) | `Point()` or `Point(int x=0, int y=0)` |
| **Alternate (parameterized) constructor** | Takes parameters | `Point(int x, int y)` |
| **Overloaded constructors** | Multiple constructors with different parameter lists | `Point()` and `Point(int, int)` coexist |
| **Copy constructor** | Initializes with another object of the same class | `Point(const Point& other)` |

> [!success]- Show Answer — Default constructor with all-default parameters
> > `Point(int xVal = 0, int yVal = 0)` acts as BOTH a default constructor AND a parameterized constructor. `Point p;` calls it with defaults, `Point p(5,10);` calls it with explicit values. But be careful: if you add another constructor like `Point(int xVal)`, you risk ambiguity when calling `Point p;`.

### 4.3 Copy Constructor

Creates an object by initializing it with an object of the SAME class that was previously created.

**Syntax:** `ClassName(const ClassName& other);`

- The parameter MUST be a reference (not by value — that would cause infinite recursion)
- The parameter SHOULD be `const` (you're copying, not modifying the source)
- If you do NOT define a copy constructor, the **compiler generates one** that does a **SHALLOW copy** (member-by-member copy of values/pointers)

> [!success]- Show Answer — When does the compiler NOT generate a copy constructor?
> > In modern C++, the compiler may implicitly delete the copy constructor if: a member has a deleted copy constructor, a member is a move-only type, or a base class has a private/inaccessible copy constructor.

### 4.4 Examples of Constructor Calls

```cpp
Point p;                          // default constructor
Point a(p), b = p;                // copy constructor (both syntaxes)
Point c(20, 30);                  // alternate (parameterized) constructor
Point figure[3];                  // default constructor called 3 times
Point figure[2] = {p, c};        // copy constructor called twice
```

> [!success]- Show Answer — `Point b = p;` — does this call the copy constructor?
> > YES. Despite the `=` sign, this is initialization, NOT assignment. `Point b = p;` calls the copy constructor because `b` is being created. This is different from:
> > ```cpp
> > Point b;      // default constructor
> > b = p;        // ASSIGNMENT OPERATOR (not copy constructor) — different!
> > ```

> [!success]- Show Answer — All situations that invoke the copy constructor
> > 1. `ClassName a(b);` — direct initialization
> > 2. `ClassName a = b;` — copy initialization
> > 3. Passing object by value to a function: `void foo(ClassName obj);`
> > 4. Returning object by value from a function: `ClassName bar() { ClassName c; return c; }`

---

## 5. POINTERS TO OBJECTS & DESTRUCTORS

### 5.1 Pointers to Class Objects

```cpp
Student *p;                    // pointer declaration — no object yet
p = new Student;               // dynamic allocation — constructor called
if (!p)                        // check if allocation failed (null pointer)
    // could not create Student

Point *figure = new Point[10]; // array of 10 Points — default ctor called 10 times
```

> [!success]- Show Answer — `if (!p)` in modern C++
> > By default, `new` throws `std::bad_alloc` on failure rather than returning `nullptr`. The `if (!p)` check expects the `nothrow` version: `p = new(std::nothrow) Student;`

> [!success]- Show Answer — Static vs. Dynamic pointers
> > ```cpp
> > Point p(5, 10);           // static: object on stack
> > Point* pp = &p;           // pointer to static object — NO delete needed for pp
> > Point* dp = new Point;    // dynamic: object on heap — MUST delete dp
> > ```

### 5.2 Destructors

Called when an object is to be **deleted/destroyed**. Performs cleanup — freeing dynamic memory, closing files, releasing resources.

**Declaration:** `~classname();` — NO parameters, NO return type.

```cpp
class Point {
public:
    ~Point() { cout << "Destructor called." << endl; }
};
```

- Only ONE destructor per class (cannot be overloaded — no parameters means no signature to distinguish)
- Destructor is called automatically when:
  - Stack object goes out of scope
  - `delete` is called on a heap object
  - `delete[]` is called on a heap array of objects
  - Temporary object's lifetime ends

> [!success]- Show Answer — Destructor execution order within a destructor body
> > 1. Destructor body executes (your code in `~ClassName() { ... }`)
> > 2. Member objects' destructors run (in reverse declaration order)
> > 3. Base class destructor runs (in inheritance cases)

> [!success]- Show Answer — Virtual destructor
> > If your class is meant to be a base class, declare the destructor `virtual`. Without it, deleting a derived object through a base-class pointer calls only the base destructor — leaking derived resources. More on this in Lec7/Lec8.

---

## 6. DEEP COPY vs SHALLOW COPY (CRITICAL)

### 6.1 Definitions from Lecture

| Type | Mechanism | Memory Diagram |
|---|---|---|
| **Deep copy** | Copies the CONTENTS of the data | Two independent blocks of memory |
| **Shallow copy** | Copies the POINTER (address) | Two pointers to the SAME memory |

```cpp
// SHALLOW copy — copies the pointer, NOT the data
char name[] = "John Smith";
char *cp = name;               // cp points to the SAME array as name

// DEEP copy — copies the actual data
char name[] = "John Smith";
char *cp = new char[30];
strcpy(cp, name);              // cp has its OWN copy of the characters
```

> [!success]- Show Answer — Shallow copy visual
> > ```
> > Shallow:   name ──→ ['J']['o']['h']['n'][' ']['S']['m']['i']['t']['h']['\0']
> >            cp   ──→  (same memory)
> >
> > Deep:      name ──→ ['J']['o']['h']['n'][' ']['S']['m']['i']['t']['h']['\0']
> >            cp   ──→ ['J']['o']['h']['n'][' ']['S']['m']['i']['t']['h']['\0']  (separate copy)
> > ```

### 6.2 The Student Copy Problem (FULL lecture example)

```cpp
#include <string>

class Course {
private:
    string name;
public:
    Course() {}
    Course(const string& cname);
};

class Student {
private:
    Course *coursesTaken;
    unsigned numCourses;
public:
    Student(unsigned nCourses);
    ~Student();
};

Student::Student(unsigned nCourses) {
    coursesTaken = new Course[nCourses];
    numCourses = nCourses;
}

Student::~Student() {
    delete[] coursesTaken;
}
```

**THE BUG:**

```cpp
int nCourses = 7;
Student x(nCourses);   // Constructor: allocates array of 7 Courses → x.coursesTaken
Student y(x);          // Copy constructor: COMPILER-GENERATED → shallow copy!
```

**What happens:**
- The compiler-generated copy constructor does a **shallow copy** of `coursesTaken` (just copies the pointer address, NOT the array contents).
- Both `x.coursesTaken` and `y.coursesTaken` point to the **SAME array of Course objects**.
- When `x`'s destructor runs, it calls `delete[] coursesTaken` — array is freed.
- When `y`'s destructor runs, it calls `delete[] coursesTaken` on the **SAME already-freed memory**.
- **DOUBLE DELETE → CRASH / undefined behavior.**

> [!success]- Show Answer — Memory diagram of the bug
> > ```
> > After Student x(7):
> >   x.coursesTaken ──→ [Course0][Course1][Course2][Course3][Course4][Course5][Course6]
> >
> > After Student y(x):  (shallow copy!)
> >   x.coursesTaken ──→ [Course0][Course1][Course2][Course3][Course4][Course5][Course6]
> >   y.coursesTaken ──→ (same array!)
> >
> > After ~x():
> >   array is DELETED — both pointers now DANGLING
> >
> > After ~y():
> >   delete[] on DANGLING pointer → CRASH!
> > ```

### 6.3 The Solution: Custom Copy Constructor

```cpp
Student(const Student &s) {
    numCourses = s.getNumCourses();
    coursesTaken = new Course[numCourses];    // 1. ALLOCATE a new, separate array
    for (int i = 0; i < numCourses; i++)
        coursesTaken[i] = s.getCourse(i);     // 2. COPY each Course to the new array
}
```

**Desired outcome:** `x.coursesTaken` and `y.coursesTaken` now point to **different arrays** — each with its own copy of the Course objects. Destructor on `x` deletes `x`'s array only; `y`'s array remains intact.

> [!success]- Show Answer — Memory diagram of the fix
> > ```
> > After Student x(7):
> >   x.coursesTaken ──→ [C0][C1][C2][C3][C4][C5][C6]
> >
> > After Student y(x):  (deep copy!)
> >   x.coursesTaken ──→ [C0][C1][C2][C3][C4][C5][C6]
> >   y.coursesTaken ──→ [C0][C1][C2][C3][C4][C5][C6]  (separate array!)
> >
> > After ~x(): x's array deleted. y's array still valid.
> > After ~y(): y's array deleted. No double delete.
> > ```

> [!success]- Show Answer — What about the copy assignment operator?
> > The same problem exists for assignment. If you write:
> > ```cpp
> > Student y(7);
> > Student x(5);
> > x = y;  // compiler-generated assignment operator = SHALLOW COPY!
> > ```
> > You need a custom `Student& operator=(const Student& s)` too. This is the full Rule of Three.

> [!success]- Show Answer — Required helper methods for the fix
> > ```cpp
> > unsigned getNumCourses() const { return numCourses; }
> > Course getCourse(int i) const { return coursesTaken[i]; }
> > ```

---

## 7. COMPOSITE CLASSES

### 7.1 Definition

A **composite class** is a class containing data members that are **objects of other classes**. When a class contains **instances**, **references**, or **pointers** to other classes, it is a composite class.

Examples:
- A `Circle` contains a `Point` (center)
- A `Figure` contains an array of `Points`
- A `Car` contains an `Engine`, 4 `Wheel` objects
- A `Student` record contains a `Date` (birthdate), `Address`, etc.

> [!success]- Show Answer — Composite vs. pointer-to-class member
> > ```cpp
> > class Circle {
> >     Point center;        // composite: Point IS a direct member
> >     double radius;
> > };
> >
> > class Drawing {
> >     Point* points;       // pointer to array: still composite
> >     int numPoints;
> > };
> > ```

### 7.2 Pre-defined Construction/Destruction Order

These rules are **guaranteed by the C++ standard** and CANNOT be changed:

1. **Construction order:**
   - Constructors for ALL member objects execute in the **order they appear in the class definition** (NOT the order in the initializer list!).
   - All member constructors execute **BEFORE** the body of the enclosing class constructor.

2. **Destruction order:**
   - Destructors are called in **REVERSE order** of constructors.
   - The body of the enclosing class destructor executes **BEFORE** the destructors of its member objects.

> [!success]- Show Answer — Construction order visualization
> > ```cpp
> > class Composite {
> >     MemberA a;   // declared FIRST → ctor runs FIRST
> >     MemberB b;   // declared SECOND → ctor runs SECOND
> >     MemberC c;   // declared THIRD → ctor runs THIRD
> > public:
> >     Composite() : c(1), a(2), b(3) {  // initializer list order DOES NOT MATTER
> >         // body runs AFTER all member ctors
> >     }
> >     ~Composite() {
> >         // body runs FIRST
> >     }  // then ~c(), then ~b(), then ~a() — REVERSE of declaration order
> > };
> > ```
> > Initializer list says `c, a, b` — but actual execution is `a, b, c` (declaration order).

> [!success]- Show Answer — Destructor order visualization
> > ```
> > Construction:  a() → b() → c() → Composite body
> > Destruction:   ~Composite body → ~c() → ~b() → ~a()
> > ```

> [!success]- Show Answer — Why reverse order?
> > Because later-constructed objects might depend on earlier-constructed ones. During destruction, dependencies must be torn down safely — the dependent object must still be alive when its dependency is destroyed.

### 7.3 Exercise from Lecture

The lecture asks you to **write a program to test this order**. Here's what to write:

> [!success]- Show Answer — Test program for construction/destruction order
> > ```cpp
> > #include <iostream>
> > using namespace std;
> >
> > class A {
> > public:
> >     A()  { cout << "A() "; }
> >     ~A() { cout << "~A() "; }
> > };
> >
> > class B {
> > public:
> >     B()  { cout << "B() "; }
> >     ~B() { cout << "~B() "; }
> > };
> >
> > class C {
> >     A a;  // declared FIRST
> >     B b;  // declared SECOND
> > public:
> >     C()  { cout << "C() "; }
> >     ~C() { cout << "~C() "; }
> > };
> >
> > int main() {
> >     C obj;
> >     return 0;
> > }
> > // Expected output: A() B() C() ~C() ~B() ~A()
> > ```

---

## 8. MUST-MEMORIZE SYNTAX TEMPLATES

### Template 1: Basic Class Definition with private/public

```cpp
class ClassName {
private:
    // data members — each object gets its own copy
    int data1;
    double data2;
public:
    // member functions — shared among all objects
    ClassName(int d1, double d2);
    int getData1() const;
    void setData2(double val);
};  // ← MANDATORY SEMICOLON
```

### Template 2: Inline vs. Out-of-line Member Functions

```cpp
class Point {
private:
    int x, y;
public:
    void setX(int valX) { x = valX; }         // In-line: defined INSIDE class
    void setY(int valY);                        // Out-of-line: only DECLARED here
    int getX() const { return x; }             // In-line + const
};

void Point::setY(int valY) { y = valY; }       // Out-of-line DEFINITION
```

### Template 3: const Member Function

```cpp
class Point {
    int x, y;
public:
    int getX() const { return x; }    // const AFTER parameter list
    int getY() const;                  // const in BOTH declaration AND definition
};

int Point::getY() const {             // const MUST appear in definition too
    return y;
}
```

### Template 4: Constructors (Default, Alternate, Copy)

```cpp
class Point {
    int x, y;
public:
    Point() { x = 0; y = 0; }                       // Default: no parameters
    Point(int xVal, int yVal) { x = xVal; y = yVal; } // Alternate: with parameters
    Point(const Point& other) { x = other.x; y = other.y; } // Copy constructor
};
```

### Template 5: Destructor

```cpp
class Student {
    Course* coursesTaken;
public:
    ~Student() {                   // No parameters, no return type
        delete[] coursesTaken;     // Cleanup dynamic memory
        coursesTaken = nullptr;    // Prevent dangling pointer (defensive)
    }
};
```

### Template 6: Deep Copy Constructor Pattern

```cpp
class MyClass {
    int* data;
    int size;
public:
    MyClass(int s) : size(s) {
        data = new int[size];
    }

    MyClass(const MyClass& other) {       // 1. Copy simple members
        size = other.size;
        data = new int[size];             // 2. Allocate NEW memory
        for (int i = 0; i < size; i++)    // 3. Copy each element
            data[i] = other.data[i];      // 4. (for objects, copy/move)
    }

    ~MyClass() {
        delete[] data;
    }
};
```

### Template 7: Friend Class Declaration

```cpp
class A {
private:
    int secret;
public:
    A() : secret(42) {}
    friend class B;    // B has FULL access to ALL A members
};

class B {
public:
    void reveal(A& a) {
        cout << a.secret;  // accessing A's PRIVATE member — allowed
    }
};
```

### Template 8: Constructor-Initializer for Composite Classes

```cpp
class Engine {
    int horsepower;
public:
    Engine(int hp) : horsepower(hp) {}
};

class Car {
    Engine engine;   // composite: member object
    int year;
public:
    Car(int hp, int y) : engine(hp), year(y) {   // initializer list
        // engine is already constructed before this body runs
    }
};
```

---

## 9. EXAM TRAPS

### Trap 1: Forgetting the semicolon after the class closing brace
```cpp
class Point {
    int x, y;
}  // ← MISSING SEMICOLON! Compiler error: "expected ';' after class definition"
```

> [!success]- Show Answer
> > Every class definition must end with `};`. This is the single most common syntax error in handwritten code on exams. The compiler's error message will be confusing because it thinks the next line is part of the class.

### Trap 2: Default copy constructor does SHALLOW copy → double delete with dynamic members
If your class has `new` in the constructor and `delete` in the destructor, the compiler-generated copy constructor copies pointers, not data. Two objects will share the same dynamic memory. When both go out of scope, the second destructor crashes.

> [!success]- Show Answer
> > ALWAYS ask: "Does my class own dynamic memory (`new`/`new[]`)?" If yes, you NEED a custom copy constructor, copy assignment operator, and destructor (Rule of Three).

### Trap 3: delete vs delete[]
`new` → `delete`. `new[]` → `delete[]`. Mixing them causes undefined behavior — only the first element's destructor runs if you use `delete` on an array.

```cpp
Student* s = new Student;       // single
delete s;                       // correct
Student* arr = new Student[10]; // array
delete[] arr;                   // correct — NOT delete arr;
```

> [!success]- Show Answer
> > Using `delete` on a `new[]` array calls the destructor only for the first element. The remaining 9 elements' destructors never run — potential resource leak. The memory layout is also different, so the allocator may crash.

### Trap 4: Constructor-initializer order depends on DECLARATION order, NOT initializer list order
```cpp
class X {
    int a;  // declared FIRST
    int b;  // declared SECOND
public:
    X() : b(1), a(b) {}  // initializer list: b before a
    // ACTUAL order: a(b) then b(1) — a gets uninitialized b!
};
```
`a` is initialized with `b` before `b` is initialized → undefined behavior.

> [!success]- Show Answer
> > Always write initializers in declaration order. The compiler won't warn you by default — use `-Wreorder` (GCC/Clang) or `/W4` (MSVC) to catch this.

### Trap 5: inline is a suggestion, not a command
The compiler decides whether to inline. Writing `inline` does NOT guarantee inlining. Also, overly large inline functions increase code size and can make debugging harder.

> [!success]- Show Answer
> > On exams, the right answer is: "`inline` is a hint to the compiler. The compiler may choose to inline or not based on optimization settings and function complexity."

### Trap 6: const member functions cannot modify ANY data member
```cpp
void foo() const {
    x = 5;   // ERROR: cannot assign to member in const function
    bar();   // ERROR if bar() is NOT const
}
```

> [!success]- Show Answer
> > Every data member access inside a `const` member function is implicitly through `const this`. The compiler treats all members as `const` within the function. `mutable` is the only escape hatch.

### Trap 7: Access is per-CLASS, not per-OBJECT
A member function can access private members of ANY object of the same class, not just `this`:
```cpp
class Point {
    int x;
public:
    void steal(const Point& other) { x = other.x; }  // LEGAL
};
```

> [!success]- Show Answer
> > This is a common exam trick. "Can method `foo` of class `A` access private member `x` of another `A` object passed as parameter?" YES. Access control is at the class boundary, not the object boundary.

### Trap 8: Friend classes break encapsulation
Granting friendship gives complete access to ALL private and protected members. This defeats encapsulation for the granting class with respect to the friend. Use sparingly and deliberately.

> [!success]- Show Answer
> > On theory questions: friendship is a deliberate, narrow violation of encapsulation — it should be used as a last resort, not a default pattern.

### Trap 9: Composite class — member constructors run BEFORE enclosing constructor body
```cpp
class Outer {
    Inner i;
public:
    Outer() {   // by the time this body runs, i is FULLY CONSTRUCTED
        // i is safe to use
    }
};
```

> [!success]- Show Answer
> > This means you can safely use member objects inside the enclosing constructor body. The danger is thinking members aren't initialized yet — they ARE.

### Trap 10: Destructors run in reverse order of constructors
Barrier object: construction order is a→b→c; destruction is ~c→~b→~a. Stack (LIFO) semantics.

> [!success]- Show Answer
> > In composite + inheritance combined: base class is constructed first, then members in declaration order, then derived body. Destruction: derived body, then members (reverse), then base (reverse).

### Trap 11: No constructor defined = compiler generates default constructor
If you define ZERO constructors, the compiler generates a default constructor. If you define ANY constructor (even one with parameters), the compiler does NOT generate a default constructor. Then `ClassName obj;` fails if no default constructor exists.

```cpp
class Point {
    int x, y;
public:
    Point(int xVal, int yVal) { x = xVal; y = yVal; }  // only parameterized ctor
};
Point p;   // ERROR: no default constructor!
```

> [!success]- Show Answer
> > This is especially dangerous with arrays: `Point arr[5];` requires a default constructor for each element. If only a parameterized constructor exists, this won't compile.

### Trap 12: Pointers to dynamic objects need explicit delete
Stack objects are auto-destroyed. Heap objects allocated with `new` MUST be manually `delete`d. Forgetting leads to memory leaks.

```cpp
void func() {
    Point p;                   // auto-destroyed when func() ends
    Point* pp = new Point;     // NOT auto-destroyed → MEMORY LEAK
}  // p destroyed, pp's pointed-to object still on heap — leaked!
```

> [!success]- Show Answer
> > The pointer `pp` itself (4/8 bytes on stack) is auto-destroyed. The Point object it POINTED TO (on the heap) is NOT auto-destroyed. That's the leak.

### Trap 13: Copy constructor is called in these four situations
1. `ClassName a(b);` — direct initialization
2. `ClassName a = b;` — copy initialization (NOT assignment!)
3. Passing object by value to a function parameter
4. Returning object by value from a function

> [!success]- Show Answer — `=` in initialization vs. assignment
> > ```cpp
> > ClassName a = b;    // Copy CONSTRUCTOR — a is being CREATED
> > ClassName a;        // Default constructor
> > a = b;              // Copy ASSIGNMENT OPERATOR — a already exists
> > ```
> > Different operators, different function calls. Crucial distinction on exams.

### Trap 14: Out-of-line definitions need ClassName:: prefix
```cpp
class Point {
    void setY(int valY);         // declaration inside class
};

void setY(int valY) { }         // ERROR: this is a GLOBAL function, not Point::setY
void Point::setY(int valY) { }  // CORRECT: qualified with ClassName::
```

> [!success]- Show Answer
> > Without the `Point::` prefix, the compiler thinks you're defining a free function with the same name. The linker will complain about the missing definition of `Point::setY`.

### Trap 15: Friend is NOT symmetric, NOT transitive, NOT inheritable
- **NOT symmetric:** A friends B does NOT mean B friends A
- **NOT transitive:** A friends B and B friends C does NOT mean A friends C
- **NOT inheritable:** A friends B; class D: public B; D is NOT a friend of A

> [!success]- Show Answer
> > "Is friend a one-way street?" YES. "Does my derived class inherit my friendships?" NO. Each friendship must be explicitly granted.

### Trap 16: Assignment operator is also a shallow copy by default
Just like the copy constructor, the compiler-generated `operator=` does a shallow copy. If you have dynamic members, you need a custom one.

> [!success]- Show Answer
> > Rule of Three: if you need a destructor, you probably need a custom copy constructor AND a custom copy assignment operator. This lecture focuses on the copy constructor, but the same logic applies to `operator=`.

### Trap 17: Not initializing pointers in constructors
```cpp
class Student {
    Course* coursesTaken;
public:
    Student(int n) {
        coursesTaken = new Course[n];  // good
    }
    Student() {
        // coursesTaken is UNINITIALIZED → dangling/wild pointer
        // ~Student() will delete[] a random address → CRASH
    }
};
```

> [!success]- Show Answer
> > Always initialize pointers — either to `nullptr` or to valid memory. An uninitialized pointer in a destructor's `delete[]` is a guaranteed crash.

---

## 10. HAND-CODING DRILLS

### Drill 1: Constructor/Destructor Trace

Given the following code, write the exact output in order:

```cpp
#include <iostream>
using namespace std;

class A {
    int id;
public:
    A(int i) : id(i) { cout << "A(" << id << ") "; }
    ~A() { cout << "~A(" << id << ") "; }
};

class B {
    A a1, a2;
public:
    B(int x, int y) : a1(x), a2(y) { cout << "B() "; }
    ~B() { cout << "~B() "; }
};

int main() {
    B obj(10, 20);
    return 0;
}
```

> [!success]- Show Answer
> > ```
> > A(10) A(20) B() ~B() ~A(20) ~A(10)
> > ```
> > Explanation:
> > 1. `a1` declared FIRST → `A(10)` runs
> > 2. `a2` declared SECOND → `A(20)` runs
> > 3. `B()` body runs
> > 4. `~B()` body runs
> > 5. `~a2` runs (reverse order) → `~A(20)`
> > 6. `~a1` runs → `~A(10)`

### Drill 2: Deep Copy Bug — Find and Fix

The following code crashes. Identify the bug and write the corrected version:

```cpp
class Array {
    int* data;
    int len;
public:
    Array(int l) : len(l) {
        data = new int[len];
        for (int i = 0; i < len; i++) data[i] = i;
    }
    ~Array() { delete[] data; }
    void print() const {
        for (int i = 0; i < len; i++) cout << data[i] << " ";
        cout << endl;
    }
};

int main() {
    Array a(5);
    Array b(a);       // This line causes the eventual crash
    a.print();
    b.print();
    return 0;
}  // CRASH: double delete on data
```

> [!success]- Show Answer
> > **Bug:** No custom copy constructor. The compiler-generated one does a shallow copy of `data` pointer. Both `a` and `b` have `data` pointing to the same array. When `main()` ends, `~a()` delete[]s the array, then `~b()` delete[]s the same already-freed memory → crash.
> >
> > **Fix:**
> > ```cpp
> > class Array {
> >     int* data;
> >     int len;
> > public:
> >     Array(int l) : len(l) {
> >         data = new int[len];
> >         for (int i = 0; i < len; i++) data[i] = i;
> >     }
> >     Array(const Array& other) : len(other.len) {     // custom copy ctor
> >         data = new int[len];
> >         for (int i = 0; i < len; i++) data[i] = other.data[i];
> >     }
> >     ~Array() { delete[] data; }
> >     void print() const {
> >         for (int i = 0; i < len; i++) cout << data[i] << " ";
> >         cout << endl;
> >     }
> > };
> > ```

### Drill 3: Composite Class Constructor Order

What is the output of this program?

```cpp
#include <iostream>
using namespace std;

struct X {
    X()  { cout << "X "; }
    ~X() { cout << "~X "; }
};

struct Y {
    Y()  { cout << "Y "; }
    ~Y() { cout << "~Y "; }
};

struct Z {
    Y y;   // declared FIRST
    X x;   // declared SECOND
    Z()  { cout << "Z "; }
    ~Z() { cout << "~Z "; }
};

int main() {
    Z z;
    return 0;
}
```

> [!success]- Show Answer
> > ```
> > Y X Z ~Z ~X ~Y
> > ```
> > `y` is declared before `x`, so `Y()` runs first, then `X()`, then `Z()` body. Destruction: `~Z()` body, then `~x`, then `~y` (reverse of declaration order).

### Drill 4: Friend Class Access

Write a pair of classes `Bank` and `Account` such that:
- `Account` has private members: `double balance` and `int accountNumber`
- `Account` has a constructor taking those two values
- `Bank` is a friend of `Account` and can read AND modify `balance` directly
- `Bank` has a method `transfer(Account& from, Account& to, double amount)` that deducts from `from` and adds to `to` (accessing `balance` directly)
- Outside code (main) CANNOT touch `balance` directly

> [!success]- Show Answer
> > ```cpp
> > #include <iostream>
> > using namespace std;
> >
> > class Account {
> > private:
> >     double balance;
> >     int accountNumber;
> > public:
> >     Account(int num, double bal) : accountNumber(num), balance(bal) {}
> >     void display() const {
> >         cout << "Account " << accountNumber << ": $" << balance << endl;
> >     }
> >     friend class Bank;
> > };
> >
> > class Bank {
> > public:
> >     void transfer(Account& from, Account& to, double amount) {
> >         if (from.balance >= amount) {
> >             from.balance -= amount;   // direct access to private balance
> >             to.balance += amount;     // thanks to friend declaration
> >             cout << "Transferred $" << amount << endl;
> >         } else {
> >             cout << "Insufficient funds." << endl;
> >         }
> >     }
> > };
> >
> > int main() {
> >     Account a1(1001, 500.0);
> >     Account a2(1002, 100.0);
> >     Bank bank;
> >     bank.transfer(a1, a2, 200.0);
> >     a1.display();  // Account 1001: $300
> >     a2.display();  // Account 1002: $300
> >     // a1.balance = 1000;  // ERROR: balance is private
> >     return 0;
> > }
> > ```

### Drill 5: const Member Function Error Hunt

Find all compile errors in this code:

```cpp
class Counter {
    int count;
    int step;
public:
    Counter(int s) : count(0), step(s) {}
    void increment() const { count += step; }
    int getCount() { return count; }
    void display() const {
        cout << "Count: " << count << endl;
        increment();
    }
};

int main() {
    const Counter c(5);
    cout << c.getCount() << endl;
    c.display();
    return 0;
}
```

> [!success]- Show Answer
> > Three errors:
> >
> > 1. **`void increment() const { count += step; }`** — ERROR: modifying `count` inside a `const` member function. Remove `const` from `increment()`.
> > 2. **`void display() const { ... increment(); }`** — ERROR: calling non-const `increment()` from a `const` function. Fix by removing `const` from `display()` or removing the `increment()` call.
> > 3. **`const Counter c(5); cout << c.getCount();`** — ERROR: `getCount()` is not `const`, cannot call on `const` object. Fix: `int getCount() const { return count; }`
> >
> > Corrected:
> > ```cpp
> > class Counter {
> >     int count;
> >     int step;
> > public:
> >     Counter(int s) : count(0), step(s) {}
> >     void increment() { count += step; }
> >     int getCount() const { return count; }
> >     void display() const { cout << "Count: " << count << endl; }
> > };
> > ```

### Drill 6: Inline vs Out-of-line Identification

For each function, state whether it is: in-line, out-of-line (not inline), or out-of-line with inline keyword.

```cpp
class Widget {
    int val;
public:
    Widget() { val = 0; }                           // (a)
    Widget(int v);                                    // (b)
    int getVal() const { return val; }                // (c)
    void setVal(int v);                                // (d)
    void doubleVal();                                  // (e)
};

Widget::Widget(int v) { val = v; }                   // (b)

void Widget::setVal(int v) { val = v; }               // (d)

inline void Widget::doubleVal() { val *= 2; }         // (e)
```

> [!success]- Show Answer
> > (a) `Widget()` — **In-line** (defined inside class body, implicitly inline)
> > (b) `Widget(int v)` — **Out-of-line** (defined outside, no `inline` keyword)
> > (c) `getVal()` — **In-line** (defined inside class body, implicitly inline)
> > (d) `setVal(int v)` — **Out-of-line** (defined outside, no `inline` keyword)
> > (e) `doubleVal()` — **Out-of-line with inline keyword** (defined outside, explicit `inline` keyword)

### Drill 7: Pointers to Objects — Complete Trace

```cpp
#include <iostream>
using namespace std;

class Tracker {
    static int nextID;
    int id;
public:
    Tracker() : id(nextID++) {
        cout << "ctor " << id << endl;
    }
    Tracker(const Tracker& other) : id(nextID++) {
        cout << "copy ctor " << id << " from " << other.id << endl;
    }
    ~Tracker() { cout << "dtor " << id << endl; }
    int getID() const { return id; }
};

int Tracker::nextID = 1;

int main() {
    Tracker t1;
    Tracker* p = new Tracker;
    Tracker* arr = new Tracker[2];
    Tracker t2(t1);
    delete p;
    delete[] arr;
    return 0;
}
```

Write the COMPLETE output in order.

> [!success]- Show Answer
> > ```
> > ctor 1
> > ctor 2
> > ctor 3
> > ctor 4
> > copy ctor 5 from 1
> > dtor 2
> > dtor 4
> > dtor 3
> > dtor 5
> > dtor 1
> > ```
> > Trace:
> > - `t1`: ctor id=1 (stack)
> > - `new Tracker`: ctor id=2 (heap, single)
> > - `new Tracker[2]`: ctor id=3, ctor id=4 (heap array)
> > - `t2(t1)`: copy ctor id=5 from t1's id=1
> > - `delete p`: dtor id=2 (the single heap object)
> > - `delete[] arr`: dtor 4 then dtor 3 (reverse order of array construction)
> > - `return 0`: t2 destroyed (dtor 5), then t1 destroyed (dtor 1) — stack objects in reverse order
