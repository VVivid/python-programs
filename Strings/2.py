"""Write a Python program to count the number of characters (character frequency) in a string."""

Sample_String = 'google.com'
result = dict()
for item in Sample_String:
    result[item] = Sample_String.count(item)
print(result)