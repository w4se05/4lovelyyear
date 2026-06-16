1. Write a C++ program to input data from a text file to an array, the text file containing the information of shapes on the coordinate plane has the following format: 

   - The first line contains the number of shapes (max. 100). 

   - From the second line onwards is the information of each shape; the first character is the type of shape (t->triangle, r->rectangle and s->square) followed by the coordinates of the vertices of that shape. 

For example, file input.txt 

2 t  0  1  1  3  12  1 r  1  2  4  8 

means that there are two shapes. The first shape is a triangle with the vertex’s coordinates (0,1), (1,3), and (12,1), respectively. The second shape is a rectangle with the coordinates of lower-left and upper-right corners being (1,2) and (4,8) respectively. 

2. Compute and the area of each shape and save the shapes in the output file in the decreasing order of their area, for example the output file (output.txt) should be 

2 r  1  2  4  8 -> 18 t  0  1  1  3  12  1->12 

3. Extend the processing capabilities in question 2 to a new shape, parallelogram. The information read from the file in the case of a parallelogram is (p x1 y1 y2 x2 y3 y4), where (x1, y1), (x1, y2), (x2 y3) and (x2, y4) are the coordinates of parallelogram. 

Hints: Use the principles of inheritance and polymorphism in OOP. 

