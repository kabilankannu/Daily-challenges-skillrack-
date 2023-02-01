a,b=map(str,input().split())
a.lower()
b.lower()
a1=ord(a)
b1=ord(b)
count=0
for i in range(a1,b1+1):
    if chr(i) not in "AEIOUaeiou":
        print(chr(i))
        count+=1
print(count)
