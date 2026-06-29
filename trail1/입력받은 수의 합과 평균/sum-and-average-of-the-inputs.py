import math

n=int(input())
sum_result=0
avg_result=0


nums=[int(input()) for _ in range (n)]

for i in range(0,n,1):
    sum_result=sum_result+nums[i]
    avg_result=sum_result/n

print(sum_result, end=" ")
print(round(avg_result,1))