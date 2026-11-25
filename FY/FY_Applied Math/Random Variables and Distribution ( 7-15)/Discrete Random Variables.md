Tags: [[Lecture 7.pdf]]

#RandomVariables

> [!Definition]
> - Each discrete random variables match with each outcomes of the event
> - We will consider using discrete random variables when there is a ==limited and countable== numbers of outcomes.

![[Screenshot 2024-11-27 183857.png]]
## 1. Probability Mass Function

 It is a set of all probability values of each discrete random variable. Those value is said to be $p_{i}$
$$P(X=x_{i})=p_{i}$$
 With:
 - $0<p_{i}<1$
 - $\displaystyle\sum_{i} p_{i} = 1$
### We can illustrate pmf in 2 ways:

![[Screenshot 2024-11-27 210013.png]]

## 2. Cumulative Distribution Function
We use this when we want to illustrate the proportion of each discrete random variable. 
$$F(x)=P(X\leq x)$$
 Example of illustrating cdf:
 
![[Screenshot 2024-11-27 212112.png]]
## 3. The link between pmf and cdf
Given the pmf, we have:

 $F(x)=\displaystyle\sum_{y\leq x} P(X=y)$

Given the cdf, we have:

$P(X=x)=F(x)-F(x^-)$

