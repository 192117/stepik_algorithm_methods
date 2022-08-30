n = int(input())


data = {}

for i in range(n):
    text = input().split()
    if text[0] == 'add':
        data[text[1]] = text[2]
    elif text[0] == 'del':
        try:
            del data[text[1]]
        except KeyError:
            pass
    else:
        print(data.get(text[1], 'not found'))
