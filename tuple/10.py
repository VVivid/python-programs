"""Write a Python program to check whether an element exists within a tuple."""

user_input_1 = tuple(map(int, input("Enter tuple: ").split()))
find = 2
print(find in user_input_1)
