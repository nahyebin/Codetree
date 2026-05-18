a1,a2=input().split()
a2=int(a2)
b1,b2=input().split()
b2=int(b2)
c1,c2=input().split()
c2=int(c2)

a=0
b=0
c=0
d=0

if a1=="Y" :
    if a2>=37:
        a=a+1
    else:
        c=c+1
if b1=="N":
    if b2>=37:
        b=b+1
    else:
        d=d+1
if b1=="Y" :
    if b2>=37:
        a=a+1
    else:
        c=c+1
if b1=="N":
    if b2>=37:
        b=b+1
    else:
        d=d+1
if c1=="Y" :
    if c2>=37:
        a=a+1
    else:
        c=c+1
if c1=="N":
    if c2>=37:
        b=b+1
    else:
        d=d+1
if a>=2:
    print("E")
else:
    print("N")