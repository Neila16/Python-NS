def all_eq(lst):
    longest = 0

    for s in lst:
        if len(s) > longest:
            longest = len(s)

    result = []

    for s in lst:
        result.append(s + "_" * (longest - len(s)))

    return result


words = input().split()

res = all_eq(words)

for x in res:
    print(x)
