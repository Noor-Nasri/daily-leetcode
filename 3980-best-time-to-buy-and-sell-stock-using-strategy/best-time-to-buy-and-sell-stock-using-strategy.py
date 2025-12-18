class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        profitPrefixSums = [0]
        curProfit = 0
        for day in range(len(prices)):
            curProfit += strategy[day] * prices[day]
            profitPrefixSums.append(curProfit)
        
        curSellTotal = 0
        for initWindowInd in range(k//2, k - 1):
            curSellTotal += prices[initWindowInd]

        #print("Old profit is", curProfit)
        maxBonusProfit = 0
        curWindowInd = k-1
        while curWindowInd < len(prices):
            curSellTotal += prices[curWindowInd]
            oldWindowProfit = profitPrefixSums[curWindowInd + 1] - profitPrefixSums[curWindowInd + 1 - k]
            #print("At", curWindowInd, "we would sell", curSellTotal, "instead of", oldWindowProfit)
            maxBonusProfit = max(maxBonusProfit, curSellTotal - oldWindowProfit)

            curSellTotal -= prices[curWindowInd - k//2 + 1]
            curWindowInd += 1
        
        return curProfit + maxBonusProfit
