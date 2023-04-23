# Calculate Delayed Arrival Time
# You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.
# Return the time when the train will arrive at the station.
# Note that the time in this problem is in 24-hours format.

def findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime)% 24
print(findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11))