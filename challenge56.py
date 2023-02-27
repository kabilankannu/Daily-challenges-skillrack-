r,c=map(int,input().split())
m=[]
for i in range(r):
    sr=list(map(int,input().split()))
    x=sum(sr)
    sr.append(x)
    m.append(sr)
for i in range(r):
    for j in range(c+1):
        print(m[i][j],end=" ")
    print()
