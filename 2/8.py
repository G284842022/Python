def mult_mat(A, B):
    rows_A, cols_A, rows_B, cols_B = len( A ), len( A[0] ), len( B ), len( B[0] )
    if  cols_A != rows_B:
        return "積が計算できません."

    mult_m = [[0 for _ in range( cols_B )] for _ in range( rows_A )]

    for i in range( rows_A ):
        for j in range( cols_B ):
            for k in range( cols_A ):
                mult_m[ i ][ j ] += A[ i ][ k ] * B[ k ][ j ]

    return mult_m


a=[
    [3, 7, 3], 
    [7, 4, 9]
]

b= [
    [7, 2], 
    [9, 1], 
    [0, 8]
]

print(mult_mat(a, b))