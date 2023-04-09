# Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

def findDifference (nums1, nums2) :
    result = [[], []]
    for num in nums1 :
        if num not in nums2 and num not in result[0]:
            result[0].append(num)
    for num in nums2 :
        if num not in nums1 and num not in result[1] :
            result[1].append(num)
    return result
print(findDifference(nums1 = [1,2,3], nums2 = [2,4,4,6]))