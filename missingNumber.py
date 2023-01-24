# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber (nums) :
    # nums.append(-1)
    numsNew = []
    length = len(nums)
    for i in range (0, length+1) :
        numsNew.append(i)
    nums.append("")
    for i in range (len(numsNew)) :
        if numsNew[i] not in nums :
            return numsNew[i]
        
print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))