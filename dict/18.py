"""Write a Python program to check a dictionary is empty or not. """


def empty_or_not(dic):
    if len(dic) == 0:
        return "empty"
    else:
        return "not empty"


print(empty_or_not({}))
