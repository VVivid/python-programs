""" Write a Python program to remove an item from a tuple."""

user_input_1 = tuple(map(int, input("Enter tuple: ").split()))
lst_user_input = list(user_input_1)
lst_user_input.remove(2)
print(f"Original Tuple: {user_input_1}\n"
      f"After delete: {tuple(lst_user_input)}")
