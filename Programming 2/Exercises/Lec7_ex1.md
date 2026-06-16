**Question 1)** Design and implement a simple E-Wallet system that allows users to manage their digital balance and perform basic financial transactions securely. This system allows users to (1) store money, (2) transfer funds, and (3) perform transactions. The core requirements include: 

- Each user has a wallet that stores a balance and cannot be accessed directly from outside of the class 

- The system allows performing transactions such as (1) adding money to a wallet (amount must be positive), (2) withdrawing money from a wallet (not exceed current balance), and (3) transferring money from one wallet to another. 

- Every transaction should be recorded (E.g. _[Time] Nam transferred 10 million to B_ ). 

**Question 2)** Are the following class declarations incorrect? If so, how can they be fixed? Explain. 

a) class C1 { private: int x; public: C1() { x=10; } void setx(int value) {x= value;}; }; class C2 { private: int x; public: void show(C1 x) { std::cout << x.x; }; b) class C { private: int x; public: C() { x=10; } void setx(C x); }; C::setx(C x) { x.x=100; } 

