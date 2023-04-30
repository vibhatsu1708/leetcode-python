# Sort the Matrix Diagonally
# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
def diagonalSort(mat):
    rows, cols = len(mat), len(mat[0])
    diagonals = {}
    for i in range(rows):
        for j in range(cols):
            diagonal = i-j
            if diagonal not in diagonals:
                diagonals[diagonal] = []
            diagonals[diagonal].append(mat[i][j])
    for diagonal in diagonals:
        diagonals[diagonal].sort()
    for i in range(rows):
        for j in range(cols):
            diagonal = i-j
            mat[i][j] = diagonals[diagonal].pop(0)
    return mat
print(diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))