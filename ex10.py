k, l = map(int, input().split())

data = {}

for i in range(k):
    key, value = input().split(':')
    data.setdefault(value.lstrip(), key)

line = input()

answer = ''

s = ''
for i in line:
    s += i
    if s in data:
        answer += data[s]
        s = ''

print(answer)