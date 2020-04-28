"""Write a Python program to append items from inerrable to the end of the array."""

from array import *

array_test = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_test))
array_test.extend(array_test)
print("Extended array: "+str(array_test))
