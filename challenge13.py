num=int(input())
lt=list(map(int,input().split()))
new=[]
for i in lt:
    new.append(i)
lt.sort(reverse=True)
if lt==new:
    print("yes")
else:
    print("no")
