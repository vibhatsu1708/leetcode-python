# Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones (jewels, stones) :
    count = 0
    for s in stones :
        for j in jewels :
            if j == s :
                count += 1
    return count
print(numJewelsInStones(jewels="z", stones="ZZ"))