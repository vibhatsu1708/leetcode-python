# N-Repeated Element in Size 2N Array
# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

def repeatedNTimes (nums) :
    seen = {}
    for num in nums :
        if num in seen :
            return num
        else :
            seen[num] = 1
print(repeatedNTimes(nums = [1,2,3,3]))