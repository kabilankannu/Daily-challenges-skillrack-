num=input().strip()
lt=list(num)
for i in range(len(lt)):
    if int(lt[i])%2==0:
        lt[i]='1'
    else:
        lt[i]='2'
print(*lt,sep=" ")

