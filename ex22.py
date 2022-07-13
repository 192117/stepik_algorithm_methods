s = input()

def check_order(s):
    stack = []
    for ind, char in enumerate(s, start=1):
        if char in ['(', '{', '[']:
            stack.append((ind, char))
        elif char in [')', '}', ']']:
            if len(stack) == 0:
                return ind
            last = stack.pop()
            if (last[1] == '[' and char != ']') or (last[1] == '(' and char != ')') or (last[1] == '{' and char != '}'):
                return ind
    if len(stack) == 0:
        return 'Success'
    else:
        return stack[0][0]

print(check_order(s))


# test = [
#     '[]',
#     '{}[]',
#     '[()]',
#     '(())',
#     '{[]}()',
#     '{',
#     '{[}',
#     'foo(bar);',
#     'foo(bar[i);',
#     '([](){([])})'
# ]
#
# for i in test:
#     print(i, '------', check_order(i))