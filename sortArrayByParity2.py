# Sort Array By Parity II
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

def sortArrayByParityII (nums) :
    evenPointer, oddPointer = 0, 1
    while (True) :
        while (evenPointer < len(nums) and nums[evenPointer]%2 == 0) :
            evenPointer += 2
        while (oddPointer < len(nums) and nums[oddPointer]%2 != 0) :
            oddPointer += 2
        while (evenPointer < len(nums) and oddPointer < len(nums)) :
            nums[evenPointer], nums[oddPointer] = nums[oddPointer], nums[evenPointer]
        else :
            break
    return nums
print(sortArrayByParityII(nums = [4,2,5,7]))