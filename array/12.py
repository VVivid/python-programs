"""Write a Python program to remove the first occurrence of a specified element from an array."""

from array import *
array_test = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print(f"Original array: {array_test}")
print("Remove the first occurrence of 3 from the said array:")
array_test.remove(3)
print("New array: "+str(array_test))
