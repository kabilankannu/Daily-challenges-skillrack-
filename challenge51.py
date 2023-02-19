s=input().strip()
sr="abcdefghijklmnopqrstuvwxyz"
for i in sr:
  if i not in s:
    print(i,end="")
