n=int(input())
lt=list(map(int,input().split()))
num=int(input())
if lt.count(num)==num:
    print("YES")
else:
    print("NO")
