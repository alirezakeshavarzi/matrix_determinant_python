
def matrix_det(mat1, row, col):
    zero_val = 0.0

    for k in range(col):
        for i in range(k, row-1):            
            zero_val = (mat1[i+1][k] / mat1[k][k]) * (-1)
            for j in range(col):
                mat1[i+1][j] += zero_val * mat1[k][j]
    
    det_m=1
    for i in range(row):
        det_m *= mat1[i][i]
    return det_m






