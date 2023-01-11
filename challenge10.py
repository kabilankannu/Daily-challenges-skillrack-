n=int(input())
lt=list(map(int,input().split()))
l=[lt[0]]
for i in range(0,n):
    if(i<=n-2):
     if lt[i]<lt[i+1]:
        l.append(lt[i+1])
print(l)
