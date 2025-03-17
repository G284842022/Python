def multmult(m, l):
    return [[mult * e for e in innerlist] for mult, innerlist in zip(m, l)]
    # return [[j * m[i] for j in l[i]] for i in range( len(m) )]


m = [3, 1, 5]
l = [[1, 2, 3], [2, 3, 1], [1, 2, 3]]
print(multmult(m, l))
