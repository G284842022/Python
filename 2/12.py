def sieve_of_eratosthenes(n):
    l = [True for _ in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if l[i]:
            for j in range(i * i, n + 1, i):
                l[j] = False

    return [i for i in range(2, n + 1) if l[i]]


print(sieve_of_eratosthenes(200))