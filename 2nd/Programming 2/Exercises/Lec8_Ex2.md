1. Consider the following class declarations in C++: class C { protected: int x; public: void f(){...}; }; class C1: public C { protected: int x1; public: void h(C *obj){...}; }; class C2: public C1 { public: int x2; }; class C3: public C { public: f(){...}; }; 

- a. Draw the class hierarchy 

- b. Assume that main contains the following declaration: 

C1 obj1; 

For each of the following expressions, say whether it is allowed in the code of main or not (they can be forbidden either because they violate the class definition or the protection mechanism) 

obj1.x , obj1.f() , obj1.x1 , obj1.x2 

- c. Assume that the body of C1::h contains the following declarations 

C2 *obj2; C3 *obj3; 

For each of the following expressions, say whether it is allowed in the body of C1::h or not 

obj->x , obj2->x , obj3->x 

2. Refer to the following figure. Write a C++ program, defining base class and derived classes as well as instantiating objects as in the figure. 

**==> picture [220 x 59] intentionally omitted <==**

**----- Start of picture text -----**<br>
Shape<br>Rectangle  Triangle<br>**----- End of picture text -----**<br>


3. Define classes according to the following inheritance hierarchy. Explore the order of execution of constructors when an object of class D is created. 

**==> picture [167 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
A1  A2  B1  B2<br>C1  C2<br>D<br>**----- End of picture text -----**<br>


4. Create a simple “shape” hierarchy: a base class called **Shape** and derived classes called **Circle, Square,** and **Triangle.** In the base class, make a virtual function called **draw( )** , and override this in the derived classes. Make an array of pointers to **Shape** objects while each element is either a **Circle,** a **Square,** or a **Triangle** (and thus perform upcasting of the pointers), then call **draw()** through the base-class pointers, to verify the behavior of the virtual function. (This is similar to the example presented in the lecture note.) 

5. Assume that we have now boarded a starship to search for a planet that will sustain life (e.g. has an atmosphere and is at the right distance from the sun) beyond our Earth. Just like our galaxy, planets orbit the sun, have gravity, are affected by their distance from the sun, and may or may not have atmospheres. Our orbits will be affected by the gravitational pull of large neighboring planets, suns, and even moons. 

Your program should include the following components: 

## **A galaxy** : 

- a. A galaxy consisting of at least two solar systems with at least 5 planets each. 

- b. For each planet, there may be different types (terrestrial (inner) planets and gas giants (outer planets)). Terrestrial planets have solid surfaces. 

- c. For each planet, the distance from the sun, the size of the planets, and the information about the atmosphere must be affected by a random number generator. It should not be predictable, and it should not be the same each time you run your program. 

- d. The remaining information can be read from an external data file (e.g. such as the planet’s name and the sun that the planet is orbiting). 

- e. Information about the solar system should not be hard coded! 

## **A small spaceship:** 

- a. To get the spaceship where we want it to go, we need to know how fast it needs to go and take the gravity of large bodies (like planets and suns) into account as it will bend the flight of our spaceship. Use your imagination and have some fun with this! 

The program can also determine if each planet is habitable or not. It should have a data structure for a dynamically allocated array of solar 

systems, with a doubly linked list of all planets in that solar system arranged by distance. 

