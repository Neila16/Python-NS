def incircle(x, y, xa, yb, R):
    return (x - xa)**2 + (y - yb)**2 < R**2

xa, yb, R = map(float, input().split())
px, py = map(float, input().split())
fx, fy = map(float, input().split())
lx, ly = map(float, input().split())

count = 0
if incircle(px, py, xa, yb, R):
    count += 1
if incircle(fx, fy, xa, yb, R):
    count += 1
if incircle(lx, ly, xa, yb, R):
    count += 1
print("How many points lie inside the circle", count)


