import math

a,b=map(int, input().split())
cnt=0
sum_result=0
avg_result=0

for i in range(a,b+1,1):
    if ((i%5==0) or (i%7==0)):
        cnt=cnt+1
        sum_result=sum_result+i
        avg_result=sum_result/cnt

print(sum_result,round(avg_result,1))
