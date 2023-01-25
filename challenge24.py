num=int(input())
lt=list(map(int,input().split()))
for i in range(0,len(lt),2):
    if lt[i]>lt[i+1]:
        temp=lt[i]
        lt[i]=lt[i+1]
        lt[i+1]=temp
print(*lt,sep=" ")
