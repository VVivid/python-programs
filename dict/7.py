"""Write a Python script to print a dictionary where the keys are numbers
 between 1 and 15 (both included) and the values are square of keys. """

n = 15
result = dict()
for item in range(1, n + 1):
    result[item] = item * item
print(result)
