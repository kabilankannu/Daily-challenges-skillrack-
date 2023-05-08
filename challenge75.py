x,y=map(int,input().split())
count=0

while(x>0):
    if y > x:
        break
    if x%y==0:
        x=x//y
        count+=1
    else:
        count+=x%y
        x-=x%y
print(count+x)
