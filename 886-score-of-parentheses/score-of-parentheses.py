class Solution:
    # Seems like a basic D&C. Just split into sections, call them, and add results.
    # Worst case we only reduce the outer bracket every loop, so n^2.  Fine for n=50.

    def computeSubScore(self, s, indStart, indEnd):
        groups = []
        numOpen = 0
        groupStartInd = indStart

        for ind in range(indStart, indEnd + 1):
            if s[ind] == "(":
                numOpen += 1
            else:
                numOpen -= 1

                if not numOpen:
                    groups.append((groupStartInd, ind))
                    groupStartInd = ind + 1
        
        totalScore = 0
        for st, en in groups:
            if st + 1 == en:
                totalScore += 1
            else:
                totalScore += 2 * self.computeSubScore(s, st + 1, en - 1)
        
        return totalScore



    def scoreOfParentheses(self, s: str) -> int:
        return self.computeSubScore(s, 0, len(s) - 1)