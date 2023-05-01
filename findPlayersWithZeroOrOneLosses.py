# Find Players With Zero or One Losses
# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

def findWinners(matches):
    winners, losers = set(), set()
    for winner, loser in matches:
        winners.add(winner)
        losers.add(loser)
    notLost = winners - losers
    losses = {}
    for _, loser in matches:
        losses[loser] = losses.get(loser, 0) + 1
    lostOnce = set(key for key, value in losses.items() if value == 1)
    return [sorted(list(notLost)), sorted(list(lostOnce))]
        
print(findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))