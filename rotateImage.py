# Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate (matrix) :
    # find transpose of a matrix.
    for i in range (len(matrix)) :
        for j in range (i+1, len(matrix)) :
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse the rows of each row in the matrix.
    for i in range (len(matrix)) :
        start = 0
        end = len(matrix[0])-1
        while (start < end) :
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1
    return matrix
print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))