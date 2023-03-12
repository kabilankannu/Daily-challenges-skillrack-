s=input().strip()
lt=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if s=='a':
    s='b'
elif s=='e':
    s='f'
elif s == 'i':
    s = 'j'
elif s == 'o':
    s = 'p'
elif s=='u':
    s='v'
for i in range(len(lt)):
       if lt[i]==s:
           for k in range(i,i+21):
               print(lt[k%21],end="")
