num=int(input())
m=[]
for i in range(num):
    r=list(map(int,input().split()))
    m.append(r)
print(m)
summ=0
flag=0
k=0
p=0
for i in range(num):
    p=0
    for j in range(num):
        summ += m[p][k]
        # print(m[p][k],end=" ")
        p+=1
    # print(summ)
    if summ==0:
        flag+=1
    else:
        flag=0
        break
    k+=1
if flag==num:
    print("yes")
else:
    print("no")
