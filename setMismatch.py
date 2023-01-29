# Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

def findErrorNums (nums) :
    originalNums = [i for i in range (1, len(nums)+1)]
    # duplicateNumber = sum(nums) - sum(set(nums))
    # missingNumber = sum(originalNums) - sum(set(nums))
    return [sum(nums) - sum(set(nums)), sum(originalNums) - sum(set(nums))]
print(findErrorNums(nums = [1,2,2,4]))