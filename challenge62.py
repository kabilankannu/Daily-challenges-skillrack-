n=int(input())
s=str(n)
l=[]
p=[]
for i in range(len(s)):
    if i%2==0:
        l.append(s[i])
    else:
        p.append(s[i])
if n%2==0:
    y=""
    for i  in l:
        y+=i
    print(int(y))
else:
    y = ""
    for i in p:
        y += i
    print(int(y))
