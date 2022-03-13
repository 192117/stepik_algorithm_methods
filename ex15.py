n = int(input())

A = [[str(i), 0] for i in range(11)]

for key in input().split():
    A[int(key)][1] += 1

for element in A:
    if element[1] != 0:
        print('{} '.format(element[0]) * element[1], end='')
