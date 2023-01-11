lt = list(map(str, input().split()))
le = len(lt)
wordlength=len(lt[0])
print(le)
print(wordlength)
lti = []
j = 0
s = ""
s1 = ""
count = 0
m = []
for i in range(le):
    p = 0
    for z in range(wordlength):
      if p <= wordlength and j <= wordlength:
         lti += [lt[p][j]]
      p += 1
    j += 1
    lti = m
    lti.sort()
    for k in lti:
        s = s+k
    for l in m:
        s1 = s1+l
    if s == s1:
        count = 0
    else:
        count += 1
    print(lti)
    lti.clear()
print(count)
