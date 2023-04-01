# Form Smallest Number From Two Digit Arrays
# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.

def minNumber(nums1, nums2) :
    # check if a number exists in both the arrays.
    similarNums = []
    for num in nums1:
        if num in nums2:
            similarNums.append(num)
    if similarNums:
        return min(similarNums)
    
    firstNum = min(nums1)
    secondNum = min(nums2)
    if firstNum > secondNum:
        firstNum, secondNum = secondNum, firstNum
    result = firstNum*10 + secondNum
    return result
print(minNumber(nums1 = [6,4,3,7,2,1,8,5], nums2 = [6,8,5,3,1,7,4,2]))