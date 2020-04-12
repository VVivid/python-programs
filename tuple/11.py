"""Write a Python program to convert a list to a tuple."""

user_input_1 = tuple(map(int, input("Enter tuple: ").split()))
user_input_1_list = list(user_input_1)

print(f"Tuple: {user_input_1}\n"
      f"List: {user_input_1_list}")