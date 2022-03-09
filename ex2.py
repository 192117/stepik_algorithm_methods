def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = [0, 1]
        for i in range(2, n+1):
            a.append(a[i-1] + a[i-2])
        return a[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()