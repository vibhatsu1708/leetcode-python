# Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

def diagonalSum (mat) :
    sumDiagonal = 0
    for i in range (len(mat)) :
        for j in range (len(mat)) :
            if i == j :
                sumDiagonal += mat[i][j]
            if (i+j) == (len(mat)-1) :
                sumDiagonal += mat[i][j]
    if len(mat)%2 != 0 :
        sumDiagonal -= mat[len(mat)//2][len(mat)//2]
    return sumDiagonal
print(diagonalSum(mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]))