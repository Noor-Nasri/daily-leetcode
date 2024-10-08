class Solution:
    def minSwaps(self, s: str) -> int:
        seen = []
        for c in s:
            seen.append(c)

            if len(seen) >= 2 and seen[-2] == "[" and seen[-1] == "]":
                seen.pop()
                seen.pop()
        
        return math.ceil(len(seen)/4)
        
        