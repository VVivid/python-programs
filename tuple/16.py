"""Write a Python program to convert a tuple to a dictionary. """
test = ((1, "David"), (2, "Lily"))
print(dict((y, x) for x, y in test))
