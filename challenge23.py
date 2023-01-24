num=int(input())
for i in range(num):
        print(i+1,end=" ")
print()
n=num
for m in range(1,num-1):
    for k in range(n-1):
        if(k+m==num-1):
            print(n-1)
            n-=1
        else:
            print("%",end=" ")
    # print()

for i in range(num):
        print(i+1,end=" ")
