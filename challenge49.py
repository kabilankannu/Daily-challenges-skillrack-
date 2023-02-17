s=input().strip()
last=ord(s[-1])
count=0
l=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not in "aeiou":
            count+=1
    l.append(count)
    count=0
print(*l,sep=" ")
