"""Write a Python program to convert an array to an ordinary list with the same items. """

from array import *
array_test = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print(f"Original array: {array_test}")
num_test = array_test.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_test)
