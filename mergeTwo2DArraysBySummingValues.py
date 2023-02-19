# Merge Two 2D Arrays by Summing Values
# You are given two 2D integer arrays nums1 and nums2.
# nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
# Only ids that appear in at least one of the two arrays should be included in the resulting array.
# Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.

def mergeArrays (nums1, nums2) :
    left, right = 0, 0
    result = []
    while (left < len(nums1) or right < len(nums2)) :
        if (right == len(nums2)) or (left < len(nums1) and nums1[left][0] < nums2[right][0]) :
            result.append(nums1[left])
            left += 1
        elif (left == len(nums1)) or (right < len(nums2) and nums1[left][0] > nums2[right][0]) :
            result.append(nums2[right])
            right += 1
        else :
            result.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
            left += 1
            right += 1
    return result
print(mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))