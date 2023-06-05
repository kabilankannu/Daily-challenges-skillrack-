num=int(input())
sr=list(str(num))
if len(sr)%2==0:
    for i in range(0,len(sr),2):
        x=int(sr[i])*int(sr[i+1])
        print(x,end=" ")
else:
    for i in range(0,len(sr),2):
        if i==len(sr)-1:
            x=int(sr[i])*1
            print(x, end=" ")
        else:
            x = int(sr[i]) * int(sr[i + 1])
            print(x, end=" ")

