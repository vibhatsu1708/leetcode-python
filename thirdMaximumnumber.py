# Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

def thirdMax (nums) :
    numsSet = list(set(nums))
    numsSet.sort(reverse=True)
    if len(numsSet) >= 3 :
        return numsSet[2]
    else :
        return numsSet[0]
print(thirdMax(nums = [1,2]))