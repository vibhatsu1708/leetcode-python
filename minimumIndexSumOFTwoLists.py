# Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

def findRestaurant (list1, list2) :
    count = {}
    for i in range (len(list1)) :
        for j in range (len(list2)) :
            if list1[i] == list2[j] :
                count[list1[i]] = i + j
    sortedCount = dict(sorted(count.items(), key = lambda x : x[1]))
    result = []
    minCount = min([i for i in sortedCount.values()])
    for index, value in sortedCount.items() :
        if value == minCount :
            result.append(index)
    return result
print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))