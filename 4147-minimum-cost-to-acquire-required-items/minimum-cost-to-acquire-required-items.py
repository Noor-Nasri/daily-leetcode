class Solution:
    # If costBoth < c1 + c2, just fill up until one need is met
    # Becuase if we don't, we will need to spend c1 + c2 that many times anyways. 
    # So then the rest is just that. And if its more expensive, we'd just buy individuals

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth > cost1 + cost2:
            return int(cost1 * need1 + cost2 * need2)

        numCombos = min(need1, need2)
        numRemaining = max(need1, need2) - numCombos
        if need1 > need2:
            costPerExtra = min(cost1, costBoth)
        else:
            costPerExtra = min(cost2, costBoth)
        
        return int(costBoth * numCombos + numRemaining * costPerExtra)