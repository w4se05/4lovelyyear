Tags: [[Lecture 12.pdf]], [[Bernoulli Random Variables]], [[Discrete Random Variables]]

>[!Definition]
>This random variable is used to count the number of trials conducted until achieving ==the first success==
>
>**REMEMBER THAT THIS IS A DISCRETE RANDOM VARIABLE**
>
### PMF of Geometric Random Variable
$$P(X=x)=(1-p)^{x-1}p$$
==> $x-1$ trials has been conducted before the first success

We have:
$$E(X)=\frac{1}{p}$$
$$Var(X)=\frac{1-p}{p^2}$$
### The CDF of Geometric Random Variable
$$P(X\leq x)=\sum_{i=1}^x(1-p)^{i-1}p=p\times\frac{1-(1-p)^x}{p}=1-(1-p)^x$$
