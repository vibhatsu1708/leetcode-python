# Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords (s) :
    # in this program, i'll be trying out list comprehension to avoid creating multiple variables to store values.
    return " ".join(w[::-1] for w in s.split(" "))
            
print(reverseWords(s="God Ding"))