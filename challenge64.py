a,b=map(int,input().split())
lt=list(map(int,input().split()))
p=[]
for i in lt:
    if not i%b==0:
        p.append(i)
p.sort()
# print(p)
k = 0
for i in range(len(lt)):
    if not lt[i]%b==0:
        # print(k,end=" ")
        lt[i]=p[k]
        k += 1

print(*lt,sep=" ")
