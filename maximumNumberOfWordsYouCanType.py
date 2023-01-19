# Maximum Number of Words You Can Type
# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

def canBeTypedWords (text, brokenLetters) :
    splitText = text.split(" ")
    count = len(splitText)
    for word in splitText :
        for letter in brokenLetters :
            if letter in word :
                count -= 1
                break
    return count
print(canBeTypedWords(text="leet code", brokenLetters="e"))