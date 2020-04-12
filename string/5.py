"""Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings."""

Sample_List = ['abc', 'xyz', 'aba', '1221']
print(f"Input list: {Sample_List}\n"
      f"Result: {len(list(filter(lambda x : x[0] == x[-1], Sample_List)))}")