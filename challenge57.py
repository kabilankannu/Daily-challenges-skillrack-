import re
s=input().strip()
res=re.split(r'(\d+)',s)
if len(res)==1:
   newres = res
else:
    newres = res[:-1]

flag=0
for i in newres:
    if len(i)==5:
        flag+=1
    else:
        flag=0
        break
if flag==0:
    print("no")
else:
    print("yes")
