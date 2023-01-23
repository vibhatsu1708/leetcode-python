# Transpose Matrix
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

def transpose (matrix) :
    result = [[0]*len(matrix) for i in range (len(matrix[0]))]
    for i in range (len(matrix)) :
        for j in range (len(matrix[0])) :
            result[j][i] = matrix[i][j]
    return result
        
print(transpose(matrix = [[1,2,3],[4,5,6]]))