"""Write a Python program to multiplies all the items in a list."""
import math

user_input = list(map(int, input("Enter the number in list: ").split()))
print(f"Input lsit: {user_input}\n"
      f"Result: {math.prod(user_input)}")
