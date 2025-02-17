class Solution:
    def branchAllCombinations(self, chrList, availableOptions):
        if availableOptions.count(None) == len(availableOptions):
            self.allSequences.add("".join(chrList))
            return

        # For each index, you can either choose to include it now or never include it
        for ind in range(len(availableOptions)):
            if availableOptions[ind] == None: continue
            newChar = availableOptions[ind]

            newOptions = availableOptions[:]
            oldChrList = chrList[:]
            newChrList = chrList[:]
            newChrList.append(newChar)
            newOptions[ind] = None

            self.branchAllCombinations(oldChrList, newOptions)
            self.branchAllCombinations(newChrList, newOptions)

    def numTilePossibilities(self, tiles: str) -> int:
        self.allSequences = set()
        self.branchAllCombinations([], list(tiles))
        return len(self.allSequences) - 1
        