"""Write a Python program to generate and print a list except for the first 5 elements,
 where the values are square of numbers between 1 and 30 (both included)."""

lst = [x * x for x in range(1,21)]
print([item for number,item in enumerate(lst) if number not in range(0,5)])