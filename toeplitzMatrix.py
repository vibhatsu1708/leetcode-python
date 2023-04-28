# Toeplitz Matrix
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

def isToeplitzMatrix (matrix) :
    count = {}
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if r-c not in count:
                count[r-c] = value
            elif count[r-c] != value:
                return False
    return True
print(isToeplitzMatrix(matrix = [[1,2],[2,2]]))