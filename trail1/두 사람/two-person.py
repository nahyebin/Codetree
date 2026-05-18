a1, a2 = input().split()
b1, b2 = input().split()

a1 = int(a1)
b1 = int(b1)

if (a1 >= 19 and a2=="M") or (b1>=19 and b2=="M") :
    print(1)
else :
    print(0)