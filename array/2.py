"""Write a Python program to append a new item to the end of the array. """
from array import *

array_test = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original Array {}".format(array_test))
array_test.append(10)
print('Update array :')
print(array_test)
