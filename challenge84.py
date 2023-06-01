a,b=map(str,input().split())
s=""
for i in range(0,len(a),int(b)):
    s+=a[i:i+int(b)][::-1]

print(s)
