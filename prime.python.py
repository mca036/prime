# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
Output

[114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]
In this program, we have used nested for loops to iterate through each row and each column. We accumulate the sum of products in the result.

This technique is simple but computationally expensive as we increase the order of the matrix.

For larger matrix operations we recommend optimized software packages like NumPy which is several (in the order of 1000) times faster than the above code.

Source Code: Matrix Multiplication Using Nested List Comprehension
# Program to multiply two matrices using list comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)
The output of this program is the same as above. To understand the above code we must first know about built-in function zip() and unpacking argument list using * operator.

We have used nested list comprehension to iterate through each element in the matrix. The code looks complicated and unreadable at first. But once you get the hang of list comprehensions, you will probably not go back to nested loops.

Share on:
Did you find this article helpful?
Related Examples
Python Example

Transpose a Matrix

Python Example

Add Two Matrices

Python Example

Make a Flattened List from Nested List

Python Example

Split a List Into Evenly Sized Chunks


Join our newsletter for the latest updates.
Enter Email Address*
Join


Tutorials
Python 3 Tutorial
JavaScript Tutorial
C Tutorial
J
