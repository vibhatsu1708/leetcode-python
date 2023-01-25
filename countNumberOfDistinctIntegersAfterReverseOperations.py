# Count Number of Distinct Integers After Reverse Operations
# You are given an array nums consisting of positive integers.
# You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.
# Return the number of distinct integers in the final array.

def countDistinctIntegers (nums) :
    reverseNums = []
    for num in nums :
        reversedNum = str(num)[::-1]
        reverseNums.append(int(reversedNum))
    for num in reverseNums :
        nums.append(num)
    return len(set(nums))
print(countDistinctIntegers(nums = [1,13,10,12,31]))