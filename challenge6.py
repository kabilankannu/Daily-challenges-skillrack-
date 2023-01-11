st=input()
length=len(st)
mid=length//2
if(length%2==0):
   s=st[0:mid]
   s1=st[mid:length+1]
else:
    s=st[0:mid]
    s1=st[mid+1:length]
if s==s1:
    print("yes")
else:
    print("no")
