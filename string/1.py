"""Write a Python program to sum all the items in a list."""

user_input = list(map(int, input("Enter the number in list: ").split()))
print(f"Input list:{user_input}\n"
      f"Result: {sum(user_input)}")
