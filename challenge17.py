num=int(input())
count=0
lt=list(map(int,input().split()))
for i in lt:
    if i ==(lt[0]+lt[-1]):
        count+=1
print(count)
