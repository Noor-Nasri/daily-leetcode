class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [0 for i in range(26)]
        for char in word:
            counts[ord(char) - 97] += 1
        
        counts = sorted(counts, reverse = True)

        totalClicks = 0
        for i in range(26):
            totalClicks += counts[i] * (1 + i // 8)
        
        return totalClicks
        