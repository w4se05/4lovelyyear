# Programming 1: C Fundamentals & Operators

## 1. Conceptual Section (Teach Mode)

### 1.1 C Tokens and Comments

> [!Definition] 🧱 Tokens
> A **token** is the smallest individual unit in a C program. The compiler breaks a program into tokens to understand it.

[cite_start]There are **6 types** of tokens in C [cite: 5-8]:
1.  **Keywords:** Reserved words with special meaning (e.g., `int`, `while`, `return`). Cannot be used as identifiers.
2.  **Identifiers:** Names given to variables, functions, etc. (e.g., `myVar`, `calculateSum`).
3.  **Constants:** Fixed values that do not change (e.g., `100`, `3.14`, `'A'`).
4.  **Strings:** Sequences of characters enclosed in double quotes (e.g., `"Hello"`).
5.  **Special Symbols:** Characters with specific meanings (e.g., `{}`, `[]`, `()`, `;`).
6.  **Operators:** Symbols that perform operations on operands (e.g., `+`, `-`, `*`).

#### Comments
[cite_start]Comments are ignored by the compiler and used for documentation [cite: 3-4].
* **Single-line:** Starts with `//`. Terminates at the end of the line.
* **Multi-line:** Starts with `/*` and ends with `*/`. Can span multiple lines.

---

### 1.2 Data Types

[cite_start]C provides various data types to define the nature of variables [cite: 17-20].

#### Primary (Fundamental) Data Types
| Type | Description | Size (Typical) | Format Specifier |
| :--- | :--- | :--- | :--- |
| **`int`** | Integer (whole numbers) | 2 or 4 bytes | `%d` or `%i` |
| **`float`** | Single-precision floating point | 4 bytes | `%f` |
| **`double`** | Double-precision floating point | 8 bytes | `%lf` |
| **`char`** | Character (stores ASCII value) | 1 byte | `%c` |
| **`void`** | Empty/No value | 0 bytes | N/A |

#### Derived & User-Defined Types
* **Derived:** Arrays, Pointers, Functions.
* **User-Defined:** Structures (`struct`), Unions (`union`), Enumerations (`enum`).

#### Type Modifiers
[cite_start]Modifiers alter the range or storage size of basic types[cite: 20]:
* `signed` / `unsigned`: Determines if negative values are allowed.
* `short` / `long`: Alters the storage capacity (e.g., `long double`).

---

### 1.3 Variables, Constants, and Literals

> [!Definition] 📦 Variable
> A container for storing data values. The syntax is: `type variable_name = value;`

* **Scope:** Local (inside a function) or Global (outside functions).
* [cite_start]**Initialization:** Assigning a value at the time of declaration [cite: 15-16].

> [!Definition] 🗿 Constant
> A variable whose value cannot be changed after definition.
> * **Defined using `const`:** `const int MAX = 100;`
> [cite_start]* **Defined using `#define`:** `#define PI 3.14` (Preprocessor macro)[cite: 14].

[cite_start]**Literals:** The actual values assigned to variables (e.g., `12` is an integer literal, `"C"` is a string literal)[cite: 13].

---

### 1.4 Input and Output (I/O)

#### Standard I/O Functions
1.  [cite_start]**`printf()`**: Outputs formatted data to the screen [cite: 23-24].
2.  **`scanf()`**: Reads formatted data from the keyboard.
    * **Note:** Requires the address-of operator `&` for variables (except strings).

#### Character I/O
[cite_start]Specialized functions for single characters [cite: 25-26]:
* **`getchar()`**: Reads a single character from standard input.
* **`putchar()`**: Writes a single character to standard output.

> [!Example] Character I/O
> ```c
> char c;
> c = getchar(); // Reads 'A'
> putchar(c);    // Prints 'A'
> ```

---

### 1.5 Operators

[cite_start]Operators specify the operation to be performed on operands (variables/values)[cite: 28].

#### 1. Arithmetic Operators
[cite_start]Used for mathematical calculations [cite: 30-31].
* `+` (Add), `-` (Subtract), `*` (Multiply), `/` (Divide).
* `%` (Modulus): Returns the **remainder** of division. *Only works with integers*.

#### 2. Increment and Decrement Operators
[cite_start]Unary operators that change value by 1[cite: 41].
* **Pre-increment (`++a`):** Increment first, then use the value.
* **Post-increment (`a++`):** Use the value first, then increment.

> [!Example] Pre vs. Post
> ```c
> int a = 5, b;
> b = ++a; // a becomes 6, then b becomes 6
> b = a++; // b becomes 6, then a becomes 7
> ```

#### 3. Relational Operators
Used to compare two values. [cite_start]Returns `1` (True) or `0` (False)[cite: 34].
* `==` (Equal to), `!=` (Not equal to).
* `>`, `<`, `>=`, `<=`.

#### 4. Logical Operators
[cite_start]Used to combine conditional statements [cite: 36-37].
* `&&` (Logical AND): True if **both** operands are non-zero.
* `||` (Logical OR): True if **at least one** operand is non-zero.
* `!` (Logical NOT): Reverses the logical state.

#### 5. Bitwise Operators
[cite_start]Operations at the bit level [cite: 38-40].
* `&` (Bitwise AND), `|` (Bitwise OR), `^` (XOR).
* `~` (Complement/NOT), `<<` (Left Shift), `>>` (Right Shift).

#### 6. Assignment Operators
[cite_start]Assigns values from right to left[cite: 32].
* Simple: `=`
* Compound: `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`.
    * `a += b` is equivalent to `a = a + b`.

#### 7. Special Operators
* [cite_start]**`sizeof()`**: Returns the size of a variable or type in bytes[cite: 45].
* **Ternary Operator (`?:`)**: A shorthand for `if-else`.
    * Syntax: `Condition ? Value_if_True : Value_if_False;`

---

### 1.6 Operator Precedence and Associativity

> [!Note] 📏 Order of Operations
> When multiple operators appear in an expression, **Precedence** determines which operator is executed first. [cite_start]**Associativity** determines the order when operators have the same precedence [cite: 46-47].

**General Hierarchy (High to Low):**
1.  Postfix (`()`, `[]`, `->`, `.`, `++`, `--`)
2.  Unary (`+`, `-`, `!`, `~`, `++`, `--`, `sizeof`, `&`, `*`)
3.  Arithmetic (`*`, `/`, `%` then `+`, `-`)
4.  Shift (`<<`, `>>`)
5.  Relational (`<`, `<=`, `>`, `>=` then `==`, `!=`)
6.  Bitwise (`&` then `^` then `|`)
7.  Logical (`&&` then `||`)
8.  Conditional (`?:`)
9.  Assignment (`=`, `+=`, etc.)
10. Comma (`,`)

---

## 2. 📘 Examples (Application Mode)

### Example 1: Explicit vs. Implicit Type Casting
**Concept:** Converting one data type to another.
* **Implicit:** Done automatically by the compiler (e.g., `int` to `float`).
* **Explicit:** Forced by the user using `(type)`.

> [!Code] Casting
> ```c
> #include <stdio.h>
> int main() {
>     int sum = 17, count = 5;
>     double mean;
>
>     // Implicit: integer division (17/5 = 3), then assigned to double (3.0)
>     mean = sum / count; 
>     printf("Implicit: %f\n", mean); // Output: 3.000000
>
>     // Explicit: sum cast to double (17.0), then divided (17.0/5 = 3.4)
>     mean = (double) sum / count;
>     printf("Explicit: %f\n", mean); // Output: 3.400000
>     return 0;
> }
> ```

### Example 2: Bitwise Operation Logic
**Concept:** Manipulating individual bits.
Let $A = 60$ (`0011 1100`) and $B = 13$ (`0000 1101`).

> [!Code] Bitwise Logic
> ```c
> int A = 60; // 0011 1100
> int B = 13; // 0000 1101
> int result;
>
> result = A & B; // 0000 1100 (12) - AND
> result = A | B; // 0011 1101 (61) - OR
> result = A ^ B; // 0011 0001 (49) - XOR
> result = ~A;    // 1100 0011 (-61) - NOT (2's complement)
> result = A << 2;// 1111 0000 (240) - Left Shift by 2
> ```

### Example 3: The Ternary Operator
**Concept:** Replacing simple `if-else` blocks for conciseness.

> [!Code] Max Value
> ```c
> #include <stdio.h>
> int main() {
>     int a = 10, b = 20, max;
>
>     // Logic: If a > b is true, return a, else return b
>     max = (a > b) ? a : b;
>
>     printf("Max value is %d", max); // Output: 20
>     return 0;
> }
> ```

---

## 3. Summary

* **Tokens:** The building blocks (Keywords, Identifiers, Literals, Operators, Separators).
* **Data Types:** Use `int` for counters, `float/double` for precision, `char` for text. Modifiers like `unsigned` double the positive range.
* **Operators:**
    * **Arithmetic:** `%` works only on integers.
    * **Logical:** `&&` and `||` use short-circuit evaluation.
    * **Assignment:** `a = b` puts the value of `b` into `a`.
    * **Equality:** `==` compares values; `=` assigns values. Confusing them is a common bug.
* **I/O:** `printf` and `scanf` use format specifiers (`%d`, `%f`, `%c`). `scanf` generally needs `&` before variable names.
* **Precedence:** Unary > Arithmetic > Relational > Logical > Assignment. Use parentheses `()` to force order.