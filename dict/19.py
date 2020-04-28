"""Write a Python program to combine two dictionary adding values for common keys."""

from collections import Counter

dictionary1 = {'a': 100, 'b': 200, 'c': 300}
dictionary2 = {'a': 300, 'b': 200, 'd': 400}
Sum = Counter(dictionary1) + Counter(dictionary2)
print(Sum)
