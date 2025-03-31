class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # [1, 5, |6,| 7, 8, 2]
        cutValues = sorted([
            weights[i] + weights[i+1] for i in range(len(weights) - 1)
        ], reverse = True)

        total_min = weights[0] + weights[-1]
        total_max = weights[0] + weights[-1]
        for i in range(k-1):
            total_max += cutValues[i]
            total_min += cutValues[len(cutValues) - 1 - i]
        
        return total_max - total_min
