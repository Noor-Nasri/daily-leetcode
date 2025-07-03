class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        total = 0
        middle_exists = False
        for c in counts:
            if counts[c] % 2 == 1:
                counts[c] -= 1
                middle_exists = True
            
            total += counts[c]

        return total + int(middle_exists)