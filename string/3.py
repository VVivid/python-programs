"""Write a Python program to get the largest number from a list"""

user_input = list(map(int,input("Enter the number in list: ").split()))
print(f"Input list: {user_input}\n"
      f"Result: {max(user_input)}")