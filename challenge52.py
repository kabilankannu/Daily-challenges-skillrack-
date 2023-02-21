num=int(input())
s=input().strip()
for i in s:
  if i.isalpha():
    print(",",end="")
  else:
    print(i,end="")
