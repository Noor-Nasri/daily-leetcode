class Solution:
    def contSplit(self, s, ind_start, seen):
        #print("Looking at", s, ind_start, seen)
        if ind_start == len(s): return True, 0

        best = 0
        for ind_end in range(ind_start, len(s)):
            substr = s[ind_start:ind_end+1]
            if substr in seen: continue

            seen_copy = {e:True for e in seen}
            seen_copy[substr] = True
            possible, res = self.contSplit(s, ind_end+1, seen_copy)

            if not possible: continue
            best = max(best, res + 1)

        #print(ind_start, seen, "results in:", best)
        if best == 0:
            return False, 0
        return True, best
    

    def maxUniqueSplit(self, s: str) -> int:
        pos, best = self.contSplit(s, 0, {})
        return best
        