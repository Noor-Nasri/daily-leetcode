class Solution:    
    def maxProfit(self, row, col, remBullets):
        uid = (row, col, remBullets)
        if not (0 <= row < self.nrow and 0 <= col < self.ncol and remBullets >= 0):
            return float('-inf')  
        elif uid in self.sols:
            return self.sols[uid]

        bonus = self.coins[row][col]
        if row == self.nrow - 1 and col == self.ncol - 1:
            if bonus < 0 and remBullets:
                bonus = 0
            return bonus

        options = [
            bonus + self.maxProfit(row + 1, col, remBullets),
            bonus + self.maxProfit(row, col + 1, remBullets),
            max(bonus, 0) + self.maxProfit(row + 1, col, remBullets - 1),
            max(bonus, 0) + self.maxProfit(row, col + 1, remBullets - 1),
        ]

        self.sols[uid] = max(options)
        return self.sols[uid] 
        
    def maximumAmount(self, coins: List[List[int]]) -> int:
        self.sols = {}
        self.nrow, self.ncol = len(coins), len(coins[0])
        self.coins = coins
        return self.maxProfit(0, 0, 2)