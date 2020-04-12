""" Write a Python function that takes two lists and returns True if they have at least one common member."""

def check_common(lst1, lst2):
    for item in lst1:
        for items in lst2:
            if item == items:
                return 'Yes'
    return 'No'

print(check_common([1,2,3,4,5], [5,6,7,8,9]))
print(check_common([1,2,3,4,5], [6,7,8,9]))