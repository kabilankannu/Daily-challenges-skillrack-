n=int(input())
maxx=-9999
res=""
lt=[]
for i in range(n+1):
    x=input()
    lt.append(x)
ma=lt[-1]
print(ma[1:])
c=0
print(lt)
for i in range(len(lt)-1):
    a,b=map(str,lt[i].split("."))
    y=len(a)
    if y>maxx and b==ma[1:] :
        maxx=y
        res=lt[i]
    else:
         c+=1
if(c == n):
    print("FILE NOT FOUND")
else:
    print(res)
