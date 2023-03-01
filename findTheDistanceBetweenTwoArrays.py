# Find the Distance Value Between Two Arrays
# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

def findTheDistanceValue (arr1, arr2, d) :
    finalCount = 0
    for i in range (len(arr1)) :
        count = True
        for j in range (len(arr2)) :
            if abs(arr1[i] - arr2[j]) <= d :
                count = False
                break
        if count :
            finalCount += 1
    return finalCount
print(findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))