# Add Binary
# Given two binary strings a and b, return their sum as a binary string.

def addBinary (a, b) :
    def toDecimal (strNum) :
        strNum = int(strNum)
        newNum = 0
        power = 0
        while (strNum > 0) :
            digit = strNum%10
            newNum += digit * 2**power
            strNum //= 10
            power += 1
        return newNum
    
    def toBinary (num) :
        if num == 0 :
            return "0"
        numBinary = ""
        while (num > 0) :
            numBinary = str(num%2) + numBinary
            num //= 2
        return numBinary
    
    aDecimal = toDecimal(a)
    bDecimal = toDecimal(b)
    
    result = aDecimal + bDecimal
    resultBinary = toBinary(result)
    
    return resultBinary
print(addBinary(a = "1010", b = "1011"))
    