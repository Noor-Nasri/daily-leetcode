class Solution:
    def solve(self, prices, curInd, activeTransaction, normalTransaction, kRem):
        # If we decide to BUY: Now next ind has to sell. They will return max(sell price + future profits)
        # We can determine best option without knowing the buy price, because +1 in sell price is just +1 profit
        # Same logic for SELL. Next ind has to buy. They return max(future profits - buy price)
        uid = (curInd, activeTransaction, normalTransaction, kRem)
        if uid in self.sols:
            return self.sols[uid]
        elif curInd == len(prices):
            return 0
        
        maxOption = -float('inf')
        if activeTransaction:
            # Option 1: End current transaction
            futureProfit = self.solve(prices, curInd + 1, False, False, kRem)
            curMultiplier = normalTransaction and 1 or -1
            maxOption = max(maxOption, futureProfit + curMultiplier*prices[curInd])

        elif curInd < len(prices) - 1 and kRem:
            # Option 2: Start new transaction
            maxOption = max(maxOption, self.solve(prices, curInd + 1, True, True, kRem - 1) - prices[curInd])
            maxOption = max(maxOption, self.solve(prices, curInd + 1, True, False, kRem - 1) + prices[curInd])

        # Option 3: Don't use this index
        if not(activeTransaction and curInd == len(prices) - 1):
            maxOption = max(maxOption, self.solve(prices, curInd + 1, activeTransaction, normalTransaction, kRem))

        self.sols[uid] = maxOption
        return maxOption

    def maximumProfit(self, prices: List[int], k: int) -> int:
        self.sols = {}
        ans = self.solve(prices, 0, False, False, k)
        return ans