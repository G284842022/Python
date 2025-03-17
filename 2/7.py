def trans_mat(M):
    # 転置行列にする配列を初期化. Mが 3 行 2 列の時 [2][3]
    trans_M = [[0 for _ in range(len( M ))] for _ in range(len( M[0] ))]

    # 列 : trans_mの列 Mが 3 行 2 列の時 y = 0 ~ 2
    for y in range(len( M[0] )):
        # 行 : trans_mの行 Mが 3 行 2 列の時 x = 0 ~ 1
        for x in range(len( M )):
            trans_M[y][x] = M[x][y]

    return trans_M


matrix = [
    [7, 9], 
    [2, 7],
    [6, 2]
]
print(trans_mat (matrix))