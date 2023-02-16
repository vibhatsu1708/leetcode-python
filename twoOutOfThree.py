# Two Out of Three
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

def twoOutOfThree (nums1, nums2, nums3) :
    nums1Set, nums2Set, nums3Set = set(nums1), set(nums2), set(nums3)
    result = set()
    for num in nums1 :
        if num in nums2Set or num in nums3Set :
            result.add(num)
    for num in nums2Set :
        if num in nums1Set or num in nums3Set :
            result.add(num)
    return list(result)
print(twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))