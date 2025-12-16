N = int(input())

if N >= 1:
    sum = sum(range(1, N + 1))
else:
    sum = sum(range(N, 1 + 1))

print(sum)
