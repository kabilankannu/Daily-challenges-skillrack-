n=int(input())
lt=list(map(int,input().split()))
x,y=map(int,input().split())
print(lt.count(x))
print(lt.count(y))
if lt.count(x)>=lt.count(y):
    print("yes")
else:
    print("no")
