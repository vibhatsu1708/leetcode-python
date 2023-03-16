# Special Positions in a Binary Matrix
# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

def numSpecial (mat) :
    m = len(mat)
    n = len(mat[0])
    count = 0
    rowOnes = [0] * m
    colOnes = [0] * n
    for i in range (m) :
        for j in range (n) :
            if mat[i][j] == 1 :
                rowOnes[i] += 1
                colOnes[j] += 1
    for i in range (m) :
        for j in range (n) :
            if mat[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1 :
                count += 1
    return count
print(numSpecial(mat = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))