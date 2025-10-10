class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        bestPath = float('-inf')
        for startPoint in range(k):
            curCost = 0
            for magician in range(startPoint, len(energy), k):
                if curCost < 0:
                    curCost = 0 # Reset where we start
                curCost += energy[magician]
            bestPath = max(bestPath, curCost)
        
        return bestPath