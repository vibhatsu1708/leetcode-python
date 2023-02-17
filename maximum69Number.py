# Maximum 69 Number
# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

def maximum69Number (num) :
    if "6" not in str(num) :
        return num
    # newNum = [int(digit) for digit in str(num)]
    # for i in range (len(newNum)) :
    #     if newNum[i] == 6 :
    #         newNum[i] = 9
    #         break
    # numInt = 0
    # power = len(newNum)-1
    # for num in newNum :
    #     numInt += num*(10**power)
    #     power -= 1
    # return numInt
    num = str(num)
    power = len(num)-1
    for i in range (len(num)) :
        if num[i] == "6" :
            num = int(num) + 3*(10**power)
            break
        power -= 1
    return int(num)
print(maximum69Number(num = 9996))