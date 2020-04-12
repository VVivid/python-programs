""" Write a Python program to convert a tuple to a string."""

user_input = tuple(map(str, input("Input tuple: ").split()))
print(f"Input tuple: {user_input}\n"
      f"Result: {' '.join(user_input)}")