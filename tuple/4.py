"""Write a Python program to unpack a tuple in several variables."""

item1, item2 = tuple(map(eval, input("Enter the value: ").split()))
print(f'Item1 = {item1}\n'
      f'Item2 = {item2}')
