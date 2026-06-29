import math #반올림 round 사용하기 위한 import문
cnt=0 #평균 구할 때 갯수변수
sum_result=0 #합계변수
avg_result=0 #평균변수

#10개 정수 한줄씩 입력받기 -> 반복변수 사용 안하므로 _사용
tenint = [int(input()) for _ in range(10)] 
for i in range(0,10,1):
    if (tenint[i]>=0) and (tenint[i]<=200):
        cnt=cnt+1
        sum_result=sum_result+tenint[i]
        avg_result=sum_result/cnt

print(sum_result, end=" ") #값 출력 후 공백
print(round(avg_result,1)) #avg_result값을 소수 첫째자리까지 표현
