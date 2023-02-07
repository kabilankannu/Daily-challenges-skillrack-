y1,y2 = map(int,input().split())
l=[]
for input_year in range(y1,y2+1):
  if (( input_year%400 == 0)or (( input_year%4 == 0 ) and ( input_year%100 != 0))):
      l.append(input_year)
  else:
     pass
if len(l)!=0:
      print(*l,sep=" ")
else:
      print("-1")
