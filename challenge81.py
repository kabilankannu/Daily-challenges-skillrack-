num=int(input())
m=[]
p=[]
count1,count2=0,0
for i in range(num):
    l=list(map(str,input().split()))
    for i in l:
        if i in "AEIOUaeiou":
            # print(i,end=" ")
            count1 +=1
    m.append(l)
for i in range(num):
    o=list(map(str,input().split()))
    for i in o:
        if i in "AEIOUaeiou":
            # print(i ,end=" ")
            count2 += 1
    p.append(o)
print(count1,count2)
if count1>count2 or count1==count2:
    for i in range(num):
        for j in range(num):
            print(m[i][j],end=" ")
        print()
else:
   for i in range(num):
        for j in range(num):
            print(p[i][j],end=" ")
        print()
