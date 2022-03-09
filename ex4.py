def fib_mod(n, m):
    period = [0, 1]
    i = 2
    while i < m * 6:
        period.append((period[i - 1] + period[i - 2]) % m)
        if period[i] == 1 and period[i - 1] == 0:
            break
        i += 1
    return (period[n % (len(period) - 2)])

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))

if __name__ == "__main__":
    main()