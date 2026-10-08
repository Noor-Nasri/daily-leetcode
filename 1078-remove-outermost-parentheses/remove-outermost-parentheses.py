class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        included = []
        curOpen = 0
        for c in s:
            if c == "(":
                if curOpen:
                    included.append(c)
                curOpen += 1
            else:
                curOpen -= 1
                if curOpen:
                    included.append(c)
        
        return "".join(included)

        