# size, n = map(int, input().split())
#
# stack = []
#
# def buffer(packages, size, stack):
#     start_time = 0
#     end_time = 0
#     for arrival, duration in packages:
#         if len(stack) == 0:
#             start_time = arrival
#             end_time = start_time + duration
#             stack.append((start_time, end_time))
#             print(start_time)
#         elif len(stack) < size:
#             if end_time <= arrival:
#                 start_time = arrival
#                 end_time = start_time + duration
#                 stack.append((start_time, end_time))
#                 print(start_time)
#             else:
#                 start_time = end_time
#                 end_time = start_time + duration
#                 stack.append((start_time, end_time))
#                 print(start_time)
#         else:
#             current = stack[0]
#             while current[1] <= arrival:
#                 stack.pop(0)
#                 if len(stack) != 0:
#                     current = stack[0]
#                     start_time, end_time = stack[-1][0], stack[-1][1]
#                 else:
#                     break
#             if len(stack) < size:
#                 if end_time <= arrival:
#                     start_time = arrival
#                     end_time = start_time + duration
#                     stack.append((start_time, end_time))
#                     print(start_time)
#                 else:
#                     start_time = end_time
#                     end_time = start_time + duration
#                     stack.append((start_time, end_time))
#                     print(start_time)
#             else:
#                 print(-1)
#
#
#
# packages = []
#
# for i in range(n):
#     arrival, duration = map(int, input().split())
#     packages.append((arrival, duration))
#
#
# buffer(packages, size, stack)

# Самый элегантный код из решения.
# from collections import deque
#
# packages = []
#
# size, n = map(int, input().split())
#
# for i in range(n):
#     arrival, duration = map(int, input().split())
#     packages.append((arrival, duration))
#
# times = deque()
# for a, d in packages:
#     while times and times[0] <= a:
#             times.popleft()
#     if len(times) < size:
#         if times:
#             a = max(a, times[-1])
#         print(a)
#         times.append(a+d)
#     else:
#         print(-1)