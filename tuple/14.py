"""Write a Python program to find the index of an item of a tuple."""

test = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(f"Original Tuple: {test}")
for index, item in enumerate(test):
    print(f"Index{index}: {item}")
