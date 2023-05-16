l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(e)>len(o):
    m=e[::-1]
    res=m+o
elif len(e)<len(o):
    m=o[::-1]
    res=m+e
else:
    res=l[::-1]
    
print(*res,sep=" ")
