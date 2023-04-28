num=int(input())
m=[]
for i in range(num):
    l=list(map(int,input().split()))
    m.append(l)
lf=[]
rd=[]
if num%2==0:
 for i in range(num):
     for j in range(num):
         if i==j:
             lf.append(m[i][j])
     rd.append(m[i][num-1-i])
else:
    for i in range(num):
        for j in range(num):
            if i==j:
                lf.append(m[i][j])
        if i!=num-1-i:
            rd.append(m[i][num-1-i])
lfs=sum(lf)
rds=sum(rd)
res=lfs+rds
print(res)
for i in range(num):
    for j in range(num):
        if i==j:
            m[i][j]=res
    m[i][num-1-i]=res
for i in range(num):
    for j in range(num):
        print(m[i][j],end=" ")
    print()
