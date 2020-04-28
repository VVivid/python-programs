"""Write a Python program to get the number of occurrences of a specified element in an array"""

from array import *

array_num = array('i', [1, 2, 3, 4, 4, 5, 6])
print(f"Original array: {array_num}")
print("Number of occurrences of the number 4 in the said array: " + str(array_num.count(4)))
