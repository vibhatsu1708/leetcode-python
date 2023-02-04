# Number of Different Integers in a String
# You are given a string word that consists of digits and lowercase English letters.
# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
# Return the number of different integers after performing the replacement operations on word.
# Two integers are considered different if their decimal representations without any leading zeros are different.

def numDifferentIntegers (word) :
    wordNumbers = ""
    for ch in word :
        if ch >= "0" and ch <= "9" :
            wordNumbers += ch
        else :
            wordNumbers += " "
    numbers = wordNumbers.split()
    numbers = list(set([int(num) for num in numbers]))
    return len(numbers)
print(numDifferentIntegers(word = "a1b01c001"))