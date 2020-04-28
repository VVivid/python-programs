"""Write a Python program to append items from a specified list."""

from array import *

array_test = array('i', [4])
num_test = [1, 2, 3, 4]
print(f"Items in the list: {num_test}")
print(f"Append items from the list: ")
array_test.fromlist(num_test)
print("Items in the array: "+str(array_test))