x, y, z, t = map(float, input().split())

t_area = z * t / 2
r_area = x * y

area = t_area + r_area

print(area)
