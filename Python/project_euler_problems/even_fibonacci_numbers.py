def main():
    upper_bound = 4 * 10**6
    result = 0
    prev = 1
    current = 2

    while current < upper_bound:
        temp = current
        current += prev
        prev = temp
        if prev % 2 == 0:
            result += prev

    print('Sum of even Fibonacci numbers up to %d: %d' % (upper_bound, result))


if __name__ == '__main__':
    main()
