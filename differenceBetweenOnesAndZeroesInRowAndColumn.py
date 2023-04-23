# Difference Between Ones and Zeros in Row and Column
# You are given a 0-indexed m x n binary matrix grid.
# A 0-indexed m x n difference matrix diff is created with the following procedure:
# Let the number of ones in the ith row be onesRowi.
# Let the number of ones in the jth column be onesColj.
# Let the number of zeros in the ith row be zerosRowi.
# Let the number of zeros in the jth column be zerosColj.
# diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
# Return the difference matrix diff.

def onesMinusZeros(grid):
    onesRow, onesCol, zeroesRow, zeroesCol = [0]*len(grid), [0]*len(grid[0]), [0]*len(grid), [0]*len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                onesRow[i] += 1
                onesCol[j] += 1
            else:
                zeroesRow[i] += 1
                zeroesCol[j] += 1
    diff = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            diff[i][j] = onesRow[i] + onesCol[j] - zeroesRow[i] - zeroesCol[j]
    return diff
    
print(onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))