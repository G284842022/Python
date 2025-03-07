def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(fact(3))
print(fact(4))
print(fact(5))


def perm1(n, k):
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result


def perm2(n, k):
    return fact(n) / fact(n-k)


def print_perm(n):
    for i in range(1, n+1):
        print(f"【perm1({n}, {i})の結果】：{perm1(n, i)} 【perm2({n}, {i})の結果】：{perm2(n, i)}")

print_perm(4)