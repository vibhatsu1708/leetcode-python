# Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

def diagonalSum (mat) :
    sum = 0
    rows, cols, length = len(mat), len(mat[0]), len(mat)
    for i in range (rows) :
        for j in range (cols) :
            if i == j :
                sum += mat[i][j]
            if (i+j) == (length-1) :
                sum += mat[i][j]
    if length%2 != 0 :
        return sum - mat[length//2][length//2]
    else :
        return sum
print(diagonalSum(mat=[[5]]))