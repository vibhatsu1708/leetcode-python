# Check If All 1's Are at Least Length K Places Away
# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

def kLengthApart (nums, k) :
    lastOne = -1
    for i in range (len(nums)) :
        if nums[i] == 1 :
            if lastOne != -1 and i - lastOne <= k :
                return False
            lastOne = i
    return True
            
print(kLengthApart(nums=[1,0,0,1,0,1], k=2))