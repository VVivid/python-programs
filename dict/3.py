"""Write a Python program to concatenate following dictionaries to create a new one."""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

for item in dic2, dic3:
    dic1.update(item)
print(dic1)
