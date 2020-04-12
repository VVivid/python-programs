"""Write a Python program to clone or copy a list."""

user_input = list(map(int,input("Enter the orignal list: ").split()))
clone = user_input
print(f"Orignal list: {user_input}\n"
      f"Clone list: {clone}")