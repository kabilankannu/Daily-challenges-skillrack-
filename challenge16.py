a,b=map(int, input().split())
fl = 0
for i in range(a):
    s = input().strip()
    if len(s) != b:
        print(s)
        fl = 1
if fl == 0:
    print(-1)
