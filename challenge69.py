num=int(input())
l=[]
m=[]
j=1
for i in range(1,num+1):
    for p in range(1,num+1):
        l.append(j)
        j+=1
    if i%2==0:
        m.append(l)
    else:
        m.append(l[::-1])
    l=[]
for i in range(num):
    for j in range(num):
        print(m[i][j],end=" ")
    print()
