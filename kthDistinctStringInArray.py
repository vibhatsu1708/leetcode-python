# Kth Distinct String in an Array
# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.

def kthDistinct (arr, k) :
    count, newarr = {}, []
    for i in arr :
        if i in count :
            count[i] += 1
        else :
            count[i] = 1
    for i, key in enumerate(count) :
        if count[key] == 1 :
            newarr.append(key)
    if k > len(newarr) :
        return ""
    if k <= len(newarr) :
        return newarr[k-1]
    
print(kthDistinct(arr=["aaa","aa","a"], k=1))