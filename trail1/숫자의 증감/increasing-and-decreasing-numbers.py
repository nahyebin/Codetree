c, n = input().split()
n = int(n)

if c == "A" :
    # for i in range (n):
    #     i=i+1
    #     print(i, end=" ")
    for i in range (1, n+1):
        print(i, end=" ")
else:
    # for i in range (n):
    #     print(n, end=" ")
    #     n=n-1
    for i in range(n,0,-1):
        print(i, end=" ")
