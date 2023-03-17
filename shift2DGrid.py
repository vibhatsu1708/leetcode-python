# Shift 2D Grid
# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
# In one shift operation:
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

def shiftGrid (grid, k) :
    numbers = []
    m = len(grid)
    n = len(grid[0])
    for i in range (m) :
        for j in range (n) :
            numbers.append(grid[i][j])
    k = k%len(numbers)
    newNumbers = numbers[len(numbers)-k:] + numbers[0:len(numbers)-k]
    result = []
    for i in range (0, m*n, n) :
        result.append(newNumbers[i:i+n])
    return result
print(shiftGrid(grid = [[1],[2],[3],[4],[7],[6],[5]], k = 23))