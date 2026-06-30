a,b = map(int, input().split())
result=1

for i in range (a,b+1,1):
    result=result*i

print(result)