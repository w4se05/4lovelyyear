# Lec6: Objects and Classes in C++ — Study Guide

---

## 1. CONCEPT CARD: Class Definition in C++

**What it is:** The concrete C++ syntax for defining a class — specifying data members, constructors, destructors, member functions, and access control — then creating objects from it.

**What problem it solves:** Knowing what a class IS conceptually (Lec5) doesn't help you write one that compiles. This lecture bridges theory to practice: where semicolons go, how constructors chain, why you need a destructor, how to copy objects safely, and what happens when one class contains another.

**How it works:**
1. Declare the class with `class Name { };` — members default to `private`.
2. Add a constructor (same name as class) to initialize new objects. If you don't write one, the compiler generates a default.
3. Add a destructor (`~ClassName()`) to clean up resources (dynamic memory especially). Called automatically when the object dies.
4. Member functions defined inside the class body are implicitly `inline`. Defined outside use `ClassName::functionName`.
5. For classes that own heap memory, you MUST write a copy constructor and assignment operator, or shallow copies will cause double-delete crashes.

**Concrete example:** A `Transcript` class for a university registration system. It holds a dynamically allocated array of course names. If you copy a `Transcript` using the compiler-generated copy constructor, both the original and copy will point to the SAME array. When one is destroyed (deleting the array), the other holds a dangling pointer. A **deep copy** constructor allocates a NEW array and copies the strings individually.

**What it is NOT:** A C++ class is NOT automatically safe. Unlike Java or C#, C++ gives you raw pointers and manual memory management. You are responsible for the Rule of Three: if your class needs a destructor, copy constructor, or assignment operator, it probably needs all three.

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
class ClassName {                    // Class declaration
private:                             // Data: hidden from outsiders
    int* data;                       // Dynamically allocated member
    int size;
public:
    ClassName(int sz);               // Constructor
    ClassName(const ClassName& other);// Copy constructor (deep copy)
    ~ClassName();                     // Destructor
    ClassName& operator=(const ClassName& other); // Assignment op
    int getValue(int i) const;       // const = won't modify *this
};                                   // SEMICOLON!!!

// Out-of-line definitions use scope resolution:
ClassName::ClassName(int sz) {       // Constructor body
    size = sz;                       // Copy scalar
    data = new int[size];           // Allocate new memory
}
ClassName::ClassName(const ClassName& other) { // Copy ctor
    size = other.size;               // Copy scalar
    data = new int[size];           // Allocate SEPARATE memory
    for (int i = 0; i < size; i++)   // Copy each element
        data[i] = other.data[i];
}
ClassName::~ClassName() {            // Destructor
    delete[] data;                   // Release owned memory
}
```

---

## 3. EXAM TRAPS

- **Forgetting the semicolon after the class closing brace.** This is the #1 syntax error on hand-written exams. `class Foo { };` — always.
- **Default copy constructor does a shallow copy.** If your class has `int* p = new int[10];`, the auto-generated copy constructor copies the pointer, not the pointed-to data. Two objects now share one array. When the first destructor runs `delete[] p`, the second object's pointer is dangling.
- **Calling `delete` on an array with `delete` instead of `delete[]`.** If you allocated with `new Type[size]`, you MUST free with `delete[]`. Plain `delete` only calls ONE destructor, leaks the rest, and is undefined behavior.
- **Constructor-initializer order depends on declaration order, NOT the order in the initializer list.** If `int x; int y;` are declared in that order, then `Foo() : y(5), x(y) {}` initializes x first (using uninitialized y!), then y.
- **`inline` is a suggestion, not a command.** The compiler can ignore it. "In-line" means defined inside the class body; "out-of-line" means defined outside with `ClassName::`.
- **`const` member functions cannot modify ANY data member.** Trying to do `x = 5;` inside a `const` function is a compile error. Non-const objects can call const functions, but const objects can ONLY call const functions.
- **Access is per-class, not per-object.** Inside `Date::Date(Date& d)`, you CAN write `d.month` even though `month` is private — `d` is the same class.
- **Friend functions/classes break encapsulation.** A `friend` declaration grants access to ALL private and protected members. Use sparingly.

---

## 4. HAND-CODING DRILLS

### Drill 1: Constructor and Destructor Trace

```cpp
class Game {
public:
    Game()  { cout << "G"; }
    ~Game() { cout << "~G"; }
};
class Player {
    Game g;
public:
    Player()  { cout << "P"; }
    ~Player() { cout << "~P"; }
};
int main() {
    Player p1;
    Player* p2 = new Player();
    delete p2;
    return 0;
}
```
**What is the exact output?** Write the sequence character by character.

> [!success]- Show Answer
> `GPGP~P~G~P~G`
>
> Why:
> - `Player p1;` → Game constructor runs first (member objects construct before the containing class body), so `G`, then Player body `P`. Output so far: `GP`
> - `new Player()` → same thing: `GP`. Output: `GPGP`
> - `delete p2` → destructions in REVERSE order: Player destructor `~P`, then Game destructor `~G`. Output: `GPGP~P~G`
> - `return 0` → p1 goes out of scope: `~P~G`. Final: `GPGP~P~G~P~G`

### Drill 2: Deep Copy — Find the Bug

```cpp
class Playlist {
    char** songs;
    int count;
public:
    Playlist(int c) {
        count = c;
        songs = new char*[count];
        for (int i = 0; i < count; i++)
            songs[i] = new char[50];
    }
    ~Playlist() {
        for (int i = 0; i < count; i++)
            delete[] songs[i];
        delete[] songs;
    }
};

int main() {
    Playlist p1(3);
    Playlist p2 = p1;  // <-- WHAT HAPPENS HERE?
}
```
Explain what goes wrong and write the missing copy constructor.

> [!success]- Show Answer
> The compiler-generated copy constructor does a **shallow copy**: `p2.songs` points to the same `char**` array as `p1.songs`. Both also share the same inner `char*` arrays. When `p2`'s destructor runs, it deletes all the arrays. Then `p1`'s destructor tries to delete them again → **double delete, undefined behavior/crash.**
>
> ```cpp
> Playlist(const Playlist& other) {
>     count = other.count;
>     songs = new char*[count];
>     for (int i = 0; i < count; i++) {
>         songs[i] = new char[50];
>         int j = 0;
>         while (other.songs[i][j]) {
>             songs[i][j] = other.songs[i][j];
>             j++;
>         }
>         songs[i][j] = '\0';
>     }
> }
> ```

### Drill 3: Composite Class — Constructor Order

You must write a `Laptop` class that contains a `CPU` object and a `Battery` object. The `CPU` constructor takes a string model name; `Battery` takes an int capacity in mAh. `Laptop` takes a brand name, CPU model, and battery capacity. Use **constructor initializer lists** (not assignment in the body). The `Laptop` constructor body prints "Laptop assembled". What does the full program output when `Laptop l("Dell", "i7-13700", 5000);` runs?

> [!success]- Show Answer
> ```cpp
> class CPU {
>     char model[20];
> public:
>     CPU(const char* m) {
>         int i = 0; while (m[i]) { model[i] = m[i]; i++; }
>         model[i] = '\0';
>         cout << "CPU(" << model << ") ";
>     }
> };
> class Battery {
>     int capacity;
> public:
>     Battery(int c) : capacity(c) {
>         cout << "Battery(" << capacity << "mAh) ";
>     }
> };
> class Laptop {
>     CPU cpu;
>     Battery battery;
>     char brand[20];
> public:
>     Laptop(const char* b, const char* cpuModel, int batCap)
>         : cpu(cpuModel), battery(batCap) {
>         int i = 0; while (b[i]) { brand[i] = b[i]; i++; }
>         brand[i] = '\0';
>         cout << "Laptop assembled";
>     }
> };
> ```
> Output: `CPU(i7-13700) Battery(5000mAh) Laptop assembled`
>
> Members construct in declaration order (CPU first, then Battery), regardless of initializer list order. Then the Laptop constructor body runs.
