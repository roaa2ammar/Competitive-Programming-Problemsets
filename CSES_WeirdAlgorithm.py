a = [] 
n = int(input())
a.append(n)

while n != 1 :
    if (n%2) == 0 :
        n = int(n/2)
        
    else:
        n = int(3*n + 1)
    a.append(n)
for item in a:
    print(item,end=" ")

