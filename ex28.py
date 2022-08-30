import heapq

n, m = map(int, input().split())

A = [(0, i) for i in range(n)]

heapq.heapify(A)

t = list(map(int, input().split()))

for i in t:
    current = heapq.heappop(A)
    print(current[1], current[0], sep=' ')
    heapq.heappush(A, (current[0]+i, current[1]))