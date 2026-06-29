a,b = map(int, input().split())
result=0

for i in range(a,b+1,1):
    if (i%6==0) and (i%8!=0):
        result=result+i

print(result)