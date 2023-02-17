
s=input().strip()
last=ord(s[-1])
# print(last)
count=0
l=[]
p=[last]
for i in s:
    r=ord(i)
    p.append(r)
    p.sort()
    print(p[0],p[1])
    for j in range(p[0],p[1]):
        if chr(j) not in "AEIOUaeiou":
            print(chr(j),end=" ")
            count+=1
    l.append(count)
    count=0
    p=[last]
print(l)
