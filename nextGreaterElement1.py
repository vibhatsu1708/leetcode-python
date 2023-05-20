# Next Greater Element I
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

def nextGreaterElement(nums1, nums2):
    result = [-1] * len(nums1)
    for i in range(len(nums1)):
        index = nums2.index(nums1[i])
        for j in range(index+1, len(nums2)):
            if nums2[j] > nums1[i]:
                result[i] = nums2[j]
                break
            else:
                continue
    return result
print(nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]))