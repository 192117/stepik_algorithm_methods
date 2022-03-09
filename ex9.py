s = input()

data = list()
for i in set(s):
    data.append([i, s.count(i)])

data.sort(key=lambda x:(x[1], x[0]))

new_data = []
tranclate = {}

if len(data) == 1:
    tranclate.setdefault(data[0][0], '0')
else:
    while len(data) != 1:
        data.sort(key=lambda x:(x[1], x[0]))
        i = data.pop(0)
        j = data.pop(0)
        data.append([i[0]+j[0], i[1]+j[1]])
        data.sort(key=lambda x:(x[1], x[0]))
        new_data.append([i[0], '0'])
        new_data.append([j[0], '1'])

    new_data.sort(key=lambda x:len(x[0]), reverse=True)

    for i in set(s):
        for j in range(len(new_data)):
            if i in new_data[j][0]:
                if tranclate.get(i) is None:
                    tranclate.setdefault(i, new_data[j][1])
                else:
                    tranclate[i] += new_data[j][1]

answer = ''
for i in s:
    answer += tranclate[i]

print('{} {}'.format(len(tranclate), len(answer)))
for i in tranclate:
    print('{}: {}'.format(i, tranclate[i]))
print(answer)