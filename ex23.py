n = input()
parents = list(map(int, input().split()))


def height(r):
    h = 1
    for i in parents:
        if parents[i] == r:
            h = max(h, 1+height(i))
    return h


print(height(parents.index(-1)))