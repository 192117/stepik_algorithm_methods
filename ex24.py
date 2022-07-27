size, n = map(int, input().split())

stack = []

def buffer(arrival, duration, size, stack):
    if len(stack) == 0:
        stack.append((arrival, arrival+duration))
    elif len(stack) < size:
        stack.append((arrival, arrival+duration))
    else:
        current = stack.pop(0)
        while current[1] < arrival:
             print(current[0])
             stack.append((arrival, arrival+duration))
             current = stack.pop(0)
        else:
            print(-1)


for i in range(n):
    arrival, duration = map(int, input().split())
    buffer(arrival, duration, size, stack)
