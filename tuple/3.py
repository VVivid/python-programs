"""Write a Python program to create a tuple with numbers and print one item."""

user_input = tuple(map(int,input("Enter the value: ").split()))
print(f"Entire values in tuple: {user_input}\n"
      f"First values in tuple: {user_input[0]}")
