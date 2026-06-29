a,b=map(int, input().split())
result=0

if a<=b:
    for i in range(a,b+1,1):
        if i%5==0:
            result=result+i

else:
    for i in range(b,a+1,1):
        if i%5==0:
            result=result+i

print(result)