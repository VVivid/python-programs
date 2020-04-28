""" Write a Python program to insert a new item before the second element in an existing array. """

from array import *
array_test = array('i', [1, 3, 5, 7, 9])
print(f"Original array: {array_test}")
print("Insert new value 4 before 3:")
array_test.insert(1, 4)
print("New array: "+str(array_test))
