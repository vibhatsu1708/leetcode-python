# Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

def countNegatives (grid) :
    count = 0
    for i in range (len(grid)) :
        for j in range (len(grid[i])) :
            if grid[i][j] < 0 :
                count += 1
    return count
print(countNegatives(grid = [[3,2],[1,0]]))