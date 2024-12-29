class Solution:
    def bottomUpSolve(self):
        # Normally this would be 2D DP based on target and cutoff, then have another loop
        # But to save time, we can reduce this to a 1D DP that returns the solution to all cutoffs
        # We then optimize with rolling the sum and by building bottom up
        current = [1 for i in range(self.lenGiven + 1)]

        for indTarget in range(len(self.desired) - 1, -1, -1):
            let = self.desired[indTarget]
            numWaysByCutoff = [0 for i in range(self.lenGiven + 1)]

            for cutoff in self.givenIndices[let]:
                numWaysByCutoff[cutoff] += current[cutoff + 1] * self.givenCounts[(let, cutoff)]
                numWaysByCutoff[cutoff] %= (10**9 + 7)

            total = 0
            for cutoff in range(len(current) - 1, -1, -1):
                total += numWaysByCutoff[cutoff]
                total %= (10**9 + 7)
                current[cutoff] = total
        
        return current[0]


    def numWays(self, words: List[str], target: str) -> int:
        # Must crate target by using letters in words
        # when you use a letter, all indices <= ind become unusable 
        letterIndices = [[] for i in range(26)]
        letterCounts = {}
        self.lenGiven = len(words[0])
        for indLetter in range(len(words[0])):
            for indWord in range(len(words)):
                let = ord(words[indWord][indLetter]) - 97

                if (let, indLetter) in letterCounts:
                    letterCounts[(let, indLetter)] += 1
                else:
                    letterIndices[let].append(indLetter)
                    letterCounts[(let, indLetter)] = 1

        
        self.desired = [ord(e) - 97 for e in target]
        self.givenIndices = letterIndices
        self.givenCounts = letterCounts
        return self.bottomUpSolve()
