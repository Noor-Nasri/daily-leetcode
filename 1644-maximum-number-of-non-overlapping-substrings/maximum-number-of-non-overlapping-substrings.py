class Solution:
    # The second condition makes this very interesting
    # The best case is 26 subarrays, one per letter.
    # I would consider binary search, but even 26C13 is 10mil options. 

    # My instinct is about graphs here. If any letter shows up in the chain of another, it is connected.
    # Then isnt the solution just the # of disconnected components?
    # Ie if you include a, you must include b, which must include c.
    # Maybe you can just include c, BUT then you cant put b in another array, so you cant put a, etc.

    # The issue: abbbccca --> a is stuck with b and c, but if you exclude a you get both b and c.
    # Can we instead do DP? At each ind, we choose to include or ignore
    # If you keep an ind, you're forced to include the full chain

    # For this to work, we would need to precompute the valid chain starts and their valid ends.
    # Okay: I think that is the solution: Precompute the jumps, then DP on which to include
    # 26 * n sweeps to compute, then DP(ind). Can optimise the DP to be 26 options and BS but its fine
    # O(n) overall. 27 total sweeps.

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        stringChars = [ord(e) - 97 for e in s]
        charCounts = [0 for i in range(26)]
        firstInd = [-1 for i in range(26)]
        n = len(s)
        for i in range(n):
            v = stringChars[i]
            charCounts[v] += 1
            if firstInd[v] == -1:
                firstInd[v] = i
        
        # Phase 1: Prepare the valid (start, end) combos.
        validSubstringInds = {} # [start] = end
        for startingChar in range(26):
            initInd = firstInd[startingChar] 
            if initInd == -1:
                continue
            
            requiredChars = {startingChar}
            remainingCount = charCounts[startingChar] - 1
            curEnd = initInd + 1

            while remainingCount and curEnd < n:
                curChar = stringChars[curEnd]
                if curChar in requiredChars:
                    remainingCount -= 1
                elif curEnd == firstInd[curChar]:
                    remainingCount += charCounts[curChar] - 1
                    requiredChars.add(curChar)
                else:
                    break # Cant include it if it predates our start
                
                curEnd += 1
            
            if not remainingCount:
                validSubstringInds[initInd] = curEnd

        # Phase 2: Use 1D DP to solve max len backwards
        # [numSubarrays, totalLen, [list of (i, j)]]
        # We can technically avoid the memory and solve at the end, but list is at most 26 so its ok
        solutions = [[0, 0, []] for i in range(n + 1)]
        for ind in range(n - 1, -1, -1):
            solutions[ind] = solutions[ind + 1]
            if ind in validSubstringInds:
                end = validSubstringInds[ind]
                numSubarrays = 1 + solutions[end][0]
                totalLength = (end - ind) + solutions[end][1]
                chosenArrays = solutions[end][2] + [[ind, end]]

                if numSubarrays > solutions[ind][0] or (numSubarrays == solutions[ind][0] and totalLength < solutions[ind][1]):
                    solutions[ind] = [numSubarrays, totalLength, chosenArrays]


        substrings = [s[i:j] for i, j in solutions[0][2]]
        return substrings