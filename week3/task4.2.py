def inside_circle(x, y, xa, yb, R):
    return (x - xa)**2 + (y - yb)**2 < R**2

xc, yc, R = map(float, input("Ente xc yc and R: ").split())

px, py = map(float, input("Enter P coordinates: ").split())
fx, fy = map(float, input("Enter F coordinates: ").split())
lx, ly = map(float, input("Enter L coordinates: ").split())

count = 0
if inside_circle(px, py, xc, yc, R):
    count += 1
if inside_circle(fx, fy, xc, yc, R):
    count += 1
if inside_circle(lx, ly, xc, yc, R):
    count += 1

print("Number of points inside the circle:", count)


