def sieve_of_eratosthenes(n):
    prime_list = [ True for _ in range(n + 1) ]

    for i in range(2, int(n ** 0.5) + 1):
        if prime_list[ i ]:
            for j in range(i * i, n + 1, i):
                prime_list[ j ] = False

    return [ i for i in range(2, n + 1) if prime_list[ i ] ]


print(sieve_of_eratosthenes(120))