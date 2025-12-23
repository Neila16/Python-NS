s = input()
ans = 0

for i in range(len(s) - 4):
    arrows = s[i:i+5]
    if arrows == ">>-->":
        ans += 1
    if arrows == "<--<<":
        ans += 1

print(ans)


