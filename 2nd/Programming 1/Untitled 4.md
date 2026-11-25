#### 1. Syntax & formatting (The "Stupid" Mistakes)

- [ ] **Struct Semicolon:** Check every `struct`. Does it end with `};`? 1
    
    - _Right:_ `struct Book { ... };`
        
- [ ] **Loop/If Semicolons:** Did you accidentally put a `;` after `if` or `for`?
    
    - _Wrong:_ `if (x > 5);` (Delete the semicolon!)
        
- [ ] **Matching Braces:** Count your `{` and `}`. Do they match? Indent your code on the paper so you can see them clearly. 2
    
- [ ] **Header Files:** Did you write `#include <stdio.h>` and `<string.h>` (if using strings)? 3
    

#### 2. Variables & Data Types

- [ ] **Integer Division:** Are you dividing two integers?
    
    - _Wrong:_ `float avg = sum / n;` (if sum/n are int).
        
    - _Right:_ `float avg = (float)sum / n;`
        
- [ ] **Initialization:** Did you set counters to 0?
    
    - _Check:_ `int sum = 0;`, `int count = 0;`. Uninitialized variables have garbage values.
        
- [ ] **Scanf Ampersands:** Check every `scanf`.
    
    - _Int/Float:_ Needs `&`. `scanf("%d", &x);` 
        
    - _String:_ NO `&`. `scanf("%s", str);` 
        

#### 3. Control Flow (Logic)

- [ ] **Equality Check:** Look at every `if`. Did you use `==`?
    
    - _Fatal:_ `if (x = 5)` sets x to 5.
        
    - _Right:_ `if (x == 5)` compares x to 5. 6
        
- [ ] **Infinite Loops:** Check your `while` loop. Does the condition variable change inside the loop? 7
    
- [ ] **Switch Breaks:** Did you put `break;` after every `case`? If not, it falls through to the next one. 8
    

#### 4. Pointers & Arrays

- [ ] **Array Bounds:** If array size is `N`, valid indices are `0` to `N-1`.
    
    - _Check:_ Loops should typically be `i < N`, **NOT** `i <= N`. 9
        
- [ ] **Pointer Access:**
    
    - To get the value: `*ptr`
        
    - To get the address: `ptr` (or `&variable`) 10
        
- [ ] **Dereference Safety:** never write `*ptr` if `ptr` might be NULL or uninitialized.
    

#### 5. Strings (The "C" Special)

- [ ] **Comparison:** NEVER use `str1 == str2`.
    
    - _Right:_ `strcmp(str1, str2) == 0`. 11
        
- [ ] **Assignment:** NEVER use `str1 = "Hello"`.
    
    - _Right:_ `strcpy(str1, "Hello");`. 12
        
- [ ] **Space Input:** If reading a sentence, use `fgets(str, size, stdin)` or `scanf("%[^\n]", str)`. `scanf("%s")` stops at space. 13
    
- [ ] **Sizing:** array size must be `Length + 1` for the `\0`. 14
    

#### 6. Structs

- [ ] **Access:**
    
    - Variable: `s1.age` (Dot) 15
        
    - Pointer: `ptr->age` (Arrow) 16
        

#### 7. File I/O (Crucial)

- [ ] **Open Check:** Immediately after `fopen`, write:
    

    ```c
    if (fptr == NULL) { printf("Error"); return 1; }
    ```
    
- [ ] **Mode:**
    
    - Reading? `"r"` 18
        
    - Writing (new file)? `"w"` 19
        
    - Appending? `"a"` 20
        
- [ ] **Close:** Did you `fclose(fptr)` at the end? 21
    

### 🚨 "Panic Button" (If you get stuck)

- **Blank out?** Check the "Cheat Sheet" I made you earlier.
    
- **Logic not working?** Trace it manually. Write `i=0, sum=0` on scratch paper and step through your own code line-by-line.
    
- **Don't know the syntax?** Look at your lecture slides for a similar example and copy the pattern.
    

**You are ready. Good luck!**