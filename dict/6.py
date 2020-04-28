"""Write a Python script to generate and print a dictionary that contains a number
 (between 1 and n) in the form (x, x*x)."""

n = 5
result = dict()
for item in range(1, n):
    result[item] = item * item
print(result)
