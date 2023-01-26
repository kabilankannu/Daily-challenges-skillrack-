num, n = map(int, input().split())
word = str(num)
rec = word[::-1]
n=n-1
print(int(word[n])*int(rec[n]))
