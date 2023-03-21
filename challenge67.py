s = input().strip()
p = s[::-1]
x = " "
y= " "
ind = ''
ind1 = ''
for i in range(len(s)):
    if s[i] not in "aeiou" and s[i] not in "AEIOU":
        x = s[i]
        ind=i
        break
for i in range(len(p)):
    if p[i] not in "aeiou" and p[i] not in "AEIOU":
        y = p[i]
        ind1 = i
        break
print(s[:ind]+s[ind:-ind1][::-1]+s[-ind:])
