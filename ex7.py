n, W = map(int, input().split())

items = []

for i in range(n):
    c, w = map(float, input().split())
    items.append([c, w])

items.sort(key=lambda x: float(x[0]/x[1]), reverse=True)

cost = float(0)
new_w = float(0)
W = float(W)

# print(items)

for i in items:
    if cost == 0:
        if i[1] >= W:
            cost += float(i[0]/i[1]) * W
            new_w = W
            break
        else:
            cost += i[0]
            new_w += i[1]
    else:
        if W - new_w >= i[1]:
            cost += i[0]
            new_w += i[1]
            if new_w == W:
                break
        else:
            cost += float(i[0]/i[1]) * (W - new_w)
            new_w = W
            break

print('{0:.3f}'.format(cost))
