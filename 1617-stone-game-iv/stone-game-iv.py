class Solution:
    # I don't get it, isnt this just a super basic DP?
    # Solve for just (remaining pile)->true if winner.
    # Each step only has to consider sqaure values, so < 350

    def winnerSquareGame(self, n: int) -> bool:
        squares = []
        for i in range(1, int(n**0.5) + 1):
            squares.append(int(i**2))
        
        winnerGivenRemaining = [False, True] # [0] is a loser, [1] takes the last one
        for remaining in range(2, n+1):
            canWin = False
            for chosenAmount in squares:
                if chosenAmount > remaining:
                    break
                
                if not winnerGivenRemaining[remaining - chosenAmount]:
                    canWin = True
                    break
            
            winnerGivenRemaining.append(canWin)

        return winnerGivenRemaining[n]