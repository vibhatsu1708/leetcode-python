# Sum of All Odd Length Subarrays
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

def sumOddLengthSubarrays (arr) :
    subarrays = []
    sum = 0
    for i in range (0, len(arr)+1) :
        for j in range (i+1, len(arr)+1) :
            if len(arr[i:j])%2 != 0 : 
                subarrays.append(arr[i:j])
    for subarray in subarrays :
        for value in subarray :
            sum += value
    return sum
print(sumOddLengthSubarrays(arr=[1,4,2,5,3]))