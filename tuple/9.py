""" Write a Python program to find the repeated items of a tuple."""

user_input_1 = tuple(map(int, input("Enter tuple number01: ").split()))
user_input_2 = tuple(map(int, input("Enter tuple number02: ").split()))

print(f"Repeated item in tuple: {tuple([item for item in user_input_1 if item in user_input_2])}")
