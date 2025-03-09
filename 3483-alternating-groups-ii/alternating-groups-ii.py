class Solution:
    def getInitialAlternating(self, colors, k):
        numAlterating = 1
        numSeen = 1
        lastIndex = 0
        curIndex = len(colors) - 1

        while numSeen < k:
            if colors[curIndex] == colors[lastIndex]:
                return numAlterating
            
            numAlterating += 1
            numSeen += 1
            lastIndex = curIndex
            curIndex -= 1
            if curIndex == -1:
                curIndex = len(colors) - 1
        
        return k
            
            

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k > len(colors): return 0

        numAlt = self.getInitialAlternating(colors, k)
        tot = 0
        if numAlt == k: tot = 1

        for i in range(1, len(colors)):
            if colors[i] != colors[i-1]:
                numAlt += 1
                if numAlt >= k:
                    tot += 1
            else:
                numAlt = 1
        
        return tot