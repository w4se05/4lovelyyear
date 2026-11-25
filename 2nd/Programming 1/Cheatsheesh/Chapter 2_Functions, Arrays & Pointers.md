## 1. Conceptual Section (Teach Mode)

### 1.1 Functions: The Building Blocks
Functions allow code reusability. They are defined by a return type, a name, and parameters.

> [!Definition] Function Syntax
> ```c
> return_type function_name(parameter_list) {
>     // Body
>     return value;
> }
> ```
> * **Prototype**: Declaration before `main` (e.g., `int add(int a, int b);`).
> * **Definition**: The actual code block (usually after `main`).
> * **Call**: Invoking the function (e.g., `int sum = add(5, 10);`).

**Pass by Value vs. Pass by Reference:**
* **Pass by Value** (Default): A *copy* of the variable is passed. Changes inside the function do **not** affect the original variable.
* **Pass by Reference** (Simulated with Pointers): The *address* is passed. Changes inside the function **do** affect the original variable.

---

### 1.2 Arrays: Storing Lists
An array is a fixed-size collection of elements of the same type stored in contiguous memory.

> [!Note] Array Declaration
> * **1D Array**: `int arr[5];` (Indices 0 to 4).
> * **Initialization**: `int arr[5] = {10, 20, 30, 40, 50};`
> * **2D Array (Matrices)**: `int matrix[rows][cols];`

**Visualizing 2D Arrays:**
`int mat[2][3]` can be seen as a table:
$$
\begin{bmatrix}
(0,0) & (0,1) & (0,2) \\
(1,0) & (1,1) & (1,2)
\end{bmatrix}
$$
In memory, this is stored linearly: Row 0 followed immediately by Row 1.

---

### 1.3 Pointers: The Memory Address
A pointer is a variable that stores the memory address of another variable.

> [!Definition] Pointer Operators
> * **`&` (Address-of)**: Returns the memory address of a variable. `&x` $\rightarrow$ Address of x.
> * **`*` (Dereference)**: Accesses the value stored at that address. `*ptr` $\rightarrow$ Value of x.



**Pointer Arithmetic & Arrays:**
Arrays and pointers are closely related.
* `arr` (the array name) acts as a pointer to the first element `&arr[0]`.
* `arr[i]` is equivalent to `*(arr + i)`.

---

### 1.4 Sorting Algorithms (The Bubble Sort)
Dr. Bao's notes emphasize **Bubble Sort**. You must memorize this logic for the written exam.

> [!Theorem] Bubble Sort Logic
> 1.  Compare adjacent elements ($a_i$ and $a_{i+1}$).
> 2.  Swap them if they are in the wrong order ($a_i > a_{i+1}$).
> 3.  Repeat this process $N-1$ times.
>
> **Complexity**: $O(N^2)$ (Slow, but simple to write).

---

## 2. Application Section (Exam Mode)

### 📘 Examples & Applications

> [!Example] Ex 1: The "Swap" Function (Pass by Reference)
> **Using**: Pointers, Dereferencing
> **Problem**: Write a function to swap the values of two integers.
>
> **Solution**:
> ```c
> void swap(int *a, int *b) {
>     int temp = *a;  // 1. Store value at address 'a' in temp
>     *a = *b;        // 2. Copy value at 'b' to address 'a'
>     *b = temp;      // 3. Copy temp to address 'b'
> }
> 
> // Call in main:
> // int x = 5, y = 10;
> // swap(&x, &y);
> ```

> [!Example] Ex 2: Array Traversal with Pointers
> **Using**: Pointer Arithmetic
> **Problem**: Sum all elements in an array using only pointers (no `arr[i]`).
>
> **Solution**:
> ```c
> int sumArray(int *arr, int size) {
>     int sum = 0;
>     int i;
>     for (i = 0; i < size; i++) {
>         // *(arr + i) gets the value at index i
>         sum += *(arr + i); 
>     }
>     return sum;
> }
> ```

> [!Example] Ex 3: Sorting an Array (Standard Bubble Sort)
> **Using**: Nested Loops, Array Indexing, Swap Logic
> **Problem**: Sort an array of $N$ integers in ascending order.
>
> **Solution**:
> ```c
> void bubbleSort(int arr[], int n) {
>     int i, j, temp;
>     // Outer loop: Number of passes
>     for (i = 0; i < n - 1; i++) {
>         // Inner loop: Comparison per pass
>         for (j = 0; j < n - i - 1; j++) {
>             // Swap if current > next
>             if (arr[j] > arr[j + 1]) {
>                 temp = arr[j];
>                 arr[j] = arr[j + 1];
>                 arr[j + 1] = temp;
>             }
>         }
>     }
> }
> ```

---

## 3. Summary for Revision

* **Prototype Mismatch**: If you define `void func(int x)` below `main`, you MUST write `void func(int x);` above `main`.
* **Pointer Declaration**: `int* ptr` declares a pointer. `*ptr` accesses the value. Don't confuse them!
* **Array Bounds**: `int arr[5]` has indices 0, 1, 2, 3, 4. Accessing `arr[5]` is Garbage Value or Crash.
* **Math Library**: If using `sqrt()` or `pow()`, include `#include <math.h>`.
* **Static Arrays**: You cannot return a locally created array from a function (it is destroyed when the function ends). Pass the array *into* the function to modify it.

---