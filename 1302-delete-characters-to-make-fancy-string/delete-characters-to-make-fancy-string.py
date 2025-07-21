class Solution:
    def makeFancyString(self, s: str) -> str:
        final = []
        for c in s:
            if len(final) >= 2 and final[-1] == final[-2] == c:
                continue
            final.append(c)
        
        return "".join(final)