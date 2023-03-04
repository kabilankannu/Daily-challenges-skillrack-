flag=1
summ=0
while flag:
  x,y=map(int,input().split())
  summ+=x+y
  if x!=y:
    flag=0
print(summ)
  
