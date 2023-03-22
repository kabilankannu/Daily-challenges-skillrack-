a,b=map(int,input().split())
m=[]
p=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    if(i==0 or i==a-1):
        p.append(l[0])
        p.append(l[-1])
print(*p,sep=" ")
