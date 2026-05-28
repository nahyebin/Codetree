# n=int(input())
# yyear=0

# for i in range(1, n+1, 1):
#     if i % 4 == 0:
#         yyear=yyear+1
#     elif i % 100 !=0 and i % 400 == 0:
#         yyear=yyear+1

# print(yyear)
# 내가 푼 답

n = int(input())
yyear = 0

for i in range(1, n + 1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        yyear += 1

print(yyear)
        