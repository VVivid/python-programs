""" Write a Python program to remove duplicates from a list"""

user_input = list(map(int,input("Enter the list: ").split()))
print(f"Input list: {user_input}\n"
      f"Result: {list(set(user_input))}")