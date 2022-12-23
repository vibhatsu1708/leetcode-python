# Shuffle String
# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

def restoreString (s, indices) :
    shuffleString = [""]*len(s)
    for i in range (len(indices)) :
        shuffleString[indices[i]] = s[i]
    shuffleString = "".join(shuffleString)
    return shuffleString
print(restoreString(s="codeleet", indices=[4,5,6,7,0,2,1,3]))