# Sort Even and Odd Indices Independently
# You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
# Sort the values at odd indices of nums in non-increasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
# Sort the values at even indices of nums in non-decreasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
# Return the array formed after rearranging the values of nums.

def sortEvenOdd (nums) :
    evenArr = [nums[i] for i in range (len(nums)) if i%2 == 0]
    oddArr = [nums[i] for i in range (len(nums)) if i%2 != 0]
    for i in range (len(evenArr)) :
        for j in range (i+1, len(evenArr)) :
            if evenArr[i] > evenArr[j] :
                evenArr[i], evenArr[j] = evenArr[j], evenArr[i]
    for i in range (len(oddArr)) :
        for j in range (i+1, len(oddArr)) :
            if oddArr[i] < oddArr[j] :
                oddArr[i], oddArr[j] = oddArr[j], oddArr[i]
    for i in range (len(nums)) :
        if i%2 == 0 :
            nums[i] = evenArr[i//2]
        if i%2 != 0 :
            nums[i] = oddArr[i//2]
    return nums
print(sortEvenOdd(nums = [4,1,2,3]))