n, m = map(int, input().split())

rank = list(map(int, input().split()))
parents = [i for i in range(n)]

max_rank = max(rank)

def find_parent(parents, i):
    if i != parents[i]:
        parents[i] = find_parent(parents, parents[i])
    return parents[i]

def union(destination, source, max_rank):
    destination = find_parent(parents, destination)
    source = find_parent(parents, source)
    if destination != source:
        rank[destination] += rank[source]
        parents[source] = destination
        if rank[destination] > max_rank:
            max_rank = rank[destination]
    return max_rank

for i in range(m):
    destination, source = map(int, input().split())
    max_rank = union(destination-1, source-1, max_rank)
    print(max_rank)