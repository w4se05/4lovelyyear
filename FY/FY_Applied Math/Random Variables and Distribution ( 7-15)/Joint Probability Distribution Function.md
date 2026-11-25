Tags: [[Lecture 10.pdf]],, [[Discrete Random Variables]], [[Intersection]]

> [!Definition]
> We have two random variable X and Y, which illustrate the outcome of two random events A and B, and the joint probability distribution of X and Y illustrates $A\cap B$

Example:
	An air-conditioner repairing company want to schedule
their employee more efficient. By using joint probability distribution function, they recognize that the service time depends to the number of air conditioner units

![[Screenshot 2024-12-07 112230.png|center]]

## 1. Joint Probability Mass Function

It works the same way as the probability of mass function of [[Discrete Random Variables]].
$$\sum_{i}\sum_{j}p_{ij}=1$$
With: $p_{ij}=P(X=i,Y=j)$
Note that the comma stands for AND, which can be understood as $\cap$
## 2. Joint Cumulative Distribution Function

$$F(x,y)=P(X\leq x,Y\leq y)=\sum_{i::x_{i}\leq x}\sum_{j::y_{j}\leq y}p_{ij}$$
