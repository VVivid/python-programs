"""Write a Python program to get the difference between the two lists."""

list1 = [1, 2, 3, 4]
list2 = [1, 2]

print(list(set(item for item in list2 for items in list1 if item != items)))