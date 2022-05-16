W, n = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

def knapsackwithoutrepsbu(W, n, p):
    D = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if p[i-1] > w:
                D[i][w] = D[i-1][w]
            else:
                D[i][w] = max(D[i-1][w], D[i-1][w-p[i-1]] + p[i-1])
    print(D)
    return D[n][W]


print(knapsackwithoutrepsbu(W, n, p))

