"""Write a Python program to convert a list of tuples into a dictionary."""

test = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
dic = {}
for key, value in test:
    dic.setdefault(key, []).append(value)
print(dic)
