Tags: [[Lecture 12.pdf]], [[Bernoulli Random Variables]],[[Linear Function Of The Random Variable X]], [[Sum of Random Variables]], [[Discrete Random Variables]]

> [!Definition]
> Given ==discrete and independent== Bernoulli random variables $X_{1},X_{2},X_{3},\dots,X_{n}$ whose $p$ are the same.
>  
> $X=X_{1}+X_{2}+X_{3}+\dots+X_{n}$ is called binomial random variable 
> 
> $X$ is denoted by $X\sim B(n,p)$

We have:
$$E(X)=E(X_{1})+E(X_{2})+E(X_{3})+\dots+ E(X_{n})=n\,p$$
With Var(X), it is a bit more special. We cannot just add the $Var(X_{i})$ together, because of the Covariance. However, if the X1, X2,... are independent, we have:
$$Var(X)=Var(X_{1})+Var(X_{2})+\dots+Var(X_{n})=n\,p(1-p)$$
### P.M.F of Binomial Random Variable
$$P(X=x)=\binom{n}{x}\,(1-p)^{n-x}\,p^x$$
Example:
![[Screenshot 2024-12-22 225606.png]]

### With $Y=\frac{X}{n}$
We have: 
- $E(Y)=\frac{1}{n}np=p$
- $Var(Y)=\frac{1}{n^2}np(1-p)=\frac{p(1-p)}{n}$
