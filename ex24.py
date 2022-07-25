size, n = map(int, input().split())

stack = []

for i in range(n):
    arrival, duration = map(int, input().split())
    if len(stack) == 0:
        stack.append((arrival, duration))
        print(arrival)
    elif len(stack) <= size:
        current = stack.pop

