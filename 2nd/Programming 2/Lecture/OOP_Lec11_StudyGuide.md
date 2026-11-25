# Lec11: Templates and Friends — Study Guide

---

## 1. CONCEPT CARD: TEMPLATES

### 1.1 What They Are — A Framework for Generating a Family of Functions or Classes Sharing the Same Functionality but Differing in Data Type

Templates give us the means to define a **family** of functions or classes that share the same functionality but which may differ with respect to the **data type** used internally.

- A **function template** is a framework for generating related functions.
- A **class template** is a framework for generating the source code for any number of related classes.

Templates implement **parametric polymorphism** — the same code works for any type, and the type is supplied as a parameter. The compiler generates a **separate copy** of the function/class for each type used, all at **compile time**.

### 1.2 What Problem They Solve — Write Once, Work with Any Type (No Code Duplication)

Without templates, you would need to write separate functions/classes for every type:

```cpp
void swap(int &x, int &y)      { int temp = x; x = y; y = temp; }
void swap(float &x, float &y)  { float temp = x; x = y; y = temp; }
void swap(string &x, string &y){ string temp = x; x = y; y = temp; }
// ... and so on for every type
```

With templates:

```cpp
template <class T>
void swap(T &x, T &y) { T temp = x; x = y; y = temp; }
// One definition works for int, float, string, Student, etc.
```

### 1.3 How It Works

1. You write the template with a **placeholder type** (conventionally `T`).
2. When you call/use it with a concrete type, the compiler **instantiates** the template — generates a version with `T` replaced by the actual type.
3. This happens at **compile time** — no runtime overhead compared to hand-written type-specific code.
4. Each unique combination of template arguments produces a **distinct instantiation**.

```
swap<int>(a, b)     → compiler generates void swap(int &x, int &y) { ... }
swap<float>(a, b)   → compiler generates void swap(float &x, float &y) { ... }
swap<string>(a, b)  → compiler generates void swap(string &x, string &y) { ... }
```

### 1.4 Concrete Example — Generic Array Class

```cpp
template <class T>
class Array {
public:
    Array(unsigned sz);
    ~Array();
    T & operator[](unsigned i);
private:
    T * values;
    unsigned size;
};

int main() {
    Array<int>    ages(5);    // array of 5 ints
    Array<float>  gpas(5);    // array of 5 floats
    Array<string> names(5);   // array of 5 strings
    // One class template → three concrete classes, generated automatically
}
```

### 1.5 What It Is NOT

- A **template is NOT a class** — it's a blueprint for generating classes. You cannot inherit from a template directly (`class D : public Array` is an error). You can only inherit from an **instantiation** (`class D : public Array<int>`).
- Templates are **NOT runtime polymorphism** — they are resolved at compile time via code generation. No vtables, no dynamic dispatch.
- A template is **NOT inherited** — a derived class does not inherit the template itself, only the concrete instantiated class.

---

## 2. FUNCTION TEMPLATES

### 2.1 Definition — A Function Defined in Terms of an Unspecified Type; Compiler Generates Separate Versions Based on Argument Types

A function can be defined in terms of an **unspecified** type. The compiler generates separate versions of the function based on the type of the arguments passed in the function calls.

### 2.2 Syntax

```cpp
template <class T>
return-type function-name(T param)
```

- `T` is called a **template parameter**.
- The keyword `class` can be replaced with `typename` (equivalent in this context): `template <typename T>`.

### 2.3 One-Parameter Function Templates

**Basic form:**
```cpp
template <class T>
void display(const T &val) { cout << val; }
```

**With an additional non-template parameter:**
```cpp
template <class T>
void display(const T &val, ostream &os) { os << val; }
```

**Same template parameter appearing multiple times:**
```cpp
template <class T>
void swap(T &x, T &y) { T temp = x; x = y; y = temp; }
// T appears three times — ensures both args AND the temp variable have the SAME type
```

### 2.4 Swap as a Function Template

```cpp
#include <iostream>
using namespace std;

template <class T>
void swap(T &x, T &y) {
    T temp;
    temp = x;
    x = y;
    y = temp;
}

int main() {
    int a = 1, b = 2;
    swap(a, b);        // T = int

    float c = 1.5, d = 2.5;
    swap(c, d);        // T = float

    string e = "Hello", f = "World";
    swap(e, f);        // T = string
}
```

### 2.5 Multiple Parameter Function Template

```cpp
template <class T1, class T2>
void arrayInput(T1 array, T2 &count) {
    for (T2 j = 0; j < count; j++) {
        cout << "value: ";
        cin >> array[j];
    }
}

// Usage:
const unsigned tempCount = 3;
float temperature[tempCount];
const unsigned stationCount = 4;
int station[stationCount];

arrayInput(temperature, tempCount);  // T1=float[], T2=const unsigned
arrayInput(station, stationCount);   // T1=int[],    T2=const unsigned
```

### 2.6 Table Lookup — Generic Search

```cpp
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) {
    for (unsigned i = 0; i < size; i++)
        if (searchVal == table[i])
            return i;
    return -1;
}

int main() {
    const unsigned iCount = 10, fCount = 5, sCount = 5;
    int iTable[iCount] = { 0, 10, 20, 30, 40, 50, 60, 70, 80, 90 };
    float fTable[fCount] = { 1.1, 2.2, 3.3, 4.4, 5.5 };

    cout << indexOf(20, iTable, iCount) << endl;        // prints 2
    cout << indexOf(2.2f, fTable, fCount) << endl;      // prints 1

    string names[sCount] = { "John", "Mary", "Sue", "Dan", "Bob" };
    cout << indexOf((string)"Dan", names, sCount) << endl; // prints 3
}
```

### 2.7 Making Custom Types Work with Templates — Operator Overloading Required

If a template uses an operator (e.g., `==`), every type used with that template **must support** that operator. Use operator overloading to ensure compatibility:

```cpp
class Student {
public:
    Student(long idVal) { id = idVal; }
    int operator==(const Student &s2) const {
        return id == s2.id;
    }
private:
    long id;
};

int main() {
    const unsigned sc = 5;
    Student sTable[sc] = { 10000, 11111, 20000, 22222, 30000 };
    Student s(22222);
    cout << indexOf(s, sTable, sc) << endl;  // prints 3
    // Works because Student defines operator==
}
```

### 2.8 Overriding (Specializing) a Function Template

When a function template does not apply to a particular type, you may need to either:
- **Override** the function template (provide an explicit non-template version), or
- Make the type **conform** to the function template (by adding operators).

```cpp
// Generic template works for most types via operator==
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) { /* uses == */ }

// But char* strings need strcmp — operator== compares pointers, not content!
// So we provide an EXPLICIT override:
long indexOf(const char *searchVal, const char *table[], unsigned size) {
    for (unsigned i = 0; i < size; i++)
        if (strcmp(searchVal, table[i]) == 0)
            return i;
    return -1;
}

int main() {
    int iTable[] = { 0, 10, 20, 30, 40, 50, 60, 70, 80, 90 };
    cout << indexOf(20, iTable, 10) << endl;  // calls template version → 2

    const char *names[] = { "John", "Mary", "Sue", "Dan", "Bob" };
    cout << indexOf("Dan", names, 5) << endl; // calls explicit version → 3
    // The explicit version takes priority over the template for const char*
}
```

**Rule**: An **explicit (non-template) function** takes precedence over a template instantiation when both are equally good matches. This allows you to hand-craft specializations for problematic types.

---

## 3. CLASS TEMPLATES

### 3.1 Definition — A Framework for Generating Related Classes; Type Parameterized at Declaration

```cpp
template <class T>
class MyClass {
    // using T inside (parametrically)
};

MyClass<int> x;         // instantiation with int
MyClass<Student> a;     // instantiation with Student
```

### 3.2 Simple Example — Circle with Generic Coordinates

```cpp
template <class T1, class T2>
class Circle {
private:
    T1 x, y;         // coordinates — any numeric type
    T2 radius;       // radius — potentially different type
};

Circle<int, long>        c1;     // x,y=int, radius=long
Circle<unsigned, float>  c2;     // x,y=unsigned, radius=float
```

### 3.3 Array Class Template — Full Implementation

```cpp
template <class T>
class Array {
public:
    Array(unsigned sz);
    ~Array();
    T & operator[](unsigned i);
private:
    T * values;
    unsigned size;
};

// Method definitions OUTSIDE the class — note the template prefix on EACH:
template <class T>
Array<T>::Array(unsigned sz) {
    values = new T[sz];
    size = sz;
}

template <class T>
T & Array<T>::operator[](unsigned i) {
    if (i >= size) {
        cout << "ERROR: array index out of bound!!!\n";
        abort();
    }
    return values[i];
}

template <class T>
Array<T>::~Array() {
    delete[] values;
}

// Usage:
int main() {
    const unsigned numStudents = 2;
    Array<int>    ages(numStudents);
    Array<float>  gpas(numStudents);
    Array<string> names(numStudents);

    for (int j = 0; j < numStudents; j++) {
        ages[j] = 20 + j;
        gpas[j] = 3.5 + j * 0.1;
        names[j] = "Student" + to_string(j);
    }
}
```

**Critical syntax rule**: When defining template class members **outside** the class body, EVERY member function must be preceded by `template <class T>` and the class name must include `<T>` (e.g., `Array<T>::Array` not `Array::Array`).

---

## 4. TEMPLATES AND INHERITANCE

### 4.1 Template Is NOT a Class

- A **template is not a class** — it's a pattern for generating classes.
- A template **cannot be inherited directly**.

```cpp
// ERROR — template is not a class:
// class D : public Array { };   // Which T? Illegal!

// OK — inheriting from an instantiation:
class D : public Array<int> { }; // correct: Array<int> IS a concrete class

// OK — a class template can inherit from an ordinary class:
template <class T>
class MyClass : public aClass { }; // inheriting from a regular class
```

### 4.2 Templates and Static Members

- Static members defined in a template are **static members of the classes associated with a template** — NOT of the template itself.
- Each template **instantiation** gets its **own copy** of the static member:

```cpp
template <class T>
class Counter {
    static int count;
public:
    Counter() { count++; }
    static int getCount() { return count; }
};

template <class T> int Counter<T>::count = 0;

int main() {
    Counter<int> c1, c2;
    Counter<float> c3;

    cout << Counter<int>::getCount() << endl;    // 2 (c1, c2)
    cout << Counter<float>::getCount() << endl;  // 1 (c3 only)
    // Counter<int> and Counter<float> have SEPARATE static count variables!
}
```

---

## 5. FRIENDS

### 5.1 Friend Classes

A **friend class** is a class in which **all member functions** have been granted **full access** to all (`private`, `protected`, and `public`) members of the class defining it as a friend.

**Declaration:** The friend class is declared inside the class granting friendship.

```cpp
class C1 {
    friend class C2;    // C2 can access ALL members of C1
    int privateData;
};

class C2 {
    friend class C3;    // C3 can access ALL members of C2
    void accessC1(C1 &obj) {
        obj.privateData = 5;  // OK — C2 is a friend of C1
    }
};

class C3 {
    void accessC1(C1 &obj) {
        // obj.privateData = 5;  // ERROR — C3 is NOT a friend of C1
    }
};
```

### 5.2 Friend Functions

A **friend function** is a function which has been granted **full access** to the `private` and `protected` members of an instance of the class. The friend function is declared inside the class granting friendship.

```cpp
class Employee {
    int id;
    double salary;
public:
    Employee(int i, double s) : id(i), salary(s) {}
    friend float calcPay(Employee &e);  // calcPay can access private members
};

float calcPay(Employee &e) {
    return e.salary * 0.85f;  // OK — calcPay is a friend, can access salary
}

// Also common: overloading << as a friend
class Point {
    int x, y;
public:
    friend ostream & operator<<(ostream &os, const Point &p) {
        os << "(" << p.x << ", " << p.y << ")";  // Access to private x, y
        return os;
    }
};
```

### 5.3 Properties of Friends — The Three "NOTs"

| Property | Meaning | Example |
|----------|---------|---------|
| **Non-symmetrical** | If C2 is a friend of C1, C1 is NOT necessarily a friend of C2 | C2 can access C1's privates, but C1 cannot access C2's privates (unless C2 also declares C1 as friend) |
| **Non-transitive** | If C2 is a friend of C1 and C3 is a friend of C2, C3 is NOT necessarily a friend of C1 | Friendship does NOT propagate through chains |
| **Not inheritable** | A friend of a base class is NOT inherited by derived classes | A function that is a friend of `Employee` CANNOT access private members of `SalariedEmployee` |

**Example of non-inheritability:**
```cpp
class Employee {
    int empID;
public:
    friend float calcPay(Employee &e);
};

class SalariedEmployee : public Employee {
    double annualSalary;
    // calcPay() is NOT a friend here!
};

float calcPay(Employee &e) {
    // CAN access e.empID (friend of Employee)
    // CANNOT access any SalariedEmployee-specific private members
}
```

### 5.4 Things to Consider When Using Friends

- Friends make loosely coupled classes **tightly coupled** — problems with modularity and error searching.
- Friends **diminish encapsulation and information hiding**.
- **Limit the use of "friends"** — use them sparingly and only when truly necessary (e.g., operator overloading for stream insertion/extraction).

---

## 6. MUST-MEMORIZE SYNTAX TEMPLATES

### 6.1 Function Template

```cpp
template <class T>
returnType functionName(T param) {
    // use T
}
```

### 6.2 Function Template with Multiple Parameters

```cpp
template <class T1, class T2>
returnType functionName(T1 p1, T2 p2) {
    // use T1 and T2
}
```

### 6.3 Class Template Declaration

```cpp
template <class T>
class MyClass {
    T data;
public:
    MyClass(T val);
    T getValue() const;
};
```

### 6.4 Class Template Member Definitions (Outside Class)

```cpp
template <class T>
MyClass<T>::MyClass(T val) {
    data = val;
}

template <class T>
T MyClass<T>::getValue() const {
    return data;
}
```

### 6.5 Explicit (Non-Template) Override of a Template Function

```cpp
// Template version for general types
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) { /* general impl */ }

// Explicit override for const char*
long indexOf(const char *searchVal, const char *table[], unsigned size) {
    // specialized impl using strcmp
}
```

### 6.6 Friend Class Declaration

```cpp
class A {
    friend class B;   // B has full access to A
    int secret;
};

class B {
    void peek(A &a) { a.secret = 42; }  // OK
};
```

### 6.7 Friend Function Declaration

```cpp
class MyClass {
    int data;
public:
    friend void accessor(MyClass &m);
    friend ostream & operator<<(ostream &, const MyClass &);
};
```

### 6.8 Templates + Inheritance (Correct Usage)

```cpp
// Inherit from a concrete template instantiation
class IntArray : public Array<int> { };

// Template class inheriting from a regular class
template <class T>
class SmartPtr : public RefCounter { };
```

---

## 7. EXAM TRAPS

### Trap 1: Template Is NOT a Class — Cannot Inherit from a Template Directly

```cpp
template <class T> class Array { ... };

// ERROR: which T? Array is not a concrete type
// class D : public Array { };

// CORRECT: specify the type
class D : public Array<int> { };
```

### Trap 2: Forgetting `template <class T>` and `<T>` on Member Definitions Outside Class

```cpp
// ERROR — missing template prefix and <T>
// Array::Array(unsigned sz) { ... }

// CORRECT:
template <class T>
Array<T>::Array(unsigned sz) { values = new T[sz]; size = sz; }
```

### Trap 3: Templates Require Used Operators to Be Defined for the Type

If a function template uses `==`, every type you instantiate it with **must** define `operator==`. Otherwise → compilation error.

```cpp
class MyType { };  // No operator== defined
// indexOf(MyType(), myArray, 5);  // COMPILE ERROR — MyType has no ==
```

### Trap 4: Each Template Instantiation Gets Its OWN Static Members

```cpp
template <class T> class C { static int count; };
// C<int>::count and C<float>::count are DIFFERENT variables
```

### Trap 5: Explicit Function Overrides Take Priority Over Template Matches

When both an explicit function and a template instantiation are viable, the **non-template** version wins.

### Trap 6: Friendship Is NOT Symmetrical

```cpp
class A { friend class B; };
// B can access A's privates, but A CANNOT access B's privates (unless B also declares friend class A)
```

### Trap 7: Friendship Is NOT Transitive

```cpp
class A { friend class B; };
class B { friend class C; };
// C is NOT a friend of A — friendship does not propagate
```

### Trap 8: Friendship Is NOT Inherited

```cpp
class Base { friend class F; };
class Derived : public Base { int derivedData; };
// F can access Base's members through Derived, but NOT Derived's own members
```

### Trap 9: `class` Keyword in `template <class T>` — Don't Confuse with Inheritance

`template <class T>` is declaring a **type parameter**, not defining a class. The keyword `typename` can be used instead: `template <typename T>`.

### Trap 10: Template Code Must Be in Header Files (Typically)

Since the compiler needs the full template definition to instantiate it, template definitions are usually placed in header files (not compiled separately in .cpp files).

---

## 8. HAND-CODING DRILLS

### Drill 1: Write a Function Template — Maximum of Two Values

Write a function template `maximum` that takes two parameters of the same type and returns the larger one.

```cpp
// TODO: Write the template

int main() {
    cout << maximum(3, 7) << endl;        // 7
    cout << maximum(3.5, 2.1) << endl;    // 3.5
    cout << maximum('a', 'z') << endl;    // z
}
```

> [!success]- Show Answer
> ```cpp
> template <class T>
> T maximum(T a, T b) {
>     return (a > b) ? a : b;
> }
> ```

### Drill 2: Class Template — Pair

Implement a `Pair` class template that stores two values of (potentially) different types.

```cpp
// TODO: Write the Pair template with constructor, getFirst(), getSecond()

int main() {
    Pair<int, string> p1(42, "hello");
    cout << p1.getFirst() << " " << p1.getSecond() << endl;  // 42 hello

    Pair<string, double> p2("pi", 3.14159);
    cout << p2.getFirst() << " " << p2.getSecond() << endl;  // pi 3.14159
}
```

> [!success]- Show Answer
> ```cpp
> template <class T1, class T2>
> class Pair {
>     T1 first;
>     T2 second;
> public:
>     Pair(T1 f, T2 s) : first(f), second(s) {}
>     T1 getFirst() const { return first; }
>     T2 getSecond() const { return second; }
> };
> ```

### Drill 3: Friend Class Access

```cpp
class Vault {
    int secretCode;
public:
    Vault(int code) : secretCode(code) {}
    friend class KeyMaster;
};

class KeyMaster {
public:
    void reveal(Vault &v) { cout << "Secret: " << v.secretCode << endl; }
};

class Apprentice {
public:
    // Can Apprentice access Vault::secretCode? Write the answer.
};
```

> [!success]- Show Answer
> `Apprentice` **cannot** access `Vault::secretCode`. Friendship is non-symmetrical and non-transitive. Only `KeyMaster` (explicitly declared as friend) has access. `Apprentice` has no special relationship to `Vault`.

### Drill 4: Explicit Function Override of Template

The template `indexOf` uses `==` to compare. Write an explicit override for C-style strings (`const char*`).

```cpp
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) {
    for (unsigned i = 0; i < size; i++)
        if (searchVal == table[i]) return i;
    return -1;
}

// TODO: Write explicit override for const char*

int main() {
    const char *names[] = { "Alice", "Bob", "Charlie" };
    cout << indexOf("Bob", names, 3) << endl;  // should print 1
}
```

> [!success]- Show Answer
> ```cpp
> long indexOf(const char *searchVal, const char *table[], unsigned size) {
>     for (unsigned i = 0; i < size; i++)
>         if (strcmp(searchVal, table[i]) == 0)
>             return i;
>     return -1;
> }
> ```

### Drill 5: Template with Static Member

```cpp
template <class T>
class Tracker {
    static int instances;
public:
    Tracker() { instances++; }
    ~Tracker() { instances--; }
    static int count() { return instances; }
};
template <class T> int Tracker<T>::instances = 0;

int main() {
    Tracker<int> a, b, c;
    Tracker<float> x, y;
    cout << Tracker<int>::count() << endl;     // ?
    cout << Tracker<float>::count() << endl;   // ?
}
```

> [!success]- Show Answer
> ```
> 3
> 2
> ```
> `Tracker<int>` and `Tracker<float>` have **separate** static `instances` variables. `a, b, c` are 3 int-trackers → `Tracker<int>::count()` = 3. `x, y` are 2 float-trackers → `Tracker<float>::count()` = 2.

---

> [!NOTE]
> This study guide covers all lecture content for Lec11: Templates and Friends. Master the syntax for function templates, class templates (including member definitions outside the class), and friend declarations. Remember the three properties of friendship: non-symmetrical, non-transitive, and not inheritable.
