""" Write a Python program to check a list is empty or not"""

user_input = list(map(int,input('Enter the list: ').split()))
print(f"Input list: {user_input}\n"
      f"Result: {'List Empty' if len(user_input) == 0 else 'Not Empty'}")
