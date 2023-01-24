# How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

def smallerNumbersThanCurrent (nums) :
    smaller = []
    for i in nums :
        count = 0
        for j in nums :
            if i > j :
                count += 1
        smaller.append(count)
    return smaller
print(smallerNumbersThanCurrent(nums=[8,1,2,2,3]))
        