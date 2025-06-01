class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        twoPerson = [] 
        # At i = remaining candies, how many ways can the 2 people divide them?
        for numCandy in range(n + 1):
            maxEach = min(numCandy, limit)
            minEach = max(0, numCandy - maxEach)
            numWays = max(0, maxEach - minEach + 1)
            twoPerson.append(numWays)

        total = 0
        for candyForThird in range(0, min(n, limit) + 1):
            extraCandy = n - candyForThird
            total += twoPerson[extraCandy]
        
        return total



        