a = input()
b = input()

k = len(b)
bb = b + b
ans = 0

for i in range(len(a) - k + 1):
    if a[i:i+k] in bb:
        ans += 1

print(ans)

