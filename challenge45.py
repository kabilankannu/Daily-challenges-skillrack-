a,b=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
main=a1+a2
main.sort(reverse=True)
arr1=[]
arr2=[]
for i in range(a):
    arr1.append(main[i])
for j in range(a,len(main)):
    arr2.append(main[j])
print("Array1:",end=" ")
print(*arr1,sep=" ")
print("Array1:",end=" ")
print(*arr2,sep=" ")
