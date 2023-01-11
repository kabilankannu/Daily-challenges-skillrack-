n=int(input())
lt=list(map(int,input().split()))
ne=[]
for i in lt[1:(n-2)+1]:
    ne.append(i)
flag=0
for i in ne:
    if i < lt[0] and i > lt[-1]:
        flag=0
    else:
        flag+=1
if flag==len(ne):
    print("yes")
else:
    print("no")
