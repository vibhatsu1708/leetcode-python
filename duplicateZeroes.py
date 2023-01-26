# Duplicate Zeros
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

def duplicateZeros (arr) :
    i = 0
    while (i < len(arr)) :
        if arr[i] == 0 :
            arr.insert(i, 0)
            i += 2
            arr.pop()
            continue
        i += 1
    return arr    
print(duplicateZeros(arr = [1,0,2,3,0,4,5,0]))