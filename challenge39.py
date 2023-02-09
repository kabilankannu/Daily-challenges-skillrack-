num=int(input())
lt=list(map(int,input().split()))
l=0
i=0
j=2
while(i != num):
    temp=lt[l]
    lt[l]=lt[j]
    lt[j]=temp
    j+=3
    i+=3
    l+=3
print(lt)
