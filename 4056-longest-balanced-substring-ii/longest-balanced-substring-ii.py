class Solution:
    # This lets us set the abc permutation we want, but can we do DP on this?
    # This is screaming BS but if we set len=n, it doesn't mean that we can/cannot find n+6
    # Is there a way to sweep for *any* subs of size >= n? Hard to do that in O(n) if we can grow and shrink

    # Okay, for the case of a + b, we can store this as (ind, diff) but this seems too big. 
    # Can we just take each chunk of ab then do something about it?

    # This would be the same as taking the full array for a+b+c. What then?
    # Can we do some prefix sum technique? For each ind, store [diff1, diff2]
    # Then at a given ind, can we do some reverse lookup for the required [diff1, diff2] seen previously?
    # Example: aabcc
    # At [0], we are at {+1, +1}. At [3], there are a=2, b=1, c=1. So we also have {+1, +1}.
    # So that means all we need is to find the earliest +1, +1, which means we simply keep it during the sweep!

    # God forgive me for this atrocity I call code ... It's a messy problem
    def singleCharSweep(self, s):
        curChar = 'z'
        curLen = 0
        maxLen = 0
        for c in s:
            if c == curChar:
                curLen += 1
            else:
                curLen = 1
                curChar = c
            maxLen = max(maxLen, curLen)

        return maxLen
    
    def twoCharSweep(self, s, char1, char2):
        maxLen = 0
        curDiff = 0
        earliestDiffOccur = {0 : -1}
        for ind in range(len(s)):
            c = s[ind]
            if c != char1 and c != char2:
                curDiff = 0
                earliestDiffOccur = {0 : ind}
                continue
            
            curDiff += (c == char1) and 1 or -1
            if curDiff in earliestDiffOccur:
                maxLen = max(maxLen, ind - earliestDiffOccur[curDiff])
            else:
                earliestDiffOccur[curDiff] = ind

        return maxLen

    def threeCharSweep(self, s):
        maxLen = 0
        diff1, diff2 = 0, 0
        earliestDiffOccur = { (0, 0) : -1}
        
        for ind in range(len(s)):
            c = s[ind]
            if c == 'a':
                diff1 += 1
                diff2 += 1
            elif c == 'b':
                diff1 -= 1
            else:
                diff2 -= 1
            
            uid = (diff1, diff2)
            if uid in earliestDiffOccur:
                maxLen = max(maxLen, ind - earliestDiffOccur[uid])
            else:
                earliestDiffOccur[uid] = ind

        return maxLen


    def longestBalanced(self, s: str) -> int:
        return max(
            self.singleCharSweep(s),
            self.twoCharSweep(s, 'a', 'b'),
            self.twoCharSweep(s, 'a', 'c'),
            self.twoCharSweep(s, 'b', 'c'),
            self.threeCharSweep(s)
        )
        