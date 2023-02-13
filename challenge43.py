s=input().strip()
sr=s[::-1]
lk=[]
for i in range(len(s)):
    if s[i] not in "AEIOUaeiou":
        lk.append(i)
for i in lk:
    x=sr.replace(sr[i]," ",1)
    sr=x
o=""
for k in x:
    if k.isalpha():
        o=o+k
print(o)
