# Python program to check for a longest common prefix in Python.
def checkPrefix (strs) :
    result = ""
    for i in range(len(strs[0])) :
        for str in strs :
            if (i == len(str)) or (str[i] != strs[0][i]) :
                return result
        result += strs[0][i]
    return result

print(checkPrefix(strs=["flower","flow","flight"]))