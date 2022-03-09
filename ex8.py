n = int(input())
i = 1

numbers = []
while n > 2 * i:
    n -= i
    numbers.append(i)
    i += 1

numbers.append(n)
print(i)
print(*numbers, sep=' ')