# Check if Number Has Equal Digit Count and Digit Value
# You are given a 0-indexed string num of length n consisting of digits.
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

def digitCount (num) :
    for i in range (len(num)) :
        countDigit = num.count(str(i))
        if countDigit == int(num[i]) :
            continue
        else :
            return False
    return True
        
        
print(digitCount(num="1210"))