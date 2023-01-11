# GCD AND LCM OF TWO NUMBERS
first=int(input())
second=int(input())
def find_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd
lcm = first * second / find_gcd(first, second)
print(int(lcm))
res=find_gcd(first,second)
print(res)
