n = int(input())


def calc(n):
    D = [float('inf') for i in range(n+1)]
    parents = [None for i in range(n+1)]
    D[0] = -1
    for i in range(1, n+1):
        current_parent = i - 1
        current_d = D[current_parent] + 1

        if i % 2 == 0:
            parent = i // 2
            d = D[parent] + 1
            if d < current_d:
                current_d, current_parent = d, parent

        if i % 3 == 0:
            parent = i // 3
            d = D[parent] + 1
            if d < current_d:
                current_d, current_parent = d, parent

        D[i] = current_d
        parents[i] = current_parent

    answer = []
    k = n
    while k > 0:
        answer.append(k)
        k = parents[k]

    print(D[n])
    print(*answer[::-1], end=' ')

calc(n)