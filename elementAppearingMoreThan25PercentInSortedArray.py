# Element Appearing More Than 25% In Sorted Array
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

def findSpecialInteger (arr) :
    count = {}
    for num in arr :
        if num not in count :
            count[num] = 1
        else :
            count[num] += 1
            
        if (count[num]/len(arr))*100 > 25 :
            return num
print(findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))