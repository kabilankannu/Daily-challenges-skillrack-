a,b,c=map(int,input().split())
lt=list(map(int,input().split()))
l=[]
for i in lt:
    if i>=b and i<=c:
        l.append(i)
print(sum(l))
