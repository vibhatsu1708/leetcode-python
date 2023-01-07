# Sum of Unique Elements
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

def sumOfUnique (nums) :
    count = {}
    sum = 0
    for i in range (len(nums)) :
        if nums[i] not in count :
            count[nums[i]] = 1
        else :
            count[nums[i]] += 1
    for i in count.keys() :
        if count[i] == 1 :
            sum += i
    return sum
        
print(sumOfUnique(nums=[1,2,3,2]))