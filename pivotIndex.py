# Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex (nums) :
    sum, leftSum = 0, 0
    for num in nums :
        sum += num
    for i, num in enumerate(nums) :
        if (leftSum == (sum - num - leftSum)) :
            return i
        leftSum += num
    return -1
print(pivotIndex(nums=[1,7,3,6,5,6]))

# working of the program, 
# First loop, calculates the sum of the nums in the nums array.
# second loop, loops through the array, the leftsum variable calculates the sum till the current index.
# the first condition checks if the leftsum == (sum of the nums in the array - the current num[i] - the leftsum).
# If the condition is true, it returns that particular index of the number, where the leftsum if equal to the right sum.
# if the above condition isn't met, it returns -1.
