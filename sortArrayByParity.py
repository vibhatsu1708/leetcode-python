# Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

def sortArrayByParity (nums) :
    evenNums, oddNums = [], []
    for i in range (len(nums)) :
        if nums[i]%2 == 0 :
            evenNums.append(nums[i])
        if nums[i]%2 != 0 :
            oddNums.append(nums[i])
    return evenNums + oddNums
print(sortArrayByParity(nums = [3,1,2,4]))