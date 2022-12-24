# Goal Parser Interpretation
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

def interpret (command) :
    newStr = ""
    for i in range(len(command)) :
        if command[i] == "G" :
            newStr += "G"
        if command[i] == "(" :
            if command[i+1:i+3] == "al" :
                newStr += "al"
            else :
                newStr += "o"
    return newStr
        
print(interpret(command="(al)G(al)()()G"))