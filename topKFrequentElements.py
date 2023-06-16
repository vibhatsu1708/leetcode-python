# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent (nums, k) :
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sortedCount = sorted(count.items(), key=lambda x:x[1], reverse=True)
    kFrequent = []
    for i in range(k):
        kFrequent.append(sortedCount[i][0])
    return kFrequent
print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))