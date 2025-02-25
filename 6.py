def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n%2 == 0:
        return False
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True


def print_primes(n):
    for i in range(1, n):
        if is_prime(i):
            print(i)

print_primes(20)