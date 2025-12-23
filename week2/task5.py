lt = "ABCEHKMOPTXY"

n = int(input())

for i in range(n):
    s = input()

    if len(s) != 6:
        print("No")
        continue

    if s[0] not in lt:
        print("No")
        continue

    if not s[1].isdigit() or not s[2].isdigit() or not s[3].isdigit():
        print("No")
        continue

    if s[4] not in lt or s[5] not in lt:
        print("No")
        continue

    print("Yes")