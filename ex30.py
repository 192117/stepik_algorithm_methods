n, e, d = map(int, input().split())

parents = [i for i in range(n)]
ranks = [0 for i in range(n)]

def find(i):
    while i != parents[i]:
        i = parents[i]
    return i

def union(i, j):
    i_id = find(i-1)
    j_id = find(j-1)
    if i_id == j_id:
        return
    if ranks[i_id] > ranks[j_id]:
        parents[j_id] = i_id
    else:
        parents[i_id] = j_id
        if ranks[i_id] == ranks[j_id]:
            ranks[j_id] += 1

for i in range(e):
    i, j = map(int, input().split())
    union(i, j)

flag = 1

for i in range(d):
    i, j = map(int, input().split())
    if find(i-1) == find(j-1):
        flag = 0
        break

print(flag)