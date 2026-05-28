n = int(input())

bathroom=0
classroom=0
way=0

for i in range(1,n+1,1):
    if i % 12 == 0:
        bathroom=bathroom+1
    elif i % 3 == 0:
        way=way+1
    elif i % 2 == 0:
        classroom=classroom+1

print(classroom, way, bathroom)
        