"""Write a Python program to sort (ascending and descending) a dictionary by value."""

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ', d)
sorted_descending = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
sorted_ascending = dict(sorted(d.items(), key=lambda x: x[0]))
print(sorted_ascending)
print(sorted_descending)
