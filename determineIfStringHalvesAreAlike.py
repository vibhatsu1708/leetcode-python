# Determine if String Halves Are Alike
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

def halvesAreAlike (s) :
    a, b = "", ""
    count1, count2 = 0, 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in range (len(s)//2) :
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        alike = True
        if a[i] in vowels :
            count1 += 1
        if b[i] in vowels :
            count2 += 1
    if count1 == count2 :
        return True
    else :
        return False
print(halvesAreAlike(s="book"))