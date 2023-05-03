s=input().strip()
l=len(s)
si=""
if l%2==0:
    nl=(l//2)
else:
    nl=(l//2)+1
for i in s[nl:]:
    if i in "aeiou":
        si+=i
for j in s[:nl+1]:
    if j in "aeiou":
        si+=j
if len(si)==0:
    print(-1)
else:
    print(si)
