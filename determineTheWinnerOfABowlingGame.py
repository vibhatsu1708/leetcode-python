# Determine the Winner of a Bowling Game
# You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.

# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

# Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:

# 2xi if the player hit 10 pins in any of the previous two turns.
# Otherwise, It is xi.
# The score of the player is the sum of the values of their n turns.

# Return

# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw.

def isWinner(player1, player2):
    def calculateScore(player):
        score = 0
        for i in range(2, len(player)):
            if player[i-2] == 10 or player[i-1] == 10:
                score += 2*player[i]
            else:
                score += player[i]
        score += player[0]
        if len(player) >= 2 :
            if player[0] == 10:
                score += 2*player[1]
            else:
                score += player[1]
        return score
    
    player1Score, player2Score = calculateScore(player1), calculateScore(player2)
    if player1Score > player2Score: return 1
    if player2Score > player1Score: return 2
    else: return 0
print(isWinner(player1 = [2,3], player2 = [4,1]))