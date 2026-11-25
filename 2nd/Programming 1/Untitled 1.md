# Programming 1: Flow Control, Decisions, and Looping

## 1. Conceptual Section (Teach Mode)

### 1.1 Conditional Logic

> [!Definition] ⚖️ Logical Conditions
> C uses standard mathematical logical operators to test conditions. These return a boolean value (True/Non-zero or False/Zero).

[cite_start]**Relational Operators:** [cite: 3-4]
* **Less than:** $a < b$
* **Less than or equal to:** $a <= b$
* **Greater than:** $a > b$
* **Greater than or equal to:** $a >= b$
* **Equal to:** $a == b$ (Note the double equals)
* **Not Equal to:** $a != b$

---

### 1.2 Selection Statements (Decision Making)

Selection statements allow the program to choose different paths of execution based on the outcome of a logical condition.

#### The `if` Statement
Executes a block of code *only if* the specified condition is true.

> [!Syntax]
> ```c
> if (condition) {
>     // block of code to be executed if the condition is true
> }
> ```

#### The `if...else` Statement
[cite_start]Specifies a block of code to execute if the condition is true, and another block if it is false [cite: 4-6].

> [!Syntax]
> ```c
> if (condition) {
>     // executes if condition is true
> } else {
>     // executes if condition is false
> }
> ```

#### The `else if` Ladder
Used to specify a new condition to test if the first condition is false.

> [!Syntax]
> ```c
> if (condition1) {
>     // executes if condition1 is true
> } else if (condition2) {
>     // executes if condition1 is false and condition2 is true
> } else {
>     // executes if both condition1 and condition2 are false
> }
> ```

#### The `switch` Statement
Selects one of many code blocks to be executed. [cite_start]It is often a cleaner alternative to long `else if` ladders when comparing a single variable against multiple constant values [cite: 13-14].

> [!Syntax]
> ```c
> switch (expression) {
>     case constant1:
>         // code to be executed if expression == constant1;
>         break; 
>     case constant2:
>         // code to be executed if expression == constant2;
>         break;
>     default:
>         // code to be executed if expression doesn't match any case
> }
> ```

> [!Warning] 🛑 The `break` Keyword
> When C reaches a `break` keyword, it breaks out of the switch block. [cite_start]If you omit the `break`, execution will **"fall through"** to the next case automatically [cite: 15-16].

---

### 1.3 Repetition Statements (Loops)

Loops are used to execute a block of code repeatedly as long as a specified condition is reached.

#### The `for` Loop
[cite_start]Used when you know exactly how many times you want to loop [cite: 18-20].

> [!Syntax]
> ```c
> for (initialization; condition; increment/decrement) {
>     // code block to be executed
> }
> ```
> * **Statement 1:** Executed one time before the block starts (Initialization).
> * **Statement 2:** Defines the condition for executing the block (Termination Condition).
> * **Statement 3:** Executed every time *after* the code block has been executed (Increment).

#### The `while` Loop
Loops through a block of code as long as a specified condition is true. [cite_start]This is an **Entry-Controlled Loop** (condition checked *before* execution) [cite: 25-26].

> [!Syntax]
> ```c
> while (condition) {
>     // code block to be executed
> }
> ```

#### The `do...while` Loop
This is an **Exit-Controlled Loop**. [cite_start]It will execute the code block **once**, before checking if the condition is true, then it will repeat the loop as long as the condition is true [cite: 31-32].

> [!Syntax]
> ```c
> do {
>     // code block to be executed
> } while (condition);
> ```

---

### 1.4 Jump Statements

Statements used to alter the normal flow of control.

> [!Definition] 🚪 `break`
> Jumps **out** of a loop or switch statement completely. [cite_start]Execution continues at the statement immediately following the loop [cite: 35-36].

> [!Definition] ⏭️ `continue`
> Breaks **one iteration** (in the loop). [cite_start]It skips the remaining code in the current iteration and jumps to the next iteration (evaluating the condition again) [cite: 39-40].

> [!Definition] 🏷️ `goto`
> Transfers control to a labeled statement within the same function.
> [cite_start]* *Note:* Use of `goto` is generally discouraged as it makes code hard to trace ("spaghetti code") [cite: 42-43].

---

## 2. 📘 Examples (Application Mode)

### Example 1: `switch` vs. `else if`
**Scenario:** Determine the name of the day based on an integer (1 = Monday, 7 = Sunday).

> [!Code] Using Switch
> ```c
> int day = 4;
> switch (day) {
>   case 1: printf("Monday"); break;
>   case 2: printf("Tuesday"); break;
>   case 3: printf("Wednesday"); break;
>   case 4: printf("Thursday"); break; // Matches, prints Thursday, then breaks
>   case 5: printf("Friday"); break;
>   case 6: printf("Saturday"); break;
>   case 7: printf("Sunday"); break;
>   default: printf("Invalid day"); // Handles 8, 0, -1, etc.
> }
> ```

### Example 2: The `do...while` Guarantee
**Scenario:** Ask the user for a number. If the number is negative, ask again. This requires the code to run at least once.

> [!Code] Input Validation
> ```c
> int num;
> do {
>     printf("Enter a positive number: ");
>     scanf("%d", &num);
> } while (num < 0); 
> // Loop continues IF num is negative.
> // Stops once user enters 0 or positive.
> ```

### Example 3: `break` and `continue` Mechanics
**Scenario:** Print numbers from 0 to 9, but skip 4, and stop completely at 8.

> [!Code] Flow Control
> ```c
> int i;
> for (i = 0; i < 10; i++) {
>     if (i == 4) {
>         continue; // Skips printf for 4, jumps to i++ (becomes 5)
>     }
>     if (i == 8) {
>         break;    // Exits the loop entirely. 8 and 9 are never printed.
>     }
>     printf("%d ", i);
> }
> // Output: 0 1 2 3 5 6 7
> ```

### Example 4: Nested Loops
**Scenario:** Print a multiplication table matrix (Outer loop `i`, Inner loop `j`).

> [!Code] Matrix Logic
> ```c
> int i, j;
> for (i = 1; i <= 2; ++i) {       // Outer Loop
>    printf("Outer: %d\n", i);
>    for (j = 1; j <= 3; ++j) {   // Inner Loop
>       printf(" Inner: %d\n", j);
>    }
> }
> /* Output:
> Outer: 1
>  Inner: 1
>  Inner: 2
>  Inner: 3
> Outer: 2
>  Inner: 1... and so on
> */
> ```

---

## 3. Summary

* **Logical Conditions:** Use `==` for comparison, not `=` (assignment).
* **Decisions:**
    * Use `if` for simple checks.
    * Use `switch` for checking one variable against many constants (cleaner).
    * Remember `break` in `switch` cases to prevent fall-through.
* **Loops:**
    * **`for`**: Best when the number of iterations is known (e.g., arrays).
    * **`while`**: Best when the number of iterations is unknown (e.g., reading file until EOF).
    * **`do...while`**: Guarantees the code runs at least once (e.g., input validation).
* **Flow Control:**
    * `break` kills the loop.
    * `continue` skips the rest of the current iteration.