a,b=map(int,input().split())
lt=list(map(int,input().split()))
l=[]
i=lt[0]
while(len(l)<b):
    if i % a == 0:
        l.append(i)
    i+=1
print(l)
for k in l:
    if k not in lt:
        print(k)
