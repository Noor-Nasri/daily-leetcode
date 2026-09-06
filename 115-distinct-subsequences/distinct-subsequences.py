class Solution:
    # Isnt this a standard DP? (ind1, ind2) -> Options are include or skip.
    # n is 1k so this should work fine. Why hard?

    def solve(self, ind1, ind2):
        if (ind1, ind2) in self.sols:
            return self.sols[(ind1, ind2)]
        elif ind2 == len(self.t):
            return 1
        elif ind1 == len(self.s):
            return 0

        total = self.solve(ind1 + 1, ind2) # Skip this
        if self.s[ind1] == self.t[ind2]:
            total += self.solve(ind1 + 1, ind2 + 1)
        
        self.sols[(ind1, ind2)] = total
        return total
        
    def numDistinct(self, s: str, t: str) -> int:
        self.sols = {}
        self.s, self.t = s, t
        return self.solve(0, 0)