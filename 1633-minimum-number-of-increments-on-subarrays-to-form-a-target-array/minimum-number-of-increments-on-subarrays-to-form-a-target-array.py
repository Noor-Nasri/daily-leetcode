class Solution:
    # Seems like a simple greedy: First val needs to be incremented x times. The question becomes: How much should roll over?
    # If we go to the next number, and it needs y < x, then from this point we only had y.
    # If it needs y > x, then from this point we can distribute y. 
    
    def minNumberOperations(self, target: List[int]) -> int:
        curRollover = 0
        totalSubarrs = 0
        for val in target:
            if val > curRollover:
                totalSubarrs += val - curRollover
            curRollover = val

        return totalSubarrs