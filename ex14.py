import bisect

n, m = map(int, input().split())

start_point = []
end_point = []

for i in range(n):
    x, y = map(int, input().split())
    start_point.append(x)
    end_point.append(y)


def quick_sort(points, low, high):
    if low >= high:
        return

    i, j = low, high
    m = points[(low + high) // 2]

    while i <= j:
        while points[i] < m: i += 1
        while points[j] > m: j -= 1
        if i <= j:
            points[i], points[j] = points[j], points[i]
            i, j = i + 1, j - 1
    quick_sort(points, low, j)
    quick_sort(points, i, high)


quick_sort(start_point, 0, len(start_point)-1)
quick_sort(end_point, 0, len(end_point)-1)


for element in input().split():
    print(bisect.bisect_right(start_point, int(element)) - bisect.bisect_left(end_point, int(element)), end=' ')

