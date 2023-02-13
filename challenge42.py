s=input().strip()
sr=s[::-1]
# print(sr)
for i in range(len(sr)):
    if sr[i] in "AEIOUaeiou":
        new=sr[i+1:len(sr)]
        os=sr[0:i+1]
        print(new+os[::-1])
        break
