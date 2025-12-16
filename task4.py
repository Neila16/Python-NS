N = int(input())

if N >= 1:
    result = sum(range(1, N + 1))
else:
    result = sum(range(N, 1 + 1))

print(result)
