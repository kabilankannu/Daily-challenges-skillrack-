num=int(input())
lt=list(map(int,input().split()))
rest=int(input())
rev = lt[::-1]
l = []
r = []
if rest!= 1:
    for i in range(rest):
          l.append(lt[i])
          r.append(rev[i])
else:
    l.append(lt[0])
    r.append(lt[-1])
r = r[::-1]
print(l)
print(r)
if l==r:
    print("yes")
else:
    print("no")
