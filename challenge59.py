s=input().strip()
lt=['a','e','i','o','u']
c=-1
for i in range(len(s)):
    if s[i] in "aeiou":
        c+=1
        print(lt[c%5],end="")
    else:
        print(s[i],end="")

