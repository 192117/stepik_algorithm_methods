n = int(input())
a = list(map(int, input().split()))

def stairs_max(a):
    prev2 = 0
    prev1 = a[0]
    for i in range(1, n):
        current = max(prev1+a[i], prev2+a[i])
        prev2 = prev1
        prev1 = current
    return prev1

print(stairs_max(a))