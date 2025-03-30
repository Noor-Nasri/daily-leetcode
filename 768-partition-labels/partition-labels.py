class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterCounts = {}
        for char in s:
            if char in letterCounts:
                letterCounts[char] += 1
            else:
                letterCounts[char] = 1
        
        included = {}
        parts = []
        numChars = 0
        for char in s:
            numChars += 1
            if char in included:
                included[char] += 1
            else:
                included[char] = 1

            if included[char] == letterCounts[char]:
                del included[char]
            
            if not included:
                parts.append(numChars)
                numChars = 0

        return parts