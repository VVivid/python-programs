"""Write a Python program to create an array of 5 integers and
 display the array items. Access individual element through indexes. """

from array import *

array_test = array('i', [1, 2, 3, 4, 5, 6])

print(array_test)
for item in array_test:
    print(item)
print('Access item by index:')
for item in range(len(array_test)):
    print(array_test[item])
