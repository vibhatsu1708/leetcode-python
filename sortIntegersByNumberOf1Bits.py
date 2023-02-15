# Sort Integers by The Number of 1 Bits
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# Return the array after sorting it.

def sortByBits (arr) :
    def count1Bits (num) :
        count = 0
        while (num > 0) :
            count += num%2
            num //= 2
        return count
    return sorted(arr, key = lambda x : (count1Bits(x), x))
print(sortByBits(arr = [0,1,2,3,4,5,6,7,8]))
    
    