"""Write a Python program to remove a specified item using the index from an array."""

from array import *
array_test = array('i', [1, 2, 3, 4, 5])
print(f"Original array: {array_test}")
print("Remove the fourth item form the array:")
array_test.pop(3)
print("New array: "+str(array_test))
