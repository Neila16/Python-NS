def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

A, B = map(int, input("First fractions:").split())
C, D = map(int, input("Second fractions:").split())

num = A*D - B*C
den = B*D

g = gcd(abs(num), den)

print(num // g, "/", den // g)

