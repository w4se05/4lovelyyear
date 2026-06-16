## **Exercises (Template and container classes)** 

1. Let A is a generic matrix with the size of _nxn_ , and consider the following subset of matrix norm: 

   - Frobenius norm 

**==> picture [113 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
||𝐴||𝐹 𝑖𝑗|2<br>𝑖,𝑗<br>= √∑|𝑎<br>||𝐴||∞ = max𝑖 ∑|𝑎𝑖𝑗|<br>𝑗<br>= 𝑛⋅max<br>||𝐴||𝐺 𝑖,𝑗 [|𝑎][𝑖𝑗][|]<br>**----- End of picture text -----**<br>


- Row sum norm 

- Total norm 

Write a program to implementand test the above norms. 

2. Design and implement a generic Stack data structure in C++ using Class Templates. The Stack must operate on the LIFO (Last In, First Out) principle and be capable of storing any data type (e.g., int, double, char, std::string). 

   - Create a class template named Stack<T> with the following components: 

## _* Private Attributes_ 

- _T* arr_ : A dynamic array pointer to store the elements of type T. 

- _int capacity_ : The maximum number of elements the stack can hold. 

- _int topIndex_ : An integer tracking the index of the top element. It should be initialized to -1 when the stack is empty. 

## _* Public Methods_ 

- Constructor _Stack(int size)_ : Allocates dynamic memory for the array with the given _size_ and initializes _topIndex_ to -1. 

- Destructor _~Stack()_ : Safely deallocates the dynamically allocated memory to prevent memory leaks. 

- _bool isEmpty()_ : Returns _true_ if the stack contains no elements, otherwise false. 

- _bool isFull()_ : Returns _true_ if the stack has reached its maximum capacity, otherwise false. 

- _void push(T value)_ : Inserts a new element onto the top of the stack. If the stack is full, print an error message (Stack Overflow). 

- _T pop()_ : Removes and returns the top element of the stack. If the stack is empty, print an error message (Stack Underflow) and return a default value T(). 

- _T peek()_ : Returns the top element without removing it. If the stack is empty, 

   - handle the error gracefully. 

