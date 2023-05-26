s1=input().split()
s2=input().split()
l=[]
for i in s1:
    if  i not in s2:
        l.append(i)
if len(l)!=0:
    print(*l,sep=" ")
else:
    print(-1)
