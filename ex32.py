m = int(input())
n = int(input())

data = {}

delit = 1000000007

for i in range(n):
    text = input().split()
    k = 0
    for j in range(len(text[1])):
        k += ord(text[1][j]) * 263 ** j
    k = (k % delit) % 5
    if text[0] == 'add':
        if k not in data:
            data.setdefault(k, [])
            data[k].insert(0, text[1])
        else:
            if text[1] not in data[k]:
                data[k].insert(0, text[1])
    elif text[0] == 'del':
        try:
            data[k].remove(text[1])
        except KeyError:
            pass
    elif text[0] == 'check':
        if int(text[1]) not in data:
            print()
        else:
            print(*data[int(text[1])])
    elif text[0] == 'find':
        try:
            if text[1] in data[k]:
                print('yes')
            else:
                print('no')
        except KeyError:
            print('no')