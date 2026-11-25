Tags: [[Lecture 9.pdf]], [[Expected Value ( Expectation)]]

Imagine we have a graph of random variables and we have calculated the expected values of that function. The problem is that expected values can not be satisfactory to people. They want to know more about the function. So they ask themself: How spread is the graph from the expectation ?

To answer that question, we have to calculate the average distance between each component of the graph and the expected value. Which looks like this
$$Average\;distance = \displaystyle\sum_{i}p_{i}|x_{i}-E(X)|$$
	*Note that E(X) is just a ==constant*==

However, since the absolute value is too hard to work with, they come up with the idea to use the square to make it disappeared.
$$Average\;distance\,^2= {\displaystyle\sum_{i}p_{i}(x_{i}-E(X))^2}=E((x_{i}-E(X))^2)$$
Or:
$$Average \;distance\,^2= E(X^2)-E(X)^2$$
 So, we define $Average \;distance\,^2$ as $Var(X)$ and $Average$ $distance$ as [[Standard Deviation]] or $\sigma$
 