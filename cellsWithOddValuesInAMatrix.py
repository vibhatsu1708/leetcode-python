# Cells with Odd Values in a Matrix
# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

# For each location indices[i], do both of the following:

# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

def oddCells(m, n, indices):
    matrix = [[0] * n for _ in range(m)]
    # increment all the row and column elements
    for index in indices:
        rowIndex, colIndex = index[0], index[1]
        for i in range(n):
            matrix[rowIndex][i] += 1
        for j in range(m):
            matrix[j][colIndex] += 1
    # count the number of odd elements
    oddCount = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]%2 != 0:
                oddCount += 1
    return oddCount
print(oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))