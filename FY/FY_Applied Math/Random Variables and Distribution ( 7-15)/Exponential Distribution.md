Tags: [[Lecture 13.pdf]], [[Continuous Random Variables]], [[Expected Value ( Expectation)]], [[Variance]]

We usually use this to model ==failure times or waiting times==. It has a probability density function:
$$f(x)=\lambda e^{-\lambda x}$$
for $x\geq{0}$ and $\lambda>0$ 

Its cumulative distribution function is:
$$F(x)=\int^x_{0}\lambda e^{-\lambda y}\,dy=1-e^{-\lambda x}$$
The expectation is:
$$E(X)=\frac{1}{\lambda}$$
The variance is:
$$Var(X)=\frac{1}{\lambda^2}$$
Proof for those shit:

![[Screenshot 2025-01-02 211130.png]]