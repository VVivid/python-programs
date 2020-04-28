"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string."""


def string_both_ends(user_input):
    if len(user_input) < 2:
        return 'Length smaller than 2'

    return user_input[0:2] + user_input[-2:]


print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))
