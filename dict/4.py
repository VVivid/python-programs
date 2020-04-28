"""Write a Python script to check whether a given key already exists in a dictionary."""

example = {'StudentA': 'David', 'StudentB': 'David2'}
test = ['StudentA', 'StudentC']

for item in test:
    if item in example:
        print(f"{item} is in the dictionary and the value is {example[item]}")
    else:
        print(f"{item} not in dictionary")

