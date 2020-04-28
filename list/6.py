"""Write a Python program to get a list, sorted in increasing order by the last
 element in each tuple from a given list of non-empty tuples. """

Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sorted(Sample_List, key=lambda x: x[-1]))
