def main():
    prime = 13195  # 600851475143
    save_prime = prime
    factors = []

    done = False

    while not done:
        for i in range(prime+1)[2:]:
            if i % 2 == 0:
                continue
            if not is_prime(i):
                continue
            if not isinstance(prime / i, int):
                continue
            print('Factor found: %d' % i)
            factors.append(i)
            prime /= i
            done = (prime == 1)
            break

    factors.append(prime)
    prime = save_prime
    s = '%d = ' % prime
    for i in factors:
        s += '%d * ' % i

    print(s[:-3])
    print('Largest factor: %d' % factors.sort()[-1])


def is_prime(n):
    for i in range(n)[2:]:
        if isinstance(n / i, int):
            return False
    return True

if __name__ == '__main__':
    main()
