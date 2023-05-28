# Remove Trailing Zeros From a String
# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

def removeTrailingZeros(num):
    end = len(num)
    while (end > 0) and (num[end-1]) == "0":
        end -= 1
    return num[:end]
print(removeTrailingZeros(num = "51230100"))