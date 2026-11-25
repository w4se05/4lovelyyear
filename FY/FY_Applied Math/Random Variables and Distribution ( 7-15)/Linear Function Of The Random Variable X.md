Tags: [[Lecture 11.pdf]], [[Expected Value ( Expectation)]], [[Variance]], [[Standard Deviation]], 

Given a random variable X and a random variable Y taking value of X:
$$Y=aX+b$$
with $a$ and $b$ are constant and $a,b\in R$

We have:
$$E(Y)=aE(X)+b$$
$$Var(Y)=a^2Var(X)$$
Consequently:
$$\sigma_{Y}=|a|\sigma_{X}$$
Using those rules, we can manipulate the function to make the $E(Y)=0$ and $Var(Y)=1$
$$Y=\frac{1}{\sigma}X-\frac{u}{\sigma}$$
Furthermore, we can obtain the cumulative distribution function of $Y$:
$$F_{Y}(y)=P(Y\leq y)=P(aX+b\leq y)=P(aX\leq y-b)$$
If $a>0$:
$$F_{Y}(y)=P\left( X\leq \frac{y-b}{a} \right)=F_{X}\left( X\leq\frac{ y-b}{a} \right)$$
If $a<0$:
$$F_{Y}(y)=P\left( X\geq \frac{y-b}{a} \right)=1-F_{X}\left( X\leq\frac{ y-b}{a} \right)$$

