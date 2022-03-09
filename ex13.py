n, A = int(input()), [int(i) for i in input().split()]


def merge(left, right):
    count = 0
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            count += (len(left) - i)
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count


def merge_sort(data):
    if len(data) <= 1:
        return data, 0
    else:
        middle = len(data) // 2
        left, inv_left = merge_sort(data[:middle])
        right, inv_right = merge_sort(data[middle:])
        merge_list, c = merge(left, right)
        c += (inv_left + inv_right)
        return merge_list, c

m, count = merge_sort(A)
print(count)