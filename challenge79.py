a,st=map(str,input().strip().split())
K=0
for i in range(int(a)):
    for j in range(i+1):
        print(st[K%len(st)],end="")
        K+=1
    print()
