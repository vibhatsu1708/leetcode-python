# Separate the Digits in an Array
# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
# To separate the digits of an integer is to get all the digits it has in the same order.
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

def separateDigits (nums) :
    sepNums = []
    for i in range (len(nums)) :
        temp = str(nums[i])
        for j in range (len(temp)) :
            sepNums.append(int(temp[j]))
    return sepNums
print(separateDigits(nums = [72,1,3,9,5]))