class Solution:
    def makeFancyString(self, s: str) -> str:
        final = []
        for c in s:
            final.append(c)
            if len(final) >= 3 and final[-1] == final[-2] == final[-3]:
                final.pop()
        return "".join(final)
        