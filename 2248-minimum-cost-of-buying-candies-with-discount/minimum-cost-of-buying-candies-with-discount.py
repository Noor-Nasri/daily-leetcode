class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = sum(cost)
        cost = sorted(cost, reverse = True)
        for ind in range(2, len(cost), 3):
            total -= cost[ind]
        
        return total

        