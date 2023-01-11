st=input().strip()
lt=list(st)
x=lt[0]
y=lt[-1]
i=input()
s=""
if x!=i and y!=i:
    lt.insert(0,i)
    # print(lt)
    lt.append(i)
    # print(lt)
    for k in range(len(lt)):
        s+=lt[k]
    print(s)
elif x!=i:
    lt.insert(0,i)
    for k in range(len(lt)):
        s+=lt[k]
    print(s)
elif y!=i:
    lt.append(i)
    for k in range(len(lt)):
        s+=lt[k]
    print(s)
