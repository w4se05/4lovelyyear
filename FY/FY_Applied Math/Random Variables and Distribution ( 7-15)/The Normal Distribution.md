Tags: [[Lecture 14.pdf]], [[Continuous Random Variables]]

>[!Definition]
>The standard normal distribution $X$ having mean $μ = 0$ and variance $σ^2$ = 1 is denoted by $X\sim N(\mu,\sigma^2)$
>The graph of f is a bell-shaped curve that is symmetric about $μ$

### The p.d.f of $X$ ~ $N(\mu,\sigma^2)$ is:
$$f(x)=\frac{1}{\sigma \sqrt{ 2\pi }}~e^{\frac{-(x-\mu)^2}{2\sigma^2}}$$
![[Screenshot 2025-01-09 214350.png]]

### The standard normal distribution:
$X\sim N(0,1)$ is called the standard normal distribution. Respectively, we have its p.d.f:
$$\phi(x)=\frac{1}{ \sqrt{ 2\pi }}~e^{\frac{-x^2}{2}}~~~~~,x\in R$$
and its c.d.f:
$$\Phi(x)=\displaystyle\int^x_{-\infty}\phi(y)\,dy~~~~~,x\in R$$
### From $N(\mu,\sigma^2)$ to $N(0,1)$

$$P(X\leq x)=\Phi\left( \frac{x-\mu}{\sigma} \right)$$
This make calculate cdf easier