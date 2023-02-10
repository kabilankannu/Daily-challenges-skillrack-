s=input()
count=0
for i in s:
    if i.isdigit() or i.isalpha():
        pass
    else:
        count+=1
print(count)
