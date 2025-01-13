class Solution:
    def minimumLength(self, s: str) -> int:
        counts = [0 for i in range(26)]

        for c in s:
            char = ord(c) - 97
            if counts[char] == 2: 
                counts[char] = 1
            else:
                counts[char] += 1

        return sum(counts)
        