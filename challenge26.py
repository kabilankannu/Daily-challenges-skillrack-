num=int(input())
lt=list(map(int,input().split()))
l=[]
for i in lt:
  if i %100==10:
    l.append(i)
if len(l)!=0:
  print(*l,sep=" ")
else:
  print(-1)
