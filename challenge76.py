n = int(input("Enter a number: "))
for i in range(1, n + 1):
    digits = str(i)
    all_odd = all(int(d) % 2 == 1 for d in digits)
    if all_odd:
        print(i,end=" ")


