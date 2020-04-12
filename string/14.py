"""Write a Python program to print the numbers of a specified list after removing even numbers from it."""

num = [7,8, 120, 25, 44, 20, 27]
print(list(filter(lambda x: x % 2 !=0, num)))