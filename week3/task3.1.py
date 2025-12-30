import math

def hyp(a, b):
    return math.sqrt(a ** 2 + b ** 2)

a1, b1 = map(float, input().split())
a2, b2 = map(float, input().split())

h1 = hyp(a1, b1)
h2 = hyp(a2, b2)

if h1 > h2:
    print("h1 is bigger")
elif h1 < h2:
    print("h2 is bigger")
else:
    print("Equal")
