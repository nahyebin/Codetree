a,b = map(int, input().split())
c,d = map(int, input().split())

if a>c:
    name="A"
else:
    name="B"

if (a==c and b>d):
    name="A"
else :
    name="B"

print(name)
