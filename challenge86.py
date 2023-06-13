a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(str,input().split()))
    m.append(l)
for i in range(a):
    for j in range(b):
        m[i][j]=int(m[i][j][::-1])
for j in range(b):
    for i in range(a):
        for k in range(i+1,a):
            if m[i][j]>m[k][j]:
                m[i][j],m[k][j]= m[k][j],m[i][j]
for i in range(a):
    for j in range(b):
        print(m[i][j],end=" ")
    print()
