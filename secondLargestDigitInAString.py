# Second Largest Digit in a String
# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
# An alphanumeric string is a string consisting of lowercase English letters and digits.

def secondHighest (s) :
    numbers = set()
    for ch in s :
        if ch not in numbers and ch >= "0" and ch <= "9":
            numbers.add(ch)
    if len(numbers) <= 1 :
        return -1
    return int(sorted(numbers)[-2])
print(secondHighest(s = "dfa12321afd"))