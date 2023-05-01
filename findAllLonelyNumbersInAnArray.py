# Find All Lonely Numbers in the Array
# You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

# Return all lonely numbers in nums. You may return the answer in any order.

from collections import Counter
def findLonely(nums):
    frequency = Counter(nums)
    lonely = []
    for num in nums:
        if frequency[num] == 1 and num - 1 not in frequency and num + 1 not in frequency:
            lonely.append(num)
    return lonely
print(findLonely(nums = [1,3,5,3]))