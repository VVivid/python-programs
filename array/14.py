"""Write a Python program to find whether a given array of integers contains any duplicate element.
Return true if any value appears at least twice in the said array and return false if every element is distinct."""


def test_duplicate(array_test):
    nums_test = set(array_test)
    return len(array_test) != len(nums_test)


print(test_duplicate([1, 2, 3, 4, 5]))
print(test_duplicate([1, 2, 3, 4, 4]))
print(test_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]))
