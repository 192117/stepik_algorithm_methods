import bisect

n, m = map(int, input().split())

start_point = []
end_point = []

for i in range(n):
    x, y = map(int, input().split())
    start_point.append(x)
    end_point.append(y)


def partition(points, low, high):
    m = (low+high) // 2
    i = low
    j = high
    while True:
        while points[i] < points[m]:
            i += 1
        while points[j] > points[m]:
            j -= 1
        if i >= j:
            return j
        points[i], points[j] = points[j], points[i]


def quick_sort(points, low, high):
    while low < high:
        index = partition(points, low, high)
        quick_sort(points, low, index)
        low = index + 1


def get_count_equal_or_less(element, points):
    s = 0
    m = len(points) // 2
    if len(points) > 2:
        if element >= points[m]:
            s += get_count_equal_or_less(element, points[m:])
        else:
            s += get_count_equal_or_less(element, points[:m])
    elif len(points) == 2:
        if element >= points[1]:
            s += 2
        elif element >= points[0]:
            s += 1
    else:
        if element >= points[0]:
            s += 1
    return s


def get_count_less(element, points):
    s = 0
    m = len(points) // 2
    if len(points) > 2:
        if element > points[m]:
            s += get_count_equal_or_less(element, points[m:])
        else:
            s += get_count_equal_or_less(element, points[:m])
    elif len(points) == 2:
        if element > points[1]:
            s += 2
        elif element > points[0]:
            s += 1
    else:
        if element > points[0]:
            s += 1
    return s


quick_sort(start_point, 0, len(start_point)-1)
quick_sort(end_point, 0, len(end_point)-1)

# for element in input().split():
#     print(get_count_equal_or_less(int(element), start_point) - get_count_less(int(element), end_point), end=' ')

for element in input().split():
    print(bisect.bisect_right(start_point, int(element)) - bisect.bisect_left(end_point, int(element)), end=' ')


# def quick_sort(points, low, high):
#     m = (low+high) // 2
#     i = low
#     j = high
#     while i <= j:
#         while points[i] < points[m]:
#             i += 1
#         while points[j] > points[m]:
#             j -= 1
#         if i <= j:
#             points[i], points[j] = points[j], points[i]
#             i += 1
#             j -= 1
#     if low < j:
#         quick_sort(points, low, j)
#     if i < high:
#         quick_sort(points, i, high)