"""Write a Python program to get the length in bytes of one array
item in the internal representation."""

from array import *

array_test = array('i', [1, 2, 3, 4, 5, 6, 7])
print(f"Array {array_test}\n"
      f"Length in bytes of one array item {array_test.itemsize}")
