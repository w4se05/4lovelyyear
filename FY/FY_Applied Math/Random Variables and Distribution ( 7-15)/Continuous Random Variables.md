Tags: [[Lecture 8.pdf]]

#RandomVariables 

> [!Definition]
> - We use continuous random variables to illustrate the probability of all outcomes which can take any value in an interval $[x,y]$
> - We will consider using continuous random variables when there are ==unlimited or uncountable== outcomes
> 

## 1. Probability Density Function

![[Screenshot 2024-11-28 211302.png]]

The probability that the random variables lies between $a$ and $b$ is given by:
$$P(a\leq X\leq b)=\int_{a}^{b}f(x)dx $$
With:
- $f(x)\geq 0\:\forall\: x$
- $\int_{state\;space}\,f(x)dx=1$
### *Note: The probability that a random variable takes the specific value of a is 0*
$$P(X=a)=\int_{a}^af(x)dx=0$$
## 2. Cumulative Distribution Function

It work the same way with that of [[Discrete Random Variables]]
$$F(x)=P(X\leq x)$$
Since $F(x)$ is a continuous and increasing function:
- $F(X\leq state\; space)=0$
- $F(X\geq state\;space)=1$

![[Screenshot 2024-11-28 214604.png]]

## 3. The link between pdf and cdf

Given the $f(x)$, we have:
$$F(x)=\int_{-\infty}^x  f(x)\,dx$$
Given the $cdf$, we have:
$$f(x)=F'(x)$$