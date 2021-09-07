n = int(input())
for i in range(1,n+1):
    w = str(input())
    if len(w) > 10 :
        print (w[0]+str(len(w)-2)+w[len(w)-1])
    else:
        print (w)
