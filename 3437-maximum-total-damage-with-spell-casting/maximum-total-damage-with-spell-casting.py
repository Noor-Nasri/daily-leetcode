class Solution:
    # I misread this question the first time, and didnt have much time as I was traveling
    # Reading it again, its a simple DP setup. If you take all values x, you can't take any values x+1 or x+2
    # Since we cant DP on the values, we wil need to use the indices.

    def maxDamage(self, ind):
        if ind in self.sols:
            return self.sols[ind]
        elif ind >= len(self.uniquePowers):
            return 0
        
        value = self.uniquePowers[ind]
        op1 = self.maxDamage(ind + 1)
        op2 = value * self.magicCounts[value] # + next option
        for nextInd in range(ind + 1, ind + 4):
            if nextInd < len(self.uniquePowers) and self.uniquePowers[nextInd] > value + 2:
                op2 += self.maxDamage(nextInd)
                break

        self.sols[ind] = max(op1, op2)
        return self.sols[ind]

    def maximumTotalDamage(self, power: List[int]) -> int:
        self.magicCounts = {}
        for p in power:
            self.magicCounts[p] = self.magicCounts.get(p, 0) + 1
        
        self.uniquePowers = sorted(list(self.magicCounts.keys()))
        self.sols = {}
        return self.maxDamage(0)
        