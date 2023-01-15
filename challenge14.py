num=int(input())
lt=list(map(int,input().split()))
k=int(input())
for i in lt:
  if i>=k:
    print(abs(k-i),end=" ")
  else:
    print(k+i,end=" ")
