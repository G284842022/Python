def numbers(n):
    for i in range(2, n+1):
        for j in range(1,i):
            print(j, end="")
        for j in range(i - 2, 0, -1):
            print(j, end="")
        print()

numbers(5)