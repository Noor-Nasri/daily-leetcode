class Solution:
    # Hold on, length 20 has > 1mil combinations to check for. Would it even fit?
    # For len=10, we would store all substrings of length 10 (at most 50000), then check against the 1024 combos
    # The real question is how to construct the hashes, which is easy: just compute the numeric value!

    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        cutoff = 2 ** k
        seen = [False for i in range(cutoff)]
        curValue = 0
        for ind in range(k):
            curValue = curValue * 2 + int(s[ind])

        seen[curValue] = True
        for ind in range(k, len(s)):
            curValue = curValue * 2 + int(s[ind])
            if s[ind - k] == '1':
                curValue -= cutoff
            
            seen[curValue] = True
        
        return all(seen)

