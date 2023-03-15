# Reshape the Matrix
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

def matrixReshape (mat, r, c) :
    rows, cols = len(mat),len(mat[0]) 
    if rows*cols != r*c :
        return mat
    elements = []
    for i in range (rows) :
        for j in range (cols) :
            elements.append(mat[i][j])
    result = []
    for i in range (0, r*c, c) :
        result.append(elements[i:i+c])
    return result
print(matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))