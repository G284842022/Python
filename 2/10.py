def multmult(m, l):
    return [[i*m[j] for i in l[j]] for j in range(len(m))]


m = [3, 1, 5]
l = [[1, 2, 3], [2, 3, 1], [1, 2, 3]]
print(multmult(m, l))
