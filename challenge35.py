a,b=map(int,input().split())
lt=[]
p=[]
for i in  range(1,a+1):
      if i%b==0:
            lt.append(i)
ltr=lt[::-1]
# print(lt)
# print(ltr)
if len(lt)%2 == 0:
      for i in range((len(lt)//2)):
            p.append(lt[i])
            p.append(ltr[i])
else:
      for i in range((len(lt) // 2)+1):
            p.append(lt[i])
            p.append(ltr[i])
      p.pop()
print(*p,sep=" ")
