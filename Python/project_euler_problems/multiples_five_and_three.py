import sys


def main():

    if len(sys.argv) == 1:
        n = 1000
    else:
        n = sys.argv[1]

    if not isinstance(n, int):
        print('Pass integer as argument.', file=sys.stderr)
        sys.exit(1)
    result = 0

    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            result += i

    print('Sum of multiples of 3 or 5 below %d: %d' % (n, result))


if __name__ == '__main__':
    main()
