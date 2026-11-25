Tags: [[Lecture 10.pdf]], [[Joint Probability Distribution Function]]

Given the joint probability distribution function of 2 random variables X and Y. **What if we want to calculate specific $P(X=x)$ or $P(Y=y)$ ?**

Think in this way: Since the joint probability distribution illustrates $A\cap B$. It divine the $P(X)$ into many parts, so if we want to find a specific $P(X)$, we take the sum of all parts: 
$$\displaystyle\sum_{j}P(X=x,Y=j)$$
We call that Marginal Probability Mass Function
$$P(X=x_{i})=p_{i+}=\sum_{j}p_{ij}$$
Note: $p_{i+}$ means we take the sum of all $p_{ij}$ while $i$ staying constant and $j$ increasing. Similarly, with $p_{+j}$, $j$ stays constant while $i$ is increasing

By calculating $P(X)$, we can also calculate $E(X)$ and $Var(X)$

Example:

![[Screenshot 2024-12-07 121332.png |center]]

==Keep in mind that what we are doing have nothing to do with the other random variable==



