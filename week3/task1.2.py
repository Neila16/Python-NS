for i in range(3):
    n = int(input())          
    arr = list(map(int, input().split()))

    s = sum(arr)              
    avg = s / n               

    print("Sum:", s)
    print("Arithmetic mean:", avg)
