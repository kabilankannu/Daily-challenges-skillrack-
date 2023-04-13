num=int(input())
j=1
for i in range(1,num+1):
    print("*"*(num-i),end="")
    for p in range(i):
        print(j,end="")
        j+=1
    print()
#############################
6
*****1
****23
***456
**78910
*1112131415
161718192021
