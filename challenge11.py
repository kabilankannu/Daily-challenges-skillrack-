num=int(input())
lt=list(map(int,input().split()))
z=[]
n=[]
p=[]
for i in range(num):
    if lt[i]<0:
        n.append(lt[i])
    elif  lt[i]>0:
        p.append(lt[i])
    elif  lt[i]==0:
        z.append(lt[i])
newlist=n[::-1]+z+p[::-1]
print(*newlist,sep=" ")

