# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# O(n*k)
# n = int(input())
#
# def max_in_window(arr, size):
#     if size == 1:
#         yield from arr
#         return
#     else:
#         for i in range(len(arr) - size + 1):
#             yield max(arr[i: i + size])
#
# print(*max_in_window(list(int(i) for i in input().split()), int(input())))

# O(n*log k)
# def findKMaxElement(arr, k, n):
#
#     queue = []
#     res = []
#     i = 0
#     while (i < k):
#         queue.append(arr[i])
#         i += 1
#     queue.sort(reverse=True)
#     res.append(queue[0])
#     queue.remove(arr[0])
#     while (i < n):
#         queue.append(arr[i])
#         queue.sort(reverse=True)
#         res.append(queue[0])
#         queue.remove(arr[i - k + 1])
#         i += 1
#     return res
#
# arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
# k, n = 4, len(arr)
# res = findKMaxElement(arr, k, n)
# for x in res:
#     print(x, end=" ")
#
# O(n*)
# from collections import deque
#
# def max_windows(array, n, m):
#
#     Q = deque()
#
#     for i in range(m):
#         while Q and array[i] >= array[Q[-1]]:
#             Q.pop()
#         Q.append(i)
#
#     for i in range(m, n):
#         print(array[Q[0]], end=' ')
#         while Q and Q[0] <= i-m:
#             Q.popleft()
#         while Q and array[i] >= array[Q[-1]]:
#             Q.pop()
#         Q.append(i)
#     print(array[Q[0]], end=' ')
#
# n = int(input())
#
# A = list(int(i) for i in input().split())
#
# m = int(input())
#
# max_windows(A, n, m)

