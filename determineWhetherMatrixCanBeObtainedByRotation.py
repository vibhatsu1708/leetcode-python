# Determine Whether Matrix Can Be Obtained By Rotation
# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

def findRotation (mat, target) :
    if mat == target :
        return True
    def rotateMat (mat) :
        for i in range (len(mat)) :
            for j in range (i+1, len(mat)) :
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range (len(mat)) :
            start = 0
            end = len(mat[0])-1
            while (start < end) :
                mat[i][start], mat[i][end] = mat[i][end], mat[i][start]
                start += 1
                end -= 1
    rotations = 3
    while (rotations > 0) :
        rotateMat (mat)
        rotations -= 1
        if mat == target :
            return True
        else :
            continue
    return False 
print(findRotation(mat = [[0,0,0],[0,0,1],[0,0,1]], target = [[0,0,0],[0,0,1],[0,0,1]]))