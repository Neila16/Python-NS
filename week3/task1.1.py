import math

geo_sh = input()

if geo_sh == "rectangle":
    a, b = map(float, input().split())
    print(a * b)

elif geo_sh == "triangle":
    a, h = map(float, input().split())
    print(a * h / 2)

elif geo_sh == "circle":
    r = float(input())
    print(math.pi * r ** 2)

