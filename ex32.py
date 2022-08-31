m = int(input())
n = int(input())

data = {}

def hash(string, m):
    result = 0
    p = 1000000007
    x = 263
    for i in range(len(string)):
        result += ord(string[i]) * (x ** i)
    result = result % p
    result = result % m
    return result

def operation(text, m):
    if text[0] == 'add':
        k = hash(text[1], m)
        if k not in data:
            data.setdefault(k, [])
            data[k].append(text[1])
        else:
            if text[1] not in data[k]:
                data[k].insert(0, text[1])
    elif text[0] == 'del':
        k = hash(text[1], m)
        try:
            if text[1] in data[k]:
                data[k].remove(text[1])
        except KeyError:
            pass
    elif text[0] == 'find':
        k = hash(text[1], m)
        try:
            if text[1] in data[k]:
                print('yes')
            else:
                print('no')
        except KeyError:
            print('no')
    elif text[0] == 'check':
        try:
            print(*data[int(text[1])])
        except Exception:
            print()

for i in range(n):
    text = input().split()
    operation(text, m)