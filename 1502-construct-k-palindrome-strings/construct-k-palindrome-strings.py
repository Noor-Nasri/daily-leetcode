class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counts = [0 for i in range(26)]
        for c in s:
            counts[ord(c) - 97] += 1

        longestPalindrome = 0
        addedCenter = 0

        for ind in range(26):
            if not counts[ind]:
                continue
            
            if counts[ind] % 2 == 0:
                longestPalindrome += counts[ind]
            elif not addedCenter:
                addedCenter = True
                longestPalindrome += counts[ind]
            else:
                longestPalindrome += counts[ind] - 1
        
        remainingChars = len(s) - longestPalindrome

        if remainingChars >= k:
            # We have too many single chars that make their own palindrome 
            return False
        
        extraPalindromesNeeded = k - 1 - remainingChars
        numExtraPossible = (longestPalindrome - 1) // 2 * 2
        return numExtraPossible >= extraPalindromesNeeded

        