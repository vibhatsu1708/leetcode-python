# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def check (nums) :
    # counts = {}
    
    # # count the num of occurences of each element.
    # for num in nums :
    #     if num not in counts :
    #         counts[num] = 1
    #     else :
    #         counts[num] += 1
            
    # # return true if an element appears more than once.
    # for count in counts.values() :
    #     if count > 1 :
    #         return True
    # return False

    # duplicates = {}
    # for num in nums :
    #     if num not in duplicates :
    #         duplicates[num] = 1
    #         continue
    #     if num in duplicates :
    #         return True
    # return False
    
    # seen = {}
    # for num in nums :
    #     if num not in seen :
    #         seen[num] = 1
    #     else :
    #         return True
    # return False
    
    hashset = set()
    for num in nums :
        if num in hashset :
            return True
        hashset.add(num)
    return False
print(check (nums=[1,2,3,1]))
            