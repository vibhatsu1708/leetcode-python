# Check If N and Its Double Exist
# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

def checkIfExist (arr) :
    for i in range (0, len(arr)) :
        for j in range (0, len(arr)) :
            if ((i != j) and (i >= 0 and j < len(arr)) and (arr[i] == 2*arr[j])) :
                return True
    return False
print(checkIfExist(arr = [3,1,7,11]))