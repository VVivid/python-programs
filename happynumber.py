Number = int(input("Enter a number: "))
result = Number


def Happy(n):
    digit = total = 0
    while n > 0:
        digit = n % 10
        total = total + (digit * digit)
        n = n // 10
    return sum


while result != 1 and result != 4:
    result = Happy(result)
if result == 1:
    print(Number, " is a Happy Number!!!")
else:
    print(Number, " is an Unhappy Number!!!")
