# Three Consecutive Odds
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

def threeConsecutiveOdds (arr) :
    if len(arr) < 3 :
        return False
    else :
        for i in range (0, len(arr)-2) :
            if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0 :
                return True
        return False
print(threeConsecutiveOdds(arr=[1,2,34,3,4,5,7,23,12]))