## 1. Conceptual Section (Teach Mode)

### 1.1 Program Skeleton & Compilation
Every C program must have a `main()` function. The compiler translates human-readable source code into machine code.

> [!Definition] Structure of a C Program
> ```c
> #include <stdio.h> // Preprocessor directive for Input/Output
> 
> // Main function - entry point
> int main(void) {
>     // Variable declarations
>     int x; 
>     
>     // Executable statements
>     printf("Hello World\n");
>     
>     return 0; // Exit status (0 = success)
> }
> ```

**Key Phases of Execution:**
1.  **Preprocessing**: Handles `#include` and `#define`.
2.  **Compiling**: Translates C to object code.
3.  **Linking**: Combines object code with libraries (e.g., Standard Library) to create the executable.

---

### 1.2 Data Types & Variables
C is statically typed. Variables must be declared before use.

> [!Note] Primitive Data Types
> | Type | Size (Typical) | Format Specifier | Range (Approx) |
> | :--- | :--- | :--- | :--- |
> | `char` | 1 byte | `%c` | -128 to 127 (ASCII) |
> | `int` | 4 bytes | `%d` or `%i` | -2.1B to +2.1B |
> | `float` | 4 bytes | `%f` | 6-7 decimal digits |
> | `double` | 8 bytes | `%lf` | 15-16 decimal digits |

**Variable Naming Rules:**
* Case-sensitive (`sum` $\neq$ `Sum`).
* Must start with a letter or underscore `_`.
* Cannot be a keyword (e.g., `while`, `int`, `return`).

---

### 1.3 Input/Output Operations
The `stdio.h` library provides `printf` (output) and `scanf` (input).

**Input (`scanf`):**
* **Syntax**: `scanf("format_specifier", &variable);`
* **Critical Rule**: You **must** use the address-of operator `&` for primitive types (`int`, `float`, `char`).
* **Example**: `scanf("%d", &age);`

**Output (`printf`):**
* **Syntax**: `printf("Text %format_specifier", variable);`
* **Formatting**:
    * `%.2f`: Prints a float with 2 decimal places.
    * `%5d`: Prints an int right-aligned in a 5-character width.

> [!Warning] Common Exam Trap
> Forgetting the `&` in `scanf` is a fatal logic error that causes segmentation faults.
> * Wrong: `scanf("%d", age);`
> * Correct: `scanf("%d", &age);`

---

### 1.4 Operators

**Arithmetic**: `+`, `-`, `*`, `/`, `%` (Modulus/Remainder).
> [!Tip] Integer Division
> In C, `int / int` results in an `int`.
> * `5 / 2` $\rightarrow$ `2`
> * `5.0 / 2` $\rightarrow$ `2.5` (Implicit casting)

**Relational** (Returns 1 for True, 0 for False):
* `==` (Equal to), `!=` (Not equal)
* `>`, `<`, `>=`, `<=`

**Logical**:
* `&&` (AND): True if **both** are true.
* `||` (OR): True if **at least one** is true.
* `!` (NOT): Inverses the boolean value.

---

### 1.5 Control Flow: Branching

**If-Else Statement:**
```c
if (condition) {
    // Code if true
} else if (another_condition) {
    // Code if 1st is false and 2nd is true
} else {
    // Code if all above are false
}
````

**Switch Statement:
Used for selecting among many discrete values (must be int or char).

```
switch (variable) {
    case 1:
        // Code for case 1
        break; // Crucial! Prevents falling into case 2
    case 2:
        // Code for case 2
        break;
    default:
        // Code if no match found
}
```

---

### 1.6 Control Flow: Looping

> [!Theorem] The 3 Loop Types
> 
> 1. **For Loop**: Use when iterations are known.
>     
>     - `for (init; condition; update) { ... }`
>         
> 2. **While Loop**: Use when iterations are unknown (pre-check).
>     
>     - `while (condition) { ... }`
>         
> 3. **Do-While Loop**: Use when code must run **at least once** (post-check).
>     
>     - `do { ... } while (condition);`
>         

**Loop Control:**

- `break`: Exits the loop immediately.
    
- `continue`: Skips the rest of the current iteration and jumps to the update/condition step.
    

---

## 2. Application Section (Exam Mode)

### 📘 Examples & Applications

> [!Example] Ex 1: Input/Output & Logic (The "Prime Check")
> 
> Using: Loops, Modulus Operator, Flags
> 
> Problem: Write a program to check if an input integer $n$ is prime.
> 
> **Solution**:
> 
> C
> 
> ```
> #include <stdio.h>
> ```
````
int main() {
int n, i, flag = 0; // flag=0 means prime
printf("Enter a positive integer: ");
scanf("%d", &n);
````

> ```
> // 0 and 1 are not prime numbers
> if (n == 0 || n == 1)
>     flag = 1;
> ```

> ```
> // Loop from 2 to n/2
> for (i = 2; i <= n / 2; ++i) {
>     // If n is divisible by i, it is not prime
>     if (n % i == 0) {
>         flag = 1;
>         break; // Optimization: stop finding factors
>     }
> }
> ```

> ```
> if (flag == 0)
>     printf("%d is a prime number.", n);
> else
>     printf("%d is not a prime number.", n);
> ```

> ```
> return 0;
> ```
> 
> }

> [!Example] Ex 2: Summation Series
> 
> Using: for loop, Accumulator
> 
> Problem: Calculate the sum of the series $S = 1 + 2 + ... + N$.
> 
> **Solution**:
> 
> C
> 
> ```
> #include <stdio.h>
> 
> int main() {
> int n, i, sum = 0;
> printf("Enter a positive integer: ");
> scanf("%d", &n);
> // Loop to accumulate sum
> for (i = 1; i <= n; ++i) {
>     sum += i; // Equivalent to sum = sum + i;
> }
> printf("Sum = %d", sum);
> return 0;
> ```
> 
> }

> [!Example] Ex 3: Pattern Printing (Nested Loops)
> 
> Using: Nested for loops
> 
> Problem: Print a right-angled triangle of stars for height $N$.
> 
> **Solution**:
> 
> C
> 
> ```
> /* Output for N=3:
> *
> **
> ***
> */
> #include <stdio.h>
> int main() {
> 
> int rows, i, j;
> 
> printf("Enter number of rows: ");
> 
> scanf("%d", &rows);


> ```
> for (i = 1; i <= rows; ++i) {      // Outer loop: Rows
>     for (j = 1; j <= i; ++j) {     // Inner loop: Columns
>         printf("*");
>     }
>     printf("\n"); // Newline after each row
> }
> return 0;
> ```
> 
> }

---

## 3. Summary for Revision

- **Header**: Always include `#include <stdio.h>` for standard I/O.
    
- **Variable Declaration**: Declare variables at the top of the block (C89 standard, preferred in exams).
    
- **`scanf` Trap**: Never forget the `&` for `int` and `float`.
    
- **`if` vs `=`**: `if (x = 5)` assigns 5 to x and evaluates to TRUE. You always want `if (x == 5)`.
    
- **Semicolon Trap**: Do NOT put a semicolon after `if(...)` or `for(...)`.
    
    - Wrong: `if (x > 5);`
        
    - Right: `do { ... } while(condition);` (This is the only loop with a semicolon at the end).
        
- **Modulus**: `%` only works with integers. `5 % 2 = 1`.
