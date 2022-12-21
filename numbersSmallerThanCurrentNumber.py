# How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

def smallerNumbersThanCurrent (nums) :
    result = []
    for num in nums :
        count = 0
        for i in nums :
            if i < num :
                count += 1
        result.append(count)
    return result
        
print(smallerNumbersThanCurrent([7,7,7,7]))
        