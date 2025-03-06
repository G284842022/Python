def numbers(n):
    for i in range(2, n + 1):

        for j in range(1,i):
            print(j, end="")

        for k in range(i - 2, 0, -1):
            print(k, end="")

        print()

numbers(5)