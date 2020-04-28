"""Write a Python program to print all unique values in a dictionary."""

Test = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print("Original List: ", Test)
result = set(val for dic in Test for val in dic.values())
print("Unique Values: ", result)
