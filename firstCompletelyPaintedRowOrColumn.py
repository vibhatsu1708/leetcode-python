# First Completely Painted Row or Column
# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

# Return the smallest index i at which either a row or a column will be completely painted in mat.

def firstCompleteIndex(arr, mat):
    positions = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            positions[mat[i][j]] = (i, j)
    rowCount, columnCount = [0]*len(mat), [0]*len(mat[0])
    for i in range(len(arr)):
        row, column = positions[arr[i]]
        rowCount[row] += 1
        columnCount[column] += 1
        if rowCount[row] == len(mat) or columnCount[column] == len(mat[0]):
            return i
    return -1
print(firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))