class Solution:
    def isValid(self, s: str) -> bool:
        lastOpen = []
        closedMappings = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closedMappings:
                if lastOpen and closedMappings[c] == lastOpen[-1]:
                    lastOpen.pop()
                else:
                    return False
            else:
                lastOpen.append(c)

        return not lastOpen

        