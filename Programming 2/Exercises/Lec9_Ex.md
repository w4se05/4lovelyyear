1. Create a simple “shape” hierarchy: a base class called **Shape** and derived classes called **Circle, Square,** and **Triangle.** In the base class, make a virtual function called **draw( )** , and override this in the derived classes. Make an array of pointers to **Shape** objects while each element is either a **Circle,** a or a 

**Square, Triangle** (and thus perform upcasting of the pointers), then call **draw()** through the base-class pointers, to verify the behavior of the virtual function. (This is similar to the example presented in the lecture note.) 

2. Modify Exercise 1 so **draw( )** is a pure virtual function. Try creating an object of type **Shape.** Try to call the pure virtual function inside the constructor and see what happens. Leaving it as a pure virtual, give **draw( )** a definition. 

3. Expanding on Exercise 2, create a function that takes a **Shape** object _by value_ and try to upcast a derived object in as an argument. See what happens. Fix the function by taking a reference to the **Shape** object. 

4. Assume that each shape has the data members of sizes and its area. Inside the class defines the _print_ () method that prints the area. Write the _double area_ () method to calculate the area of Shape. 

5. Create an array of _N_ shapes (each element is a circle, square, or trangle). Set the sizes of each shape and print its area in the decreasing order. 

