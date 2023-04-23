# Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

def relativeSortArray(arr1, arr2):
    count = {}
    newArr = []
    for num in arr1:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    for num in arr2:
        newArr.extend([num] * count[num])
        count.pop(num)
    nonIntersecting = []
    for _, value in enumerate(count):
        nonIntersecting.extend([value] * count[value])
    return newArr + sorted(nonIntersecting)
    
print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))