class Solution:

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # If we do DP, we can compute probabilities. Def (remK) -> iterate on [1, maxP]
        # Seems like O(k * maxP), although its a bit weird with the shrinking
        # Instead of doing a for loop backwards for sum of probs, we can just maintain product array!
        if n < k:
            return 0
        elif n >= k + maxPts - 1:
            return 1
        
        probabilities = [-1 for i in range(k + maxPts)]
        curAvg = 0
        for excessVal in range(k + maxPts - 1, k - 1, -1):
            probabilities[excessVal] = int(excessVal <= n)
            curAvg += probabilities[excessVal] / maxPts


        for curVal in range(k - 1, -1, -1):
            probabilities[curVal] = curAvg
            curAvg += probabilities[curVal] / maxPts
            curAvg -= probabilities[curVal + maxPts] / maxPts

        
        return probabilities[0]