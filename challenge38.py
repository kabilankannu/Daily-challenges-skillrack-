num=int(input())
ra=num//100
num1=num%100
# print(ra)
rev=0
if num%2==1:
    while(num1>0):
      s=num1%10
      rev=rev*10+s
      num1=num1//10
    print(ra*100+rev)
else:
    print(ra)
