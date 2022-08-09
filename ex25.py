n = int(input())

def stack_max(values):
    maximum = []
    stack = []
    prev = 0
    for operation in values:
        if len(operation) == 2:
            stack.append(int(operation[1]))
            maximum.append(max(prev, int(operation[1])))
            prev = maximum[-1]
        else:
            if operation[0] == 'pop':
                stack.pop(-1)
                maximum.pop(-1)
                prev = maximum[-1]
            elif operation[0] == 'max':
                if len(maximum) == 0:
                    print(0)
                else:
                    print(maximum[-1])

values = []

for i in range(n):
    values.append(input().split())

stack_max(values)