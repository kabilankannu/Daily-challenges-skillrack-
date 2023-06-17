sr=input().strip()
s=list(sr)
for i in range(len(s)):
    if s[i] not in "aeiouAEIOU":
        for j in range(i+1,len(s)-1):
            if s[j] in "AEIOUaeiou":
                s[i]=s[j]
                break
p=""
for i in range(len(s)):
    if s[i]  in "AEOIUaeiou":
        p+=s[i]

if p=="":
    print("-1")
else:
    print(p)

