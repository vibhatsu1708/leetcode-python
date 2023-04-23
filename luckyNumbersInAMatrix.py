# Lucky Numbers in a Matrix
# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

def luckyNumbers(matrix):
    elements = []
    for row in matrix:
        minElement, maxElement = min(row), -1
        colIndex = row.index(minElement)
        for col in matrix:
            if col[colIndex] > maxElement:
                maxElement = col[colIndex]
        if minElement == maxElement:
            elements.append(minElement)
    return elements
print(luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))