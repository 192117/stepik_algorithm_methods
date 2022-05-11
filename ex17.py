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
            if F[middle] < A[i]:
                right = middle
            else:
                left = middle
        F[right] = A[i]
        pos[right] = i
    print(F)
    print(pos)


gis(A)