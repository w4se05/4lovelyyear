# Lec5: Objects and Classes (Conceptual) — Study Guide

---

## 1. CONCEPT CARD: Class and Object

**What it is:** A class is a template that defines what data and functions a group of objects will have. An object is one concrete instance created from that template.

**What problem it solves:** Before classes, you had to manually define every variable and function separately. If you needed three bank accounts, you'd declare three separate balance variables, three separate deposit functions, etc. There was no way to say "these things belong together." Classes let you define the pattern once, then stamp out as many instances as you need — each with its own independent copy of the data.

**How it works:**
1. You write a class definition listing the data members (state) and member functions (behavior).
2. The class acts as a **factory**: you call its constructor to create objects.
3. The class acts as a **classifier**: all objects of that class share the same structure.
4. Each object gets its own copy of data members, but all objects share the same function code.
5. Objects communicate by sending **messages** — calling each other's public methods.

**Concrete example:** A hotel reservation system. The class `Room` defines that every room has a number, a type, a rate, and a status (vacant/occupied). You create object `room_301` and object `room_302`. Both follow the same blueprint but hold different actual data (different room numbers, possibly different rates). The `book()` method exists once in the class code, but when you call `room_301.book("Alice")`, it modifies `room_301`'s data only.

**What it is NOT:** A class is NOT the same as a struct from C, even though C++ allows them to look similar. A C struct is a passive bag of data with no built-in behavior. A class bundles data WITH the functions that operate on it and controls who can access what.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
class ClassName {              // Template/blueprint definition
private:                       // State: data members (per-object)
    int attribute1;            // Each OBJECT gets its own copy
    double attribute2;
public:                        // Behavior: member functions (shared)
    ClassName(int a, double b); // Constructor: creates new object
    void method1();             // Message receiver
    int method2() const;        // const = won't modify object
};                             // MANDATORY semicolon

// Creating objects (instantiation):
ClassName obj1(5, 3.14);       // Static: on the stack
ClassName *obj2 = new ClassName(10, 2.71); // Dynamic: on the heap
```

---

## 3. EXAM TRAPS

- **Confusing static vs. dynamic instantiation.** Static = `ClassName obj;` (compiler allocates on stack, auto-destroyed when out of scope). Dynamic = `new ClassName();` (heap, you must `delete` it manually).
- **Thinking all objects share data members.** Data members are per-object. Only member functions are shared (one copy in code memory, not duplicated per object).
- **Confusing class relationships.** "Use-a" = one object calls another's method (a `Driver` uses a `Car`). "Has-a" = one class contains another as a data member (a `Car` has an `Engine`). These are different from "is-a" (inheritance).
- **Forgetting that messages = method calls.** In OOP theory, "sending a message" means calling a method. If the method is private, the message is rejected at compile time.
- **The class definition IS the interface.** Only `public` members form the interface. Private members are implementation details — outsiders can't call them even if they know the names.
- **Meta-class is an abstract concept, not C++ syntax.** Don't try to write `class ClassName : public meta_class` — C++ doesn't have meta-classes as a language feature (this lecture is theoretical).

---

## 4. HAND-CODING DRILLS

### Drill 1: Class from Description

A digital music player tracks songs. Each song has a title, artist name, and duration in seconds. Users can play a song (prints "Playing [title] by [artist]"), get the title, and get the duration. Write the full class definition with private data and public interface.

> [!success]- Show Answer
> ```cpp
> class Song {
> private:
>     char title[100];
>     char artist[100];
>     int duration; // in seconds
> public:
>     Song(const char t[], const char a[], int d) {
>         int i = 0;
>         while (t[i]) { title[i] = t[i]; i++; }
>         title[i] = '\0';
>         i = 0;
>         while (a[i]) { artist[i] = a[i]; i++; }
>         artist[i] = '\0';
>         duration = d;
>     }
>     void play() {
>         cout << "Playing " << title << " by " << artist << endl;
>     }
>     const char* getTitle() const { return title; }
>     int getDuration() const { return duration; }
> };
> ```

### Drill 2: Instantiation Styles

Given `class Widget { public: Widget(); Widget(int x); };`, write code that creates:
(a) A single Widget with default constructor on the stack
(b) An array of 5 default Widgets on the heap
(c) A single Widget with parameter 42 on the heap
Then show the `delete` statements needed to clean up (b) and (c).

> [!success]- Show Answer
> ```cpp
> Widget w1;                        // (a) stack, default ctor
> Widget* arr = new Widget[5];      // (b) heap array, 5x default ctor
> Widget* w2 = new Widget(42);      // (c) heap, parameterized ctor
> 
> delete[] arr;  // array delete for (b)
> delete w2;     // single delete for (c)
> // w1 is auto-destroyed when it goes out of scope
> ```

### Drill 3: Classification vs. Instantiation

Explain the difference between a class's "intentional notion" and "extensional notion" from the lecture. Then demonstrate both by writing a class `Library` that:
- Intentionally defines what a library is (shelves, books, name)
- Extensionally maintains a count of how many Library objects exist

> [!success]- Show Answer
> **Intentional notion** = the class as a template that defines STRUCTURE (what data and methods instances will have). It's the blueprint.
> **Extensional notion** = the class as a warehouse/factory that TRACKS all its instances. It knows what objects have been created.
>
> ```cpp
> class Library {
> private:
>     int numShelves;
>     int numBooks;
>     char name[50];
>     static int totalLibraries;  // extensional: tracks all instances
> public:
>     Library(const char n[], int shelves, int books) {
>         int i = 0;
>         while (n[i]) { name[i] = n[i]; i++; }
>         name[i] = '\0';
>         numShelves = shelves;
>         numBooks = books;
>         totalLibraries++;        // each new object increments count
>     }
>     ~Library() { totalLibraries--; }
>     static int getTotalLibraries() { return totalLibraries; }
> };
> int Library::totalLibraries = 0;
> ```
