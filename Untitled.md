### Problem 1: Matrix-Chain Multiplication

**Objective:** Compute the optimal parenthesization for a chain of five matrices to minimize scalar multiplications.

**Matrix Dimensions ($p_{i-1} \times p_i$):**

- $A_1: 8 \times 15$
    
- $A_2: 15 \times 4$
    
- $A_3: 4 \times 10$
    
- $A_4: 10 \times 12$
    
- $A_5: 12 \times 20$
    

This yields the dimension array $p = [8, 15, 4, 10, 12, 20]$.

**Step 1: Recurrence Relation**

To construct the dynamic programming cost table, we utilize the following recurrence relation for the minimum scalar multiplications $m[i, j]$ required to compute the matrix product $A_i \dots A_j$:

$$m[i, j] = \begin{cases} 0 & \text{if } i = j \\ \min_{i \le k < j} (m[i, k] + m[k+1, j] + p_{i-1}p_kp_j) & \text{if } i < j \end{cases}$$

**Step 2: Constructing the DP Cost Table (Part c & a)**

We evaluate chains of increasing length $L$.

- **Length $L=1$:** $m[i, i] = 0$ for all $i \in \{1, 2, 3, 4, 5\}$.
    
- **Length $L=2$:**
    
    - $m[1, 2] = 8 \times 15 \times 4 = 480$ (split at $k=1$)
        
    - $m[2, 3] = 15 \times 4 \times 10 = 600$ (split at $k=2$)
        
    - $m[3, 4] = 4 \times 10 \times 12 = 480$ (split at $k=3$)
        
    - $m[4, 5] = 10 \times 12 \times 20 = 2400$ (split at $k=4$)
        
- **Length $L=3$:**
    
    - $m[1, 3] = \min(0 + 600 + 480, 480 + 0 + 320) = \min(1080, 800) = 800$ (split at $k=2$)
        
    - $m[2, 4] = \min(0 + 480 + 720, 600 + 0 + 1800) = \min(1200, 2400) = 1200$ (split at $k=2$)
        
    - $m[3, 5] = \min(0 + 2400 + 800, 480 + 0 + 960) = \min(3200, 1440) = 1440$ (split at $k=4$)
        
- **Length $L=4$:**
    
    - $m[1, 4] = \min(0 + 1200 + 1440, 480 + 480 + 384, 800 + 0 + 960) = \min(2640, 1344, 1760) = 1344$ (split at $k=2$)
        
    - $m[2, 5] = \min(0 + 1440 + 1200, 600 + 2400 + 3000, 1200 + 0 + 3600) = \min(2640, 6000, 4800) = 2640$ (split at $k=2$)
        
- **Length $L=5$:**
    
    - $m[1, 5] = \min(0+2640+2400, 480+1440+640, 800+2400+1600, 1344+0+1920)$
        
    - $m[1, 5] = \min(5040, 2560, 4800, 3264) = 2560$ (split at $k=2$)
        

**Final Cost Table $m[i, j]$:**

|**i \ j**|**1**|**2**|**3**|**4**|**5**|
|---|---|---|---|---|---|
|**1**|0|480|800|1344|**2560**|
|**2**||0|600|1200|2640|
|**3**|||0|480|1440|
|**4**||||0|2400|
|**5**|||||0|

**a. Minimum number of scalar multiplications:** **2560**

**b. Optimal parenthesization:** By tracing the optimal splits $k$, we deduce the grouping: **$((A_1 A_2) ((A_3 A_4) A_5))$**

---

### Problem 2: 0/1 Knapsack Problem

**Objective:** Maximize the total value of items placed into a knapsack with capacity $W = 15$.

**Item Data:**

1. $w=2, v=12$
    
2. $w=3, v=10$
    
3. $w=5, v=20$
    
4. $w=7, v=15$
    
5. $w=1, v=5$
    
6. $w=6, v=18$
    

**Step 1: DP Table Construction (Part C)**

We define $dp[i][w]$ as the maximum value achievable using a subset of the first $i$ items with a total weight limit of $w$.

$$dp[i][w] = \begin{cases} dp[i-1][w] & \text{if } w_i > w \\ \max(dp[i-1][w], dp[i-1][w-w_i] + v_i) & \text{if } w_i \le w \end{cases}$$

Iterating through all items $i \in [1, 6]$ and weights $w \in [0, 15]$ constructs the following optimal substructure array.

**Complete DP Table:**

|**i \ w**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**0**|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|**1**|0|0|12|12|12|12|12|12|12|12|12|12|12|12|12|12|
|**2**|0|0|12|12|12|22|22|22|22|22|22|22|22|22|22|22|
|**3**|0|0|12|12|12|22|22|32|32|32|42|42|42|42|42|42|
|**4**|0|0|12|12|12|22|22|32|32|32|42|42|42|42|47|47|
|**5**|0|5|12|17|17|22|27|32|37|37|42|47|47|47|47|52|
|**6**|0|5|12|17|17|22|27|32|37|37|42|47|47|50|55|**55**|

**A. Maximum achievable value:** **55**

**B. Selected Items (Backtracking the Solution)**

To find which items are included in the optimal solution, we trace backward from $dp[6][15]$:

1. $dp[6][15] = 55$. Since $55 \neq dp[5][15] (52)$, **Item 6 is selected**. Remaining capacity: $15 - 6 = 9$.
    
2. $dp[5][9] = 37$. Since $37 \neq dp[4][9] (32)$, **Item 5 is selected**. Remaining capacity: $9 - 1 = 8$.
    
3. $dp[4][8] = 32$. Since $32 = dp[3][8]$, Item 4 is **not** selected. Remaining capacity: $8$.
    
4. $dp[3][8] = 32$. Since $32 \neq dp[2][8] (22)$, **Item 3 is selected**. Remaining capacity: $8 - 5 = 3$.
    
5. $dp[2][3] = 12$. Since $12 = dp[1][3]$, Item 2 is **not** selected. Remaining capacity: $3$.
    
6. $dp[1][3] = 12$. Since $12 \neq dp[0][3] (0)$, **Item 1 is selected**. Remaining capacity: $3 - 2 = 1$.
    

**Optimal Items Selected:** **Item 6, Item 5, Item 3, Item 1** (Total weight = 14, Total value = 55).

---

### Alternative Perspective: Memory Optimization

While a 2D table explicitly maps the overlapping subproblems required for a manual exam solution, implementing the 0/1 Knapsack algorithm in software rarely utilizes an $O(n \cdot W)$ space complexity matrix. Since calculating the current row only depends on the immediate preceding row, the state can be compressed into a 1D array of size $W+1$, iterating backwards through the weights to prevent using an item multiple times. This optimizes the space complexity strictly to $O(W)$.