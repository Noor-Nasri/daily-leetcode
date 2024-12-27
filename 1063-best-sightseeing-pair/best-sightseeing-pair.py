class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        bestPair = -1
        prev_val = values[0]

        for ind in range(1, len(values)):
            prev_val -= 1

            if values[ind] + prev_val > bestPair:
                bestPair =  values[ind] + prev_val
            
            if values[ind] > prev_val:
                prev_val = values[ind]


        return bestPair
        