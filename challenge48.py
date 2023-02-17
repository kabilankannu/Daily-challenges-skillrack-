num = int(input())
count=0
lt=list(map(int,input().split()))
for i in range(0,len(lt)-1,2):
    print(lt[i],end=" ")
    if lt[i]!=lt[i+1]:
        count+=1
    else:
        count=0
        break
if count==0:
    print("no")
else:
    print("yes")
