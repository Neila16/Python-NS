import math

def t_area(x, y, z):
    p = (x + y + z)/2
    return math.sqrt(p*(p - x)*(p - y)*(p - z))

a, b, c, d, diagonal = map(float, input().split())

area = t_area(a, b, diagonal) + t_area(c, d, diagonal)
print("area of a convex quadrilateral :", area)
