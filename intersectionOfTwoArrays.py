# Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
def intersection (nums1, nums2) :
    intersectionArray = []
    for i in range (len(nums1)) :
        for j in range (len(nums2)) :
            if (nums1[i] == nums2[j]) and (nums1[i] not in intersectionArray) :
                intersectionArray.append(nums1[i])
    return intersectionArray
print(intersection(nums1=[4,9,5], nums2=[9,4,9,8,4]))
        
    