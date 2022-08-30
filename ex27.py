n = int(input())
A = list(map(int, input().split()))

result = []

def sift_down(i):
    min_index = i
    l = 2*i + 1
    if l<=n-1 and A[l] < A[min_index]:
        min_index = l
    r = 2*i + 2
    if r<=n-1 and A[r] < A[min_index]:
        min_index = r
    if i != min_index:
        A[i], A[min_index] = A[min_index], A[i]
        result.append((i, min_index))
        sift_down(min_index)


def build_heap(A):
    for i in range(n//2, -1, -1):
        sift_down(i)


build_heap(A)

print(len(result))
for i in result:
    print(*i)