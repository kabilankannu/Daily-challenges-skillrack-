num=input().strip()
s=""
for i in num:
    if int(i)%2==0:
        s+=str(int(i)+1)
    else:
        s+=str(int(i)-1)
print(int(s))

