# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes (nums) :
    countOnes, count = [], 0
    for i in range (len(nums)) :
        if nums[i] == 1 :
            count += 1
            countOnes.append(count)
            continue
        count = 0
    if len(countOnes) >= 1 :
        max = countOnes[0]
        for i in range (len(countOnes)) :
            if max < countOnes[i] :
                max = countOnes[i]
    else :
        return count
    return max
print(findMaxConsecutiveOnes(nums = [1,0]))