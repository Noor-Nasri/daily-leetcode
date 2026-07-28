class Solution:
    # Only 26 letters, we can put all as, then all bs, etc.
    # We know its guaranteed to have enough letters so we just do it.

    def smallestPalindrome(self, s: str) -> str:
        counts = [0 for i in range(26)]
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        final = [None for i in range(len(s))]
        curInd = 0
        for letterInd in range(26):
            letter = chr(letterInd + ord('a'))
            for i in range(counts[letterInd] // 2):
                final[curInd] = letter
                final[-curInd -1] = letter
                curInd += 1
            
            if counts[letterInd] % 2:
                final[len(s)//2] = letter

        return "".join(final) 

        