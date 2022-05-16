n = int(input())


def calc(n):
    if n == 1:
        print(0)
        print(1)
    if n == 2:
        print(1)
        print(*[1, 2], end=' ')
    if n == 3:
        print(1)
        print(*[1, 3], end=' ')
    if n > 3:
        D = [float('inf') for i in range(n + 1)]
        D[1] = 0
        D[2] = 1
        D[3] = 1
        for i in range(4, n+1):
            if i % 2 == 0 and i % 3 == 0:
                D[i] = 1 + min(D[i-1], D[i//2], D[i//3])
            elif i % 2 == 0:
                D[i] = 1 + min(D[i - 1], D[i // 2])
            elif i % 3 == 0:
                D[i] = 1 + min(D[i - 1], D[i // 3])
            else:
                D[i] = 1 + D[i - 1]
        print(D[n])

calc(n)