# Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

def findRestaurant(list1, list2):
    count = {}
    for i, item in enumerate(list1) :
        count[item] = i
    minSum = len(list1) + len(list2)
    result = []
    for j, item in enumerate(list2) :
        if item in count :
            indicesSum = j + count[item]
            if indicesSum < minSum :
                minSum = indicesSum
                result = [item]
            elif indicesSum == minSum :
                result.append(item)
    return result
print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))