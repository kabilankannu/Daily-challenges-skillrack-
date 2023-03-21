s = input().strip()
p=s[::-1]
l=[]
j=0
for i in range(len(p)):
    j=i+1
    x=int(p[i])*(10**i)
    l.append(x)
print(l[::-1])
