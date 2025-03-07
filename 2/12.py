def sieve_of_eratosthenes(n):
    l = [True for _ in range(n + 1)]
    current, finish = 2, False

    while finish == False:
        for i in range(current*2, n+1, current):
            l[i] = False
        finish = True
        for i in range(current+1, int(n**0.5) ):
            if l[i] == True:
                current = i
                finish = False
                break
    return [i for i in range(2, n+1) if l[i]]
    

print( sieve_of_eratosthenes(100) )