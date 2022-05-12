n = int(input())
A = list(map(int, input().split()))

def gis(A):
    pos = [-1] * (len(A)+1)
    prev = [None] * (len(A)+1)
    F = [float('-inf')] * (len(A)+2)
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
        prev[i] = pos[right-1]
    k = -1
    for i in range(len(F)-1, -1, -1):
        if F[i] != float('-inf'):
            k = i
            break
    print(k)
    answer = []
    for i in range(len(prev)-1, -1, -1):
        if prev[i] is None:
            break
        if prev[i][0] == k:
            answer.append(prev[i][1]+1)
            k -= 1
    for i in range(len(answer)-1, -1, -1):
        print(answer[i], end=' ')


gis(A)
