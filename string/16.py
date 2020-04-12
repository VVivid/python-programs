"""Write a Python program to generate and print a list of first
 and last 5 elements where the values are square of numbers between 1 and 30 (both included). """

lst = [x * x for x in range(1,31)]
print(lst[0:6], lst[-5:])