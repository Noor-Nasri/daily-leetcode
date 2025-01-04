class Solution:
    def isLetterWithinRange(self, occurances, cutoffSmall, cutoffBig):
        # return True iff occurances has value > small and < big
        l = 0
        h = len(occurances) - 1

        while l <= h:
            m = (l + h)//2
            if occurances[m] <= cutoffSmall:
                l = m + 1
            elif occurances[m] >= cutoffBig:
                h = m - 1
            else:
                return True

        return False

    def countPalindromicSubsequence(self, s: str) -> int:
        # only 26^2=676 possible 3-letter palidromes
        # We can verify if a specific palindrome is possible by checking when the letters occur in s

        occurances = [[] for i in range(26)]
        for ind in range(len(s)):
            ch = ord(s[ind]) - 97
            occurances[ch].append(ind)
        
        total = 0
        for let in range(26):
            if len(occurances[let]) < 2: continue
            earliest = occurances[let][0]
            latest = occurances[let][-1]

            # for each other letter, check if is occurs within that slot
            for let2 in range(26):
                if self.isLetterWithinRange(occurances[let2], earliest, latest):
                    total += 1
        
        return total