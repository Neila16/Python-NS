def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input())
a = list(map(int, input().split()))

print("Original:", a)
swap(a)
print("Result:", a)
