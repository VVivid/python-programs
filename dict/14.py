"""Write a Python program to sort a dictionary by key."""

color_dict = {'red': '#FF0000',
              'green': '#008000',
              'black': '#000000',
              'white': '#FFFFFF'}

for item in sorted(color_dict):
    print(item, color_dict[item])
