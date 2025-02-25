def numbers(n):
    for i in range(2, n+1):
        for j in range(1,i):
            print(j, end="")
        for j in range(1,i-1):
            print(i-j-1, end="")
        print()

numbers(5)