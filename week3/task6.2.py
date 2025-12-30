a, b, c, d, diag = map(float, input().split())
s1 = (a + b + diag) / 2
s2 = (c + d + diag) / 2

import math
area = math.sqrt(s1*(s1-a)*(s1-b)*(s1-diag)) + math.sqrt(s2*(s2-c)*(s2-d)*(s2-diag))
print(area)
