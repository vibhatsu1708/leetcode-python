# Sort the People
# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

def sortPeople (names, heights) :
    for i in range (len(heights)) :
        for j in range (i+1, len(heights)) :
            if heights[i] < heights[j] :
                temp = heights[i]
                heights[i] = heights[j]
                heights[j] = temp
                
                tempName = names[i]
                names[i] = names[j]
                names[j] = tempName
    return names
print(sortPeople(names=["Alice","Bob","Bob"], heights=[155,185,150]))