n=int(input())
lt=list(map(int,input().split()))
x=int(input())
maxx=-99999
maxz=-99999
for i in lt:
    y=((i%(10**x))//(10**(x-1)))
    print(y,end=" ")
    if y>maxx:
        maxx=y
        maxz=i
print(maxz)
