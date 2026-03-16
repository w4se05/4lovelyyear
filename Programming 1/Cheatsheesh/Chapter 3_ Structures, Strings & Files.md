## 1. Conceptual Section (Teach Mode)

### 1.1 Structures (`struct`)
A structure groups variables of *different* types under a single name.

> [!Definition] Struct Definition
> ```c
> struct Student {
>     int id;
>     char name[50];
>     float gpa;
> }; // Don't forget the semicolon!
> ```
> * **Accessing Members**: Use the dot operator `.` (e.g., `s1.id = 10;`).
> * **Pointer to Struct**: Use the arrow operator `->` (e.g., `ptr->id = 10;`).

**Array of Structures:**
Instead of managing 100 separate names and IDs, use: `struct Student class_list[100];`
* Access: `class_list[0].gpa = 3.5;`

---

### 1.2 Strings (Advanced)
A string is a null-terminated character array.

> [!Warning] The Null Terminator (`\0`)
> C strings **must** end with a special character `\0` (ASCII 0) to mark the end.
> * `char s[5] = "Hello";` $\rightarrow$ **WRONG** (Needs 6 bytes: 'H','e','l','l','o','\0').
> * `char s[6] = "Hello";` $\rightarrow$ **Correct**.

**Standard Library `<string.h>`**:
* `strlen(s)`: Returns length (excluding `\0`).
* `strcpy(dest, src)`: Copies `src` to `dest`.
* `strcmp(s1, s2)`: Returns `0` if equal, `<0` if `s1` comes before `s2`, `>0` if after.

**Character Handling `<ctype.h>`**:
* `isdigit(c)`: Checks if character is '0'-'9'.
* `toupper(c)`: Converts 'a' $\rightarrow$ 'A'.

---

### 1.3 File Input/Output
Used to store data permanently.

> [!Definition] File Operations
> 1.  **Open**: `FILE *fp = fopen("filename.txt", "mode");`
>     * Modes: `"r"` (read), `"w"` (write - overwrites), `"a"` (append).
> 2.  **Check**: Always check if `fp == NULL` (file didn't open).
> 3.  **Process**:
>     * `fprintf(fp, ...)`: Write to file.
>     * `fgets(buffer, size, fp)`: Read a line.
>     * `fscanf(fp, ...)`: Read formatted data.
> 4.  **Close**: `fclose(fp);` (Critical to save data).

---

## 2. Application Section (Exam Mode)

### 📘 Examples & Applications

> [!Example] Ex 1: Student Database (Structs + Arrays)
> **Using**: Structs, Loops, Input
> **Problem**: Store data for 3 students and find the one with the highest GPA.
>
> **Solution**:
> ```c
> #include <stdio.h>
> 
> struct Student {
>     int id;
>     float gpa;
> };
> 
> int main() {
>     struct Student s[3];
>     int i, bestIndex = 0;
> 
>     // Input Loop
>     for(i = 0; i < 3; i++) {
>         printf("ID: ");
>         scanf("%d", &s[i].id);
>         printf("GPA: ");
>         scanf("%f", &s[i].gpa);
>         
>         // Logic: Check max immediately
>         if (s[i].gpa > s[bestIndex].gpa) {
>             bestIndex = i;
>         }
>     }
>     
>     printf("Best Student ID: %d", s[bestIndex].id);
>     return 0;
> }
> ```

> [!Example] Ex 2: Manual String Length (No `<string.h>`)
> **Using**: While Loop, Null Terminator
> **Problem**: Write a function `myStrlen` that calculates string length without libraries.
>
> **Solution**:
> ```c
> int myStrlen(char str[]) {
>     int count = 0;
>     // Loop until we hit the null terminator
>     while (str[count] != '\0') {
>         count++;
>     }
>     return count;
> }
> ```

> [!Example] Ex 3: Reading a File
> **Using**: `fopen`, `fgets`, Loop
> **Problem**: Read "data.txt" and print its content line by line.
>
> **Solution**:
> ```c
> #include <stdio.h>
> 
> int main() {
>     FILE *fptr;
>     char buffer[100]; // Buffer to hold one line
> 
>     fptr = fopen("data.txt", "r");
> 
>     // Safety Check
>     if (fptr == NULL) {
>         printf("File open error!");
>         return 1;
>     }
> 
>     // Read until End of File (NULL)
>     while (fgets(buffer, 100, fptr) != NULL) {
>         printf("%s", buffer);
>     }
> 
>     fclose(fptr);
>     return 0;
> }
> ```

---

## 3. Summary for Revision

* **Struct Semicolon**: `struct X { ... };` ← If you forget this `;` after the closing brace, the compiler will generate very confusing errors later in the code.
* **String Assignment**: You cannot do `str = "Hello";` after declaration. You MUST use `strcpy(str, "Hello");`.
* **File Safety**: Always check `if (fptr != NULL)` before reading/writing.
* **Buffer Overflow**: When reading strings with `scanf("%s", buf)`, it stops at whitespace. Use `fgets` for sentences.

---