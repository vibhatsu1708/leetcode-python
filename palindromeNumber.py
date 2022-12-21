# Given an integer x, return true if x is a palindrome, and false otherwise.
def palindromeNumber (x) :
    temp = str(x)
    return (temp == temp[::-1])

print(palindromeNumber(-121))x