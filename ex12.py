n, *A = map(int, input().split())

k, *B = map(int, input().split())

result = []
def search(data, value):
    l, r = 0, n-1
    while l <= r:
        m = (l+r)//2
        if data[m] == value:
            result.append(m + 1)
            break
        elif data[m] > value:
            r = m - 1
        else:
            l = m + 1
    else:
        result.append(-1)

for i in B:
    search(A, i)

print(*result, sep=' ')