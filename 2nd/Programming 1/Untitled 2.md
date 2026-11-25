# Programming 1: Working with C Functions

## 1. Conceptual Section (Teach Mode)

### 1.1 Introduction to Functions

> [!Definition] 🧩 Function
> A **function** is a self-contained block of code designed to perform a specific task. It runs only when called.
>
> **Key Benefits:**
> 1.  **Reusability:** Define code once, use it many times.
> [cite_start]2.  **Modularity:** Breaks large programs into smaller, manageable chunks[cite: 1040, 1152].
> [cite_start]3.  **Maintainability:** Easier to debug and understand[cite: 1150].

[cite_start]Functions in C are categorized into two types [cite: 1041-1042]:
1.  **Standard Library Functions (Built-in):** Pre-defined in header files (e.g., `printf()`, `sqrt()`).
2.  **User-Defined Functions:** Created by the programmer to satisfy specific needs.

---

### 1.2 Standard Library Functions

C provides a rich collection of built-in functions optimized for performance and portability. To use them, you must include the appropriate **Header File** (files ending in `.h`).

> [!Note] 📚 Common Header Files
> [cite_start]* `<stdio.h>`: Standard Input/Output (e.g., `printf`, `scanf`)[cite: 1100].
> [cite_start]* `<math.h>`: Mathematical operations (e.g., `sqrt`, `pow`)[cite: 1095].
> [cite_start]* `<stdlib.h>`: Utility functions (e.g., `rand`, `srand`, `exit`)[cite: 1100].
> [cite_start]* `<time.h>`: Date and time functions[cite: 1100].

#### Math Functions (`<math.h>`)
Most math functions accept `double` as arguments and return `double`.

| Function | Description | Example | Result |
| :--- | :--- | :--- | :--- |
| `sqrt(x)` | Square root of $x$ | `sqrt(900.0)` | $30.0$ |
| `pow(x, y)` | Power function $x^y$ | `pow(2, 7)` | $128.0$ |
| `ceil(x)` | Rounds $x$ **up** to nearest integer | `ceil(9.2)` | $10.0$ |
| `floor(x)` | Rounds $x$ **down** to nearest integer | `floor(9.2)` | $9.0$ |
| `fabs(x)` | Absolute value $\|x\|$ | `fabs(-5.0)` | $5.0$ |
| `fmod(x, y)` | Floating point remainder of $x/y$ | `fmod(13.657, 2.333)`| $1.992$ |

---

### 1.3 User-Defined Functions

Creating a function involves three distinct parts: the **Prototype**, the **Definition**, and the **Call**.

#### 1. Function Prototype (Declaration)
Tells the compiler about the function's name, return type, and parameters *before* it is defined. [cite_start]This allows the compiler to check for type errors [cite: 1163-1165].

> [!Syntax]
> `returnType functionName(type1 arg1, type2 arg2);`
> [cite_start]* **Important:** Must end with a semicolon `;`[cite: 1182].

#### 2. Function Definition (Implementation)
Contains the actual code to be executed.

> [!Syntax]
> ```c
> returnType functionName(type1 arg1, type2 arg2) {
>     // body of the function
>     return value; // (if returnType is not void)
> }
> ```
> * **Local Variables:** Variables defined here are local to this function.
> [cite_start]* **Return Statement:** Terminates execution and passes a value back to the caller [cite: 1230-1232].

#### 3. Function Call (Usage)
Transfers control to the function.
* **Syntax:** `functionName(value1, value2);`

> [!Warning] ⚠️ Common Errors
> [cite_start]* **Void Return:** Returning a value from a `void` function is a syntax error[cite: 1343].
> [cite_start]* **Missing Return:** Forgetting to return a value from a non-void function leads to undefined behavior[cite: 1340].
> [cite_start]* **Argument Mismatch:** Defining parameters like `double x, y` instead of `double x, double y` is a syntax error[cite: 1357].

---

### 1.4 Recursion

> [!Definition] 🔄 Recursion
> Recursion is the process where a function calls itself.
>
> A recursive function **must** have two parts:
> [cite_start]1.  **Base Case:** A condition that stops the recursion (e.g., `if (n == 0) return 1;`)[cite: 1876].
> [cite_start]2.  **Recursive Step:** The function calls itself with a modified argument (moving towards the base case)[cite: 1888].

* [cite_start]**Pros:** Elegant code for problems like tree traversal, Factorials, Fibonacci[cite: 1791].
* [cite_start]**Cons:** Slower than loops (iteration) and consumes more memory (stack overhead)[cite: 1791].
* [cite_start]**Risk:** Missing the base case causes **Infinite Recursion** (Stack Overflow)[cite: 1935].

---

### 1.5 C Storage Classes

[cite_start]Storage classes determine the **scope** (visibility) and **lifetime** of a variable[cite: 2040].

| Storage Class | Keyword | Scope | Lifetime | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Automatic** | `auto` (default) | Local (Block) | Function execution | Variables declared inside a block. [cite_start]Destroyed when function exits[cite: 2053]. |
| **External** | `extern` | Global | Entire program | Variables declared outside all functions. [cite_start]Accessible everywhere[cite: 2078]. |
| **Static** | `static` | Local (Block) | Entire program | **Persists** between function calls. [cite_start]Initializes only once [cite: 2112-2113]. |
| **Register** | `register` | Local | Function execution | [cite_start]Hints to store variable in CPU register for speed (rarely used now)[cite: 2105]. |

---

### 1.6 Random Number Generation

To generate random numbers, use `<stdlib.h>` and `<time.h>`.

1.  **`rand()`**: Returns a pseudo-random integer between 0 and `RAND_MAX`.
2.  **`srand(seed)`**: Seeds the random number generator.
    * [cite_start]Using `srand(time(NULL))` seeds it with the current time, ensuring different numbers each run [cite: 2143-2144].
    * **Formula for specific range:** `number = min + (rand() % (max - min + 1));`

---

## 2. 📘 Examples & Applications (Exam Mode)

### Example 1: Function Anatomy & Prototype
**Problem:** Write a function `get_max` that takes two integers and returns the larger one. Ensure a prototype is used.

> [!Code] Solution
> ```c
> #include <stdio.h>
>
> // 1. Prototype (Declaration) - Semicolon required!
> int get_max(int a, int b);
>
> int main() {
>     int x = 10, y = 20;
>     // 3. Function Call
>     int m = get_max(x, y);
>     printf("Max is: %d\n", m);
>     return 0;
> }
>
> // 2. Definition (Implementation)
> int get_max(int a, int b) {
>     if (a > b)
>         return a;
>     else
>         return b;
> }
> ```

### Example 2: Static Variables (Exam Trick)
**Concept:** Static variables retain their value between calls.
**Question:** What is the output of the following code?

> [!Code] Static Logic
> ```c
> void counter() {
>     static int count = 0; // Initialized only ONCE
>     count++;
>     printf("%d ", count);
> }
>
> int main() {
>     counter();
>     counter();
>     counter();
>     return 0;
> }
> ```
> **Analysis:**
> * Call 1: `count` starts at 0, becomes 1. Prints `1`.
> * Call 2: `count` is REMEMBERED as 1. Becomes 2. Prints `2`.
> * Call 3: `count` is REMEMBERED as 2. Becomes 3. Prints `3`.
>
> **Output:** `1 2 3` (If `static` was removed, output would be `1 1 1`).

### Example 3: Recursion Logic (Factorial)
**Problem:** Implement $n!$ using recursion.
**Formula:** $n! = n \times (n-1)!$ with Base Case $0! = 1$.

> [!Code] Recursive Solution
> ```c
> long factorial(int n) {
>     // Base Case
>     if (n <= 1) {
>         return 1;
>     }
>     // Recursive Step
>     else {
>         return n * factorial(n - 1);
>     }
> }
> ```

### Example 4: Random Numbers in Range
**Problem:** Simulate rolling a 6-sided die (values 1 to 6).

> [!Code] Solution
> ```c
> #include <stdio.h>
> #include <stdlib.h>
> #include <time.h>
>
> int main() {
>     // Seed using current time so numbers change every run
>     srand(time(NULL));
>
>     // Formula: 1 + (rand() % 6) generates 0-5, then adds 1 -> 1-6
>     int roll = 1 + (rand() % 6);
>     
>     printf("You rolled a %d\n", roll);
>     return 0;
> }
> ```

---

## 3. Summary

* **Prototypes:** Always declare functions before `main()` if the definition comes after. Don't forget the `;`.
* **Return Values:** Use `void` if nothing is returned. If a type is specified (e.g., `int`), you *must* return a value.
* **Recursion:** Needs a **Base Case** to stop and a **Recursive Step** to proceed. Great for logical definitions (Fibonacci, Factorial) but heavy on memory.
* **Storage Classes:**
    * `auto`: Local, temporary.
    * `global`: Accessible everywhere.
    * `static`: Local scope but **Global lifetime** (remembers value).
* **Libraries:** Use `<math.h>` for complex math and `<stdlib.h>` for random numbers (`rand`).