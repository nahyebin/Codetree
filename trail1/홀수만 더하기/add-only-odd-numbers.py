n=int(input())
result=0

for n in range (1,n+1,1):
    a=int(input())
    if ((a % 2 !=0) and (a % 3 == 0)) :
        result=result+a


print(result)