# Lec11: Templates and Friends — Study Guide

---

## 1. CONCEPT CARD: Templates

**What it is:** A template is a pattern for generating code. You write ONE function or class definition using placeholder types, and the compiler automatically creates type-specific versions when you use them.

**What problem it solves:** Without templates, if you need a `swap` function for `int`, `double`, `char*`, `Student`, etc., you'd write identical code for each type — just changing the type names. When you find a bug in the logic, you fix it in 10 places. With templates, you write the logic ONCE and the compiler stamps out versions on demand. Same for container classes — one `Array<int>` and one `Array<Student>` without duplicating all the bounds-checking code.

**How it works:**
1. Declare a template with `template <class T>` (or `typename T`).
2. Use `T` as a placeholder type throughout the function or class definition.
3. When the compiler sees `swap(a, b)` where `a` and `b` are `int`s, it automatically generates a version with `T` replaced by `int`.
4. You can have multiple template parameters: `template <class T1, class T2>`.
5. A class template's methods must be defined with `template <class T>` prefix and `ClassName<T>::` scope.
6. If a template function uses an operator (like `==`), every type you use with it must support that operator. Use operator overloading to make your classes compatible.
7. If a template doesn't work for a specific type (e.g., `char*` needs `strcmp`, not `==`), you write an **explicit (non-template) override** with the exact signature. The compiler prefers the non-template version.

**Concrete example:** A leaderboard system for a game. You write `template <class T> int findRank(T score, const T leaderboard[], int size)` to find a player's position. Works with `int` scores, `float` scores, even a custom `PlayerScore` object — as long as it has `operator==`. One search function, any score type, zero code duplication.

**What it is NOT:** A template is NOT a class. `Array` is not a class — `Array<int>` is. You cannot inherit from a template directly (`class Foo : public Array` is wrong). You CAN inherit from a specific template instantiation (`class Foo : public Array<int>` is fine).

---

## 2. MUST-MEMORIZE SYNTAX TEMPLATE

```cpp
// FUNCTION TEMPLATE — one placeholder type:
template <class T>                // T is a placeholder for any type
void swapValues(T& a, T& b) {    // Both parameters must be the same T
    T temp = a;
    a = b;
    b = temp;
}

// FUNCTION TEMPLATE — multiple parameters:
template <class T1, class T2>
T1 findMax(T1 a, T2 b) {         // Return type is T1
    return (a > b) ? a : (T1)b;
}

// CLASS TEMPLATE:
template <class T>
class Container {
    T* data;
    unsigned size;
public:
    Container(unsigned sz);       // Constructor
    ~Container();
    T& operator[](unsigned i);    // Access element
};

// Out-of-line member definition:
template <class T>
Container<T>::Container(unsigned sz) {  // Note: Container<T>, not Container
    data = new T[sz];
    size = sz;
}

template <class T>
T& Container<T>::operator[](unsigned i) {
    return data[i];               // Bounds-checking omitted for brevity
}

// Explicit override — non-template preferred over template:
int findMax(const char* a, const char* b) {   // Specific for char*
    return (strcmp(a, b) > 0) ? 1 : 0;
}

// Usage:
Container<int> ints(10);          // T replaced with int
Container<Student> roster(50);    // T replaced with Student
```

---

## 3. EXAM TRAPS

- **`template <class T>` on EVERY out-of-line member function.** For class templates, each method defined outside the class body needs its own `template <class T>` prefix and `ClassName<T>::` scope. Forgetting this is a common compile error.
- **Template parameter scope is LOCAL to that one function/class.** `T` in one template has nothing to do with `T` in another. They're completely independent.
- **Static members in class templates are per-instantiation, not per-template.** `Array<int>::count` and `Array<double>::count` are TWO DIFFERENT static variables. The template itself doesn't have static members; each generated class does.
- **A template function that uses `==` on T will fail to compile if T has no `==`.** You must ensure all types used with the template support the operators it uses.
- **Explicit (non-template) function overrides take priority over template versions.** If both `void swap(int&, int&)` and `template<class T> void swap(T&, T&)` exist, `swap(i, j)` with two ints calls the non-template version.
- **Friend declarations inside templates:** `friend class TList<T>;` inside `TNode<T>` — this grants TList access to TNode's private members. Friendship is NOT symmetric (if A is friend of B, B is NOT automatically friend of A), NOT transitive (friend of friend doesn't count), and NOT inheritable.
- **Friend functions must be declared INSIDE the class granting friendship.** The `friend` keyword goes in the class that owns the private members being shared.
- **`template <class T>` vs `template <typename T>` — they mean the same thing.** Use either, be consistent.

---

## 4. HAND-CODING DRILLS

### Drill 1: Function Template — Minimum of Two

Write a template function `minValue` that takes two parameters of the same type and returns the smaller one. Use it to find the minimum of `(10, 5)`, `(3.14, 2.71)`, and `('Z', 'A')`.

> [!success]- Show Answer
> ```cpp
> template <class T>
> T minValue(T a, T b) {
>     return (a < b) ? a : b;
> }
> 
> int main() {
>     int i = minValue(10, 5);        // T = int, returns 5
>     double d = minValue(3.14, 2.71); // T = double, returns 2.71
>     char c = minValue('Z', 'A');     // T = char, returns 'A'
>     // Note: char comparison works because ASCII 'A'(65) < 'Z'(90)
> }
> ```

### Drill 2: Class Template — Simple Stack

Write a class template `Stack` that holds up to `CAPACITY` elements of type `T`. It needs:
- `push(T item)` — adds to the top (fail silently if full)
- `pop()` — removes and returns the top item (assume never called on empty)
- `bool isEmpty()` — returns true if stack is empty

Use a fixed-size internal array. Define ALL methods inside the class body.

> [!success]- Show Answer
> ```cpp
> template <class T, int CAPACITY>
> class Stack {
>     T data[CAPACITY];
>     int topIndex;
> public:
>     Stack() : topIndex(-1) {}
>
>     void push(T item) {
>         if (topIndex < CAPACITY - 1) {
>             topIndex++;
>             data[topIndex] = item;
>         }
>     }
>
>     T pop() {
>         T item = data[topIndex];
>         topIndex--;
>         return item;
>     }
>
>     bool isEmpty() const {
>         return topIndex == -1;
>     }
> };
> // Usage: Stack<int, 10> intStack; Stack<Student, 30> studentStack;
> ```

### Drill 3: Template + Operator Overloading + Friend

A `Pair` class template holds two values of (possibly) different types. Write the full template class with:
- `first` and `second` as public data members (simplified)
- A constructor `Pair(T1 a, T2 b)`
- A friend `operator<<` that prints `(first, second)`
- A `bool operator==` that returns true if both first AND second match

Then write the explicit non-template override for `operator==` when comparing two `Pair<const char*, const char*>` using `strcmp`.

> [!success]- Show Answer
> ```cpp
> template <class T1, class T2>
> class Pair {
> public:
>     T1 first;
>     T2 second;
>
>     Pair(T1 a, T2 b) : first(a), second(b) {}
>
>     bool operator==(const Pair<T1, T2>& other) const {
>         return (first == other.first) && (second == other.second);
>     }
>
>     template <class X1, class X2>
>     friend ostream& operator<<(ostream& os, const Pair<X1, X2>& p) {
>         os << "(" << p.first << ", " << p.second << ")";
>         return os;
>     }
> };
>
> // Explicit non-template override for const char* pairs:
> bool operator==(const Pair<const char*, const char*>& a,
>                  const Pair<const char*, const char*>& b) {
>     return (strcmp(a.first, b.first) == 0)
>         && (strcmp(a.second, b.second) == 0);
> }
> ```
