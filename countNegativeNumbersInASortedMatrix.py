# Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
def countNegatives(grid):
    rows = len(grid)
    columns = len(grid[0])
    i = rows - 1
    j = 0
    count = 0
    while (i >= 0 and j < columns) :
        if grid[i][j] < 0 :
            count += (columns - j)
            i -= 1
        else :
            j += 1
    return count
print(countNegatives(grid = [[4,3,2,-1],
                             [3,2,1,-1],
                             [1,1,-1,-2],
                             [-1,-1,-2,-3]]))
