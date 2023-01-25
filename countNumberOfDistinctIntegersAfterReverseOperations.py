# Count Number of Distinct Integers After Reverse Operations
# You are given an array nums consisting of positive integers.
# You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.
# Return the number of distinct integers in the final array.

def countDistinctIntegers (nums) :
    reverseNums = []
    for num in nums :
        reversedNum = 0
        temp = num
        while (temp > 0) :
            remainder = temp % 10
            reversedNum = reversedNum*10 + remainder
            temp //= 10
        reverseNums.append(reversedNum)
    for num in reverseNums :
        nums.append(num)
    return len(set(nums))
print(countDistinctIntegers(nums = [2,2,2]))