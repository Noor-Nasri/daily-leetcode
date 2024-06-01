class Solution:
    def sellOption(self, prices, ind, rem):
        if ind == len(prices) - 1: 
            return prices[ind] # Forced to sell
        
        if (ind, rem) in self.solsSell:
            return self.solsSell[(ind, rem)]

        option1 = self.sellOption(prices, ind + 1, rem)
        option2 = prices[ind] + self.buyOption(prices, ind + 1, rem - 1)
        
        self.solsSell[(ind, rem)] = max(option1, option2)
        return self.solsSell[(ind, rem)] 

    def buyOption(self, prices, ind, rem):
        if not rem or ind == len(prices) - 1: return 0 # Cant buy more stock
        if (ind, rem) in self.solsBuy:
            return self.solsBuy[(ind, rem)]

        option1 = self.buyOption(prices, ind + 1, rem)
        option2 = self.sellOption(prices, ind + 1, rem) - prices[ind]
        
        self.solsBuy[(ind, rem)] = max(option1, option2)
        return self.solsBuy[(ind, rem)]
    

    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.solsBuy = {}
        self.solsSell = {}
        return self.buyOption(prices, 0, k)
        