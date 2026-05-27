a=0
b=0

for i in range (1,11,1):
    n=int(input())
    if n % 3 == 0:
        a=a+1
    if n % 5 == 0:
        b=b+1

print(a, b)
