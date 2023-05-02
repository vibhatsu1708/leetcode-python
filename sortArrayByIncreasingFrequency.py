# Sort Array by Increasing Frequency
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
def frequencySort (nums) :
    count = {}
    for num in nums :
        count[num] = count.get(num, 0) + 1
    return sorted(nums, key=lambda x:(count[x], -x))
print(frequencySort(nums = [2,3,1,3,2]))