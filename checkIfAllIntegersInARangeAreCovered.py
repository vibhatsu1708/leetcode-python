# Check if All the Integers in a Range Are Covered
# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.
# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

def isCovered (ranges, left, right) :
    rangesSet = []
    for rangeArr in ranges :
        for i in range (rangeArr[0], rangeArr[1]+1) :
            rangesSet.append(i)
    numsArr = []
    for num in range (left, right+1) :
        numsArr.append(num)
    for num in numsArr :
        if num not in rangesSet :
            return False
    return True
print(isCovered(ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5))