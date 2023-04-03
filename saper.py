row = []
matrix = []
result_matrix = []
result_row =[]

while row != ['end']:
    row = [str(i) for i in input().split()]
    matrix.append(row)

matrix.remove(['end'])
row_1 = len(matrix)
col_1 = len(matrix[0])

for i in range(row_1):
    for j in range(col_1):
        result_row.append(int(matrix[(i - 1) % row_1][j])
                            + int(matrix[(i + 1) % row_1][j])
                            + int(matrix[i][(j - 1) % col_1])
                            + int(matrix[i][(j + 1) % col_1])
                             )
    result_matrix.append(result_row)  
    result_row = []

for i in range(row_1):    
    print(*result_matrix[i])
