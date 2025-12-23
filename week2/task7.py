items = input().split()

count = {}

for item in items:
    count[item] = count.get(item, 0) + 1

print("Purchase frequency:")
for k, v in count.items():
    print(k + ":", v)

most = max(count, key=count.get)
print("Most popular item:", most)

print("Purchased once:", end=" ")
for k, v in count.items():
    if v == 1:
        print(k, end=" ")
print()

print("Sorted by frequency:")
for k in sorted(count, key=count.get, reverse=True):
    print(k, count[k])