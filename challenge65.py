area=0
num=int(input())
for i in range(num):
    lt=list(map(str,input().split()))
    if lt[0]=="square":
        area+=int(lt[1])*int(lt[1])
    if lt[0]=="rectangle":
        area+=int(lt[1])*int(lt[2])
print(area)

