#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2, 3, 5))

#4. Print a.

print (a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))

#6. Print b.

print (b)

#7. Do a and b have the same size? How do you prove that in Python code?

size_comparison = a.size == b.size
size_comparison
# Since the boolean is true, a and b have the same size

#8. Are you able to add a and b? Why or why not?

# c = a + b
# This will result in an error since a and b dont have the same shape. a is (2,3,5) and b is (5,2,3)

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
# It works now becase c is b transposed so that it has the same shape as a. Since they both have the same shape, they can be added

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print (a)
print (d)

# Since b (and therefore c) are arrays of ones, the result of adding a and c (d) is a matrix very similar to a but with 1 added to every number.


#12. Multiply a and c. Assign the result to e.

e = a * c

#13. Does e equal to a? Why or why not?

e == a
# yes because c is a matrix of only ones, multiplying 1 by any number results in itself. Therefore, multiplying any array by an array of the same shape of only ones, results in the same array.

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for x in range(0,d.shape[0]):
        for y in range(0,d.shape[1]):
                for z in range(0,d.shape[2]):
                        if d[(x,y,z)] == d_max:
                                f[(x,y,z)] = 100
                        elif d[(x,y,z)] == d_min:
                                f[(x,y,z)] = 0
                        elif d[(x,y,z)] == d_mean:
                                f[(x,y,z)] = 50
                        elif d[(x,y,z)] < d_mean:
                                f[(x,y,z)] = 25
                        elif d[(x,y,z)] > d_mean:
                                f[(x,y,z)] = 75
                        else:
                                print('error')

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(d)
print(f)
# Yes! no 50 is printed because no value is exactly the same as d_mean

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

g = np.empty((2,3,5),dtype=str)

for x in range(0,d.shape[0]):
        for y in range(0,d.shape[1]):
                for z in range(0,d.shape[2]):
                        if d[(x,y,z)] == d_max:
                                g[(x,y,z)] = 'E'
                        elif d[(x,y,z)] == d_min:
                                g[(x,y,z)] = 'A'
                        elif d[(x,y,z)] == d_mean:
                                g[(x,y,z)] = 'C'
                        elif d[(x,y,z)] < d_mean:
                                g[(x,y,z)] = 'B'
                        elif d[(x,y,z)] > d_mean:
                                g[(x,y,z)] = 'D'
                        else:
                                print('error')

g