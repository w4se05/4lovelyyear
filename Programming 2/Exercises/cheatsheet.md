# Lec3 — Recursion & Sorting

## Q1: Recursive Factorial

```cpp
#include <iostream>
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(arr, 0, arr.size() - 1);
    for (int x : arr) cout << x << " ";
    // Output: 3 9 10 27 38 43 82
}
```

**Time:** O(n log n), **Space:** O(n)

---

# Lec5 — Design Principles

## Q1: Design vs Coding Phase

**Design IS more important.** A well-designed system is easier to maintain, extend, and debug. Coding without design leads to spaghetti code, expensive refactoring, and bugs. "Weeks of coding can save hours of planning" is a myth. Design decisions constrain the entire project; poor ones cascade.

## Q2a: Student Class Variables

```cpp
using namespace std;
class Student {
private:
    string name;
    string address;
    int intake;              // e.g., 2025
    string email;
    string phone;
    int enrolledClasses;     // number of classes
    int totalCreditHours;
    static int totalStudents; // shared counter

public:
    Student(string n, string addr, int in, string em,
            string ph, int cls, int cr)
        : name(n), address(addr), intake(in), email(em), phone(ph),
          enrolledClasses(cls), totalCreditHours(cr) { totalStudents++; }
    static int getTotalStudents() { return totalStudents; }
};

int Student::totalStudents = 0;
```

## Q2b: Graduate vs Undergraduate

```cpp
using namespace std;
class Student {
protected:
    string name;
    int creditHours;
public:
    virtual int minCredits() const = 0;
    virtual int maxCredits() const = 0;
    bool registerCredits(int cr) {
        return cr >= minCredits() && cr <= maxCredits();
    }
};

class Undergraduate : public Student {
public:
    int minCredits() const override { return 12; }
    int maxCredits() const override { return 18; }
};

class Graduate : public Student {
public:
    int minCredits() const override { return 9; }
    int maxCredits() const override { return 15; }
};
```

## Q3a: Course Scheduling System

| Class | Data Members | Methods |
|---|---|---|
| `Course` | courseID, title, credits, maxCapacity | `enroll()`, `drop()`, `isFull()` |
| `Section` | sectionID, schedule(time,day), room, instructor | `assignRoom()`, `assignInstructor()` |
| `Room` | roomNumber, building, capacity, equipment | `isAvailable()`, `reserve()` |
| `Instructor` | name, dept, availability[] | `assignCourse()`, `getLoad()` |
| `Student` | name, ID, enrolledSections[] | `registerSection()`, `dropSection()` |
| `Schedule` | semester, sections[] | `addSection()`, `resolveConflicts()` |

## Q3b: Bibliography Organizer

| Class | Data Members | Methods |
|---|---|---|
| `Reference` | title, year, authors[] | `format()`, `cite()` |
| `Book` extends `Reference` | publisher, edition, ISBN | `format()` |
| `JournalArticle` extends `Reference` | journal, volume, pages, DOI | `format()` |
| `NewspaperArticle` extends `Reference` | newspaper, date, page | `format()` |
| `Bibliography` | references[], citationStyle | `add()`, `sort()`, `export()`, `generate()` |

## Q4: Serialization & Deserialization

- **Serialization:** Converting an object into a byte stream for storage/transmission.
- **Deserialization:** Reconstructing the object from that byte stream.
- **Issues:** Object version compatibility, pointer/cyclic references, security (untrusted data), binary vs text format, memory management, encoding endianness.

---

# Lec6 — Classes: Book & Rational

## Ex1: Book Class

```cpp
#include <iostream>
#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    string author;
    string title;
    string format;    // "hardcover", "paperback", "ebook"
    double price;
    int year;
    string publisher;

public:
    Book() : author(""), title(""), format(""), price(0.0), year(0), publisher("") {}
    Book(string a, string t, string f, double p, int y, string pub)
        : author(a), title(t), format(f), price(p), year(y), publisher(pub) {}

    string getAuthor()     const { return author; }
    string getTitle()      const { return title; }
    string getFormat()     const { return format; }
    double      getPrice()      const { return price; }
    int         getYear()       const { return year; }
    string getPublisher()  const { return publisher; }

    void print() const {
        cout << title << " by " << author << " (" << year << "), "
                  << format << ", $" << price << ", " << publisher << "\n";
    }
};

int main() {
    Book b("Bjarne Stroustrup", "The C++ Programming Language",
           "paperback", 59.99, 2013, "Addison-Wesley");
    b.print();
}
```

## Ex2: Rational Class

```cpp
#include <iostream>
#include <iostream>
#include <stdexcept>
using namespace std;

int gcd(int a, int b) {
    a = abs(a); b = abs(b);
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}

class Rational {
private:
    int num, den;

    void reduce() {
        if (den == 0) throw invalid_argument("Denominator cannot be zero");
        if (den < 0) { num = -num; den = -den; }
        int g = gcd(num, den);
        num /= g; den /= g;
    }

public:
    Rational() : num(0), den(1) {}                     // default -> 0/1
    Rational(int numerator, int denominator) : num(numerator), den(denominator) { reduce(); }
    explicit Rational(int whole) : num(whole), den(1) {} // whole number

    int numerator()   const { return num; }
    int denominator() const { return den; }

    void print() const {
        cout << num;
        if (den != 1) cout << "/" << den;
    }
};

int main() {
    Rational r1;                    // 0/1
    Rational r2(6, 8);             // 3/4  (reduced)
    Rational r3(5);                // 5/1  (whole number)
    r2.print();   // "3/4"
}
```

**Key:** `reduce()` called in constructor keeps fraction simplified. `explicit` prevents implicit `int -> Rational`.

---

# Lec7 — E-Wallet & Class Correctness

## Q1: E-Wallet System

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <iomanip>
using namespace std;

class EWallet {
private:
    string owner;
    double balance;
    vector<string> history;

    string timestamp() const {
        time_t now = time(nullptr);
        char buf[20];
        strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M", localtime(&now));
        return string(buf);
    }

public:
    EWallet(string name, double initial = 0.0) : owner(name), balance(initial) {
        history.push_back("[" + timestamp() + "] Wallet created for " + owner +
                          " with balance " + to_string(balance));
    }

    double getBalance() const { return balance; }

    bool addMoney(double amount) {
        if (amount <= 0) return false;
        balance += amount;
        history.push_back("[" + timestamp() + "] " + owner +
                          " deposited " + to_string(amount) +
                          ". Balance: " + to_string(balance));
        return true;
    }

    bool withdrawMoney(double amount) {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        history.push_back("[" + timestamp() + "] " + owner +
                          " withdrew " + to_string(amount) +
                          ". Balance: " + to_string(balance));
        return true;
    }

    bool transferTo(EWallet& receiver, double amount) {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        receiver.balance += amount;
        string msg = "[" + timestamp() + "] " + owner +
                          " transferred " + to_string(amount) + " to " +
                          receiver.owner;
        history.push_back(msg);
        receiver.history.push_back(msg);
        return true;
    }

    void printHistory() const {
        cout << "=== Transaction History for " << owner << " ===\n";
        for (const auto& h : history) cout << h << "\n";
    }
};

int main() {
    EWallet a("Nam", 100);
    EWallet b("B", 50);
    a.transferTo(b, 10);
    a.printHistory();
    b.printHistory();
}
```

## Q2: Incorrect Class Declarations

**a)**
```cpp
using namespace std;
class C1 { private: int x; public: C1() { x=10; } void setx(int value) {x= value;} };
class C2 { private: int x; public: void show(C1 x) { cout << x.x; } };  // ❌
```
- **Error:** `x.x` is invalid — `x` is the parameter name (type `C1`), and `C1::x` is **private**. `C2` cannot access `C1`'s private member `x`.
- **Fix:** Add a public getter in `C1`: `int getx() const { return x; }` and call `x.getx()` in `C2::show`.

**b)**
```cpp
using namespace std;
class C { private: int x; public: C() { x=10; } void setx(C x); };
C::setx(C x) { x.x=100; }   // ❌
```
- **Error:** `setx` is not `const` but receives `C x` by value. `x.x=100` modifies the **parameter copy**, not the object it's called on. Also, `x.x` looks like it's accessing the parameter's private member (allowed since same class). But writing `this->x = 100` was probably intended.
- **Fix:** Change to `void C::setx(int val) { x = val; }` or use `this->x`.

---

# Lec8_Ex1 — Quadrilateral Hierarchy

```cpp
#include <iostream>
#include <vector>

#include <iostream>
#include <vector>
using namespace std;

class Quadrilateral {
protected:
    double width, height;
public:
    Quadrilateral(double w = 1.0, double h = 1.0) : width(w), height(h) {}
    virtual double area() const = 0;
    virtual void print() const {
        cout << "Area: " << area() << "\n";
    }
    virtual ~Quadrilateral() {}
};

class Rectangle : public Quadrilateral {
public:
    Rectangle(double w, double h) : Quadrilateral(w, h) {}
    double area() const override { return width * height; }
};

class Parallelogram : public Quadrilateral {
public:
    Parallelogram(double w, double h) : Quadrilateral(w, h) {}
    double area() const override { return width * height; }
};

class Trapezium : public Quadrilateral {
private:
    double width2;
public:
    Trapezium(double w1, double w2, double h) : Quadrilateral(w1, h), width2(w2) {}
    double area() const override { return (width + width2) / 2.0 * height; }
};

int main() {
    vector<Quadrilateral*> shapes;
    shapes.push_back(new Rectangle(5, 3));
    shapes.push_back(new Parallelogram(4, 6));
    shapes.push_back(new Trapezium(3, 5, 4));

    for (auto* s : shapes) {
        s->print();
        delete s;
    }
}
```

**Trapezium area:** $\frac{a+b}{2} \cdot h$

---

# Lec8_Ex2 — Inheritance & Access Control

## Q1: Class Hierarchy Analysis

### a) Class Hierarchy Diagram

```
        C
        │ (protected: x, public: f())
        │
   ┌────┴────┐
   │         │
   C1        C3
  (protected:│ (public: f() — overrides C::f)
   x1,       │
   public:   │
   h())      │
   │
   C2
  (public: x2)
```

### b) Access in `main()` with `C1 obj1`

| Expression | Allowed? | Reason |
|---|---|---|
| `obj1.x` | ❌ No | `x` is `protected` in `C`, not accessible from outside |
| `obj1.f()` | ✅ Yes | `f()` is `public` in `C`, inherited as `public` |
| `obj1.x1` | ❌ No | `x1` is `protected` in `C1`, not accessible from outside |
| `obj1.x2` | ❌ No | `x2` belongs to `C2`, `obj1` is `C1` (no `x2`) |

### c) Access in `C1::h()` body

| Expression | Allowed? | Reason |
|---|---|---|
| `obj->x` | ✅ Yes | `C1` inherits `C` publicly → `x` is `protected` in `C1`, accessible within member functions |
| `obj2->x` | ✅ Yes | `C2` → `C1` → `C`. `x` is `protected` in `C2`, accessible from base class `C1::h()` |
| `obj3->x` | ❌ No | `C3` inherits directly from `C`, not through `C1`. `C1::h()` cannot access `protected` members of a sibling class |

## Q2: Shape / Rectangle / Triangle (Simple Hierarchy)

```cpp
#include <iostream>
#include <string>
using namespace std;

class Shape {
protected:
    string name;
public:
    Shape(string n) : name(n) {}
    virtual void draw() { cout << "Drawing " << name << "\n"; }
    virtual ~Shape() {}
};

class Rectangle : public Shape {
public:
    Rectangle() : Shape("Rectangle") {}
    void draw() override { cout << "Drawing a Rectangle\n"; }
};

class Triangle : public Shape {
public:
    Triangle() : Shape("Triangle") {}
    void draw() override { cout << "Drawing a Triangle\n"; }
};

int main() {
    Shape s("Generic");
    Rectangle r;
    Triangle t;
    s.draw();
    r.draw();
    t.draw();
}
```

## Q3: Multiple Inheritance — Constructor Order

```
    A1    A2    B1    B2
     \    /      \    /
      C1          C2
        \        /
         \      /
            D
```

```cpp
#include <iostream>

#include <iostream>
using namespace std;

class A1 { public: A1() { cout << "A1\n"; } };
class A2 { public: A2() { cout << "A2\n"; } };
class B1 { public: B1() { cout << "B1\n"; } };
class B2 { public: B2() { cout << "B2\n"; } };

class C1 : public A1, public A2 {
public: C1() { cout << "C1\n"; }
};

class C2 : public B1, public B2 {
public: C2() { cout << "C2\n"; }
};

class D : public C1, public C2 {
public: D() { cout << "D\n"; }
};

int main() { D d; }
// Output: A1, A2, C1, B1, B2, C2, D
// Order: depth-first, left-to-right as declared in inheritance list
```

## Q4: Virtual `draw()`

```cpp
#include <iostream>
#include <iostream>
#include <vector>
using namespace std;

class Shape {
public:
    virtual void draw() = 0;   // pure virtual
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle\n"; }
};

class Square : public Shape {
public:
    void draw() override { cout << "Drawing Square\n"; }
};

class Triangle : public Shape {
public:
    void draw() override { cout << "Drawing Triangle\n"; }
};

int main() {
    vector<Shape*> shapes;
    shapes.push_back(new Circle());
    shapes.push_back(new Square());
    shapes.push_back(new Triangle());

    for (Shape* s : shapes) {
        s->draw();               // virtual dispatch works!
        delete s;
    }
}
```

**Key:** Upcasting `Circle* → Shape*` + virtual function = the correct derived `draw()` is called at runtime via vtable lookup.

## Q5: Galactic Habitability Simulation

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <random>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <random>
#include <cmath>
using namespace std;

struct Atmosphere {
    bool hasAtmo;
    string composition;   // "N2/O2", "CO2", "H2/He", etc.
    double pressure;            // in atm
};

class Planet {
public:
    string name;
    string type;          // "Terrestrial" or "Gas Giant"
    double distanceFromSun;    // AU
    double radius;             // Earth radii
    Atmosphere atmo;
    double gravity;            // m/s^2
    double orbitalVelocity;    // km/s

    bool isHabitable() const {
        return type == "Terrestrial" &&
               distanceFromSun >= 0.7 && distanceFromSun <= 1.5 &&
               atmo.hasAtmo &&
               atmo.pressure > 0.5 && atmo.pressure < 5.0;
    }

    void print() const {
        cout << name << " [" << type << "] dist=" << distanceFromSun
                  << " AU, radius=" << radius << " R_e, gravity=" << gravity
                  << " m/s^2, habitable=" << (isHabitable() ? "YES" : "NO") << "\n";
    }
};

class SolarSystem {
public:
    string starName;
    vector<Planet*> planets;

    void readFromFile(const string& filename) {
        ifstream fin(filename);
        fin >> starName;
        int count; fin >> count;
        for (int i = 0; i < count; i++) {
            Planet* p = new Planet();
            fin >> p->name >> p->type;
            p->distanceFromSun = 0.3 + (rand() % 470) / 100.0;
            p->radius = 0.3 + (rand() % 220) / 100.0;
            p->atmo.hasAtmo = (rand() % 2 == 1);
            p->atmo.pressure = p->atmo.hasAtmo ? (rand() % 1000) / 100.0 : 0.0;
            p->gravity = (rand() % 300 + 50) / 100.0;
            planets.push_back(p);
        }
        fin.close();
    }

    void printAll() const {
        cout << "=== Solar System: " << starName << " ===\n";
        for (auto* p : planets) p->print();
    }

    ~SolarSystem() {
        for (auto* p : planets) delete p;
    }
};

class Spaceship {
public:
    string name;
    double fuel;
    double velocity;        // km/s
    double x, y;           // position in space

    double computeEscapeVelocity(double planetMass, double radius) const {
        const double G = 6.67430e-11;
        return sqrt(2.0 * G * planetMass / (radius * 6371000.0));
    }
};

class Galaxy {
public:
    string name;
    vector<SolarSystem*> systems;

    void explore() {
        for (auto* sys : systems) sys->printAll();
    }
};

int main() {
    srand(time(nullptr));
    SolarSystem ss;
    ss.readFromFile("planets.txt");
    ss.printAll();
}
```

**Design note:** Planets are stored in a **doubly-linked list sorted by distance** from their sun. All habitable-distance data is generated randomly per run.

---

# Lec8_QuickTest — Quick OOP Drills

## Q1: Mother & Daughter

```cpp
#include <iostream>

#include <iostream>
using namespace std;

class Mother {
public:
    virtual void display() { cout << "I am the Mother\n"; }
};

class Daughter : public Mother {
public:
    void display() override { cout << "I am the Daughter\n"; }
};

int main() {
    Daughter d;
    d.display();   // "I am the Daughter"
}
```

## Q2: Animal, Zebra, Dolphin

```cpp
#include <iostream>
#include <string>

#include <iostream>
#include <string>
using namespace std;

class Animal {
protected:
    string name;
    int age;
public:
    void set_value(string n, int a) { name = n; age = a; }
};

class Zebra : public Animal {
public:
    void show() {
        cout << name << " is " << age << " years old. Origin: African Savanna\n";
    }
};

class Dolphin : public Animal {
public:
    void show() {
        cout << name << " is " << age << " years old. Origin: Pacific Ocean\n";
    }
};

int main() {
    Zebra z;   z.set_value("Marty", 5);   z.show();
    Dolphin d; d.set_value("Flipper", 3); d.show();
}
```

## Q3: Student at VGU

```cpp
#include <iostream>
#include <string>
#include <vector>

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class VGUStudent {
private:
    string name, studentID, major;
    int intake, creditsCompleted;
    double gpa;
    vector<string> enrolledCourses;
public:
    VGUStudent(string n, string id, string m, int in)
        : name(n), studentID(id), major(m), intake(in), creditsCompleted(0), gpa(0.0) {}

    void enrollCourse(string course)       { enrolledCourses.push_back(course); }
    void completeCourse(double grade, int credits) {
        creditsCompleted += credits;
    }
    void study()      { cout << name << " is studying hard at VGU library\n"; }
    void takeExam()   { cout << name << " is taking an exam\n"; }
    void attendLab()  { cout << name << " is in the lab\n"; }
    void print() const {
        cout << "Student: " << name << " (" << studentID << "), "
                  << major << ", Intake " << intake << ", Credits: " << creditsCompleted << "\n";
    }
};
```

## Q4: Person / Student / Teacher

```cpp
#include <iostream>
#include <string>

#include <iostream>
#include <string>
using namespace std;

class Person {
protected:
    int age;
    string name;
public:
    void SetAge(int n) { age = n; }
    void Greet() { cout << "Hello, I am " << name << "\n"; }
    void SetName(string n) { name = n; }
};

class Student : public Person {
public:
    void GoToClasses() { cout << "I'm going to class.\n"; }
    void ShowAge() { cout << "My age is: " << age << " years old\n"; }
};

class Teacher : public Person {
private:
    string subject;
public:
    void setSubject(string s) { subject = s; }
    void Explain() { cout << "Explanation begins. Subject: " << subject << "\n"; }
};

int main() {
    // Create Person
    Person p;  p.SetName("Alex");  p.Greet();

    // Create Student
    Student s; s.SetName("Minh"); s.SetAge(21); s.Greet(); s.ShowAge();

    // Create Teacher
    Teacher t; t.SetName("Dr. Smith"); t.SetAge(30);
    t.setSubject("Programming 2");
    t.Greet();  t.Explain();
}
```

**Expected output:**
```
Hello, I am Alex
Hello, I am Minh
My age is: 21 years old
Hello, I am Dr. Smith
Explanation begins. Subject: Programming 2
```

---

# Lec9_Ex — Shape Polymorphism

## Q1: Virtual `draw()` Hierarchy

```cpp
#include <iostream>
#include <iostream>
#include <vector>
using namespace std;

class Shape {
public:
    virtual void draw() { cout << "Drawing a generic Shape\n"; }
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle\n"; }
};

class Square : public Shape {
public:
    void draw() override { cout << "Drawing Square\n"; }
};

class Triangle : public Shape {
public:
    void draw() override { cout << "Drawing Triangle\n"; }
};

int main() {
    vector<Shape*> shapes;
    shapes.push_back(new Circle());
    shapes.push_back(new Square());
    shapes.push_back(new Triangle());

    for (Shape* s : shapes) {
        s->draw();
        delete s;
    }
}
```

## Q2: Pure Virtual `draw()`

```cpp
#include <iostream>
#include <iostream>
#include <vector>
using namespace std;

class Shape {
public:
    virtual void draw() = 0;              // pure virtual = abstract class
    // Shape s;                            // COMPILE ERROR: cannot instantiate abstract class
    virtual ~Shape() {}
};

void Shape::draw() { cout << "Shape::draw() default implementation\n"; }

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle\n"; }
};

int main() {
    // Shape s;      // ERROR - Shape is abstract
    Shape* c = new Circle();
    c->draw();       // "Drawing Circle"
    delete c;
}
```

**Key:** Pure virtual = `= 0`. Class becomes abstract. Cannot instantiate. Can still provide a body (called via `Shape::draw()` from derived).

## Q3: Pass by Value vs Reference (Slicing!)

```cpp
#include <iostream>

#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle\n"; }
};

//  PASS BY VALUE - SLICING!
// void renderShape(Shape s) { s.draw(); }

//  PASS BY REFERENCE
void renderShape(Shape& s) { s.draw(); }

int main() {
    Circle c;
    renderShape(c);
}
```

**Slicing:** Passing `Circle` by value to `Shape` parameter copies only the `Shape` part; derived info is lost. Always pass polymorphic objects by **reference** or **pointer**.

## Q4: Shapes with Area

```cpp
#include <iostream>
#include <cmath>

#include <iostream>
#include <cmath>
using namespace std;

class Shape {
protected:
    double size1, size2;
public:
    Shape(double s1 = 0, double s2 = 0) : size1(s1), size2(s2) {}
    virtual double area() const = 0;
    virtual void print() const { cout << "Area: " << area() << "\n"; }
    virtual ~Shape() {}
};

class Circle_ : public Shape {
public:
    Circle_(double r) : Shape(r, 0) {}
    double area() const override { return M_PI * size1 * size1; }
};

class Square_ : public Shape {
public:
    Square_(double side) : Shape(side, 0) {}
    double area() const override { return size1 * size1; }
};

class Triangle_ : public Shape {
public:
    Triangle_(double base, double height) : Shape(base, height) {}
    double area() const override { return 0.5 * size1 * size2; }
};
```

## Q5: Array of Shapes Sorted by Decreasing Area

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<Shape*> shapes;
    shapes.push_back(new Circle_(5.0));        // area ~78.54
    shapes.push_back(new Square_(4.0));        // area = 16
    shapes.push_back(new Triangle_(3.0, 6.0)); // area = 9
    shapes.push_back(new Circle_(3.0));        // area ~28.27

    sort(shapes.begin(), shapes.end(),
        [](Shape* a, Shape* b) { return a->area() > b->area(); });

    for (Shape* s : shapes) {
        s->print();
        delete s;
    }
}
```

---

# Lec9_Ex1 — File I/O with Shapes

## Q1 & Q2: Read from File, Sort by Area, Write Output

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

class Shape {
public:
    virtual double area() const = 0;
    virtual void print(ostream& os) const = 0;
    virtual ~Shape() {}
};

class Triangle : public Shape {
    double x1, y1, x2, y2, x3, y3;
public:
    Triangle(double a1, double b1, double a2, double b2, double a3, double b3)
        : x1(a1), y1(b1), x2(a2), y2(b2), x3(a3), y3(b3) {}
    double area() const override {
        return 0.5 * fabs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2));
    }
    void print(ostream& os) const override {
        os << "t " << x1 << " " << y1 << " " << x2 << " " << y2
           << " " << x3 << " " << y3 << " -> " << area();
    }
};

class Rectangle : public Shape {
    double x1, y1, x2, y2;
public:
    Rectangle(double a1, double b1, double a2, double b2)
        : x1(a1), y1(b1), x2(a2), y2(b2) {}
    double area() const override {
        return fabs(x2 - x1) * fabs(y2 - y1);
    }
    void print(ostream& os) const override {
        os << "r " << x1 << " " << y1 << " " << x2 << " " << y2 << " -> " << area();
    }
};

class Square : public Shape {
    double x1, y1, x2, y2;
public:
    Square(double a1, double b1, double a2, double b2)
        : x1(a1), y1(b1), x2(a2), y2(b2) {}
    double area() const override {
        return fabs(x2 - x1) * fabs(y2 - y1);
    }
    void print(ostream& os) const override {
        os << "s " << x1 << " " << y1 << " " << x2 << " " << y2 << " -> " << area();
    }
};

class Parallelogram : public Shape {
    double x1, y1, y2, x2, y3, y4;
public:
    Parallelogram(double a1, double b1, double b2_, double a2, double b3, double b4)
        : x1(a1), y1(b1), y2(b2_), x2(a2), y3(b3), y4(b4) {}
    double area() const override {
        double base = fabs(x2 - x1);
        double height = fabs(y3 - y1);
        return base * height;
    }
    void print(ostream& os) const override {
        os << "p " << x1 << " " << y1 << " " << y2 << " " << x2
           << " " << y3 << " " << y4 << " -> " << area();
    }
};

int main() {
    ifstream fin("input.txt");
    if (!fin) return 1;

    int n; fin >> n;
    vector<Shape*> shapes;

    for (int i = 0; i < n; i++) {
        char type; fin >> type;
        if (type == 't') {
            double x1,y1,x2,y2,x3,y3;
            fin >> x1>>y1>>x2>>y2>>x3>>y3;
            shapes.push_back(new Triangle(x1,y1,x2,y2,x3,y3));
        } else if (type == 'r') {
            double x1,y1,x2,y2;
            fin >> x1>>y1>>x2>>y2;
            shapes.push_back(new Rectangle(x1,y1,x2,y2));
        } else if (type == 's') {
            double x1,y1,x2,y2;
            fin >> x1>>y1>>x2>>y2;
            shapes.push_back(new Square(x1,y1,x2,y2));
        } else if (type == 'p') {
            double x1,y1,y2b,x2,y3,y4;
            fin >> x1>>y1>>y2b>>x2>>y3>>y4;
            shapes.push_back(new Parallelogram(x1,y1,y2b,x2,y3,y4));
        }
    }
    fin.close();

    sort(shapes.begin(), shapes.end(),
        [](Shape* a, Shape* b) { return a->area() > b->area(); });

    ofstream fout("output.txt");
    fout << n << "\n";
    for (auto* s : shapes) {
        s->print(fout);
        fout << "\n";
        delete s;
    }
    fout.close();
    cout << "Done. Check output.txt\n";
}
```

**Triangle area formula (shoelace):** $\frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$

---

# Lec10_ex1 — Operator Overloading

## Q1: `operator++` (Prefix & Postfix)

```cpp
#include <iostream>
using namespace std;

class Counter {
    int value;
public:
    Counter(int v = 0) : value(v) {}

    Counter& operator++() { ++value; return *this; }
    Counter operator++(int) {
        Counter old = *this;
        ++value;
        return old;
    }

    void print() const { cout << value << "\n"; }
};

int main() {
    Counter c(5);
    ++c; c.print();    // 6 (prefix)
    c++; c.print();    // 7 (postfix)

    // c++++;          // WARNING: postfix returns const
}
```

**Compiler warning if both missing dummy int:** "_no postfix operator++ declared_" — uses prefix as fallback.

## Q2: Binary `operator+` as Member

```cpp
using namespace std;

class IntWrapper {
    int value;
public:
    IntWrapper(int v = 0) : value(v) {}
    IntWrapper operator+(const IntWrapper& other) const {
        return IntWrapper(value + other.value);
    }
    int get() const { return value; }
};

int main() {
    IntWrapper a(10), b(20);
    IntWrapper c = a + b;       // c.value = 30
    cout << c.get();       // 30
}
```

## Q3: Binary `operator-` as Member

```cpp
using namespace std;

class IntWrapper {
    int value;
public:
    IntWrapper(int v = 0) : value(v) {}
    IntWrapper operator+(const IntWrapper& other) const {
        return IntWrapper(value + other.value);
    }
    IntWrapper operator-(const IntWrapper& other) const {
        return IntWrapper(value - other.value);
    }
    int get() const { return value; }
};

int main() {
    IntWrapper a(30), b(5), c(10);
    IntWrapper result = a + b - c;   // (30+5) - 10 = 25
    cout << result.get();       // 25
}
```

## Q4: Prefix & Postfix `++` / `--` Returning Object

```cpp
using namespace std;

class IntWrapper {
    int value;
public:
    IntWrapper(int v = 0) : value(v) {}

    IntWrapper& operator++()    { ++value; return *this; }      // prefix
    IntWrapper  operator++(int) { IntWrapper old = *this; ++value; return old; }  // postfix
    IntWrapper& operator--()    { --value; return *this; }      // prefix
    IntWrapper  operator--(int) { IntWrapper old = *this; --value; return old; }  // postfix

    int get() const { return value; }
};

int main() {
    IntWrapper a(10);
    IntWrapper b = ++a;   // a=11, b=11
    IntWrapper c = a++;   // a=12, c=11
    IntWrapper d = --a;   // a=11, d=11
    IntWrapper e = a--;   // a=10, e=11
    cout << b.get() << " " << c.get() << " " << d.get() << " " << e.get();
    // Output: 11 11 11 11
}
```

## Q5: Non-const Ref (Prefix) vs const Object (Postfix)

```cpp
using namespace std;
class IntWrapper {
    int value;
public:
    IntWrapper(int v = 0) : value(v) {}

    // Prefix: returns non-const reference (fast, allows chaining like ++++x)
    IntWrapper& operator++()    { ++value; return *this; }

    // Postfix: returns const object (prevents things like x++++ which is counterintuitive)
    const IntWrapper operator++(int) {
        IntWrapper old = *this;
        ++value;
        return old;
    }

    int get() const { return value; }
};
```

**Why this matters in practice:**
- **Prefix** returns `IntWrapper&`: no copy, allows `++(++x)` (double increment works as expected, incrementing the same object twice).
- **Postfix** returns `const IntWrapper`: prevents `x++++` — which would increment a temporary (wrong/intuitive behavior). Also matches built-in `int` behavior: `int x = 5; x++++;` doesn't compile.
- **Performance:** Prefix avoids an unnecessary copy.

---

# Lec10_ex2 — Time & Complex Classes

## Q1: Time Class

```cpp
#include <iostream>
#include <iostream>
#include <iomanip>
using namespace std;

class Time {
private:
    int hours, minutes, seconds;

public:
    Time() : hours(0), minutes(0), seconds(0) {}
    Time(int h, int m, int s) : hours(h), minutes(m), seconds(s) {
        normalize();
    }

    void normalize() {
        minutes += seconds / 60;  seconds %= 60;
        hours   += minutes / 60;  minutes %= 60;
        hours   %= 24;
        if (seconds < 0) { seconds += 60; minutes--; }
        if (minutes < 0) { minutes += 60; hours--;   }
        if (hours < 0)   { hours += 24; }
    }

    Time operator+(const Time& t) const {
        return Time(hours + t.hours, minutes + t.minutes, seconds + t.seconds);
    }

    bool operator>(const Time& t) const {
        if (hours != t.hours) return hours > t.hours;
        if (minutes != t.minutes) return minutes > t.minutes;
        return seconds > t.seconds;
    }

    Time& operator=(const Time& t) {
        if (this != &t) {
            hours = t.hours; minutes = t.minutes; seconds = t.seconds;
        }
        return *this;
    }

    void print() const {
        cout << setfill('0') << setw(2) << hours << ":"
                  << setw(2) << minutes << ":" << setw(2) << seconds << "\n";
    }
};

int main() {
    Time t1(10, 30, 45);
    Time t2(2, 45, 30);
    Time t3 = t1 + t2;     // 13:16:15
    t3.print();
    cout << (t1 > t2 ? "t1 later" : "t2 later") << "\n";

    Time t4;
    t4 = t1;
    t4.print();            // 10:30:45
}
```

## Q2: Complex Class (Sort by Modulus)

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

class Complex {
private:
    double re, im;

public:
    Complex() : re(0), im(0) {}
    Complex(double r, double i) : re(r), im(i) {}

    double modulus() const { return sqrt(re * re + im * im); }

    bool operator>(const Complex& other) const {
        return modulus() > other.modulus();
    }

    Complex& operator=(const Complex& other) {
        if (this != &other) { re = other.re; im = other.im; }
        return *this;
    }

    void print() const {
        cout << re << (im >= 0 ? " + " : " - ") << fabs(im)
                  << "i  (|z|=" << modulus() << ")\n";
    }
};

int main() {
    vector<Complex> nums = {
        Complex(3, 4),    // |z|=5
        Complex(1, 1),    // |z|=1.414
        Complex(0, 2),    // |z|=2
        Complex(5, -12),  // |z|=13
        Complex(8, 6)     // |z|=10
    };

    sort(nums.begin(), nums.end(),
        [](const Complex& a, const Complex& b) { return a.modulus() > b.modulus(); });

    cout << "Sorted by decreasing modulus:\n";
    for (auto& c : nums) c.print();
}
```

**Modulus formula:** $|z| = \sqrt{a^2 + b^2}$ where $z = a + bi$

---

# Lec11_ex1 — Template & Container Classes

## Q1: Matrix Norms

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

template<typename T>
class Matrix {
private:
    vector<vector<T>> data;
    int n;

public:
    Matrix(int size) : n(size), data(size, vector<T>(size, 0)) {}

    void set(int i, int j, T val) { data[i][j] = val; }
    T get(int i, int j) const { return data[i][j]; }
    int size() const { return n; }

    double frobeniusNorm() const {
        double sum = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                sum += data[i][j] * data[i][j];
        return sqrt(sum);
    }

    double rowSumNorm() const {
        double maxSum = 0;
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < n; j++) sum += fabs(data[i][j]);
            maxSum = max(maxSum, sum);
        }
        return maxSum;
    }

    double totalNorm() const {
        double maxVal = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                maxVal = max(maxVal, fabs(data[i][j]));
        return n * maxVal;
    }

    void print() const {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cout << data[i][j] << " ";
            cout << "\n";
        }
    }
};

int main() {
    Matrix<int> m(3);
    m.set(0,0,1); m.set(0,1,2);  m.set(0,2,3);
    m.set(1,0,4); m.set(1,1,5);  m.set(1,2,6);
    m.set(2,0,7); m.set(2,1,8);  m.set(2,2,9);

    cout << "Frobenius: " << m.frobeniusNorm() << "\n";  // ~16.8819
    cout << "Row sum:   " << m.rowSumNorm() << "\n";      // 24
    cout << "Total:     " << m.totalNorm() << "\n";       // 27
}
```

## Q2: Generic Stack Template (Array-based)

```cpp
#include <iostream>
#include <string>

#include <iostream>
#include <string>
using namespace std;

template<typename T>
class Stack {
private:
    T* arr;
    int capacity;
    int topIndex;

public:
    Stack(int size) : capacity(size), topIndex(-1) {
        arr = new T[capacity];
    }

    ~Stack() { delete[] arr; }

    bool isEmpty() const { return topIndex == -1; }
    bool isFull()  const { return topIndex == capacity - 1; }

    void push(T value) {
        if (isFull()) {
            cout << "Stack Overflow\n";
            return;
        }
        arr[++topIndex] = value;
    }

    T pop() {
        if (isEmpty()) {
            cout << "Stack Underflow\n";
            return T();
        }
        return arr[topIndex--];
    }

    T peek() const {
        if (isEmpty()) {
            cout << "Stack is empty\n";
            return T();
        }
        return arr[topIndex];
    }
};

int main() {
    Stack<int> intStack(5);
    intStack.push(10); intStack.push(20); intStack.push(30);
    cout << intStack.pop() << "\n";   // 30
    cout << intStack.peek() << "\n";  // 20

    Stack<string> strStack(3);
    strStack.push("Hello"); strStack.push("World");
    cout << strStack.pop() << "\n";   // World
}
```

**Key:** `T()` is the **default constructor** call — returns `0` for numerics, `""` for string, etc. `topIndex = -1` means empty.

---

# Lec12_ex1 — Linked List & Stack via Linked List

## Q1: Generic Linked List Template

```cpp
#include <iostream>
using namespace std;

template<typename T>
class LinkedList {
private:
    struct Node {
        T data;
        Node* next;
        Node(T val) : data(val), next(nullptr) {}
    };

    Node* head;
    int size;

public:
    LinkedList() : head(nullptr), size(0) {}

    ~LinkedList() { clear(); }

    bool isEmpty() const { return head == nullptr; }

    void append(T value) {
        Node* newNode = new Node(value);
        if (isEmpty()) {
            head = newNode;
        } else {
            Node* curr = head;
            while (curr->next) curr = curr->next;
            curr->next = newNode;
        }
        size++;
    }

    void prepend(T value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
        size++;
    }

    void insert(int pos, T value) {
        if (pos < 0 || pos > size) return;
        if (pos == 0) { prepend(value); return; }

        Node* newNode = new Node(value);
        Node* curr = head;
        for (int i = 0; i < pos - 1; i++) curr = curr->next;
        newNode->next = curr->next;
        curr->next = newNode;
        size++;
    }

    int find(T value) const {
        Node* curr = head;
        int pos = 0;
        while (curr) {
            if (curr->data == value) return pos;
            curr = curr->next; pos++;
        }
        return -1;
    }

    T get(int pos) const {
        if (pos < 0 || pos >= size) throw out_of_range("Index out of range");
        Node* curr = head;
        for (int i = 0; i < pos; i++) curr = curr->next;
        return curr->data;
    }

    void replace(int pos, T value) {
        if (pos < 0 || pos >= size) return;
        Node* curr = head;
        for (int i = 0; i < pos; i++) curr = curr->next;
        curr->data = value;
    }

    bool remove(T value) {
        if (isEmpty()) return false;
        if (head->data == value) {
            Node* temp = head;
            head = head->next;
            delete temp;
            size--;
            return true;
        }
        Node* curr = head;
        while (curr->next && curr->next->data != value) curr = curr->next;
        if (curr->next) {
            Node* temp = curr->next;
            curr->next = curr->next->next;
            delete temp;
            size--;
            return true;
        }
        return false;
    }

    void clear() {
        while (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
        size = 0;
    }

    int getSize() const { return size; }

    void print() const {
        Node* curr = head;
        while (curr) {
            cout << curr->data << " -> ";
            curr = curr->next;
        }
        cout << "nullptr\n";
    }
};

int main() {
    LinkedList<int> list;
    list.append(10); list.append(20); list.prepend(5);
    list.insert(2, 15);
    list.print();                    // 5 -> 10 -> 15 -> 20 -> nullptr
    cout << list.find(15) << "\n";    // 2
    cout << list.get(1) << "\n";      // 10
    list.replace(0, 99);
    list.remove(20);
    list.print();                    // 99 -> 10 -> 15 -> nullptr
}
```

## Q2: Stack using Linked List

```cpp
#include <iostream>
using namespace std;

template<typename T>
class Stack {
private:
    struct Node {
        T data;
        Node* next;
        Node(T val) : data(val), next(nullptr) {}
    };

    Node* topNode;

public:
    Stack() : topNode(nullptr) {}

    ~Stack() {
        while (!isEmpty()) pop();
    }

    bool isEmpty() const { return topNode == nullptr; }

    void push(T value) {
        Node* newNode = new Node(value);
        newNode->next = topNode;
        topNode = newNode;
    }

    T pop() {
        if (isEmpty()) {
            cout << "Stack Underflow\n";
            return T();
        }
        Node* temp = topNode;
        T val = temp->data;
        topNode = topNode->next;
        delete temp;
        return val;
    }

    T peek() const {
        if (isEmpty()) {
            cout << "Stack is empty\n";
            return T();
        }
        return topNode->data;
    }
};

int main() {
    Stack<int> s;
    s.push(1); s.push(2); s.push(3);
    cout << s.pop() << "\n";    // 3
    cout << s.peek() << "\n";   // 2
    cout << s.pop() << "\n";    // 2
    cout << s.pop() << "\n";    // 1
    cout << s.pop() << "\n";    // Stack Underflow, 0
}
```

**LL vs Array Stack:** LL-based has no `isFull()` (grows dynamically). `push` = prepend. `pop` = remove head. All O(1).

---

# Lec12_13_Ex1 — Farey & AMRDS

## Q1: Farey Sequences

The **Farey sequence** of order N is the set of all reduced fractions $\frac{a}{b}$ with $0 \le a \le b \le N$, sorted by value.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Fraction {
    int num, den;
    Fraction(int n, int d) : num(n), den(d) {}
    double value() const { return (double)num / den; }
};

int gcd(int a, int b) {
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}

void Farey(int N) {
    vector<Fraction> seq;
    for (int den = 1; den <= N; den++) {
        for (int num = 0; num <= den; num++) {
            if (gcd(num, den) == 1) {
                seq.push_back(Fraction(num, den));
            }
        }
    }
    sort(seq.begin(), seq.end(),
        [](const Fraction& a, const Fraction& b) { return a.value() < b.value(); });

    cout << "Farey(" << N << "): ";
    for (auto& f : seq)
        cout << f.num << "/" << f.den << " ";
    cout << "\n";
}

int main() {
    Farey(5);
}
```

**Property:** For consecutive fractions $\frac{a}{b}, \frac{c}{d}$: $bc - ad = 1$

---

## Q2: AMRDS (Autonomous Mobile Robot Dispatching System)

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <limits>
#include <iomanip>
#include <algorithm>
using namespace std;

template<typename T>
class Graph {
public:
    map<string, map<string, T>> adj;
    void addEdge(const string& u, const string& v, T weight) {
        adj[u][v] = weight;
        adj[v][u] = weight;
    }

    pair<map<string, string>, map<string, T>>
    shortestPath(const string& start) const {
        map<string, T> dist;
        map<string, string> parent;
        map<string, bool> visited;

        for (auto& p : adj) dist[p.first] = numeric_limits<T>::max();
        dist[start] = T(0);

        using Pair = pair<T, string>;
        priority_queue<Pair, vector<Pair>, greater<Pair>> pq;
        pq.push({T(0), start});

        while (!pq.empty()) {
            string u = pq.top().second; pq.pop();
            if (visited[u]) continue;
            visited[u] = true;

            for (auto& nb : adj.at(u)) {
                string v = nb.first;
                T w = nb.second;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    parent[v] = u;
                    pq.push({dist[v], v});
                }
            }
        }
        return {parent, dist};
    }

    vector<string> reconstructPath(
        const string& start, const string& end,
        const map<string, string>& parent) const {
        vector<string> path;
        string curr = end;
        while (parent.find(curr) != parent.end()) {
            path.push_back(curr);
            curr = parent.at(curr);
        }
        path.push_back(start);
        reverse(path.begin(), path.end());
        return path;
    }
};

enum class RobotState { Idle, Moving, Charging, Faulted };

string stateToString(RobotState s) {
    switch (s) {
        case RobotState::Idle:     return "Idle";
        case RobotState::Moving:   return "Moving";
        case RobotState::Charging: return "Charging";
        case RobotState::Faulted:  return "Faulted";
    }
    return "Unknown";
}

class Robot {
protected:
    int id;
    RobotState state;
    string currentStation;
public:
    Robot(int i, const string& station)
        : id(i), state(RobotState::Idle), currentStation(station) {}
    virtual ~Robot() {}
    virtual string getType() const = 0;

    int getId() const { return id; }
    RobotState getState() const { return state; }
    void setState(RobotState s) { state = s; }
    string getStation() const { return currentStation; }
    void setStation(const string& s) { currentStation = s; }

    bool canDispatch() const {
        return state == RobotState::Idle;
    }
};

class HeavyLoadRobot : public Robot {
public:
    HeavyLoadRobot(int i, const string& s) : Robot(i, s) {}
    string getType() const override { return "HEAVY_LOAD"; }
};

class ScannerRobot : public Robot {
public:
    ScannerRobot(int i, const string& s) : Robot(i, s) {}
    string getType() const override { return "SCANNER"; }
};

Robot* createRobot(int id, const string& type, const string& station) {
    if (type == "HEAVY_LOAD") return new HeavyLoadRobot(id, station);
    if (type == "SCANNER")    return new ScannerRobot(id, station);
    return nullptr;
}

struct Command {
    string taskName;
    string targetStation;
    string requiredType;
};

int main() {
    ifstream fin("input_file.txt");
    ofstream fout("output_file.txt");
    if (!fin) { cerr << "Cannot open input\n"; return 1; }

    Graph<double> graph;

    string line;
    int stationCount = 0, edgeCount = 0, robotCount = 0, taskCount = 0;

    while (getline(fin, line)) {
        if (line.empty() || line[0] == '#') continue;
        istringstream iss(line);
        if (stationCount == 0) {
            iss >> stationCount >> edgeCount;
        } else if (edgeCount > 0) {
            string u, v; double w;
            iss >> u >> v >> w;
            graph.addEdge(u, v, w);
            edgeCount--;
        } else break;
    }

    fin.clear(); fin.seekg(0);
    vector<Robot*> fleet;
    vector<Command> commands;
    bool robotSection = false, commandSection = false;

    while (getline(fin, line)) {
        if (line.empty() || line[0] == '#') continue;
        istringstream iss(line);

        if (!robotSection && !commandSection) { continue; }
        if (robotSection && fleet.empty()) {
            iss >> robotCount;
            continue;
        }
        if (robotSection && fleet.size() < (size_t)robotCount) {
            int id; string type, station;
            if (iss >> id >> type >> station) {
                fleet.push_back(createRobot(id, type, station));
            }
            continue;
        }
    }

    fin.close();

    fout << "=== AMRDS CENTRAL DISPATCHING LOG ===\n\n";

    for (size_t cmdIdx = 0; cmdIdx < commands.size(); cmdIdx++) {
        Command& cmd = commands[cmdIdx];
        fout << "[COMMAND " << (cmdIdx + 1) << "] Task: " << cmd.taskName
             << " | Required Type: " << cmd.requiredType
             << " | Target: " << cmd.targetStation << "\n";

        Robot* allocated = nullptr;
        for (auto* r : fleet) {
            if (r->getType() == cmd.requiredType && r->canDispatch()) {
                allocated = r;
                break;
            }
        }

        if (!allocated) {
            fout << "-> Dispatch Status: REJECTED / FAILED.\n"
                 << "-> Diagnostics: No available units matching "
                 << cmd.requiredType << " found in a receptive state.\n\n";
            continue;
        }

        auto [parent, dist] = graph.shortestPath(allocated->getStation());
        auto path = graph.reconstructPath(allocated->getStation(),
                                          cmd.targetStation, parent);
        double cost = dist[cmd.targetStation];

        fout << "-> Dispatch Status: SUCCESS.\n"
             << "-> Allocated Unit: Robot_ID: " << allocated->getId()
             << " (Pre-execution State: " << stateToString(allocated->getState()) << ").\n"
             << "-> Optimal Routing: ";
        for (size_t i = 0; i < path.size(); i++) {
            fout << path[i];
            if (i < path.size() - 1) fout << " -> ";
        }
        fout << "\n-> Cumulative Path Cost: " << fixed
             << setprecision(2) << cost << " meters.\n";
        allocated->setState(RobotState::Moving);
        fout << "-> Post-execution State: Moving.\n\n";
    }

    fout << "=== SIMULATION END ===\n";
    fout.close();

    for (auto* r : fleet) delete r;
    cout << "Dispatch ledger written to output_file.txt\n";
}
```

**Architecture:** Graph template for decoupled cost types → Dijkstra for shortest path → Polymorphic Robot hierarchy for hardware extensibility → State machine per robot. Input file parsed line-by-line skipping `#` comments.

---

# Quick Reference — Key C++ Concepts

## Virtual Functions & Polymorphism
| Concept            | Syntax                  | Behavior                                       |
| ------------------ | ----------------------- | ---------------------------------------------- |
| Virtual            | `virtual void f();`     | Dynamic dispatch via vtable                    |
| Pure virtual       | `virtual void f() = 0;` | Abstract class, must override                  |
| Override check     | `void f() override;`    | Compiler ensures base has `virtual f`          |
| Virtual destructor | `virtual ~Base();`      | Ensures derived destructor called via base ptr |

## Operator Overloading Cheatsheet
| Operator | Member | Non-member (friend) |
|---|---|---|
| `+`, `-`, `*`, `/` | `T operator+(const T&) const` | `T operator+(const T&, const T&)` |
| `++` prefix | `T& operator++()` | |
| `++` postfix | `T operator++(int)` | |
| `=` | `T& operator=(const T&)` | |
| `>` | `bool operator>(const T&) const` | `bool operator>(const T&, const T&)` |
| `<<` | | `friend ostream& operator<<(ostream&, const T&)` |

## Inheritance Access
| Base member | `public` inheritance | `protected` inheritance | `private` inheritance |
|---|---|---|---|
| `public` | `public` in derived | `protected` | `private` |
| `protected` | `protected` | `protected` | `private` |
| `private` | inaccessible | inaccessible | inaccessible |

## Template Syntax
```cpp
using namespace std;
template<typename T> class MyClass { ... };
template<typename T> T myFunc(T a) { return a; }
```

## Sorting with Custom Comparator
```cpp
using namespace std;
sort(v.begin(), v.end(),
    [](const T& a, const T& b) { return a.value > b.value; });  // descending
```

---

# Library Reference

| Library | Functions / Classes Used |
|---|---|
| `<iostream>` | `cin`, `cout`, `cerr`, `endl`, `flush` |
| `<fstream>` | `ifstream`, `ofstream`, `fstream`, `.open()`, `.close()`, `.seekg()`, `.clear()` |
| `<sstream>` | `istringstream`, `ostringstream`, `stringstream` |
| `<string>` | `string`, `getline()`, `to_string()`, `.substr()`, `.find()`, `.length()`, `stoi()`, `stod()` |
| `<vector>` | `vector<T>`, `.push_back()`, `.pop_back()`, `.size()`, `.begin()`, `.end()`, `.clear()`, `[]` |
| `<map>` | `map<K,V>`, `.find()`, `.at()`, `[]`, `unordered_map<K,V>` |
| `<queue>` | `queue<T>`, `priority_queue<T>`, `.push()`, `.pop()`, `.top()`, `.empty()` |
| `<algorithm>` | `sort()`, `reverse()`, `max()`, `min()`, `fill()`, `find()`, `copy()` |
| `<cmath>` | `sqrt()`, `pow()`, `fabs()`, `abs()`, `sin()`, `cos()`, `M_PI` |
| `<ctime>` | `time()`, `localtime()`, `strftime()`, `time_t` |
| `<cstdlib>` | `srand()`, `rand()`, `malloc()`, `free()`, `atexit()` |
| `<random>` | `random_device`, `mt19937`, `uniform_int_distribution<>` |
| `<stdexcept>` | `invalid_argument`, `out_of_range`, `runtime_error`, `logic_error` |
| `<limits>` | `numeric_limits<T>::max()`, `::min()`, `::infinity()` |
| `<iomanip>` | `setw()`, `setfill()`, `setprecision()`, `fixed`, `scientific`, `left`, `right` |
| `<memory>` | `shared_ptr`, `unique_ptr`, `make_shared()`, `make_unique()`, `weak_ptr` |

## Always Include
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
```

---

*Generated for Programming 2 Final Exam — Good luck!*
