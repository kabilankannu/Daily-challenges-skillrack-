lt=list(map(int,input().split()))
ltt=[]
targ=int(input())
for i in range(len(lt)):
  for j in range(i+1,len(lt)):
     if(lt[i]+lt[j]==targ):
       ltt.append(i)
       ltt.append(j)
print(ltt)
