# Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic (s, t) :
    sMap, tMap = {}, {}
    for i in range (len(s)) :
        sCh, tCh = s[i], t[i]
        if (sCh in sMap and sMap[sCh] != tCh) or (tCh in tMap and tMap[tCh] != sCh):
            return False
        sMap[sCh] = tCh
        tMap[tCh] = sCh
    return True
print(isIsomorphic(s = "paper", t = "title"))