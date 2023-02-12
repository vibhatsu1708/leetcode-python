# Find the Array Concatenation Value
# You are given a 0-indexed integer array nums.
# The concatenation of two numbers is the number formed by concatenating their numerals.
# For example, the concatenation of 15, 49 is 1549.
# The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:
# If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
# If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.

def findTheArrayConcVal (nums) :
    left, right = 0, len(nums)-1
    concValues = []
    while (left < right) :
        concValues.append(int(str(nums[left]) + "" + str(nums[right])))
        left += 1
        right -= 1
    if len(nums)%2 != 0 :
        return sum(concValues) + nums[len(nums)//2]
    return sum(concValues)
print(findTheArrayConcVal(nums = [5,14,13,8,12]))