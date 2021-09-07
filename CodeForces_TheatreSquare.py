import math
n, m, a = [int(n) for n in input().split()]
y = math.ceil(n/a)
x = math.ceil(m/a)
print (x*y)

