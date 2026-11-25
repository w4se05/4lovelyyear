

# Programming 1: Working with Arrays

## 1. Conceptual Section (Teach Mode)

### 1.1 Introduction to Arrays

> [!Definition] 📚 Array
> [cite_start]An **array** is a fixed-size collection of elements of the **same data type** stored in contiguous memory locations[cite: 2256, 2258].

**Key Characteristics:**
1.  [cite_start]**Homogeneous:** All elements must be of the same type (e.g., `int`, `float`)[cite: 2280].
2.  **Contiguous Memory:** Elements are stored strictly side-by-side in memory.
3.  [cite_start]**Static Entity:** The size is fixed once declared and cannot change during execution[cite: 2279].

#### Declaration and Indexing
* **Syntax:** `type arrayName[size];`
* [cite_start]**Indexing:** Starts at **0** and ends at **size - 1**[cite: 2270].
    * [cite_start]Accessing `array[size]` (out of bounds) is a common error[cite: 2321].

> [!Warning] ⚠️ "Off-by-One" Error
> The "7th element" is at index `6` (`array[6]`).
> [cite_start]`array[7]` is actually the 8th element [cite: 2261-2262].

---

### 1.2 Initialization

You can initialize arrays at the moment of declaration:

1.  **Sized Initialization:**
    ```c
    int n[5] = {1, 2, 3, 4, 5};
    ```
2.  **Partial Initialization:**
    ```c
    int n[5] = {1, 2}; 
    // Remaining elements n[2]...n[4] are automatically set to 0[cite: 2268].
    ```
3.  **Unsized Initialization:**
    ```c
    int n[] = {1, 2, 3}; 
    // Compiler automatically determines size is 3[cite: 2268].
    ```

---

### 1.3 Multidimensional Arrays

[cite_start]C supports "arrays of arrays", most commonly **2D Arrays** (Matrices)[cite: 2350].

> [!Syntax] 2D Array
> `type name[rows][columns];`
>
> [cite_start]* **Access:** `matrix[i][j]` (Row `i`, Column `j`)[cite: 2355].
> * **Memory:** Stored row by row.

**Initialization:**
```c
int b[2][2] = { {1, 2}, {3, 4} }; 
// Row 0: 1, 2
// Row 1: 3, 4
````

---

### 1.4 Passing Arrays to Functions

> [!Theorem] ⚡ Pass by Reference
> 
> When you pass an array to a function, you are actually passing the address of the first element.
> 
> * Effect: The function can modify the original array data1.
> 
> - **Syntax:** `void modify(int arr[], int size);`
>     

To prevent a function from modifying the array, use the `const` qualifier:

C

```
void readOnly(const int arr[]); // Compiler throws error if code tries to modify arr[cite: 2389].
```

---

### 1.5 Sorting Algorithms (Comprehensive)

Your course covers six specific sorting algorithms.

#### 1. Bubble Sort (Sinking Sort)

- **Concept:** Repeatedly compares adjacent pairs. If `arr[i] > arr[i+1]`, swap them. Large values "bubble" to the top (end)2.
    
- **Complexity:** Simple but slow ($O(n^2)$).
    

#### 2. Selection Sort

- **Concept:** Divide array into sorted and unsorted parts. Repeatedly **find the minimum** element in the unsorted part and swap it with the first unsorted element 3.
    
- **Process:**
    
    1. Find min in `arr[0...n]`, swap with `arr[0]`.
        
    2. Find min in `arr[1...n]`, swap with `arr[1]`.
        

#### 3. Insertion Sort

- **Concept:** Like sorting playing cards in your hand. Take one element and **insert** it into its correct position among the already sorted elements to its left 4.
    

#### 4. Merge Sort (Divide & Conquer)

- **Concept:**
    
    1. **Divide:** Recursively split array in half until elements are single.
        
    2. **Conquer:** Merge two sorted halves into a larger sorted array 5.
        
- **Key Function:** `merge(arr, left, mid, right)` uses temporary arrays to combine sorted lists.
    

#### 5. Quick Sort (Divide & Conquer)

- **Concept:**
    
    1. Pick a **Pivot** (e.g., last element).
        
    2. **Partition:** Reorder so elements $<$ pivot are left, $>$ pivot are right.
        
    3. Recursively sort the sub-arrays 6.
        
- **Performance:** Very efficient for large datasets.
    

#### 6. Heap Sort

- **Concept:** Build a **Binary Heap** (Max-Heap). Repeatedly extract the root (max value), move it to the end, and heapify the remaining tree 7.
    

---

## 2. 📘 Practical Exercises & Solutions

Per your syllabus requirements 8, here are the implementations for the practical exercises.

### Exercise 1: Sum & Average

**Problem:** Calculate sum and average of an integer array with $N$ elements.

> [!Code] Solution
> 
> C
> 
> ```
> #include <stdio.h>
> ```

> int main() {
> 
> int n, i, sum = 0;
> 
> float avg;
> 
> ```
> printf("Enter number of elements: ");
> scanf("%d", &n);
> int arr[n]; // Variable Length Array (C99)
> ```

> ```
> printf("Enter %d integers: ", n);
> for(i = 0; i < n; i++) {
>     scanf("%d", &arr[i]);
>     sum += arr[i];
> }
> ```

> ```
> avg = (float)sum / n;
> printf("Sum: %d\nAverage: %.2f", sum, avg);
> return 0;
> ```
> 
> }

### Exercise 4: Cyclic Permutation

Problem: Cyclically permute elements of an array $P$ times.

Input: 3 40 72 100 68, $P=3$

Output: 100 68 3 40 72

> [!Code] Solution
> 
> C
> 
> ```
> #include <stdio.h>
> ```

> void cyclicPermute(int arr[], int size, int p) {
> 
> // p % size handles cases where p > size
> 
> p = p % size;
> 
> int temp[size];

> ```
> for(int i = 0; i < size; i++) {
>     // New position logic: (current_index + p) % size
>     // Note: The example shifts RIGHT. 
>     // If input 3 40 72 100 68 -> shift 1 -> 68 3 40 72 100
>     // The example output shifts 3 40 72 100 68 -> 100 68 3 40 72 (Shift Right by 2? Or Left?)
>     // Let's strictly follow example pattern: 
>     // Original: [0]=3, [1]=40, [2]=72, [3]=100, [4]=68
>     // Output:   [0]=100, [1]=68, [2]=3, [3]=40, [4]=72
>     // 100 moved from idx 3 to 0. 68 moved from idx 4 to 1.
>     // This is a RIGHT ROTATION by 2.
>     
>     // Standard Right Rotate Logic:
>     // new_pos = (i + p) % size
>     // We need to place arr[i] into new_pos
> }
> // Simplified Printing Logic for Exam:
> // Print last P elements, then first Size-P elements
> ```
> 
> }

> int main() {
> 
> int arr[] = {3, 40, 72, 100, 68};
> 
> int n = 5;
> 
> int p = 2; // Based on the example output, P=2 gives the result shown

> ```
> // Logic to rotate right by P
> int temp[n];
> for(int i=0; i<n; i++) {
>     temp[(i + p) % n] = arr[i];
> }
> ```

> ```
> printf("Permuted: ");
> for(int i=0; i<n; i++) printf("%d ", temp[i]);
> return 0;
> ```
> 
> }

### Exercise 7: Add Two Matrices

**Problem:** Add two matrices $M \times N$.

> [!Code] Solution
> 
> C
> 
> ```
> #include <stdio.h>
> #define ROW 2
> #define COL 2
> ```

> int main() {
> 
> int a[ROW][COL] = { {1, 2}, {3, 4} };
> 
> int b[ROW][COL] = { {5, 6}, {7, 8} };
> 
> int sum[ROW][COL];

> ```
> for(int i = 0; i < ROW; i++) {
>     for(int j = 0; j < COL; j++) {
>         sum[i][j] = a[i][j] + b[i][j];
>         printf("%d ", sum[i][j]);
>     }
>     printf("\n");
> }
> return 0;
> ```
> 
> }

---

## 3. Summary

- **Definition:** Arrays are fixed collections of the same data type. .
    
- **Indexing:** Zero-based ($0$ to $N-1$).
    
- **Functions:** Arrays pass by reference (pointer decay), allowing functions to modify original data.
    
- **Sorting:**
    
    - **Simple:** Bubble, Selection, Insertion ($O(N^2)$).
        
    - **Efficient:** Merge, Quick, Heap ($O(N \log N)$).
        
- **2D Arrays:** Used for matrices; requires nested loops to traverse rows and columns.