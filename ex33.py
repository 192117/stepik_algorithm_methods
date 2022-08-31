pattern = input()
text = input()


def hashe(string, x, m):
    result, last = 0, 0
    for i in range(m):
        last = abs(ord(string[i]) * x ** i)
        result += last
    return [result, last, string]

def rabinkarp(string, pattern):
    result = []
    n, m = len(string), len(pattern)
    hpattern = hashe(pattern, 1, m)
    hs = 0
    for i in range(0, n-m+1):
        if hs == 0:
            hs = hashe(string[n-m-i:n-i], 1, m)
            if hpattern[0] % n == hs[0] % n:
                if pattern == hs[2]:
                    result.append(n-m-i)
        else:
            hs[0] = hs[0] - hs[1] + abs(ord(string[n-m-i]))
            hs[1] = abs(ord(string[n-i-1]) * 1 ** 3)
            hs[2] = string[n-m-i:n-i]
            if hpattern[0] % n == hs[0] % n:
                if pattern == hs[2]:
                    result.append(n-m-i)
    return result

print(*rabinkarp(text, pattern)[::-1])

# pattern = input()
# text = input()
#
# def rabinkarp(string, pattern):
#     result = []
#     n, m = len(string), len(pattern)
#     hpattern = hash(pattern)
#     for i in range(n-m+1):
#         hs = hash(string[i:i+m])
#         if hs == hpattern:
#             if string[i:i+m] == pattern:
#                 result.append(i)
#     return result
#
# print(*rabinkarp(text, pattern))