# Maximum Count of Positive Integer and Negative Integer
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

def maximumCount (nums) :
    poscount, negcount = 0, 0
    for i in nums :
        if i > 0 :
            poscount += 1
        if i < 0 :
            negcount += 1
    return max(poscount, negcount)

print(maximumCount(nums=[5,20,66,1314]))