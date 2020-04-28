"""Write a Python program to reverse the order of the items in the array."""

from array import *

array_test = array('i',[1,2,3,4,5,6,7])
array_test_reverse = array_test[::-1]
print(f"Original Array: {array_test}\n"
      f"Reverse Array: {array_test_reverse}")
