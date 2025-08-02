class Solution:
    def getVarsToGiveAway(self, mainBasket, sideBasket):
        # For all vals in mainBasket, if we have more than sideBasket, give that many away
        vals = []
        for val in mainBasket:
            if mainBasket[val] > sideBasket.get(val, 0):
                diff = mainBasket[val] - sideBasket.get(val, 0)
                if diff % 2 == 1: # impossible, cuz we will never be equal by giving some away
                    return -1

                for _ in range(diff // 2):
                    vals.append(val)
        return vals

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Need to make the counts match. If 2 in one basket and not other, obv one needs to swap with other basket.
        # Should go through min vals until we get a necessary swap, then swap it with a necessary swap from the other basket with max cost
        # What if other side doesn't have any necessary swaps? That means all vals they have are equal and we'd already be done, so thats impossible if we need to swap from (1)
        # That means, when one side needs to give one element away, the other side will always either have an element to give away or its -1 (diff values)
        
        counts1 = {}
        counts2 = {}
        for ind in range(len(basket1)):
            counts1[basket1[ind]] = counts1.get(basket1[ind], 0) + 1
            counts2[basket2[ind]] = counts2.get(basket2[ind], 0) + 1
        
        vals1 =  self.getVarsToGiveAway(counts1, counts2)
        vals2 =  self.getVarsToGiveAway(counts2, counts1)

        if vals1 == -1 or vals2 == -1 or len(vals1) != len(vals2):
            return -1
        
        # The swaps are possible, and here are the necessary ones to swap
        # One option is to just take the cheapest half. But there is a trick to swap a correct one twice instead
        cheapestSwaps = sorted(vals1 + vals2)[:len(vals1)]
        alternativeCost = min(min(basket1), min(basket2)) * 2
        total = 0
        for cost in cheapestSwaps:
            total += min(cost, alternativeCost)
        return total