"""Write a Python program to find the list of words that are longer than n from a given list of words."""

user_input = list(map(str,input("Enter the words you want to check: ").split()))
Length = int(input("Get words that has length more than: "))
result = list(filter(lambda x: len(x) > Length, user_input))
print(f'Input words: {" ".join(user_input)}\n'
      f"Result: {' '.join(result)}")
