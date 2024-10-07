class Solution:
    def minLength(self, s: str) -> int:
        letters = []

        for c in s:
            letters.append(c)

            if len(letters) >= 2 and ((letters[-2] == "A" and letters[-1] == "B") or (letters[-2] == "C" and letters[-1] == "D")):
                letters.pop()
                letters.pop()
        
        return len(letters)