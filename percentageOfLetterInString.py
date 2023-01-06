# Percentage of Letter in String
# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

def percentageLetter (s, letter) :
    count, length = 0, len(s)
    for i in s :
        if i == letter :
            count += 1
    return int((count/length)*100)
print(percentageLetter(s="jjjj", letter="k"))