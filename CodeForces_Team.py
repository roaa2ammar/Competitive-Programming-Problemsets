n = int(input())
c = 0
for i in range(1,n+1):
    p, v, t = [int(p) for p in input().split()]
    if p ==1 and (v ==1 or t ==1):
        c = c + 1
    elif v == 1 and (p == 1 or t ==1):
        c = c + 1
    elif t == 1 and (v == 1 or p ==1):
        c = c + 1
print(c)


