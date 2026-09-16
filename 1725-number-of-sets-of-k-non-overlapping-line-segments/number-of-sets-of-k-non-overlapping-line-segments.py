class Solution:
    # So we place k lines of size >= 1 across [0, n) without overlapping
    # Then we want the total number of possible options
    # Seems like a classic DP: (i, k): total ways for k lines in [i, n)
    # We avoid an inner loop by just taking all options at i+1 and adding 1 len to them

    def solve(self, i, k):
        # returns (total options from i, num that include i)
        if i >= self.n:
            return (0, 0)
        elif k == 1:
            # numOptions choices at len=1, then numOptions-1 at len=2, ... 1 option at len=numOptions
            numOptions = self.n - i - 1
            totalOptions = (numOptions + 1)/2 * numOptions
            return (totalOptions, numOptions)

        elif (i, k) in self.sols:
            return self.sols[(i, k)]
        
        totalAfterSkip, numStartAtNext = self.solve(i + 1, k)
        totalAfterTinyLine, _ = self.solve(i + 1, k - 1)
        
        # Options are skip, or take next and add len + 1 to all, or just take len=1
        totalOptions = (totalAfterSkip + numStartAtNext + totalAfterTinyLine) % (10**9 + 7)
        numIncludeThis = (totalAfterTinyLine + numStartAtNext) % (10**9 + 7)
        self.sols[(i, k)] = (totalOptions, numIncludeThis)
        return self.sols[(i, k)]

    def numberOfSets(self, n: int, k: int) -> int:
        self.sols = {}
        self.n = n
        total, _ = self.solve(0, k)
        
        return int(total)