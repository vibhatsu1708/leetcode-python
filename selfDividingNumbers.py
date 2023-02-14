# Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

def selfDividingNumbers (left, right) :
    def checkSelfDividing (num) :
        for ch in str(num) :
            if ch == "0" or num%int(ch) != 0 :
                return False
        return True
    trueNums = []
    for num in range (left, right+1) :
        if checkSelfDividing (num) :
            trueNums.append(num)
    return trueNums
print(selfDividingNumbers(left = 1, right = 22))