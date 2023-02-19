# Merge Similar Items
# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:
# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.
# Note: ret should be returned in ascending order by value.

def mergeSimilarItems (items1, items2) :
    # idValues = {}
    # for id, value in items1 :
    #     idValues[id] = idValues.get(id, 0) + value
    # for id, value in items2 :
    #     idValues[id] = idValues.get(id, 0) + value
    # sortedValues = [[id, value] for id, value in idValues.items()]
    # return sorted(sortedValues)
    items1, items2 = sorted(items1), sorted(items2)
    left, right = 0, 0
    result = []
    while (left < len(items1) or right < len(items2)) :
        if (right == len(items2) or (left < len(items1) and items1[left][0] < items2[right][0])) :
            result.append(items1[left])
            left += 1
        elif (left == len(items1) or (right < len(items2) and items1[left][0] > items2[right][0])) :
            result.append(items2[right])
            right += 1
        else :
            result.append([items1[left][0], items1[left][1] + items2[right][1]])
            left += 1
            right += 1
    return result
print(mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))