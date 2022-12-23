# Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr (address) :
    newAddress = ""
    for ch in range (len(address)) :
        if address[ch] == '.' :
            newAddress += "[.]"
        else :
            newAddress += address[ch]
    return newAddress
print(defangIPaddr(address="255.100.50.0"))