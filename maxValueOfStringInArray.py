# Maximum Value of a String in an Array
# The value of an alphanumeric string can be defined as:
# The numeric representation of the string in base 10, if it comprises of digits only.
# The length of the string, otherwise.
# Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

def maximumValue (strs) :
    for i in range (len(strs)) :
        if strs[i].isnumeric() :
            strs[i] = int(strs[i])
        else :
            strs[i] = len(strs[i])
    return max(strs)
    
print(maximumValue(strs=["alic3","bob","3","4","000010"]))