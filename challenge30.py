ch=input()
lt=ord(ch)
vow="AEIOUaeiou"
for i in range(lt+1,123):
  if chr(i) not in vow:
    print(chr(i))
    break
