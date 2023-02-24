# Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

def singleNonDuplicate (nums) :
    first, second = 0, 1
    while (first < len(nums) and second < len(nums)-1) :
        if nums[first] != nums[second] :
            return nums[first]
        first += 2
        second += 2
    return nums[-1]
print(singleNonDuplicate(nums = [0,0,2,2,3,3,4]))
    