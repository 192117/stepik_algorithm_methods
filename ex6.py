n = int(input())

a = []
values = []

for i in range(n):
    l, r = map(int, input().split())
    a.append([l, r])

a.sort(key=lambda x: x[1])

for point in a:
    if len(values) == 0:
        values.append(point[1])
    if point[0] > values[-1]:
        values.append(point[1])


print(len(values))
print(*values, sep=' ')