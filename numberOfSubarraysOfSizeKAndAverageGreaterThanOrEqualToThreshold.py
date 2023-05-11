# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

def numOfSubarrays(arr, k, threshold):
    currentSum = sum(arr[:k-1])
    count = 0
    for i in range(0, len(arr)-k+1):
        currentSum += arr[i+k-1]
        if currentSum/k >= threshold:
            count += 1
        currentSum -= arr[i]
    return count
print(numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))