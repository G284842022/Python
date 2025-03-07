def remove_zero(l):
    a = [[j for j in i if j != 0] for i in l]
    return a


l = [[1, 0, 2, 3], [0, 2, 0, 4], [0, 0, 1, 5]]
print(remove_zero(l))