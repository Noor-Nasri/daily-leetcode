class Solution:
    # Lol, after doing 4 hards to reclaim my streak, this simple one is funny.
    # This is a classic greedy, just take the cheapest bars

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        for numBars in range(len(costs)):
            coins -= costs[numBars]
            if coins < 0:
                return numBars
            
        return len(costs)     