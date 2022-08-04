size, n = map(int, input().split())

stack = []

def buffer(packages, size, stack):
    time = 0
    process_time = 0
    for arrival, duration in packages:
        if len(stack) == 0:
            stack.append((arrival, duration, arrival))
            print(stack[-1][2])
            time = arrival
            process_time = duration
        elif len(stack) < size:
            if arrival >= time + process_time:
                stack.append((arrival, duration, arrival))
                print(stack[-1][2])
                time = arrival
                process_time = duration
            else:
                stack.append((arrival, duration, arrival+process_time))
                time = arrival+process_time
                process_time = duration
                print(stack[-1][2])
        else:
            if arrival >= time + process_time:
                procces = stack[0]
                while procces[0] + procces[1] <= arrival:
                    stack.pop(0)
                    if len(stack) != 0:
                        procces = stack[0]
                    else:
                        break
                stack.append((arrival, duration, arrival))
                print(stack[-1][2])
                time = arrival
                process_time = duration
            else:
                print(-1)


packages = []

for i in range(n):
    arrival, duration = map(int, input().split())
    packages.append((arrival, duration))


buffer(packages, size, stack)

