# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent (nums, k) :
    count = {}
    for num in nums :
        if num not in count :
            count[num] = 1
        else :
            count[num] += 1
    sortedCount = dict(sorted(count.items(), key = lambda x : x[1], reverse = True))
    answer = [num for num in sortedCount.keys()]
    return answer[:k]
print(topKFrequent(nums = [1], k = 1))