while True:
    n, m = map(int, input().split())

    # Terminate if any number is <= 0
    if n <= 0 or m <= 0:
        break

    # Determine the range in increasing order
    start = min(n, m)
    end = max(n, m)

    numbers = list(range(start, end + 1))
    total = sum(numbers)

    # Print numbers followed by sum
    print(*numbers, "sum =", total)
