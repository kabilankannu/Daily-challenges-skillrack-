num,a=map(int,input().split())
s=""
while(num>0):
    d=num%2
    s+=str(d)
    num=num//2
l=a-len(s)
if l>0:
    p='0'*l
    rs=p+s[::-1]
    print(rs)
elif l==0:
    print(s[::-1])
else:
    print("-1")
