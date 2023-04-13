# Number of Distinct Averages
# You are given a 0-indexed integer array nums of even length.
# As long as nums is not empty, you must repetitively:
# Find the minimum number in nums and remove it.
# Find the maximum number in nums and remove it.
# Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.
# For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
# Return the number of distinct averages calculated using the above process.
# Note that when there is a tie for a minimum or maximum number, any can be removed.

def distinctAverages(nums):
    nums.sort()
    first, second = 0, len(nums) - 1
    result = set()
    while first <= second:
        average = (nums[first] + nums[second]) / 2
        if average not in result:
            result.add(average)
        first += 1
        second -= 1
    return nums, result


print(distinctAverages(nums=[9, 5, 7, 8, 7, 9, 8, 2, 0, 7]))
