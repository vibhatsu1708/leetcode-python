# Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle (nums, n) :
    result = []
    for i in range(n) :
        result.append(nums[i])
        result.append(nums[i+n])
    return result
print(shuffle(nums=[1,1,2,2], n=2))