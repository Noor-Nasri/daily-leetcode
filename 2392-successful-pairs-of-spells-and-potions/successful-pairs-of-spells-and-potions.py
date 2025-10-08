class Solution:
    # For each spell we need to know the # of potions that are >= [success / spell]
    # So we can just sort the potions and use binary search
    def getIndFirstGECutoff(self, potions, cutoff):
        low = 0
        high = len(potions) - 1
        best = len(potions)

        while low <= high:
            mid = (low + high) // 2
            if potions[mid] >= cutoff:
                best = mid
                high = mid - 1
            else:
                low = mid + 1

        return best

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        combos = []
        for spell in spells:
            cutoff = success/spell
            numMatches = len(potions) - self.getIndFirstGECutoff(potions, cutoff)
            combos.append(numMatches)

        return combos

