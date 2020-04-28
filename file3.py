def count_para(find):
    File = open("new.txt", "r")
    Count = 0
    Count2 = 0
    for i in File:
        if "\n" in i:
            Count += 1
        for j in i.split():
            if j == find:
                Count2 += 1
    return f"There are {Count} Paragraph in this file\
            \nAnd The frequency of the word {find} is {Count2}"


print(count_para("the"))
