def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

n = int(input())
arr = list(map(int, input().split()))
print("Original:", arr)
swap(arr)
print("Result:", arr)




