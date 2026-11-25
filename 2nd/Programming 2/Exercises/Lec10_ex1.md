1. Create a simple class with an overloaded **operator++.** Try calling this operator in both pre- and postfix form and see what kind of compiler warning you get. 

2. Create a simple class containing an **int** and overload the (binary) **operator+** as a member function. In other words, adding 2 objects of your class would result in the addition of the 2 corresponding integers. Test your class to show that it works correctly. 

3. Add a binary **operator-** to Exercise 2 as a member function. Demonstrate that you can use your objects in complex expressions like **a + b – c.** 

4. Add an **operator++** and **operator--** to Exercise 2 (and 3), both the prefix and the postfix versions, such that they return the incremented or decremented object. Make sure that the postfix versions return the correct value. 

5. Modify the increment and decrement operators in Exercise 4 so that the prefix versions return a non- **const** reference and the postfix versions return a **const** object. Show that they work correctly and explain why this should be done in practice. 

