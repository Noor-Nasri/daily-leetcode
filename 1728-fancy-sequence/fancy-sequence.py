class Fancy:
    # Given ind, we get [actionInd], which means all actions from actionInd matter
    # We need some form of prefix sums to solve val across [actionInd, cur] in O(1)

    # val = initVal * productOfMults + accumulatedBonus
    # Where accumulatedBonus comes from the increments and how much they've also been multiplied
    # accumulatedBonus = fullBonus - bonusToExclude * productOfMults
    # Meaning we track how much bonus ind0 is getting from all actions, then take out the amount
    # from the ind right before us, but we also need to scale this exclusion by all the mults since

    # How do we track modulo here .. ? The math probably just lets you modolo back if you get negative
    # Turns out we need to mult by modular inverse to make the math work. Whatver bro

    def __init__(self):
        self.initValues = []
        self.rollingValuesUntilInd = []
        self.rollingMultiplier = 1
        self.rollingBonus = 0


    def append(self, val: int) -> None:
        self.initValues.append(val)
        self.rollingValuesUntilInd.append((self.rollingMultiplier, self.rollingBonus))
        

    def addAll(self, inc: int) -> None:
        self.rollingBonus += inc
        self.rollingBonus %= 10**9 + 7
        

    def multAll(self, m: int) -> None:
        self.rollingBonus *= m
        self.rollingBonus %= 10 ** 9 + 7
        self.rollingMultiplier *= m
        self.rollingMultiplier %= 10 ** 9 + 7
        

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.initValues):
            return -1
        MOD = 10**9 + 7

        multToExclude, bonusToExclude = self.rollingValuesUntilInd[idx]
        appliedMultiplier = self.rollingMultiplier * pow(multToExclude, MOD-2, MOD) % MOD
        removalAmount = bonusToExclude * appliedMultiplier % MOD
        realBonus = (self.rollingBonus - removalAmount) % MOD
        return (self.initValues[idx] * appliedMultiplier + realBonus) % MOD


        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)