class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        newStr = []
        for char in s:
            newStr.append(char)

            if len(newStr) >= len(part) and newStr[-len(part):] == part:
                del newStr[-len(part):]

        return "".join(newStr)