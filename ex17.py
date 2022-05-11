n = int(input())
A = list(map(int, input().split()))

def gis(A):
    pos = [-1] * (len(A)+1)
    F = [float('-inf')] * (len(A)+1)
    F[0] = float('inf')
    for i in range(len(A)):
        left = 0
        right = len(A)
        while right - left > 1:
            middle = (left + right) // 2
            if F[middle] >= A[i]:
                left = middle
            else:
                right = middle
        F[right] = A[i]
        pos[right] = i
    print(F)
    print(pos)
    k = -1
    for i in range(len(F)-1,-1, -1):
        if F[i] != float('-inf'):
            k = i
            break
    print(k)
    answer = [i+1,]
    for i in range(k-1, -1, -1):
        if A[i] >= A[i+1]:
            answer.append(i+1)
    print(*answer[::-1], end=' ')


gis(A)