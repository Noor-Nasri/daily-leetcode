class Solution:
    # If we ignore 'distinct', we just do basic DP on (ind) -> {take, ignore}
    # How about: (ind) -> Tries all 26 letters by jumping to their [ind + 1] as next
    # This means [n] space, 26 options, each finding earliest ind (logn) --> nlogn
    # This should give us all options but forces no overlap since each choice is diff branch

    def smallestIndGEMin(self, inds, minVal):
        low = 0
        high = len(inds) - 1
        best = None

        while low <= high:
            mid = (low + high) // 2
            if inds[mid] >= minVal:
                best = inds[mid]
                high = mid - 1
            else:
                low = mid + 1

        return best

    def distinctSubseqII(self, s: str) -> int:
        letterInds = [[] for i in range(26)]
        n = len(s)
        for ind in range(n):
            val = ord(s[ind]) - 97    
            letterInds[val].append(ind)
        
        answerFromInd = [0 for i in range(n + 1)]
        for ind in range(n - 1, -1, -1): 
            # Build DP array backwards by just choosing next char each ind
            options = 0
            for chosenChar in range(26):
                nextInd = self.smallestIndGEMin(letterInds[chosenChar], ind)
                if nextInd == None:
                    continue
                
                # Include just the one char, or include it as a prefix to all non-empty arrays after
                options += 1 + answerFromInd[nextInd + 1]

            answerFromInd[ind] = options % (10**9 + 7)
        
        return answerFromInd[0]



