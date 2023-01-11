n = int(input())
rev = 0
org= n
while n > 0:
    rem = n % 10
    rev = rev*10 + rem
    n = n//10
if org>0:
   if org != rev:
       print("no")
   else:
    print("yes")
else:
    print("no")
