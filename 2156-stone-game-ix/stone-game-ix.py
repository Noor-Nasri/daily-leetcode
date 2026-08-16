class Solution:
    # For alice to win, all remaining stones must make the sum of removed stones divisible by 3
    # We can also reduce this question down to 3 counts, based on (v % 3).
    # So then DP: (isAlice, curRemainder, num0, num1, num2):
    # How large is the space of (num0, num1, num2), when they add up to n?
    # Every permutation of (0->n/3, 0->n/3, 0->n/3) exists so this wont work. 

    # There needs to be some sort of trick for alice.
    # Alice needs to reduce counts to n1 or n2, with the remainder being the other.
    # After the first turn, its always safe to just take 0.

    # So alice gets to choose n1 or n2. Then n0 is just a buffer until the pattern is forced!
    # For example, if alice takes n2, then bob must take n2. Now remainder is 1.
    # Then alice must take n1 -> remainder is 2. Then bob must take n2 -> remainder is 1.

    # SO: ALICE gets to skim off TWO n1s and start the count at n2, or skim TWO n2s and start at n1.
    # Whoever is forced to break the chain loses. n0 is free buffer both players take.

    def doesAliceWin(self, buffer, counts):
        # Alice forces bob to start alternating counts[0], counts[1], counts[0], ...
        # Alice wins if bob is forced to break the pattern. Buffers are free 
        maxTurns = sum(counts) + buffer
        numValidTurns = min(counts)*2 + buffer
        if counts[0] > counts[1]: # Can keep the pattern going one last time
            numValidTurns += 1
            
        return (numValidTurns % 2 == 0) and numValidTurns < maxTurns 


    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0, 0, 0]
        for val in stones:
            counts[val % 3] += 1
        
        if counts[1] >= 1 and self.doesAliceWin(counts[0], [counts[1] - 1, counts[2]]):
            return True
        elif counts[2] >= 1 and self.doesAliceWin(counts[0], [counts[2] - 1, counts[1]]):
            return True
            
        return False