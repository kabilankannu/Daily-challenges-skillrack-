l=list(map(int,input().split()))
diff=-99
for i in range(len(l)):
    for j in range(i+1,len(l)):
        dif=l[i]-l[j]
        # print(dif,end=" ")
        if abs(dif)>diff:
            diff=abs(dif)
            x=l[i]
            y=l[j]
print(x,y)
