# Make Array Zero by Subtracting Equal Amounts
# You are given a non-negative integer array nums. In one operation, you must:
# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

def minimumOperations(nums):
    count = 0
    expectedNums = [0] * len(nums)
    while (nums != expectedNums) :
        count += 1
        minNum = min([num for num in nums if num > 0])
        for i in range (len(nums)) :
            if nums[i] > 0 :
                nums[i] -= minNum
    return count
print(minimumOperations(nums = [1,5,0,3,5]))