# Sender With Largest Word Count
# You have a chat log of n messages. You are given two string arrays messages and
# senders where messages[i] is a message sent by senders[i].
#
# A message is list of words that are separated by a single space with no leading or trailing spaces. The word count
# of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.
#
# Return the sender with the largest word count. If there is more than one sender with the largest word count,
# return the one with the lexicographically largest name.
#
# Note:
#
# Uppercase letters come before lowercase letters in lexicographical order.
# "Alice" and "alice" are distinct.

def largestWordCount(messages, senders):
    count = {}
    newMessages = []
    for message in messages:
        newMessages.append(len(message.split(" ")))
    for i in range(len(senders)):
        if senders[i] not in count:
            count[senders[i]] = newMessages[i]
        else:
            count[senders[i]] += newMessages[i]
    largestValue, largestName = 0, ""
    for name, value in count.items():
        if value > largestValue:
            largestValue = value
            largestName = name
        elif value == largestValue and name > largestName:
            largestName = name
    return largestName


print(largestWordCount(messages=["tP x M VC h lmD", "D X XF w V", "sh m Pgl", "pN pa", "C SL m G Pn v", "K z UL B W ee",
                                 "Yf yo n V U Za f np", "j J sk f qr e v t", "L Q cJ c J Z jp E", "Be a aO",
                                 "nI c Gb k Y C QS N", "Yi Bts", "gp No g s VR", "py A S sNf", "ZS H Bi De dj dsh",
                                 "ep MA KI Q Ou"],
                       senders=["OXlq", "IFGaW", "XQPeWJRszU", "Gb", "HArIr", "Gb", "FnZd", "FnZd", "HArIr", "OXlq",
                                "IFGaW", "XQPeWJRszU", "EMoUs", "Gb", "EMoUs", "EMoUs"]))
