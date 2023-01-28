# Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def validMountainArray (arr) :
    if len(arr) < 3 :
        return False
    peakElement, peakElementIndex = arr[0], 0
    for i in range (len(arr)) :
        if arr[i] > peakElement :
            peakElement = arr[i]
            peakElementIndex = i
    if peakElementIndex == len(arr)-1 or peakElementIndex == 0 :
        return False
    for i in range (0, peakElementIndex) :
        if arr[i] >= arr[i+1] :
            return False
    for i in range (peakElementIndex, len(arr)-1) :
        if arr[i] <= arr[i+1] :
            return False
    return True
print(validMountainArray(arr=[3,5,5]))