# Most Frequent Even Element
# Given an integer array nums, return the most frequent even element.
# If there is a tie, return the smallest one. If there is no such element, return -1.

def mostFrequentEvenElement(nums):
    countEven = {}
    for num in nums :
        if num%2 == 0 :
            if num not in countEven :
                countEven[num] = 1
            else :
                countEven[num] += 1
    if not countEven :
        return -1
    evenNumbers = list(countEven.keys())
    evenNumbers.sort()
    maximumFrequency = max(countEven.values())
    return min([i for i in evenNumbers if countEven[i] == maximumFrequency])
print(mostFrequentEvenElement(nums = [0,1,2,2,4,4,1]))