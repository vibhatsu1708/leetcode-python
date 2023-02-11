# Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

def uniqueOccurrences (arr) :
    count = {}
    for num in arr :
        if num not in count :
            count[num] = 1
        else :
            count[num] += 1
    countNums = sorted([count[value] for i, value in enumerate(count)])
    for i in range (len(countNums)-1) :
        if countNums[i] == countNums[i+1] :
            return False
    return True        
print(uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))