s=int(input())
uni=s%10
sr=str(s)
sre=sr.replace(str(uni),"")
if sre=="":
    print("-1")
else:
    print(int(sre))
