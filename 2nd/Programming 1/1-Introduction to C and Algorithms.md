## 1. Conceptual Section (Teach Mode)

### 1.1 Computer Programming and Algorithms

> [!Definition] ⚙️ Computer Program
> A **computer program** is a sequence of instructions written using a **Computer Programming Language** to perform a specified task by the computer.

To solve a problem using a computer, one must define an **algorithm**.

> [!Definition] 🗺️ Algorithm
> An **algorithm** is a finite set of instructions that, if followed, accomplishes a particular task.
>
> **Key Characteristics:**
> 1.  **Input:** Zero or more quantities are externally supplied.
> 2.  **Output:** At least one quantity is produced.
> 3.  **Definiteness:** Each instruction is clear and unambiguous.
> 4.  **Finiteness:** The algorithm terminates after a finite number of steps.
> 5.  **Effectiveness:** Every instruction must be basic enough to be carried out strictly.

#### Algorithm Representation

Algorithms are typically represented in two ways:
1.  **Pseudo-code:** English-like representation of the logic.
2.  **Flowchart:** A graphical representation using standard symbols.

> [!Note] 📊 Standard Flowchart Symbols
> * **Oval (Rounded Rectangle):** Start / End (Terminal).
> * **Parallelogram:** Input / Output operations.
> * **Rectangle:** Process / Calculation / Assignment.
> * **Diamond:** Decision / Conditional check (Yes/No branching).
> * **Arrows:** Flow of control.



---

### 1.2 Structure of a C Program

A C program is constructed from functions and directives. The execution always begins at the `main()` function.

> [!Syntax] 🏗️ Basic Structure
> ```c
> // Preprocessor Directives
> #include <stdio.h> 
>
> // Global Declarations (Optional)
> int global_var;
>
> // Main Function
> int main(void) {
>     // Variable Declarations
>     int variable;
>     
>     // Executable Statements
>     printf("Hello, World!");
>     
>     return 0; // Termination
> }
> ```

* **Preprocessor Directives:** Lines beginning with `#` (e.g., `#include`). They are processed before compilation. `<stdio.h>` stands for **Standard Input Output** header file, required for functions like `printf` and `scanf`.
* **`main()` Function:** The entry point of every C program. `int` indicates it returns an integer to the OS; `void` indicates it takes no arguments.
* **Comments:** Ignored by the compiler, used for documentation.
    * Single line: `// comment`
    * Multi-line: `/* comment */`.

---

### 1.3 Identifiers and Keywords

> [!Definition] 🏷️ Identifier
> A name given to entities such as variables, functions, and arrays.

**Rules for Identifiers:** 
1.  Must consist of letters ($A-Z, a-z$), digits ($0-9$), or underscores ($\_$).
2.  **Must** start with a letter or an underscore.
3.  **Cannot** start with a digit.
4.  **Case-sensitive** (`sum` $\neq$ `Sum`).
5.  **Cannot** be a reserved **Keyword** (e.g., `int`, `return`, `if`, `while`).

---

### 1.4 Variables and Data Types

> [!Definition] 📦 Variable
> A named location in memory used to store a value that can be modified during program execution.

#### Variable Declaration and Initialization
Variables must be declared before use.
* **Syntax:** `type variable_list;`
* **Initialization:** `type variable_name = value;`

> [!Example]
> ```c
> int width, height;      // Declaration
> int area = 100;         // Initialization
> char grade = 'A';
> ```

#### Fundamental Data Types
C provides several basic types to store different kinds of data:

| Type | Description | Format Specifier | Example |
| :--- | :--- | :--- | :--- |
| **`int`** | Integer (whole numbers) | `%d` | `10`, `-5` |
| **`float`** | Floating-point (single precision) | `%f` | `3.14f` |
| **`double`** | Floating-point (double precision) | `%lf` | `3.14159` |
| **`char`** | Character (single byte) | `%c` | `'a'`, `'Z'` |
| **`_Bool`** | Boolean (0 or 1) | `%d` (as int) | `0`, `1` |
| **`void`** | Valueless (used for functions) | N/A | `void func()` |

**Qualifiers:** `short`, `long`, `signed`, `unsigned` can modify these types (e.g., `unsigned int`, `long double`).

---

### 1.5 Constants

> [!Definition] 🗿 Constant
> A value that **cannot** be changed during program execution.

**Defining Constants:**
1.  **Literals:** Fixed values used directly (e.g., `3.14`, `100`).
2.  **`const` Keyword:** Defines a read-only variable.
    ```c
    const double PI = 3.14159;
    ```
3.  **`#define` Preprocessor:** Creates a macro.
    ```c
    #define MAX_SIZE 100
    ```
    *Note: `#define` does not use a semicolon*.

---

### 1.6 Input and Output (I/O)

C uses standard library functions for I/O operations.

> [!Function] 📤 `printf()` (Output)
> Prints formatted output to the standard output (screen).
>
> **Syntax:** `printf("format string", argument_list);`
>
> **Escape Sequences:**
> * `\n`: Newline
> * `\t`: Tab
> * `\"`: Double quote.

> [!Function] 📥 `scanf()` (Input)
> Reads formatted input from the standard input (keyboard).
>
> **Syntax:** `scanf("format string", &variable_name);`
>
> **Important:** The `&` (address-of operator) is required for standard variables (int, float, char) to tell `scanf` *where* in memory to store the input.
