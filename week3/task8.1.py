num = int(input())

for i in range(1, num + 1):
    div = True
    for n in str(i):
        if n == '0' or i % int(n) != 0:
            div = False
    if div:
        print(i, end=" ")


