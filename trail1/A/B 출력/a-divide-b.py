a, b = map(int,input().split())

#정수 부분 출력
print(a//b, end=".")

# 나머지 저장
a = a % b

# 소수점 아래 20자리 출력
for i in range(20):
    a = a * 10
    print(a//b, end="")
    a= a % b

