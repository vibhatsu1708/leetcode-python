# Number of Arithmetic Triplets
# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

def arithmeticTriplets (nums, diff) :
    # count = 0
    # for i in range (len(nums)) :
    #     for j in range (i+1, len(nums)) :
    #         for k in range (j+1, len(nums)) :
    #             if ((i < j < k) and (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff)) :
    #                 count += 1
    
    tripletNums = set()
    count = 0
    for num in nums :
        if num - diff in tripletNums and num - diff*2 in tripletNums :
            count += 1
        tripletNums.add(num)
    return count
print(arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))