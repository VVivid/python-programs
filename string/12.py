""" Write a Python program to print a specified list after removing the 0th, 4th and 5th elements"""

Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print([item for number, item in enumerate(Sample_List) if number not in (0,4,5)])