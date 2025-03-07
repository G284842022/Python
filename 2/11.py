def trans(l):
    a = [[j for j in range(len(l[0])) if l[i][j] == 1] for i in range(len(l))]
    return a

l = [
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 1]
]

print(trans(l))